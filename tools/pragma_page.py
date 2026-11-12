"""Hyper Pragma product page: a demonstration of the product, not a description of it.

Umar, 12 Nov 2026: the page shows Pragma working, the way a platform page shows its
product in motion, and every demonstration is drawn in Pragma's own design system
(tokens from Hyper Desktop's renderer stylesheet: violet #5200ff, base #f8f7fb, Space
Grotesk, Inter, JetBrains Mono, radii 6/10/14/20). The content is real: the fleet,
its rules and the run replayed below come from Pragma on CodeNinja's own machine (the
Mining GOLD Copper demo tenant, synthetic records), and the memory panel is the
Self-Improving Memory loop's own output (~/pragma-memory, export_demo.py writes
hyper-pragma/demo.json). Never names a competitor; never says "world's first".

    python tools/pragma_page.py      (product_pages.py calls build() for hyper-pragma)
"""
from __future__ import annotations

import datetime as dt
import html
import json
from pathlib import Path

import brand

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
MARK = "M15.6261 0H28.0897L18.3451 11.4995H24.6264L24.6265 11.4994H37.09L21.4126 30.0001H9.00037L22.5148 13.9996H16.2265L12.4123 18.5007H0L15.6261 0Z"

PCSS = """
.pw{--pf-d:'Space Grotesk',system-ui,sans-serif;--pf-t:'Inter',system-ui,sans-serif;--pf-m:'JetBrains Mono',ui-monospace,monospace;
--p-bg:#f8f7fb;--p-sf:#fff;--p-sk:#efedf5;--p-hv:rgba(33,27,44,.05);--p-ac2:rgba(33,27,44,.09);--p-ln:rgba(33,27,44,.1);--p-ln2:rgba(33,27,44,.19);
--p-ink:#211b2c;--p-ink2:#5d5176;--p-mu:#8c82a3;--p-ac:#5200ff;--p-acs:rgba(82,0,255,.09);--p-ok:#0f8a5f;--p-oks:rgba(15,138,95,.12);--p-wa:#b0740f;--p-bad:#e7000b;
font:400 13px/1.45 var(--pf-t);color:var(--p-ink);background:var(--p-bg);border-radius:14px;border:1px solid rgba(33,27,44,.14);
box-shadow:0 16px 40px rgba(33,20,66,.16),0 4px 10px rgba(33,20,66,.07);overflow:hidden;text-align:left;-webkit-font-smoothing:antialiased}
.pw .bar{height:30px;display:flex;align-items:center;gap:7px;padding:0 12px;border-bottom:1px solid var(--p-ln);background:var(--p-bg)}
.pw .bar i{width:10px;height:10px;border-radius:50%;background:#dcd8e6}.pw .bar span{margin-left:8px;font:500 10px var(--pf-t);letter-spacing:.06em;color:var(--p-mu)}
.pw .app{display:grid;grid-template-columns:200px 1fr;min-height:420px;padding:6px}
.pw .sd{background:var(--p-sf);border:1px solid var(--p-ln);border-radius:16px;padding:8px 6px;display:flex;flex-direction:column;gap:1px}
.pw .sd a{display:flex;align-items:center;gap:8px;padding:5px 8px;border-radius:6px;color:var(--p-ink);font-size:12px;text-decoration:none}
.pw .sd a.on{background:var(--p-ac2)}.pw .sd a.nw{color:var(--p-ac);font-weight:500}.pw .sd a svg{width:13px;height:13px;stroke:currentColor;fill:none;stroke-width:1.7;flex:none}
.pw .sd .lb{font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--p-mu);padding:10px 8px 3px}
.pw .sd .s{justify-content:space-between}.pw .sd .s b{font-weight:400;display:flex;align-items:center;gap:8px}.pw .sd .s b::before{content:"";width:5px;height:5px;border-radius:50%;background:var(--p-ac)}
.pw .sd .s small{font-size:10px;color:var(--p-mu)}
.pw .mn{padding:22px 24px;overflow:hidden;position:relative}
.pw h4{font:600 16px/1.2 var(--pf-d);letter-spacing:-.01em;margin:0 0 3px;color:var(--p-ink)}.pw .sub{color:var(--p-ink2);font-size:11.5px;margin:0 0 14px}
.pw .hd{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.pw .bt{display:inline-flex;align-items:center;height:26px;padding:0 11px;border-radius:8px;border:1px solid var(--p-ln2);background:var(--p-sf);font:500 11.5px var(--pf-t);color:var(--p-ink);white-space:nowrap}
.pw .bt.pr{background:var(--p-ac);border-color:var(--p-ac);color:#fff}.pw .bt.gh{border-color:rgba(82,0,255,.35);color:var(--p-ac);height:22px;font-size:10.5px;border-radius:6px;padding:0 8px}
.pw .bt.dg{border-color:rgba(231,0,11,.35);color:var(--p-bad);height:22px;font-size:10.5px;border-radius:6px;padding:0 8px}
.pw .tk{background:var(--p-sf);border:1px solid var(--p-ln);border-radius:10px;padding:8px 12px;display:grid;grid-template-columns:1fr auto 34px;gap:2px 14px;align-items:center;margin-bottom:6px;transition:border-color .3s,box-shadow .3s}
.pw .tk .n{font:500 11.5px var(--pf-m);display:flex;align-items:center;gap:7px}.pw .tk .d{grid-column:1;color:var(--p-ink2);font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pw .tk .w{grid-row:1/3;grid-column:2;text-align:right;font-size:11px;color:var(--p-ink2)}.pw .tk .w em{display:block;font-style:normal;color:var(--p-mu);font-size:10.5px}
.pw .tk .sw{grid-row:1/3;grid-column:3;width:28px;height:16px;border-radius:99px;background:var(--p-ac);position:relative}.pw .tk .sw::after{content:"";position:absolute;right:2px;top:2px;width:12px;height:12px;border-radius:50%;background:#fff}
.pw .tk.run{border-color:rgba(82,0,255,.55);box-shadow:0 0 0 1px rgba(82,0,255,.3)}
.pw .pill{display:inline-flex;align-items:center;height:16px;padding:0 6px;border-radius:99px;font:500 9.5px var(--pf-t);background:var(--p-acs);color:var(--p-ac)}
.pw .pill.ok{background:var(--p-oks);color:var(--p-ok)}
.pw .ch{max-width:560px;margin:0 auto;display:flex;flex-direction:column;gap:6px;height:388px;overflow:hidden;scroll-behavior:smooth;padding-bottom:4px}
.pw .ch .u{align-self:flex-end;background:var(--p-sk);border-radius:12px;padding:7px 11px;font-size:11.5px;max-width:80%}
.pw .ch .a{font-size:12px;line-height:1.55;color:var(--p-ink)}
.pw .ch .c{display:flex;align-items:center;gap:8px;border:1px solid var(--p-ln);background:rgba(82,0,255,.04);border-radius:8px;padding:5px 9px;font:500 10.5px var(--pf-m);color:var(--p-ink2)}
.pw .ch .c::before{content:"";width:11px;height:11px;border-radius:50%;border:1.5px solid var(--p-ac);border-right-color:transparent;animation:pwspin .7s linear infinite;flex:none}
.pw .ch .c.dn::before{animation:none;border:0;background:var(--p-ok) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='m3 6 2 2 4-4' stroke='white' stroke-width='1.6' fill='none'/%3E%3C/svg%3E") center/11px no-repeat}
.pw .ch .c q{quotes:none;color:var(--p-mu);font-weight:400}
.pw .ch .wo{border:1px solid var(--p-ln);border-radius:10px;background:var(--p-sf);padding:9px 12px;display:grid;grid-template-columns:auto 1fr auto;gap:2px 10px;align-items:center;font-size:11.5px}
.pw .ch .wo b{font:600 11.5px var(--pf-m)}.pw .ch .wo span{color:var(--p-ink2)}
.pw .ch > *{animation:pwin .35s cubic-bezier(.16,1,.3,1)}@keyframes pwin{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}@keyframes pwspin{to{transform:rotate(360deg)}}
.pw .cp{max-width:560px;margin:8px auto 0;border:1px solid var(--p-ln);border-radius:16px;background:var(--p-sf);padding:9px 12px;color:var(--p-mu);font-size:11.5px}
.pw .cd{background:var(--p-sf);border:1px solid var(--p-ln);border-radius:10px;padding:11px 13px;margin-top:9px}.pw .cd h5{margin:0 0 4px;font:600 11.5px var(--pf-t)}
.pw .mt{color:var(--p-mu);font-size:10.5px}.pw .st{display:flex;gap:16px;align-items:center;font-size:11px;color:var(--p-ink2)}.pw .st .ok{color:var(--p-ok);font-weight:500}.pw .st b{color:var(--p-ink);font-weight:500}
.pw .sc{font-weight:600}.pw .sc.strong,.pw .sc.good{color:var(--p-ok)}.pw .sc.weak{color:var(--p-wa)}.pw .sc.failed{color:var(--p-bad)}
.pw .sp{display:flex;align-items:flex-end;gap:3px;height:46px;margin-top:9px}.pw .sp i{flex:1;border-radius:2px 2px 0 0;transform-origin:bottom;transform:scaleY(0);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.pw.live .sp i{transform:scaleY(1)}.pw .sp i.p{background:var(--p-ok)}.pw .sp i.z{background:var(--p-wa)}.pw .sp i.n{background:var(--p-bad)}
.pw .ls{border:1px solid var(--p-ln);border-radius:9px;padding:8px 10px;margin-top:7px;opacity:0;transform:translateY(5px);transition:all .45s cubic-bezier(.16,1,.3,1)}.pw.live .ls{opacity:1;transform:none}
.pw .ls p{margin:0 0 6px;font-size:11.5px;line-height:1.5}.pw .ls .f{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--p-mu)}
.pw .dl{position:absolute;inset:0;background:rgba(23,16,37,.42);display:flex;align-items:center;justify-content:center;padding:18px}
.pw .dg2{background:var(--p-sf);border-radius:14px;box-shadow:0 16px 40px rgba(33,20,66,.2);width:min(470px,100%);padding:16px 18px;font-size:11.5px}
.pw .dg2 .k{font:400 9.5px var(--pf-m);color:var(--p-mu)}.pw .dg2 h5{font:600 14px var(--pf-d);margin:3px 0}.pw .dg2 p{color:var(--p-ink2);margin:0 0 10px;font-size:11px}
.pw .dg2 h6{font:600 10.5px var(--pf-t);margin:10px 0 5px}.pw .fl{border:1px solid var(--p-ln);border-radius:8px;padding:6px 9px;display:flex;justify-content:space-between}.pw .fl code{font:400 10.5px var(--pf-m)}
.pw .tc{display:grid;grid-template-columns:1fr 1fr;gap:6px}.pw .op{border:1px solid var(--p-ln);border-radius:8px;padding:6px 9px;font-size:10.5px;color:var(--p-mu)}.pw .op b{display:block;color:var(--p-ink);font-weight:500}
.pw .op.on{border-color:var(--p-ac);box-shadow:0 0 0 1px var(--p-ac);background:var(--p-acs)}.pw .op.on b{color:var(--p-ac)}
.pw .su{background:var(--p-sk);border-radius:8px;padding:8px 10px;margin-top:10px;font-size:10.5px;color:var(--p-ink2)}.pw .su b{color:var(--p-ink);display:block;margin-bottom:2px}
.pw .ft{display:flex;justify-content:flex-end;gap:6px;margin-top:11px}
.pw .ob{display:grid;grid-template-columns:1fr 1fr;gap:6px}.pw .ob div{border:1px solid var(--p-ln);border-radius:8px;background:var(--p-sf);padding:6px 9px;font:500 11px var(--pf-m)}.pw .ob div small{display:block;font:400 10px var(--pf-t);color:var(--p-mu)}
.pw .rl{margin-top:10px;display:flex;flex-direction:column;gap:5px}.pw .rl div{border-left:2px solid var(--p-ac);background:var(--p-sf);padding:5px 9px;font-size:11px;border-radius:0 6px 6px 0}
@media (max-width:820px){.pw .app{grid-template-columns:1fr}.pw .sd{display:none}.pw .mn{padding:16px 14px}.pw .ch{height:360px}}
"""

