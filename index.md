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
    1. 全ページを取得し、管理ファイルを除外
  {% endcomment %}
  {% assign all_pages = site.pages | where_exp: "item", "item.path != 'index.md'" | where_exp: "item", "item.path != 'README.md'" %}
  
  {% comment %} 
    2. dateが設定されているものだけを抽出
  {% endcomment %}
  {% assign dated_pages = all_pages | where_exp: "item", "item.date" %}

  {% comment %} 
    3. 比較エラーを防ぐため、dateが配列になっているものを除外（重要！）
  {% endcomment %}
  {% assign valid_pages = "" | split: "" %}
  {% for p in dated_pages %}
    {% comment %} date.sizeがnilなら単一の値（日付/文字列）、sizeがあれば配列 {% endcomment %}
    {% if p.date.size == nil %}
      {% assign valid_pages = valid_pages | push: p %}
    {% endif %}
  {% endfor %}

  {% comment %} 4. 安全になったリストを日付順でソートして逆順にする {% endcomment %}
  {% assign sorted_pages = valid_pages | sort: "date" | reverse %}

  {% for page in sorted_pages limit:10 %}
    <li style="margin-bottom: 8px;">
      {% assign parts = page.path | split: "/" %}
      <span style="font-size: 0.7em; color: #aaa; border: 1px solid #555; padding: 2px 5px; border-radius: 3px; margin-right: 8px; text-transform: uppercase; font-weight: bold; display: inline-block; min-width: 80px; text-align: center;">
        {{ parts[0] }}
      </span>
      <a href="{{ page.url | relative_url }}" style="font-weight: bold;">
        {{ page.title | default: page.name }}
      </a>
      <span style="color: #666; margin-left: 10px; font-size: 0.9em;">
        ({{ page.date | date: "%Y/%m/%d" }})
      </span>
    </li>
  {% endfor %}
</ul> 

---

© 2026 shunchama. Built with GitHub Pages.
