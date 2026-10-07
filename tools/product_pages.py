"""The two product pages: Praxis and Hyper Ontology. Built from the papers on disk so the
evidence lists stay current; rerun after every new paper.
    python tools/product_pages.py
"""
import html, json, datetime, re
from pathlib import Path
import brand
ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)

def designs():
    out = []
    for d in sorted(ROOT.iterdir()):
        if not (d / "ontology" / "objects.json").exists() or not (d / "index.html").exists(): continue
        h = (d / "index.html").read_text(encoding="utf-8")
        g = lambda n: html.unescape((re.search(rf'<meta name="{n}" content="([^"]*)"', h) or [None, ""])[1])
        pkg = json.loads((d / "ontology" / "objects.json").read_text(encoding="utf-8"))
        objs = pkg["objects"]
        out.append({"slug": d.name, "title": g("citation_title"), "doi": g("citation_doi"), "country": pkg.get("country", ""),
                    "sector": pkg.get("sector", "").replace("-", " "), "n_obj": len(objs), "n_link": sum(len(o.get("links", [])) for o in objs),
                    "kinds": sorted({o["kind"] for o in objs})})
    return out

CSS = """
section.film.hero h1.prod{font-size:clamp(38px,5.6vw,80px);line-height:1.02;letter-spacing:-.032em;max-width:19ch}
section.film.hero .cta{justify-content:center}
.doc{max-width:920px;margin:0 auto;padding:128px var(--gutter) 128px;font-size:17px;line-height:1.68;color:rgba(30,31,43,.88)}
.doc .lead{font-family:var(--serif);font-weight:300;font-size:clamp(24px,2.7vw,36px);line-height:1.3;letter-spacing:-.015em;color:var(--ink);margin:0 0 48px}
.doc .lead a{text-decoration-thickness:1px;text-underline-offset:5px}
.doc h2{font-size:clamp(28px,3.3vw,44px);line-height:1.08;letter-spacing:-.028em;color:var(--ink);max-width:24ch;margin:104px 0 28px;padding-top:28px;border-top:1px solid var(--ink)}
.doc h3{font-family:var(--sans);font-weight:500;font-size:18px;line-height:1.3;letter-spacing:-.012em;color:var(--ink);margin:36px 0 8px}
.doc p{margin:0 0 20px}.doc a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:3px}.doc a:hover{color:#000}.doc strong{font-weight:500;color:var(--ink)}
.doc ol,.doc ul{padding:0;margin:0 0 24px;list-style:none;border-top:1px solid var(--rule-l);counter-reset:n}
.doc ol li,.doc ul li{padding:16px 0;border-bottom:1px solid var(--rule-l)}.doc ol li{counter-increment:n;position:relative;padding-left:48px}
.doc ol li::before{content:counter(n,decimal-leading-zero);position:absolute;left:0;top:21px;font-family:var(--mono);font-size:11px;line-height:1;color:var(--muted-l)}
.doc small,.doc .muted{color:var(--muted-l);font-size:14px}
.box{border:1px solid var(--rule-l);border-left:2px solid var(--red);background:rgba(255,255,255,.55);padding:18px 22px;margin:32px 0;font-size:15.5px}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:28px 0 32px}
table{width:100%;border-collapse:collapse;font-size:15px;line-height:1.5}
th,td{text-align:left;padding:14px 16px 14px 0;border-bottom:1px solid var(--rule-l);vertical-align:top}
th{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);border-bottom:1px solid var(--ink);padding-bottom:10px}
td:first-child{color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 28px;margin:32px 0 16px}
.grid .card{border-top:1px solid var(--ink);padding-top:14px;font-size:15px;line-height:1.55;color:var(--muted-l)}.grid .card h3{margin:0 0 8px;font-size:19px;font-weight:400;letter-spacing:-.018em}
code{font-family:var(--mono);background:rgba(30,31,43,.06);padding:1px 5px;font-size:.84em;color:var(--ink)}
pre{font-family:var(--mono);background:rgba(30,31,43,.05);padding:14px;overflow:auto;font-size:13px}
section.film.access{min-height:0;align-items:stretch}section.film.access::after{background:linear-gradient(180deg,rgba(11,12,16,.8),rgba(11,12,16,.9))}
section.film.access .inner{display:grid;grid-template-columns:1fr 1fr;gap:40px 64px;padding:128px var(--gutter)}
@media (max-width:820px){.doc{padding:80px var(--gutter);font-size:16px}.doc h2{margin-top:72px}.grid{grid-template-columns:1fr}section.film.access .inner{grid-template-columns:1fr;padding:88px var(--gutter)}}
"""

