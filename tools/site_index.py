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
BASE = "https://muhammadumar89.github.io/codeninja-research"


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


CSS = """
:root{--bg:#07090B;--fg:#E8ECEF;--muted:#9AA5AF;--line:rgba(255,255,255,.12);--amber:#E0A84A;--panel:#0E1216}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 "Inter",Arial,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}.mono{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;letter-spacing:.14em;text-transform:uppercase;font-size:11px;color:var(--amber)}
header.top{position:fixed;top:0;left:0;right:0;z-index:10;display:flex;justify-content:space-between;align-items:center;padding:16px 28px;background:rgba(7,9,11,.72);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.top b{letter-spacing:.24em;font-size:13px}header.top nav a{margin-left:22px;font-size:13px;text-decoration:none;color:var(--muted)}header.top nav a:hover{color:var(--fg)}
section.film{position:relative;min-height:88vh;display:flex;align-items:flex-end;overflow:hidden;border-bottom:1px solid var(--line)}
section.film video,section.film img.poster{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}
section.film::after{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(7,9,11,.35) 0%,rgba(7,9,11,.55) 45%,rgba(7,9,11,.94) 100%)}
section.film .inner{position:relative;z-index:2;max-width:1120px;width:100%;margin:0 auto;padding:0 28px 72px}
h1{font-size:clamp(38px,6.4vw,84px);line-height:1.02;font-weight:600;letter-spacing:-.02em;margin:.25em 0 .3em;max-width:13ch}
h2{font-size:clamp(28px,4vw,48px);line-height:1.08;font-weight:600;letter-spacing:-.015em;margin:.3em 0 .4em;max-width:18ch}
.lede{font-size:clamp(17px,2vw,21px);max-width:58ch;color:#D5DCE1}.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.btn{display:inline-block;padding:12px 18px;border:1px solid var(--line);text-decoration:none;font-size:14px;background:rgba(255,255,255,.04)}.btn.primary{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));border-bottom:1px solid var(--line)}
.strip div{padding:26px 28px;border-right:1px solid var(--line)}.strip b{display:block;font-size:34px;font-weight:600}.strip span{color:var(--muted);font-size:13px}
.wrap{max-width:1120px;margin:0 auto;padding:88px 28px}.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:28px}
.card{border:1px solid var(--line);background:var(--panel);padding:22px 22px 18px;display:flex;flex-direction:column;gap:8px}
.card h3{font-size:19px;line-height:1.25;margin:4px 0;font-weight:600}.card p{color:var(--muted);margin:0;font-size:14.5px}.card small{color:var(--muted);font-size:12.5px;margin-top:auto;padding-top:10px}
.card a.t{text-decoration:none}.card a.t:hover{text-decoration:underline}.tags{display:flex;gap:8px;flex-wrap:wrap}.tag{border:1px solid var(--line);padding:2px 8px;font-size:11px;color:var(--muted);letter-spacing:.06em;text-transform:uppercase}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:start}.list{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}
.list li{padding:14px 0;border-bottom:1px solid var(--line);color:#D5DCE1}.list li b{color:var(--fg)}
footer{border-top:1px solid var(--line);padding:36px 28px;color:var(--muted);font-size:13px}footer .wrapf{max-width:1120px;margin:0 auto;display:flex;gap:24px;flex-wrap:wrap;justify-content:space-between}
@media (max-width:760px){header.top{padding:14px 16px}header.top nav a{margin-left:12px;font-size:12px}section.film .inner{padding:110px 16px 48px}.wrap{padding:64px 16px}header.top nav a.opt{display:none}.split{grid-template-columns:1fr}.strip div{border-right:none;border-bottom:1px solid var(--line)}section.film{min-height:78vh}}
@media (prefers-reduced-motion:reduce){section.film video{display:none}}
"""


def film(video, inner, eager=False):
    v = f"assets/video/{video}"
    return (f'<section class="film"><img class="poster" src="{v}.jpg" alt="" aria-hidden="true">'
            f'<video autoplay muted loop playsinline preload="{"auto" if eager else "none"}" poster="{v}.jpg" aria-hidden="true">'
            f'<source src="{v}.mp4" type="video/mp4"></video><div class="inner">{inner}</div></section>')


