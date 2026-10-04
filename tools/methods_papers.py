"""The two methods papers, built from methods/evidence.json and the packages on disk.
    python3 tools/methods_papers.py            -> praxis-method/ and ontology-method/ (index.html + paper/*.html)
Then print each paper/*.html to PDF with headless Chrome (see build_pdfs below)."""
import html, json, subprocess, sys, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "hyper-ontology-py"))
from hyper_ontology import load, traverse
BASE = "https://muhammadumar89.github.io/codeninja-research"
E = lambda s: html.escape(str(s), quote=True)
EV = json.loads((ROOT / "methods" / "evidence.json").read_text())
O, LN, D = EV["order"], EV["lenses"], EV["designs"]
TODAY = "2026-10-04"

CSS = """@page{size:letter;margin:0.8in 0.85in}body{font:11pt/1.55 Arial,Helvetica,sans-serif;color:#222;max-width:760px;margin:0 auto;padding:32px 16px}
.eyebrow{font-size:9pt;letter-spacing:.16em;color:#B7791F;font-weight:700;text-transform:uppercase}h1{font-size:25pt;line-height:1.15;color:#1F3348;margin:.3em 0 .4em}
.sub{font-size:13pt;color:#3A4652}.authors{margin-top:14px;font-weight:700}.meta{color:#6B7683;font-size:9.5pt}
h2{font-size:15pt;color:#1F3348;margin:1.6em 0 .4em;page-break-after:avoid}h3{font-size:12pt;color:#1F3348;margin:1.1em 0 .3em;page-break-after:avoid}
.abstract{background:#F6F8FA;border-left:3px solid #B7791F;padding:12px 16px;margin:18px 0}table{width:100%;border-collapse:collapse;font-size:9pt;margin:10px 0 6px;page-break-inside:avoid}
th{font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:#B7791F;text-align:left;border-bottom:1.5px solid #1F3348;padding:5px 6px}td{border-bottom:1px solid #E3E7EC;padding:5px 6px;vertical-align:top}
.cap{font-size:9pt;color:#5B6673;margin:4px 0 16px}figure{margin:14px 0;page-break-inside:avoid}code,pre{font-family:Menlo,Consolas,monospace;font-size:8.6pt}pre{background:#F6F8FA;padding:10px;border-radius:4px;white-space:pre-wrap}
.refs li{margin-bottom:4px;font-size:9.5pt}a{color:#1F3348}.tw{overflow-x:auto}"""

def head(title, desc, url, pdf, kw):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)}</title>'
            f'<meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}"><meta name="codeninja:kind" content="method">'
            f'<meta name="citation_title" content="{E(title)}"><meta name="citation_author" content="CodeNinja Engineering Team"><meta name="citation_author" content="Umar Bilal">'
            f'<meta name="citation_publication_date" content="{TODAY.replace("-", "/")}"><meta name="citation_publisher" content="CodeNinja"><meta name="citation_abstract_html_url" content="{url}">'
            f'<meta name="citation_pdf_url" content="{pdf}"><meta name="citation_keywords" content="{E("; ".join(kw))}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">'
            f'<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":["TechArticle","ScholarlyArticle"],"headline":title,"description":desc,"url":url,"datePublished":TODAY,"author":[{"@type":"Organization","name":"CodeNinja"}],"keywords":kw,"license":"https://creativecommons.org/licenses/by/4.0/","about":[{"@type":"SoftwareApplication","name":"Praxis","url":BASE+"/praxis/"},{"@type":"SoftwareApplication","name":"Hyper Ontology","url":BASE+"/hyper-ontology/"}]})}</script>'
            f'<style>{CSS}</style></head><body>')

