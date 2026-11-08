"""Featured strip under the home hero (Umar, 6 Nov 2026): a Palantir style band of topic chips
over one large image card with a dark label box, scrolled sideways by hand, the next card in view. site_index.py calls
featured.html() between the hero film and the intro. Images and credits in assets/featured/.
"""
import html

E = lambda s: html.escape(str(s), quote=True)

# (eyebrow, headline, href relative to the home page, image in assets/featured/, chip label)
FEATURED = [
    ("Case Study · Sea Power", "Rebuilding Middle Eastern Sea Power", "co-build/defense-and-intelligence/", "sea-power.jpg", "Sea Power"),
    ("Case Study · Saudi Arabia", "Bringing Intelligence to Every Truck in Saudi Arabia", "open-pit-mine-haul-fleet-saudi-arabia/", "saudi-trucks.jpg", "Saudi Trucks"),
    ("On Device AI", "Deploying On Device AI Stacks to Defend Against Hardware Cyber Attacks", "developer/", "on-device.jpg", "On Device AI"),
    ("13 Industries", "Training Models for 13 Physical AI Industries", "sectors/", "thirteen-industries.jpg", "13 Industries"),
]

CSS = """
section.featured{background:#EDEDEB;color:var(--ink);padding:40px 0 64px;overflow:hidden}
section.featured .fhead{max-width:var(--max);margin:0 auto 22px;padding:0 var(--gutter);display:flex;align-items:center;gap:16px}
section.featured .chips{display:flex;flex-wrap:wrap;gap:8px}
section.featured .chips a{font:400 14.5px/1 var(--sans);color:var(--muted-l);background:#fff;padding:9px 12px;text-decoration:none;letter-spacing:-.005em}
section.featured .chips a:hover{color:var(--ink)}section.featured .chips a.on{color:var(--ink);background:linear-gradient(90deg,#DADAD8 calc(var(--p,0) * 100%),#fff calc(var(--p,0) * 100%))}

section.featured .nav{margin-left:auto;display:flex;gap:6px}
section.featured .nav button{width:36px;height:36px;border:1px solid var(--rule-l);background:#fff;color:var(--ink);cursor:pointer;display:grid;place-items:center;border-radius:0}
section.featured .nav button:disabled{opacity:.35;cursor:default}section.featured .nav svg{width:14px;height:14px}
section.featured .track{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:var(--gutter);padding:0 var(--gutter);scrollbar-width:none;-ms-overflow-style:none;cursor:grab}
section.featured .track::-webkit-scrollbar{display:none}section.featured .track.drag{cursor:grabbing;scroll-snap-type:none}
section.featured .card{position:relative;flex:0 0 min(94%,1180px);aspect-ratio:1920/902;overflow:hidden;background:#0B0C10;color:#F2F2F0;text-decoration:none;scroll-snap-align:start}
section.featured .card img{position:absolute;inset:0;width:100%;height:100%!important;max-width:none;object-fit:cover;display:block;transition:transform .8s ease;user-select:none;-webkit-user-drag:none}

section.featured .lbl{position:absolute;left:20px;top:20px;max-width:min(520px,calc(100% - 40px));background:rgba(20,21,27,.88);padding:16px 20px 18px;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
section.featured .lbl .mono{color:#A3A6AE;margin:0 0 8px}
section.featured .lbl h3{font:300 clamp(20px,2.1vw,28px)/1.2 var(--sans);letter-spacing:-.015em;margin:0;color:#F2F2F0}
@media (max-width:820px){section.featured{padding:24px 0 44px}section.featured .fhead{margin-bottom:16px;padding:0}section.featured .chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding:0 var(--gutter)}section.featured .chips::-webkit-scrollbar{display:none}section.featured .chips a{flex:none;font-size:14px;padding:9px 12px;white-space:nowrap}section.featured .nav{display:none}section.featured .track{gap:12px}section.featured .card{flex-basis:85%;aspect-ratio:2/3}section.featured .lbl{left:12px;top:12px;max-width:calc(100% - 24px);padding:12px 14px 14px}section.featured .lbl h3{font-size:19px}}
"""

