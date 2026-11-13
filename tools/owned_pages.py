"""Owned keyword pages (Umar, 13 Nov 2026, episode 45 chat: "build the four pages"). One page per owned head term that had none:
    /physical-ai/              the owned keyword "physical AI"
    /industrial-ai/            the owned keyword "industrial AI"
    /ontologies/               the owned keyword "ontologies"
    /self-improving-systems/   the owned keyword "self-improving system(s)"
("sovereign AI" is owned by the home page.) Each answers the term in its first screen and links DOWN to its locked stepping stones
and the designs behind them. Built only from published data, the same loaders as target_pages.py; rebuilt by site_index.py.
The stepping stone pages are not edited to link up (keep rule); they reach these pages through the footer Collections column.
    python tools/owned_pages.py
"""
import json, datetime
from collections import Counter
import target_pages as T
from target_pages import (designs, patterns, layers, write, ld_pair, md_head, md_table, the, link, table, E, BASE, ROOT,
                          SOV, ONT, IND, PHY, RSI, DAT, KINDS, WORKS)

PAI, IAI, ONTS, SIS = "physical-ai", "industrial-ai", "ontologies", "self-improving-systems"
OWNED = [(PAI, "Physical AI"), (IAI, "Industrial AI"), (ONTS, "Ontologies"), (SIS, "Self-improving systems")]


def where(countries):
    return ", ".join(f"{the(c)} ({k})" for c, k in countries.most_common())


def steps(pairs):
    """The stepping stone row: the locked pages a reader goes to next, in the term's own words."""
    return '<ul class="ans">' + "".join(f'<li><a href="{BASE}/{p}/"><strong>{E(t)}</strong></a>: {E(w)}</li>' for p, t, w in pairs) + "</ul>"


def steps_md(pairs):
    return [f"- [{t}]({BASE}/{p}/): {w}" for p, t, w in pairs]


def owned_footer(me):
    return " · ".join(f'<a href="{BASE}/{p}/">{E(t)}</a>' for p, t in OWNED if p != me)


def src(me, today):
    return (f'<p class="src">Built from the published designs only: each paper\'s At a glance table, its object model and the '
            f'<a href="https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures">dataset</a>. Designed on <a href="{BASE}/praxis/">Praxis</a>; '
            f'object models load into <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>. Also: {owned_footer(me)} · '
            f'<a href="{BASE}/">sovereign AI</a>. Updated {today}.</p>')


def by_sector(ds):
    secs = sorted({d["sector"] for d in ds}, key=lambda s: (-sum(1 for d in ds if d["sector"] == s), s))
    rows = []
    for s in secs:
        g = [d for d in ds if d["sector"] == s]
        rows.append((s[:1].upper() + s[1:], g, ", ".join(sorted({d["country"] for d in g}))))
    return rows


