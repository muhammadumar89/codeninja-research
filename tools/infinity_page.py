"""Infinity Founders (Umar, 26 Nov 2026): a positioning page at /infinity-founders/ and a founder application
at /infinity-founders/apply/. Copy from Umar's "Infinity Founders Page Brief" (26 Nov 2026) with his three edits:
the section that compared us with partner programs states what Infinity Founders is (never what it is not), every
mention names CodeNinja Atoms, and applications go to hello@ through the same inbound route as the contact form
(the Lambda gives them the subject "Infinity Founders application"). The Praxis /infinity panel is a separate thing
and is not linked or touched from here.

Design: the site's physical AI language. Full bleed real world film bands (assets/video), the scroll rise
(featured.RISE_JS), rules that draw in, bars that fill to the PADI numbers and a step line that runs as you
reach it. Every primary button goes to the apply page.
    python tools/infinity_page.py
"""
import html, json, datetime
from pathlib import Path
import brand, featured

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
APPLY = f"{BASE}/infinity-founders/apply/"
TITLE = "Infinity Founders | CodeNinja Atoms"
DESC = "Build your forward deployed engineering company for physical AI. You lead. We build. We deliver."

# Proof band under the hero (Umar, 26 Nov 2026): the companies already launched, in Umar's numbers.
LAUNCHED = "We have already launched four companies with forward deployed engineering founders."
PROOF = [("4", "", "Companies launched with forward deployed engineering founders"),
         ("2", "$|M+", "Revenue a year, each company"),
         ("40", "|%", "Margin, each company")]

SELLS = [("Sovereign", "Open weights on hardware the customer owns, in their own country."),
         ("Air gapped", "Frontier AI inside the walls, with no data leaving the site."),
         ("Owned", "The operational intelligence becomes the customer's asset, not a vendor's.")]

GET = [("platforms", "Platforms", "The CodeNinja Atoms platforms, including Praxis for designing physical AI systems and the Hyper sovereign AI suite.", False),
       ("stack", "Stack and tools", "Open reference architectures across 13 industries, object models, and the delivery tooling our own engineers use.", False),
       ("hardware", "Hardware technologies", "Edge devices built for physical sites, designed to run AI where the work happens.", False),
       ("services", "CodeNinja Atoms services capabilities", "Our engineering teams, working under your leadership on your accounts. This is the most important thing we bring.", True),
       ("sales", "Sales engine", "The playbooks, pipeline systems and go to market machinery we use to win physical AI customers.", False),
       ("investment", "Investment", "Capital to help you launch and roll out, so the first customer is not limited by your balance sheet.", False)]

STEPS = [("Apply.", "Tell us who you are, the industry you know and the region you want to serve."),
         ("Shape your company.", "Together we pick your vertical, your first target accounts and your offer."),
         ("Win your first major customer.", "CodeNinja Atoms engineering teams work under your leadership to design, pitch and close it."),
         ("Roll it out together.", "We deploy side by side, then you scale on the same platform with each new customer.")]

COMPARE = [("Resell a vendor's product", "Build and own your company"),
           ("Vendor owns the customer", "You own the customer"),
           ("Margin on licences", "All revenue is yours"),
           ("Support tickets", "Our engineers under your leadership"),
           ("No capital", "Investment to launch and roll out")]

LOOKING = ["Deep experience in a physical industry such as energy, oil and gas, mining, manufacturing, logistics, utilities, agriculture or infrastructure.",
           "Relationships with operators in your region.",
           "The drive to build and run a company, technical or commercial.",
           "No fully formed idea required. We will shape it with you."]

FAQ = [("Do I need a technical background?", "No. You need industry depth and the will to lead. Our engineers bring the delivery."),
       ("Who owns the customer contract?", "Your company does."),
       ("How does CodeNinja Atoms make money?", "Through services margins on the engineering work we deliver for you."),
       ("What kind of investment is available?", "Capital to support your launch and first rollout, agreed founder by founder."),
       ("Where can I operate?", "Anywhere. We want forward deployed engineering companies in every region."),
       ("What do I sell?", "Sovereign, air gapped AI systems that let organizations build and own their operational intelligence.")]

INDUSTRIES = ["Energy", "Oil and gas", "Mining", "Manufacturing", "Semiconductors", "Logistics and transport", "Utilities", "Agriculture",
              "Infrastructure and construction", "Healthcare operations", "Defense and government", "Other"]