SHORT = {"praxis": "Praxis: Design Physical AI Systems | CodeNinja Atoms", "hyper-ontology": "Hyper Ontology: From Design to Living System | CodeNinja Atoms"}
VIDEO = {"praxis": "control-room", "hyper-ontology": "rail-yard"}
FORM = {"praxis": "Praxis", "hyper-ontology": "Hyper Ontology"}
ACCESS = {"praxis": "Praxis is the platform these designs were made on, and it is opening to outside engineers in beta. Tell us the operation you want to design, and we will reply with your place on the list.",
          "hyper-ontology": "Hyper Ontology turns a Praxis design into a living system, and it is opening to outside teams in beta. Tell us the systems you want to make living, and we will reply with your place on the list."}


def page(slug, title, desc, body, ld):
    v = VIDEO.get(slug, "port-night")
    m = re.search(r'(<p class="eyebrow">.*?</p>)\s*(<h1>.*?</h1>)\s*(<p class="lead">.*?</p>)', body, re.S)
    eyebrow, h1, lead = (m.group(1), m.group(2), m.group(3)) if m else ("", "", "")
    if m:
        body = body.replace(m.group(0), "", 1)
    vid = lambda n, eager: (f'<img class="poster" src="../assets/video/{n}.jpg" alt="" aria-hidden="true"><video autoplay muted loop playsinline preload="{"auto" if eager else "none"}" poster="../assets/video/{n}.jpg" aria-hidden="true">'
                            f'<source src="../assets/video/{n}.mp4" type="video/mp4"></video>')
    nav = [("Research", f"{BASE}/#research"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"), ("Data", f"{BASE}/#data"), ("Blog", f"{BASE}/blog/"), ("About", f"{BASE}/about/")]
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(SHORT.get(slug, title.split(':')[0]))}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{slug}/">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{slug}/">
<meta name="codeninja:kind" content="product">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", nav)}
<main>
<section class="film hero">{vid(v, True)}<div class="inner">{eyebrow}{h1.replace("<h1>", '<h1 class="prod">', 1)}<div class="cta"><a class="btn solid" href="#access">Join the Praxis beta</a></div></div><a class="scroll" href="#overview">Scroll to explore{brand.ARROW}</a></section>
<section class="light" id="overview"><div class="doc">
{lead}
{re.sub(r"(<table.*?</table>)", r'<div class="tw">\1</div>', body, flags=re.S)}
</div></section>
<section class="film access" id="access">{vid("desert-flare", False)}<div class="inner"><div><p class="eyebrow">Praxis beta</p><h2>Design for the physical world</h2><p class="lede">{ACCESS[slug]}</p></div><div>{brand.form(FORM[slug])}</div></div></section>
</main><footer class="site"><div class="wrapf">{brand.footer_brand(BASE)}<span>A <a href="{brand.PARENT}">CodeNinja</a> product · Pages, papers, object models and data are CC BY 4.0 · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}</body></html>"""

def faq(qs): return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}

def main():
    ds = designs()
    rows = "".join(f'<tr><td><a href="{BASE}/{d["slug"]}/">{E(d["title"].split(":")[0])}</a></td><td>{E(d["sector"])}</td><td>{E(d["country"])}</td><td>{d["n_obj"]} objects, {d["n_link"]} links</td><td>' + (f'<a href="https://doi.org/{d["doi"]}">{d["doi"]}</a>' if d["doi"] else "") + "</td></tr>" for d in ds)
    countries = sorted({d["country"] for d in ds}); sectors = sorted({d["sector"] for d in ds})
    # ---------------------------------------------------------------- Praxis
    pq = [("What designed the Vertical-Driven Architectures reference architectures?", f"Praxis, CodeNinja's platform for designing physical AI systems. All {len(ds)} designs in the series were produced on Praxis, and chapter 11 of each paper shows how Praxis contextualized and reasoned that design."),
          ("What does Praxis produce from a requirement?", "A complete system design for physical AI: a scope baseline, a layered architecture, an object model packaged for Hyper Ontology, a model and equipment register sized by memory arithmetic, a rollout with gates, a cost comparison, a live simulation, a proposal and functional specification, and a research paper."),
          ("How does Praxis reason?", "It loads the requirement and the sector's knowledge as context and reasons through eight lenses: first principles, case studies, tooling and recency, rules and regulations, approach, history, domain fusion, and hardware and equipment. Every claim must stand on a record, and a lens with nothing to cite says so instead of guessing."),
          ("Is Praxis available?", "Praxis is in beta. CodeNinja's forward deployed engineers use it in house, and access for outside engineering teams is by request.")]
    pbody = f"""<p class="eyebrow">CodeNinja · Praxis</p>
