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
    1. site.html_pages（HTML/MDファイル）から、除外したいページを弾く
    2. path で並び替えて reverse（最新順）にする
  {% endcomment %}
  
  {% assign all_items = site.html_pages | where_exp: "item", "item.name != 'index.md'" | where_exp: "item", "item.path != 'README.md'" | where_exp: "item", "item.path != '404.html'" %}
  
  {% assign sorted_items = all_items | sort: "path" | reverse %}

  {% for item in sorted_items limit:8 %}
    <li>
      {% comment %} 
        カテゴリ名（親フォルダ名）を表示して、どこが更新されたか分かりやすくする
      {% endcomment %}
      {% assign path_parts = item.path | split: "/" %}
      <small>[{{ path_parts[0] | upcase }}]</small> 
      <a href="{{ item.url | relative_url }}">{{ item.title | default: item.name }}</a>
    </li>
  {% endfor %}
</ul>

© 2026 shunchama. Built with GitHub Pages.