def physical_ai(ds, today):
    n, countries = len(ds), Counter(d["country"] for d in ds)
    secs = by_sector(ds)
    pats = patterns(ds)
    answer = (f"Physical AI is AI that senses the physical world, reasons about it and acts in it. Cameras, instruments and machines feed it; a typed "
              f"model of the operation (an ontology) holds what it knows; open-weight models reason over that model; and a named person approves every "
              f"action that changes the physical world. Where generative AI works on text, physical AI works on plants, fleets, grids, ports, mines and fields. "
              f"CodeNinja Atoms has published {n} open physical AI designs for real operations across {len(secs)} sectors in {where(countries)}, "
              f"each free to reuse under CC BY 4.0.")
    body = (f'<p class="eyebrow">Physical AI</p><h1>Physical AI</h1><p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{n}</b>open designs</span><span><b>{len(secs)}</b>sectors</span><span><b>{len(countries)}</b>countries</span>'
            f'<span><b>{len(pats)}</b>compute patterns</span></div>'
            + '<h2 id="what">What physical AI does, sector by sector</h2>'
            + '<p class="ans">Each row is a sector with at least one published design. Every design is one real operation, newest first; open it for what it senses, the models it runs and what it costs.</p>'
            + table(["Sector", "Countries", "Designs"], [[f"<strong>{E(s)}</strong>", E(w), ", ".join(link(d) for d in g)] for s, g, w in secs])
            + '<h2 id="design">How a physical AI system is designed</h2>'
            + '<p class="ans">Every published design makes the same decisions in the same order: what to sense, where inference runs, the object model, '
              'the open-weight models, the compute sized from their weights, and the write paths back into the operator\'s systems with a person in control.</p>'
            + steps([(PHY, "Physical AI system design", "the step by step method and the six decisions, counted across every design"),
                     (SOV, "Sovereign AI reference architectures", "every design side by side with its compute and three year cost"),
                     (ONT, "Industrial ontology examples", "the object model inside each physical AI design")])
            + '<h2 id="where">Where physical AI runs</h2>'
            + f'<p class="ans">Physical AI runs next to the operation, not in a distant cloud: on the edge, on the site or on one node in the operator\'s own country. '
              f'The {n} designs fall into {len(pats)} compute patterns.</p>'
            + table(["Pattern", "What runs where", "Designs"], [[f"<strong>{E(a)}</strong>", E(b), str(len(g))] for a, b, g in pats])
            + '<h2 id="sovereign">Sovereign physical AI</h2>'
            + f'<p class="ans">In every published design the models are open weights, self hosted in the operator\'s country, and no frame or reading leaves it. '
              f'That is what makes physical AI <a href="{BASE}/">sovereign AI</a>: the operator owns the models, the data and the decisions.</p>'
            + src(PAI, today))
    title = f"Physical AI: what it is, how it is designed, and {n} open designs"
    desc = f"Physical AI senses the physical world, reasons over it and acts through a named person. What it is, where it runs, and {n} open designs."
    ld = ld_pair(PAI, "Physical AI", desc, today, ["physical AI", "embodied AI", "industrial AI"], "What is physical AI?", answer, ds)
    md = md_head("Physical AI", PAI, answer)
    md += ["## What physical AI does, sector by sector", ""] + md_table(["Sector", "Countries", "Designs"],
          [[s, w, ", ".join(f"[{d['short']}]({d['url']})" for d in g)] for s, g, w in secs]) + [""]
    md += ["## How a physical AI system is designed", ""] + steps_md([(PHY, "Physical AI system design", "the method and the six decisions"),
          (SOV, "Sovereign AI reference architectures", "every design with compute and cost"), (ONT, "Industrial ontology examples", "the object models")]) + [""]
    md += ["## Where physical AI runs", ""] + md_table(["Pattern", "What runs where", "Designs"], [[a, b, len(g)] for a, b, g in pats])
    write(PAI, title, desc, body, ld, md)
    return n


def industrial_ai(ds, today):
    n, countries = len(ds), Counter(d["country"] for d in ds)
    secs = by_sector(ds)
    lead_l, rows_l = layers(ds)
    objs = sum(d.get("n_objects") or 0 for d in ds)
    answer = (f"Industrial AI is AI put to work inside industrial operations: plants, grids, mines, pipelines, rail, ports and factories. It reads the "
              f"operation's own systems of record and sensors, joins them in one object model, reasons over that model with open-weight models running on "
              f"the operator's hardware, and puts each decision in front of the person who owns it. CodeNinja Atoms has published {n} industrial AI designs, "
              f"one per real operation, across {len(secs)} sectors in {where(countries)}, with {objs} typed objects between them.")
    body = (f'<p class="eyebrow">Industrial AI</p><h1>Industrial AI</h1><p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{n}</b>industrial AI designs</span><span><b>{len(secs)}</b>sectors</span><span><b>{len(countries)}</b>countries</span>'
            f'<span><b>{objs}</b>typed objects</span></div>'
            + '<h2 id="uses">Industrial AI use cases by sector</h2>'
            + '<p class="ans">One row per sector. Each design is one industrial AI use case at a real operation, written up as a complete reference architecture.</p>'
            + table(["Sector", "Countries", "Industrial AI use cases"], [[f"<strong>{E(s)}</strong>", E(w), ", ".join(link(d) for d in g)] for s, g, w in secs])
            + '<h2 id="architecture">The architecture of industrial AI</h2>'
            + f'<p class="ans">{E(lead_l)}</p>' + table(["Layer", "What it holds"], rows_l)
            + steps([(IND, "Industrial AI reference architecture", "every design by sector, with patterns, layers, compute, cost and DOI"),
                     (DAT, "Industrial data ontology", "the data model under each industrial AI design"),
                     (PHY, "Physical AI system design", "how each one was designed, decision by decision")])
            + '<h2 id="data">Industrial AI starts with the data the operation already has</h2>'
            + f'<p class="ans">No design here begins with a new data platform. Each reads the systems of record the operation already runs, read only, '
              f'and joins them in an object model; the models come after. Browse every object model at <a href="{BASE}/{ONT}/">industrial ontology examples</a>.</p>'
            + src(IAI, today))
    title = f"Industrial AI: use cases, architecture and {n} open designs by sector"
    desc = f"Industrial AI reads an operation's own systems, joins them in one object model and puts each decision before its owner. {n} open designs."
    ld = ld_pair(IAI, "Industrial AI", desc, today, ["industrial AI", "AI in manufacturing", "industrial AI reference architecture"], "What is industrial AI?", answer, ds)
    md = md_head("Industrial AI", IAI, answer)
    md += ["## Industrial AI use cases by sector", ""] + md_table(["Sector", "Countries", "Industrial AI use cases"],
          [[s, w, ", ".join(f"[{d['short']}]({d['url']})" for d in g)] for s, g, w in secs]) + [""]
    md += ["## The architecture of industrial AI", "", lead_l, ""] + md_table(["Layer", "What it holds"], [[f"{i + 1}. {a}", b] for i, (a, b) in enumerate(T.LAYERS)]) + [""]
    md += steps_md([(IND, "Industrial AI reference architecture", "every design by sector"), (DAT, "Industrial data ontology", "the data model")])
    write(IAI, title, desc, body, ld, md)
    return n