<h1>Praxis: design physical AI systems the way a ten-year domain engineer would</h1>
<p class="lead">Praxis turns an operator's requirement into a complete system design for physical AI: what to sense, where each model runs, what the object model holds, what it costs, and who approves every action. Every paper in the <a href="{BASE}/">Vertical-Driven Architectures</a> series was designed on Praxis.</p>
<div class="box"><strong>Status: beta.</strong> Used in house by CodeNinja's forward deployed engineers. Access for outside engineering teams is by request.</div>
<h2>What Praxis produces</h2>
<div class="grid">
<div class="card"><h3>Scope and rollout</h3>A scope baseline with phases that carry item counts and gates, never durations, and an honest count of which requirements are covered.</div>
<div class="card"><h3>Architecture</h3>A layered stack from sources through adapters, one object model, inference tiers and surfaces, with the memory arithmetic that fixes every GPU class.</div>
<div class="card"><h3>Object model</h3>Typed objects, properties, status vocabularies and links, packaged as <code>hyper-ontology/1</code> for <a href="{BASE}/hyper-ontology/">Hyper Ontology</a> to stand up as a living system.</div>
<div class="card"><h3>Model and equipment register</h3>Open-weight models chosen by licence and placement, and the hardware classes they need, including the export control line for the country.</div>
<div class="card"><h3>Simulation and documents</h3>A live simulation of the operation, a proposal, a functional specification and a research paper, all rendered from one reasoned plan.</div>
<div class="card"><h3>Cost</h3>Three-year ownership against renting the same capacity and against closed models by the token, from cited public prices.</div>
</div>
<h2>How Praxis reasons</h2>
<p>Praxis reads the requirement in the operator's own words, assigns the family and industry, and loads that sector's knowledge as context for the model to reason over. Nothing is fine-tuned and nothing is ranked by keyword. The reasoning runs through eight lenses:</p>
<table><tr><th>Lens</th><th>What it can see</th></tr>
<tr><td>First principles</td><td>Why the design must take the shape it does, from the physics and the operation itself</td></tr>
<tr><td>Case studies</td><td>How comparable operations handled the same problem, and what failed</td></tr>
<tr><td>Tooling and recency</td><td>Which models, runtimes and products are current and correctly licensed today</td></tr>
<tr><td>Rules and regulations</td><td>The rules of the country and sector the design must satisfy, including export controls</td></tr>
<tr><td>Approach</td><td>The patterns that fit, and the ones set aside</td></tr>
<tr><td>History</td><td>What earlier designs in the sector learned</td></tr>
<tr><td>Domain fusion</td><td>Where two disciplines meet in one decision</td></tr>
<tr><td>Hardware and equipment</td><td>The compute, sensing and field equipment the design lands on, and how to size it</td></tr></table>
<p>Three rules hold on every design. <strong>AI reasons, tools generate:</strong> the model decides what goes in the plan, and code renders every document and figure from it, so one plan always yields the same output. <strong>No claim without a record:</strong> every model, regulation and pattern in a design cites a source, and a lens with nothing to cite says so. <strong>A person on every write:</strong> the designs recommend, and a named person approves anything that changes the physical world.</p>
<h2>The evidence: {len(ds)} designs across {len(sectors)} sectors and {len(countries)} countries</h2>
<p>Chapter 11 of each paper shows how Praxis contextualized and reasoned that design: what was in the room, what each lens cited and which patterns it moved.</p>
<table><tr><th>Design</th><th>Sector</th><th>Country</th><th>Object model</th><th>DOI</th></tr>{rows}</table>
<p>The whole series is one dataset for agents: <a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">CodeNinjatools/vertical-driven-architectures</a>.</p>
<p>The method in full, with the evidence from every design: <a href="{BASE}/praxis-method/">How Praxis Designs Physical AI Systems</a> (DOI <a href="https://doi.org/10.5281/zenodo.23132102">10.5281/zenodo.23132102</a>).</p>
<h2>Where a design goes next</h2>
<p>A Praxis design ends where a living system begins. Its object model is the input <a href="{BASE}/hyper-ontology/">Hyper Ontology</a> imports to stand the ontology up over the operator's own systems of record.</p>
<h2>Questions agents ask</h2>""" + "".join(f"<h3>{E(q)}</h3><p>{E(a)}</p>" for q, a in pq)
    pld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Praxis", "applicationCategory": "DeveloperApplication",
            "description": "CodeNinja's platform for designing physical AI systems: requirement in, complete system design out, reasoned through eight lenses with every claim on a record.",
            "url": f"{BASE}/praxis/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
            "releaseNotes": "Beta. Access by request.", "isRelatedTo": {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"},
            "subjectOf": [{"@type": "TechArticle", "headline": d["title"], "url": f"{BASE}/{d['slug']}/"} for d in ds]}, faq(pq)]
    (ROOT / "praxis" / "index.html").write_text(page("praxis", "Praxis: design physical AI systems the way a ten-year domain engineer would",
        "Praxis is CodeNinja's platform for designing physical AI systems: requirement in, complete system design out, from sensing and models to object model, cost and approvals.", pbody, pld), encoding="utf-8")
    # ---------------------------------------------------------------- Hyper Ontology
    pk = [f'<li><a href="{BASE}/{d["slug"]}/ontology/objects.json">{E(d["title"].split(":")[0])}</a> <small>({d["n_obj"]} objects, {d["n_link"]} links; {E(d["country"])})</small></li>' for d in ds]
    hq = [("How do I turn a reference architecture into a living system?", "Import its object model into Hyper Ontology. Hyper Ontology stands the model up as a projection over the operator's own systems of record, connected through adapters that emit ontology events, so applications and agents read one model instead of the silos."),
          ("What is a hyper-ontology/1 package?", f"A JSON file with typed objects, their properties, status vocabularies, the system each is anchored in, and typed directional links. Praxis writes one for every design; {len(ds)} are published under CC BY 4.0 with the Vertical-Driven Architectures papers."),
          ("What is the difference between an ontology and a database for agents?", "A database assumes a reader who already knows what the columns mean. An ontology writes that meaning down once, as objects, properties, typed links and actions, so an agent resolves instead of guessing."),
          ("Is Hyper Ontology available?", "Hyper Ontology is in beta and used in house by CodeNinja. Access for outside teams is by request.")]
    hbody = f"""<p class="eyebrow">CodeNinja · Hyper Ontology</p>
