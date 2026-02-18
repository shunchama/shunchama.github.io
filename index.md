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
    複雑なソートは使わず、investment/report フォルダ内のファイルを
    名前順（20260218...）で表示するだけの最もシンプルな方法です
  {% endcomment %}
  {% assign reports = site.pages | where_exp: "item", "item.path contains 'investment/report/'" | where_exp: "item", "item.path != 'investment/report/index.md'" %}

  {% for page in reports limit:10 %}
    <li style="margin-bottom: 8px;">
      <span style="font-size: 0.7em; color: #aaa; border: 1px solid #555; padding: 2px 5px; border-radius: 3px; margin-right: 8px; text-transform: uppercase; font-weight: bold; display: inline-block;">
        REPORT
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
