"""Locked Google target pages (Umar, 17 Oct 2026; task step 16e). Two pages, each titled in the exact
search term and built ONLY from published data (dataset/*.jsonl, each design's objects.json and its
At a glance table), so every new design joins both the day site_index.py runs:
    /sovereign-ai-reference-architectures/   every design as a sovereign reference architecture
    /industrial-ontology-examples/           every published object model, browsable, with downloads
    python tools/target_pages.py        # site_index.py runs it before main(); seo.py runs last
"""
import json, re, datetime
from collections import Counter
from pathlib import Path
import brand
from sector_pages import an, load, shell, table, link, md_inline, plain, stop, E, BASE, COMPUTE, COST, CSS as _CSS

ROOT = Path(__file__).resolve().parent.parent
SOV, ONT = "sovereign-ai-reference-architectures", "industrial-ontology-examples"
# Three stepping-stone terms locked by Umar on 25 Oct 2026, each a page titled in the exact term, built from the same published data
IND, PHY, RSI = "industrial-ai-reference-architecture", "physical-ai-system-design", "self-improving-ai-system"
COLLECTIONS = [(SOV, "sovereign AI reference architectures"), (ONT, "industrial ontology examples"),
               (IND, "industrial AI reference architecture"), (PHY, "physical AI system design"), (RSI, "self-improving AI system")]
# the collection itself as a citable Zenodo dataset record (published 21 Oct 2026 under the 20 Oct ruling; a snapshot, the page stays the living version)
SOV_DOI = "10.5281/zenodo.23527131"
CSS_EXTRA = """
.doc details{border-top:1px solid var(--rule-l);padding:14px 0}.doc details summary{cursor:pointer;color:var(--ink);font-size:18px}
.doc .stats{display:flex;flex-wrap:wrap;gap:12px 40px;margin:28px 0 8px;font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.doc .stats b{display:block;font-family:var(--sans,inherit);font-size:34px;font-weight:300;letter-spacing:-.02em;color:var(--ink);text-transform:none}
"""


def designs():
    by = load()
    ds = [d for sec in by.values() for d in sec]
    return sorted(ds, key=lambda d: (d.get("published", ""), d["design_id"]), reverse=True)


def first(rows, keys):
    for k in keys:
        if k in rows:
            return k, rows[k]
    return "", ""


def others(me):
    """Links to the other collection pages, for the src paragraph of each one (every page links every other)."""
    return ", ".join(f'<a href="{BASE}/{p}/">{E(t)}</a>' for p, t in COLLECTIONS if p != me)


def others_md(me):
    return ", ".join(f"[{t}]({BASE}/{p}/)" for p, t in COLLECTIONS if p != me)


def the(c):
    return f"the {c}" if c == "United States" else c


def sentence(s):
    """The first sentence of a published summary, plain text."""
    s = plain(s or "").strip()
    return re.split(r"(?<=[.!?])\s", s, maxsplit=1)[0] if s else ""


def day(iso):
    try:
        return datetime.date.fromisoformat(iso).strftime("%-d %b %Y")
    except (TypeError, ValueError):
        return iso or ""


def write(path, title, desc, body, ld, md):
    assert 25 <= len(desc) <= 160, (path, len(desc))  # Bing's limits on the meta description (21 Oct 2026)
    out = ROOT / path
    out.mkdir(parents=True, exist_ok=True)
    html = shell(f"{path}/", title, desc, body, ld).replace("</style>", CSS_EXTRA + "</style>", 1)
    (out / "index.html").write_text(html, encoding="utf-8")
    (out / "index.md").write_text("\n".join(md) + "\n", encoding="utf-8")


PATTERNS = [  # (pattern, what it is, test on the design's own At a glance compute text); first match wins
    ("Frontier reasoning node", "eight 141 GB HBM-class GPUs holding an open-weight frontier model at FP8, owned or hosted in the country",
     lambda c: "141 GB" in c),
    ("One inference card", "48 GB PCIe inference cards, from one card to one eight-card server, at the site or in the country; no frontier model",
     lambda c: "48 GB" in c or "L40S" in c),
    ("No new compute", "the design runs on servers or software the operator already owns; nothing to buy",
     lambda c: True),
]


LAYERS = [  # bottom up, the layered stack every published design draws as its Figure 3 (pulled forward by Umar's ruling of 22 Oct 2026)
    ("Sources", "the systems of record the operation already runs, read only; they stay the system of record"),
    ("Sensing", "cameras, detectors and instruments, existing or added, sized from the streams they produce"),
    ("Adapters", "one family per kind of source, owning its contract, retries and ordering; the only way data enters"),
    ("Object model", "the operation as typed objects, properties and links (an ontology), held on infrastructure the operator controls"),
    ("Inference", "open-weight models only, placed at the edge, the site or one in-country node by latency and link loss"),
    ("Services", "what the design computes over the object model: forecasts, detections, joins, evidence"),
    ("Surfaces", "where people see the result and a named person decides; actions are written one way into the owning system"),
]


