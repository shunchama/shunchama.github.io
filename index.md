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
  {% comment %} 全ページの中から、特定のディレクトリに含まれる md ファイルを取得 {% endcomment %}
  {% assign all_pages = site.pages | where_exp: "item", "item.path contains 'investment/report/'" | where_exp: "item", "item.name != 'index.md'" %}
  
  {% comment %} 並び替えの基準となる日付データがないため、ファイル名で逆順（新しい順）に並び替え {% endcomment %}
  {% assign sorted_pages = all_pages | sort: "path" | reverse %}

{% for page in sorted_pages limit:5 %}
<li>
{% comment %} ファイル名から日付らしき部分（20260217）を抽出して整形（任意） {% endcomment %}
{% assign date_part = page.name | slice: 0, 8 %}
{{ date_part | slice: 0, 4 }}-{{ date_part | slice: 4, 2 }}-{{ date_part | slice: 6, 2 }}:
<a href="{{ page.url | relative_url }}">{{ page.title | default: page.name }}</a>
</li>
{% endfor %}

</ul>

© 2026 shunchama. Built with GitHub Pages.
