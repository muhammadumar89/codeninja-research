"""Rebuild the crawlable index for every paper in this repository: the research
index page (index.html at the repo root, served by GitHub Pages), sitemap.xml
and llms.txt. Run after adding or changing a paper folder.

    python tools/site_index.py
"""
import datetime
import html
import json
import re
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import brand

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"


def papers():
    out = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and (p / "index.html").exists() and (p / "paper").is_dir() and not p.name.startswith(".")):
        h = (d / "index.html").read_text(encoding="utf-8")
        g = lambda name: (re.search(rf'<meta name="{name}" content="([^"]*)"', h) or [None, ""])[1]
        pdf = next(iter(sorted((d / "paper").glob("*.pdf"))), None) if (d / "paper").exists() else None
        out.append({"slug": d.name, "title": html.unescape(g("citation_title")),
                    "description": html.unescape((re.search(r'<meta property="og:description" content="([^"]*)"', h) or [None, ""])[1]),
                    "date": g("citation_publication_date").replace("/", "-"), "doi": g("citation_doi"),
                    "pdf": f"{BASE}/{d.name}/paper/{pdf.name}" if pdf else "",
                    "ontology": f"{BASE}/{d.name}/ontology/objects.json" if (d / "ontology" / "objects.json").exists() else "",
                    **_pkg(d)})
    return sorted(out, key=lambda p: p["date"], reverse=True)


def _pkg(d):
    f = d / "ontology" / "objects.json"
    if not f.exists():
        return {"country": "", "sector": "", "n_obj": 0, "n_link": 0}
    j = json.loads(f.read_text(encoding="utf-8")); o = j.get("objects", [])
    return {"country": j.get("country", ""), "sector": j.get("sector", "").replace("-", " "),
            "n_obj": len(o), "n_link": sum(len(x.get("links", [])) for x in o)}


def solutions():
    """Solutions to published requirements: solutions/<slug>/meta.json with title, issuer_class,
    country, sector, summary, date, and optional url, pdf, doi."""
    out = []
    root = ROOT / "solutions"
    if root.is_dir():
        for d in sorted(root.iterdir()):
            if (d / "meta.json").exists():
                m = json.loads((d / "meta.json").read_text(encoding="utf-8")); m["slug"] = d.name; out.append(m)
    return sorted(out, key=lambda m: m.get("date", ""), reverse=True)