def layers(ds):
    """The layers section: what each layer is, with totals read from the published designs."""
    objs, links_, models = sum(d.get("n_objects") or 0 for d in ds), sum(d.get("n_links") or 0 for d in ds), sum(d.get("n_models") or 0 for d in ds)
    human = sum(1 for d in ds if d.get("human_loop"))
    rows = [[f"<strong>{i + 1}. {E(a)}</strong>", E(b)] for i, (a, b) in enumerate(LAYERS)]
    lead = (f"Every published design follows the same seven layers, bottom up. Across the {len(ds)} designs the object model layer holds "
            f"{objs} objects and {links_} typed links, the inference layer names {models} open-weight model choices, and {human} of {len(ds)} "
            f"designs name the person who approves each action. The sovereign boundary is what makes it sovereign: every layer runs on "
            f"hardware the operator owns or controls, in its own country, with no third-party AI service in the serving path.")
    return lead, rows


def patterns(ds):
    """Group the designs by deployment pattern, by rule from each design's own compute figure, so the table
    answers 'which sovereign AI reference architecture fits my operation' in the first screen."""
    out = []
    for name, what, test in PATTERNS:
        out.append((name, what, []))
    for d in ds:
        c = plain(first(d["rows"], COMPUTE)[1])
        for name, what, test in PATTERNS:
            if test(c):
                next(x for x in out if x[0] == name)[2].append(d)
                break
    return [x for x in out if x[2]]


def sovereign(ds, today):
    countries = Counter(d["country"] for d in ds)
    sectors = sorted({d["sector"] for d in ds})
    n = len(ds)
    answer = (f"A sovereign AI reference architecture is a complete design for running AI inside an operation on infrastructure the operator "
              f"owns or controls, in its own country, with open-weight models and no third-party AI service in the serving path. "
              f"CodeNinja Atoms has published {n} of them, for {len(sectors)} physical-world sectors in "
              + ", ".join(f"{'the ' if c == 'United States' else ''}{c} ({k})" for c, k in countries.most_common())
              + ". Each names its sources, object model, models, compute, three-year cost and the person who approves every action, "
              "and each is free to reuse under CC BY 4.0 with a DOI.")
    rows = []
    for d in ds:
        ck, cv = first(d["rows"], COMPUTE)
        kk, kv = first(d["rows"], COST)
        doi = f'<a href="https://doi.org/{E(d["doi"])}">{E(d["doi"])}</a>' if d.get("doi") else ""
        rows.append([link(d), E(d["sector"]), E(d["country"]), md_inline(cv), md_inline(kv), doi])
    contains = [("Sources joined", "the existing systems the design reads, named, with what each one holds"),
                ("Object model", "the typed objects, properties and links that make the operation an ontology, published as hyper-ontology/1 JSON"),
                ("Models", "open-weight models only, each with its licence and why it was picked"),
                ("Compute", "the hardware sized from the models' own weights, from no new hardware to a GPU node"),
                ("Three-year cost", "owning against renting, every price cited with its source and date"),
                ("Human control", "the named person who approves every action that changes the physical world")]
    body = (f'<p class="eyebrow">Sovereign AI · Reference architectures</p><h1>Sovereign AI reference architectures</h1>'
            f'<p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{n}</b>published designs</span><span><b>{len(sectors)}</b>sectors</span><span><b>{len(countries)}</b>countries</span>'
            f'<span><b>{sum(d["n_objects"] for d in ds)}</b>ontology objects</span></div>'
            f'<p class="ans">Cite the collection: <a href="https://doi.org/{SOV_DOI}">{SOV_DOI}</a> (Zenodo, CC BY 4.0, the table below as CSV).</p>'
            + '<h2 id="patterns">Sovereign AI reference architecture patterns</h2>'
            + '<p class="ans">Three deployment patterns cover all ' + str(len(ds)) + ' published designs, grouped by rule from each design\'s own compute figure. Start from the one that matches the hardware your operation can own.</p>'
            + table(["Pattern", "What runs where", "Designs"], [[f"<strong>{E(a)}</strong> ({len(g)})", E(b), ", ".join(link(d) for d in g)] for a, b, g in patterns(ds)])
            + '<h2 id="layers">The layers of a sovereign AI reference architecture</h2>'
            + f'<p class="ans">{E(layers(ds)[0])}</p>'
            + table(["Layer", "What it holds"], layers(ds)[1])
            + f'<h2 id="all">Every published sovereign AI reference architecture</h2>'
            f'<p class="ans">Newest first. The compute and cost columns are each design\'s own At a glance figures.</p>'
            + table(["Design", "Sector", "Country", "Compute", "Three-year cost", "DOI"], rows)
            + '<h2 id="contains">What each sovereign AI reference architecture contains</h2>'
            + table(["Part", "What the design states"], [[E(a), E(b)] for a, b in contains])
            + '<h2 id="by-country">By country</h2>'
            + "".join(f'<p class="ans"><strong>{E(c)}.</strong> ' + ", ".join(link(d) for d in ds if d["country"] == c) + ".</p>" for c, _k in countries.most_common())
            + f'<p class="src">Built from the published designs only: each paper\'s At a glance table and the dataset at '
              f'<a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">Hugging Face</a>. Their object models are collected at '
              f'<a href="{BASE}/{ONT}/">industrial ontology examples</a>; questions by sector at <a href="{BASE}/sectors/">sectors</a>. '
              f'Designed on <a href="{BASE}/praxis/">Praxis</a>; object models load into <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. '
              f'The same designs read three other ways: <a href="{BASE}/{IND}/">industrial AI reference architecture</a>, '
              f'<a href="{BASE}/{PHY}/">physical AI system design</a>, <a href="{BASE}/{RSI}/">self-improving AI system</a>. Updated {today}.</p>')
    title = "Sovereign AI Reference Architectures: 18 Open Designs".replace("18", str(n))
    # Bing URL Inspection flags a meta description outside 25 to 160 characters as an error (21 Oct 2026); the term leads
    desc = f"{n} open sovereign AI reference architectures for physical operations: open-weight models, compute and three-year cost, each with a DOI."
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Sovereign AI reference architectures", "headline": "Sovereign AI reference architectures",
           "description": desc, "url": f"{BASE}/{SOV}/", "dateModified": today, "inLanguage": "en", "license": "https://creativecommons.org/licenses/by/4.0/",
           "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"},
           "identifier": f"https://doi.org/{SOV_DOI}", "sameAs": [f"https://doi.org/{SOV_DOI}", f"https://zenodo.org/records/{SOV_DOI.rsplit('.', 1)[1]}"],
           "about": [{"@type": "Thing", "name": "sovereign AI"}, {"@type": "Thing", "name": "reference architecture"}, {"@type": "Thing", "name": "physical AI"}],
           "mainEntity": {"@type": "ItemList", "numberOfItems": n, "itemListElement": [
               {"@type": "ListItem", "position": i + 1, "item": {"@type": "TechArticle", "name": d["title"], "url": d["url"],
                                                                 **({"identifier": f"https://doi.org/{d['doi']}"} if d.get("doi") else {})}} for i, d in enumerate(ds)]}},
          {"@context": "https://schema.org", "@type": "FAQPage", "url": f"{BASE}/{SOV}/", "mainEntity": [
              {"@type": "Question", "name": "What is a sovereign AI reference architecture?", "acceptedAnswer": {"@type": "Answer", "text": answer}}]}]
    md = ["# Sovereign AI reference architectures", "", f"Canonical: {BASE}/{SOV}/", "License: CC BY 4.0", "Publisher: CodeNinja Atoms (https://codeatoms.ai)", f"DOI: {SOV_DOI}", "", answer, "",
          "## Sovereign AI reference architecture patterns", "", "| Pattern | What runs where | Designs |", "|---|---|---|"]
    md += [f"| {a} ({len(g)}) | {b} | " + ", ".join(f"[{d['short']}]({d['url']})" for d in g) + " |" for a, b, g in patterns(ds)]
    md += ["", "## The layers of a sovereign AI reference architecture", "", layers(ds)[0], "", "| Layer | What it holds |", "|---|---|"]
    md += [f"| {i + 1}. {a} | {b} |" for i, (a, b) in enumerate(LAYERS)]
    md += ["", "## Every published sovereign AI reference architecture", "",
          "| Design | Sector | Country | Compute | Three-year cost | DOI |", "|---|---|---|---|---|---|"]
    for d in ds:
        md.append(f"| [{d['short']}]({d['url']}) | {d['sector']} | {d['country']} | {plain(first(d['rows'], COMPUTE)[1])} | {plain(first(d['rows'], COST)[1])} | {d.get('doi', '')} |")
    write(SOV, title, desc, body, ld, md)
    return n