def ontologies(ds, today):
    objs = [json.loads(l) for l in (ROOT / "dataset" / "objects.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    n, no = len(ds), len(objs)
    nl = sum(len(o.get("links", [])) for o in objs)
    kinds = Counter(o.get("kind") or "object" for o in objs)
    countries = Counter(d["country"] for d in ds)
    secs = sorted({d["sector"] for d in ds})
    answer = (f"An ontology is a typed model of a domain: the kinds of things in it, the properties each one has, and the named links between them. "
              f"Ontologies let people and AI agents work from one shared model instead of many tables. In an industrial operation, an ontology names "
              f"each asset, record, event, site and person the operation holds, anchors each one in the system that stores its data, and joins them "
              f"by typed links. CodeNinja Atoms has published {n} ontologies of real operations across {len(secs)} sectors in {where(countries)}: "
              f"{no} objects and {nl} links, each downloadable as hyper-ontology/1 JSON under CC BY 4.0.")
    kinds = Counter({k: c for k, c in kinds.items() if k in KINDS})
    krows = [[f"<strong>{E(k)}</strong>", E(KINDS.get(k, "")), str(c)] for k, c in kinds.most_common()]
    srows = []
    for s in secs:
        g = [d for d in ds if d["sector"] == s]
        srows.append([f"<strong>{E(s[:1].upper() + s[1:])}</strong>", str(sum(d.get("n_objects") or 0 for d in g)), ", ".join(link(d) for d in g)])
    body = (f'<p class="eyebrow">Ontologies</p><h1>Ontologies</h1><p class="lead">{E(answer)}</p>'
            f'<div class="stats"><span><b>{n}</b>published ontologies</span><span><b>{no}</b>objects</span><span><b>{nl}</b>typed links</span>'
            f'<span><b>{len(secs)}</b>sectors</span></div>'
            + '<h2 id="contains">What an ontology contains</h2>'
            + f'<p class="ans">Objects of a few kinds, each with properties, status values and links. The counts are read from the {n} published ontologies.</p>'
            + table(["Kind", "What it is", "Objects"], krows)
            + '<h2 id="examples">Ontology examples by sector</h2>'
            + '<p class="ans">Every published ontology belongs to one real operation. Open a design to read its object model, or download it as JSON.</p>'
            + table(["Sector", "Objects", "Ontologies"], srows)
            + steps([(ONT, "Industrial ontology examples", "every published object model, browsable and downloadable"),
                     (DAT, "Industrial data ontology", "what an industrial data ontology holds, kind by kind")])
            + '<h2 id="agents">Ontologies for AI agents</h2>'
            + f'<p class="ans">An agent that reads an ontology reasons over named objects instead of raw rows, and every action it proposes names the object it touches. '
              f'The published ontologies load with the open <a href="{BASE}/developer/reference/loader/">loader</a>, are served to agents by the '
              f'<a href="{BASE}/developer/reference/mcp-server/">MCP server</a>, follow the <a href="{BASE}/developer/reference/hyper-ontology-1/">hyper-ontology/1 format</a>, '
              f'and stand up as a living ontology in <a href="{BASE}/hyper-ontology/">Hyper Ontology</a>.</p>'
            + src(ONTS, today))
    title = f"Ontologies: what they are, what they contain, and {n} open examples"
    desc = f"Ontologies are typed models of a domain: objects, properties and links. What they contain, and {n} open ontologies of real operations."
    ld = ld_pair(ONTS, "Ontologies", desc, today, ["ontologies", "ontology", "knowledge graph", "industrial ontology"], "What is an ontology?", answer, ds)
    md = md_head("Ontologies", ONTS, answer)
    md += ["## What an ontology contains", ""] + md_table(["Kind", "What it is", "Objects"], [[k, KINDS.get(k, ""), c] for k, c in kinds.most_common()]) + [""]
    md += ["## Ontology examples by sector", ""] + md_table(["Sector", "Objects", "Ontologies"],
          [[s, sum(d.get("n_objects") or 0 for d in ds if d["sector"] == s), ", ".join(f"[{d['short']}]({d['url']})" for d in ds if d["sector"] == s)] for s in secs]) + [""]
    md += steps_md([(ONT, "Industrial ontology examples", "every object model"), (DAT, "Industrial data ontology", "kind by kind")])
    write(ONTS, title, desc, body, ld, md)
    return no


def self_improving_systems(ds, today):
    import padi
    j = padi.load()
    L = j["latest"] if j else None
    loops = len(j["cycles"]) if j else 0
    n = len(ds)
    hl = sum(1 for d in ds if d.get("human_loop"))
    answer = ("A self-improving system is a system that measures its own output, finds where it fell short, and changes itself so the next round does "
              "better, without a person rewriting it each time. In AI the safest form improves the system's context (its documents, models of the domain, "
              "rules and records of past gaps) rather than its weights, so every change can be read and reverted. CodeNinja runs Praxis this way and "
              f"publishes each loop's results in the open" + (f": {loops} RSI loops so far, the latest at {L['platform_pct']:.1f}% of checks passed against "
              f"frontier AI on its own at {L['bare_pct']:.1f}%." if L else "."))
    body = (f'<p class="eyebrow">Self-improving systems</p><h1>Self-improving systems</h1><p class="lead">{E(answer)}</p>'
            + (f'<div class="stats"><span><b>{loops}</b>RSI loops published</span><span><b>{L["platform_pct"]:.1f}%</b>Praxis, latest loop</span>'
               f'<span><b>{L["bare_pct"]:.1f}%</b>frontier AI, same tasks</span><span><b>{n}</b>designs produced</span></div>' if L else "")
            + '<h2 id="works">How self-improving systems work</h2>'
            + '<ol class="ans">' + "".join(f"<li><b>{a}</b> {b}</li>" for a, b in WORKS) + "</ol>"
            + '<h2 id="safe">What makes a self-improving system safe to run</h2>'
            + '<ul class="ans"><li><b>Fresh tasks.</b> A gain only counts on work the system has not seen, and a blind set checks it.</li>'
              '<li><b>Readable changes.</b> What changes between rounds is written down and can be reverted, one change at a time.</li>'
              '<li><b>A baseline.</b> The same tasks are scored for a system that does not improve, so the difference is the improvement.</li>'
              f'<li><b>A person in control.</b> {hl} of the {n} published designs name the person who approves each action that changes the physical world.</li></ul>'
            + '<h2 id="measured">A self-improving system measured in the open</h2>'
            + f'<p class="ans">Praxis is measured on <a href="{BASE}/padi/">PADI</a>, the Physical AI Design Index, against frontier AI on its own, loop by loop. '
              f'The results, the blind evaluation and the {n} designs it produced are on one page.</p>'
            + steps([(RSI, "Self-improving AI system", "Praxis measured RSI loop by RSI loop, and what it produced"),
                     (f"padi", "PADI", "the benchmark, its tasks by industry and its limitations")])
            + src(SIS, today))
    title = "Self-improving systems: how they work, and one measured in the open"
    desc = "Self-improving systems measure their output, find gaps and improve their context. How they work, what makes them safe, and one measured in the open."
    ld = ld_pair(SIS, "Self-improving systems", desc, today, ["self-improving systems", "self-improving system", "recursive self improvement"],
                 "What is a self-improving system?", answer, ds)
    md = md_head("Self-improving systems", SIS, answer)
    md += ["## How self-improving systems work", ""] + [f"{i}. **{a}** {b}" for i, (a, b) in enumerate(WORKS, 1)] + [""]
    md += steps_md([(RSI, "Self-improving AI system", "Praxis loop by loop"), ("padi", "PADI", "the benchmark")])
    write(SIS, title, desc, body, ld, md)
    return loops


def main():
    ds = designs()
    today = datetime.date.today().isoformat()
    print(f"{PAI}/ {physical_ai(ds, today)} designs")
    print(f"{IAI}/ {industrial_ai(ds, today)} designs")
    print(f"{ONTS}/ {ontologies(ds, today)} objects")
    print(f"{SIS}/ {self_improving_systems(ds, today)} loops")


if __name__ == "__main__":
    main()