def padi_numbers():
    """The headline blind result from the PADI export, so the proof strip never drifts from /padi/."""
    try:
        import padi
        b = (padi.load() or {}).get("blind") or {}
        n = b.get("checks_total")
        if n:
            return round(100 * b["platform"] / n, 1), round(100 * b["bare"] / n, 1)
    except Exception:
        pass
    return 48.5, 28.4


CSS = """
.ifp{--ifw:var(--max)}
.ifp .wrap{max-width:var(--max);margin:0 auto;padding:128px var(--gutter)}
.ifp .eyebrow,.ifp .mono{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin:0}
.ifp section.film.hero.bright::after{background:linear-gradient(180deg,rgba(11,12,16,.55) 0%,rgba(11,12,16,.38) 30%,rgba(11,12,16,.42) 70%,rgba(11,12,16,.7) 100%)}
.ifp section.film.hero .mono{color:rgba(242,242,240,.85)}
section.film.hero .hero-line{font-family:var(--sans);font-weight:300;font-size:clamp(22px,2.4vw,32px);letter-spacing:-.02em;color:var(--on-dark);margin:22px auto 0;max-width:none}
section.film.hero .support{max-width:58ch;margin:18px auto 0;color:rgba(242,242,240,.82);font-size:clamp(15px,1.35vw,18px);line-height:1.55}
section.film.hero .cta{justify-content:center}
/* proof band: what is already running */
.ifp .launched{max-width:var(--max);margin:0 auto;padding:136px var(--gutter) 128px}
.ifp .launched .big{font-family:var(--sans);font-weight:300;font-size:clamp(30px,4vw,56px);line-height:1.1;letter-spacing:-.03em;max-width:24ch;margin:22px 0 0;color:var(--ink)}
.ifp .nums{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 32px;margin-top:88px}
.ifp .nums>div{padding-top:22px}
.ifp .nums b{display:block;font-family:var(--sans);font-weight:300;font-size:clamp(72px,9vw,140px);line-height:.92;letter-spacing:-.05em;color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
.ifp .nums b small{font-size:.5em;letter-spacing:-.03em;vertical-align:.62em;margin:0 .04em}
.ifp .nums span{display:block;margin-top:20px;font-family:var(--mono);font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--muted-l);max-width:26ch;line-height:1.55}
.ifp .nums>div:nth-child(2)::before{transition-delay:.15s}.ifp .nums>div:nth-child(3)::before{transition-delay:.3s}
/* statement */
.ifp .stmt{text-align:center;max-width:var(--max);margin:0 auto;padding:152px var(--gutter) 136px}
.ifp .stmt h2{margin:18px auto 0;max-width:20ch;font-weight:300;font-size:clamp(34px,4.8vw,68px);line-height:1.04}
.ifp .stmt p.body{font-family:var(--serif);font-weight:300;font-size:clamp(19px,1.9vw,25px);line-height:1.5;color:var(--muted-l);max-width:46ch;margin:40px auto 0}
.ifp .stmt p.body b{font-weight:400;color:var(--ink)}
/* film bands with two columns */
.ifp section.film .inner.two{display:grid;grid-template-columns:1fr 1fr;gap:32px 64px;align-items:end;padding-bottom:96px}
.ifp section.film .inner.two h2{margin:.3em 0 0}
.ifp section.film.band{min-height:78vh}
/* head row */
.ifp .head{display:grid;grid-template-columns:1fr 1fr;gap:24px 64px;align-items:end;padding-bottom:44px;margin-bottom:56px;border-bottom:1px solid var(--rule-l)}
.ifp .head h2{margin:.35em 0 0}.ifp .head p{margin:0;color:var(--muted-l);font-size:17px;line-height:1.62;max-width:56ch}
/* rule that draws in */
.ifp .draw{position:relative}.ifp .draw::before{content:"";position:absolute;left:0;top:0;height:1px;width:100%;background:var(--ink);transform-origin:0 50%;transform:scaleX(0);transition:transform 1.1s cubic-bezier(.2,.7,.2,1)}
.ifp .in .draw::before,.ifp .draw.in::before{transform:scaleX(1)}html:not(.js) .ifp .draw::before{transform:scaleX(1)}
/* what your company sells */
.ifp .three{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 32px}
.ifp .three>div{padding-top:22px}.ifp .three .n{font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted-l)}
.ifp .three h3{font-weight:300;font-size:clamp(30px,3vw,44px);letter-spacing:-.03em;line-height:1.05;margin:26px 0 14px;color:var(--ink)}
.ifp .three p{margin:0;color:var(--muted-l);font-size:16px;line-height:1.6;max-width:34ch}
.ifp .three>div:nth-child(2)::before{transition-delay:.15s}.ifp .three>div:nth-child(3)::before{transition-delay:.3s}
/* what you get: image cards */
.ifp .gets{display:grid;grid-template-columns:repeat(3,1fr);gap:48px 28px}
.ifp .get{display:flex;flex-direction:column;color:var(--ink)}
.ifp .get .im{position:relative;aspect-ratio:8/5;overflow:hidden;background:#111;margin-bottom:22px}
.ifp .get img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.9);transform:scale(1.06);transition:transform 1.6s cubic-bezier(.2,.7,.2,1),filter .6s}
.ifp .in .get img,.ifp .get.in img{transform:scale(1)}.ifp .get:hover img{transform:scale(1.03);filter:saturate(1)}
.ifp .get .n{font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted-l);margin:0 0 10px}
.ifp .get h3{font-weight:400;font-size:clamp(20px,1.7vw,24px);letter-spacing:-.02em;line-height:1.2;margin:0 0 10px}
.ifp .get p{margin:0;color:var(--muted-l);font-size:15.5px;line-height:1.6}
.ifp .get.key .im::after{content:"Most important";position:absolute;left:14px;top:14px;font:400 10.5px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;background:var(--red);color:#fff;padding:7px 9px}
.ifp .get.key h3{font-weight:500}
/* proof strip */
.ifp .proof{margin-top:88px;padding-top:28px;border-top:1px solid var(--ink);display:grid;grid-template-columns:5fr 7fr;gap:24px 64px;align-items:center}
.ifp .proof p{margin:0;font-size:15px;line-height:1.6;color:var(--muted-l);max-width:52ch}.ifp .proof p a{color:var(--ink)}
.ifp .bars{display:grid;gap:14px}.ifp .bar{display:grid;grid-template-columns:150px 1fr 64px;gap:16px;align-items:center;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.ifp .bar i{display:block;height:10px;background:rgba(30,31,43,.08);position:relative;overflow:hidden}
.ifp .bar i::after{content:"";position:absolute;inset:0 auto 0 0;width:var(--w);background:var(--ink);transform-origin:0 50%;transform:scaleX(0);transition:transform 1.6s cubic-bezier(.2,.7,.2,1) .2s}
.ifp .bar.f i::after{background:#A3A6AE}.ifp .proof.in .bar i::after{transform:scaleX(1)}html:not(.js) .ifp .bar i::after{transform:scaleX(1)}
.ifp .bar b{font:300 24px/1 var(--sans);letter-spacing:-.03em;color:var(--ink);text-transform:none;text-align:right;font-variant-numeric:tabular-nums}
/* how it works: dark, a line that runs */
.ifp .how{background:var(--night);color:var(--on-dark)}
.ifp .how .head{border-bottom-color:var(--rule-d)}.ifp .how .head p{color:var(--muted-d)}.ifp .how .eyebrow{color:var(--muted-d)}
.ifp .steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:40px 28px;position:relative;counter-reset:s}
.ifp .steps::before{content:"";position:absolute;left:0;right:0;top:5px;height:1px;background:var(--rule-d)}
.ifp .steps::after{content:"";position:absolute;left:0;right:0;top:5px;height:1px;background:var(--red);transform-origin:0 50%;transform:scaleX(0);transition:transform 2.4s cubic-bezier(.3,.6,.2,1)}
.ifp .steps.in::after{transform:scaleX(1)}html:not(.js) .ifp .steps::after{transform:scaleX(1)}
.ifp .steps li{position:relative;padding-top:44px;opacity:.35;transition:opacity .8s}.ifp .steps.in li{opacity:1}
.ifp .steps.in li:nth-child(2){transition-delay:.6s}.ifp .steps.in li:nth-child(3){transition-delay:1.2s}.ifp .steps.in li:nth-child(4){transition-delay:1.8s}
.ifp .steps li::before{content:"";position:absolute;left:0;top:0;width:11px;height:11px;border-radius:50%;background:var(--night);border:1px solid var(--on-dark);transition:background .6s}
.ifp .steps.in li::before{background:var(--red);border-color:var(--red)}
.ifp .steps.in li:nth-child(2)::before{transition-delay:.6s}.ifp .steps.in li:nth-child(3)::before{transition-delay:1.2s}.ifp .steps.in li:nth-child(4)::before{transition-delay:1.8s}
.ifp .steps .n{font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--muted-d)}
.ifp .steps h3{font-weight:400;font-size:clamp(22px,2vw,28px);letter-spacing:-.025em;line-height:1.15;margin:14px 0 12px}
.ifp .steps p{margin:0;color:var(--muted-d);font-size:15.5px;line-height:1.6}
.ifp .how .cta{margin-top:72px}
/* comparison */
.ifp .cmp{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--ink)}
.ifp .cmp>div{padding:18px 24px 18px 0;border-bottom:1px solid var(--rule-l);font-size:17px;letter-spacing:-.01em;line-height:1.4}
.ifp .cmp>div:nth-child(odd){color:var(--muted-l)}.ifp .cmp>div:nth-child(even){color:var(--ink);padding-left:24px;border-left:1px solid var(--rule-l);background:rgba(30,31,43,.035)}
.ifp .cmp .th{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;padding-top:16px;padding-bottom:16px}
.ifp .cmp .th:nth-child(2){background:var(--ink);color:var(--paper)}
/* who we look for */
.ifp .split{display:grid;grid-template-columns:1fr 1fr;gap:48px 64px;align-items:start}
.ifp .list{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink)}
.ifp .list li{padding:20px 0 20px 34px;border-bottom:1px solid var(--rule-l);color:var(--ink);font-size:17px;line-height:1.5;letter-spacing:-.008em;position:relative}
.ifp .list li::before{content:"";position:absolute;left:0;top:29px;width:14px;height:1px;background:var(--red)}
/* faq */
.ifp .faq details{border-top:1px solid var(--rule-l);padding:20px 0}.ifp .faq details:last-child{border-bottom:1px solid var(--rule-l)}
.ifp .faq summary{cursor:pointer;font-size:19px;letter-spacing:-.012em;color:var(--ink);list-style:none}.ifp .faq summary::-webkit-details-marker{display:none}
.ifp .faq summary::after{content:"+";float:right;color:var(--muted-l)}.ifp .faq details[open] summary::after{content:"\\2212"}
.ifp .faq p{margin:12px 0 0;color:var(--muted-l);font-size:16px;line-height:1.6;max-width:62ch}
/* closing */
.ifp section.film.close{min-height:86vh;align-items:center;text-align:center}
.ifp section.film.close .inner{display:flex;flex-direction:column;align-items:center;padding:140px var(--gutter)}
.ifp section.film.close h2{max-width:20ch;margin:.4em auto 0;font-weight:300;font-size:clamp(36px,5vw,72px)}
.ifp section.film.close .cta{justify-content:center;margin-top:40px}
@media (max-width:1000px){.ifp .gets{grid-template-columns:repeat(2,1fr)}.ifp .steps{grid-template-columns:repeat(2,1fr)}.ifp .steps::before,.ifp .steps::after{display:none}
.ifp .steps li{border-top:1px solid var(--rule-d);padding-top:28px}.ifp .steps li::before{top:-6px}}
@media (max-width:820px){.ifp .nums{grid-template-columns:1fr;gap:48px;margin-top:56px}.ifp .launched{padding:96px var(--gutter) 88px}.ifp .wrap{padding:88px var(--gutter)}.ifp .stmt{padding:104px var(--gutter) 96px}
.ifp .head,.ifp .split,.ifp .proof,.ifp section.film .inner.two{grid-template-columns:1fr}.ifp .three{grid-template-columns:1fr}
.ifp .gets{grid-template-columns:1fr;gap:44px}.ifp .steps{grid-template-columns:1fr}
.ifp .bar{grid-template-columns:96px 1fr 52px;gap:10px}.ifp .bar b{font-size:20px}
.ifp .cmp>div{font-size:15px;padding:14px 12px 14px 0}.ifp .cmp>div:nth-child(even){padding-left:12px}
.ifp section.film .inner.two{padding-bottom:72px}}
"""