def worked(ds, objs):
    """One worked example near the first screen: the published object with the most links (then most properties), chosen
    by rule from the data, never by hand, so it changes only when the corpus does."""
    o = max(objs, key=lambda x: (len(x.get("links", [])), len(x.get("properties", [])), x["object_id"]))
    d = next(x for x in ds if x["design_id"] == o["design_id"])
    labels = {x["object_id"]: x["label"] for x in objs if x["design_id"] == o["design_id"]}
    snippet = json.dumps({k: o[k] for k in ("object_id", "label", "kind", "anchored_in", "properties", "status_vocabulary", "links") if k in o}, indent=2, ensure_ascii=False)
    links = "".join(f"<li><strong>{E(l['label'])}</strong> {E(labels.get(l['to'], l['to']))}</li>" for l in o.get("links", []))
    return (f'<h2 id="example">An industrial ontology example, read object by object</h2>'
            f'<p class="ans">Take one object from {link(d)} ({E(d["sector"])}, {E(d["country"])}): <strong>{E(o["label"])}</strong>, '
            f'{an(o.get("kind", "object"))} {E(o.get("kind", "object"))}' + (f' held in {E(o["anchored_in"])}' if o.get("anchored_in") else "") + '. '
            f'Its properties are what the operation records about it: {E(", ".join(o.get("properties", [])) or "none listed")}. '
            'Its links are what make this an ontology rather than a table: each one is typed and points at another object in the same model.</p>'
            f'<ul class="ans">{links}</ul>'
            '<p class="ans">The same object as it appears in the package, hyper-ontology/1 JSON:</p>'
            f'<pre style="overflow-x:auto;font-size:13px;line-height:1.5;background:rgba(30,31,43,.04);padding:16px">{E(snippet)}</pre>')


