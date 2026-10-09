"""The developer home: /developer/ is where developers start with Hyper, the architecture under
everything CodeNinja builds. Hub (capabilities, getting started, reference, samples, platform
updates, community), reference pages rendered from the repository's own documents, and a
platform-updates page built from git history. All from existing material; nothing is invented.
    python tools/developer.py        # site_index.py runs it before seo.py
Community threads come from developer/discussions.json, written by tools/discussions_pull.py.
"""
import html, json, re, datetime, subprocess
from collections import defaultdict
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
DEV = ROOT / "developer"
BASE = "https://codeatoms.ai"
REPO = "https://github.com/muhammadumar89/codeninja-research"
DISC = f"{REPO}/discussions"
E = lambda s: html.escape(str(s), quote=True)

HEADLINE = "Hyper. The architecture under everything CodeNinja builds."
LEDE = ("Hyper is the architecture CodeNinja's platforms are built on. Praxis designs a physical AI system. Hyper Ontology structures the "
        "operation's context. Hyper Pragma runs agents inside the enterprise boundary. Hyper Engram keeps the decision memory every run reads "
        "before it acts. Hyper Noesis opens the models an organization owns so their reasoning can be inspected. CodeNinja Atoms, the reference "
        "architectures on this site, is the first thing built on it. This is where developers start.")

# One card per capability. The sentences are Umar's own (the About page, the Praxis page, the first blog post).
CAPS = [
    {"name": "Praxis", "verb": "Design a physical AI system", "status": "Beta, open to outside engineers",
     "what": "Praxis turns an operator's requirement into a complete design for physical AI, with every claim on a record and a person on every write.",
     "build": "A complete system design for one operation: what to sense, where each model runs, the object model, the hardware, the three-year cost and who approves every action.",
     "links": [("Praxis", f"{BASE}/praxis/"), ("Join the beta", brand.SIGNUP)]},
    {"name": "Hyper Ontology", "verb": "Structure the operation", "status": "Beta, a small number of teams",
     "what": "Hyper Ontology holds the governed model of the organization. It imports the object model a Praxis design publishes and stands it up as a living system over the operator's own systems of record.",
     "build": "A living ontology over an operator's existing systems: typed objects, typed links, and actions that sense, decide, act and learn.",
     "links": [("How it becomes living", f"{BASE}/hyper-ontology/"), ("Package format", f"{BASE}/developer/reference/hyper-ontology-1/")]},
    {"name": "Hyper Pragma", "verb": "Run agents inside the boundary", "status": "Used in house, not yet open",
     "what": "Hyper Pragma is agent execution inside the enterprise boundary, on models the organization can change without losing what was built.",
     "build": "Agents that work on the operator's own hardware, on open-weight models the operator can swap, with the context carried across the swap.",
     "links": []},
    {"name": "Hyper Engram", "verb": "Remember every decision", "status": "Used in house, not yet open",
     "what": "Hyper Engram is decision memory each run reads before it acts: the record of what was decided, by whom, and what worked.",
     "build": "Systems that improve run over run because every run starts by reading what earlier runs and people recorded.",
     "links": []},
    {"name": "Hyper Noesis", "verb": "Inspect the model", "status": "Used in house, not yet open",
     "what": "Hyper Noesis opens models the organization owns so their reasoning can be inspected, rather than taken on trust.",
     "build": "Verification of a model's behaviour before it is trusted with an operation, and after every change of model.",
     "links": []},
]

START = [
    ("Design a system on Praxis", "Unlock free access, paste a requirement, and Praxis returns a complete system design. Every account is approved by CodeNinja, usually within a day.",
     None, [(brand.FREE, brand.SIGNUP), ("Sign in", brand.SIGNIN)]),
    ("Give your coding agent every design", "The MCP server lists, searches and reads the published designs: object models, model and hardware registers, cost lines and full papers.",
     'claude mcp add codeninja-research -- uvx --from "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=mcp-server" codeninja-research-mcp',
     [("MCP server reference", f"{BASE}/developer/reference/mcp-server/")]),
    ("Load an object model", "The loader reads any published hyper-ontology/1 package, validates it, walks its typed links and converts it to Mermaid, Cypher or JSON-LD.",
     'pip install "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=hyper-ontology-py"\nhyper-ontology show port-digital-twin-us\nhyper-ontology cypher port-digital-twin-us > load.cypher',
     [("Loader reference", f"{BASE}/developer/reference/loader/"), ("Package format", f"{BASE}/developer/reference/hyper-ontology-1/")]),
    ("Query the dataset", "Every design is a row in five tables: designs, objects, models, costs and full text. One load gives you all of them.",
     'from datasets import load_dataset\nobjects = load_dataset("CodeNinjatools/vertical-driven-architectures", "objects", split="train")\nprint(objects.filter(lambda r: r["kind"] == "event")["label"])',
     [("Dataset reference", f"{BASE}/developer/reference/dataset/"), ("On Hugging Face", "https://huggingface.co/datasets/CodeNinjatools/vertical-driven-architectures")]),
]