def svg_heatmap():
    cw, ch, lw, top = 92, 28, 168, 118
    w = lw + cw * len(O) + 10; h = top + ch * len(LN) + 10
    out = [f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Arial" role="img" aria-label="Sources each reasoning lens cited per design">']
    for j, k in enumerate(O):
        x = lw + j * cw + cw / 2
        out.append(f'<text x="{x}" y="{top-10}" font-size="9.5" text-anchor="start" transform="rotate(-40 {x} {top-10})" fill="#1F3348">{E(D[k]["name"])}</text>')
    for i, n in enumerate(LN):
        y = top + i * ch
        out.append(f'<text x="{lw-8}" y="{y+ch/2+4}" font-size="10.5" text-anchor="end" fill="#222">{E(n)}</text>')
        for j, k in enumerate(O):
            v = D[k]["lens"][n]; x = lw + j * cw
            if v == "gap":
                out.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" fill="#FBF3E4" stroke="#B7791F" stroke-dasharray="3 2"/><text x="{x+cw/2}" y="{y+ch/2+4}" font-size="10" text-anchor="middle" fill="#B7791F" font-weight="bold">gap</text>')
            else:
                a = min(1, 0.12 + v / 7)
                out.append(f'<rect x="{x+2}" y="{y+2}" width="{cw-4}" height="{ch-4}" fill="#1F3348" fill-opacity="{a:.2f}"/><text x="{x+cw/2}" y="{y+ch/2+4}" font-size="10.5" text-anchor="middle" fill="{"#fff" if v >= 4 else "#1F3348"}">{v}</text>')
    out.append("</svg>"); return "".join(out)

def svg_kinds():
    kinds = sorted({kd for k in O for kd in D[k]["kinds"]})
    cols = ["#1F3348","#3E6A8A","#7FA7C7","#B7791F","#D9B26A","#6B7683","#A9B3BE","#2F7D6D","#9C4F3A","#C9D6E2"]
    bw, gap, lw, top, sc = 64, 26, 40, 56, 14
    w = lw + len(O) * (bw + gap) + 20; maxv = max(D[k]["objects"] for k in O); h = top + maxv * sc + 70
    out = [f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Arial" role="img" aria-label="Object kinds per design">']
    for i, kd in enumerate(kinds):
        lx, ly = lw + (i % 5) * 110, 6 + (i // 5) * 16
        out.append(f'<rect x="{lx}" y="{ly}" width="10" height="10" fill="{cols[i]}"/><text x="{lx + 14}" y="{ly + 9}" font-size="10" fill="#222">{kd}</text>')
    base = top + maxv * sc
    for j, k in enumerate(O):
        x = lw + j * (bw + gap); y = base
        for i, kd in enumerate(kinds):
            n = D[k]["kinds"].get(kd, 0)
            if n:
                y -= n * sc; out.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{n*sc}" fill="{cols[i]}"/>')
        out.append(f'<text x="{x+bw/2}" y="{y-5}" font-size="10" text-anchor="middle" fill="#1F3348">{D[k]["objects"]}</text>')
        out.append(f'<text x="{x+bw/2}" y="{base+14}" font-size="9.5" text-anchor="middle" fill="#222">{E(D[k]["name"].split()[0])}</text><text x="{x+bw/2}" y="{base+26}" font-size="9.5" text-anchor="middle" fill="#222">{E(" ".join(D[k]["name"].split()[1:]))}</text>')
    out.append("</svg>"); return "".join(out)

def refs():
    return "<ol class='refs'>" + "".join(f'<li>CodeNinja Engineering Team and Umar Bilal. 2026. <em>{E(json.loads((ROOT/k/"ontology/objects.json").read_text())["paper"]["title"])}</em>. CodeNinja. <a href="https://doi.org/{D[k]["doi"]}">https://doi.org/{D[k]["doi"]}</a></li>' for k in O) + "</ol>"

def tot(f): return sum(f(D[k]) for k in O)

def praxis_paper():
    url = f"{BASE}/praxis-method/"; slug = "praxis-method-designing-physical-ai-systems"; pdf = f"{url}paper/{slug}.pdf"
    title = "How Praxis Designs Physical AI Systems: Method and Evidence from Seven Reference Architectures"
    desc = "The method behind the Vertical-Driven Architectures series: how Praxis turns an operator's requirement into a complete physical AI system design through eight reasoning lenses, and what seven published designs show about it."
    listed, read, cited = tot(lambda d: d["listed"]), tot(lambda d: d["read"]), tot(lambda d: sum(v for v in d["lens"].values() if v != "gap"))
    gaps = tot(lambda d: sum(1 for v in d["lens"].values() if v == "gap"))
    full = [k for k in O if D[k]["req_total"] and D[k]["req_covered"] == D[k]["req_total"]]
    hw = [k for k in O if D[k]["lens"]["Hardware and equipment"] != "gap" and D[k]["lens"]["Hardware and equipment"] >= 4]
    gap_by_lens = {n: sum(1 for k in O if D[k]["lens"][n] == "gap") for n in LN}
    t1 = "".join(f'<tr><td><a href="{D[k]["url"]}">{E(D[k]["name"])}</a></td><td>{E(D[k]["sector"])}</td><td>{E(D[k]["country"])}</td><td>{D[k]["listed"]:,}</td><td>{D[k]["read"]}</td>'
                 f'<td>{sum(v for v in D[k]["lens"].values() if v != "gap")}</td><td>{sum(1 for v in D[k]["lens"].values() if v == "gap")}</td><td>{D[k]["phases"]} / {D[k]["items"]}</td><td>{D[k]["req_covered"]} of {D[k]["req_total"]}</td></tr>' for k in O)
    body = f"""<p class="eyebrow">Vertical-Driven Architectures · Methods · Designed with Praxis · October 2026</p>
<h1>{E(title)}</h1><p class="sub">What it takes to design a system for the physical world, and how Praxis does it: the inputs, the eight reasoning lenses, the rules that hold on every design, and the evidence from seven published reference architectures.</p>
<p class="authors">CodeNinja Engineering Team · Umar Bilal</p><p class="meta">CodeNinja · {TODAY} · CC BY 4.0 · Web edition: <a href="{url}">{url}</a></p>
<div class="abstract"><strong>Abstract.</strong> Designing physical AI, for a port, a grid, a mill or a construction site, has always needed deep domain expertise: what to sense, where each model may run, which rules bind, what the hardware must hold and who must approve each action. Praxis is CodeNinja's platform for designing such systems. It reads an operator's requirement in the operator's own words, loads the sector's knowledge as context, reasons through eight lenses (first principles, case studies, rules and regulations, approach, tooling and recency, history, domain fusion, and hardware and equipment) and renders one validated plan into a complete design: scope and rollout, layered architecture, object model, model and equipment register, cost and a live simulation. Across the seven designs published in the Vertical-Driven Architectures series, covering {len({D[k]["sector"] for k in O})} sectors in {len({D[k]["country"] for k in O})} countries, Praxis listed {listed:,} records as candidate context and read {read} of them in full, its lenses cited {cited} sources, and {gaps} times a lens found nothing citable and said so instead of filling the gap. {len(full)} of the seven designs cover every recorded requirement through a rollout gate; the other two print their lower coverage as counted. Every design ships its object model as a <code>hyper-ontology/1</code> package that <a href="{BASE}/hyper-ontology/">Hyper Ontology</a> imports to stand up a living system.</div>

<h2>1. The problem: physical systems need a domain engineer's judgement</h2>
<p>A software system can be designed from its data model outward. A physical AI system cannot. Its first decisions are physical: whether detection must happen at the edge because the link drops in the storm that matters, whether a thermal camera crosses an export threshold, whether a 753 billion parameter model fits the GPUs the country can receive, whether a model may ever write to life-safety equipment. Those decisions have traditionally been made by engineers with a decade in one sector, and they are the reason designs for ports, grids, mills and sites take months to write and are rarely shared.</p>
<p>Praxis exists to make that judgement explicit, reproducible and fast: to design the system a ten-year domain engineer would, show the reasoning, and cite what justified each choice.</p>

<h2>2. What Praxis takes in</h2>
<p><strong>The requirement, in the operator's own words.</strong> Praxis reads the ask as written, often a published request for proposals, and does not paraphrase it before reasoning. The forward deployed engineer may pin what the requirement leaves open: the sector, a reference architecture, and the country the design is written for.</p>
<p><strong>The room.</strong> Praxis assigns the family and industry, then lists the sector's knowledge as candidate context: regulations, tooling and model records, approaches, case studies, history and hardware entries. Across the seven designs the room held between {min(D[k]["listed"] for k in O):,} and {max(D[k]["listed"] for k in O):,} records, and Praxis read between {min(D[k]["read"] for k in O)} and {max(D[k]["read"] for k in O)} of them in full. Nothing is ranked or filtered by keyword: the model reads and decides what applies. Nothing is fine-tuned: the knowledge rides as context, so a design in a new sector needs a thicker room, not a new model.</p>

<h2>3. How Praxis reasons: eight lenses</h2>
<table><tr><th>Lens</th><th>The question it answers</th></tr>
<tr><td>First principles</td><td>Why must the design take this shape, from the physics and the operation itself?</td></tr>
<tr><td>Case studies</td><td>How did comparable operations handle this problem, and what failed?</td></tr>
<tr><td>Rules and regulations</td><td>Which rules of this country and sector bind the design, including export controls?</td></tr>
<tr><td>Approach</td><td>Which patterns fit, which are set aside, and why?</td></tr>
<tr><td>Tooling and recency</td><td>Which models, runtimes and products are current and correctly licensed today?</td></tr>
<tr><td>History</td><td>What did earlier designs in this sector learn?</td></tr>
<tr><td>Domain fusion</td><td>Where do two disciplines meet in one decision?</td></tr>
<tr><td>Hardware and equipment</td><td>Which compute, sensing and field equipment does the design land on, and how is it sized?</td></tr></table>
<p class="cap">Table 1. The eight lenses. Each returns either a contribution with sources the design can cite, or a gap stated in a sentence.</p>
<p>Three rules hold on every design. <strong>AI reasons, tools generate:</strong> the model writes one validated plan, and code renders every document, figure and simulation from it, so one plan always yields the same output. <strong>No claim without a record:</strong> a model, regulation or pattern survives into a design only if a source supports it, and a lens with nothing to cite says so. <strong>A person on every write:</strong> designs recommend; a named person approves anything that changes a plan, a schedule or a piece of equipment.</p>

<h2>4. What Praxis produces</h2>
<p>From one plan Praxis renders a scope baseline whose phases carry item counts and gates rather than durations; a layered architecture from sources through adapters, one object model, inference tiers and surfaces; the object model as a <code>hyper-ontology/1</code> package; a model and equipment register in which every GPU class follows from memory arithmetic (parameters times bytes per parameter, plus a factor for cache and activations, against the memory of the class the country can receive); a three-year cost comparison from cited public prices; a live simulation; a proposal and functional specification; and the research paper. Chapter 11 of every paper in the series is the reasoning record of that design.</p>

<h2>5. Evidence from seven designs</h2>
<div class="tw"><table><tr><th>Design</th><th>Sector</th><th>Country</th><th>Listed</th><th>Read in full</th><th>Cited</th><th>Gaps</th><th>Phases / items</th><th>Requirements covered</th></tr>{t1}</table></div>
<p class="cap">Table 2. What Praxis read and cited for each design, and the coverage each design prints. Listed and read in full are the room; cited is the sum across the eight lenses; gaps counts lenses that found nothing citable.</p>
<figure>{svg_heatmap()}<figcaption class="cap">Figure 1. Sources each lens cited, per design. A dashed cell is a lens that found nothing citable in the room and said so.</figcaption></figure>
<h3>What the evidence shows</h3>
<p><strong>Praxis reads about one record in ten in full.</strong> Across the series it read {read} of {listed:,} listed records ({100*read/listed:.0f} percent). The rest stay available as titles; the model chooses which to open, and the choice is recorded.</p>
<p><strong>Hardware is never an afterthought.</strong> The hardware and equipment lens cited four or more sources in {len(hw)} of the seven designs. It is the lens that fixes whether a frontier model runs on one node of eight 141 GB GPUs, whether vision runs on a Jetson Orin class edge box in a solar enclosure, or whether the design buys no compute at all, as in the port and factory designs.</p>
<p><strong>Gaps are stated, not filled.</strong> {gaps} lens results across the series are gaps: {", ".join(f"{n.lower()} {c}" for n, c in gap_by_lens.items() if c)}. They mark where the sector's knowledge is thin today, most often in case studies, and they are printed in the paper rather than papered over with a plausible source.</p>
<p><strong>Coverage is counted, not asserted.</strong> {len(full)} designs close every recorded requirement through a rollout gate. Structure Phase Watch covers two of seven and states that five sit outside its baseline as later scope. Sovereign HSE Watch prints none of twelve as covered by a gate. Both numbers are the platform's count, published as counted.</p>

<h2>6. Where people stay in the loop</h2>
<p>The forward deployed engineer pins what the requirement leaves open and reviews every design before it leaves. Every design names its write paths and the person who approves each. Before publication a separate gate reads every paper, figure and file for operator names, near identifiers and claims that will not survive scrutiny, such as an export control statement for the wrong country group, and the paper does not ship until it passes.</p>

<h2>7. Limits</h2>
<p>The designs are reference architectures, not quotations: hardware prices are public list prices on a stated date, and counts such as users or installation points are assumptions printed where they are used. The quality of a design follows the thickness of the sector's room; the gaps in Figure 1 are where it is thinnest today. Praxis is in beta, used in house by CodeNinja's forward deployed engineers; access for outside teams is by request at <a href="{BASE}/praxis/">{BASE}/praxis/</a>.</p>

<h2>References</h2>{refs()}"""
    return slug, title, desc, url, pdf, body, ["Praxis","physical AI","system design","reference architecture","domain expertise","reasoning lenses","sovereign AI","forward deployed engineering","ontology"]

def ontology_paper():
    url = f"{BASE}/ontology-method/"; slug = "from-reference-architecture-to-living-ontology"; pdf = f"{url}paper/{slug}.pdf"
    title = "From Reference Architecture to Living Ontology: the hyper-ontology/1 Package and Hyper Ontology"
    desc = "How a Praxis design's object model is packaged as hyper-ontology/1, what seven published packages contain, how to load and convert them, and how Hyper Ontology stands a package up as a living system over an operator's own systems of record."
    objs, links = tot(lambda d: d["objects"]), tot(lambda d: d["links"])
    kinds = {}
    for k in O:
        for kd, n in D[k]["kinds"].items(): kinds[kd] = kinds.get(kd, 0) + n
    t1 = "".join(f'<tr><td><a href="{D[k]["url"]}ontology/objects.json">{E(D[k]["name"])}</a></td><td>{E(D[k]["country"])}</td><td>{D[k]["objects"]}</td><td>{D[k]["links"]}</td><td>{D[k]["anchors"]}</td><td>{E(D[k]["focal"])} ({D[k]["focal_deg"]} links)</td></tr>' for k in O)
    port = load(ROOT / "port-digital-twin-us/ontology/objects.json"); reach = traverse(port, "berth", 2)
    steel = load(ROOT / "steel-production-count-pakistan/ontology/objects.json"); reach2 = traverse(steel, "count_event", 2)
    body = f"""<p class="eyebrow">Vertical-Driven Architectures · Methods · Hyper Ontology · October 2026</p>
<h1>{E(title)}</h1><p class="sub">Every design Praxis produces ends in an object model. This paper specifies the package that carries it, measures the seven published packages, shows how to load them, and describes how Hyper Ontology turns one into a living system.</p>
<p class="authors">CodeNinja Engineering Team · Umar Bilal</p><p class="meta">CodeNinja · {TODAY} · CC BY 4.0 · Web edition: <a href="{url}">{url}</a></p>
<div class="abstract"><strong>Abstract.</strong> Ontologies are to agents what databases are to humans: a database assumes a reader who already knows what the columns mean, while an ontology writes that meaning down once, as objects, properties, typed links and actions, so an agent resolves instead of guessing. Every system design reasoned on <a href="{BASE}/praxis/">Praxis</a> ends in such a model, packaged as <code>hyper-ontology/1</code>: typed objects with properties and status vocabularies, the system of record each is anchored in, typed directional links, the write paths and the human approval the design requires. Seven packages are published with the Vertical-Driven Architectures series, holding {objs} objects and {links} typed links across {len(kinds)} object kinds. An open, dependency-free loader validates them and converts them to Mermaid, Cypher and JSON-LD. <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>, CodeNinja's ontology platform, imports a package and stands it up as a projection over the operator's own systems of record, connected through adapters that emit ontology events, with actions that write back under approval, so the model senses, decides, acts and learns.</div>

<h2>1. Why the design ends in an ontology</h2>
<p>A physical operation's meaning is scattered: the berth window lives in the port community system, the channel depth in the survey archive, the lease in the finance backbone. Every report, application and agent that reads the silos directly re-derives the business, and derives it slightly differently. A design that ends in an object model fixes the meaning once. Praxis therefore treats the object model as the join the systems never made, and every paper in the series has a chapter that names each object, its anchor and its links.</p>

<h2>2. The package</h2>
<pre>{{"package": "hyper-ontology/1", "designed_with": "Praxis", "implemented_with": "Hyper Ontology",
 "paper": {{"title": "...", "url": "...", "doi": "..."}}, "sector": "...", "country": "...",
 "objects": [{{"id": "berth", "label": "Berth", "kind": "asset", "anchored_in": "Port Community System",
   "properties": ["Berth ID", "Alongside depth", "Berth window"], "status_vocabulary": ["Occupied", "Reserved", "Available"],
   "links": [{{"to": "navigation_channel", "label": "adjoins"}}]}}],
 "write_paths": ["..."], "human_loop": "..."}}</pre>
<p><strong>Objects</strong> carry an id, a label and one of ten kinds: asset, record, event, person, actor, site, material, measure, document and system. <strong>anchored_in</strong> names the system of record the object is read from, or says the object is born in the design itself, such as a decision record. <strong>Links</strong> are typed and directional; the reverse is implied. A link whose label a paper's figure could not print carries a <code>note</code> instead of an invented label. <strong>write_paths</strong> and <strong>human_loop</strong> carry the design's rules about what may change the world and who approves it. Nothing in a package names the operator; the same gate that reads the paper reads the package. The full specification is <a href="https://github.com/muhammadumar89/codeninja-research/blob/main/ONTOLOGY_PACKAGE.md">ONTOLOGY_PACKAGE.md</a>.</p>

<h2>3. Seven packages in numbers</h2>
<div class="tw"><table><tr><th>Design</th><th>Country</th><th>Objects</th><th>Links</th><th>Systems anchored</th><th>Most-linked object</th></tr>{t1}</table></div>
<p class="cap">Table 1. The seven published packages. Systems anchored counts the distinct systems of record the objects are read from.</p>
<figure>{svg_kinds()}<figcaption class="cap">Figure 1. Objects per design by kind. Assets and records dominate, and every design carries at least one event: a moment that happens and that the model must record.</figcaption></figure>
<p>Across the series: {", ".join(f"{n} {kd}" for kd, n in sorted(kinds.items(), key=lambda x: -x[1]))}. The most-linked object is where the design's questions meet: the berth in the port twin, the feeder segment in the wildfire design, the container in the terminal design, the pour on the construction site.</p>

<h2>4. Reach: what a query on the model can traverse</h2>
<p>The value of an ontology is the traversal a document store cannot make. From one berth in Port Twin, two hops of typed links reach:</p>
<pre>{E(chr(10).join(reach[:10]))}</pre>
<p>From one production count event in Steel Count Ledger:</p>
<pre>{E(chr(10).join(reach2[:10]))}</pre>
<p class="cap">Both listings are the output of <code>hyper-ontology reach</code> on the published packages.</p>

<h2>5. Loading a package</h2>
<pre>pip install "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=hyper-ontology-py"
hyper-ontology list
hyper-ontology show port-digital-twin-us
hyper-ontology validate steel-production-count-pakistan
hyper-ontology cypher truck-turn-container-terminal-us &gt; load.cypher
hyper-ontology mermaid factory-fire-monitoring-saudi-arabia &gt; model.mmd</pre>
<p>The loader has no dependencies, validates kinds, ids and link targets, and converts a package to a Mermaid class diagram, a Cypher script for a graph database, or JSON-LD for a triple store. All seven published packages validate. The loader reads and converts the schema; it does not connect to live systems.</p>

<h2>6. What Hyper Ontology adds</h2>
<p>A package is the schema of a design. Hyper Ontology makes it living. It stands the model up in three layers, and the order is the argument: systems of record below, never replaced, modified or migrated; the ontology in the middle, built once and owned by the operator, as a projection over those systems rather than a copy; applications and agents on top, reading meaning from the model and never from the silos directly. Each anchored system connects through an adapter that emits ontology events, so the integration contract is the event, not a vendor's payload, and a system can be replaced without touching anything above the adapter.</p>
<p>The model has a grammar of four verbs: nouns become objects, facts become properties, relationships become typed links, and actions change them. The fourth is what makes the model living: it senses as data lands on objects, decides as questions are answered on the model, acts as approved decisions write back, and learns as the outcome lands on the model again. The package's write paths and human loop become the rules on those actions: a recommendation is a record, and a named person's approval is what turns it into a change.</p>

<h2>7. Limits</h2>
<p>A package is schema, not data: it names what the model holds and how it links, not the records of any operator. Status vocabularies a design left at a default were dropped rather than invented, and links a figure could not label are kept with a note. Hyper Ontology is in beta and used in house by CodeNinja; access for outside teams is by request at <a href="{BASE}/hyper-ontology/">{BASE}/hyper-ontology/</a>.</p>

<h2>References</h2>{refs()}"""
    return slug, title, desc, url, pdf, body, ["Hyper Ontology","ontology","living ontology","knowledge graph","hyper-ontology/1","physical AI","reference architecture","digital twin","Praxis","sovereign AI"]

def main():
    for folder, fn in (("praxis-method", praxis_paper), ("ontology-method", ontology_paper)):
        slug, title, desc, url, pdf, body, kw = fn()
        page = head(title, desc, url, pdf, kw) + body + "</body></html>"
        (ROOT / folder / "paper" / f"{slug}.html").write_text(page, encoding="utf-8")
        nav = f'<p class="meta"><a href="{BASE}/">CodeNinja Research</a> · <a href="{BASE}/praxis/">Praxis</a> · <a href="{BASE}/hyper-ontology/">Hyper Ontology</a> · <a href="paper/{slug}.pdf">PDF</a></p>'
        (ROOT / folder / "index.html").write_text(head(title, desc, url, pdf, kw) + nav + body + "</body></html>", encoding="utf-8")
        print(folder, len(body.split()), "words")

if __name__ == "__main__": main()