# Marks a section "in" once it is on screen: the rules draw, the bars fill, the step line runs. Without JS
# (or with reduced motion) everything shows at rest.
REVEAL = """<script>(function(){var els=document.querySelectorAll('.ifp .draw,.ifp .proof,.ifp .steps,.ifp .get');
if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.35,rootMargin:'0px 0px -8% 0px'});
els.forEach(function(e){io.observe(e)});
var ns=document.querySelectorAll('.ifp .nums [data-to]');var nio=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;nio.unobserve(e.target);
var el=e.target,to=+el.getAttribute('data-to'),t0=null,D=1400;el.textContent='0';function step(t){if(!t0)t0=t;var x=Math.min(1,(t-t0)/D),v=Math.round(to*(1-Math.pow(1-x,3)));el.textContent=v;if(x<1)requestAnimationFrame(step)}requestAnimationFrame(step)})},{threshold:.5});
ns.forEach(function(n){nio.observe(n)})})();</script>"""


def film(video, inner, cls="", sid="", eager=False, tail=""):
    v = f"{BASE}/assets/video/{video}"
    return (f'<section class="film {cls}"{f" id={chr(34)}{sid}{chr(34)}" if sid else ""}><img class="poster" src="{v}.jpg" alt="" aria-hidden="true">'
            f'<video autoplay muted loop playsinline preload="{"auto" if eager else "none"}" poster="{v}.jpg" aria-hidden="true"><source src="{v}.mp4" type="video/mp4"></video>'
            f'<div class="inner{" two" if "band" in cls.split() else ""}">{inner}</div>{tail}</section>')


