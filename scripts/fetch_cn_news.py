#!/usr/bin/env python3
"""中国関連ニュースをRSSから収集し、_data/cn_news.json に保存する。

記事本文は保存せず、見出し・リンク・媒体名・日時のみを扱う。
標準ライブラリのみで動作する。
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
OUTPUT = Path(__file__).resolve().parent.parent / "_data" / "cn_news.json"
RETENTION_DAYS = 14
MAX_ITEMS = 400
TIMEOUT = 20
USER_AGENT = "Mozilla/5.0 (compatible; my-portal-news-bot)"


def google_news(query, hint=None):
    q = urllib.parse.quote(f"{query} when:2d")
    return {
        "name": "Google ニュース",
        "url": f"https://news.google.com/rss/search?q={q}&hl=ja&gl=JP&ceid=JP:ja",
        "lang": "ja",
        "filter": False,  # 検索クエリで絞り込み済み
        "hint": hint,
        "google": True,
    }


# filter=True のフィードは、見出しに中国関連キーワードを含むものだけ採用する
FEEDS = [
    google_news("中国 -中国地方 -中国電力 -中国銀行", None),
    google_news("中国 外交 OR 習近平 OR 共産党", "政治・外交"),
    google_news("中国 経済 OR 景気 OR 不動産 OR 輸出", "経済"),
    google_news("中国 軍 OR 海警 OR 尖閣 OR 空母", "軍事・安全保障"),
    google_news("台湾 OR 香港 中国", "台湾・香港"),
    {"name": "NHK", "url": "https://www3.nhk.or.jp/rss/news/cat6.xml", "lang": "ja", "filter": True},
    {"name": "Yahoo!ニュース", "url": "https://news.yahoo.co.jp/rss/topics/world.xml", "lang": "ja", "filter": True},
    {"name": "BBC News (China)", "url": "https://feeds.bbci.co.uk/news/world/asia/china/rss.xml", "lang": "en", "filter": False},
    {"name": "SCMP", "url": "https://www.scmp.com/rss/4/feed", "lang": "en", "filter": False},
]

CHINA_RE = re.compile(
    r"中国|中共|習近平|北京|上海市|香港|台湾|尖閣|南シナ海|人民解放軍|"
    r"China|Chinese|Beijing|Xi Jinping|Hong Kong|Taiwan|\bPLA\b",
    re.IGNORECASE,
)

# 上から順に判定し、最初に一致したカテゴリを採用する
CATEGORY_RULES = [
    ("台湾・香港", re.compile(r"台湾|香港|Taiwan|Hong Kong", re.IGNORECASE)),
    ("軍事・安全保障", re.compile(
        r"軍|防衛|ミサイル|空母|海警|尖閣|南シナ海|領海|演習|核兵器|核実験|"
        r"military|navy|missile|warship|coast guard|defen[cs]e|\bPLA\b", re.IGNORECASE)),
    ("経済", re.compile(
        r"経済|景気|不動産|株価|人民元|関税|輸出|輸入|貿易|GDP|半導体|\bEV\b|投資|企業|"
        r"econom|trade|tariff|yuan|property|export|chip|stock|market", re.IGNORECASE)),
    ("政治・外交", re.compile(
        r"外交|首脳|会談|習近平|共産党|政府|大使|制裁|"
        r"diplomat|Xi Jinping|Communist Party|sanction|summit|ambassador", re.IGNORECASE)),
]
DEFAULT_CATEGORY = "社会・その他"


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
            dt = datetime.fromisoformat(text.replace("Z", "+00:00"))  # ISO 8601 (RSS 1.0)
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


def classify(title, hint):
    for category, pattern in CATEGORY_RULES:
        if pattern.search(title):
            return category
    return hint or DEFAULT_CATEGORY


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
        source = feed["name"]
        if feed.get("google"):
            # Google ニュースの見出しは「タイトル - 媒体名」形式
            source = child_text(node, "source") or source
            suffix = f" - {source}"
            if title.endswith(suffix):
                title = title[: -len(suffix)]
        if not (title and link and published and is_http(link)):
            continue
        if feed.get("filter") and not CHINA_RE.search(title):
            continue
        items.append({
            "title": re.sub(r"\s+", " ", title),
            "url": link,
            "source": source,
            "lang": feed["lang"],
            "category": classify(title, feed.get("hint")),
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
            print(f"ok   {len(got):3d}  {feed['name']}  {feed['url'][:70]}")
            collected.extend(got)
        except Exception as e:  # 1つのフィードの失敗で全体を止めない
            failed += 1
            print(f"FAIL      {feed['name']}  {feed['url'][:70]}  ({e})", file=sys.stderr)

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
