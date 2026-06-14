from __future__ import annotations

import asyncio
from datetime import datetime, timezone

import httpx

from src.models import HuggingFacePapersConfig, SourceType
from src.scrapers.huggingface_papers import HuggingFacePapersScraper


def test_huggingface_papers_filters_and_parses_daily_papers() -> None:
    payload = [
        {
            "paper": {
                "id": "2606.12345",
                "title": "A VLM Agent for Visual Reasoning in Games",
                "summary": "We train a vision-language model agent with RLVR.",
                "ai_summary": "A VLM game-playing agent improves visual reasoning.",
                "ai_keywords": ["VLM", "visual reasoning", "RLVR"],
                "upvotes": 42,
                "submittedOnDailyAt": "2026-06-12T00:00:00.000Z",
                "authors": [{"name": "Ada Lovelace"}],
            }
        },
        {
            "paper": {
                "id": "2606.00001",
                "title": "Unrelated Biology Paper",
                "summary": "Cells and proteins.",
                "ai_keywords": ["biology"],
                "upvotes": 100,
                "submittedOnDailyAt": "2026-06-12T00:00:00.000Z",
            }
        },
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/daily_papers"
        return httpx.Response(200, json=payload)

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    scraper = HuggingFacePapersScraper(
        HuggingFacePapersConfig(enabled=True, keywords=["rlvr"], min_upvotes=1),
        client,
    )

    items = asyncio.run(scraper.fetch(datetime.now(timezone.utc)))
    asyncio.run(client.aclose())

    assert len(items) == 1
    item = items[0]
    assert item.source_type == SourceType.HUGGINGFACE_PAPERS
    assert item.title == "A VLM Agent for Visual Reasoning in Games"
    assert str(item.url) == "https://huggingface.co/papers/2606.12345"
    assert item.metadata["upvotes"] == 42
    assert item.metadata["source_name"] == "Hugging Face Papers"
    assert "Ada Lovelace" in item.content