CSS = """.faq details{border-top:1px solid var(--rule-l);padding:18px 0}.faq details:last-child{border-bottom:1px solid var(--rule-l)}.faq summary{cursor:pointer;font-size:19px;letter-spacing:-.012em;color:var(--ink);list-style:none}.faq summary::-webkit-details-marker{display:none}.faq summary::after{content:"+";float:right;color:var(--muted-l)}.faq details[open] summary::after{content:"\\2212"}.faq p{margin:12px 0 0;color:var(--muted-l);font-size:16px;line-height:1.6;max-width:62ch}

.wrap{max-width:var(--max);margin:0 auto;padding:128px var(--gutter)}
section.film .inner.two{display:grid;grid-template-columns:1.15fr .85fr;gap:24px 64px;align-items:end}section.film .inner.two .lede{margin:0 0 8px}
section.film .inner.two h2{margin-bottom:0}section.film .inner.two .cta{margin-top:24px}
/* statement + numbers */
.statement{text-align:center;padding:152px var(--gutter) 0}
.statement p.big{font-family:var(--sans);font-weight:300;font-size:clamp(28px,3.9vw,54px);line-height:1.14;letter-spacing:-.028em;max-width:29ch;margin:0 auto;color:var(--ink)}
.statement p.sub{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);margin:40px auto 0}
.statement .cta{justify-content:center;margin-top:36px}
.strip{max-width:var(--max);margin:120px auto 0;padding:0 var(--gutter) 120px;display:grid;grid-template-columns:repeat(5,1fr)}
.strip div{border-top:1px solid var(--ink);padding:22px 20px 0 0}
.strip b{display:block;font-family:var(--sans);font-weight:300;font-size:clamp(64px,8.4vw,128px);line-height:.95;letter-spacing:-.05em;color:var(--ink);font-variant-numeric:tabular-nums}
.strip span{display:block;margin-top:18px;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);max-width:22ch;line-height:1.55}
/* research */
.head{display:grid;grid-template-columns:1fr 1fr;gap:24px 64px;align-items:end;padding-bottom:56px;border-bottom:1px solid var(--rule-l)}
.head h2{margin-bottom:0}.serif{font-family:var(--serif);font-weight:300;font-size:clamp(20px,1.9vw,26px);line-height:1.4;letter-spacing:-.01em;color:var(--ink);margin:0;max-width:34ch}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:32px 0 8px}.chips[hidden]{display:none}
.chips button{font:400 12.5px/1 var(--sans);padding:10px 14px;border:1px solid var(--rule-l);border-radius:0;background:transparent;color:var(--ink);cursor:pointer;letter-spacing:-.005em}
.chips button:hover{border-color:var(--ink)}.chips button[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.chips button span{font-family:var(--mono);font-size:10px;margin-left:8px;opacity:.6}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:64px 32px;margin-top:40px}
.card{display:flex;flex-direction:column;gap:12px;border-top:1px solid var(--rule-l);padding-top:16px}.card[hidden]{display:none}
.card .media{display:block;aspect-ratio:16/10;overflow:hidden;background:#fff;border:1px solid var(--rule-l);margin-bottom:6px}
.card .media img{width:100%;height:100%;object-fit:contain;padding:5% 4%;display:block;transition:transform .6s ease}.card:hover .media img{transform:scale(1.025)}
.card .meta{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.card h3{font-family:var(--sans);font-weight:400;font-size:clamp(22px,1.9vw,27px);line-height:1.12;letter-spacing:-.022em;margin:0}
.card a.t{text-decoration:none}.card a.t:hover{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}
.card p{color:var(--muted-l);margin:0;font-size:15px;line-height:1.55}
.card small{margin-top:auto;padding-top:8px;font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;color:var(--muted-l);line-height:1.8}.card small a{color:var(--ink)}
.methods{margin-top:128px}.methods .cards{grid-template-columns:repeat(2,1fr)}.methods .card h3{font-size:clamp(24px,2.4vw,34px)}
/* lists */
.split{display:grid;grid-template-columns:1fr 1fr;gap:48px 64px;align-items:start}.list{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink)}
.list li{padding:18px 0;border-bottom:1px solid var(--rule-l);color:var(--muted-l);font-size:15px}.list li b{color:var(--ink);font-weight:400;font-size:17px;letter-spacing:-.01em}.list li a{color:var(--ink)}
.light code{font-family:var(--mono);font-size:13px;background:rgba(30,31,43,.06);padding:1px 5px}
/* access */
section.film.access{min-height:0;align-items:stretch}section.film.access::after{background:linear-gradient(180deg,rgba(11,12,16,.78),rgba(11,12,16,.9))}
section.film.access .inner{padding:128px var(--gutter)}section.film.access .split{align-items:start}
@media (max-width:1100px){.cards{grid-template-columns:repeat(2,1fr)}.strip{grid-template-columns:repeat(3,1fr);row-gap:48px}}
@media (max-width:820px){.wrap{padding:88px var(--gutter)}.statement{padding:104px var(--gutter) 0}.statement p.big{font-size:clamp(26px,7.4vw,40px)}
.strip{grid-template-columns:repeat(2,1fr);gap:40px 16px;margin-top:80px;padding-bottom:88px}.strip div:last-child{grid-column:1/-1}.strip b{font-size:clamp(56px,17vw,84px)}
section.film .inner.two,.head,.split{grid-template-columns:1fr}.cards,.methods .cards{grid-template-columns:1fr;gap:48px}.methods{margin-top:88px}
section.film.access .inner{padding:88px var(--gutter)}}
"""



# Questions an engineer, a buyer or an AI search engine asks first. Shown on the page and
# mirrored as FAQPage data, so the visible answer and the structured answer are the same text.
FAQ = [
    ("What is CodeNinja Atoms?",
     "CodeNinja Atoms is building a sovereign AI operating system for the physical world. It publishes open reference architectures for physical AI in operations such as energy grids, ports, oil and gas, manufacturing and agriculture, designed on Praxis and made living with Hyper Ontology. CodeNinja Atoms is a fully owned subsidiary of CodeNinja."),
    ("What is a reference architecture for physical AI?",
     "A complete system design for one real operation: what to sense, which models run where and on which hardware, the object model (ontology) that joins the operator's existing systems, what it costs over three years, and which named person approves every action."),
    ("What does sovereign AI mean here?",
     "The system runs on hardware the operator owns, inside its own country, on open-weight models whose licences let the operator keep and change them, so no operational data has to leave and no single outside AI company sits in the serving path."),
    ("What is Praxis?",
     "Praxis is CodeNinja's platform for designing physical AI systems. It turns an operator's requirement into a complete design, reasoned through eight lenses from first principles to hardware. Every design on this site was made on Praxis. It is in beta."),
    ("What is Hyper Ontology?",
     "Hyper Ontology is CodeNinja's ontology platform. It imports the object model a Praxis design publishes (format hyper-ontology/1) and stands it up as a living system over the operator's own systems of record. It is in beta."),
    ("Can I reuse the designs?",
     "Yes. Every paper, object model, model register and dataset row is published under CC BY 4.0 with a DOI. The full set loads as one dataset on Hugging Face, and an MCP server gives coding agents every design."),
]
ORG_ID = "https://codeatoms.ai/#org"
SITE_ID = "https://codeatoms.ai/#website"


