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
    1. 全ページを取得し、管理用ファイルを除外
    2. date（日付）が Front Matter に設定されているものだけを抽出
  {% endcomment %}
  {% assign all_pages = site.pages | where_exp: "item", "item.path != 'index.md'" | where_exp: "item", "item.path != 'README.md'" %}
  {% assign dated_pages = all_pages | where: "date" %}

  {% comment %} 
    3. 設定された日付順（date）で並び替え、reverseで最新を一番上にする
  {% endcomment %}
  {% assign sorted_pages = dated_pages | sort: "date" | reverse %}

  {% for page in sorted_pages limit:10 %}
    <li>
      {% assign parts = page.path | split: "/" %}
      {% comment %} カテゴリタグ表示 {% endcomment %}
      <span style="font-size: 0.7em; color: #aaa; border: 1px solid #555; padding: 2px 5px; border-radius: 3px; margin-right: 8px; text-transform: uppercase; font-weight: bold;">
        {{ parts[0] }}
      </span>

      <a href="{{ page.url | relative_url }}">
        {{ page.title | default: page.name }}
      </a>

      {% comment %} 記事の日付を表示 {% endcomment %}
      <small style="color: #666; margin-left: 10px;">
        ({{ page.date | date: "%Y/%m/%d" }})
      </small>
    </li>
  {% endfor %}
</ul>

---

© 2026 shunchama. Built with GitHub Pages.