PAGE_CSS = """
body{background:#f4f4f2}main.pg{background:#f4f4f2;color:var(--ink)}
.pg .wrap2{max-width:1240px;margin:0 auto;padding:0 var(--gutter)}
.pwall{position:relative;overflow:hidden;height:100vh;min-height:640px;max-height:1100px;background:#0b0c10;color:#fff}
.pwall .wv{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.pwall .wg{position:absolute;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(4,1fr)}
.pwall .wc{position:relative;border:1px solid rgba(0,0,0,.35);transition:box-shadow .4s,background .4s}
.pwall .wc:nth-child(4n+1) .op,.pwall .wc:nth-child(4n+1) .chip{left:calc(12px + var(--cx,0px))}.pwall .wc .op{position:absolute;left:12px;bottom:10px;font:500 10px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.82);text-shadow:0 1px 6px rgba(0,0,0,.7)}
.pwall .wc .chip{position:absolute;left:12px;top:12px;display:inline-flex;align-items:center;gap:7px;padding:6px 10px;border-radius:99px;background:rgba(12,9,22,.74);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);font:500 11px var(--mono);color:#fff;opacity:0;transform:translateY(-5px);transition:opacity .35s,transform .35s}
.pwall .wc .chip::before{content:"";width:7px;height:7px;border-radius:50%;background:#a98bff}
.pwall .wc.on{box-shadow:inset 0 0 0 2px #7d5cff;background:rgba(82,0,255,.12)}.pwall .wc.on .chip{opacity:1;transform:none}
.pwall .wc.g .chip::before{background:#2bd98f}.pwall .wc.l .chip::before{background:#ffd166}
.pwall .wsh{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(7,6,11,.62) 0,rgba(7,6,11,0) 22%),linear-gradient(0deg,rgba(7,6,11,.86) 0,rgba(7,6,11,.35) 38%,rgba(7,6,11,0) 62%),linear-gradient(90deg,rgba(7,6,11,.55) 0,rgba(7,6,11,0) 55%)}
.pwall .wcopy{position:absolute;left:0;right:0;bottom:64px}.pwall .eyebrow{color:rgba(255,255,255,.66)}
.pwall h1{font:300 clamp(38px,4.6vw,70px)/1.02 var(--sans);letter-spacing:-.04em;margin:14px 0 14px;max-width:18ch;color:#fff;text-shadow:0 2px 24px rgba(0,0,0,.35)}
.pwall .wsub{font:300 clamp(18px,1.7vw,24px)/1.35 var(--sans);color:rgba(255,255,255,.8);margin:0 0 28px}
.pwall .cta{display:flex;gap:10px;flex-wrap:wrap}.pwall .btn.wh{background:#fff;color:#07060b;border-color:#fff}.pwall .btn.wl{background:transparent;color:#fff;border-color:rgba(255,255,255,.45)}.pwall .btn.wl:hover{border-color:#fff}
@media (max-width:900px){.pwall{height:92vh;min-height:560px}.pwall .wc .op{display:none}.pwall .wcopy{bottom:40px}}
.pban{position:relative;overflow:hidden;background:#07060b;color:#fff;min-height:min(100vh,940px);display:flex;align-items:center;padding:150px 0 90px}
.pban::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 70% at 72% 48%,rgba(82,0,255,.38),transparent 70%),radial-gradient(40% 50% at 12% 90%,rgba(82,0,255,.16),transparent 70%)}
.pban::after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:56px 56px;mask-image:radial-gradient(70% 70% at 60% 50%,#000 30%,transparent 80%);-webkit-mask-image:radial-gradient(70% 70% at 60% 50%,#000 30%,transparent 80%)}
.pban .wrap2{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:40px;align-items:center;width:100%}
.pban .eyebrow{color:rgba(255,255,255,.55)}
.pban h1{font:200 clamp(64px,9.5vw,148px)/.92 var(--sans);letter-spacing:-.05em;margin:18px 0 26px;color:#fff}
.pban .lede{font:300 clamp(20px,1.9vw,27px)/1.35 var(--sans);color:rgba(255,255,255,.78);max-width:24ch;margin:0 0 34px}
.pban .cta{display:flex;gap:10px;flex-wrap:wrap}.pban .btn.wh{background:#fff;color:#07060b;border-color:#fff}.pban .btn.wl{background:transparent;color:#fff;border-color:rgba(255,255,255,.35)}.pban .btn.wl:hover{border-color:#fff}
.pban .meta{display:flex;justify-content:flex-start;gap:22px;flex-wrap:wrap;margin-top:44px;font:400 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.45)}
.loop{position:relative;width:min(520px,100%);aspect-ratio:1;margin-left:auto}
.loop svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.loop .rg{fill:none;stroke:rgba(255,255,255,.14);stroke-width:1}.loop .rg2{fill:none;stroke:rgba(255,255,255,.07);stroke-width:1;stroke-dasharray:2 6}
.loop .arc{fill:none;stroke:url(#lg);stroke-width:2.5;stroke-linecap:round;transform-origin:260px 260px;animation:larc 6s linear infinite}
.loop .nd circle{fill:#07060b;stroke:rgba(255,255,255,.35);stroke-width:1.2;transition:all .35s}.loop .nd text{fill:rgba(255,255,255,.6);font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;transition:fill .35s}
.loop .nd.on circle{fill:#5200ff;stroke:#a98bff;filter:drop-shadow(0 0 10px rgba(130,90,255,.9))}.loop .nd.on text{fill:#fff}
.loop .core{position:absolute;inset:27% 22%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:8px}
.loop .core .k{font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#a98bff}
.loop .core .v{font:300 clamp(15px,1.5vw,19px)/1.35 var(--sans);color:#fff;transition:opacity .35s,transform .35s}.loop .core .v.out{opacity:0;transform:translateY(6px)}
.loop .core .s{font:400 10.5px var(--mono);color:rgba(255,255,255,.45)}
@keyframes larc{from{transform:rotate(-180deg)}to{transform:rotate(180deg)}}
@media (max-width:900px){.pban{min-height:0;padding:120px 0 64px}.pban .wrap2{grid-template-columns:1fr}.loop{margin:10px auto 0;width:min(400px,100%)}}
@media (prefers-reduced-motion:reduce){.loop .arc{animation:none}}
.pw{position:relative}
.pw .hl{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;border:2px solid #7d5cff;border-radius:12px;z-index:5;opacity:0;
 box-shadow:0 0 0 9999px rgba(12,9,22,0),0 0 0 4px rgba(82,0,255,0);
 transition:left .8s cubic-bezier(.65,0,.35,1),top .8s cubic-bezier(.65,0,.35,1),width .8s cubic-bezier(.65,0,.35,1),height .8s cubic-bezier(.65,0,.35,1),box-shadow .7s ease,border-color .5s,opacity .4s}
.pw .hl.on{opacity:1;box-shadow:0 0 0 9999px rgba(12,9,22,.46),0 0 0 4px rgba(82,0,255,.2)}
.pw .hl.full{opacity:1;border-color:rgba(125,92,255,.55);box-shadow:0 0 0 9999px rgba(12,9,22,0),0 0 0 4px rgba(82,0,255,0)}
.pw .hl b{position:absolute;left:-15px;top:-15px;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(140deg,#9a7dff,#5200ff);color:#fff;font:500 13px var(--pf-m);border:2px solid rgba(255,255,255,.75);box-shadow:0 4px 16px rgba(82,0,255,.5);transform:scale(1);transition:transform .35s cubic-bezier(.34,1.56,.64,1) .45s}
.pw .hl.full b{transform:scale(0);transition-delay:0s}
.pg .abc li b{border-radius:50%}
.pg .hero2{padding:168px 0 72px;text-align:center}.pg .hero2 .eyebrow{color:var(--muted-l)}
.pg .hero2 h1{font:200 clamp(40px,5.2vw,78px)/1.02 var(--sans);letter-spacing:-.035em;margin:20px auto 22px;max-width:19ch;color:var(--ink)}
.pg .hero2 .lede{font:300 clamp(18px,1.6vw,22px)/1.45 var(--sans);color:var(--muted-l);max-width:52ch;margin:0 auto 30px}
.pg .hero2 .cta{display:flex;gap:10px;justify-content:center;margin-bottom:64px}
.pg .btn.dk{background:var(--ink);color:#fff;border-color:var(--ink)}.pg .btn.dk:hover{background:#000}.pg .btn.ln{border-color:var(--rule-l);color:var(--ink);background:transparent}.pg .btn.ln:hover{border-color:var(--ink)}
.pg .stage{max-width:1100px;margin:0 auto}
.pg .meta{display:flex;justify-content:center;gap:28px;margin-top:22px;font:400 10.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.pg section.blk{padding:120px 0;border-top:1px solid var(--rule-l)}
.pg .bh{display:grid;grid-template-columns:1fr 1fr;gap:24px 64px;align-items:end;margin-bottom:44px}
.pg .bh h2{font:300 clamp(36px,4.4vw,64px)/1.02 var(--sans);letter-spacing:-.03em;margin:10px 0 0;color:var(--ink)}
.pg .bh p{font:300 19px/1.5 var(--sans);color:var(--muted-l);margin:0;max-width:44ch}
.pg #beyond{padding-bottom:40px}.pg #beyond .bh{margin-bottom:10px}
@media (min-width:901px){.pg .pin{height:calc(100vh + 150vh)}.pg .stick{position:sticky;top:84px;height:calc(100vh - 84px);display:flex;align-items:center}.pg .stick .wrap2{width:100%}
 .pg .tabs2 button{position:relative;overflow:hidden}.pg .tabs2 button i{position:absolute;left:0;bottom:0;height:2px;background:#5200ff;width:0}}
.pg .tabs2{display:flex;gap:6px;margin-bottom:22px;flex-wrap:wrap}.pg .tabs2 button{font:500 11.5px var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:10px 16px;border:1px solid var(--rule-l);background:transparent;color:var(--muted-l);cursor:pointer;border-radius:0}
.pg .tabs2 button[aria-selected=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
.pg .tp{display:none;grid-template-columns:minmax(0,1.7fr) minmax(0,1fr);gap:40px;align-items:start}.pg .tp.on{display:grid}
.pg .abc{list-style:none;margin:0;padding:0;border-top:1px solid var(--ink)}.pg .abc li{display:grid;grid-template-columns:34px 1fr;gap:4px 12px;padding:18px 0;border-bottom:1px solid var(--rule-l);transition:opacity .3s}
.pg .abc li b{font:500 12px var(--mono);color:var(--ink);border:1px solid var(--ink);width:24px;height:24px;display:grid;place-items:center}.pg .abc li p{margin:0;font:400 16px/1.5 var(--sans);color:var(--ink)}
.pg .abc li.dim{opacity:.38}
.pg .num{display:flex;align-items:center;gap:10px;font:400 12px var(--mono);color:var(--muted-l);margin-bottom:26px}.pg .num i{flex:0 1 120px;min-width:12px;height:1px;background:var(--rule-l)}.pg .num b{font-weight:400;color:var(--ink)}
.pg .feat{display:grid;grid-template-columns:1fr 1fr;gap:28px 64px;align-items:start;margin-bottom:40px}.pg .feat h3{font:300 clamp(32px,3.6vw,52px)/1.05 var(--sans);letter-spacing:-.03em;margin:0;color:var(--ink)}
.pg .feat p{font:300 19px/1.55 var(--sans);color:var(--muted-l);margin:0}.pg .feat p+p{margin-top:14px}
.pg .feat-stage{max-width:1000px}
.pg .fsec{padding:110px 0}.pg .fgrid{display:grid;grid-template-columns:minmax(300px,.62fr) minmax(0,1fr);gap:56px;align-items:start;padding-left:max(var(--gutter),calc((100vw - 1240px) / 2 + var(--gutter)))}
.pg .fside{position:sticky;top:120px}.pg .fside h3{font:300 clamp(34px,3.7vw,58px)/1.04 var(--sans);letter-spacing:-.035em;margin:0 0 26px;color:var(--ink)}
.pg .fside .fp p{font:300 18px/1.55 var(--sans);color:var(--muted-l);margin:0}.pg .fside .fp p+p{margin-top:14px}
.pg .fstage .pw{border-radius:14px 0 0 14px;border-right:0}.pg .fstage .pw .app{min-height:470px}
.pg .num b+i{flex:1 1 auto}
.pg .fside .abc li{padding:15px 0}.pg .fside .abc li p{font:300 17px/1.5 var(--sans)}
/* the reveal: lines draw in, numbers fade up, the heading types itself, the paragraphs follow */
[data-rv] .num i{transform:scaleX(0);transform-origin:left;transition:transform .8s cubic-bezier(.65,0,.35,1)}[data-rv] .num b,[data-rv] .num span{opacity:0;transform:translateY(5px);transition:opacity .5s,transform .5s}
[data-rv].rv .num i{transform:none}[data-rv].rv .num b,[data-rv].rv .num span{opacity:.84;transform:none;transition-delay:.45s}[data-rv].rv .num b{opacity:1}
[data-type] .ch{opacity:0;transition:opacity .18s}[data-type] .ch.v{opacity:1}[data-type] .w{display:inline-block;white-space:nowrap}
[data-rv] .fp li,[data-rv] .bh p{opacity:0;transform:translateY(10px);transition:opacity .7s,transform .7s cubic-bezier(.16,1,.3,1)}[data-rv].rv2 .fp li,[data-rv].rv2 .bh p{opacity:1;transform:none}[data-rv].rv2 .fp li.dim{opacity:.38}
[data-rv] .fstage .pw{opacity:0;transform:translateX(40px);transition:opacity .9s,transform 1.1s cubic-bezier(.16,1,.3,1)}[data-rv].rv .fstage .pw{opacity:1;transform:none}
@media (max-width:900px){.pg .fgrid{grid-template-columns:1fr;padding:0 var(--gutter);gap:30px}.pg .fside{position:static}.pg .fstage .pw{border-radius:14px;border-right:1px solid rgba(33,27,44,.14)}}
@media (prefers-reduced-motion:reduce){[data-rv] *{transition:none!important}}
.pg .ents{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--ink)}.pg .ents div{padding:26px 28px 26px 0;border-bottom:1px solid var(--rule-l)}
.pg .ents h4{font:500 15px var(--sans);margin:0 0 8px;color:var(--ink)}.pg .ents p{margin:0;color:var(--muted-l);font-size:15px;line-height:1.55}
.pg .close{text-align:center;padding:140px 0}.pg .close h2{font:200 clamp(40px,5vw,76px)/1.02 var(--sans);letter-spacing:-.035em;margin:0 auto 28px;max-width:16ch;color:var(--ink)}
.pg .src{font:400 11px var(--mono);letter-spacing:.04em;color:var(--muted-l);margin-top:14px}
.pg .depth{background:#fff;border-top:1px solid var(--rule-l);padding:110px 0 120px}
.pg .dgrid{display:grid;grid-template-columns:minmax(260px,.62fr) minmax(0,1fr);gap:56px;align-items:start;padding:0 var(--gutter) 0 max(var(--gutter),calc((100vw - 1240px) / 2 + var(--gutter)))}
.pg .drail{position:sticky;top:110px}.pg .drail h2{font:300 clamp(32px,3.2vw,48px)/1.05 var(--sans);letter-spacing:-.03em;margin:12px 0 28px;color:var(--ink)}
.pg .drail nav{display:flex;flex-direction:column;border-top:1px solid var(--ink);margin-bottom:28px}
.pg .drail nav a{font:400 14px/1.35 var(--sans);color:var(--muted-l);text-decoration:none;padding:10px 0 10px 14px;border-bottom:1px solid var(--rule-l);border-left:2px solid transparent;transition:color .25s,border-color .25s,padding .25s}
.pg .drail nav a:hover{color:var(--ink)}.pg .drail nav a.on{color:var(--ink);border-left-color:#5200ff;padding-left:18px}
.pg .depth .doc{max-width:760px;padding:0}.pg .depth .doc>h2:first-child,.pg .depth .doc>.box+h2{margin-top:0}
.pg .depth .doc h2{scroll-margin-top:110px}
.pg .qa{border-top:1px solid var(--ink)}.pg .qa details{border-bottom:1px solid var(--rule-l)}
.pg .qa summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:16px;padding:18px 0;font:500 17px/1.4 var(--sans);color:var(--ink)}.pg .qa summary::-webkit-details-marker{display:none}
.pg .qa summary::after{content:"+";font:300 22px/1 var(--sans);color:var(--muted-l);transition:transform .25s}.pg .qa details[open] summary::after{transform:rotate(45deg)}
.pg .qa details p{margin:0 0 20px;max-width:64ch}
@media (max-width:900px){.pg .dgrid{grid-template-columns:1fr;padding:0 var(--gutter);gap:28px}.pg .drail{position:static}.pg .drail nav{display:none}}
.pg .depth .doc h2{font:300 32px/1.1 var(--sans);letter-spacing:-.02em;margin:56px 0 16px;color:var(--ink)}.pg .depth .doc h3{font:500 17px var(--sans);margin:28px 0 8px;color:var(--ink)}
.pg .depth .doc p,.pg .depth .doc li{font:400 17px/1.65 var(--sans);color:rgba(30,31,43,.86)}.pg .depth .doc a{color:var(--ink)}
.pg .depth .doc table{width:100%;border-collapse:collapse;font-size:15px;margin:16px 0}.pg .depth .doc th,.pg .depth .doc td{text-align:left;padding:10px 12px 10px 0;border-bottom:1px solid var(--rule-l);vertical-align:top}
@media (max-width:900px){.pg .bh,.pg .feat,.pg .tp.on{grid-template-columns:1fr}.pg .ents{grid-template-columns:1fr}.pg .hero2{padding:120px 0 48px}.pg section.blk{padding:80px 0}}
"""