JS = """<script>(function(){var r=document.getElementById('featured');if(!r)return;var t=r.querySelector('.track'),cs=[].slice.call(t.querySelectorAll('.card')),ch=[].slice.call(r.querySelectorAll('.chips a')),pv=r.querySelector('.prev'),nx=r.querySelector('.next');
function cur(){var x=t.scrollLeft,b=0,d=1e9;cs.forEach(function(c,i){var q=Math.abs(c.offsetLeft-t.offsetLeft-x-0);if(q<d){d=q;b=i}});return b}
function to(i){i=Math.max(0,Math.min(cs.length-1,i));t.scrollTo({left:cs[i].offsetLeft-cs[0].offsetLeft,behavior:'smooth'})}
function mark(){var i=cur();ch.forEach(function(a,j){a.classList.toggle('on',j===i)});pv.disabled=t.scrollLeft<4;nx.disabled=t.scrollLeft+t.clientWidth>=t.scrollWidth-4}
ch.forEach(function(a,j){a.addEventListener('click',function(e){e.preventDefault();to(j)})});pv.addEventListener('click',function(){to(cur()-1)});nx.addEventListener('click',function(){to(cur()+1)});
t.addEventListener('scroll',function(){requestAnimationFrame(mark)},{passive:true});
var down=false,sx=0,sl=0,moved=false;t.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;down=true;moved=false;sx=e.clientX;sl=t.scrollLeft});
window.addEventListener('pointermove',function(e){if(!down)return;var dx=e.clientX-sx;if(Math.abs(dx)>4){moved=true;t.classList.add('drag')}t.scrollLeft=sl-dx});
window.addEventListener('pointerup',function(){if(!down)return;down=false;if(moved){t.classList.remove('drag');to(cur())}});
var DWELL=3000,el=0,seen=false,still=matchMedia('(prefers-reduced-motion: reduce)').matches;
function touch(){el=0;paint()}function paint(){var i=cur();ch.forEach(function(a,j){a.style.setProperty('--p',j===i?Math.min(1,el/DWELL):0)})}
['wheel','touchstart','pointerdown','keydown'].forEach(function(ev){r.addEventListener(ev,touch,{passive:true})});ch.forEach(function(a){a.addEventListener('click',touch)});pv.addEventListener('click',touch);nx.addEventListener('click',touch);
if('IntersectionObserver' in window)new IntersectionObserver(function(es){seen=es[0].isIntersecting},{threshold:.4}).observe(t);else seen=true;
var lt=0;function loop(ts){var dt=lt?Math.min(ts-lt,100):0;lt=ts;if(seen&&!document.hidden&&!down){el+=dt;if(el>=DWELL){el=0;var i=cur();to(i>=cs.length-1?0:i+1)}paint()}requestAnimationFrame(loop)}if(!still)requestAnimationFrame(loop);
mark()})();</script>"""


# Palantir's scroll glide: a marked layer starts 100 px low at 70% opacity and rises to rest
# as it scrolls into view, faster than the band behind it, so the gap closes as you scroll.
RISE_JS = """<style>.shade{color:var(--muted-l)}</style><script>(function(){function init(){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var els=[].slice.call(document.querySelectorAll('[data-rise],main>section:not(.hero):not(.featured)>.wrap,main>section.film:not(.hero)>.inner'));if(!els.length)return;
var S=els.map(function(e){e.style.willChange='transform,opacity';e.style.transformOrigin='50% 0';
 var tx=[].slice.call(e.querySelectorAll('.big,h2')).map(function(t){var cs=getComputedStyle(t),lh=parseFloat(cs.lineHeight);if(isNaN(lh))lh=parseFloat(cs.fontSize)*1.15;return {el:t,lh:lh}});
 return {el:e,cur:-1,tgt:0,tx:tx,sh:[].slice.call(e.querySelectorAll('.shade'))}});
function ease(x){return 1-Math.pow(1-x,3)}
function paint(o){var p=o.cur,e=o.el;e.style.transform='translate3d(0,'+((1-p)*170).toFixed(1)+'px,0) scale('+(.95+.05*p).toFixed(4)+')';e.style.opacity=(.18+.82*p).toFixed(3);
 o.tx.forEach(function(t){t.el.style.lineHeight=(t.lh*(1+.3*(1-p))).toFixed(1)+'px'});o.sh.forEach(function(x){x.style.opacity=Math.max(0,Math.min(1,(p-.55)/.45)).toFixed(3)})}
function measure(){var vh=window.innerHeight;S.forEach(function(o){var top=o.el.parentElement.getBoundingClientRect().top;o.tgt=ease(Math.max(0,Math.min(1,(vh-top)/(vh*.9))));if(o.cur<0||document.hidden){o.cur=o.tgt;paint(o)}})}
var run=false;function loop(){var busy=false;S.forEach(function(o){var d=o.tgt-o.cur;if(Math.abs(d)>.0008){o.cur+=d*.11;busy=true;paint(o)}else if(d){o.cur=o.tgt;paint(o)}});if(busy)requestAnimationFrame(loop);else run=false}
function kick(){measure();if(!run&&!document.hidden){run=true;requestAnimationFrame(loop)}}
window.addEventListener('scroll',kick,{passive:true});window.addEventListener('resize',kick);measure()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init()})();</script>"""


def html_block():
    chips = "".join(f'<a href="#f{k}" class="{"on" if k == 0 else ""}">{E(a)}</a>' for k, (*_r, a) in enumerate(FEATURED))
    cards = "".join(f'<div class="card" id="f{k}"><img src="assets/featured/{img}" alt="" width="1920" height="902" '
                    f'loading="{"eager" if k < 2 else "lazy"}" decoding="async" draggable="false"><div class="lbl"><p class="mono">{E(a)}</p>'
                    f'<h3>{E(t)}</h3></div></div>' for k, (a, t, h, img, _c) in enumerate(FEATURED))
    arrow = lambda d: f'<svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="{d}" stroke="currentColor" stroke-width="1.2"/></svg>'
    nav = (f'<div class="nav"><button type="button" class="prev" aria-label="Previous">{arrow("M9 2 4 7l5 5")}</button>'
           f'<button type="button" class="next" aria-label="Next">{arrow("M5 2l5 5-5 5")}</button></div>')
    return (f'<style>{CSS}</style><section class="featured" id="featured" aria-label="Featured"><div data-rise><div class="fhead">'
            f'<div class="chips">{chips}</div>{nav}</div><div class="track">{cards}</div></div></section>{JS}{RISE_JS}')
