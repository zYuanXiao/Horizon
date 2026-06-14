from __future__ import annotations

import asyncio
from datetime import datetime, timezone

import httpx

from src.models import GitHubTrendingConfig, SourceType
from src.scrapers.github_trending import GitHubTrendingScraper


def test_github_trending_filters_and_parses_repos() -> None:
    html = """
    <html><body>
      <article class="Box-row">
        <h2><a href="/LMCache/LMCache">LMCache / LMCache</a></h2>
        <p>Supercharge your LLM inference with the fastest KV Cache layer.</p>
        <span itemprop="programmingLanguage">Python</span>
        <a href="/LMCache/LMCache/stargazers">8,988</a>
        <a href="/LMCache/LMCache/forks">612</a>
        <span>238 stars today</span>
      </article>
      <article class="Box-row">
        <h2><a href="/example/noise">example / noise</a></h2>
        <p>Unrelated project.</p>
        <span>2 stars today</span>
      </article>
    </body></html>
    """

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/trending/python"
        assert request.url.params["since"] == "daily"
        return httpx.Response(200, text=html)

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    scraper = GitHubTrendingScraper(
        GitHubTrendingConfig(
            enabled=True,
            languages=["python"],
            keywords=["kv cache"],
            min_stars_today=10,
        ),
        client,
    )

    items = asyncio.run(scraper.fetch(datetime.now(timezone.utc)))
    asyncio.run(client.aclose())

    assert len(items) == 1
    item = items[0]
    assert item.source_type == SourceType.GITHUB_TRENDING
    assert item.title == "LMCache/LMCache (+238 stars today)"
    assert str(item.url) == "https://github.com/LMCache/LMCache"
    assert item.metadata["stars_today"] == 238
    assert item.metadata["source_name"] == "GitHub Trending"
