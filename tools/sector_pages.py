"""Sector question pages: /sectors/<sector>/ answers the six questions an engineer asks an AI
assistant about physical AI in that sector, in short answers and tables built ONLY from the
published designs (each design's At a glance table, its model register and its cost lines).
Nothing is written here that a paper does not say. /sectors/ lists every sector.
    python tools/sector_pages.py        # before site_index.py (which runs seo.py last)
"""
import html, json, re, datetime
from collections import defaultdict
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)

# One plain, true sentence per sector on why the question matters there. Sector facts only.
WHY = {
    "agriculture and earth observation": "Farms, irrigation and land use are watched by sensors, satellites and aircraft, but the readings, the licences and the field records usually sit in separate systems.",
    "energy and utilities": "Grids and plants run on control systems, maintenance records and field crews that were never designed to share one picture of risk.",
    "heavy industry and construction": "Mills, factories and building sites produce counts, alarms and progress data in many systems, and each one sees only part of the operation.",
    "maritime and ports": "Terminals and port authorities run gates, cranes, yards and finance on separate systems, so nobody sees the whole flow of a box or a truck.",
    "oil and gas": "Wells, terminals and plants hold safety, inventory and process data in systems that were never joined, often on sites where the data may not leave the country.",
}


def md_inline(s):
    s = E(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def plain(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)


def glance(folder):
    p = ROOT / folder / "paper" / "at_a_glance.md"
    if not p.exists():
        return {}, ""
    t = p.read_text(encoding="utf-8")
    rows = {m.group(1).strip(): m.group(2).strip() for m in re.finditer(r"^\| ([^|]+) \| (.+) \|$", t, re.M) if m.group(1).strip() not in ("Part", "---")}
    m = re.search(r"\*\*What this is\.\*\*\s*(.+?)(?:\n\n|$)", t, re.S)
    what = m.group(1).strip() if m else ""
    what = re.sub(r"^An open reference architecture for system design in physical AI:\s*", "", what)
    what = what.split(" It is written for")[0].strip()
    return rows, what


def load():
    rd = lambda n: [json.loads(l) for l in (ROOT / "dataset" / f"{n}.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    designs, models, costs = rd("designs"), rd("models"), rd("costs")
    by = defaultdict(list)
    for d in designs:
        f = d["design_id"]
        if not (ROOT / f / "ontology" / "objects.json").exists():
            continue
        pkg = json.loads((ROOT / f / "ontology" / "objects.json").read_text(encoding="utf-8"))
        rows, what = glance(f)
        by[d["sector"]].append({**d, "short": d["title"].split(":")[0], "url": f"{BASE}/{f}/", "rows": rows, "what": what,
                                "objects": [o["label"] for o in pkg["objects"]], "n_links": sum(len(o.get("links", [])) for o in pkg["objects"]),
                                "models": [m for m in models if m["design_id"] == f], "costs": [c for c in costs if c["design_id"] == f]})
    return by


def an(w):
    return "an" if w[:1].lower() in "aeiou" else "a"


def stop(t):
    t = plain(t).strip()
    return t if t.endswith((".", "!", "?")) else t + "."


def slug(sector):
    return sector.replace(" and ", "-and-").replace(" ", "-")


COMPUTE = ["Compute", "Frontier compute", "Edge", "Stack", "Ground", "Acquisition", "Equipment, per factory", "Field scope", "Boundary", "The hard dependency"]
COST = ["Three-year cost", "Three-year cost, owned", "Three-year cost, rented", "Three-year cost, 100 factories", "Closed model break-even"]


def table(head, rows):
    if not rows:
        return ""
    return ('<div class="tw"><table><thead><tr>' + "".join(f"<th>{E(h)}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


def link(d):
    return f'<a href="{d["url"]}">{E(d["short"])}</a>'


def qa(sector, ds):
    S = sector
    out = []
    # 1. what it looks like
    lead = (f"A complete physical AI design for {S} names what to sense, which existing systems to join, the object model that joins them, "
            f"the models and hardware, the three-year cost and the person who approves every action. CodeNinja Atoms has published "
            f"{len(ds)} such reference architecture{'s' if len(ds) != 1 else ''} for {S}, each free to reuse under CC BY 4.0.")
    body = table(["Design", "Country", "What it does"], [[link(d), E(d["country"]), md_inline(d["what"])] for d in ds])
    out.append((f"What does a physical AI system for {S} look like?", lead, body,
                lead + " " +  " ".join(f"{d['short']} ({d['country']}): {stop(d['what'])}" for d in ds)))
    # 2. models
    lead = (f"Each published {S} design names its models and why, and every model is open-weight or no model is used at all, "
            "so the operator can run it on hardware it owns.")
    rows = [[link(d), md_inline(d["rows"].get("Models", ""))] for d in ds]
    detail = table(["Design", "Choice", "What was picked", "Why"], [[link(d), E(m["choice"]), E(m["picked"]), E(m["why"])] for d in ds for m in d["models"]])
    out.append((f"Which AI models can {an(S)} {S} operator run on its own hardware?", lead, table(["Design", "Models"], rows) + detail,
                lead + " " +  " ".join(f"{d['short']}: {stop(d['rows'].get('Models', ''))}" for d in ds)))
    # 3. compute
    rows = [[link(d), E(k), md_inline(d["rows"][k])] for d in ds for k in COMPUTE if k in d["rows"]]
    lead = f"The compute follows from the models: the published {S} designs size it as follows, from no new hardware to a full GPU node."
    out.append((f"How much compute and hardware does AI in {S} need?", lead, table(["Design", "Part", "The design"], rows),
                lead + " " +  " ".join(f"{r[0]}, {r[1].lower()}: {stop(r[2])}" for r in [[d['short'], k, d['rows'][k]] for d in ds for k in COMPUTE if k in d['rows']])))
    # 4. cost
    rows = [[link(d), E(k), md_inline(d["rows"][k])] for d in ds for k in COST if k in d["rows"]]
    lead = (f"Each {S} design prices three years of ownership in its Appendix A, with every price cited, against renting the same "
            "capacity from a cloud region at its deepest three-year commitment where hardware is bought.")
    out.append((f"Is it cheaper to own AI hardware or rent cloud GPUs in {S}?", lead, table(["Design", "Line", "Three years"], rows),
                lead + " " +  " ".join(f"{d['short']}: " + "; ".join(f"{k.lower()}, {plain(d['rows'][k])}" for k in COST if k in d['rows']) + "." for d in ds)))
    # 5. ontology
    lead = (f"The object model is the part that makes the system an ontology rather than a pipeline: typed objects for the things in the "
            f"{S} operation, with properties, status values and typed links. Every published design ships its object model as "
            "hyper-ontology/1 JSON that loads into Hyper Ontology.")
    rows = [[link(d), f'{len(d["objects"])} objects, {d["n_links"]} links', E(", ".join(d["objects"])), f'<a href="{d["url"]}ontology/objects.json">objects.json</a>'] for d in ds]
    out.append((f"What ontology or object model does {an(S)} {S} AI system need?", lead, table(["Design", "Size", "Objects", "Download"], rows),
                lead + " " + " ".join(f"{d['short']}: {', '.join(d['objects'])}." for d in ds)))
    # 6. human control
    lead = f"In every published {S} design a named person makes the decision that changes the physical world; the system prepares it."
    rows = [[link(d), md_inline(d["rows"].get("Human control", ""))] for d in ds]
    out.append((f"Who approves the decisions an AI system makes in {S}?", lead, table(["Design", "Human control"], rows),
                lead + " " +  " ".join(f"{d['short']}: {stop(d['rows'].get('Human control', ''))}" for d in ds)))
    return out


CSS = """
.doc{max-width:1040px;margin:0 auto;padding:128px var(--gutter) 112px;font-size:17px;line-height:1.66;color:rgba(30,31,43,.88)}
.doc h1{font-weight:300;font-size:clamp(36px,4.8vw,64px);line-height:1.04;letter-spacing:-.032em;color:var(--ink);margin:0 0 24px;max-width:22ch}
.doc .lead{font-family:var(--serif);font-weight:300;font-size:clamp(21px,2.2vw,28px);line-height:1.38;color:var(--ink);margin:0 0 20px;max-width:46ch}
.doc .toc{list-style:none;padding:0;margin:40px 0 0;border-top:1px solid var(--ink)}.doc .toc li{border-bottom:1px solid var(--rule-l);padding:12px 0}
.doc .toc a{color:var(--ink);text-decoration:none}.doc .toc a:hover{text-decoration:underline}
.doc h2{font-size:clamp(24px,2.7vw,34px);line-height:1.15;letter-spacing:-.024em;color:var(--ink);max-width:30ch;margin:96px 0 18px;padding-top:24px;border-top:1px solid var(--ink)}
.doc p.ans{font-size:18.5px;color:var(--ink);max-width:62ch;margin:0 0 20px}
.doc a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:3px}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:20px 0 28px}
table{width:100%;border-collapse:collapse;font-size:14.5px;line-height:1.5}th,td{text-align:left;padding:12px 14px 12px 0;border-bottom:1px solid var(--rule-l);vertical-align:top}
th{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);border-bottom:1px solid var(--ink)}
td:first-child{white-space:nowrap;color:var(--ink)}
.doc .src{font-size:14px;color:var(--muted-l);margin-top:64px;border-top:1px solid var(--rule-l);padding-top:16px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:28px;margin-top:40px}.cards a.c{display:block;border-top:1px solid var(--ink);padding-top:14px;text-decoration:none;color:var(--ink)}
.cards a.c h3{font-weight:400;font-size:22px;letter-spacing:-.02em;margin:0 0 8px}.cards a.c p{margin:0;color:var(--muted-l);font-size:15px}
@media (max-width:820px){.doc{padding:96px var(--gutter) 72px;font-size:16px}td:first-child{white-space:normal}}
body{background:var(--paper)}html.js header.top:not(.solid):not(.open){background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d)}
"""


def shell(path, title, desc, body, ld):
    nav = [("Research", f"{BASE}/#research"), ("Sectors", f"{BASE}/sectors/"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"), ("About", f"{BASE}/about/")]
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{path}">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", nav, access=f"{BASE}/praxis/#access")}
<main class="light"><div class="doc">{body}</div></main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Pages, papers, object models and data are CC BY 4.0 · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}</body></html>"""


def main():
    by = load()
    today = datetime.date.today().isoformat()
    cards = []
    for sector in sorted(by):
        ds = by[sector]
        s = slug(sector)
        name = sector[:1].upper() + sector[1:]
        qs = qa(sector, ds)
        countries = sorted({d["country"] for d in ds})
        title = f"Physical AI for {name}: Questions Answered | CodeNinja Atoms"
        desc = (f"How to design sovereign physical AI for {sector}: models, compute, three-year cost, ontology and human control, "
                f"answered from {len(ds)} published reference architectures ({', '.join(countries)}).")[:300]
        toc = "".join(f'<li><a href="#q{i+1}">{E(q)}</a></li>' for i, (q, *_rest) in enumerate(qs))
        secs = "".join(f'<section id="q{i+1}"><h2>{E(q)}</h2><p class="ans">{E(lead)}</p>{body}</section>' for i, (q, lead, body, _t) in enumerate(qs))
        body = (f'<p class="eyebrow">Sector · {E(name)}</p><h1>Physical AI for {E(sector)}</h1>'
                f'<p class="lead">{E(WHY.get(sector, ""))} These are the questions engineers ask first, answered from {len(ds)} published CodeNinja Atoms reference architecture{"s" if len(ds) != 1 else ""}.</p>'
                f'<ol class="toc">{toc}</ol>{secs}'
                f'<p class="src">Every answer on this page is drawn from the papers linked in it: each paper\'s At a glance table, model register and cost appendix. '
                f'Full text for agents: <a href="{BASE}/llms-full.txt">llms-full.txt</a>. Designed on <a href="{BASE}/praxis/">Praxis</a>; object models load into <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>.</p>')
        faq = {"@context": "https://schema.org", "@type": "FAQPage", "url": f"{BASE}/sectors/{s}/", "name": title,
               "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t[:1800]}} for q, _l, _b, t in qs]}
        art = {"@context": "https://schema.org", "@type": "TechArticle", "headline": f"Physical AI for {sector}: questions answered", "description": desc,
               "url": f"{BASE}/sectors/{s}/", "datePublished": "2026-10-06", "dateModified": today, "inLanguage": "en", "license": "https://creativecommons.org/licenses/by/4.0/",
               "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"},
               "about": [{"@type": "Thing", "name": sector}, {"@type": "Thing", "name": "physical AI"}, {"@type": "Thing", "name": "sovereign AI"}],
               "citation": [{"@type": "TechArticle", "name": d["title"], "url": d["url"]} for d in ds]}
        out = ROOT / "sectors" / s
        out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(shell(f"sectors/{s}/", title, desc, body, [art, faq]), encoding="utf-8")
        md = [f"# Physical AI for {sector}: questions answered", "", f"Canonical: {BASE}/sectors/{s}/", "License: CC BY 4.0", "Publisher: CodeNinja Atoms (https://codeatoms.ai)", "", WHY.get(sector, ""), ""]
        for q, lead, _b, t in qs:
            md += [f"## {q}", "", t, ""]
        md += ["## Sources", ""] + [f"- [{d['title']}]({d['url']}) ({d['country']})" + (f", DOI https://doi.org/{d['doi']}" if d.get('doi') else "") for d in ds]
        (out / "index.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        cards.append(f'<a class="c" href="{BASE}/sectors/{s}/"><h3>{E(name)}</h3><p>{len(ds)} reference architecture{"s" if len(ds) != 1 else ""} · {E(", ".join(countries))}</p></a>')
        print(f"sectors/{s}/ {len(ds)} designs, {len(qs)} questions")
    body = (f'<p class="eyebrow">Sectors</p><h1>Physical AI, sector by sector</h1>'
            f'<p class="lead">The first questions engineers ask about putting AI into a physical operation, answered for each sector from the reference architectures CodeNinja Atoms has published.</p>'
            f'<div class="cards">{"".join(cards)}</div>')
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Physical AI by sector", "url": f"{BASE}/sectors/",
          "publisher": {"@id": f"{BASE}/#org"}, "hasPart": [{"@type": "TechArticle", "url": f"{BASE}/sectors/{slug(s)}/", "headline": f"Physical AI for {s}"} for s in sorted(by)]}
    (ROOT / "sectors" / "index.html").write_text(shell("sectors/", "Physical AI by Sector | CodeNinja Atoms",
                                                       "Questions engineers ask about AI in physical operations, answered per sector from published reference architectures.", body, [ld]), encoding="utf-8")


if __name__ == "__main__":
    main()