ICON = {"new": '<path d="M12 5v14M5 12h14"/>', "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
        "proj": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
        "art": '<path d="M21 16V8l-9-5-9 5v8l9 5 9-5z"/><path d="M3.3 7 12 12l8.7-5M12 22V12"/>', "task": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'}
ic = lambda k: f'<svg viewBox="0 0 24 24">{ICON[k]}</svg>'


def cron(s: str) -> str:
    m, h, dom, mon, dow = (s.split() + ["*"] * 5)[:5]
    if m.startswith("*/"): return f"Every {m[2:]} minutes"
    if "," in m and h == "*": return "Twice an hour"
    if h == "*" and m.isdigit(): return f"Hourly at :{int(m):02d}"
    if h.startswith("*/"): return f"Every {h[2:]} hours"
    if "," in h: return "Twice a day"
    if h.isdigit() and m.isdigit():
        t = f"{int(h):02d}:{int(m):02d}"
        return {"1": f"Mondays at {t}", "0": f"Sundays at {t}", "1-5": f"Weekdays at {t}"}.get(dow, f"Daily at {t}")
    return s


def window(inner: str, active: str, fleet, wid: str = "", label: str = "PRAGMA") -> str:
    sch = "".join(f'<a class="s" href="#"><b>{E(t["name"])}</b><small>{E(cron(t["schedule"]).split(" at ")[-1][:5]) if " at " in cron(t["schedule"]) else ""}</small></a>' for t in fleet[:5])
    nav = "".join(f'<a class="{"on" if k == active else ""}" href="#">{ic(k)}{lab}</a>' for k, lab in (("chat", "Chats"), ("proj", "Projects"), ("art", "Artifacts"), ("task", "Tasks")))
    return (f'<div class="pw"{f" id={chr(34)}{wid}{chr(34)}" if wid else ""}><div class="bar"><i></i><i></i><i></i><span>{label}</span></div><div class="app">'
            f'<aside class="sd"><a class="nw" href="#">{ic("new")}New chat</a>{nav}<div class="lb">Scheduled</div>{sch}</aside><div class="mn">{inner}</div></div></div>')


def fleet_view(fleet, mem_task: str) -> str:
    rows = "".join(f'<div class="tk" data-i="{i}"><div class="n">{E(t["name"])}{" <span class=pill>Self-Improving Memory · on</span>" if t["name"] == mem_task else ""}</div>'
                   f'<div class="d">{E(t["description"])}</div><div class="w">{E(cron(t["schedule"]))}<em data-s>in {3 + i * 7}m</em></div><i class="sw"></i></div>'
                   for i, t in enumerate(fleet[:7]))
    return (f'<div class="hd"><div><h4>Scheduled tasks</h4><p class="sub">Prompts that run on their own. Each run opens a fresh chat under Scheduled.</p></div>'
            f'<span class="bt pr">New task in chat</span></div><div class="fleet">{rows}</div>')


def chat_view() -> str:
    return '<div class="ch" data-chat></div><div class="cp">Write a message…</div>'


def memory_view(mem) -> str:
    eps = mem.get("episodes") or []
    if not eps:
        return '<h4>Self-Improving Memory</h4><p class="sub">No run scored yet.</p>'
    last = eps[-1]
    fmt = lambda iso: dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%a %-d %b")
    bars = "".join(f'<i class="{"p" if e["score"] > 0.24 else "z" if e["score"] > -0.25 else "n"}" style="height:{int(8 + 38 * (e["score"] + 1) / 2)}px;transition-delay:{i * 45}ms"></i>' for i, e in enumerate(eps))
    ls = "".join(f'<div class="ls" style="transition-delay:{400 + i * 150}ms"><p>{E(l["text"])}</p><div class="f"><span>Learned {fmt(l["learned_at"])}</span><span class="bt dg">Stop using this lesson</span></div></div>'
                 for i, l in enumerate(mem.get("lessons", [])[:3]))
    return (f'<div class="mt" style="margin-bottom:3px">Tasks · <span style="font-family:var(--pf-m)">{E(mem["task"])}</span></div><h4>Self-Improving Memory</h4>'
            f'<div class="cd st"><span class="ok">● Connected</span><span>Judge <b>{E(mem.get("judge_model", "glm-5.3"))}</b></span><span>Runs scored <b>{len(eps)}</b></span></div>'
            f'<div class="cd lr"><h5>Latest result</h5><div style="font-size:11.5px">Run on {fmt(last["at"])} scored <span class="sc {last["verdict"]}">{last["verdict"].title()}</span> '
            f'<span class="mt">({last["score"]:+.2f} on a scale from -1 to +1)</span></div><div class="mt" style="margin-top:3px">{E(last["reason"])}</div><div class="sp">{bars}</div></div>'
            f'<div class="cd lw"><h5>What it learned</h5><div class="mt">The next run starts with up to 5 of these lessons.</div>{ls}</div>')


def turnon_view(task: str) -> str:
    return (f'<div style="opacity:.55"><h4>Scheduled tasks</h4><p class="sub">Prompts that run on their own.</p></div><div class="dl"><div class="dg2">'
            f'<div class="k">Scheduled task · {E(task)}</div><h5>Turn on Self-Improving Memory</h5><p>After each run, a judge grades the work against the workflow\'s own instructions, and the workflow writes a lesson. The next run starts with its best 5 lessons.</p>'
            f'<h6>1. Workflow</h6><div class="fl"><code>{E(task)}</code><span class="mt">Hourly at :05</span></div>'
            '<h6>2. Technique</h6><div class="tc"><div class="op on"><b>ICRL</b>A judge scores each run. The workflow writes lessons.</div><div class="op"><b>Outcome learning · later</b>Scores runs from real results.</div></div>'
            '<h6>3. When it runs</h6><div class="tc wr"><div class="fl">2 hours after each run</div><div class="fl">Token cap per run</div></div>'
            '<div class="su"><b>Pragma sets this up for you</b>A judge grades each run against the workflow\'s own instructions. A permanent memory routine is created; it uses memory tools only. Lessons apply on their own; changes to the main instructions wait for your approval.</div>'
            '<div class="ft"><span class="bt">Cancel</span><span class="bt pr">Turn on Self-Improving Memory</span></div></div></div>')


def ontology_view(rules) -> str:
    objs = [("collision-alert", "From the collision avoidance system"), ("supervisor-alert", "Routed to a named supervisor"), ("interaction-event", "Two assets inside a proximity threshold"),
            ("evidence-clip", "Fixed camera footage of the event"), ("fixed-camera", "Status, road segment, dump pocket"), ("maintenance-work-order", "Repair tracking for machinery and cameras")]
    ob = "".join(f'<div>{E(a)}<small>{E(b)}</small></div>' for a, b in objs)
    rl = "".join(f'<div>{E(r)}</div>' for r in rules[:5])
    return (f'<h4>Mining safety ontology</h4><p class="sub">What each agent reads before it acts, and the rules it may never break.</p><div class="ob">{ob}</div>'
            f'<div class="mt" style="margin:12px 0 0">Rules every agent in the fleet carries</div><div class="rl">{rl}</div>')


def boundary_view() -> str:
    box = lambda t, d: f'<div style="border:1px solid var(--p-ln);border-radius:10px;background:var(--p-sf);padding:9px 11px"><b style="font:600 11.5px var(--pf-t)">{E(t)}</b><div class="mt" style="margin-top:2px">{E(d)}</div></div>'
    inner = "".join(box(t, d) for t, d in [("Pragma agents", "The fleet, its schedules and every governed action"), ("Hyper Ontology", "What each record means and which actions are allowed"),
                                           ("Self-Improving Memory", "Every run, every grade and every lesson"), ("Open weight models", "Frontier reasoning on your own GPUs"),
                                           ("Systems of record", "Read through the ontology, written only through its actions"), ("A record of every action", "What was read, decided and approved, by whom")])
    return ('<h4>Your boundary</h4><p class="sub">Everything a run touches stays inside it. On premises, in your private cloud, or air gapped.</p>'
            '<div class="bx" style="border:1.5px dashed rgba(82,0,255,.45);border-radius:14px;padding:12px;background:rgba(82,0,255,.03)">'
            '<div class="mt" style="font:500 9.5px var(--pf-m);letter-spacing:.06em;margin-bottom:8px;color:var(--p-ac)">INSIDE YOUR WALLS</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px">{inner}</div></div>'
            '<div class="st" style="margin-top:10px"><span>Outbound calls at run time <b>none required</b></span><span>Model swap <b>memory carries over</b></span></div>')


JS = r"""<script>(function(){
var D=window.PRAGMA_DEMO||{};var still=matchMedia('(prefers-reduced-motion: reduce)').matches;
function el(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function md(s){return esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/`([^`]+)`/g,'<code style="font:400 10.5px var(--pf-m);background:var(--p-sk);padding:0 3px;border-radius:3px">$1</code>')}
/* chat: replays the real run, step by step */
function chat(box){if(!box||!D.run)return;var steps=D.run.steps,i=0,t=null;
 function short(s){var f=s.split(/\n\n/)[0];return f.length>240?f.slice(0,238)+'…':f}
 function step(){if(i===0){box.innerHTML='';box.appendChild(el('div','u','Run the Maintainer fault scan: open a work order for every fault no open order covers.'))}
  if(i>=steps.length){var a=el('div','wo','<b>MFS-115</b><span>Fixed camera F · repeated degraded state · 2 proving clips</span><span class="pill">high</span>');box.appendChild(a);
   box.appendChild(el('div','wo','<b>MFS-116</b><span>Fixed camera q · lens dust · 2 proving clips</span><span class="pill">high</span>'));
   box.appendChild(el('div','a','<b>16 faults found, 2 work orders created, 14 skipped as duplicates.</b> No alert closed, nobody notified about shadow mode alerts, both orders left unassigned for a person.'));
   t=setTimeout(function(){i=0;step()},6000);trim();return}
  var s=steps[i++];
  if(s.k==='call'){var c=el('div','c',esc(s.t)+(s.q?' <q>'+esc(s.q)+'</q>':''));c.dataset.k=/ontology|contract/.test(s.t)?'onto':/open work orders/.test(s.t)?'dedup':/create work order/.test(s.t)?'act':'';box.appendChild(c);setTimeout(function(){c.classList.add('dn')},380);t=setTimeout(step,still?0:520)}
  else{box.appendChild(el('div','a',md(short(s.t))));t=setTimeout(step,still?0:1300)}trim()}
 function trim(){box.scrollTop=box.scrollHeight}
 box._start=function(){clearTimeout(t);i=0;step()};box._stop=function(){clearTimeout(t)}}
/* fleet: one task after another picks up its run */
function fleet(w){if(!w)return;var rows=[].slice.call(w.querySelectorAll('.tk')),k=0,t=null;
 function tick(){rows.forEach(function(r){r.classList.remove('run');var s=r.querySelector('[data-s]');if(s&&s.dataset.d)s.textContent=s.dataset.d});var r=rows[k%rows.length];var s=r.querySelector('[data-s]');if(s){s.dataset.d=s.dataset.d||s.textContent;s.textContent='Running…'}r.classList.add('run');k++;t=setTimeout(tick,1100)}
 w._start=function(){clearTimeout(t);tick()};w._stop=function(){clearTimeout(t)}}
document.querySelectorAll('[data-chat]').forEach(chat);
document.querySelectorAll('.pw').forEach(function(w){if(w.querySelector('.fleet'))fleet(w)});
/* run a window only while it is on screen */
var io=new IntersectionObserver(function(es){es.forEach(function(e){var w=e.target,x=w.querySelector('[data-chat]')||w;
 if(e.isIntersecting){w.classList.add('live');if(x._start&&!x._on){x._on=1;x._start()}}else{if(x._stop){x._stop();x._on=0}}})},{threshold:.35});
document.querySelectorAll('.pw').forEach(function(w){io.observe(w)});
/* the focus frame: starts around the whole screen, then shrinks onto what the active callout is about,
   the rest dimmed, the callout's letter on the screen. One per group: a tab panel or a numbered section. */
function mark(g){var w=g.querySelector('.pw'),li=g.querySelectorAll('.abc li'),a=g._n||0;if(!w)return;var h=w.querySelector('.hl');
 if(!h){h=el('i','hl full','<b></b>');w.appendChild(h)}h.firstChild.textContent='ABCD'.charAt(a);
 var wr=w.getBoundingClientRect(),full=Date.now()<(g._hold||0),r=null;
 if(!full){var sel=li[a]&&li[a].dataset.hl,box=w.querySelector('.ch'),br=box?box.getBoundingClientRect():null;
  if(sel)w.querySelectorAll(sel).forEach(function(e){var q=e.getBoundingClientRect();if(!q.width)return;
   if(br&&box.contains(e)){if(q.bottom<br.top+4||q.top>br.bottom-4)return;q={left:q.left,right:q.right,top:Math.max(q.top,br.top),bottom:Math.min(q.bottom,br.bottom)}}
   r=r?{left:Math.min(r.left,q.left),right:Math.max(r.right,q.right),top:Math.min(r.top,q.top),bottom:Math.max(r.bottom,q.bottom)}:{left:q.left,right:q.right,top:q.top,bottom:q.bottom}})}
 if(!r){h.style.left='0px';h.style.top='0px';h.style.width=wr.width+'px';h.style.height=wr.height+'px';h.classList.remove('on');h.classList.add('full');return}
 var pd=6,L=Math.max(18,r.left-wr.left-pd),T=Math.max(18,r.top-wr.top-pd);
 h.style.left=L+'px';h.style.top=T+'px';h.style.width=Math.min(wr.width-L-4,r.right-wr.left+pd-L)+'px';h.style.height=Math.min(wr.height-T-4,r.bottom-wr.top+pd-T)+'px';h.classList.remove('full');h.classList.add('on')}
function intro(g){var w=g.querySelector('.pw'),h=w&&w.querySelector('.hl');g._hold=Date.now()+(still?0:+(g.dataset.hold||900));
 if(h){h.style.transition='none';h.classList.remove('on');h.classList.add('full');h.style.left='0px';h.style.top='0px';h.style.width='100%';h.style.height='100%';void h.offsetWidth;h.style.transition=''}mark(g)}
function pick(g,n){g._n=n;g.querySelectorAll('.abc li').forEach(function(l,j){l.classList.toggle('dim',j!==n)});mark(g)}
function stopF(g){clearInterval(g._ct);clearInterval(g._ht);g._run=0}
function startF(g){stopF(g);g._run=1;var n=g.querySelectorAll('.abc li').length;intro(g);pick(g,0);
 g._ct=setInterval(function(){if(!g._hov&&Date.now()>(g._hold||0))pick(g,((g._n||0)+1)%n)},3000);g._ht=setInterval(function(){mark(g)},120)}
var groups=[].slice.call(document.querySelectorAll('.fgroup'));
groups.forEach(function(g){g.querySelectorAll('.abc li').forEach(function(l,j){l.addEventListener('mouseenter',function(){g._hov=true;g._hold=0;pick(g,j)});l.addEventListener('mouseleave',function(){g._hov=false})})});
/* each time a group comes on screen its frame starts wide again; off screen it rests */
var fio=new IntersectionObserver(function(es){es.forEach(function(e){var g=e.target,tab=g.classList.contains('tp');
 if(e.isIntersecting&&(!tab||g.classList.contains('on'))){if(!g._run)startF(g)}else if(!e.isIntersecting)stopF(g)})},{threshold:.4});
groups.forEach(function(g){fio.observe(g)});
/* tabs: switching restarts that panel's frame. On wide screens the section pins and scrolling walks the tabs. */
var tb=document.getElementById('beyond');if(tb){var bs=tb.querySelectorAll('.tabs2 button'),ps=tb.querySelectorAll('.tp'),cur=0;
 function show(k){cur=k;bs.forEach(function(b,j){b.setAttribute('aria-selected',j===k?'true':'false')});ps.forEach(function(p,j){p.classList.toggle('on',j===k);
  var w=p.querySelector('.pw');if(j===k&&w){w.classList.remove('live');void w.offsetWidth;w.classList.add('live')}if(j!==k)stopF(p)});startF(ps[k])}
 var pin=tb.querySelector('.pin'),stick=tb.querySelector('.stick'),mq=matchMedia('(min-width:901px)');
 bs.forEach(function(b){b.appendChild(el('i'))});
 function range(){return pin.offsetHeight-stick.offsetHeight}
 function onScroll(){if(!mq.matches)return;var r=pin.getBoundingClientRect(),R=range(),p=Math.min(1,Math.max(0,-r.top/R)),n=ps.length,k=Math.min(n-1,Math.floor(p*n));
  bs.forEach(function(b,j){b.lastChild.style.width=(j<k?100:j>k?0:Math.min(100,(p*n-k)*100))+'%'});if(k!==cur)show(k)}
 addEventListener('scroll',onScroll,{passive:true});addEventListener('resize',onScroll);
 bs.forEach(function(b,j){b.addEventListener('click',function(){if(mq.matches){var top=pin.getBoundingClientRect().top+scrollY;scrollTo({top:top+range()*(j+.15)/ps.length,behavior:'smooth'})}else show(j)})});
 ps[0].classList.add('on');onScroll()}
/* section reveal, the way the reference platform pages do it */
function split(h){if(h._sp)return;h._sp=1;var t=h.textContent;h.setAttribute('aria-label',t);h.textContent='';
 t.split(' ').forEach(function(w,i){if(i)h.appendChild(document.createTextNode(' '));var ws=el('span','w');ws.setAttribute('aria-hidden','true');
  w.split('').forEach(function(c){ws.appendChild(el('span','ch',esc(c)))});h.appendChild(ws)})}
document.querySelectorAll('[data-type]').forEach(split);
function reveal(sec){if(sec._rv)return;sec._rv=1;sec.classList.add('rv');var hs=sec.querySelectorAll('[data-type]');
 if(still){sec.querySelectorAll('.ch').forEach(function(c){c.classList.add('v')});sec.classList.add('rv2');return}
 var cs=[].concat.apply([],[].map.call(hs,function(h){return [].slice.call(h.querySelectorAll('.ch'))})),i=0,d=sec.querySelector('.num')?650:200;
 setTimeout(function tick(){var n=Math.min(cs.length,i+2);for(;i<n;i++)cs[i].classList.add('v');if(i<cs.length)setTimeout(tick,60);else setTimeout(function(){sec.classList.add('rv2')},120)},d)}
var rio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){reveal(e.target);rio.unobserve(e.target)}})},{threshold:.18,rootMargin:'0px 0px -12% 0px'});
document.querySelectorAll('[data-rv]').forEach(function(s){rio.observe(s)});
/* in depth: the contents rail follows where you are */
var rail=document.querySelectorAll('.drail nav a');if(rail.length){var hs=[].map.call(rail,function(a){return document.getElementById(a.getAttribute('href').slice(1))});
 function spy(){var y=innerHeight*.3,k=0;hs.forEach(function(h,j){if(h&&h.getBoundingClientRect().top<y)k=j});rail.forEach(function(a,j){a.classList.toggle('on',j===k)})}
 addEventListener('scroll',spy,{passive:true});spy()}
/* banner: a wall of operations; across it the loop keeps running: a run starts, it is graded, a lesson is kept */
var wall=document.querySelector('.pwall');if(wall){var vd=wall.querySelector('.wv'),wg=wall.querySelector('.wg'),cells=[].slice.call(wg.children);
 function fit(){var W=wall.clientWidth,H=wall.clientHeight,k=Math.max(W/1920,H/1080),w=1920*k,h=1080*k;wg.style.width=w+'px';wg.style.height=h+'px';wg.style.left=(W-w)/2+'px';wg.style.top=(H-h)/2+'px';wg.style.setProperty('--cx',Math.max(0,(w-W)/2)+'px')}
 fit();addEventListener('resize',fit);
 var SHOW=innerWidth>900?[4,5,6,7,10,11]:[4,5,6,7,8,9,10,11],ST=[['on','Run started'],['on g','Graded by the judge'],['on l','Lesson kept'],['on','Next run, with its lessons']],busy={};
 function play(i){if(busy[i])return;busy[i]=1;var c=cells[i],ch=c.querySelector('.chip'),n=0;
  (function step(){if(n>=ST.length){c.className='wc';setTimeout(function(){busy[i]=0},600);return}c.className='wc '+ST[n][0];ch.textContent=ST[n][1];n++;setTimeout(step,1100)})()}
 if(!still){var last=-1;setInterval(function(){if(document.hidden)return;var free=cells.map(function(_,j){return j}).filter(function(j){return !busy[j]&&j!==last&&SHOW.indexOf(j)>=0});
  if(free.length){last=free[Math.floor(Math.random()*free.length)];play(last)}},1500);play(5)}
 if(still&&vd){vd.removeAttribute('autoplay');vd.pause()}}
/* banner: the learning loop, stage by stage, on the real run */
var lp=document.querySelector('.loop');if(lp&&D.memory){var eps=D.memory.episodes||[],live=eps.filter(function(e){return e.lessons_read}).sort(function(a,b){return (b.score-a.score)||(b.tool_calls-a.tool_calls)}),e=live[0]||eps[eps.length-1],ls=D.memory.lessons||[];
 var nd=lp.querySelectorAll('.nd'),k=lp.querySelector('.core .k'),v=lp.querySelector('.core .v'),sm=lp.querySelector('.core .s'),st=0;
 function cut(x,n){return x.length>n?x.slice(0,n-1).replace(/\s+\S*$/,'')+'…':x}
 var S=[['Run',D.memory.task+' reads its lessons, then scans the fleet',(e?e.tool_calls:0)+' governed actions'],
  ['Judge',e?('Scored '+(e.score>0?'+':'')+e.score.toFixed(2)+' · '+e.verdict.charAt(0).toUpperCase()+e.verdict.slice(1)):'Scored against its own instructions','judge on '+(D.memory.judge_model||'glm-5.3')],
  ['Lesson',ls[0]?cut(ls[0].text,96):'One lesson from the grade','kept in Engram'],
  ['Next run','Starts with its best '+Math.min(5,ls.length||5)+' lessons',eps.length+' runs graded so far']];
 function go(){nd.forEach(function(n,j){n.classList.toggle('on',j===st)});v.classList.add('out');setTimeout(function(){k.textContent=S[st][0];v.textContent=S[st][1];sm.textContent=S[st][2];v.classList.remove('out')},still?0:220)}
 go();if(!still)setInterval(function(){var n=Math.floor(performance.now()/1500)%4;if(n!==st){st=n;go()}},100)}   /* one clock with the arc: its head is at each node every 1.5 s */
})();</script>"""


WALL = ["Mine haul road", "Container port", "Wind farm", "Robotic assembly", "Solar farm", "Earthworks", "Rail yard", "Control room",
        "Field operations", "Steel plant", "Container shipping", "Production line", "Freight corridor", "Transmission grid", "Gas processing", "Offshore platform"]

LOOP_SVG = ('<div class="loop" aria-label="The learning loop: run, judge, lesson, next run">'
            '<svg viewBox="0 0 520 520"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5200ff" stop-opacity="0"/><stop offset="1" stop-color="#b9a2ff"/></linearGradient></defs>'
            '<circle class="rg2" cx="260" cy="260" r="236"/><circle class="rg" cx="260" cy="260" r="190"/>'
            '<circle class="arc" cx="260" cy="260" r="190" stroke-dasharray="300 894"/>'
            + "".join(f'<g class="nd"><circle cx="{x}" cy="{y}" r="9"/><text x="{tx}" y="{ty}" text-anchor="{a}">{t}</text></g>'
                      for x, y, tx, ty, a, t in ((260, 70, 260, 44, "middle", "Run"), (450, 260, 470, 264, "start", "Judge"),
                                                (260, 450, 260, 484, "middle", "Lesson"), (70, 260, 50, 264, "end", "Next run")))
            + '</svg><div class="core"><div class="k">Run</div><div class="v"></div><div class="s"></div></div></div>')


ENT = [("For the operations head", "One governed layer that puts AI to work across the operation, measured on outcomes, not seats."),
       ("For security and compliance", "Inference, memory and records stay inside your walls: on premises, in your private cloud or air gapped."),
       ("For the people doing the work", "Agents that draft, check and route, while the decisions that matter stay with the person accountable for them.")]


def depth_layout(depth_html: str) -> str:
    """In depth: a sticky contents rail on the left (it follows where you are), the text on the right,
    and the questions as rows that open. Every word stays in the page for people and answer engines."""
    import re
    d = re.sub(r'^\s*<p class="eyebrow">In depth</p>\s*<h2[^>]*>How Hyper Pragma works</h2>\s*', "", depth_html, count=1)
    toc, seen = [], set()
    def tag(m):
        attrs, title = m.group(1), m.group(2)
        hid = re.search(r'id="([^"]+)"', attrs)
        slug = hid.group(1) if hid else re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", title).lower()).strip("-")
        while slug in seen: slug += "-2"
        seen.add(slug); toc.append((slug, re.sub(r"<[^>]+>", "", title)))
        return f'<h2 id="{slug}">{title}</h2>'
    d = re.sub(r"<h2([^>]*)>(.*?)</h2>", tag, d)
    head, _, qa = d.partition('<h2 id="questions-agents-ask">Questions agents ask</h2>')
    rows = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in re.findall(r"<h3>(.*?)</h3><p>(.*?)</p>", qa, re.S))
    if rows:
        d = head + '<h2 id="questions-agents-ask">Questions agents ask</h2><div class="qa">' + rows + "</div>"
    nav = "".join(f'<a href="#{a}">{t}</a>' for a, t in toc)
    return (f'<section class="depth" data-rv><div class="dgrid"><aside class="drail"><p class="eyebrow">In depth</p><h2 data-type>How Hyper Pragma works</h2>'
            f'<nav aria-label="On this page">{nav}</nav><a class="btn dk" href="{brand.COMMERCIAL}">{brand.TALK}</a></aside><div class="doc">{d}</div></div></section>')


