#!/usr/bin/env python3
"""市況関連ニュースの見出しをGoogleニュースRSSから収集し、_data/market_wire.json に保存する。

記事本文は保存せず、見出し・リンク・媒体名・日時・カテゴリのみを扱う。
標準ライブラリのみで動作する。cn_news の収集スクリプトと同じ方式。
"""
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

JST = timezone(timedelta(hours=9))
OUTPUT = Path(__file__).resolve().parent.parent / "_data" / "market_wire.json"
RETENTION_DAYS = 14
MAX_ITEMS = 400
TIMEOUT = 20
USER_AGENT = "Mozilla/5.0 (compatible; my-portal-news-bot)"


def google_news(query, category, hl="ja", gl="JP"):
    q = urllib.parse.quote(f"{query} when:1d")
    return {
        "name": "Google ニュース",
        "url": f"https://news.google.com/rss/search?q={q}&hl={hl}&gl={gl}&ceid={gl}:{hl}",
        "lang": hl,
        "category": category,
    }


# 1カテゴリ1クエリで検索時点で絞り込むため、追加のキーワード判定は行わない
FEEDS = [
    google_news("日経平均 OR 東証 OR 日本株", "日本"),
    google_news("NYSE OR NASDAQ OR S&P500 OR FRB OR 米国株", "米国"),
    google_news("欧州株 OR ECB OR ユーロ圏 経済", "欧州"),
    google_news("アジア株 OR 中国株 OR 香港株", "アジア"),
    google_news("ドル円 OR 為替 OR FX 市場", "為替"),
    google_news("決算 OR 株価 企業", "株・企業"),
    google_news("原油 OR 金価格 OR 商品市場", "商品"),
]

CATEGORIES = ["日本", "米国", "欧州", "アジア", "為替", "株・企業", "商品"]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as res:
        return res.read()


def parse_date(text):
    if not text:
        return None
    text = text.strip()
    try:
        dt = parsedate_to_datetime(text)  # RFC 822 (RSS 2.0)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(text.replace("Z", "+00:00"))  # ISO 8601
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(JST)


def local(tag):
    return tag.rsplit("}", 1)[-1]


def child_text(node, name):
    for c in node:
        if local(c.tag) == name and c.text:
            return c.text.strip()
    return ""


def is_http(url):
    return urllib.parse.urlparse(url).scheme in ("http", "https")


def parse_feed(feed):
    root = ET.fromstring(fetch(feed["url"]))
    items = []
    for node in root.iter():
        if local(node.tag) not in ("item", "entry"):
            continue
        title = child_text(node, "title")
        link = child_text(node, "link")
        if not link:  # Atom は href 属性
            for c in node:
                if local(c.tag) == "link" and c.get("href"):
                    link = c.get("href")
                    break
        published = parse_date(child_text(node, "pubDate") or child_text(node, "date")
                               or child_text(node, "published") or child_text(node, "updated"))
        # Google ニュースの見出しは「タイトル - 媒体名」形式
        source = child_text(node, "source") or feed["name"]
        suffix = f" - {source}"
        if title.endswith(suffix):
            title = title[: -len(suffix)]
        if not (title and link and published and is_http(link)):
            continue
        items.append({
            "title": re.sub(r"\s+", " ", title),
            "url": link,
            "source": source,
            "lang": feed["lang"],
            "category": feed["category"],
            "published": published.isoformat(timespec="seconds"),
        })
    return items


def load_existing():
    try:
        return json.loads(OUTPUT.read_text(encoding="utf-8")).get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def main():
    collected = []
    failed = 0
    for feed in FEEDS:
        try:
            got = parse_feed(feed)
            print(f"ok   {len(got):3d}  {feed['category']}  {feed['url'][:70]}")
            collected.extend(got)
        except Exception as e:  # 1つのフィードの失敗で全体を止めない
            failed += 1
            print(f"FAIL      {feed['category']}  {feed['url'][:70]}  ({e})", file=sys.stderr)

    if failed == len(FEEDS):
        sys.exit("all feeds failed; keeping existing data")

    cutoff = datetime.now(JST) - timedelta(days=RETENTION_DAYS)
    seen_urls, seen_titles, merged = set(), set(), []
    # 新規取得分を優先し、続けて既存データを重複除外しながら統合する
    for item in collected + load_existing():
        title_key = re.sub(r"\W+", "", item["title"]).lower()
        if item["url"] in seen_urls or title_key in seen_titles:
            continue
        if datetime.fromisoformat(item["published"]) < cutoff:
            continue
        seen_urls.add(item["url"])
        seen_titles.add(title_key)
        merged.append(item)

    merged.sort(key=lambda i: i["published"], reverse=True)
    merged = merged[:MAX_ITEMS]

    if merged == load_existing():
        print("no new items; data unchanged")
        return

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {"updated": datetime.now(JST).isoformat(timespec="seconds"), "items": merged}
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"saved {len(merged)} items -> {OUTPUT}")


if __name__ == "__main__":
    main()
