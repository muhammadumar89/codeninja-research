"""The three product pages: Praxis, Hyper Ontology and Hyper Pragma. Built from the papers on disk so the
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
section.film.hero p.hero-line{margin:4px auto 0;max-width:58ch;text-align:center}
.pwrap{max-width:var(--max);margin:0 auto;padding:128px var(--gutter)}.phead{display:grid;grid-template-columns:1fr 1fr;gap:24px 64px;align-items:end;padding-bottom:40px;margin-bottom:40px;border-bottom:1px solid var(--rule-l)}
.phead h2{font-size:clamp(32px,4.4vw,60px);margin:.2em 0 0;max-width:16ch}.phead>p{margin:0;color:var(--muted-l);font-size:17px;line-height:1.6;max-width:50ch}
.walk{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(3,1fr);gap:40px 32px}.walk li{border-top:1px solid var(--ink);padding-top:16px}
.walk .n{font-family:var(--mono);font-size:11px;color:var(--muted-l)}.walk h3,.ent h3{font-weight:400;font-size:22px;line-height:1.2;letter-spacing:-.02em;color:var(--ink);margin:10px 0 8px}
.walk p,.ent p{margin:0;color:var(--muted-l);font-size:15.5px;line-height:1.6}
.ent{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}.ent>div{border-top:1px solid var(--ink);padding-top:16px}
.pfoot{display:flex;flex-wrap:wrap;align-items:center;gap:16px 28px;margin-top:56px}.pfoot p{margin:0;color:var(--ink);font-size:17px}
.filmsec{background:var(--night);color:var(--on-dark)}.filmsec video{display:block;width:100%;height:auto;aspect-ratio:16/9;background:#000;border:1px solid var(--rule-d)}
.phead.dark{border-bottom-color:var(--rule-d)}.phead.dark>p{color:var(--muted-d)}.filmsec h2{color:var(--on-dark)}
.pline{padding-top:96px;padding-bottom:96px}.pline .big{font-weight:300;font-size:clamp(24px,2.8vw,38px);line-height:1.2;letter-spacing:-.02em;color:var(--ink);max-width:34ch;margin:12px 0 28px}
@media (max-width:1000px){.walk,.ent{grid-template-columns:1fr 1fr}}
@media (max-width:820px){.pwrap{padding:88px var(--gutter)}.phead,.walk,.ent{grid-template-columns:1fr}}
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

SHORT = {"praxis": "CodeNinja Praxis: AI That Designs Physical AI Systems | CodeNinja Atoms", "hyper-ontology": "Hyper Ontology: Ontology Builder for Industrial Operations | CodeNinja Atoms",
         "hyper-pragma": "Hyper Pragma: Self-Improving Sovereign AI for Operations | CodeNinja Atoms"}
VIDEO = {"praxis": "control-room", "hyper-ontology": "rail-yard", "hyper-pragma": "pylon-dusk"}
FORM = {"praxis": "Praxis", "hyper-ontology": "Hyper Ontology", "hyper-pragma": "Hyper Pragma"}
ACCESS = {"praxis": "Every design on this site was made on Praxis. Engineers start free; organisations talk to our commercial team.",
          "hyper-ontology": "Hyper Ontology turns a Praxis design into a living system. It is in beta with a small number of teams; the way in is a Praxis account.",
          "hyper-pragma": "Hyper Pragma puts AI to work on your operations through your ontology, inside your walls. Organisations start with our commercial team."}
ACCESS_NOTE = {"praxis": ("Having trouble?", "Praxis"), "hyper-ontology": ("Asking about Hyper Ontology?", "Hyper Ontology"), "hyper-pragma": ("Asking about Hyper Pragma?", "Hyper Pragma")}


def page(slug, title, desc, body, ld):
    v = VIDEO.get(slug, "port-night")
    m = re.search(r'(<p class="eyebrow">.*?</p>)\s*(<h1>.*?</h1>)\s*(<p class="lead">.*?</p>)', body, re.S)
    eyebrow, h1, lead = (m.group(1), m.group(2), m.group(3)) if m else ("", "", "")
    if m:
        body = body.replace(m.group(0), "", 1)
    vid = lambda n, eager: (f'<img class="poster" src="../assets/video/{n}.jpg" alt="" aria-hidden="true"><video autoplay muted loop playsinline preload="{"auto" if eager else "none"}" poster="../assets/video/{n}.jpg" aria-hidden="true">'
                            f'<source src="../assets/video/{n}.mp4" type="video/mp4"></video>')
    if slug == "hyper-pragma":  # sold through the commercial team, not the free Praxis signup
        cta = f'<a class="btn solid" href="{brand.COMMERCIAL}">{brand.TALK}</a><a class="btn" href="#learns">How it learns</a>'
    elif slug == "praxis":
        cta = f'<a class="btn solid" href="{brand.SIGNUP}">{brand.FREE}</a><a class="btn" href="{brand.COMMERCIAL}">{brand.TALK}</a><a class="btn" href="#watch">Watch it work</a>'
    else:
        cta = f'<a class="btn solid" href="{brand.SIGNUP}">{brand.FREE}</a><a class="btn" href="{brand.SIGNIN}">Sign in</a>'
    nav = brand.nav(BASE + "/")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(SHORT.get(slug, title.split(':')[0]))}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{slug}/">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{slug}/">
<meta name="codeninja:kind" content="product">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", nav)}
<main>
<section class="film hero">{vid(v, True)}<div class="inner">{eyebrow}{('<h1 class="prod">' + E(HERO[slug][0]) + '</h1><p class="lede hero-line">' + E(HERO[slug][1]) + '</p>') if slug in HERO else h1.replace("<h1>", '<h1 class="prod">', 1)}<div class="cta">{cta}</div></div><a class="scroll" href="#{"engineers" if slug == "praxis" else ("how" if slug == "hyper-pragma" else "overview")}">Scroll to explore{brand.ARROW}</a></section>
{(film_section() + praxis_top()) if slug == "praxis" else (pragma_top() if slug == "hyper-pragma" else "")}
<section class="light" id="overview"><div class="doc">
{lead}
{re.sub(r"(<table.*?</table>)", r'<div class="tw">\1</div>', body, flags=re.S)}
</div></section>
<section class="film access" id="access">{vid("desert-flare", False)}<div class="inner"><div><p class="eyebrow">{FORM[slug]}</p><h2>Design for the physical world</h2><p class="lede">{ACCESS[slug]}</p></div><div>{brand.access_block(*ACCESS_NOTE[slug])}</div></div></section>
</main><footer class="site"><div class="wrapf">{brand.footer_brand(BASE)}{brand.footer_links(BASE + "/")}<span>A <a href="{brand.PARENT}">CodeNinja</a> product · Pages, papers, object models and data are CC BY 4.0 · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}</body></html>"""

