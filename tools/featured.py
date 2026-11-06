"""Featured strip under the home hero (Umar, 6 Nov 2026): a Palantir style band of topic chips
over one large image card with a dark label box, rotating every few seconds. site_index.py calls
featured.html() between the hero film and the intro. Images and credits in assets/featured/.
"""
import html

E = lambda s: html.escape(str(s), quote=True)

# (eyebrow, headline, href relative to the home page, image in assets/featured/)
FEATURED = [
    ("Sea Power", "Rebuilding Middle Eastern Sea Power", "co-build/defense-and-intelligence/", "sea-power.jpg"),
    ("Saudi Arabia", "Bringing Intelligence to Everything That Moves in Saudi Arabia", "open-pit-mine-haul-fleet-saudi-arabia/", "saudi-arabia.jpg"),
    ("On Device AI", "Building On Device AI Stacks to Counterbalance Proprietary AI Inference", "developer/", "on-device.jpg"),
    ("13 Industries", "Training One System Across 13 Physical AI Industries", "sectors/", "thirteen-industries.jpg"),
]

CSS = """
section.featured{background:#EDEDEB;color:var(--ink);padding:40px var(--gutter) 72px}
section.featured .fw{max-width:var(--max);margin:0 auto}
section.featured .chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}
section.featured .chips button{font:400 13.5px/1 var(--sans);color:var(--muted-l);background:rgba(30,31,43,.06);border:0;border-radius:0;padding:8px 11px;cursor:pointer;letter-spacing:-.005em}
section.featured .chips button:hover{color:var(--ink)}section.featured .chips button[aria-selected=true]{background:#fff;color:var(--ink);box-shadow:0 0 0 1px var(--rule-l)}
section.featured .stage{position:relative;aspect-ratio:1920/902;overflow:hidden;background:#0B0C10}
section.featured a.card{position:absolute;inset:0;display:block;opacity:0;transition:opacity .7s ease;pointer-events:none;color:#F2F2F0;text-decoration:none}
section.featured a.card.on{opacity:1;pointer-events:auto}
section.featured a.card img{position:absolute;inset:0;width:100%;height:100%!important;max-width:none;object-fit:cover;display:block;transform:scale(1.04);transition:transform 7s ease}
section.featured a.card.on img{transform:scale(1)}
section.featured .lbl{position:absolute;left:20px;top:20px;max-width:min(520px,calc(100% - 40px));background:rgba(20,21,27,.88);padding:16px 20px 18px;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
section.featured .lbl .mono{color:#A3A6AE;margin:0 0 8px}
section.featured .lbl h3{font:300 clamp(20px,2.1vw,28px)/1.2 var(--sans);letter-spacing:-.015em;margin:0;color:#F2F2F0}
section.featured .lbl h3 i{font-style:normal;margin-left:8px;display:inline-block;transition:transform .2s}section.featured a.card:hover .lbl h3 i{transform:translate(3px,-3px)}
section.featured .bars{display:flex;gap:6px;margin-top:14px}section.featured .bars span{flex:1;height:2px;background:rgba(30,31,43,.14);position:relative;overflow:hidden}
section.featured .bars span b{position:absolute;inset:0;background:var(--ink);transform:scaleX(0);transform-origin:left}
section.featured .bars span.done b{transform:scaleX(1)}section.featured .bars span.run b{animation:fbar 6.5s linear forwards}
@keyframes fbar{to{transform:scaleX(1)}}
@media (max-width:820px){section.featured{padding:24px var(--gutter) 48px}section.featured .stage{aspect-ratio:4/5}section.featured .lbl{left:12px;top:12px;padding:12px 14px 14px}}
@media (prefers-reduced-motion:reduce){section.featured a.card,section.featured a.card img{transition:none}section.featured .bars span.run b{animation:none;transform:scaleX(1)}}
"""

JS = """<script>(function(){var r=document.getElementById('featured');if(!r)return;var cs=r.querySelectorAll('a.card'),bs=r.querySelectorAll('.chips button'),ps=r.querySelectorAll('.bars span'),i=0,t;
function show(k){i=k;cs.forEach(function(c,j){c.classList.toggle('on',j===k)});bs.forEach(function(b,j){b.setAttribute('aria-selected',j===k?'true':'false')});ps.forEach(function(p,j){p.className='';void p.offsetWidth;p.className=j<k?'done':(j===k?'run':'')})}
function next(){show((i+1)%cs.length)}function go(){clearInterval(t);if(!matchMedia('(prefers-reduced-motion: reduce)').matches)t=setInterval(next,6500)}
bs.forEach(function(b,j){b.addEventListener('click',function(){show(j);go()})});r.addEventListener('mouseenter',function(){clearInterval(t)});r.addEventListener('mouseleave',go);show(0);go()})();</script>"""


def html_block():
    chips = "".join(f'<button type="button" role="tab" aria-selected="{"true" if k == 0 else "false"}">{E(a)}</button>'
                    for k, (a, *_r) in enumerate(FEATURED))
    cards = "".join(f'<a class="card{" on" if k == 0 else ""}" href="{h}"><img src="assets/featured/{img}" alt="" width="1920" height="902" '
                    f'loading="{"eager" if k == 0 else "lazy"}" decoding="async"><div class="lbl"><p class="mono">{E(a)}</p>'
                    f'<h3>{E(t)}<i aria-hidden="true">↗</i></h3></div></a>' for k, (a, t, h, img) in enumerate(FEATURED))
    bars = "".join("<span><b></b></span>" for _ in FEATURED)
    return (f'<style>{CSS}</style><section class="featured" id="featured" aria-label="Featured"><div class="fw">'
            f'<div class="chips" role="tablist">{chips}</div><div class="stage">{cards}</div><div class="bars">{bars}</div></div></section>{JS}')