def ontology(ds, today):
    objs = [json.loads(l) for l in (ROOT / "dataset" / "objects.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    no, nl = sum(d["n_objects"] for d in ds), sum(d["n_links"] for d in ds)
    answer = (f"An industrial ontology is a typed model of a physical operation: its assets, records, events and people as objects, each with "
              f"properties, status values and named links to the others, anchored in the systems that already hold the data. "
              f"Below are {len(ds)} published industrial ontology examples, {no} objects and {nl} links in all, one per real operation "
              f"across {len({d['sector'] for d in ds})} sectors. Each downloads as hyper-ontology/1 JSON under CC BY 4.0.")
    rows = [[link(d), E(d["sector"]), E(d["country"]), f'{d["n_objects"]} objects, {d["n_links"]} links',
             f'<a href="{d["url"]}ontology/objects.json">objects.json</a>'] for d in ds]
    browse = []
    for d in ds:
        mine = [o for o in objs if o["design_id"] == d["design_id"]]
        t = table(["Object", "Kind", "Anchored in", "Properties", "Links"],
                  [[E(o["label"]), E(o.get("kind", "")), E(o.get("anchored_in", "")), E(", ".join(o.get("properties", []))),
                    E("; ".join(f'{l["label"]} {l["to"]}' for l in o.get("links", [])))] for o in mine])
        browse.append(f'<details id="{E(d["design_id"])}"><summary>{E(d["short"])}: {E(d["sector"])}, {E(d["country"])} · {len(mine)} objects</summary>'
                      f'<p>{link(d)} · <a href="{d["url"]}ontology/objects.json">download objects.json</a></p>{t}</details>')
    ex = worked(ds, objs)
    body = (f'<p class="eyebrow">Ontology · Examples</p><h1>Industrial ontology examples</h1>'
            f'<p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{len(ds)}</b>object models</span><span><b>{no}</b>objects</span><span><b>{nl}</b>links</span></div>'
            + ex
            + f'<h2 id="all">Every published industrial ontology example</h2>'
            + table(["Operation", "Sector", "Country", "Size", "Download"], rows)
            + '<h2 id="browse">Browse each object model</h2><p class="ans">Open any operation to read its objects, the system each is anchored in, its properties and its links.</p>'
            + "".join(browse)
            + '<h2 id="format">The format</h2>'
            f'<p class="ans">Every example uses the same package format, hyper-ontology/1: objects with kind, properties, status vocabulary and typed links. '
            f'The format is documented at <a href="{BASE}/developer/reference/hyper-ontology-1/">hyper-ontology/1</a>, loads with the '
            f'<a href="{BASE}/developer/reference/loader/">Python loader</a>, and all {no} objects are one table in the '
            f'<a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">dataset</a> (objects.jsonl).</p>'
            + f'<p class="src">Built from the published object models only. The designs they come from are listed at '
              f'<a href="{BASE}/{SOV}/">sovereign AI reference architectures</a>. Designed on <a href="{BASE}/praxis/">Praxis</a>; made living in '
              f'<a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. The same designs read three other ways: <a href="{BASE}/{IND}/">industrial AI reference architecture</a>, '
              f'<a href="{BASE}/{PHY}/">physical AI system design</a>, <a href="{BASE}/{RSI}/">self-improving AI system</a>. Updated {today}.</p>')
    title = f"Industrial Ontology Examples: {len(ds)} Object Models to Download"
    # description only, under Bing's 160 limit (Umar, 21 Oct 2026: allowed despite the keep rule; title, H1 and body untouched)
    desc = f"{len(ds)} industrial ontology examples from real physical operations: {no} typed objects and {nl} links, as hyper-ontology/1 JSON under CC BY 4.0."
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Industrial ontology examples", "headline": "Industrial ontology examples",
           "description": desc, "url": f"{BASE}/{ONT}/", "dateModified": today, "inLanguage": "en", "license": "https://creativecommons.org/licenses/by/4.0/",
           "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"},
           "about": [{"@type": "Thing", "name": "industrial ontology"}, {"@type": "Thing", "name": "ontology"}, {"@type": "Thing", "name": "knowledge graph"}],
           "mainEntity": {"@type": "ItemList", "numberOfItems": len(ds), "itemListElement": [
               {"@type": "ListItem", "position": i + 1, "item": {"@type": "Dataset", "name": f"{d['short']} object model", "description": f"Industrial ontology for {d['sector']} in {d['country']}: {d['n_objects']} objects, {d['n_links']} links, hyper-ontology/1 JSON.",
                                                                 "url": f"{d['url']}ontology/objects.json", "license": "https://creativecommons.org/licenses/by/4.0/",
                                                                 "isBasedOn": d["url"]}} for i, d in enumerate(ds)]}},
          {"@context": "https://schema.org", "@type": "FAQPage", "url": f"{BASE}/{ONT}/", "mainEntity": [
              {"@type": "Question", "name": "What is an industrial ontology?", "acceptedAnswer": {"@type": "Answer", "text": answer}}]}]
    md = ["# Industrial ontology examples", "", f"Canonical: {BASE}/{ONT}/", "License: CC BY 4.0", "Publisher: CodeNinja Atoms (https://codeatoms.ai)", "", answer, ""]
    for d in ds:
        md += [f"## {d['short']} ({d['sector']}, {d['country']})", "", f"Design: {d['url']} · JSON: {d['url']}ontology/objects.json", ""]
        md += [f"- {o['label']} ({o.get('kind', '')}" + (f", in {o['anchored_in']}" if o.get("anchored_in") else "") + ")" for o in objs if o["design_id"] == d["design_id"]] + [""]
    write(ONT, title, desc, body, ld, md)
    return no


