"""Co-build pages: /co-build/ and /co-build/<sector>/ for all 13 sectors, with ONE form.

The distribution engine's F1 door (Umar, 8 Oct 2026): a decision maker at a leading
physical-world company finds us and asks to co-build an ontology for their operation.
What CodeNinja Atoms brings is drawn from the published designs only (counts come from
dataset/designs.jsonl); what the partner brings is the operation and its data. A sector
with nothing published yet shows its published neighbours as proof.

    python tools/co_build.py     # before site_index.py (which runs seo.py last)
"""
import html, json, datetime
from collections import defaultdict
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
TODAY = datetime.date.today().isoformat()

# The 13 sectors of the design grid (~/padi/lanes.json), in the order the grid lists them.
# key = url slug, value = (display name, the dataset's sector string or None, one true line about the operation)
SECTORS = [
    ("mining", "Mining", None,
     "Haul roads, pits and plants put people, light vehicles and very large machines in the same space, and the records of what happened sit in separate systems."),
    ("discrete-manufacturing-and-automotive", "Discrete manufacturing and automotive", None,
     "An assembly line measures quality, downtime and traceability in different systems, and none of them holds the whole build history of one unit."),
    ("energy-and-utilities", "Energy and utilities", "energy and utilities",
     "Grids and plants run on control systems, maintenance records and field crews that were never designed to share one picture of risk."),
    ("maritime-and-ports", "Maritime and ports", "maritime and ports",
     "Terminals and port authorities run gates, cranes, yards and finance on separate systems, so nobody sees the whole flow of a box or a truck."),
    ("rail-transport", "Rail transport", None,
     "Track, rolling stock, signalling and the works programme are measured by different teams, and a condition record rarely reaches the people planning the work."),
    ("aviation-manufacturing", "Aviation manufacturing", None,
     "Aerostructures carry an inspection and conformity record for every part, and that record usually lives apart from the shop floor that produced it."),
    ("defense-and-intelligence", "Defense and intelligence", None,
     "Sustainment, readiness and surveillance data are held under rules about where they may sit and who may read them, which is what a sovereign design has to answer first."),
    ("heavy-industry-and-construction", "Heavy industry and construction", "heavy industry and construction",
     "Mills, factories and building sites produce counts, alarms and progress data in many systems, and each one sees only part of the operation."),
    ("semiconductors", "Semiconductors", None,
     "A fab already measures almost everything, so the question is not more sensing but one object model that ties tool, lot, recipe and yield together."),
    ("supply-chain-and-logistics", "Supply chain and logistics", None,
     "A shipment is handed between carriers, yards and customs systems, and each handover loses part of what the last one knew."),
    ("agriculture-and-earth-observation", "Agriculture and earth observation", "agriculture and earth observation",
     "Farms, irrigation and land use are watched by sensors, satellites and aircraft, but the readings, the licences and the field records usually sit in separate systems."),
    ("oil-and-gas", "Oil and gas", "oil and gas",
     "Wells, terminals and plants hold safety, inventory and process data in systems that were never joined, often on sites where the data may not leave the country."),
    ("warehousing-and-intralogistics", "Warehousing and intralogistics", None,
     "A warehouse knows its stock and its orders, but not usually where its people, trucks and handling equipment are at the same moment."),
]

BRING_YOU = [
    ("The operation", "One plant, terminal, mine, farm or network, and the outcome you want from it, in your own words. One operation, not a programme."),
    ("The systems that already hold the records", "Control systems, maintenance and ERP records, cameras, inspection sheets, whatever already exists. Nothing new has to be bought to start."),
    ("One engineer who knows the place", "Somebody who can say what an alarm really means on your site and where a number comes from."),
    ("Where the data may sit", "Your rule, not ours: in country, on your own hardware, air gapped, or in a region you name."),
]

OUT = [
    ("A reference architecture for your operation", "Sensing, edge, compute, the models and their licences, the sizing arithmetic and the three year cost against the alternatives."),
    ("An object model you own", "The operation written as objects and links in the hyper-ontology/1 package format, ready to load into Hyper Ontology over your own systems."),
    ("A document your own engineers can argue with", "Every number sourced, every choice stated against what it was chosen over, and the approvals and human control written down."),
    ("Published or private, your call", "Every design published on this site has the operator removed. Yours is published the same way, under CC BY 4.0, or stays private."),
]


