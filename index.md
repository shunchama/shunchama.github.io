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
    全ファイルをスキャンし、index.mdや管理ファイル、READMEを除外
  {% endcomment %}
  {% assign all_pages = site.html_pages | where_exp: "item", "item.name != 'index.md'" | where_exp: "item", "item.path != 'README.md'" | where_exp: "item", "item.dir != '/assets/'" %}

  {% comment %} 
    ファイルパスでソートし、最新順（reverse）にする
  {% endcomment %}
  {% assign sorted_pages = all_pages | sort: "path" | reverse %}

  {% for page in sorted_pages limit:10 %}
    <li>
      {% assign path_parts = page.path | split: "/" %}
      {% comment %} フォルダ名からカテゴリタグを生成 {% endcomment %}
      <span style="font-size: 0.8em; color: #888; border: 1px solid #444; padding: 1px 4px; border-radius: 3px; margin-right: 5px;">
        {{ path_parts[0] | upcase }}
      </span>
      <a href="{{ page.url | relative_url }}">
        {{ page.title | default: page.name }}
      </a>
      {% if page.path contains 'report' %}
        {% comment %} レポートファイルの場合はファイル名から日付を表示 {% endcomment %}
        <small style="color: #666; margin-left: 10px;">({{ page.name | slice: 0, 8 }})</small>
      {% endif %}
    </li>
  {% endfor %}
</ul>

---

© 2026 shunchama. Built with GitHub Pages.
