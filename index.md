---
layout: default
title: Home
nav_order: 1
---

# HOME

## カテゴリ一覧

- [投資情報](./investment/)
  - [今日の市場の振り返り](./investment/report/)
- [プログラミング](./prog/)
- [中国(閲覧注意)](./cn/)
- [地理](./geo/)
- [統計](./statistics/)
- [ブログ(準備中)](#)

---

## 最新の記事・更新

- 2026-02-08: サイトを開設しました。

---

<ul>
  {% comment %} 
    1. 日付が設定されているページを抽出
    2. 文字列として日付をソートし、新しい順（reverse）に並べる
  {% endcomment %}
  {% assign dated_pages = site.pages | where_exp: "item", "item.date" %}
  {% assign sorted_pages = dated_pages | sort: "date" | reverse %}

  {% for page in sorted_pages limit:15 %}
    {% if page.path != "index.md" and page.path != "README.md" %}
      <li style="margin-bottom: 8px;">
        {% assign parts = page.path | split: "/" %}
        
        <span style="font-size: 0.7em; color: #aaa; border: 1px solid #555; padding: 2px 5px; border-radius: 3px; margin-right: 8px; text-transform: uppercase; font-weight: bold; display: inline-block; min-width: 60px; text-align: center;">
          {{ parts[0] | default: "ETC" }}
        </span>

        <a href="{{ page.url | relative_url }}" style="font-weight: bold;">
          {{ page.title | default: page.name }}
        </a>

        <span style="color: #666; margin-left: 10px; font-size: 0.9em;">
          ({{ page.date | date: "%Y/%m/%d" }})
        </span>
      </li>
    {% endif %}
  {% endfor %}
</ul>

---

© 2026 shunchama. Built with GitHub Pages.