def identity_ld():
    org = {"@context": "https://schema.org", "@type": "Organization", "@id": ORG_ID, "name": "CodeNinja Atoms", "url": "https://codeatoms.ai/",
           "logo": {"@type": "ImageObject", "url": "https://codeatoms.ai/icon-512.png", "width": 512, "height": 512},
           "description": "CodeNinja Atoms is building a sovereign AI operating system for the physical world: open reference architectures for physical AI, Praxis for designing them and Hyper Ontology for making them living.",
           "parentOrganization": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "sameAs": ["https://github.com/muhammadumar89/codeninja-research", "https://huggingface.co/CodeNinjatools",
                      "https://zenodo.org/communities/physical-ai-reference-architectures"],
           "knowsAbout": ["physical AI", "sovereign AI", "ontology", "reference architecture", "industrial AI", "open-weight models"]}
    site = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE_ID, "name": "CodeNinja Atoms", "alternateName": "codeatoms.ai",
            "url": "https://codeatoms.ai/", "publisher": {"@id": ORG_ID}, "inLanguage": "en"}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    return [org, site, faq]


def film(video, inner, eager=False, cls="", sid="", tail=""):
    v = f"assets/video/{video}"
    return (f'<section class="film{(" " + cls) if cls else ""}"{f" id={chr(34)}{sid}{chr(34)}" if sid else ""}><img class="poster" src="{v}.jpg" alt="" aria-hidden="true">'
            f'<video autoplay muted loop playsinline preload="{"auto" if eager else "none"}" poster="{v}.jpg" aria-hidden="true">'
            f'<source src="{v}.mp4" type="video/mp4"></video><div class="inner{(" two" if "two" in cls.split() else "")}">{inner}</div>{tail}</section>')


def _fig(slug):
    f = ROOT / slug / "figures" / "figure_01.png"
    if not f.exists():
        return ""
    cap = ROOT / slug / "figures" / "figure_01.txt"
    alt = cap.read_text(encoding="utf-8").strip() if cap.exists() else ""
    return f'<a class="media" href="{slug}/" tabindex="-1" aria-hidden="true"><img src="{slug}/figures/figure_01.png" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async" width="1700" height="940"></a>'