def designs():
    rows = [json.loads(l) for l in (ROOT / "dataset" / "designs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    by = defaultdict(list)
    for r in rows:
        by[r.get("sector")].append(r)
    for k in by:
        by[k].sort(key=lambda r: (r.get("country") or "", r.get("published") or ""))
    return by, rows


def dtable(ds):
    head = "<tr><th>Design</th><th>Country</th><th>Objects</th><th>Models</th><th>Record</th></tr>"
    body = "".join(
        f'<tr><td><a href="{E(d.get("canonical_url"))}">{E(d["title"].split(":")[0])}</a></td><td>{E(d.get("country"))}</td>'
        f'<td>{d.get("n_objects") or ""}</td><td>{d.get("n_models") or ""}</td>'
        f'<td>' + (f'<a href="https://doi.org/{E(d["doi"])}">DOI</a>' if d.get("doi") else "") + "</td></tr>" for d in ds)
    return f'<div class="tw"><table>{head}{body}</table></div>'


def cards(ds, note=None):
    out = []
    for d in ds:
        line = note(d) if note else f'{d.get("country")} · {d.get("n_objects")} objects · {d.get("n_models")} models'
        out.append(f'<a class="c" href="{E(d.get("canonical_url"))}"><h3>{E(d["title"].split(":")[0])}</h3><p>{E(line)}</p></a>')
    return f'<div class="cards">{"".join(out)}</div>'


ADJ = {"Semiconductors": "semiconductor"}


def lower(name):
    return name[0].lower() + name[1:]


def adj(name):
    """The sector as a modifier before a noun: 'a semiconductor design', 'a mining design'."""
    return ADJ.get(name, lower(name))


def headline(name):
    """The noun phrase after 'Co-build': 'a mining ontology', 'an ontology for energy and utilities'."""
    l = lower(name)
    if " and " in l:
        return f"an ontology for {l}"
    a = "an" if l[0] in "aeiou" else "a"
    return f"{a} {adj(name)} ontology"


def clist(countries):
    """Countries in prose: 'the United States, Saudi Arabia and Pakistan'."""
    cs = ["the United States" if c == "United States" else c for c in countries]
    return cs[0] if len(cs) == 1 else ", ".join(cs[:-1]) + " and " + cs[-1]


def an_op(name):
    """'a mining operation', 'an energy and utilities operation'."""
    l = lower(name)
    return ("an " if l[0] in "aeiou" else "a ") + l + " operation"


def neighbour_note(d):
    return f'{d.get("sector")} · {d.get("country")} · {d.get("n_objects")} objects'


def form(sector_name):
    """The one co-build form. Composes an email to CodeNinja's inbound address; the static site stores nothing."""
    inbox = brand.INBOX
    return f"""<form class="access" id="cb-form">
<label>Name<input name="fullname" required autocomplete="name"></label>
<label>Work email<input name="email" type="email" required autocomplete="email"></label>
<label>Organization<input name="org" required autocomplete="organization"></label>
<label>Your role<input name="role" autocomplete="organization-title" placeholder="For example: CIO, VP engineering, plant manager"></label>
<label>Where the operation is<select name="country"><option>United States</option><option>Saudi Arabia</option><option>Pakistan</option><option>Elsewhere</option></select></label>
<label>Where you want to start<select name="start"><option value="Start from the nearest published design" selected>Start from the nearest published design (recommended)</option><option value="A new design for our operation">A new design for our operation</option><option value="An ontology over systems we already have">An ontology over systems we already have</option></select></label>
<label class="full">The operation you want to make living<textarea name="usecase" required placeholder="One operation and the outcome you want from it. For example: fewer near misses between haul trucks and people on one open pit, or one record of every lot and tool in one fab."></textarea></label>
<input class="hp" name="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<button type="submit">Ask to co build</button>
<p class="note">Opens your email app with the request addressed to {inbox}; nothing is stored on this site. Prefer a form? Use the <a href="{brand.PARENT}/contact">CodeNinja contact page</a>. Organisations that would rather talk first: <a href="{brand.COMMERCIAL}">our commercial team</a>.</p>
</form>
<script>(function(){{var f=document.getElementById('cb-form');if(!f)return;f.addEventListener('submit',function(e){{e.preventDefault();if(f.hp.value)return;
var b='Sector: {sector_name}\\nName: '+f.fullname.value+'\\nEmail: '+f.email.value+'\\nOrganization: '+f.org.value+'\\nRole: '+f.role.value+'\\nOperation is in: '+f.country.value+'\\nStart: '+f.start.value+'\\n\\nOperation:\\n'+f.usecase.value+'\\n\\n(Sent from CodeNinja Atoms: '+location.href+')';
location.href='mailto:{inbox}?subject='+encodeURIComponent('Co-build: {sector_name} ('+f.org.value+')')+'&body='+encodeURIComponent(b);}});}})();</script>"""


CSS = """
.doc{max-width:1040px;margin:0 auto;padding:0 var(--gutter) 112px;font-size:17px;line-height:1.66;color:rgba(30,31,43,.88)}
.doc h1{font-weight:300;font-size:clamp(36px,4.8vw,64px);line-height:1.04;letter-spacing:-.032em;color:var(--ink);margin:0 0 24px;max-width:22ch}
.doc .lead{font-family:var(--serif);font-weight:300;font-size:clamp(21px,2.2vw,28px);line-height:1.38;color:var(--ink);margin:0 0 20px;max-width:46ch}
.doc h2{font-size:clamp(24px,2.7vw,34px);line-height:1.15;letter-spacing:-.024em;color:var(--ink);max-width:30ch;margin:88px 0 18px;padding-top:24px;border-top:1px solid var(--ink)}
.doc h3{font-weight:400;font-size:19px;letter-spacing:-.015em;color:var(--ink);margin:28px 0 6px}
.doc p{max-width:62ch}.doc a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:3px}
.doc.top{padding-top:128px}
.rec{border:1px solid var(--ink);padding:18px 20px;margin:0 0 36px;max-width:64ch;font-size:16px;background:#fff}
.rec strong{font-weight:500}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:20px 0 28px}
table{width:100%;border-collapse:collapse;font-size:14.5px;line-height:1.5}th,td{text-align:left;padding:12px 14px 12px 0;border-bottom:1px solid var(--rule-l);vertical-align:top}
th{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);border-bottom:1px solid var(--ink)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:28px;margin:28px 0 8px}
.cards a.c{display:block;border-top:1px solid var(--ink);padding-top:14px;text-decoration:none;color:var(--ink)}
.cards a.c h3{font-weight:400;font-size:20px;letter-spacing:-.02em;margin:0 0 8px}.cards a.c p{margin:0;color:var(--muted-l);font-size:14.5px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:8px 56px;margin-top:8px}
.sectorlist{list-style:none;padding:0;margin:36px 0 0;border-top:1px solid var(--ink)}
.sectorlist li{border-bottom:1px solid var(--rule-l);padding:14px 0;display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}
.sectorlist a{color:var(--ink);text-decoration:none;font-size:19px;letter-spacing:-.015em;flex:1 1 260px}
.sectorlist a:hover{text-decoration:underline}
.sectorlist span.st{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
section.film.cb{min-height:0;align-items:stretch}section.film.cb::after{background:linear-gradient(180deg,rgba(11,12,16,.82),rgba(11,12,16,.92))}
section.film.cb .inner{display:grid;grid-template-columns:1fr 1fr;gap:40px 64px;padding:120px var(--gutter)}
@media (max-width:820px){.doc{padding:0 var(--gutter) 72px;font-size:16px}.doc.top{padding-top:96px}.doc h2{margin-top:64px}.grid2{grid-template-columns:1fr}section.film.cb .inner{grid-template-columns:1fr;padding:88px var(--gutter)}}
body{background:var(--paper)}html.js header.top:not(.solid):not(.open){background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d)}
"""


def shell(path, title, desc, body, ld, form_html, form_eyebrow, form_lede, depth=2):
    nav = brand.nav(BASE + "/")
    up = "../" * depth
    vid = (f'<img class="poster" src="{up}assets/video/control-room.jpg" alt="" aria-hidden="true">'
           f'<video autoplay muted loop playsinline preload="none" poster="{up}assets/video/control-room.jpg" aria-hidden="true">'
           f'<source src="{up}assets/video/control-room.mp4" type="video/mp4"></video>')
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/{path}">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/{path}"><meta property="og:image" content="{BASE}/assets/video/control-room.jpg">
<meta name="codeninja:kind" content="co-build">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}</style></head>
<body>{brand.header(BASE + "/", nav, access="#ask")}
<main><section class="light"><div class="doc top">{body}</div></section>
<section class="film cb" id="ask">{vid}<div class="inner"><div><p class="eyebrow">{E(form_eyebrow)}</p><h2>Ask to co build</h2><p class="lede">{E(form_lede)}</p></div><div>{form_html}</div></div></section>
</main><footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Pages, papers, object models and data are CC BY 4.0 · Updated {TODAY}</span></div></footer>
{brand.SCRIPT}</body></html>"""


def sector_page(slug, name, ds, neighbours, why, totals):
    lname = lower(name)
    a = adj(name)
    hl = headline(name)
    covered = bool(ds)
    countries = sorted({d.get("country") for d in ds})
    title = f"Co-build {hl} | CodeNinja Atoms"
    desc = ((f"Co-build a sovereign physical AI reference architecture and object model for {an_op(name)} with CodeNinja Atoms. "
             f"{len(ds)} published {a} design{'s' if len(ds) != 1 else ''} ({clist(countries)}) to start from.") if covered else
            (f"Co-build the first sovereign physical AI reference architecture and object model for {an_op(name)} with CodeNinja Atoms, "
             f"starting from {totals['designs']} published designs in {totals['sectors']} other sectors."))[:300]

    rec = (f'<p class="rec"><strong>Recommended path.</strong> Start from the nearest published {a} design and we extend its '
           f'object model to your site. Send the one form below with the operation you want to make living. '
           f'<a href="#ask">Go to the form</a>.</p>') if covered else (
          f'<p class="rec"><strong>Recommended path.</strong> No {a} design is published yet, so the first one is built with a partner. '
           f'Send the one form below with the operation you want to make living, and we start from the published neighbours under this page. '
           f'<a href="#ask">Go to the form</a>.</p>')

    if covered:
        bring = (f'<h2>What we bring</h2><p>{len(ds)} published {a} reference architecture'
                 f'{"s" if len(ds) != 1 else ""}, each with its object model, its model register and its sizing and cost, '
                 f'in {clist(countries)}. All of it is CC BY 4.0 and already public.</p>{dtable(ds)}'
                 f'<p>Plus <a href="{BASE}/praxis/">Praxis</a>, the platform the designs are made on, and '
                 f'<a href="{BASE}/hyper-ontology/">Hyper Ontology</a>, which stands an object model up over your own systems.</p>')
    else:
        bring = (f'<h2>What we bring</h2><p>No {a} design is published yet. The grid is 13 sectors across the United States, '
                 f'Saudi Arabia and Pakistan, and {totals["sectors"]} of those sectors are published so far. The nearest published work '
                 f'is below: the same question of sensing, sovereign compute, an object model and who may read what, answered in another operation.</p>'
                 f'{cards(neighbours, note=neighbour_note)}'
                 f'<p>Plus <a href="{BASE}/praxis/">Praxis</a>, the platform every one of those designs was made on, and '
                 f'<a href="{BASE}/hyper-ontology/">Hyper Ontology</a>, which stands an object model up over your own systems. '
                 f'A first design in a sector is written the same way as every design already published.</p>')

    you = "".join(f"<div><h3>{E(h)}</h3><p>{E(t)}</p></div>" for h, t in BRING_YOU)
    out = "".join(f"<div><h3>{E(h)}</h3><p>{E(t)}</p></div>" for h, t in OUT)

    body = (f'<p class="eyebrow">Co-build · {E(name)}</p><h1>Co-build {E(hl)}</h1>'
            f'<p class="lead">{E(why)}</p>{rec}'
            f'{bring}'
            f'<h2>What you bring</h2><div class="grid2">{you}</div>'
            f'<h2>What comes out</h2><div class="grid2">{out}</div>'
            f'<h2>Every sector</h2><p>The same door is open for each of the 13 sectors on the grid: '
            f'<a href="{BASE}/co-build/">co-build, sector by sector</a>. Questions answered from the published designs: '
            f'<a href="{BASE}/sectors/">physical AI by sector</a>.</p>')

    faq = [("What does co-building an ontology mean?",
            f"CodeNinja Atoms designs the physical AI system for one of your {lname} operations and writes the operation as an object model "
            f"you own, in the hyper-ontology/1 package format. You bring the operation, the systems that already hold its records and one "
            f"engineer who knows the site. You get the reference architecture, the object model, the sizing arithmetic and the three year cost."),
           ("Does our data leave our country?",
            "That is your rule, not ours. Every published design is sovereign by default: open weight models on hardware the operator owns, "
            "in country, air gapped where the operation requires it."),
           (f"Is there already a {a} design to read?",
            (f"Yes. {len(ds)} published {a} reference architecture{'s' if len(ds) != 1 else ''} in {clist(countries)}, each with a DOI, "
             f"an object model and a cost appendix.") if covered else
            (f"Not yet. {totals['designs']} designs are published across {totals['sectors']} other sectors, and the nearest ones are linked on this page. "
             f"The first {a} design is built with a partner."))]

    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": f"Co-build {hl}", "description": desc,
           "url": f"{BASE}/co-build/{slug}/", "inLanguage": "en", "dateModified": TODAY,
           "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"},
           "about": [{"@type": "Thing", "name": name}, {"@type": "Thing", "name": "physical AI"}, {"@type": "Thing", "name": "sovereign AI"}, {"@type": "Thing", "name": "ontology"}],
           "mentions": [{"@type": "TechArticle", "name": d["title"], "url": d.get("canonical_url")} for d in ds]},
          {"@context": "https://schema.org", "@type": "FAQPage", "url": f"{BASE}/co-build/{slug}/",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]

    lede = (f"One operation, one outcome. We answer with the nearest published {a} design and what it would take on your site."
            if covered else
            f"One operation, one outcome. No {a} design is published yet, so the first one is built with the partner who brings the operation.")
    page = shell(f"co-build/{slug}/", title, desc, body, ld, form(name), f"Co-build · {name}", lede)
    out_dir = ROOT / "co-build" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(page, encoding="utf-8")

    md = [f"# Co-build {hl}", "", f"Canonical: {BASE}/co-build/{slug}/", "Publisher: CodeNinja Atoms (https://codeatoms.ai)",
          "License: CC BY 4.0", "", why, "",
          ("Recommended path: start from the nearest published " + a + " design; we extend its object model to your site."
           if covered else f"Recommended path: no {a} design is published yet, so the first one is built with a partner, starting from the published neighbours."), "",
          "## What we bring", ""]
    md += ([f"- [{d['title']}]({d.get('canonical_url')}) ({d.get('country')}): {d.get('n_objects')} objects, {d.get('n_models')} models"
            + (f", DOI https://doi.org/{d['doi']}" if d.get("doi") else "") for d in ds] if covered else
           [f"- Nearest published work: [{d['title']}]({d.get('canonical_url')}) ({d.get('sector')}, {d.get('country')})" for d in neighbours])
    md += ["- Praxis, the platform every design is made on: https://codeatoms.ai/praxis/",
           "- Hyper Ontology, which stands an object model up over the operator's own systems: https://codeatoms.ai/hyper-ontology/", "",
           "## What you bring", ""] + [f"- {h}: {t}" for h, t in BRING_YOU] + ["", "## What comes out", ""] + [f"- {h}: {t}" for h, t in OUT] + ["", "## Questions", ""]
    for q, a in faq:
        md += [f"### {q}", "", a, ""]
    md += [f"Ask to co-build: {BASE}/co-build/{slug}/#ask", f"Every sector: {BASE}/co-build/"]
    (out_dir / "index.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return f'<li><a href="{BASE}/co-build/{slug}/">{E(name)}</a><span class="st">' + (
        f'{len(ds)} published design{"s" if len(ds) != 1 else ""} · {E(clist(countries))}' if covered else "first design open") + "</span></li>"


def main():
    by, rows = designs()
    totals = {"designs": len(rows), "sectors": len({r.get("sector") for r in rows})}
    items = []
    for slug, name, dkey, why in SECTORS:
        ds = by.get(dkey, []) if dkey else []
        # Published neighbours as proof for an uncovered sector: one design from each covered sector, newest first.
        neighbours = []
        if not ds:
            for sec in sorted(by):
                neighbours.append(sorted(by[sec], key=lambda r: r.get("published") or "", reverse=True)[0])
        items.append(sector_page(slug, name, ds, neighbours, why, totals))

    covered = totals["sectors"]
    title = "Co-build an Ontology for Your Operation | CodeNinja Atoms"
    desc = (f"Co-build a sovereign physical AI reference architecture and object model for one of your operations with CodeNinja Atoms, "
            f"in any of 13 sectors. {totals['designs']} designs published so far across {covered} sectors and three countries.")
    body = (f'<p class="eyebrow">Co-build</p><h1>Co-build an ontology for your operation</h1>'
            f'<p class="lead">We publish the design. You bring the operation. Together they become an object model your systems can run on.</p>'
            f'<p class="rec"><strong>Recommended path.</strong> Open the page for your sector, read the nearest published design, then send the one form '
            f'with the single operation you want to make living. A sector with nothing published yet is where the first design is built with a partner.</p>'
            f'<p>CodeNinja Atoms publishes open reference architectures for physical AI: sovereign designs an operator can run on its own hardware, '
            f'under open weight licences, with the data staying where the operation requires. There are {totals["designs"]} published so far, across '
            f'{covered} of the 13 sectors on the grid, in the United States, Saudi Arabia and Pakistan. Co-building is the same work done for '
            f'your operation, with the object model handed to you.</p>'
            f'<ul class="sectorlist">{"".join(items)}</ul>'
            f'<h2>What this is not</h2><p>It is not a pilot that ends in a slide pack, and it is not a licence you buy before anything is designed. '
            f'It is one operation, one design document your engineers can argue with number by number, and one object model you own. '
            f'Engineers who want to design one themselves start on <a href="{BASE}/praxis/">Praxis</a> instead.</p>')
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Co-build an ontology", "url": f"{BASE}/co-build/",
           "description": desc, "dateModified": TODAY,
           "publisher": {"@type": "Organization", "@id": f"{BASE}/#org", "name": "CodeNinja Atoms", "url": f"{BASE}/"},
           "hasPart": [{"@type": "WebPage", "url": f"{BASE}/co-build/{s}/", "name": f"Co-build {headline(n)}"} for s, n, _d, _w in SECTORS]}]
    (ROOT / "co-build").mkdir(exist_ok=True)
    (ROOT / "co-build" / "index.html").write_text(
        shell("co-build/", title, desc, body, ld, form("Any sector"), "Co-build",
              "One operation and the outcome you want from it. Name the sector in the form and we answer with the nearest published design.", depth=1),
        encoding="utf-8")
    md = ["# Co-build an ontology for your operation", "", f"Canonical: {BASE}/co-build/", "Publisher: CodeNinja Atoms (https://codeatoms.ai)", "",
          "We publish the design. You bring the operation. Together they become an object model your systems can run on.", "",
          f"{totals['designs']} reference architectures are published so far, across {covered} of the 13 sectors on the grid, in the United States, Saudi Arabia and Pakistan.", "",
          "## Sectors", ""] + [f"- [{n}]({BASE}/co-build/{s}/)" + (f": {len(by.get(d, []))} published designs" if d and by.get(d) else ": first design open") for s, n, d, _w in SECTORS] + [
          "", "## What you bring", ""] + [f"- {h}: {t}" for h, t in BRING_YOU] + ["", "## What comes out", ""] + [f"- {h}: {t}" for h, t in OUT]
    (ROOT / "co-build" / "index.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"co-build/: index + {len(SECTORS)} sector pages ({covered} sectors published, {totals['designs']} designs)")


if __name__ == "__main__":
    main()
