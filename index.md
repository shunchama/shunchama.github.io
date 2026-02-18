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
  {% comment %} 1. 全ページを取得し、管理ファイルを除外 {% endcomment %}
  {% assign all_pages = site.pages | where_exp: "item", "item.path != 'index.md'" | where_exp: "item", "item.path != 'README.md'" %}
  
  {% comment %} 2. 日付が設定されているページを一旦抽出 {% endcomment %}
  {% assign raw_dated_pages = all_pages | where_exp: "item", "item.date" %}

{% comment %} 3. 【最重要】比較エラー（Array vs Array）を防ぐためのガード
dateが配列になっているものを除外し、安全なリストを再構築します
{% endcomment %}
{% assign valid_pages = "" | split: "" %}
{% for p in raw_dated_pages %}
{% comment %}
Jekyllでは、配列に対して .size を使うと要素数が返りますが、
単一の日付データに対して .size を使うと nil になります。これを利用して選別します。
{% endcomment %}
{% if p.date.size == nil %}
{% assign valid_pages = valid_pages | push: p %}
{% endif %}
{% endfor %}

{% comment %} 4. ガードを通過した安全なページのみをソート {% endcomment %}
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

## </ul>

© 2026 shunchama. Built with GitHub Pages.