def landing(ps, sols):
    E = lambda x: html.escape(str(x), quote=True)
    ms = [p for p in ps if not p["ontology"]]; ps = [p for p in ps if p["ontology"]]
    mcards = "".join(f'<article class="card"><span class="meta">Method</span><h3><a class="t" href="{p["slug"]}/">{E(p["title"].split(":")[0])}</a></h3><p>{E(p["title"].split(":",1)[1].strip() if ":" in p["title"] else "")}</p>'
                     f'<small><a href="{p["pdf"]}">PDF</a>' + (f' · DOI <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>' if p["doi"] else "") + "</small></article>" for p in ms)
    countries = sorted({p["country"] for p in ps if p["country"]}); sectors = sorted({p["sector"] for p in ps if p["sector"]})
    objs = sum(p["n_obj"] for p in ps); dois = sum(1 for p in ps if p["doi"])
    cards = "".join(
        f'<article class="card" data-sector="{E(p["sector"])}">{_fig(p["slug"])}<span class="meta">{E(p["country"])} · {E(p["sector"])}</span>'
        f'<h3><a class="t" href="{p["slug"]}/">{E(p["title"].split(":")[0])}</a></h3><p>{E(p["title"].split(":",1)[1].strip() if ":" in p["title"] else p["description"])}</p>'
        f'<small><a href="{p["pdf"]}">PDF</a>' + (f' · <a href="{p["ontology"]}">object model</a>' if p["ontology"] else "")
        + (f' · DOI <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>' if p["doi"] else "") + "</small></article>" for p in ps)
    chips = ('<div class="chips" role="group" aria-label="Filter by sector" hidden><button type="button" aria-pressed="true" data-f="">All<span>' + str(len(ps)) + '</span></button>'
             + "".join(f'<button type="button" aria-pressed="false" data-f="{E(s)}">{E(s[:1].upper() + s[1:])}<span>{sum(1 for p in ps if p["sector"] == s)}</span></button>' for s in sectors) + '</div>')
    if sols:
        scards = "".join(f'<article class="card"><span class="meta">{E(m.get("country",""))} · {E(m.get("sector",""))}</span>'
                         f'<h3><a class="t" href="solutions/{m["slug"]}/">{E(m["title"])}</a></h3><p>{E(m.get("summary",""))}</p>'
                         f'<small>{E(m.get("issuer_class",""))}' + (f' · DOI <a href="https://doi.org/{m["doi"]}">{m["doi"]}</a>' if m.get("doi") else "") + '</small></article>' for m in sols)
        sbody = f'<div class="cards" style="margin-top:0">{scards}</div>'
    else:
        sbody = ('<ul class="list"><li><b>The requirement as published.</b> What the operator asked for, read in its own words.</li>'
                 '<li><b>The complete solution design.</b> Scope, architecture, object model, models and hardware, rollout and cost, reasoned on Praxis.</li>'
                 '<li><b>The living system.</b> The object model packaged for Hyper Ontology, ready to stand up over the operator\'s own systems.</li></ul>')
    seclinks = '<p class="serif" style="margin:-8px 0 28px;font-size:17px">Questions answered by sector: ' + ' · '.join(f'<a href="sectors/{x.replace(" and ", "-and-").replace(" ", "-")}/">{E(x)}</a>' for x in sectors) + '</p>'
    scroll = f'<a class="scroll" href="#intro">Scroll to explore{brand.ARROW}</a>'
    nav = [("Research", "#research"), ("Solutions", "#solutions"), ("Praxis", "praxis/"), ("Hyper Ontology", "hyper-ontology/"), ("Data", "#data"), ("About", "about/")]
    return f"""{brand.header("./", nav)}
<main>
{film("port-night", '<p class="mono">CodeNinja Atoms</p><h1>Autonomy in physical operations.</h1>', eager=True, cls="hero", tail=scroll)}
<section class="light" id="intro"><div class="statement"><p class="sub" style="margin:0 0 20px">CodeNinja Atoms is building a sovereign AI operating system for the physical world.</p><p class="big">Sovereign system designs for ports, grids, mills, plants and sites: what to sense, where each model runs, what the object model holds, what it costs and who approves every action.</p>
<p class="sub">Designed on Praxis. Made living with Hyper Ontology. Open papers, open object models, open data.</p>
<div class="cta"><a class="btn solid" href="#research">Read the research</a><a class="btn" href="praxis/">Praxis</a><a class="btn" href="hyper-ontology/">Hyper Ontology</a></div></div>
<div class="strip"><div><b>{len(ps)}</b><span>reference architectures</span></div><div><b>{len(sectors)}</b><span>sectors of physical operations</span></div><div><b>{len(countries)}</b><span>countries: {E(', '.join(countries))}</span></div><div><b>{objs}</b><span>ontology objects published</span></div><div><b>{dois}</b><span>DOIs, all CC BY 4.0</span></div></div></section>
{film("control-room", '<div><p class="mono">Praxis</p><h2>Design the system a ten-year domain engineer would.</h2></div><div><p class="lede">Praxis turns an operator\'s requirement into a complete design for physical AI, reasoned through eight lenses from first principles to hardware, with every claim on a record and a person on every write.</p><div class="cta"><a class="btn" href="praxis/">How Praxis reasons</a></div></div>', cls="two")}
{film("rail-yard", '<div><p class="mono">Hyper Ontology</p><h2>From a reference architecture to a living system.</h2></div><div><p class="lede">Every design ships its object model as a package. Hyper Ontology imports it and stands it up over the operator\'s own systems of record: objects, typed links and actions that sense, decide, act and learn.</p><div class="cta"><a class="btn" href="hyper-ontology/">How it becomes living</a></div></div>', cls="two")}
<section id="research" class="light"><div class="wrap"><div class="head"><div><p class="mono">Research · Vertical-Driven Architectures</p><h2>One operation, one design, end to end.</h2></div>
<p class="serif">Each paper is a complete reference architecture for one real operation, written so an engineer, or their coding agent, can build it. Operators are described by class, never by name.</p></div>
{seclinks}
{chips}
<div class="cards" id="research-cards">{cards}</div>
<div class="methods"><div class="head"><div><p class="mono">Methods</p><h2>How the designs are made, and how they come alive.</h2></div></div><div class="cards">{mcards}</div></div></div></section>
{film("pylon-dusk", '<div><p class="mono">Solutions</p><h2>Published requirements, solved in the open.</h2></div><div><p class="lede">Operators publish what they need. We publish how to build it: the full solution design for a published requirement, from sensing to the living ontology.</p></div>', cls="two")}
<section id="solutions" class="light alt"><div class="wrap">{sbody}</div></section>
<section id="faq" class="light rule"><div class="wrap"><div class="split"><div><p class="mono">Questions</p><h2>What this is.</h2></div>
<div class="faq">{"".join(f'<details{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(FAQ))}</div></div></div></section>
<section id="data" class="light rule"><div class="wrap"><div class="split"><div><p class="mono">For agents and engineers</p><h2>Everything here is data.</h2><p class="serif" style="margin-top:28px">Load every design, object, model choice and cost line as one dataset, or read the site the way an agent does.</p></div>
<ul class="list"><li><b><a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">Vertical-Driven Architectures dataset</a></b><br>designs, objects, models, costs and full text; monthly snapshot DOI <a href="https://doi.org/10.5281/zenodo.23160819">10.5281/zenodo.23160819</a></li>
<li><b><a href="https://huggingface.co/collections/CodeNinjatools/vertical-driven-architectures-6ac0d23c8b7b3938f1a4fd00">Hugging Face collection</a></b><br>a Space and an ontology package for every design</li>
<li><b><a href="https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server">MCP server</a></b><br>give your coding agent every design: <code>codeninja-research-mcp</code></li>
<li><b><a href="llms.txt">llms.txt</a></b> · <a href="feed.xml">Atom feed</a> · <a href="sitemap.xml">sitemap</a></li>
<li><b><a href="https://zenodo.org/communities/physical-ai-reference-architectures">Zenodo community</a></b><br>every paper with its DOI, in one place</li>
<li><b><a href="https://github.com/muhammadumar89/codeninja-research">Source files on GitHub</a></b><br>papers, packages, the package format and the loader</li></ul></div></div></section>
{film("desert-flare", f'<div class="split"><div><p class="mono">Praxis beta</p><h2>Design for the physical world.</h2><p class="lede">Every design here was made on Praxis, and Praxis is opening to outside engineers in beta. Tell us the operation you want to design, or the systems you want to make living with Hyper Ontology, and we will reply with your place on the list.</p></div><div>{brand.form("both")}</div></div>', cls="access", sid="access")}
</main>
<footer class="site"><div class="wrapf">{brand.footer_brand("./")}<span>CodeNinja Atoms is part of <a href="{brand.PARENT}">CodeNinja</a> · Sovereign AI for physical operations</span><span>Papers, object models and data CC BY 4.0 · <a href="assets/video/CREDITS.md">Video credits</a></span></div></footer>"""


