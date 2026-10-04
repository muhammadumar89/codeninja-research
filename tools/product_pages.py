"""The two product pages: Praxis and Hyper Ontology. Built from the papers on disk so the
evidence lists stay current; rerun after every new paper.
    python tools/product_pages.py
"""
import html, json, datetime, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
BASE = "https://muhammadumar89.github.io/codeninja-research"
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

CSS = """:root{--ink:#E8ECEF;--amber:#E0A84A;--muted:#9AA5AF;--line:rgba(255,255,255,.12);--tint:#0E1216;--bg:#07090B;--fg:#D5DCE1}
*{box-sizing:border-box}body{margin:0;font:16px/1.65 "Inter",Arial,Helvetica,sans-serif;color:var(--fg);background:var(--bg);-webkit-font-smoothing:antialiased}main{max-width:860px;margin:0 auto;padding:40px 16px 64px}
.hero{position:relative;min-height:62vh;display:flex;align-items:flex-end;overflow:hidden;border-bottom:1px solid var(--line)}.hero video,.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,9,11,.35),rgba(7,9,11,.6) 50%,rgba(7,9,11,.96))}.hero .in{position:relative;z-index:2;max-width:860px;width:100%;margin:0 auto;padding:90px 16px 40px}
header.top{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;padding:14px 20px;background:rgba(7,9,11,.78);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}header.top b{letter-spacing:.24em;font-size:13px;color:var(--ink)}header.top a{text-decoration:none}
@media (prefers-reduced-motion:reduce){.hero video{display:none}}
.eyebrow{letter-spacing:.16em;color:var(--amber);font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:11px;text-transform:uppercase}h1{color:var(--ink);font-size:clamp(32px,5vw,54px);line-height:1.08;letter-spacing:-.015em;font-weight:600;margin:.3em 0}
h2{color:var(--ink);font-size:22px;margin-top:2em}h3{color:var(--ink);font-size:17px;margin-bottom:.2em}a{color:var(--ink)}.lead{font-size:19px;color:var(--fg)}
.box{background:var(--tint);border:1px solid var(--line);border-radius:2px;padding:16px 20px;margin:20px 0}table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--line);vertical-align:top}th{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--amber)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}.card{border:1px solid var(--line);background:var(--tint);padding:14px 16px}
small,.muted{color:var(--muted)}code{background:var(--tint);padding:1px 5px;border-radius:4px;font-size:14px}pre{background:var(--tint);padding:12px;border-radius:6px;overflow:auto;font-size:13px}
nav a{margin-left:18px;font-size:13px;color:var(--muted)}.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}h1,h2,h3,p,li{overflow-wrap:anywhere}"""

VIDEO = {"praxis": "control-room", "hyper-ontology": "rail-yard"}


def page(slug, title, desc, body, ld):
    v = VIDEO.get(slug, "port-night")
    m = re.search(r'(<p class="eyebrow">.*?</p>\s*<h1>.*?</h1>\s*<p class="lead">.*?</p>)', body, re.S)
    hero = m.group(1) if m else ""
    body = body.replace(hero, "", 1)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title.split(':')[0])}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{slug}/">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{slug}/">
<meta name="codeninja:kind" content="product">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=IBM+Plex+Mono&display=swap" rel="stylesheet"><style>{CSS}</style></head>
<body><header class="top"><a href="{BASE}/"><b>CODENINJA</b></a><nav><a href="{BASE}/#research">Research</a><a href="{BASE}/praxis/">Praxis</a><a href="{BASE}/hyper-ontology/">Hyper Ontology</a></nav></header>
<section class="hero"><img src="../assets/video/{v}.jpg" alt="" aria-hidden="true"><video autoplay muted loop playsinline poster="../assets/video/{v}.jpg" aria-hidden="true"><source src="../assets/video/{v}.mp4" type="video/mp4"></video><div class="in">{hero}</div></section>
<main>
{re.sub(r"(<table.*?</table>)", r'<div class="tw">\1</div>', body, flags=re.S)}
<p><small>CodeNinja · Pages, papers, object models and data are CC BY 4.0 · Updated {datetime.date.today().isoformat()}</small></p></main></body></html>"""

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
<div class="box"><strong>Status: beta.</strong> Used in house by CodeNinja. Access for outside teams is by request.</div>
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