def head(eyebrow, h2, body=""):
    return (f'<div class="head" data-rise><div><p class="eyebrow">{E(eyebrow)}</p><h2>{E(h2)}</h2></div>'
            + (f'<p>{E(body)}</p>' if body else "<p></p>") + '</div>')


def shell(path, title, desc, body, ld, og_image, extra_css=""):
    today = datetime.date.today().isoformat()
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}/assets/video/{og_image}.jpg"><meta name="twitter:card" content="summary_large_image">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}{extra_css}</style></head>
<body>{brand.header(BASE + "/", brand.nav(BASE + "/"))}
{body}
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Updated {today}</span><span><a href="{BASE}/assets/video/CREDITS.md">Video credits</a></span></div></footer>
{brand.SCRIPT}</body></html>"""


def main_page():
    p, f = padi_numbers()
    apply_btn = f'<a class="btn solid" href="{APPLY}">Apply as a founder</a>'
    sells = "".join(f'<div class="draw"><span class="n">0{i + 1}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(SELLS))
    gets = "".join(f'<article class="get{" key" if key else ""}"><div class="im"><img src="{BASE}/assets/infinity/{img}.jpg" alt="" loading="lazy" decoding="async" width="960" height="600"></div>'
                   f'<p class="n">0{i + 1}</p><h3>{E(t)}</h3><p>{E(d)}</p></article>' for i, (img, t, d, key) in enumerate(GET))
    def num(n, fix, label):
        pre, post = (fix.split("|") + [""])[:2] if fix else ("", "")
        return (f'<div class="draw"><b>{f"<small>{E(pre)}</small>" if pre else ""}<em data-to="{n}" style="font-style:normal">{n}</em>'
                f'{f"<small>{E(post)}</small>" if post else ""}</b><span>{E(label)}</span></div>')
    nums = "".join(num(*x) for x in PROOF)
    steps = "".join(f'<li><span class="n">0{i + 1}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d) in enumerate(STEPS))
    cmp = ('<div class="th">Partner program</div><div class="th">Infinity Founders</div>'
           + "".join(f'<div>{E(a)}</div><div>{E(b)}</div>' for a, b in COMPARE))
    looking = "".join(f'<li>{E(x)}</li>' for x in LOOKING)
    faq = "".join(f'<details{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(FAQ))
    body = f"""<main class="ifp">
{film("infinity-field", f'<p class="mono">Infinity Founders</p><h1 class="lite">Build your forward deployed engineering company for physical AI.</h1><p class="hero-line">You lead. We build. We deliver.</p><p class="support">CodeNinja Atoms backs founders with the platforms, hardware, engineers and capital to bring sovereign, air gapped AI into every organization in the world.</p><div class="cta">{apply_btn}<a class="btn" href="#how">How it works</a></div>', cls="hero bright", eager=True, tail=f'<a class="scroll" href="#launched">Scroll to explore{brand.ARROW}</a>')}