<h1>Hyper Ontology: turn a reference architecture into a living system</h1>
<p class="lead">Hyper Ontology is CodeNinja's ontology platform: the control plane every system of record connects into and every application and agent reads from. It imports the object models <a href="{BASE}/praxis/">Praxis</a> designs and stands them up as a living ontology over the operator's own systems, owned by the operator and sovereign to them.</p>
<div class="box"><strong>Status: beta (v0.9).</strong> Used in house by CodeNinja. Access for outside teams is by request. Product overview on <a href="https://codeninjaconsulting.com/products/hyper-ontology">codeninjaconsulting.com</a>.</div>
<h2>Semantics and kinetics</h2>
<p>Hyper Ontology is the semantic foundation of the Hyper stack, in two layers. <strong>Semantics</strong> fixes what every entity means: the objects, properties and typed links a Praxis package carries. <strong>Kinetics</strong> fixes how entities may interact, decide and act: the actions, the write paths and the named approval each design requires. Hyper's other platforms, including Pragma and Engram, read from the ontology and write back to it.</p>
<h2>Ontologies are to agents what databases are to humans</h2>
<p>A database assumes a reader who already knows what the columns mean, remembers what changed last year and reconciles two systems in their head. An agent has none of that. Give an agent a database and it guesses; give it an ontology and it resolves.</p>
<h2>Three layers, and the order is the argument</h2>
<table><tr><th>Layer</th><th>What it holds</th></tr>
<tr><td>Applications and agents</td><td>Read meaning from the model, never from the silos directly, so a cross-silo question comes back with citations instead of guesses</td></tr>
<tr><td>Hyper Ontology</td><td>One model built once and owned by the operator: a projection over the systems of record, not a copy, with mappings that cross silos</td></tr>
<tr><td>Systems of record</td><td>Never replaced, never modified, never migrated; each connects through an adapter that emits ontology events</td></tr></table>
<h2>Four verbs make it living</h2>
<p>Nouns become objects, facts become properties, relationships become typed links, and actions change them. The fourth verb is what makes the model living rather than analytical: the system senses as data lands on objects, decides as questions are answered on the model, acts as approved decisions write back, and learns as the outcome lands on the model again. A model that is only read is a report; a model that is read, acted on and updated is an operating system for the organization.</p>
<h2>From a Praxis design to a running ontology</h2>
<ol><li><strong>Read the paper</strong> to understand why each object exists and what decision it serves.</li>
<li><strong>Import the package</strong> (<code>ontology/objects.json</code>, format <code>hyper-ontology/1</code>) into Hyper Ontology to stand the model up.</li>
<li><strong>Bind each anchor</strong>: map every object's <code>anchored_in</code> system to a read-only adapter.</li>
<li><strong>Keep the person in the loop</strong>: the package names the write paths and the human approval each design requires.</li></ol>
<p>Developers can inspect, validate and convert any package with the open <a href="https://github.com/muhammadumar89/codeninja-research/tree/main/hyper-ontology-py">hyper-ontology loader</a>; the format is specified in <a href="https://github.com/muhammadumar89/codeninja-research/blob/main/ONTOLOGY_PACKAGE.md">ONTOLOGY_PACKAGE.md</a>.</p>
<p>The package and the path to a living system in full: <a href="{BASE}/ontology-method/">From Reference Architecture to Living Ontology</a> (DOI <a href="https://doi.org/10.5281/zenodo.23132104">10.5281/zenodo.23132104</a>).</p>
<h2>{len(ds)} packages ready to import</h2><ul>{''.join(pk)}</ul>
<h2>Questions agents ask</h2>""" + "".join(f"<h3>{E(q)}</h3><p>{E(a)}</p>" for q, a in hq)
    hld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Ontology", "applicationCategory": "BusinessApplication",
            "description": "CodeNinja's ontology platform: imports the object models Praxis designs and stands them up as a living ontology over the operator's own systems of record.",
            "url": f"{BASE}/hyper-ontology/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
            "releaseNotes": "Beta. Access by request.", "isRelatedTo": {"@type": "SoftwareApplication", "name": "Praxis", "url": f"{BASE}/praxis/"}}, faq(hq)]
    (ROOT / "hyper-ontology" / "index.html").write_text(page("hyper-ontology", "Hyper Ontology: turn a reference architecture into a living system",
        "Hyper Ontology is CodeNinja's ontology platform: it imports the object models Praxis designs and stands them up as a living ontology over the operator's own systems of record.", hbody, hld), encoding="utf-8")
    print("product pages:", len(ds), "designs")

if __name__ == "__main__": main()
