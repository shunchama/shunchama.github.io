---
layout: default
title: 投資ダッシュボード
parent: 投資情報
nav_order: 3
has_children: true
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans+JP:wght@400;500;600&family=Barlow+Condensed:wght@500;600;700&display=swap">
<style>
/* Layout: launcher — big live clock header, then one tall tile per tool, each showing a live preview of what it holds */
:root{
  --bg:#0b0d10; --panel:#12161b; --panel2:#161b21; --line:#232a32; --fg:#d9dee4; --dim:#6b7682;
  --amber:#ffb238; --up:#3ddc84; --down:#ff5c5c; --pre:#5fa8ff;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  --sans:"IBM Plex Sans JP","Hiragino Sans","Noto Sans JP",system-ui,sans-serif;
  --cond:"Barlow Condensed","Arial Narrow",sans-serif;
}
#dashboard-root{box-sizing:border-box;background:var(--bg);color:var(--fg);font-family:var(--sans);font-variant-numeric:tabular-nums;padding:16px;margin:16px -16px}
#dashboard-root *{box-sizing:border-box}
#dashboard-root .wrap{max-width:1040px;margin:0 auto;display:flex;flex-direction:column;gap:24px}
#dashboard-root .brand{font-family:var(--cond);font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:14px;color:var(--amber);display:flex;align-items:center;gap:8px}
#dashboard-root .dot{width:8px;height:8px;border-radius:50%;background:var(--amber);animation:db-blink 1s steps(2) infinite}
@keyframes db-blink{50%{opacity:.2}}
@media (prefers-reduced-motion:reduce){#dashboard-root .dot{animation:none}}
#dashboard-root .lbl{font-family:var(--cond);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
#dashboard-root header{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px;border-bottom:1px solid var(--line);padding-bottom:18px}
#dashboard-root .big{font-family:var(--mono);font-size:clamp(44px,11vw,88px);font-weight:500;line-height:1;letter-spacing:-.03em;margin-top:10px}
#dashboard-root .big small{font-size:.4em;color:var(--dim)}
#dashboard-root .date{font-family:var(--mono);font-size:13px;color:var(--dim);margin-top:8px}
#dashboard-root .sess{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
#dashboard-root .s{font-family:var(--cond);font-weight:700;font-size:12px;letter-spacing:.12em;padding:3px 9px;border:1px solid var(--line);color:var(--dim)}
#dashboard-root .s.on{color:var(--up);border-color:var(--up)}

#dashboard-root .tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
#dashboard-root a.tile{display:flex;flex-direction:column;gap:14px;background:var(--panel);border:1px solid var(--line);padding:18px;color:inherit;text-decoration:none;min-width:0;transition:border-color .15s,background .15s}
#dashboard-root a.tile:hover{border-color:var(--amber);background:var(--panel2)}
#dashboard-root a.tile:focus-visible{outline:2px solid var(--amber);outline-offset:3px}
#dashboard-root .t-head{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
#dashboard-root .t-name{font-family:var(--cond);font-weight:700;font-size:26px;letter-spacing:.04em;text-transform:uppercase}
#dashboard-root .t-go{font-family:var(--mono);font-size:13px;color:var(--amber)}
#dashboard-root .t-desc{font-size:13px;color:var(--dim);line-height:1.7}
#dashboard-root .peek{border-top:1px solid var(--line);padding-top:12px;margin-top:auto;display:flex;flex-direction:column;gap:8px;min-height:96px}
#dashboard-root .row{display:flex;justify-content:space-between;gap:10px;font-family:var(--mono);font-size:14px}
#dashboard-root .row span:first-child{font-family:var(--cond);letter-spacing:.1em;text-transform:uppercase;color:var(--dim);font-size:13px}
#dashboard-root .cd{font-family:var(--mono);font-size:28px;font-weight:500;letter-spacing:-.02em}
#dashboard-root .ev{font-size:13px;line-height:1.5}
#dashboard-root .ev2{font-size:12px;color:var(--dim);font-family:var(--mono)}
#dashboard-root .wire{display:flex;flex-direction:column;gap:6px;font-size:13px}
#dashboard-root .wire div{display:flex;gap:10px}
#dashboard-root .wire b{font-family:var(--mono);font-weight:500;color:var(--amber);min-width:44px}
#dashboard-root footer{font-size:11px;color:var(--dim);line-height:1.7}
</style>

<div id="dashboard-root">
<div class="wrap">
  <header>
    <div>
      <div class="brand"><i class="dot"></i>Trading Desk</div>
      <div class="big" id="db-jst">--:--<small>:--</small></div>
      <div class="date" id="db-date">JST</div>
    </div>
    <div>
      <div class="lbl" style="text-align:right;margin-bottom:6px">Stock markets now</div>
      <div class="sess" id="db-sess"></div>
    </div>
  </header>

  <nav class="tiles" aria-label="ツール">
    <a class="tile" href="./market_clock.html">
      <div class="t-head"><span class="t-name">Market Clock</span><span class="t-go">OPEN →</span></div>
      <div class="t-desc">世界12取引所の現地時刻と開場状況、FXセッションの24時間タイムライン。</div>
      <div class="peek" id="db-pClock"></div>
    </a>
    <a class="tile" href="./event_countdown.html">
      <div class="t-head"><span class="t-name">Event Countdown</span><span class="t-go">OPEN →</span></div>
      <div class="t-desc">米CPI・FOMC・日銀・東京CPI・短観など主要指標の発表カウントダウンと過去の結果。</div>
      <div class="peek"><span class="lbl">Next</span><span class="cd" id="db-pCd">--:--:--</span><span class="ev" id="db-pEv"></span><span class="ev2" id="db-pEv2"></span></div>
    </a>
    <a class="tile" href="./market_wire.html">
      <div class="t-head"><span class="t-name">Market Wire</span><span class="t-go">OPEN →</span></div>
      <div class="t-desc">日米欧・為替・株・商品の主要ニュースの見出しを自動収集。カテゴリ別に一覧表示。</div>
      <div class="peek">
        <span class="lbl">Auto update · JST</span>
        <div class="wire"><div><b>6時台</b>日中4回、RSSから見出しを自動収集</div></div>
        <span class="ev2" id="db-pNext"></span>
      </div>
    </a>
  </nav>

  <footer>イベント一覧は 2026年10月14日時点の日程です。</footer>
</div>
</div>

<script>
(function(){
const p2=n=>String(n).padStart(2,"0");
const fmts={};
function parts(tz,d){const f=fmts[tz]||(fmts[tz]=new Intl.DateTimeFormat("en-US",{timeZone:tz,hourCycle:"h23",hour:"2-digit",minute:"2-digit",second:"2-digit",weekday:"short",month:"2-digit",day:"2-digit",year:"numeric"}));
  const o={};for(const p of f.formatToParts(d))o[p.type]=p.value;return {h:+o.hour,m:+o.minute,s:+o.second,wd:o.weekday,y:o.year,mo:o.month,d:o.day};}
const MK=[
  {n:"Tokyo",tz:"Asia/Tokyo",s:[[540,690],[750,930]]},
  {n:"Hong Kong",tz:"Asia/Hong_Kong",s:[[570,720],[780,960]]},
  {n:"London",tz:"Europe/London",s:[[480,990]]},
  {n:"Frankfurt",tz:"Europe/Berlin",s:[[540,1050]]},
  {n:"New York",tz:"America/New_York",s:[[570,960]]}
];
const CLOCKS=[["Tokyo","Asia/Tokyo"],["London","Europe/London"],["New York","America/New_York"]];
const EV=[
  ["米CPI（9月分）","2026-10-14T12:30:00Z"],["全国CPI（9月分）","2026-10-22T23:30:00Z"],["FOMC 政策金利発表","2026-10-28T18:00:00Z"],
  ["ECB 政策金利発表","2026-10-29T13:15:00Z"],["東京都区部CPI（10月）","2026-10-29T23:30:00Z"],["日銀 決定会合 結果","2026-10-30T02:00:00Z"],
  ["米雇用統計（10月分）","2026-11-06T13:30:00Z"],["米CPI（10月分）","2026-11-10T13:30:00Z"],["GDP 1次速報（7-9月期）","2026-11-15T23:50:00Z"],
  ["全国CPI（10月分）","2026-11-19T23:30:00Z"],["東京都区部CPI（11月）","2026-11-26T23:30:00Z"],["米雇用統計（11月分）","2026-12-04T13:30:00Z"],
  ["FOMC 政策金利発表","2026-12-09T19:00:00Z"],["米CPI（11月分）","2026-12-10T13:30:00Z"],["日銀短観（12月）","2026-12-13T23:50:00Z"],
  ["ECB 政策金利発表","2026-12-17T13:15:00Z"],["日銀 決定会合 結果","2026-12-18T02:00:00Z"]
].map(([n,t])=>({n,ms:Date.parse(t)}));
const WIRE=[[6,49],[11,49],[16,49],[21,49]];
const DOW=["日","月","火","水","木","金","土"];

function tick(){
  const now=new Date(), j=parts("Asia/Tokyo",now);
  document.getElementById("db-jst").innerHTML=`${p2(j.h)}:${p2(j.m)}<small>:${p2(j.s)}</small>`;
  document.getElementById("db-date").textContent=`${j.y}-${j.mo}-${j.d} ${j.wd.toUpperCase()} · JST`;

  document.getElementById("db-sess").innerHTML=MK.map(m=>{const p=parts(m.tz,now),mins=p.h*60+p.m,wk=!["Sat","Sun"].includes(p.wd);
    const on=wk&&m.s.some(([a,b])=>mins>=a&&mins<b);return `<span class="s${on?" on":""}">${m.n}</span>`}).join("");

  document.getElementById("db-pClock").innerHTML=CLOCKS.map(([n,tz])=>{const p=parts(tz,now);return `<div class="row"><span>${n}</span><span>${p2(p.h)}:${p2(p.m)}:${p2(p.s)}</span></div>`}).join("");

  const t=now.getTime(), live=EV.find(e=>t>=e.ms&&t-e.ms<900e3), nx=live||EV.find(e=>e.ms>t);
  if(nx){
    let s=Math.abs(Math.floor((nx.ms-t)/1000));const d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60;
    document.getElementById("db-pCd").textContent=(live?"LIVE +":"")+(d?d+"d ":"")+`${p2(h)}:${p2(m)}:${p2(x)}`;
    document.getElementById("db-pCd").style.color=live?"var(--up)":(nx.ms-t<3600e3?"var(--amber)":"");
    document.getElementById("db-pEv").textContent=nx.n;
    const jt=new Date(nx.ms+9*3600e3);
    document.getElementById("db-pEv2").textContent=`${jt.getUTCMonth()+1}/${jt.getUTCDate()}(${DOW[jt.getUTCDay()]}) ${p2(jt.getUTCHours())}:${p2(jt.getUTCMinutes())} JST`;
  }else{document.getElementById("db-pCd").textContent="--:--:--";document.getElementById("db-pEv").textContent="登録済みの予定はありません";document.getElementById("db-pEv2").textContent="";}

  const jm=j.h*60+j.m, nxt=WIRE.find(([h,m])=>h*60+m>jm)||WIRE[0];
  document.getElementById("db-pNext").textContent=`次の更新 ${p2(nxt[0])}:${p2(nxt[1])} JST`;
}
tick();setInterval(tick,1000);
})();
</script>