def ld_pair(path, name, desc, today, about, question, answer, items):
    """CollectionPage (publisher CodeNinja Atoms, about the term) + FAQPage carrying the one-paragraph answer."""
    return [{"@context": "https://schema.org", "@type": "CollectionPage", "name": name, "headline": name,
             "description": desc, "url": f"{BASE}/{path}/", "dateModified": today, "inLanguage": "en", "license": "https://creativecommons.org/licenses/by/4.0/",
             "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"},
             "about": [{"@type": "Thing", "name": a} for a in about],
             "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "item": {"@type": "TechArticle", "name": d["title"], "url": d["url"],
                                                                   **({"identifier": f"https://doi.org/{d['doi']}"} if d.get("doi") else {})}} for i, d in enumerate(items)]}},
            {"@context": "https://schema.org", "@type": "FAQPage", "url": f"{BASE}/{path}/", "mainEntity": [
                {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}]}]


def md_head(h1, path, answer):
    return [f"# {h1}", "", f"Canonical: {BASE}/{path}/", "License: CC BY 4.0", "Publisher: CodeNinja Atoms (https://codeatoms.ai)", "", answer, ""]


def md_table(head, rows):
    return ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]


def industrial(ds, today):
    """/industrial-ai-reference-architecture/: the term 'industrial AI reference architecture', a stepping stone toward 'industrial AI'."""
    n = len(ds)
    countries = Counter(d["country"] for d in ds)
    sectors = sorted({d["sector"] for d in ds})
    answer = (f"An industrial AI reference architecture is a complete design for putting AI into one industrial operation: the sources it reads, "
              f"the object model that joins them, the open-weight models it runs, the compute sized from those models, the three-year cost and the "
              f"named person who approves every action. CodeNinja Atoms has published {n} of them, one per real operation, across {len(sectors)} "
              f"sectors in " + ", ".join(f"{the(c)} ({k})" for c, k in countries.most_common())
              + ". Each is free to reuse under CC BY 4.0 with a DOI.")
    bysec = [[E(s), ", ".join(link(d) for d in ds if d["sector"] == s), E(", ".join(sorted({d["country"] for d in ds if d["sector"] == s})))] for s in sectors]
    rows = []
    for d in ds:
        doi = f'<a href="https://doi.org/{E(d["doi"])}">{E(d["doi"])}</a>' if d.get("doi") else ""
        rows.append([link(d), E(d["sector"]), E(d["country"]), md_inline(first(d["rows"], COMPUTE)[1]), md_inline(first(d["rows"], COST)[1]), doi])
    pats = patterns(ds)
    lead_l, rows_l = layers(ds)
    body = (f'<p class="eyebrow">Industrial AI · Reference architecture</p><h1>Industrial AI reference architecture</h1>'
            f'<p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{n}</b>published designs</span><span><b>{len(sectors)}</b>sectors</span><span><b>{len(countries)}</b>countries</span>'
            f'<span><b>{sum(d["n_objects"] for d in ds)}</b>ontology objects</span><span><b>{sum(d.get("n_models") or 0 for d in ds)}</b>open-weight model choices</span></div>'
            + '<h2 id="by-sector">An industrial AI reference architecture for each sector</h2>'
            + f'<p class="ans">One design per real operation. Start from your own sector; the nearest design is the one to read first.</p>'
            + table(["Sector", "Designs", "Countries"], bysec)
            + '<h2 id="patterns">Industrial AI reference architecture patterns</h2>'
            + f'<p class="ans">Three deployment patterns cover all {n} published designs, grouped by rule from each design\'s own compute figure. Pick the one that matches the hardware your operation can own.</p>'
            + table(["Pattern", "What runs where", "Designs"], [[f"<strong>{E(a)}</strong> ({len(g)})", E(b), ", ".join(link(d) for d in g)] for a, b, g in pats])
            + '<h2 id="layers">The layers of an industrial AI reference architecture</h2>'
            + f'<p class="ans">{E(lead_l)}</p>' + table(["Layer", "What it holds"], rows_l)
            + '<h2 id="all">Every published industrial AI reference architecture</h2>'
            + '<p class="ans">Newest first. The compute and cost columns are each design\'s own At a glance figures.</p>'
            + table(["Design", "Sector", "Country", "Compute", "Three-year cost", "DOI"], rows)
            + f'<p class="src">Built from the published designs only: each paper\'s At a glance table and the dataset at '
              f'<a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">Hugging Face</a>. The same designs as '
              f'<a href="{BASE}/{SOV}/">sovereign AI reference architectures</a>; their object models at <a href="{BASE}/{ONT}/">industrial ontology examples</a>; '
              f'also read as <a href="{BASE}/{PHY}/">physical AI system design</a> and as the output of a <a href="{BASE}/{RSI}/">self-improving AI system</a>. '
              f'Questions by sector at <a href="{BASE}/sectors/">sectors</a>. Designed on <a href="{BASE}/praxis/">Praxis</a>; object models load into '
              f'<a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. Updated {today}.</p>')
    title = f"Industrial AI reference architecture: {n} open designs by sector"
    desc = f"Industrial AI reference architecture: {n} open designs for real industrial operations, each with object model, open-weight models, compute and three-year cost."
    ld = ld_pair(IND, "Industrial AI reference architecture", desc, today, ["industrial AI reference architecture", "industrial AI", "reference architecture"],
                 "What is an industrial AI reference architecture?", answer, ds)
    md = md_head("Industrial AI reference architecture", IND, answer)
    md += ["## An industrial AI reference architecture for each sector", ""] + md_table(["Sector", "Designs", "Countries"],
          [[s, ", ".join(f"[{d['short']}]({d['url']})" for d in ds if d["sector"] == s), ", ".join(sorted({d["country"] for d in ds if d["sector"] == s}))] for s in sectors]) + [""]
    md += ["## Industrial AI reference architecture patterns", ""] + md_table(["Pattern", "What runs where", "Designs"],
          [[f"{a} ({len(g)})", b, ", ".join(f"[{d['short']}]({d['url']})" for d in g)] for a, b, g in pats]) + [""]
    md += ["## The layers of an industrial AI reference architecture", "", lead_l, ""] + md_table(["Layer", "What it holds"], [[f"{i + 1}. {a}", b] for i, (a, b) in enumerate(LAYERS)]) + [""]
    md += ["## Every published industrial AI reference architecture", ""] + md_table(["Design", "Sector", "Country", "Compute", "Three-year cost", "DOI"],
          [[f"[{d['short']}]({d['url']})", d["sector"], d["country"], plain(first(d["rows"], COMPUTE)[1]), plain(first(d["rows"], COST)[1]), d.get("doi", "")] for d in ds])
    md += ["", f"See also: {others_md(IND)}."]
    write(IND, title, desc, body, ld, md)
    return n


