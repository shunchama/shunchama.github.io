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
    1. すべてのページ(site.pages)を対象にする
    2. htmlまたはmdファイルのみを抽出
    3. 管理用のindex.mdやREADME、assetsフォルダ等を除外
  {% endcomment %}
  
  {% assign all_docs = site.pages | where_exp: "item", "item.name != 'index.md'" | where_exp: "item", "item.path != 'README.md'" | where_exp: "item", "item.path != '404.html'" %}

  {% comment %} 
    ファイル名やパスでソート。
    中国(cn/)の記事が出てこない場合、パスのアルファベット順で後ろになっている可能性があるため、
    「最後に更新された順」にしたい場合は、日付順のファイル名にするのが一番確実です。
  {% endcomment %}
  {% assign sorted_docs = all_docs | sort: "path" | reverse %}

  {% for doc in sorted_docs limit:15 %}
    <li>
      {% assign parts = doc.path | split: "/" %}
      {% comment %} フォルダ名を表示（例: [CN] [INVESTMENT]） {% endcomment %}
      <span style="font-size: 0.75em; color: #aaa; border: 1px solid #555; padding: 1px 3px; border-radius: 3px; margin-right: 8px; text-transform: uppercase;">
        {{ parts[0] }}
      </span>

      <a href="{{ doc.url | relative_url }}">
        {{ doc.title | default: doc.name }}
      </a>
    </li>
  {% endfor %}
</ul>

---

© 2026 shunchama. Built with GitHub Pages.