REFS = [
    ("hyper-ontology-1", "The hyper-ontology/1 package format", ROOT / "ONTOLOGY_PACKAGE.md",
     "What every published object model contains, the rules it follows, and what an agent does with it."),
    ("loader", "The hyper-ontology loader", ROOT / "hyper-ontology-py" / "README.md",
     "Load, validate, traverse and convert packages from the command line or Python."),
    ("mcp-server", "The MCP server", ROOT / "mcp-server" / "README.md",
     "Five tools that give a coding agent every design: list, get, read, find, and where the designs come from."),
    ("dataset", "The Vertical-Driven Architectures dataset", ROOT / "dataset" / "README.md",
     "Five tables, one row per design, object, model choice or cost line; monthly DOI snapshots."),
]

LINK_FIX = {"hyper-ontology-py/": f"{BASE}/developer/reference/loader/", "../ONTOLOGY_PACKAGE.md": f"{BASE}/developer/reference/hyper-ontology-1/",
            "ONTOLOGY_PACKAGE.md": f"{BASE}/developer/reference/hyper-ontology-1/", "mcp-server/": f"{BASE}/developer/reference/mcp-server/"}


# ---------------------------------------------------------------- markdown (headings, code fences, tables, lists, inline)
def inline(s):
    s = E(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{E(LINK_FIX.get(m.group(2), m.group(2)))}">{m.group(1)}</a>', s)
    s = re.sub(r'(?<!href=")(?<!">)(https?://[^\s<]+?)([.,;)]?)(?=\s|$|<)', r'<a href="\1">\1</a>\2', s)
    return s


def md(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    L, out, i = text.split("\n"), [], 0
    while i < len(L):
        ln = L[i]
        if ln.startswith("```"):
            lang = ln[3:].strip(); buf = []; i += 1
            while i < len(L) and not L[i].startswith("```"):
                buf.append(L[i]); i += 1
            out.append(f'<pre><code class="lang-{E(lang)}">{E(chr(10).join(buf))}</code></pre>'); i += 1; continue
        if ln.startswith("# "):
            i += 1; continue  # the page supplies its own title
        if ln.startswith("## "):
            out.append(f"<h2>{inline(ln[3:])}</h2>")
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.startswith("|"):
            rows = []
            while i < len(L) and L[i].startswith("|"):
                rows.append([c.strip() for c in L[i].strip().strip("|").split("|")]); i += 1
            head, body = rows[0], [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
            out.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>")
            continue
        elif re.match(r"^(- |\d+\. )", ln):
            ordered = ln[0].isdigit(); items = []
            while i < len(L) and re.match(r"^(- |\d+\. )", L[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", L[i])); i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
        i += 1
    return "\n".join(out)


# ---------------------------------------------------------------- data
def designs():
    rows = [json.loads(l) for l in (ROOT / "dataset" / "designs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    by = defaultdict(list)
    for r in rows:
        by[r["sector"]].append(r)
    return by, rows


def updates():
    """Platform updates from git: commits that touched the format, loader, MCP server, dataset or added designs."""
    paths = ["ONTOLOGY_PACKAGE.md", "hyper-ontology-py", "mcp-server", "dataset", "tools/package_paper.py", "tools/dataset_rows.py"]
    log = subprocess.run(["git", "log", "--date=short", "--pretty=%ad\t%h\t%s", "--"] + paths, cwd=ROOT, capture_output=True, text=True).stdout
    seen, out = set(), []
    for ln in log.splitlines():
        d, h, s = ln.split("\t", 2)
        if h in seen or s.startswith(("nightly", "Merge")):
            continue
        seen.add(h); out.append({"date": d, "sha": h, "text": s})
    return out


def discussions():
    p = DEV / "discussions.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


# ---------------------------------------------------------------- page
CSS = """
body{background:var(--paper)}html.js header.top:not(.solid):not(.open){background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d)}
.hero{background:var(--night);color:var(--on-dark);padding:160px var(--gutter) 96px}
.hero .in{max-width:var(--max);margin:0 auto}.hero h1{font-weight:300;font-size:clamp(40px,6vw,88px);line-height:1;letter-spacing:-.036em;margin:0 0 28px;max-width:16ch}
.hero p.lede{max-width:66ch;font-size:clamp(17px,1.5vw,20px)}
.hero .strip{margin:72px 0 0;padding:0;grid-template-columns:repeat(4,1fr)}.hero .strip div{border-top:1px solid var(--rule-d)}.hero .strip b{color:var(--on-dark);font-size:clamp(48px,6vw,88px)}.hero .strip span{color:var(--muted-d)}
.wrap{max-width:var(--max);margin:0 auto;padding:112px var(--gutter)}
.head{display:grid;grid-template-columns:1fr 1fr;gap:24px 64px;align-items:end;padding-bottom:40px;border-bottom:1px solid var(--rule-l);margin-bottom:40px}
.head h2{margin:0;max-width:none}.head p{font-family:var(--serif);font-weight:300;font-size:clamp(19px,1.8vw,24px);line-height:1.4;color:var(--ink);margin:0;max-width:34ch}
.caps{display:grid;grid-template-columns:repeat(5,1fr);gap:28px}
.cap{border-top:1px solid var(--ink);padding-top:16px;display:flex;flex-direction:column;gap:10px;min-height:100%}
.cap .m{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.cap h3{font-family:var(--sans);font-weight:400;font-size:22px;letter-spacing:-.02em;margin:0}.cap h3 small{display:block;font-size:14px;color:var(--muted-l);margin-top:4px;letter-spacing:0}
.cap p{margin:0;font-size:14.5px;line-height:1.55;color:var(--muted-l)}.cap p.b{color:var(--ink)}
.cap .st{margin-top:auto;padding-top:10px;font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;color:var(--muted-l)}.cap .st.on{color:var(--ink)}
.cap .ln a{font-size:14px;color:var(--ink);margin-right:14px}
.steps{display:grid;grid-template-columns:repeat(2,1fr);gap:40px 48px;counter-reset:s}
.step{border-top:1px solid var(--ink);padding-top:16px;counter-increment:s}
.step h3{font-family:var(--sans);font-weight:400;font-size:22px;letter-spacing:-.02em;margin:0 0 8px}.step h3::before{content:counter(s,decimal-leading-zero) "  ";font-family:var(--mono);font-size:12px;color:var(--muted-l);letter-spacing:.06em}
.step p{margin:0 0 14px;font-size:15px;line-height:1.55;color:var(--muted-l)}.step .ln a{font-size:14px;color:var(--ink);margin-right:14px}
pre{font-family:var(--mono);font-size:13px;line-height:1.55;background:#111218;color:#E6E6E3;padding:16px 18px;overflow:auto;margin:0 0 14px;border-radius:0}
code{font-family:var(--mono);font-size:.9em}p code,li code,td code{background:rgba(30,31,43,.07);padding:1px 5px;color:var(--ink)}
.refs{display:grid;grid-template-columns:repeat(2,1fr);gap:28px}.ref{border-top:1px solid var(--ink);padding-top:16px;text-decoration:none;color:inherit}
.ref h3{font-family:var(--sans);font-weight:400;font-size:22px;letter-spacing:-.02em;margin:0 0 8px}.ref p{margin:0;font-size:15px;line-height:1.55;color:var(--muted-l)}.ref:hover h3{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}
.samples{columns:3;column-gap:40px}.samples section{break-inside:avoid;margin-bottom:28px}.samples h3{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);margin:0 0 8px;border-top:1px solid var(--ink);padding-top:12px}
.samples a{display:block;color:var(--ink);text-decoration:none;font-size:16px;padding:7px 0;border-bottom:1px solid var(--rule-l)}.samples a:hover{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}.samples a small{display:block;font-size:12.5px;color:var(--muted-l)}
.updates{list-style:none;margin:0;padding:0;border-top:1px solid var(--ink)}.updates li{display:grid;grid-template-columns:120px 1fr;gap:24px;padding:14px 0;border-bottom:1px solid var(--rule-l);font-size:15px}
.updates time{font-family:var(--mono);font-size:11px;letter-spacing:.04em;color:var(--muted-l);padding-top:3px}.updates a{color:var(--ink);text-decoration:none}.updates a:hover{text-decoration:underline}
.comm{display:grid;grid-template-columns:1fr 1fr;gap:40px 64px}.cats{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink)}.cats li{padding:14px 0;border-bottom:1px solid var(--rule-l);font-size:15px;color:var(--muted-l)}.cats li a{color:var(--ink);font-size:17px;text-decoration:none}.cats li a:hover{text-decoration:underline}
.threads{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink)}.threads li{padding:12px 0;border-bottom:1px solid var(--rule-l)}.threads a{color:var(--ink);text-decoration:none;font-size:16px}.threads small{display:block;font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;color:var(--muted-l);margin-top:4px}
.doc{max-width:860px;margin:0 auto;padding:132px var(--gutter) 96px;font-size:16.5px;line-height:1.65;color:rgba(30,31,43,.88)}
.doc h1{font-weight:300;font-size:clamp(34px,4.6vw,60px);line-height:1.04;letter-spacing:-.032em;color:var(--ink);margin:0 0 14px}.doc p.lead{font-family:var(--serif);font-weight:300;font-size:clamp(20px,2vw,25px);line-height:1.4;color:var(--muted-l);margin:0 0 44px}
.doc h2{font-size:clamp(24px,2.6vw,32px);letter-spacing:-.024em;color:var(--ink);margin:56px 0 14px;padding-top:20px;border-top:1px solid var(--ink)}.doc h3{font-size:19px;letter-spacing:-.012em;color:var(--ink);margin:30px 0 8px}
.doc p{margin:0 0 16px}.doc a{color:var(--ink)}.doc ul,.doc ol{padding-left:22px;margin:0 0 18px}.doc li{margin:0 0 6px}
.doc .tw{overflow-x:auto;margin:18px 0 26px}.doc table{width:100%;border-collapse:collapse;font-size:14.5px}.doc th{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);text-align:left;border-bottom:1px solid var(--ink);padding:10px 14px 10px 0}.doc td{border-bottom:1px solid var(--rule-l);padding:10px 14px 10px 0;vertical-align:top}
.doc .src{font-size:14px;color:var(--muted-l);border-top:1px solid var(--rule-l);padding-top:16px;margin-top:56px}.doc .src a{color:var(--muted-l)}
.crumb{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);margin:0 0 22px}.crumb a{color:inherit;text-decoration:none}
@media (max-width:1100px){.caps{grid-template-columns:repeat(3,1fr)}.samples{columns:2}}
@media (max-width:820px){.hero{padding:120px var(--gutter) 64px}.hero .strip{grid-template-columns:repeat(2,1fr);margin-top:48px}.wrap{padding:72px var(--gutter)}.head,.steps,.refs,.comm{grid-template-columns:1fr}.caps{grid-template-columns:1fr}.samples{columns:1}.updates li{grid-template-columns:1fr;gap:4px}.doc{padding:100px var(--gutter) 64px}}
"""


def nav():
    return [("Research", f"{BASE}/#research"), ("Sectors", f"{BASE}/sectors/"), ("Co-build", f"{BASE}/co-build/"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"), ("PADI", f"{BASE}/padi/"),
            ("Developers", f"{BASE}/developer/"), ("Blog", f"{BASE}/blog/"), ("About", f"{BASE}/about/")]


def shell(path, title, desc, body, ld, og_type="website"):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{path}">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", nav(), access=brand.SIGNUP)}
<main>{body}</main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Code Apache-2.0 · Papers, object models and data CC BY 4.0 · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}</body></html>"""


def hub(by, rows, ups, threads):
    n_obj = sum(int(r.get("n_objects") or 0) for r in rows)
    caps = "".join(
        f'<div class="cap"><span class="m">{E(c["verb"])}</span><h3>{E(c["name"])}</h3><p class="b">{E(c["what"])}</p><p><strong>Build with it:</strong> {E(c["build"])}</p>'
        + (('<p class="ln">' + "".join(f'<a href="{u}">{E(t)}</a>' for t, u in c["links"]) + "</p>") if c["links"] else "")
        + f'<span class="st{" on" if c["status"].startswith("Beta") else ""}">{E(c["status"])}</span></div>' for c in CAPS)
    steps = "".join(f'<div class="step"><h3>{E(t)}</h3><p>{E(d)}</p>' + (f"<pre><code>{E(code)}</code></pre>" if code else "")
                    + '<p class="ln">' + "".join(f'<a href="{u}">{E(x)}</a>' for x, u in links) + "</p></div>" for t, d, code, links in START)
    refs = "".join(f'<a class="ref" href="{BASE}/developer/reference/{s}/"><h3>{E(t)}</h3><p>{E(d)}</p></a>' for s, t, _p, d in REFS)
    samples = "".join(f"<section><h3>{E(sec)}</h3>" + "".join(f'<a href="{r["canonical_url"]}">{E(r["title"].split(":")[0])}<small>{E(r["country"])} · {r["n_objects"]} objects · DOI {E(r["doi"])}</small></a>' for r in rs) + "</section>"
                      for sec, rs in sorted(by.items()))
    upl = "".join(f'<li><time>{u["date"]}</time><a href="{REPO}/commit/{u["sha"]}">{E(u["text"])}</a></li>' for u in ups[:8])
    cats = [("Announcements", "What changed, release by release.", "announcements"), ("Q&A", "Ask about a design, a package, the loader or the MCP server.", "q-a"),
            ("Show and tell", "What you built on Hyper: an ontology over your systems, an agent, a tool.", "show-and-tell"), ("Ideas", "What the next design, format or tool should be.", "ideas")]
    catl = "".join(f'<li><a href="{DISC}/categories/{slug}">{E(n)}</a><br>{E(d)}</li>' for n, d, slug in cats)
    thl = ("".join(f'<li><a href="{t["url"]}">{E(t["title"])}</a><small>{E(t["category"])} · {E(t["author"])} · {t["date"]}</small></li>' for t in threads[:6])
           if threads else f'<li><a href="{DISC}/new?category=q-a">Start the first thread</a><small>Q&amp;A · open to everyone with a GitHub account</small></li>')
    body = f"""<section class="hero"><div class="in"><p class="eyebrow">Developers</p><h1>{E(HEADLINE)}</h1><p class="lede">{E(LEDE)}</p>
<div class="strip"><div><b>5</b><span>capabilities, one architecture</span></div><div><b>{len(rows)}</b><span>reference designs built on it</span></div><div><b>{n_obj}</b><span>typed objects published as packages</span></div><div><b>1</b><span>package format, loader and MCP server, all open</span></div></div></div></section>
<section class="light" id="capabilities"><div class="wrap"><div class="head"><h2>Capabilities</h2><p>Five platforms on one architecture. Each does one thing in the life of an operation's context, and each is built on Hyper.</p></div><div class="caps">{caps}</div></div></section>
<section class="light alt" id="start"><div class="wrap"><div class="head"><h2>Getting started</h2><p>Four ways in, all open today. Pick the one that matches what you are building.</p></div><div class="steps">{steps}</div></div></section>
<section class="light" id="reference"><div class="wrap"><div class="head"><h2>Reference</h2><p>The formats and tools, documented from the repository itself.</p></div><div class="refs">{refs}</div></div></section>
<section class="light alt" id="samples"><div class="wrap"><div class="head"><h2>Samples</h2><p>Every published design is a worked example: a complete system built on Hyper for one real operation, with its object model as a package you can load.</p></div><div class="samples">{samples}</div></div></section>
<section class="light" id="updates"><div class="wrap"><div class="head"><h2>Platform updates</h2><p>What changed in the format, the loader, the MCP server and the dataset, from the repository's history. <a href="{BASE}/developer/updates/">All updates</a></p></div><ul class="updates">{upl}</ul></div></section>
<section class="light alt" id="community"><div class="wrap"><div class="head"><h2>Community</h2><p>Questions, answers and what people build live in the repository's discussions. A GitHub account is all it takes.</p></div>
<div class="comm"><div><ul class="cats">{catl}</ul><p style="margin-top:20px"><a class="btn solid" href="{DISC}">Open the discussions</a></p></div><div><p class="mono" style="margin:0 0 10px">Latest threads</p><ul class="threads">{thl}</ul>
<p style="margin-top:28px;font-size:14.5px;color:var(--muted-l)">Also: <a href="{BASE}/blog/">the engineering blog</a> and <a href="{BASE}/blog/feed.xml">its feed</a>, <a href="{REPO}/issues">issues</a> for bugs in the loader or the server, and the <a href="https://huggingface.co/CodeNinjatools">Hugging Face organization</a> for every dataset and Space.</p></div></div></div></section>"""
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Hyper for developers", "url": f"{BASE}/developer/", "description": LEDE,
           "isPartOf": {"@id": f"{BASE}/#website"}, "publisher": {"@id": f"{BASE}/#org"},
           "about": [{"@type": "SoftwareApplication", "name": c["name"], "description": c["what"], "applicationCategory": "DeveloperApplication",
                      "creator": {"@id": f"{BASE}/#org"}} for c in CAPS]},
          {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": "codeninja-research", "codeRepository": REPO, "programmingLanguage": "Python",
           "license": "https://www.apache.org/licenses/LICENSE-2.0", "description": "The hyper-ontology/1 package format, the loader, the MCP server and the dataset tools.", "author": {"@id": f"{BASE}/#org"}}]
    return shell("developer/", "Developers | Hyper, the architecture under CodeNinja Atoms", LEDE[:300], body, ld)


def ref_page(slug, title, path, desc):
    body_html = md(path.read_text(encoding="utf-8"))
    rel = path.relative_to(ROOT).as_posix()
    body = (f'<div class="doc"><p class="crumb"><a href="{BASE}/developer/">Developers</a> · Reference</p><h1>{E(title)}</h1><p class="lead">{E(desc)}</p>{body_html}'
            f'<p class="src">Source: <a href="{REPO}/blob/main/{rel}">{rel}</a> in the repository. This page is generated from it and updates with it.</p></div>')
    ld = [{"@context": "https://schema.org", "@type": "TechArticle", "headline": title, "description": desc, "url": f"{BASE}/developer/reference/{slug}/",
           "isPartOf": {"@id": f"{BASE}/#website"}, "publisher": {"@id": f"{BASE}/#org"}, "license": "https://creativecommons.org/licenses/by/4.0/", "inLanguage": "en"}]
    return shell(f"developer/reference/{slug}/", f"{title} | CodeNinja Atoms Developers", desc, f'<section class="light">{body}</section>', ld, "article")


def updates_page(ups):
    by = defaultdict(list)
    for u in ups:
        by[u["date"][:7]].append(u)
    secs = "".join(f'<h2>{datetime.date.fromisoformat(m + "-01").strftime("%B %Y")}</h2><ul class="updates">' + "".join(f'<li><time>{u["date"]}</time><a href="{REPO}/commit/{u["sha"]}">{E(u["text"])}</a></li>' for u in us) + "</ul>"
                   for m, us in sorted(by.items(), reverse=True))
    body = (f'<div class="doc"><p class="crumb"><a href="{BASE}/developer/">Developers</a> · Platform updates</p><h1>Platform updates</h1>'
            f'<p class="lead">Every change to the package format, the loader, the MCP server and the dataset, newest first, from the repository\'s history. New designs appear here as they are published.</p>{secs}'
            f'<p class="src">Follow along: <a href="{REPO}/commits/main">commits</a>, <a href="{DISC}/categories/announcements">announcements</a>, <a href="{BASE}/feed.xml">the research feed</a>.</p></div>')
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Platform updates", "url": f"{BASE}/developer/updates/", "isPartOf": {"@id": f"{BASE}/#website"}}]
    return shell("developer/updates/", "Platform Updates | CodeNinja Atoms Developers", "Every change to the Hyper package format, loader, MCP server and dataset, newest first.", f'<section class="light">{body}</section>', ld)


def main():
    by, rows = designs()
    ups = updates()
    threads = discussions()
    DEV.mkdir(exist_ok=True)
    (DEV / "index.html").write_text(hub(by, rows, ups, threads), encoding="utf-8")
    for slug, title, path, desc in REFS:
        d = DEV / "reference" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(ref_page(slug, title, path, desc), encoding="utf-8")
        (d / "index.md").write_text(f"# {title}\n\nCanonical: {BASE}/developer/reference/{slug}/\nSource: {REPO}/blob/main/{path.relative_to(ROOT).as_posix()}\n\n" + path.read_text(encoding="utf-8"), encoding="utf-8")
    (DEV / "updates").mkdir(exist_ok=True)
    (DEV / "updates" / "index.html").write_text(updates_page(ups), encoding="utf-8")
    print(f"developer: hub, {len(REFS)} reference pages, {len(ups)} updates, {len(threads)} threads")


if __name__ == "__main__":
    main()
