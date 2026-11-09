---
layout: default
title: Home
nav_order: 1
---

{%- comment -%}
  ホーム画面。見た目は _includes/home_style.html にまとめています。
  カテゴリを増やすときは下の「カテゴリ」セクションにカードを1枚足し、
  cat_labels / cat_keys にも同じキーを追加してください。
{%- endcomment -%}
{%- include home_style.html -%}
{%- assign cat_keys = "investment,geo,prog,statistics,cn,variety,terms" | split: "," -%}
{%- assign cat_labels = "投資,地理,プログラム,統計,中国,ツール,用語" | split: "," -%}
{%- assign dated_pages = site.pages | where_exp: "item", "item.date" -%}
{%- assign sorted_pages = dated_pages | sort: "date" | reverse -%}
{%- assign latest = sorted_pages | first -%}

<div class="hp">

<section class="hp-hero">
  <p class="hp-eyebrow">shunchama's portal</p>
  <h1 class="hp-title">好きなことを、<span class="hp-grad">調べて、まとめる。</span></h1>
  <p class="hp-lead">投資・地理・プログラミング・中国など、趣味で調べたことを置いている個人サイトです。</p>
  <ul class="hp-stats">
    <li><b>{{ dated_pages.size }}</b>記事</li>
    <li><b>{{ cat_keys.size }}</b>カテゴリ</li>
    <li>最終更新 <b>{{ latest.date | date: "%Y/%m/%d" }}</b></li>
  </ul>
</section>

<h2 class="hp-h2">ヘッドライン <small>自動更新</small></h2>
<div class="hp-news">
  <div class="hp-panel">
    <div class="hp-panel-head">
      <span><span class="hp-live"></span>マーケット速報</span>
      <a href="{{ '/investment/dashboard/market_wire.html' | relative_url }}">すべて見る →</a>
    </div>
    <ul>
      {%- for item in site.data.market_wire.items limit:5 %}
      <li>
        <a href="{{ item.url }}" target="_blank" rel="noopener">{{ item.title }}</a>
        <span class="hp-meta"><span class="hp-tag">{{ item.category }}</span>{{ item.source }} · {{ item.published | date: "%m/%d %H:%M" }}</span>
      </li>
      {%- endfor %}
    </ul>
  </div>
  <div class="hp-panel">
    <div class="hp-panel-head">
      <span><span class="hp-live"></span>中国ニュース</span>
      <a href="{{ '/cn/news.html' | relative_url }}">すべて見る →</a>
    </div>
    <ul>
      {%- for item in site.data.cn_news.items limit:5 %}
      <li>
        <a href="{{ item.url }}" target="_blank" rel="noopener">{{ item.title }}</a>
        <span class="hp-meta"><span class="hp-tag">{{ item.category }}</span>{{ item.source }} · {{ item.published | date: "%m/%d %H:%M" }}</span>
      </li>
      {%- endfor %}
    </ul>
  </div>
</div>

<h2 class="hp-h2">カテゴリ</h2>
<div class="hp-cards">
  <a class="hp-card c-investment" href="{{ '/investment/' | relative_url }}">
    <span class="hp-ico">📈</span>
    <span class="hp-name">投資情報</span>
    <span class="hp-desc">日々の市場の振り返りとダッシュボード</span>
    <span class="hp-sub"><span>市場レポート</span><span>Market Wire</span><span>レンディング</span></span>
  </a>
  <a class="hp-card c-geo" href="{{ '/geo/' | relative_url }}">
    <span class="hp-ico">🌏</span>
    <span class="hp-name">地理</span>
    <span class="hp-desc">国旗・地図クイズや各国データの比較</span>
    <span class="hp-sub"><span>国旗ゲーム</span><span>地図クイズ</span></span>
  </a>
  <a class="hp-card c-prog" href="{{ '/prog/' | relative_url }}">
    <span class="hp-ico">💻</span>
    <span class="hp-name">プログラミング</span>
    <span class="hp-desc">アルゴリズムと言語リファレンスのメモ</span>
    <span class="hp-sub"><span>ソート</span><span>C</span><span>Java</span></span>
  </a>
  <a class="hp-card c-statistics" href="{{ '/statistics/' | relative_url }}">
    <span class="hp-ico">📊</span>
    <span class="hp-name">統計</span>
    <span class="hp-desc">金融工学など数理まわりのまとめ</span>
    <span class="hp-sub"><span>金融工学</span></span>
  </a>
  <a class="hp-card c-cn" href="{{ '/cn/' | relative_url }}">
    <span class="hp-ico">🏮</span>
    <span class="hp-name">中国</span>
    <span class="hp-desc">ニュースとネット事情・歴史の調べもの</span>
    <span class="hp-sub"><span>ニュース</span><span>ネット規制</span></span>
  </a>
  <a class="hp-card c-variety" href="{{ '/variety/' | relative_url }}">
    <span class="hp-ico">🧰</span>
    <span class="hp-name">便利ウェブツール</span>
    <span class="hp-desc">ちょっとした計算をブラウザで</span>
    <span class="hp-sub"><span>電気料金計算機</span></span>
  </a>
  <a class="hp-card c-terms" href="{{ '/terms/' | relative_url }}">
    <span class="hp-ico">📖</span>
    <span class="hp-name">調べた用語</span>
    <span class="hp-desc">気になって調べた言葉の小さな辞書</span>
  </a>
</div>

<h2 class="hp-h2">最新の記事 <small>新しい順に15件</small></h2>
<ul class="hp-list">
  {%- for p in sorted_pages limit:15 %}
  {%- assign key = p.path | split: "/" | first -%}
  {%- assign label = key -%}
  {%- for k in cat_keys -%}
    {%- if k == key -%}{%- assign label = cat_labels[forloop.index0] -%}{%- endif -%}
  {%- endfor %}
  <li>
    <span class="hp-badge c-{{ key }}">{{ label }}</span>
    <a href="{{ p.url | relative_url }}">{{ p.title | default: p.name }}</a>
    <time datetime="{{ p.date | date_to_xmlschema }}">{{ p.date | date: "%Y/%m/%d" }}</time>
  </li>
  {%- endfor %}
</ul>

<footer class="hp-foot">
  <span>2026-02-08 サイト開設</span>
  <span>© 2026 shunchama · Built with GitHub Pages</span>
</footer>

</div>