def physical(ds, today):
    """/physical-ai-system-design/: the term 'physical AI system design', a stepping stone toward 'physical AI'."""
    n = len(ds)
    countries = Counter(d["country"] for d in ds)
    sectors = sorted({d["sector"] for d in ds})
    objs, links_, models = sum(d.get("n_objects") or 0 for d in ds), sum(d.get("n_links") or 0 for d in ds), sum(d.get("n_models") or 0 for d in ds)
    edge = [d for d in ds if "Edge" in d["rows"] or "Boundary" in d["rows"]]
    src = sum(1 for d in ds if "Sources" in d["rows"] or "Sources joined" in d["rows"])
    sized = sum(1 for d in ds if first(d["rows"], COMPUTE)[0])
    costed = sum(1 for d in ds if first(d["rows"], COST)[0])
    wp = sum(1 for d in ds if d.get("write_paths"))
    hl = sum(1 for d in ds if d.get("human_loop"))
    pats = {a: len(g) for a, _b, g in patterns(ds)}
    answer = (f"Physical AI system design is the engineering of a system that senses a physical operation, reasons over it as typed objects and acts "
              f"through a named person. Its decisions are what to sense, where inference runs (the edge, the site or one in-country node), the object "
              f"model, the open-weight model choice, the compute sized from those models' weights, the write paths back into the operator's systems and "
              f"human control. CodeNinja Atoms has published {n} worked examples of physical AI system design across {len(sectors)} sectors in "
              + ", ".join(f"{the(c)} ({k})" for c, k in countries.most_common()) + ", each free to reuse under CC BY 4.0.")
    decisions = [
        ("1. Sensing and sources", f"What the system reads: the operator's existing systems of record, read only, plus the cameras, detectors and instruments the operation needs. "
                                   f"{src} of {n} designs name their sources on the first page of the paper; every design names them in the body."),
        ("2. Where inference runs", f"{len(edge)} of {n} designs state an edge or boundary tier in their At a glance table. By compute pattern: "
                                    + ", ".join(f"{v} {k.lower()}" for k, v in pats.items()) + f"; in every design inference stays in the operator's country."),
        ("3. The object model", f"{objs} typed objects and {links_} typed links across the {n} designs, each published as hyper-ontology/1 JSON."),
        ("4. Open-weight model choice", f"{models} model choices in all, each with its licence and the reason it was picked; no closed model in any serving path."),
        ("5. Sizing from the weights", f"{sized} of {n} designs state their compute and {costed} of {n} their three-year cost on the first page, sized from the models' own weights, "
                                       f"from no new hardware to an eight-GPU node."),
        ("6. Write paths and human control", f"{wp} of {n} designs name their write paths (how a decision is written into the owning system) and {hl} of {n} name the person who "
                                             f"approves each action that changes the physical world."),
    ]
    rows = [[link(d), E(d["sector"]), E(d["country"]), E(sentence(d.get("what") or d.get("summary"))), md_inline(first(d["rows"], COMPUTE)[1])] for d in ds]
    body = (f'<p class="eyebrow">Physical AI · System design</p><h1>Physical AI system design</h1>'
            f'<p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{n}</b>worked examples</span><span><b>{len(sectors)}</b>sectors</span><span><b>{len(countries)}</b>countries</span>'
            f'<span><b>{objs}</b>typed objects</span><span><b>{models}</b>open-weight model choices</span></div>'
            + '<h2 id="decisions">The six decisions in a physical AI system design</h2>'
            + f'<p class="ans">Every published design makes the same six decisions, in this order. The counts are read from the designs themselves.</p>'
            + table(["Decision", "What the published designs do"], [[f"<strong>{E(a)}</strong>", E(b)] for a, b in decisions])
            + '<h2 id="examples">Worked examples of physical AI system design</h2>'
            + '<p class="ans">Newest first. What each system senses or reads is the paper\'s own one-line description; compute is its At a glance figure.</p>'
            + table(["Design", "Sector", "Country", "What it senses or reads", "Compute"], rows)
            + '<h2 id="learn">Where to learn physical AI system design</h2>'
            + f'<p class="ans">Design one on <a href="{BASE}/praxis/">Praxis</a>, the platform every example here was reasoned on. '
              f'<a href="{BASE}/padi/">PADI</a>, the Physical AI Design Index, is the benchmark for physical AI system design: Praxis against frontier AI on its own, on fresh tasks. '
              f'Engineers start at <a href="{BASE}/developer/">developers</a>; every design, object, model and cost line is one '
              f'<a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">dataset</a> on Hugging Face.</p>'
            + f'<p class="src">Built from the published designs only: each paper\'s At a glance table and the dataset. The same designs as '
              f'<a href="{BASE}/{SOV}/">sovereign AI reference architectures</a> and as an <a href="{BASE}/{IND}/">industrial AI reference architecture</a> by sector; '
              f'their object models at <a href="{BASE}/{ONT}/">industrial ontology examples</a>; the loop that produced them at '
              f'<a href="{BASE}/{RSI}/">self-improving AI system</a>. Questions by sector at <a href="{BASE}/sectors/">sectors</a>. Updated {today}.</p>')
    title = f"Physical AI system design: {n} worked examples"
    desc = f"Physical AI system design: {n} worked examples that sense an operation, reason over typed objects and act through a named person, with compute and cost."
    ld = ld_pair(PHY, "Physical AI system design", desc, today, ["physical AI system design", "physical AI", "system design"],
                 "What is physical AI system design?", answer, ds)
    md = md_head("Physical AI system design", PHY, answer)
    md += ["## The six decisions in a physical AI system design", ""] + md_table(["Decision", "What the published designs do"], decisions) + [""]
    md += ["## Worked examples of physical AI system design", ""] + md_table(["Design", "Sector", "Country", "What it senses or reads", "Compute"],
          [[f"[{d['short']}]({d['url']})", d["sector"], d["country"], sentence(d.get("what") or d.get("summary")), plain(first(d["rows"], COMPUTE)[1])] for d in ds]) + [""]
    md += ["## Where to learn physical AI system design", "", f"Design on Praxis: {BASE}/praxis/ · PADI, the benchmark for physical AI system design: {BASE}/padi/ · "
           f"Developers: {BASE}/developer/ · Dataset: https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures", "", f"See also: {others_md(PHY)}."]
    write(PHY, title, desc, body, ld, md)
    return n