<section class="light" id="launched"><div class="launched" data-rise><p class="eyebrow">Already in the field</p><p class="big">{E(LAUNCHED)}</p>
<div class="nums">{nums}</div></div></section>

<section class="light alt" id="problem"><div class="stmt" data-rise><p class="eyebrow">The problem</p><h2>Intelligence is here. Deployment is the bottleneck.</h2>
<p class="body">Frontier AI can already reason about plants, grids, mines, fleets and factories. What it cannot do on its own is walk onto a site, understand the systems of record, and earn the trust of the people who run the operation. If organizations are not helped to transform with AI, the result will be massive job loss, most of all in physical industries. <b>The answer is not one company. It is hundreds of forward deployed engineering companies, each rooted in an industry and a region, taking this intelligence into the field.</b></p></div></section>

{film("pragma-wall", '<div><p class="mono">The mission</p><h2>Hundreds of founders. Every organization in the world.</h2></div><div><p class="lede">Infinity Founders exists to create the companies that will carry AI into physical operations. We believe this market will be winner take all, and we want the winners to be founders who own their companies and their customers, built on open, sovereign foundations.</p></div>', cls="band", sid="mission")}

<section class="light" id="sell"><div class="wrap">{head("What your company sells", "Air gapped AI that every organization owns.", "Your company helps organizations build their own operational intelligence and keep it. The models run where the data lives, on hardware the customer owns, with no internet connection required. Systems of record are read, never overwritten. Agents draft, named people approve. The customer owns the ontology, the models and the outcomes.")}
<div class="three">{sells}</div></div></section>

