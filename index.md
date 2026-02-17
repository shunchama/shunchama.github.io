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
    1. 全ページを取得
    2. 管理用ファイルやHOME自身を除外
  {% endcomment %}
  {% assign all_pages = site.pages | where_exp: "item", "item.path != 'index.md'" | where_exp: "item", "item.path != 'README.md'" %}

{% comment %} 3. ファイル名の先頭が「2」（2026年など）で始まるものだけに絞り込む
※これで「index.md」などの日付なしファイルが自動的に弾かれます
{% endcomment %}
{% assign dated_pages = all_pages | where_exp: "item", "item.name slugify | slice: 0 == '2'" %}

{% comment %} 4. パスでソートして最新順に表示
{% endcomment %}
{% assign sorted_pages = dated_pages | sort: "path" | reverse %}

{% for page in sorted_pages limit:10 %}
<li>
{% assign parts = page.path | split: "/" %}
{% comment %} カテゴリタグ [INVESTMENT] [CN] 等を表示 {% endcomment %}
<span style="font-size: 0.7em; color: #aaa; border: 1px solid #555; padding: 2px 5px; border-radius: 3px; margin-right: 8px; text-transform: uppercase; font-weight: bold;">
{{ parts[0] }}
</span>

      <a href="{{ page.url | relative_url }}">
        {{ page.title | default: page.name }}
      </a>

      {% comment %} 日付部分をファイル名から抽出して表示 (例: 20260217 -> 2026/02/17) {% endcomment %}
      <small style="color: #666; margin-left: 10px;">
        {% assign d = page.name | slice: 0, 8 %}
        {{ d | slice: 0, 4 }}/{{ d | slice: 4, 2 }}/{{ d | slice: 6, 2 }}
      </small>
    </li>

{% endfor %}

</ul>

---

© 2026 shunchama. Built with GitHub Pages.
