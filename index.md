---
layout: default
title: Home
nav_order: 1
---

{%- comment -%}
  ホーム画面。見た目は _includes/home_style.html にまとめています。
  カテゴリを増やすときは「メニュー」の表に1行足し、
  cat_keys / cat_labels にも同じキーを追加してください。
{%- endcomment -%}
{%- include home_style.html -%}
{%- assign cat_keys = "investment,geo,prog,statistics,cn,variety,terms" | split: "," -%}
{%- assign cat_labels = "投資,地理,プログラミング,統計,中国,ツール,用語" | split: "," -%}
{%- assign dated_pages = site.pages | where_exp: "item", "item.date" -%}
{%- assign sorted_pages = dated_pages | sort: "date" | reverse -%}

<div class="hp">

<h1>{{ site.title }}</h1>

<div class="hp-box">
  <p>{{ site.description }}。</p>
  <p class="hp-small">開設日：2026/02/08　／　記事数：{{ dated_pages.size }}</p>
</div>

<h2 class="hp-bar">更新履歴</h2>
<ul class="hp-log">
  {%- for p in sorted_pages limit:15 %}
  {%- assign key = p.path | split: "/" | first -%}
  {%- assign label = key -%}
  {%- for k in cat_keys -%}
    {%- if k == key -%}{%- assign label = cat_labels[forloop.index0] -%}{%- endif -%}
  {%- endfor %}
  <li><span class="hp-date">{{ p.date | date: "%Y/%m/%d" }}</span><span class="hp-cat">[{{ label }}]</span><a href="{{ p.url | relative_url }}">{{ p.title | default: p.name }}</a></li>
  {%- endfor %}
  <li><span class="hp-date">2026/02/08</span>サイトを開設しました。</li>
</ul>

<h2 class="hp-bar">メニュー</h2>
<table class="hp-table">
  <tr><th><a href="{{ '/investment/' | relative_url }}">投資情報</a></th><td class="hp-sub"><a href="{{ '/investment/report/' | relative_url }}">市場の振り返り</a>、ダッシュボード、レンディング</td></tr>
  <tr><th><a href="{{ '/geo/' | relative_url }}">地理</a></th><td class="hp-sub">国旗・地図クイズ、各国データ</td></tr>
  <tr><th><a href="{{ '/prog/' | relative_url }}">プログラミング</a></th><td class="hp-sub">アルゴリズム、C / Java リファレンス</td></tr>
  <tr><th><a href="{{ '/statistics/' | relative_url }}">統計</a></th><td class="hp-sub">金融工学</td></tr>
  <tr><th><a href="{{ '/cn/' | relative_url }}">中国</a></th><td class="hp-sub"><a href="{{ '/cn/news.html' | relative_url }}">ニュース</a>、ネット事情、歴史</td></tr>
  <tr><th><a href="{{ '/variety/' | relative_url }}">便利ウェブツール</a></th><td class="hp-sub">電気料金計算機</td></tr>
  <tr><th><a href="{{ '/terms/' | relative_url }}">調べた用語</a></th><td class="hp-sub">気になって調べた言葉</td></tr>
</table>

<h2 class="hp-bar">ニュース（自動更新）</h2>
<p><b>■ マーケット</b></p>
<ul class="hp-news">
  {%- for item in site.data.market_wire.items limit:5 %}
  <li><a href="{{ item.url }}" target="_blank" rel="noopener">{{ item.title }}</a> <span class="hp-small">（{{ item.source }} {{ item.published | date: "%m/%d %H:%M" }}）</span></li>
  {%- endfor %}
</ul>
<p class="hp-more"><a href="{{ '/investment/dashboard/market_wire.html' | relative_url }}">&gt;&gt; もっと見る</a></p>
<p><b>■ 中国</b></p>
<ul class="hp-news">
  {%- for item in site.data.cn_news.items limit:5 %}
  <li><a href="{{ item.url }}" target="_blank" rel="noopener">{{ item.title }}</a> <span class="hp-small">（{{ item.source }} {{ item.published | date: "%m/%d %H:%M" }}）</span></li>
  {%- endfor %}
</ul>
<p class="hp-more"><a href="{{ '/cn/news.html' | relative_url }}">&gt;&gt; もっと見る</a></p>

<div class="hp-foot">
  <p>Copyright &copy; 2026 shunchama. All rights reserved.<br>Built with GitHub Pages.</p>
</div>

</div>