<section class="light alt" id="get"><div class="wrap">{head("What you get", "Everything CodeNinja Atoms has built, behind your company.")}
<div class="gets">{gets}</div>
<div class="proof"><p>On the Physical AI Design Index, Praxis passed {p} percent of checks against {f} percent for frontier AI alone in a blind evaluation on unseen tasks. <a href="{BASE}/padi/">Explore the benchmark</a></p>
<div class="bars" role="img" aria-label="Checks passed in the blind evaluation: Praxis {p} percent, frontier AI alone {f} percent"><div class="bar"><span>Praxis</span><i style="--w:{p}%"></i><b>{p}%</b></div><div class="bar f"><span>Frontier AI alone</span><i style="--w:{f}%"></i><b>{f}%</b></div></div></div></div></section>

<section class="how" id="how"><div class="wrap">{head("How it works", "You lead. We build. We deliver.")}
<ol class="steps">{steps}</ol><div class="cta">{apply_btn}</div></div></section>

{film("port-night", '<div><p class="mono">The economics</p><h2>Your company. Your customers. Your revenue.</h2></div><div><p class="lede">You own the company, the customer relationships and all of the revenue. CodeNinja Atoms earns services margins on the engineering work we deliver for you. Nothing more.</p></div>', cls="band", sid="economics")}

<section class="light" id="companies"><div class="wrap">{head("Built to own", "Infinity Founders builds companies.", "You are the founder and the CEO. CodeNinja Atoms is the platform, the engineering bench and the capital behind you.")}
<div class="cmp" role="table" aria-label="Partner program compared with Infinity Founders">{cmp}</div></div></section>

<section class="light alt" id="who"><div class="wrap"><div class="split" data-rise><div><p class="eyebrow">Who we are looking for</p><h2>Founders who know an industry from the inside.</h2><div class="cta"><a class="btn solid" href="{APPLY}">Apply as a founder</a></div></div>
<ul class="list">{looking}</ul></div></div></section>

<section class="light" id="faq"><div class="wrap"><div class="split"><div><p class="eyebrow">Questions</p><h2>What founders ask first.</h2></div><div class="faq">{faq}</div></div></div></section>

