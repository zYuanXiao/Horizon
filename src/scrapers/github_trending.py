"""GitHub Trending scraper."""

from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from typing import List, Optional
from urllib.parse import quote

import httpx
from bs4 import BeautifulSoup

from .base import BaseScraper
from ..models import ContentItem, GitHubTrendingConfig, SourceType

logger = logging.getLogger(__name__)


class GitHubTrendingScraper(BaseScraper):
    """Scrape repositories from GitHub Trending."""

    BASE_URL = "https://github.com/trending"

    def __init__(self, config: GitHubTrendingConfig, http_client: httpx.AsyncClient):
        super().__init__({"github_trending": config}, http_client)
        self.cfg = config
        self._keywords_lower = [kw.lower() for kw in self.cfg.keywords if kw]

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch trending repositories across configured languages."""
        if not self.cfg.enabled:
            return []

        items: List[ContentItem] = []
        seen_ids: set[str] = set()
        for language in self.cfg.languages:
            rows = await self._fetch_language(language)
            for row in rows:
                if row["id"] in seen_ids:
                    continue
                if row["stars_today"] < self.cfg.min_stars_today:
                    continue
                if self._keywords_lower and not self._matches_keywords(row):
                    continue
                seen_ids.add(row["id"])
                items.append(self._row_to_item(row))

        items.sort(key=lambda item: item.metadata.get("stars_today", 0), reverse=True)
        return items[: self.cfg.max_items]

    async def _fetch_language(self, language: str) -> List[dict]:
        lang_path = f"/{quote(language)}" if language else ""
        url = f"{self.BASE_URL}{lang_path}"
        try:
            response = await self.client.get(
                url,
                params={"since": self.cfg.since},
                headers={
                    "User-Agent": "Mozilla/5.0 Horizon/1.0",
                    "Accept": "text/html,application/xhtml+xml",
                },
                follow_redirects=True,
                timeout=20.0,
            )
            response.raise_for_status()
        except httpx.HTTPError as exc:
            logger.warning("GitHub Trending request failed for %s: %s", language, exc)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        rows = []
        for article in soup.select("article.Box-row"):
            row = self._parse_article(article, language)
            if row:
                rows.append(row)
        return rows

    def _parse_article(self, article, requested_language: str) -> Optional[dict]:
        link = article.select_one("h2 a")
        if not link or not link.get("href"):
            return None

        repo = link.get("href", "").strip("/")
        if "/" not in repo:
            return None

        description_node = article.select_one("p")
        description = (
            description_node.get_text(" ", strip=True) if description_node else ""
        )
        language_node = article.select_one("[itemprop=programmingLanguage]")
        primary_language = (
            language_node.get_text(strip=True) if language_node else requested_language
        )
        stars_node = article.select_one('a[href$="/stargazers"]')
        forks_node = article.select_one('a[href$="/forks"]')
        stars_today_text = article.find(string=lambda s: s and "stars today" in s)

        return {
            "id": repo,
            "repo": repo,
            "url": f"https://github.com/{repo}",
            "description": description,
            "primary_language": primary_language or "Unknown",
            "stars": self._parse_int(stars_node.get_text(strip=True) if stars_node else ""),
            "forks": self._parse_int(forks_node.get_text(strip=True) if forks_node else ""),
            "stars_today": self._parse_int(str(stars_today_text or "")),
            "requested_language": requested_language or "All",
        }

    def _row_to_item(self, row: dict) -> ContentItem:
        repo = row["repo"]
        stars_today = row["stars_today"]
        title = f"{repo} (+{stars_today} stars today)"
        content = "\n".join(
            [
                f"GitHub Trending repository: {repo}",
                f"Stars today: {stars_today}",
                f"Total stars: {row['stars']}",
                f"Forks: {row['forks']}",
                f"Language: {row['primary_language']}",
                "",
                row["description"],
            ]
        ).strip()

        return ContentItem(
            id=self._generate_id("github_trending", "repo", repo),
            source_type=SourceType.GITHUB_TRENDING,
            title=title,
            url=row["url"],
            content=content,
            author=repo.split("/")[0],
            published_at=datetime.now(timezone.utc),
            metadata={
                "repo": repo,
                "stars_today": stars_today,
                "stars": row["stars"],
                "forks": row["forks"],
                "primary_language": row["primary_language"],
                "period": self.cfg.since,
                "category": "open-source-tools",
                "source_name": "GitHub Trending",
            },
        )

    def _matches_keywords(self, row: dict) -> bool:
        haystack = " ".join(
            [
                row.get("repo", ""),
                row.get("description", ""),
                row.get("primary_language", ""),
            ]
        ).lower()
        return any(keyword in haystack for keyword in self._keywords_lower)

    @staticmethod
    def _parse_int(value: str) -> int:
        match = re.search(r"[\d,]+", value or "")
        if not match:
            return 0
        return int(match.group(0).replace(",", ""))