def landing(ps, sols):
    E = lambda x: html.escape(str(x), quote=True)
    ms = [p for p in ps if not p["ontology"]]; ps = [p for p in ps if p["ontology"]]
    mcards = "".join(f'<article class="card"><div class="tags"><span class="tag">Method</span></div><h3><a class="t" href="{p["slug"]}/">{E(p["title"].split(":")[0])}</a></h3><p>{E(p["title"].split(":",1)[1].strip() if ":" in p["title"] else "")}</p>'
                     f'<small><a href="{p["pdf"]}">PDF</a>' + (f' · DOI <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>' if p["doi"] else "") + "</small></article>" for p in ms)
    countries = sorted({p["country"] for p in ps if p["country"]}); sectors = sorted({p["sector"] for p in ps if p["sector"]})
    objs = sum(p["n_obj"] for p in ps); dois = sum(1 for p in ps if p["doi"])
    cards = "".join(
        f'<article class="card"><div class="tags"><span class="tag">{E(p["country"])}</span><span class="tag">{E(p["sector"])}</span></div>'
        f'<h3><a class="t" href="{p["slug"]}/">{E(p["title"].split(":")[0])}</a></h3><p>{E(p["title"].split(":",1)[1].strip() if ":" in p["title"] else p["description"])}</p>'
        f'<small><a href="{p["pdf"]}">PDF</a>' + (f' · <a href="{p["ontology"]}">object model</a>' if p["ontology"] else "")
        + (f' · DOI <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>' if p["doi"] else "") + "</small></article>" for p in ps)
    if sols:
        scards = "".join(f'<article class="card"><div class="tags"><span class="tag">{E(m.get("country",""))}</span><span class="tag">{E(m.get("sector",""))}</span></div>'
                         f'<h3><a class="t" href="solutions/{m["slug"]}/">{E(m["title"])}</a></h3><p>{E(m.get("summary",""))}</p>'
                         f'<small>{E(m.get("issuer_class",""))}' + (f' · DOI <a href="https://doi.org/{m["doi"]}">{m["doi"]}</a>' if m.get("doi") else "") + '</small></article>' for m in sols)
        sbody = f'<div class="cols">{scards}</div>'
    else:
        sbody = ('<ul class="list"><li><b>The requirement as published.</b> What the operator asked for, read in its own words.</li>'
                 '<li><b>The complete solution design.</b> Scope, architecture, object model, models and hardware, rollout and cost, reasoned on Praxis.</li>'
                 '<li><b>The living system.</b> The object model packaged for Hyper Ontology, ready to stand up over the operator\'s own systems.</li></ul>')
    return f"""<header class="top">{brand.header_brand("./")}<nav><a href="#research">Research</a><a class="opt" href="#solutions">Solutions</a><a href="praxis/">Praxis</a><a href="hyper-ontology/">Hyper Ontology</a><a class="opt" href="#data">Data</a><a href="#access" style="color:#fff">Request access</a></nav></header>
<main>
{film("port-night", f'<p class="mono">CodeNinja Research</p><h1>Autonomy in physical operations.</h1><p class="lede">Sovereign system designs for ports, grids, mills, plants and sites: what to sense, where each model runs, what the object model holds, what it costs and who approves every action. Designed on Praxis. Made living with Hyper Ontology. Open papers, open object models, open data.</p><div class="cta"><a class="btn red" href="#access">Request beta access</a><a class="btn primary" href="#research">Read the research</a><a class="btn" href="praxis/">Praxis</a><a class="btn" href="hyper-ontology/">Hyper Ontology</a></div>', eager=True)}
<div class="strip"><div><b>{len(ps)}</b><span>reference architectures</span></div><div><b>{len(sectors)}</b><span>sectors of physical operations</span></div><div><b>{len(countries)}</b><span>countries: {E(', '.join(countries))}</span></div><div><b>{objs}</b><span>ontology objects published</span></div><div><b>{dois}</b><span>DOIs, all CC BY 4.0</span></div></div>
{film("control-room", '<p class="mono">Praxis</p><h2>Design the system a ten-year domain engineer would.</h2><p class="lede">Praxis turns an operator\'s requirement into a complete design for physical AI, reasoned through eight lenses from first principles to hardware, with every claim on a record and a person on every write.</p><div class="cta"><a class="btn" href="praxis/">How Praxis reasons</a></div>')}
{film("rail-yard", '<p class="mono">Hyper Ontology</p><h2>From a reference architecture to a living system.</h2><p class="lede">Every design ships its object model as a package. Hyper Ontology imports it and stands it up over the operator\'s own systems of record: objects, typed links and actions that sense, decide, act and learn.</p><div class="cta"><a class="btn" href="hyper-ontology/">How it becomes living</a></div>')}
<section id="research" class="wrap"><p class="mono">Research · Vertical-Driven Architectures</p><h2>One operation, one design, end to end.</h2>
<p class="lede" style="color:var(--muted)">Each paper is a complete reference architecture for one real operation, written so an engineer, or their coding agent, can build it. Operators are described by class, never by name.</p>
<div class="cols" style="margin-top:36px">{cards}</div>
<p class="mono" style="margin-top:56px">Methods</p><h2 style="font-size:clamp(24px,3vw,34px)">How the designs are made, and how they come alive.</h2><div class="cols" style="margin-top:20px">{mcards}</div></section>
{film("pylon-dusk", '<p class="mono">Solutions</p><h2>Published requirements, solved in the open.</h2><p class="lede">Operators publish what they need. We publish how to build it: the full solution design for a published requirement, from sensing to the living ontology.</p>')}
<section id="solutions" class="wrap">{sbody}</section>
<section id="data" class="wrap" style="padding-top:0"><div class="split"><div><p class="mono">For agents and engineers</p><h2>Everything here is data.</h2><p class="lede" style="color:var(--muted)">Load every design, object, model choice and cost line as one dataset, or read the site the way an agent does.</p></div>
<ul class="list"><li><b><a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">Vertical-Driven Architectures dataset</a></b><br>designs, objects, models, costs and full text</li>
<li><b><a href="https://huggingface.co/collections/CodeNinjatools/vertical-driven-architectures-6ac0d23c8b7b3938f1a4fd00">Hugging Face collection</a></b><br>a Space and an ontology package for every design</li>
<li><b><a href="https://github.com/muhammadumar89/codeninja-research/tree/main/mcp-server">MCP server</a></b><br>give your coding agent every design: <code>codeninja-research-mcp</code></li>
<li><b><a href="llms.txt">llms.txt</a></b> · <a href="feed.xml">Atom feed</a> · <a href="sitemap.xml">sitemap</a></li>
<li><b><a href="https://zenodo.org/communities/physical-ai-reference-architectures">Zenodo community</a></b><br>every paper with its DOI, in one place</li>
<li><b><a href="https://github.com/muhammadumar89/codeninja-research">Source files on GitHub</a></b><br>papers, packages, the package format and the loader</li></ul></div></section>
<section id="access" class="wrap" style="padding-top:0;border-top:1px solid var(--line);padding-top:88px"><div class="split"><div><p class="mono">Beta access</p><h2>Start the conversation.</h2><p class="lede" style="color:var(--muted)">Praxis and Hyper Ontology are in beta with a small number of outside teams. Tell us the operation you want designed, or the systems you want to make living, and a CodeNinja engineer will reply.</p></div>
<div>{brand.form("both")}</div></div></section>
</main>
<footer><div class="wrapf">{brand.footer_brand("./")}<span>CodeNinja Research is part of <a href="{brand.PARENT}">CodeNinja</a> · Sovereign AI for physical operations</span><span>Papers, object models and data CC BY 4.0 · <a href="assets/video/CREDITS.md">Video credits</a></span></div></footer>"""


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
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "CodeNinja Research",
          "description": "Open reference architectures for sovereign AI in physical operations.",
          "url": f"{BASE}/", "publisher": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
          "hasPart": [{"@type": "TechArticle", "headline": p["title"], "url": f"{BASE}/{p['slug']}/"} for p in ps]}
    sols = solutions()
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CodeNinja Research</title>
<meta name="description" content="Sovereign system designs for physical AI in ports, grids, mills, plants and sites, designed on Praxis and made living with Hyper Ontology: open papers, open object models, open data.">
<link rel="canonical" href="{BASE}/"><link rel="alternate" type="application/atom+xml" href="{BASE}/feed.xml">
<meta property="og:type" content="website"><meta property="og:title" content="CodeNinja Research: autonomy in physical operations"><meta property="og:image" content="{BASE}/assets/video/port-night.jpg"><meta property="og:url" content="{BASE}/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=IBM+Plex+Mono&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld)}</script>
<style>{CSS}{brand.CSS}</style></head><body>
{landing(ps, sols)}
<script>(function(){{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;var io=new IntersectionObserver(function(es){{es.forEach(function(e){{var v=e.target;if(e.isIntersecting){{v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){{}})}}else{{v.pause()}}}})}},{{threshold:0.15}});document.querySelectorAll('section.film video').forEach(function(v){{io.observe(v)}})}})();</script>
</body></html>"""
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    urls = [f"{BASE}/", f"{BASE}/praxis/", f"{BASE}/hyper-ontology/"] + [f"{BASE}/{p['slug']}/" for p in ps] + [p["pdf"] for p in ps if p["pdf"]]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    entries = "".join(f"""  <entry><title>{html.escape(p['title'])}</title><link href="{BASE}/{p['slug']}/"/><id>{BASE}/{p['slug']}/</id><updated>{p['date']}T00:00:00Z</updated><summary>{html.escape(p['description'])}</summary></entry>\n""" for p in ps)
    (ROOT / "feed.xml").write_text(f'<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom"><title>CodeNinja Research</title><link href="{BASE}/"/><link rel="self" href="{BASE}/feed.xml"/><id>{BASE}/</id><updated>{today}T00:00:00Z</updated>\n{entries}</feed>\n', encoding="utf-8")
    llms = ["# CodeNinja Research", "",
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
    (ROOT / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
    print(f"{len(ps)} paper(s): index.html, sitemap.xml, feed.xml, llms.txt")
    import dataset_ld; dataset_ld.main()  # Dataset markup for Google Dataset Search; index.html was just rewritten


if __name__ == "__main__":
    main()