{film("infinity-field", f'<p class="mono">Infinity Founders</p><h2>The world needs hundreds of these companies. Build one of them.</h2><div class="cta">{apply_btn}</div>', cls="close", sid="apply")}
</main>
{featured.RISE_JS}{REVEAL}"""
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": TITLE, "url": f"{BASE}/infinity-founders/", "description": DESC,
           "isPartOf": {"@id": f"{BASE}/#website"}, "publisher": {"@id": f"{BASE}/#org"},
           "potentialAction": {"@type": "ApplyAction", "name": "Apply as a founder", "target": APPLY}},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "CodeNinja Atoms", "item": f"{BASE}/"},
              {"@type": "ListItem", "position": 2, "name": "Infinity Founders", "item": f"{BASE}/infinity-founders/"}]}]
    return shell("/infinity-founders/", TITLE, DESC, body.replace(f"{BASE}/assets/", "../assets/"), ld, "infinity-field")


ACSS = """
.apply{max-width:var(--max);margin:0 auto;padding:168px var(--gutter) 120px;display:grid;grid-template-columns:4fr 7fr;gap:72px;align-items:start}
.apply h1{font-weight:300;font-size:clamp(40px,5vw,72px);line-height:1.02;letter-spacing:-.035em;margin:.25em 0 .4em}
.apply .lede{font-family:var(--serif);font-weight:300;font-size:clamp(19px,1.8vw,24px);line-height:1.45;color:var(--on-dark);margin:0 0 36px;max-width:32ch}
.apply .aside{border-top:1px solid var(--rule-d);padding-top:20px;font-size:15px;line-height:1.6;color:var(--muted-d);max-width:40ch}.apply .aside a{color:var(--on-dark)}
.apply .side{position:sticky;top:120px}
.apply .side .ph{position:relative;aspect-ratio:4/3;overflow:hidden;margin:40px 0 0;border:1px solid var(--rule-d)}
.apply .side .ph video,.apply .side .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
form.access fieldset{border:0;margin:0;padding:0;min-width:0;display:flex;flex-direction:column;gap:10px}
form.access legend{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-d);padding:0;margin:0 0 10px}
form.access .opts{display:flex;flex-wrap:wrap;gap:8px}
form.access .opts label{flex-direction:row;align-items:center;gap:0;font:400 14px/1 var(--sans);letter-spacing:0;text-transform:none;color:var(--on-dark);cursor:pointer}
form.access .opts input{position:absolute;opacity:0;width:1px;height:1px;padding:0;margin:0}
form.access .opts span{display:inline-block;padding:11px 14px;border:1px solid var(--rule-d);background:rgba(11,12,16,.55);transition:border-color .2s,background .2s}
form.access .opts label:hover span{border-color:var(--on-dark)}form.access .opts input:checked+span{background:var(--on-dark);color:var(--night);border-color:var(--on-dark)}
form.access .opts input:focus-visible+span{outline:1px solid var(--red);outline-offset:2px}
form.access .req::after{content:" *";color:var(--red)}form.access label>span.req{display:block}
form.access .count{font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;color:var(--muted-d);text-align:right;margin-top:-4px}
form.access label.consent{grid-column:1/-1;flex-direction:row;align-items:flex-start;gap:12px;font:400 14px/1.5 var(--sans);letter-spacing:0;text-transform:none;color:var(--muted-d);cursor:pointer}
form.access label.consent input{width:18px;height:18px;flex:0 0 18px;margin-top:2px;padding:0;-webkit-appearance:checkbox;appearance:auto;accent-color:var(--red)}
form.access .ifyes[hidden]{display:none}
@media (max-width:900px){.apply{grid-template-columns:1fr;gap:40px;padding:120px var(--gutter) 80px}.apply .side{position:static}.apply .side .ph{display:none}}
@media (max-width:560px){form.access{grid-template-columns:1fr}}
"""


def radios(name, label, options, required=True):
    req = " required" if required else ""
    return (f'<fieldset class="full"><legend class="{"req" if required else ""}">{E(label)}</legend><div class="opts">'
            + "".join(f'<label><input type="radio" name="{name}" value="{E(o)}"{req if i == 0 else ""}><span>{E(o)}</span></label>' for i, o in enumerate(options))
            + '</div></fieldset>')


def apply_page():
    opts = "".join(f'<option>{E(x)}</option>' for x in INDUSTRIES)
    form = f"""<form class="access" id="founder-form" novalidate>
<label><span class="req">Full name</span><input name="fullname" required autocomplete="name" maxlength="120"></label>
<label><span class="req">Email</span><input name="email" type="email" required autocomplete="email" maxlength="200"></label>
<label><span class="req">LinkedIn profile URL</span><input name="linkedin" type="url" required inputmode="url" placeholder="https://www.linkedin.com/in/" maxlength="300"></label>
<label><span class="req">Country and city</span><input name="location" required autocomplete="address-level2" maxlength="160"></label>
<label class="full"><span class="req">Current role and company</span><input name="rolecompany" required autocomplete="organization-title" maxlength="160" placeholder="For example: Head of operations, a national grid operator"></label>
<label><span class="req">Industry you know best</span><select name="industry" required><option value="">Choose one</option>{opts}</select></label>
<label><span class="req">Region you want to serve</span><input name="region" required maxlength="160" placeholder="For example: Gulf, Texas, East Africa"></label>
{radios("background", "Background", ["Technical", "Commercial", "Operator", "Mixed"])}
{radios("customer", "Do you have a first customer in mind?", ["Yes", "Not yet"], required=False)}
<label class="full ifyes" hidden>If yes, describe the organization and the problem<textarea name="customerdesc" maxlength="1000"></textarea></label>
{radios("fulltime", "Are you building full time?", ["Yes", "Within 3 months", "Exploring"], required=False)}
{radios("investment", "Will you need investment to launch?", ["Yes", "No", "Not sure"], required=False)}
<label class="full"><span class="req">Why you, and why this industry?</span><textarea name="why" required maxlength="1000"></textarea><span class="count" data-for="why">0 / 1000</span></label>
<label class="consent"><input type="checkbox" name="consent" required><span>I agree to be contacted by CodeNinja Atoms about my application.</span></label>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<p class="status" role="status" aria-live="polite"></p>
<button type="submit" data-label="Submit application">Submit application</button>
<p class="note">Goes straight to the Infinity Founders team. Nothing is published, and we only use your details to review your application and reply.</p>
</form>"""
    # The Lambda takes name, email, company, role and message; every other answer rides in the message, one per line.
    fields = ("{kind:'infinity-founders',name:f.fullname.value,email:f.email.value,company:f.rolecompany.value,role:f.industry.value+' · '+f.region.value,"
              "message:['Infinity Founders application','','LinkedIn: '+f.linkedin.value,'Country and city: '+f.location.value,'Current role and company: '+f.rolecompany.value,"
              "'Industry: '+f.industry.value,'Region to serve: '+f.region.value,'Background: '+v('background'),'First customer in mind: '+(v('customer')||'not answered'),"
              "(f.customerdesc.value&&v('customer')==='Yes'?'First customer: '+f.customerdesc.value:null),'Building full time: '+(v('fulltime')||'not answered'),'Needs investment: '+(v('investment')||'not answered'),"
              "'','Why you, and why this industry?',f.why.value,'','Consent to be contacted: yes'].filter(function(x){return x!==null}).join('\\n')}")
    sent = ('<div class="sent"><p class="eyebrow">Received</p><h3>Thank you. Your application is with the Infinity Founders team.</h3>'
            '<p>We will be in touch within two weeks.</p></div>')
    script = brand.post_script("founder-form", fields, sent=sent)
    # Before the shared submit handler: radio reader, the conditional field, the character count, and the browser's own
    # validation shown on submit (the form is novalidate so the page controls the order of messages).
    pre = """<script>function v(n){var x=document.querySelector('#founder-form input[name="'+n+'"]:checked');return x?x.value:''}
