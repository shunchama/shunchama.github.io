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
    1. サイト内の全ページを取得
    2. READMEや404、HOME(一番上のindex.md)を除外
    3. カテゴリのトップページ(nav_orderが設定されていないindex.mdなど)は除外したいが、
       中国の記事のように「タイトルがある重要なindex.md」は含めるように調整
  {% endcomment %}
  
  {% assign all_pages = site.pages | where_exp: "item", "item.path != 'index.md'" | where_exp: "item", "item.path != 'README.md'" | where_exp: "item", "item.path != '404.html'" %}

{% comment %}
path（フォルダ名含むフルパス）でソートして逆順に。
これで cn/ や investment/ の中身が混ざって出てきます。
{% endcomment %}
{% assign sorted_pages = all_pages | sort: "path" | reverse %}

{% for page in sorted_pages limit:15 %}
<li>
{% assign parts = page.path | split: "/" %}
{% comment %}
カテゴリタグの表示。
[CN] [INVESTMENT] など、一番上のフォルダ名を表示。
{% endcomment %}
<span style="font-size: 0.7em; color: #aaa; border: 1px solid #555; padding: 2px 5px; border-radius: 3px; margin-right: 8px; text-transform: uppercase; font-weight: bold;">
{{ parts[0] }}
</span>

      <a href="{{ page.url | relative_url }}">
        {{ page.title | default: page.name }}
      </a>

      {% comment %} 階層が深い場合に、少しヒントを出す（任意） {% endcomment %}
      {% if parts.size > 2 %}
        <small style="color: #666; margin-left: 5px;">in {{ parts[1] }}</small>
      {% endif %}
    </li>

{% endfor %}

</ul>

---

© 2026 shunchama. Built with GitHub Pages.