def self_improving(ds, today):
    """/self-improving-ai-system/: the term 'self-improving AI system', a stepping stone toward 'self-improving system'. PADI results are
    loaded through padi.load() (the one loader) and shown as results only: never how PADI scores or any harness internal."""
    import padi
    j = padi.load()
    n = len(ds)
    loops = (j["cycles"] if j else [])
    X = j.get("blind") if j else None
    L = j["latest"] if j else None
    answer = (f"A self-improving AI system is a system whose output is measured on fresh tasks each loop and whose context, not its weights, is improved "
              f"between loops. CodeNinja's Praxis is run as one: each RSI loop (recursive self improvement loop) measures Praxis against frontier AI on its "
              f"own on the Physical AI Design Index (PADI), and the {n} designs published here are its output."
              + (f" Latest measured RSI loop, RSI Loop {L['cycle']}: Praxis platform {L['platform_pct']:.1f}% against frontier AI {L['bare_pct']:.1f}% of checks passed."
                 if L else ""))
    pr = [[f"RSI Loop {c['cycle']}", day(c["date"]), c["tasks"], f"{c['platform_pct']:.1f}%", f"{c['bare_pct']:.1f}%"] for c in loops]
    if X:
        pr.append([f"RSI Loop {X['cycle']}, blind", day(X["date"]), X["tasks"], f"{X['platform_pct']:.1f}%", f"{X['bare_pct']:.1f}%"])
    stats = ""
    if L:
        stats += f'<span><b>{L["platform_pct"]:.1f}%</b>Praxis, RSI Loop {L["cycle"]} (frontier AI {L["bare_pct"]:.1f}%)</span>'
    if X:
        stats += f'<span><b>{X["platform_pct"]:.1f}%</b>Praxis, RSI Loop {X["cycle"]} blind (frontier AI {X["bare_pct"]:.1f}%)</span>'
    stats += f'<span><b>{len(loops) + (1 if X else 0)}</b>RSI loops published</span><span><b>{n}</b>designs produced</span>'
    produced = [[link(d), E(d["sector"]), E(d["country"]), day(d.get("published"))] for d in ds]
    running = f" RSI Loop {padi.RUNNING} is running now." if getattr(padi, "RUNNING", None) else ""
    body = (f'<p class="eyebrow">Self-improving · AI system</p><h1>Self-improving AI system</h1>'
            f'<p class="lead">{E(answer)}</p>'
            f'<div class="stats">{stats}</div>'
            + '<h2 id="loops">The self-improving AI system, RSI loop by RSI loop</h2>'
            + f'<p class="ans">Each row is one RSI loop: fresh tasks, both arms scored the same way, the share of checks passed. '
              f'The blind row is the evaluation on tasks the platform had never seen. How PADI scores is on the <a href="{BASE}/padi/">PADI page</a>, with its limitations; '
              f'this page shows results only.{E(running)}</p>'
            + (table(["RSI Loop", "Date", "Tasks", "Praxis platform", "Frontier AI"], [[E(c) for c in r] for r in pr]) if pr else
               f'<p class="ans">No PADI results export is in place on this build; the results live at <a href="{BASE}/padi/">PADI</a>.</p>')
            + '<h2 id="how">What changes between RSI loops in a self-improving AI system</h2>'
            + f'<p class="ans">The weights do not. What improves is the context Praxis reasons with: the published designs, their object models, model registers and cost lines, '
              f'and the gaps each RSI loop finds, which is why self-improving AI systems built this way can be audited loop by loop: every input to the next loop is a published document. '
              f'Design on <a href="{BASE}/praxis/">Praxis</a>; the measure is <a href="{BASE}/padi/">PADI</a>.</p>'
            + '<h2 id="produced">What the self-improving AI system produced</h2>'
            + f'<p class="ans">The {n} published designs, newest first. Each is a complete reference architecture with a DOI under CC BY 4.0.</p>'
            + table(["Design", "Sector", "Country", "Published"], produced)
            + f'<p class="src">Results from the PADI export only; designs from the published dataset at '
              f'<a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">Hugging Face</a>. The designs are also collected as '
              f'<a href="{BASE}/{SOV}/">sovereign AI reference architectures</a>, as an <a href="{BASE}/{IND}/">industrial AI reference architecture</a> by sector and as '
              f'<a href="{BASE}/{PHY}/">physical AI system design</a>; their object models at <a href="{BASE}/{ONT}/">industrial ontology examples</a>. Updated {today}.</p>')
    title = f"Self-improving AI system: Praxis measured RSI loop by RSI loop"
    desc = f"Self-improving AI system: Praxis measured RSI loop by RSI loop on PADI against frontier AI, and the {n} published designs it produced."
    ld = ld_pair(RSI, "Self-improving AI system", desc, today, ["self-improving AI system", "self-improving system", "physical AI", "AI benchmark"],
                 "What is a self-improving AI system?", answer, ds)
    md = md_head("Self-improving AI system", RSI, answer)
    md += ["## The self-improving AI system, RSI loop by RSI loop", ""] + (md_table(["RSI Loop", "Date", "Tasks", "Praxis platform", "Frontier AI"], pr) if pr else [f"Results: {BASE}/padi/"]) + [""]
    md += [f"How PADI scores, and its limitations: {BASE}/padi/", ""]
    md += ["## What the self-improving AI system produced", ""] + md_table(["Design", "Sector", "Country", "Published"],
          [[f"[{d['short']}]({d['url']})", d["sector"], d["country"], d.get("published", "")] for d in ds]) + [""]
    md += [f"Design on Praxis: {BASE}/praxis/ · PADI: {BASE}/padi/", "", f"See also: {others_md(RSI)}."]
    write(RSI, title, desc, body, ld, md)
    return len(pr)


def main():
    ds = designs()
    today = datetime.date.today().isoformat()
    n = sovereign(ds, today)
    no = ontology(ds, today)
    ni = industrial(ds, today)
    npy = physical(ds, today)
    nl = self_improving(ds, today)
    print(f"{SOV}/ {n} designs")
    print(f"{ONT}/ {no} objects")
    print(f"{IND}/ {ni} designs")
    print(f"{PHY}/ {npy} worked examples")
    print(f"{RSI}/ {nl} RSI loops, {len(ds)} designs")


if __name__ == "__main__":
    main()