(function(){var f=document.getElementById('founder-form');if(!f)return;var y=f.querySelector('.ifyes');
f.querySelectorAll('input[name=customer]').forEach(function(r){r.addEventListener('change',function(){y.hidden=v('customer')!=='Yes'})});
var w=f.why,c=f.querySelector('.count');w.addEventListener('input',function(){c.textContent=w.value.length+' / 1000'});
f.addEventListener('submit',function(e){var s=f.querySelector('.status');if(!f.checkValidity()){e.preventDefault();e.stopImmediatePropagation();
var bad=f.querySelector(':invalid');s.textContent='Please complete every required field'+(bad&&bad.name==='consent'?', including consent to be contacted.':'.');if(bad)bad.focus();if(f.reportValidity)f.reportValidity()}},true)})();</script>"""
    body = f"""<main><div class="apply">
<div class="side"><p class="eyebrow">Infinity Founders</p><h1>Apply to Infinity Founders</h1>
<p class="lede">Tell us about you and the industry you want to transform. We read every application and reply within two weeks.</p>
<p class="aside">You lead. We build. We deliver. <a href="{BASE}/infinity-founders/">Read how Infinity Founders works</a>.</p>
<div class="ph"><img src="{BASE}/assets/video/infinity-field.jpg" alt="" aria-hidden="true"><video autoplay muted loop playsinline preload="auto" poster="{BASE}/assets/video/infinity-field.jpg" aria-hidden="true"><source src="{BASE}/assets/video/infinity-field.mp4" type="video/mp4"></video></div></div>
<div>{form}</div>
</div></main>
{pre}{script}"""
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Apply to Infinity Founders", "url": APPLY,
           "description": "Apply to Infinity Founders: tell us about you and the industry you want to transform. We read every application and reply within two weeks.",
           "isPartOf": {"@id": f"{BASE}/#website"}, "publisher": {"@id": f"{BASE}/#org"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "CodeNinja Atoms", "item": f"{BASE}/"},
              {"@type": "ListItem", "position": 2, "name": "Infinity Founders", "item": f"{BASE}/infinity-founders/"},
              {"@type": "ListItem", "position": 3, "name": "Apply", "item": APPLY}]}]
    return shell("/infinity-founders/apply/", "Apply to Infinity Founders | CodeNinja Atoms",
                 "Apply to Infinity Founders. Tell us about you and the industry you want to transform. We read every application and reply within two weeks.",
                 body.replace(f"{BASE}/assets/", "../../assets/"), ld, "infinity-field", ACSS)


def main():
    d = ROOT / "infinity-founders"
    (d / "apply").mkdir(parents=True, exist_ok=True)
    a, b = main_page(), apply_page()
    (d / "index.html").write_text(a, encoding="utf-8")
    (d / "apply" / "index.html").write_text(b, encoding="utf-8")
    print("infinity-founders/index.html", len(a), "· infinity-founders/apply/index.html", len(b))


if __name__ == "__main__":
    main()
