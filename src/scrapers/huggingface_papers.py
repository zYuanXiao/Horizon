"""Hugging Face daily papers scraper."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from .base import BaseScraper
from ..models import ContentItem, HuggingFacePapersConfig, SourceType

logger = logging.getLogger(__name__)


class HuggingFacePapersScraper(BaseScraper):
    """Fetch papers from Hugging Face Daily Papers."""

    API_URL = "https://huggingface.co/api/daily_papers"

    def __init__(
        self,
        config: HuggingFacePapersConfig,
        http_client: httpx.AsyncClient,
    ):
        super().__init__({"huggingface_papers": config}, http_client)
        self.cfg = config
        self._keywords_lower = [kw.lower() for kw in self.cfg.keywords if kw]

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch latest daily papers and apply local filters."""
        if not self.cfg.enabled:
            return []

        try:
            response = await self.client.get(
                self.API_URL,
                headers={
                    "User-Agent": "Horizon/1.0",
                    "Accept": "application/json",
                },
                follow_redirects=True,
                timeout=20.0,
            )
            response.raise_for_status()
            rows = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            logger.warning("Hugging Face daily papers request failed: %s", exc)
            return []

        items: List[ContentItem] = []
        for row in rows:
            item = self._row_to_item(row)
            if item is None:
                continue
            if item.metadata.get("upvotes", 0) < self.cfg.min_upvotes:
                continue
            if self._keywords_lower and not self._matches_keywords(row):
                continue
            items.append(item)

        items.sort(key=lambda item: item.metadata.get("upvotes", 0), reverse=True)
        return items[: self.cfg.max_items]

    def _row_to_item(self, row: dict) -> Optional[ContentItem]:
        paper = row.get("paper") or {}
        paper_id = paper.get("id") or row.get("paperId")
        if not paper_id:
            return None

        title = paper.get("title") or row.get("title") or "Untitled paper"
        summary = (
            paper.get("ai_summary")
            or row.get("summary")
            or paper.get("summary")
            or ""
        )
        full_summary = paper.get("summary") or row.get("summary") or summary
        keywords = paper.get("ai_keywords") or []
        upvotes = int(paper.get("upvotes") or row.get("upvotes") or 0)
        submitted = self._parse_datetime(
            paper.get("submittedOnDailyAt") or row.get("publishedAt")
        )
        authors = [
            author.get("name")
            for author in (paper.get("authors") or [])
            if author.get("name")
        ]

        content_parts = [
            summary,
            full_summary if full_summary != summary else "",
            f"AI keywords: {', '.join(keywords)}" if keywords else "",
            f"Authors: {', '.join(authors[:8])}" if authors else "",
        ]

        return ContentItem(
            id=self._generate_id("huggingface_papers", "paper", str(paper_id)),
            source_type=SourceType.HUGGINGFACE_PAPERS,
            title=title,
            url=f"https://huggingface.co/papers/{paper_id}",
            content="\n\n".join(part for part in content_parts if part),
            author="Hugging Face Papers",
            published_at=submitted or datetime.now(timezone.utc),
            metadata={
                "paper_id": paper_id,
                "upvotes": upvotes,
                "authors": authors,
                "ai_keywords": keywords,
                "submitted_on_daily_at": (
                    submitted.isoformat() if submitted else None
                ),
                "category": "research-papers",
                "source_name": "Hugging Face Papers",
            },
        )

    def _matches_keywords(self, row: dict) -> bool:
        paper = row.get("paper") or {}
        keywords = paper.get("ai_keywords") or []
        haystack = " ".join(
            [
                str(paper.get("title") or row.get("title") or ""),
                str(paper.get("summary") or row.get("summary") or ""),
                str(paper.get("ai_summary") or ""),
                " ".join(str(keyword) for keyword in keywords),
            ]
        ).lower()
        return any(keyword in haystack for keyword in self._keywords_lower)

    @staticmethod
    def _parse_datetime(value: Optional[str]) -> Optional[datetime]:
        if not value:
            return None
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