def build(depth_html: str, faq_ld: dict, head_extra: str = "") -> str:
    demo = json.loads((ROOT / "hyper-pragma" / "demo.json").read_text())
    fleet, mem, rules = demo["fleet"], demo["memory"], demo["rules"]
    mtask = mem.get("task", "fault-to-work-order")
    tab = lambda i, title, inner, active, abc: (
        f'<div class="tp fgroup{" on" if i == 0 else ""}"><div>{window(inner, active, fleet)}</div><ol class="abc">'
        + "".join(f'<li data-hl="{E(x[1])}"><b>{"ABC"[j]}</b><p>{E(x[0])}</p></li>' for j, x in enumerate(abc)) + "</ol></div>")
    tabs = [("Agents at work", chat_view(), "chat", [("Before it acts, the agent reads the ontology: what each object means, and which actions it may take.", ".c[data-k=onto]"),
                                                     ("It checks what already exists, so it never opens a second work order for a fault that has one.", ".c[data-k=dedup]"),
                                                     ("It acts through the ontology's own actions, cites the records that prove the fault, and leaves the decisions for a person.", ".wo,.c[data-k=act]")]),
            ("Scheduled fleet", fleet_view(fleet, mtask), "task", [("Each agent has one job: watch, triage, gather evidence, maintain, guard the SLA, audit.", ".tk .d"),
                                                                    ("They run on their own schedule, every 30 minutes to once a week, inside your walls.", ".tk .w"),
                                                                    ("Every agent carries the same hard rules, so none of them closes an alert or deletes a record.", ".tk.run")]),
            ("Self-Improving Memory", memory_view(mem), "task", [("After each run a judge grades the work against the workflow's own instructions, from -1 to +1, with a reason.", ".cd.lr"),
                                                                  ("The workflow writes a lesson from the grade, and its next run starts with its best five.", ".cd.lw .ls"),
                                                                  ("Every lesson is on one screen, and a person can stop using any of them.", ".ls .bt.dg")])]
    beyond = ("<section class=\"blk\" id=\"beyond\" data-rv><div class=\"wrap2\"><div class=\"bh\"><div><p class=\"eyebrow\">Learning Loop</p><h2 data-type>Agents that run the operation, and learn from every run.</h2></div>"
              "<p>Hyper Pragma turns AI in your workflows into agents that read your ontology, take governed actions, and get better after every run.</p></div></div>"
              '<div class="pin"><div class="stick"><div class="wrap2"><div class="tabs2" role="tablist">' + "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}">{E(t[0])}</button>' for i, t in enumerate(tabs)) + "</div>"
              + "".join(tab(i, *t) for i, t in enumerate(tabs)) + f'<p class="src">Recorded from Pragma: {E(demo["source"])}.</p></div></div></div></section>')
    feats = [("Built on your ontology", [("An agent never guesses what a record means. It reads the ontology first: every object, every link, and the actions your operation allows.", ".ob"),
                                         ("The rules travel with the agent. Every agent in this mining safety fleet carries the same rules, enforced on every run.", ".rl")], ontology_view(rules), "art"),
             ("Turn on Self-Improving Memory", [("One switch per workflow. Saving it creates the judge and a permanent memory routine for that workflow.", ".ft .pr"),
                                                ("There is no rubric to write. The judge grades each run against the instructions the workflow already has.", ".op.on"),
                                                ("You choose when the check runs: two hours after each run by default, and never more than two days after it.", ".tc.wr")], turnon_view(mtask), "task"),
             ("A judge, not a rubric", [("The judge is a separate reviewer on an open weight model, not the workflow grading itself.", ".cd.st"),
                                        ("It scores every run from minus one to plus one and writes down why, in plain words.", ".cd.lr"),
                                        ("Each bar is one real run of a Maintainer agent in the mining fleet, graded the same way.", ".sp")], memory_view(mem), "task"),
             ("Inside your walls", [("The agents, the models, the memory and the record of every action run where your data lives: on premises, in your private cloud or air gapped.", ".bx"),
                                    ("Open weight frontier models on your own hardware. When a better one is released you swap it in, and the ontology, the memory and the workflows carry over.", ".mn > .st")], boundary_view(), "proj")]
    numbered = "".join(
        f'<section class="blk fsec" data-rv><div class="fgrid fgroup" data-hold="1700"><div class="fside"><div class="num">' + "".join(f'<b>[0.{j + 1}]</b>' if j == i else f'<span>0.{j + 1}</span>' for j in range(4)).replace("</b><span>", "</b><i></i><span>").replace("</span><span>", "</span><i></i><span>")
        + f'</div><h3 data-type>{E(h)}</h3><ol class="abc fp">' + "".join(f'<li data-hl="{E(sel)}"><b>{"ABCD"[j]}</b><p>{E(t)}</p></li>' for j, (t, sel) in enumerate(ps))
        + f'</ol></div><div class="fstage">{window(w, a, fleet)}</div></div></section>'
        for i, (h, ps, w, a) in enumerate(feats))
    ents = "".join(f"<div><h4>{E(a)}</h4><p>{E(b)}</p></div>" for a, b in ENT)
    tiles = "".join(f'<div class="wc"><span class="op">{E(t)}</span><span class="chip"></span></div>' for t in WALL)
    body = (f'<main class="pg"><section class="pwall"><video class="wv" autoplay muted loop playsinline preload="auto" poster="/assets/video/pragma-wall.jpg">'
            f'<source src="/assets/video/pragma-wall.mp4" type="video/mp4"></video><div class="wg" aria-hidden="true">{tiles}</div><div class="wsh"></div>'
            '<div class="wrap2 wcopy"><p class="eyebrow">CodeNinja · Hyper Pragma</p>'
            '<h1>Put AI to work on your operations, and let it learn from every run.</h1>'
            '<p class="wsub">One platform for every operation.</p>'
            f'<div class="cta"><a class="btn wh" href="{brand.COMMERCIAL}">{brand.TALK}</a><a class="btn wl" href="#beyond">See it work</a></div></div></section>'
            f'{beyond}{numbered}'
            f'<section class="blk" data-rv><div class="wrap2"><div class="bh"><div><p class="eyebrow">Who it is for</p><h2 data-type>Built for the people who run the operation.</h2></div>'
            f'<p>For banks, energy companies, utilities, industrial operators and the public sector, where the data cannot leave and the decisions must be accountable.</p></div><div class="ents">{ents}</div></div></section>'
            f'<section class="close" data-rv><div class="wrap2"><h2 data-type>Every run leaves your operation a little smarter.</h2><a class="btn dk" href="{brand.COMMERCIAL}">{brand.TALK}</a></div></section>'
            f'{depth_layout(depth_html)}</main>')
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Pragma", "applicationCategory": "BusinessApplication",
           "description": "The AI layer on top of Hyper Ontology: agents that take governed actions inside an organisation's workflows, inside its walls, with Self-Improving Memory that grades every run and keeps lessons.",
           "url": f"{BASE}/hyper-pragma/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "releaseNotes": "Used in house by CodeNinja. Access through the commercial team, as a licence or metered on tokens.",
           "isRelatedTo": {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"}}, faq_ld]
    title = "Hyper Pragma: Self-Improving Sovereign AI for Operations | CodeNinja Atoms"
    desc = "Hyper Pragma is the AI layer on your ontology: agents that take governed actions inside your workflows, inside your walls, and learn from every run with Self-Improving Memory."
    nav = brand.nav(BASE + "/")
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/hyper-pragma/">'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/hyper-pragma/">'
            '<meta name="codeninja:kind" content="product">' + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
            + f'{brand.FONTS}<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600&display=swap" rel="stylesheet">'
            f'{brand.JS_FLAG}<style>{brand.CSS}{PAGE_CSS}{PCSS}</style>{head_extra}</head><body>{brand.header(BASE + "/", nav)}{body}'
            f'<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is part of <a href="{brand.PARENT}">CodeNinja</a></span></div></footer>'
            f'<script>window.PRAGMA_DEMO={json.dumps({"run": demo["run"], "memory": {"task": mem.get("task"), "judge_model": mem.get("judge_model"), "lessons": [{"text": l["text"]} for l in mem.get("lessons", [])], "episodes": [{k: e.get(k) for k in ("score", "verdict", "tool_calls", "lessons_read")} for e in mem.get("episodes", [])]}}, ensure_ascii=False)};</script>{JS}{brand.SCRIPT}</body></html>')
