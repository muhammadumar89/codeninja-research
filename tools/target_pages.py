"""Locked Google target pages (Umar, 17 Oct 2026; task step 16e). Two pages, each titled in the exact
search term and built ONLY from published data (dataset/*.jsonl, each design's objects.json and its
At a glance table), so every new design joins both the day site_index.py runs:
    /sovereign-ai-reference-architectures/   every design as a sovereign reference architecture
    /industrial-ontology-examples/           every published object model, browsable, with downloads
    python tools/target_pages.py        # site_index.py runs it before main(); seo.py runs last
"""
import json, datetime
from collections import Counter
from pathlib import Path
import brand
from sector_pages import an, load, shell, table, link, md_inline, plain, stop, E, BASE, COMPUTE, COST, CSS as _CSS

ROOT = Path(__file__).resolve().parent.parent
SOV, ONT = "sovereign-ai-reference-architectures", "industrial-ontology-examples"
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


def write(path, title, desc, body, ld, md):
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
              f'Designed on <a href="{BASE}/praxis/">Praxis</a>; object models load into <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. Updated {today}.</p>')
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
              f'<a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. Updated {today}.</p>')
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


def main():
    ds = designs()
    today = datetime.date.today().isoformat()
    n = sovereign(ds, today)
    no = ontology(ds, today)
    print(f"{SOV}/ {n} designs · {ONT}/ {no} objects")


if __name__ == "__main__":
    main()
