import feedparser
from typing import List, Dict

def fetch_rss_articles(feed_urls: List[str], limit: int = 20) -> List[Dict]:
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": getattr(entry, "summary", ""),
                "published": getattr(entry, "published", ""),
                "source": url
            })
    return articles

if __name__ == "__main__":
    FEEDS = [
        "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "https://cryptonews.net/en/news/feed/",
        "https://blockchain.news/rss"
    ]
    articles = fetch_rss_articles(FEEDS, limit=5)
    for a in articles:
        print(f"[{a['published']}] {a['title']}\n{a['link']}\n---")