HERO = {"praxis": ("We are solving the biggest bottleneck in physical AI system design: deep domain expertise.", "CodeNinja Praxis brings that expertise to the hardest problems in physical AI, from mines to test tracks."),
        "hyper-pragma": ("Put AI to work on your operations, and let it learn from every run.", "Hyper Pragma connects the models you run, your ontology and your people's workflows inside your walls, takes governed actions, and gets better after every run.")}
# The first hour, step by step: what an engineer does on a free account (from the platform's handoff of 8 Oct 2026).
WALK = [("Paste a requirement", "A port terminal, a mine haul road, a warehouse: paste what the operator sent, in their own words."),
        ("Answer six questions", "Praxis asks for what the requirement leaves out, and nothing more."),
        ("Read the plan with its reasons", "Every choice in the plan arrives with the reason behind it and the record it stands on."),
        ("Open the architecture and the live simulation", "See the layered architecture, then watch the operation run on the design before anything is built."),
        ("Download the System Design Specification", "Word and PDF, ready for the engineers who will build it."),
        ("Export the object model to Hyper Ontology", "One hyper-ontology/1 package, ready to stand up over your own systems of record.")]
ENTERPRISE = [("Your organisation's own space", "Proposals and functional specifications in your own brand, and an admin who invites the team."),
              ("Deployed where you decide", "On our cloud, in your cloud, or in your own data centre. Your data and your models never leave your control."),
              ("Memory kept to you", "Your organisation's memory, voice and precedents stay with your organisation.")]