# Sector chips filter the research cards; without JS the chips stay hidden and every card shows.
FILTER = """<script>(function(){var g=document.querySelector('.chips');if(!g)return;var cs=document.querySelectorAll('#research-cards .card');g.hidden=false;
g.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var f=b.getAttribute('data-f');g.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
cs.forEach(function(c){c.hidden=!!f&&c.getAttribute('data-sector')!==f})})})();</script>"""


def main():
    ps = papers()
    today = datetime.date.today().isoformat()
    rows = "\n".join(
        f'<li><a href="{p["slug"]}/"><strong>{html.escape(p["title"])}</strong></a><br>'
        f'<span>{html.escape(p["description"])}</span><br>'
        f'<small>{p["date"]} · <a href="{p["pdf"]}">PDF</a>'
        + (f' · <a href="{p["ontology"]}">ontology JSON</a>' if p["ontology"] else "")
        + (f' · DOI <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>' if p["doi"] else "")
        + "</small></li>" for p in ps)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "CodeNinja Atoms",
          "description": "Open reference architectures for sovereign AI in physical operations.",
          "url": f"{BASE}/", "publisher": {"@id": ORG_ID}, "isPartOf": {"@id": SITE_ID},
          "hasPart": [{"@type": "TechArticle", "headline": p["title"], "url": f"{BASE}/{p['slug']}/"} for p in ps]}
    sols = solutions()
    idld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in identity_ld())
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CodeNinja Atoms | Sovereign AI for the Physical World</title>
<meta name="description" content="CodeNinja Atoms is building a sovereign AI operating system for the physical world: open reference architectures for physical AI in grids, ports, oil and gas, plants and farms, designed on Praxis and made living with Hyper Ontology.">
<link rel="canonical" href="{BASE}/"><link rel="alternate" type="application/atom+xml" href="{BASE}/feed.xml">
<meta property="og:type" content="website"><meta property="og:title" content="CodeNinja Atoms: autonomy in physical operations"><meta property="og:image" content="{BASE}/assets/video/port-night.jpg"><meta property="og:url" content="{BASE}/">
{brand.FONTS}{brand.JS_FLAG}
<script type="application/ld+json">{json.dumps(ld)}</script>
{idld}
<style>{brand.CSS}{CSS}</style></head><body>
{landing(ps, sols)}
{brand.SCRIPT}{FILTER}
</body></html>"""
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    urls = [f"{BASE}/", f"{BASE}/praxis/", f"{BASE}/hyper-ontology/", f"{BASE}/about/", f"{BASE}/sectors/"] + [f"{BASE}/sectors/{q.parent.name}/" for q in sorted((ROOT / "sectors").glob("*/index.html"))] + [f"{BASE}/{p['slug']}/" for p in ps] + [p["pdf"] for p in ps if p["pdf"]]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    entries = "".join(f"""  <entry><title>{html.escape(p['title'])}</title><link href="{BASE}/{p['slug']}/"/><id>{BASE}/{p['slug']}/</id><updated>{p['date']}T00:00:00Z</updated><summary>{html.escape(p['description'])}</summary></entry>\n""" for p in ps)
    (ROOT / "feed.xml").write_text(f'<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom"><title>CodeNinja Atoms</title><link href="{BASE}/"/><link rel="self" href="{BASE}/feed.xml"/><id>{BASE}/</id><updated>{today}T00:00:00Z</updated>\n{entries}</feed>\n', encoding="utf-8")
    llms = ["# CodeNinja Atoms", "",
            "> The cumulative dataset of every design (designs, objects, models, costs, full text): https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures", "",
            "> Open reference architectures for sovereign AI in physical operations: designs an operator can run on its own hardware, under open-weight licences, with no data leaving the country. CC BY 4.0.", "",
            "## Products", "",
            f"- [Praxis]({BASE}/praxis/): CodeNinja's platform for designing physical AI systems. Every design below was reasoned on Praxis. Beta, access by request.",
            f"- [Hyper Ontology]({BASE}/hyper-ontology/): CodeNinja's ontology platform. It imports the object models Praxis designs (format hyper-ontology/1) and stands them up as a living ontology over the operator's own systems. Beta, access by request.", "",
            "## For agents", "",
            "- [MCP server](https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server): codeninja-research-mcp exposes list_designs, get_design, read_paper and find over every design.", "",
            "## Methods", ""] + [f"- [{p['title']}]({BASE}/{p['slug']}/): {p['description']}" + (f" DOI {p['doi']}." if p["doi"] else "") for p in ps if not p["ontology"]] + ["",
            "## Papers", ""]
    for p in [x for x in ps if x["ontology"]]:
        llms.append(f"- [{p['title']}]({BASE}/{p['slug']}/): {p['description']}" + (f" DOI {p['doi']}." if p["doi"] else ""))
        if p["ontology"]:
            llms.append(f"  - [Object model as JSON]({p['ontology']})")
    secs = sorted((ROOT / "sectors").glob("*/index.html"))
    if secs:
        llms += ["", "## Sectors: questions answered", ""] + [f"- [Physical AI for {q.parent.name.replace('-', ' ')}]({BASE}/sectors/{q.parent.name}/): models, compute, three-year cost, ontology and human control, answered from the published designs. Markdown: {BASE}/sectors/{q.parent.name}/index.md" for q in secs]
    (ROOT / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
    print(f"{len(ps)} paper(s): index.html, sitemap.xml, feed.xml, llms.txt")
    import dataset_ld; dataset_ld.main()  # Dataset markup for Google Dataset Search; index.html was just rewritten


if __name__ == "__main__":
    import sector_pages  # sector question pages first: the sitemap lists them
    sector_pages.main()
    main()
    import seo  # search and AI retrieval pass: always last
    seo.main()