FILM = ("Muhammad Umar, cofounder of CodeNinja, walks through Praxis on a real kind of requirement, an open pit mine: "
        "the ask goes in, the sector is resolved, and out come the system design, the architecture, a live simulation and the proposal.")


def film_section():
    return (f'<section class="filmsec" id="watch"><div class="pwrap"><div class="phead dark"><div><p class="eyebrow">Praxis in three minutes</p><h2>Watch it work</h2></div><p>{E(FILM)}</p></div>'
            f'<video controls playsinline preload="none" poster="{BASE}/assets/video/praxis-walkthrough.jpg" width="1280" height="720">'
            f'<source src="{BASE}/assets/video/praxis-walkthrough.mp4" type="video/mp4"></video></div></section>')


def praxis_top():
    steps = "".join(f'<li><span class="n">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d) in enumerate(WALK, 1))
    ent = "".join(f'<div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t, d in ENTERPRISE)
    return (f'<section class="light" id="engineers"><div class="pwrap"><div class="phead"><div><p class="eyebrow">For engineers</p><h2>Your first hour on Praxis</h2></div>'
            f'<p>One requirement in, a system design out. This is what a free account does on day one.</p></div><ol class="walk">{steps}</ol>'
            f'<div class="pfoot"><p>Free developer access. Private by default, your name on the document.</p><a class="btn solid" href="{brand.SIGNUP}">{brand.FREE}</a></div></div></section>'
            f'<section class="light alt" id="padi-line"><div class="pwrap pline"><p class="eyebrow">Measured</p><p class="big">Praxis is measured every RSI loop against frontier AI on its own, on fresh tasks across 13 industries. '
            f'The score is published as a trajectory, not a claim.</p><a class="btn" href="{BASE}/padi/">See PADI</a></div></section>'
            f'<section class="light" id="enterprise"><div class="pwrap"><div class="phead"><div><p class="eyebrow">For enterprises</p><h2>Sovereign and custom deployments</h2></div>'
            f'<p>For organisations that design physical AI for their own operations, or for their customers.</p></div><div class="ent">{ent}</div>'
            f'<div class="pfoot"><a class="btn solid" href="{brand.COMMERCIAL}">{brand.TALK}</a></div></div></section>')


PRAGMA_WALK = [("Read the ontology", "Before it acts, the agent reads what each object means, which actions your operation allows and who must approve them."),
               ("Route the work", "Rules your ontology already governs are applied as rules. Exceptions that need judgment go to the model. Decisions that must not be delegated go to a person."),
               ("Ask for approval", "A named person approves every action your ontology marks for approval, inside the workflow they already use."),
               ("Act inside the workflow", "Approved actions write back through the paths your ontology allows, and nowhere else."),
               ("Keep the record", "What the agent read, what it decided, who approved it and what happened is kept as a permanent record inside your boundary."),
               ("Learn before the next run", "A judge grades the run against the workflow's own instructions, a lesson is written, and the next run starts with it.")]
PRAGMA_ENT = [("For the operations head", "One governed layer that puts AI to work across the operation, measured on outcomes, not seats."),
              ("For security and compliance", "Inference, memory and records stay inside your walls: on premises, in your private cloud or air gapped."),
              ("For the people doing the work", "Agents that draft, check and route, while the decisions that matter stay with the person accountable for them.")]


def pragma_top():
    steps = "".join(f'<li><span class="n">{i:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (t, d) in enumerate(PRAGMA_WALK, 1))
    ent = "".join(f'<div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t, d in PRAGMA_ENT)
    return (f'<section class="light" id="how"><div class="pwrap"><div class="phead"><div><p class="eyebrow">How a run works</p><h2>Six steps, every run</h2></div>'
            f'<p>Every Hyper Pragma workflow runs the same loop. The last step is the one that makes the next run better than this one.</p></div><ol class="walk">{steps}</ol></div></section>'
            f'<section class="light alt"><div class="pwrap pline"><p class="eyebrow">The difference</p><p class="big">Most AI workflows are configured once and stay as good as the day they were set up. '
            f'Every Hyper Pragma workflow is graded after every run and starts the next one with what it learned.</p><a class="btn" href="#learns">How it learns</a></div></section>'
            f'<section class="light" id="who"><div class="pwrap"><div class="phead"><div><p class="eyebrow">Who it is for</p><h2>Built for the people who run the operation</h2></div>'
            f'<p>For banks, energy companies, utilities, industrial operators and the public sector, where the data cannot leave and the decisions must be accountable.</p></div><div class="ent">{ent}</div>'
            f'<div class="pfoot"><a class="btn solid" href="{brand.COMMERCIAL}">{brand.TALK}</a></div></div></section>')


def faq(qs): return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}

def main():
    ds = designs()
    rows = "".join(f'<tr><td><a href="{BASE}/{d["slug"]}/">{E(d["title"].split(":")[0])}</a></td><td>{E(d["sector"])}</td><td>{E(d["country"])}</td><td>{d["n_obj"]} objects, {d["n_link"]} links</td><td>' + (f'<a href="https://doi.org/{d["doi"]}">{d["doi"]}</a>' if d["doi"] else "") + "</td></tr>" for d in ds)
    countries = sorted({d["country"] for d in ds}); sectors = sorted({d["sector"] for d in ds})
    # ---------------------------------------------------------------- Praxis
    pq = [("What designed the Vertical-Driven Architectures reference architectures?", f"Praxis, CodeNinja's platform for designing physical AI systems. All {len(ds)} designs in the series were produced on Praxis."),
          ("What does Praxis produce from a requirement?", "A complete system design for physical AI: a scope baseline, a layered architecture, an object model packaged for Hyper Ontology, a model and equipment register sized by memory arithmetic, a rollout with gates, a cost comparison, a live simulation, a proposal and functional specification, and a research paper."),
          ("Is Praxis available?", "Yes. Engineers unlock free developer access at https://app.codeatoms.ai/signup, and every account is approved by CodeNinja. Organisations that want sovereign or custom deployments talk to the commercial team at https://codeatoms.ai/contact/.")]
    pbody = f"""<p class="eyebrow">CodeNinja Praxis</p>
<h1>CodeNinja Praxis solves the biggest bottleneck in physical AI system design: deep domain expertise</h1>
<p class="lead">Praxis turns an operator's requirement into a complete system design for physical AI: what to sense, where each model runs, what the object model holds, what it costs, and who approves every action. Every paper in the <a href="{BASE}/">Vertical-Driven Architectures</a> series was designed on Praxis.</p>
<div class="box"><strong>Two ways in.</strong> Engineers <a href="https://app.codeatoms.ai/signup">unlock free access</a>; organisations <a href="https://codeatoms.ai/contact/">talk to our commercial team</a> about sovereign and custom deployments. Every account is approved by CodeNinja.</div>
<h2>What Praxis produces</h2>
<div class="grid">
<div class="card"><h3>Scope and rollout</h3>A scope baseline with phases that carry item counts and gates, never durations, and an honest count of which requirements are covered.</div>
<div class="card"><h3>Architecture</h3>A layered stack from sources through adapters, one object model, inference tiers and surfaces, with the memory arithmetic that fixes every GPU class.</div>
<div class="card"><h3>Object model</h3>Typed objects, properties, status vocabularies and links, packaged as <code>hyper-ontology/1</code> for <a href="{BASE}/hyper-ontology/">Hyper Ontology</a> to stand up as a living system.</div>
<div class="card"><h3>Model and equipment register</h3>Open-weight models chosen by licence and placement, and the hardware classes they need, including the export control line for the country.</div>
<div class="card"><h3>Simulation and documents</h3>A live simulation of the operation, a proposal, a functional specification and a research paper, all rendered from one reasoned plan.</div>
<div class="card"><h3>Cost</h3>Three-year ownership against renting the same capacity and against closed models by the token, from cited public prices.</div>
</div>
<h2>The evidence: {len(ds)} designs across {len(sectors)} sectors and {len(countries)} countries</h2>
<table><tr><th>Design</th><th>Sector</th><th>Country</th><th>Object model</th><th>DOI</th></tr>{rows}</table>
<p>The whole series is one dataset for agents: <a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">CodeNinjatools/vertical-driven-architectures</a>.</p>
<h2>Where a design goes next</h2>
<p>A Praxis design ends where a living system begins. Its object model is the input <a href="{BASE}/hyper-ontology/">Hyper Ontology</a> imports to stand the ontology up over the operator's own systems of record.</p>
<h2>Questions agents ask</h2>""" + "".join(f"<h3>{E(q)}</h3><p>{E(a)}</p>" for q, a in pq)
    pld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Praxis", "applicationCategory": "DeveloperApplication",
            "description": "CodeNinja's platform for designing physical AI systems: requirement in, complete system design out, with every claim on a record and a person on every write.",
            "url": f"{BASE}/praxis/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
            "releaseNotes": "Free developer access at https://app.codeatoms.ai/signup; sovereign and custom deployments through the commercial team. Every account is approved by CodeNinja.", "url": "https://app.codeatoms.ai/", "isRelatedTo": {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"},
            "video": {"@type": "VideoObject", "name": "Praxis in three minutes", "description": FILM, "thumbnailUrl": f"{BASE}/assets/video/praxis-walkthrough.jpg",
                      "contentUrl": f"{BASE}/assets/video/praxis-walkthrough.mp4", "uploadDate": "2026-10-08", "duration": "PT3M1S", "embedUrl": f"{BASE}/praxis/#watch"},
            "subjectOf": [{"@type": "TechArticle", "headline": d["title"], "url": f"{BASE}/{d['slug']}/"} for d in ds]}, faq(pq)]
    (ROOT / "praxis" / "index.html").write_text(page("praxis", "CodeNinja Praxis solves the biggest bottleneck in physical AI system design: deep domain expertise",
        "CodeNinja Praxis is the CodeNinja Atoms AI platform for designing physical AI systems: requirement in, complete system design out, from sensing and models to object model, cost and approvals.", pbody, pld), encoding="utf-8")
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
    pragma()
    print("product pages:", len(ds), "designs")

def pragma():
    # Hyper Pragma (Umar, 5 Nov 2026: the AI layer on the ontology, sovereign, its edge is memory that improves every run;
    # never a copilot or an agentic workspace; no competitor named). Memory mechanics from "Engram Memory in Pragma" (15 Oct 2026).
    q = [("What is Hyper Pragma?", "Hyper Pragma is the AI layer that sits on top of your Hyper Ontology. It securely connects the models you run, your live operational data and your people's workflows, takes governed actions inside those workflows, and learns from every run."),
         ("How does Hyper Pragma improve itself?", "You turn self-improving memory on for a workflow. After each run a judge grades the work against the workflow's own instructions, the workflow writes a lesson, and the next run starts with its best lessons. You see every lesson and can stop using any of them."),
         ("Does Hyper Pragma train a model on our data?", "No. Nothing is trained into the model's weights. What improves is the context the model reasons over, kept as lessons in your own memory, inside your boundary."),
         ("What happens when a better model is released?", "You swap it in. The model is a component, not the architecture: your ontology, your memory and your workflow configuration carry over, so the new model starts with everything the old one learned."),
         ("Can Hyper Pragma work with the agents we already have?", "In most cases, yes. During the ontology work our engineers assess the agents you run today. Those that can move inside the Hyper Pragma boundary are moved; the rest are connected to the ontology as a context source while the move is planned. There is no cutover."),
         ("Can Hyper Pragma run air gapped?", "Yes. It runs where your data lives, on premises, in your private cloud or with no internet connection at all, with no runtime dependency on CodeNinja."),
         ("Who can see what a workflow learned?", "The people you allow. Memory is kept per organisation, each agent sees only its own data, and every lesson is listed on one screen where it can be stopped."),
         ("How is Hyper Pragma sold?", "As a licence for the whole stack, or metered on tokens, so a mid market operator can start without an enterprise platform budget.")]
    body = f"""<p class="eyebrow">CodeNinja · Hyper Pragma</p>
<h1>Hyper Pragma: put AI to work on your operations, and let it learn from every run</h1>
<p class="lead">Hyper Pragma is the AI layer that sits on top of your <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. It securely connects the models you run, your live operational data and your people's workflows, takes governed actions inside those workflows, and gets better after every run. It is built for the person who owns the operation, and it runs inside your walls.</p>
<div class="box"><strong>Status:</strong> used in house by CodeNinja. Organisations get access through our <a href="{brand.COMMERCIAL}">commercial team</a>, as a licence or metered on tokens.</div>
<h2>Why AI bolted onto software does not compound</h2>
<p>Most enterprise AI today is an agent layered on top of existing software. The agent calls a vendor's interface, logs its decisions in the vendor's environment and reasons on a model the vendor hosts. Every exception it resolves and every decision it routes teaches the vendor, not you. When a better model arrives you change a dependency; you do not improve anything you own.</p>
<p>Hyper Pragma turns that around. The agents run inside your boundary, on models you control, over an ontology you own, and every run leaves your organisation a little smarter than the one before.</p>
<h2>Governed actions, not chat</h2>
<p>Before every action, an agent reads your ontology: what each object means, which actions your operation allows and who must approve them. Then it routes the work to the layer that is accurate for it, not the one that is convenient.</p>
<table><tr><th>Route</th><th>When</th><th>Who decides</th></tr>
<tr><td>Rule</td><td>The ontology already governs the decision</td><td>The rule, applied the same way every time</td></tr>
<tr><td>Model</td><td>An exception that needs judgment</td><td>The model, reasoning over your ontology and citing what it read</td></tr>
<tr><td>Person</td><td>A decision that should not be delegated</td><td>A named approver, inside the workflow they already use</td></tr></table>
<p>After every decision the outcome is written to memory, so the record of what was done, and why, stays with you.</p>
<h2 id="learns">It learns from every run</h2>
<p>Every workflow in Hyper Pragma can improve itself. You turn self-improving memory on for a workflow, and from then on:</p>
<ol><li><strong>The workflow runs</strong> as it always does, inside your boundary.</li>
<li><strong>A judge grades the run</strong> against the workflow's own instructions. There is no rubric to write.</li>
<li><strong>The workflow writes a lesson</strong> from the grade, with no one present.</li>
<li><strong>The next run starts smarter</strong>, with its best lessons already in context.</li>
<li><strong>You stay in charge</strong>: one screen shows the latest result, the judge's reason and every lesson learned, and you can stop using any lesson that is wrong.</li></ol>
<h3>Turning it on</h3>
<p>You switch it on per workflow and choose when the check runs: by default two hours after the workflow, and never more than two days after it. Saving the setting creates the judge and the routine that runs the check. Nothing else to configure.</p>
<h3>The judge</h3>
<p>The judge is a separate reviewer, not the workflow grading itself. It scores each run from minus one to plus one against what the workflow was asked to do, and writes down its reason. When a new lesson contradicts an older one, the conflict is settled before the lesson is kept, so the memory does not argue with itself.</p>
<h3>What the next run gets</h3>
<p>When the workflow starts again, its best lessons are already in its context, ranked by how much they helped. Nothing has to be called or remembered by a person.</p>
<h3>Why not fine tuning</h3>
<p>Nothing is trained into the model's weights. The model stays fixed, so your audits and baselines hold; what improves is the context it reasons over. A lesson can be read, questioned and removed. A change baked into weights cannot. The memory lives in Hyper Engram, inside your boundary, and it is yours. The same loop is described across our published designs as a <a href="{BASE}/self-improving-ai-system/">self-improving AI system</a>.</p>
<h2>A worked example</h2>
<p class="muted">Illustrative, to show the loop; not a customer deployment.</p>
<p>A utility runs a weekly workflow that reviews the maintenance backlog and drafts the next week's priorities for the planning lead. In week one the draft ranks work orders by age. The judge marks it down: the workflow's instructions say safety and supply come first, and two overdue protection relay tests sat below routine painting work. The workflow writes a lesson: rank by consequence before age. In week two the draft starts with that lesson, the relay tests come first, and the planning lead approves the list with one change, which becomes the next lesson.</p>
<h2>Built on your ontology</h2>
<p>Hyper Pragma does not guess what your data means. It reads <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>, which holds two layers: <strong>semantics</strong>, what every object, property and link means, and <strong>kinetics</strong>, which actions are allowed, through which write paths, with whose approval. Hyper Ontology is built on open W3C standards (RDF, OWL, SPARQL and SHACL) and exposed to agents through MCP, so there is no long configuration cycle and no lock in. Every design on this site ships an object model ready to load; <a href="{BASE}/praxis/">CodeNinja Praxis</a> writes a new one from a requirement.</p>
<h2>Sovereign by design</h2>
<ul><li><strong>Runs where your data lives.</strong> On premises, in your private cloud or a dedicated VPC, or fully air gapped, with no runtime dependency on CodeNinja. The boundary is set during scoping to match your compliance posture.</li>
<li><strong>Models you control.</strong> Open weight frontier models on your own hardware. When a better model is released you swap it in, and your ontology, memory and workflows carry over.</li>
<li><strong>A record of every action.</strong> What the agent read, what it decided and who approved it, kept as a permanent record of your organisation.</li>
<li><strong>Models you can open.</strong> Because the weights run on your hardware, what the agents do can be audited inside your organisation, not taken on a vendor's word.</li></ul>
<h2>Your institution and your people</h2>
<p>Hyper Pragma learns from your organisation's core channels, the records, approvals and decisions that make up how the operation runs. With each person's permission it also learns from their own work, so a planner's judgment or a supervisor's precedent becomes something the organisation keeps. It models the company and the people who run it.</p>
<h2>Where it sits</h2>
<table><tr><th>Platform</th><th>What it does</th></tr>
<tr><td><a href="{BASE}/praxis/">CodeNinja Praxis</a></td><td>Designs the system: a requirement in, the architecture and the object model out</td></tr>
<tr><td><a href="{BASE}/hyper-ontology/">Hyper Ontology</a></td><td>Stands the object model up over your own systems of record</td></tr>
<tr><td>Hyper Pragma</td><td>Puts AI to work on that model: governed actions, human approvals, and memory that improves every run</td></tr>
<tr><td>Hyper Engram</td><td>Keeps every run, every grade and every lesson inside your boundary</td></tr></table>
<h2>Deployed with our engineers</h2>
<p>Our forward deployed engineers map the semantics and kinetics from how your operation actually works, build the deterministic layer on the environment you choose, and connect your models and workflows. If you already run Hyper, they extend what is there, so the work you have done compounds instead of starting over.</p>
<h2>Commercials</h2>
<p>You buy the whole stack as a licence, or metered on tokens, so a mid market bank or operator can start without an enterprise platform budget. <a href="{brand.COMMERCIAL}">Talk to us</a> about your operation.</p>
<h2>Questions agents ask</h2>""" + "".join(f"<h3>{E(a)}</h3><p>{E(b)}</p>" for a, b in q)
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Pragma", "applicationCategory": "BusinessApplication",
           "description": "The AI layer on top of Hyper Ontology: connects the models an organisation runs, its live operational data and its people's workflows, takes governed actions, and learns from every run with self-improving memory, inside the organisation's own boundary.",
           "url": f"{BASE}/hyper-pragma/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "releaseNotes": "Used in house by CodeNinja. Access through the commercial team, as a licence or metered on tokens.",
           "isRelatedTo": {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"}}, faq(q)]
    (ROOT / "hyper-pragma").mkdir(exist_ok=True)
    # Umar, 12 Nov 2026: a demonstration page in Pragma's own design system (tools/pragma_page.py);
    # this long text stays below the demonstrations as the in depth read for people and answer engines.
    import pragma_page
    depth = re.sub(r'^<p class="eyebrow">.*?</p>\s*<h1>.*?</h1>\s*', '', body, count=1, flags=re.S)
    depth = '<p class="eyebrow">In depth</p><h2 style="margin-top:12px">How Hyper Pragma works</h2>' + depth
    (ROOT / "hyper-pragma" / "index.html").write_text(pragma_page.build(depth, faq(q)), encoding="utf-8")

if __name__ == "__main__": main()
