"""PADI, the Physical AI Design Index: /padi/ (page + Markdown copy) and the home page block.
Renders ONLY from the results export the PADI repository produces (padi_results.json), kept in the
private launch repo so its internal source paths and notes never reach the public site. Every score
is shown as a percentage, per industry first. Need to know: the page shows what a reader needs to
trust the numbers (arms, judge, families, fresh task rule, score, limitations) and nothing about
the harness internals. A new export dropped into place updates the page, the home block, the
sitemap and llms.txt on the next build.
    python tools/padi.py            # site_index.py runs it before the home page
"""
import datetime, html, json
from collections import defaultdict
from pathlib import Path
import brand

ROOT = Path(__file__).resolve().parent.parent
SRC = Path.home() / "codeninja-launch" / "padi" / "padi_results.json"
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
NAME = "Physical AI Design Index"
# The cycle running now, beyond the last published export. Set to None when the export catches up.
RUNNING = 17
CC = {"United States": "US", "Saudi Arabia": "SA", "Pakistan": "PK"}
ONE_LINE = ("When a customer sends a short requirement for physical AI in a real operation, does the design name the rules that bind "
            "in that country, flag what the requirement leaves out, and stay clear of invented specifics? PADI scores the same model "
            "twice, bare and inside Praxis, on tasks neither has seen, across 13 industries in three countries.")
SHORT = ("Does a physical AI design name the rules that bind in that country, flag what the requirement leaves out, and stay clear of "
         "invented specifics? The same model, scored bare and inside Praxis, across 13 industries in three countries.")
FRAMING = ("PADI is the benchmark CodeNinja uses to improve Praxis release by release. Scores are far from saturated: the goal is every "
           "check on every task in all 13 industries, and the best cycle so far passes under half. We publish the trajectory as it is, "
           "including the cycles where the bare model scored higher.")
HEADINGS = ["What it does", "What it reads", "Where things run", "Sensing classes", "Models and provenance", "Binding rules",
            "Human decisions", "Phase one and its exit test", "Open questions", "Risks"]
LIMITS = [
    ("Design judgement, not deployment.", "PADI scores designs on paper. No plant, sensor or model was run."),
    ("One judge model.", "A single model reads every design through three lenses. Judging the same text again can move a few checks. No human has scored the outputs yet."),
    ("Small samples.", "Each cycle is five or six tasks and roughly a hundred checks per arm. A swing of a few points is within noise, so no single cycle is a trend."),
    ("Different tasks every cycle.", "Fresh tasks keep the measure honest, and they also mean cycles are not like for like."),
    ("Written by CodeNinja.", "Tasks and checks were written by CodeNinja with model assistance and reviewed adversarially. Independent expert grading is planned and not yet done."),
    ("Two arms.", "Only the bare model and the same model inside Praxis are scored. No other system or model is in the index yet."),
    ("Partial coverage.", "Ten of thirteen industries are measured. Aviation manufacturing, semiconductors and warehousing have not been run."),
    ("One rubric change.", "Cycle 12 used rubric 0.1. Every later cycle uses 0.2."),
]
FAQ = [
    ("What is the Physical AI Design Index?",
     "PADI is CodeNinja's benchmark for design judgement in physical AI. Each task is a short anonymised requirement for an AI system in a real kind of operation, such as a mine, a port, a rail line or a substation, plus yes or no checks. A judge model scores the design from the bare model and from the same model inside the Praxis platform."),
    ("What does PADI measure?",
     "Three families of checks: what a design must name (the regulation that binds in that country, the systems it reads, where things run, which decisions a person confirms, what phase one must prove), what it must flag (a missing fact asked as a question, a foreign rule that does not apply), and what it must never do (a part number, an invented regulation or saving, a customer name, data leaving the site when residency forbids it)."),
    ("How is PADI scored?",
     "Checks passed divided by checks total, for each arm, with no partial credit and no weighting. The judge is glm-4.6 through three lenses (a strict reviewer, a plant engineer and a regulator's technical assessor); a check passes when the majority say yes. Both arms use glm-5.3-flash."),
    ("How often is PADI updated?",
     "Once per Praxis release cycle, on tasks never run before. A third of the task bank is held out for a final blind evaluation and never run in a cycle."),
]


def pct(a, b):
    return round(100.0 * a / b, 1) if b else 0.0


def load():
    """The export plus the views the page needs, or None when no export is in place."""
    if not SRC.exists():
        return None
    j = json.loads(SRC.read_text(encoding="utf-8"))
    agg = defaultdict(lambda: {"platform": 0, "bare": 0, "of": 0, "cycles": []})
    for c in j["cycles"]:
        for s, v in c["by_sector"].items():
            a = agg[s]; a["platform"] += v["platform"]; a["bare"] += v["bare"]; a["of"] += v["of"]; a["cycles"].append(c["cycle"])
    ind = []
    for s in sorted(j["sectors"], key=lambda x: x["label"]):
        a = agg.get(s["id"])
        ind.append({**s, "measured": bool(a), "p": pct(a["platform"], a["of"]) if a else None, "b": pct(a["bare"], a["of"]) if a else None,
                    "checks": a["of"] if a else 0, "cycles": a["cycles"] if a else []})
    j["industries"] = ind
    j["latest"] = j["cycles"][-1]
    return j


# ---------------------------------------------------------------- shared pieces
CSS = """
.padi-ind{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink)}
.padi-ind li{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1.6fr);gap:10px 28px;align-items:center;padding:14px 0;border-bottom:1px solid var(--rule-l)}
.padi-ind .nm{font-size:16px;letter-spacing:-.01em;color:var(--ink);line-height:1.3}.padi-ind .nm small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted-l);margin-top:4px}
.padi-ind .bars{display:grid;gap:6px}.padi-ind .bar{display:grid;grid-template-columns:62px 1fr 52px;align-items:center;gap:10px;font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted-l)}
.padi-ind .bar i{display:block;height:8px;background:rgba(30,31,43,.07);position:relative}.padi-ind .bar i b{position:absolute;left:0;top:0;bottom:0;background:var(--ink)}
.padi-ind .bar.bare i b{background:rgba(30,31,43,.32)}.padi-ind .bar em{font-style:normal;text-align:right;color:var(--ink);font-variant-numeric:tabular-nums;font-size:12px;letter-spacing:0}
.padi-ind li.off .bars{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l)}
.padi-tiles{display:grid;gap:0;border-top:1px solid var(--ink)}.padi-tiles div{padding:18px 0 22px;border-bottom:1px solid var(--rule-l)}
.padi-tiles b{display:block;font-weight:300;font-size:clamp(40px,4.6vw,64px);line-height:1;letter-spacing:-.04em;color:var(--ink);font-variant-numeric:tabular-nums}
.padi-tiles b span{font-size:.45em;letter-spacing:-.01em;color:var(--muted-l);margin-left:6px}
.padi-tiles p{margin:10px 0 0;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);line-height:1.55}
.padi-key{display:flex;gap:18px;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);margin:0 0 14px}
.padi-key span::before{content:"";display:inline-block;width:10px;height:8px;background:var(--ink);margin-right:7px}.padi-key span.bare::before{background:rgba(30,31,43,.32)}
.padi-frame{font-size:14px;line-height:1.6;color:var(--muted-l);max-width:62ch;margin:22px 0 0}
@media (max-width:820px){.padi-ind li{grid-template-columns:1fr}}
"""


def bars(i):
    if not i["measured"]:
        return '<div class="bars">Not yet measured</div>'
    return ('<div class="bars">' + "".join(f'<div class="bar{" bare" if k == "b" else ""}"><span>{lab}</span><i><b style="width:{i[k]}%"></b></i><em>{i[k]:.1f}%</em></div>'
                                          for k, lab in (("p", "Praxis"), ("b", "Bare"))) + "</div>")


def industry_list(j):
    rows = "".join(f'<li class="{"" if i["measured"] else "off"}"><div class="nm">{E(i["label"])}<small>'
                   + (f'Cycle{"s" if len(i["cycles"]) > 1 else ""} {", ".join(map(str, i["cycles"]))} · {i["checks"]} checks' if i["measured"] else f'{i["tasks_total"]} tasks in the bank')
                   + f'</small></div>{bars(i)}</li>' for i in j["industries"])
    return f'<div class="padi-key"><span>Praxis platform</span><span class="bare">Bare model</span></div><ul class="padi-ind">{rows}</ul>'


def tiles(j, rel=""):
    L, C, B = j["latest"], j["cumulative"], j["benchmark"]
    return (f'<div class="padi-tiles"><div><b>{L["platform_pct"]:.1f}%<span>vs {L["bare_pct"]:.1f}%</span></b><p>Cycle {L["cycle"]}: Praxis platform vs bare model, checks passed</p></div>'
            f'<div><b>{C["platform_pct"]:.1f}%<span>vs {C["bare_pct"]:.1f}%</span></b><p>All {len(C["cycles"])} cycles, {C["checks_total"]} checks per arm</p></div>'
            f'<div><b>{B["sectors_measured"]}<span>of {B["sector_count"]}</span></b><p>Industries measured, in the United States, Saudi Arabia and Pakistan</p></div></div>')


def home_block():
    """The home page section, Mercor style: name, one line, the numbers, every industry."""
    j = load()
    if not j:
        return "", ""
    body = (f'<section id="padi" class="light alt"><div class="wrap"><div class="head"><div><p class="mono">Benchmark · PADI</p><h2>{NAME}</h2></div>'
            f'<p class="serif">{E(SHORT)}</p></div>'
            f'<div class="split" style="margin-top:56px"><div>{tiles(j)}<p class="padi-frame">{E(FRAMING)}</p>'
            f'<div class="cta"><a class="btn solid" href="padi/">Explore the index</a><a class="btn" href="padi/#method">Methodology</a></div></div>'
            f'<div><p class="mono" style="margin:0 0 14px">Checks passed by industry · all cycles</p>{industry_list(j)}</div></div></div></section>')
    return body, CSS


# ---------------------------------------------------------------- the page
PCSS = """
body{background:var(--paper)}html.js header.top:not(.solid):not(.open){background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d)}
.ph{background:var(--night);color:var(--on-dark);padding:148px var(--gutter) 88px}.wrap{max-width:var(--max);margin:0 auto}.ph .in{max-width:calc(var(--max) - 2 * var(--gutter));margin:0 auto}
.ph h1{font-size:clamp(44px,6.4vw,96px);max-width:16ch}.ph .lede{max-width:64ch}
.ph .t3{display:grid;grid-template-columns:repeat(3,1fr);gap:0 32px;margin-top:64px}.ph .t3 div{border-top:1px solid rgba(242,242,240,.5);padding-top:18px}
.ph .t3 b{display:block;font-weight:300;font-size:clamp(48px,6vw,92px);line-height:.95;letter-spacing:-.045em;font-variant-numeric:tabular-nums}.ph .t3 b span{font-size:.4em;color:var(--muted-d);margin-left:8px;letter-spacing:-.01em}
.ph .t3 p{margin:14px 0 0;font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-d);max-width:30ch;line-height:1.55}
.ph .fr{margin:40px 0 0;max-width:70ch;color:var(--muted-d);font-size:15px;line-height:1.6}.ph .cta{margin-top:28px}
.wrap{padding:112px var(--gutter)}.head{display:grid;grid-template-columns:1fr 1fr;gap:24px 64px;align-items:end;padding-bottom:40px;margin-bottom:40px;border-bottom:1px solid var(--rule-l)}
.head h2{margin:0}.head p{margin:0;color:var(--muted-l);font-size:16.5px;line-height:1.6;max-width:56ch}
.split{display:grid;grid-template-columns:1fr 1fr;gap:48px 64px;align-items:start}
.chart .sc{overflow-x:auto;-webkit-overflow-scrolling:touch}.chart svg{width:100%;min-width:680px;height:auto;display:block}.chart .note{font-size:14px;color:var(--muted-l);margin:14px 0 0}
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 24px}.tabs[hidden]{display:none}.tabs button{font:400 13px/1 var(--sans);padding:10px 14px;border:1px solid var(--rule-l);border-radius:0;background:transparent;color:var(--ink);cursor:pointer}
.tabs button[aria-selected="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.panel h3{font-weight:400;font-size:20px;letter-spacing:-.015em;margin:32px 0 6px;color:var(--ink)}html.js .panel h3{display:none}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{width:100%;border-collapse:collapse;font-size:14.5px;line-height:1.5;color:var(--ink)}th,td{text-align:left;padding:12px 16px 12px 0;border-bottom:1px solid var(--rule-l);vertical-align:top;white-space:nowrap}
th{font-family:var(--mono);font-weight:400;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);border-bottom:1px solid var(--ink)}td.n{font-variant-numeric:tabular-nums}
td .v{color:var(--muted-l)}tr.sum td{border-top:1px solid var(--ink);font-weight:500}
.grid td{white-space:normal}.cell{display:flex;flex-wrap:wrap;gap:6px}.cell span{font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;padding:5px 8px;border:1px solid var(--rule-l);color:var(--muted-l);white-space:nowrap}
.cell span.m{background:var(--ink);color:var(--paper);border-color:var(--ink)}.cell span.h{background:repeating-linear-gradient(135deg,rgba(30,31,43,.06) 0 4px,transparent 4px 8px)}
.legend{display:flex;flex-wrap:wrap;gap:10px 20px;margin:0 0 20px}.legend .cell span{font-size:10px}
.task{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}.task>div{border-top:1px solid var(--ink);padding-top:16px}.task h3{font-weight:400;font-size:22px;letter-spacing:-.02em;margin:0 0 10px;color:var(--ink)}
.task p,.task li{font-size:15px;line-height:1.6;color:var(--muted-l)}.task ol{margin:0;padding-left:20px}.task .ex{border-left:2px solid var(--ink);padding:2px 0 2px 14px;margin:14px 0;color:var(--ink)}.task .ex b{display:block;font-family:var(--mono);font-weight:400;font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);margin-bottom:4px}
.mcards{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 32px}.mcard{border-top:1px solid var(--ink);padding-top:16px}.mcard .mono{margin:0 0 8px}.mcard h3{font-weight:400;font-size:22px;letter-spacing:-.02em;margin:0 0 10px;color:var(--ink)}
.mcard p{margin:0 0 10px;font-size:15px;line-height:1.6;color:var(--muted-l)}.mcard code{font-family:var(--mono);font-size:13px;background:rgba(30,31,43,.06);padding:1px 5px;color:var(--ink)}
.lim{list-style:none;padding:0;margin:0;border-top:1px solid var(--ink);columns:2;column-gap:64px}.lim li{break-inside:avoid;padding:16px 0;border-bottom:1px solid var(--rule-l);font-size:15.5px;line-height:1.6;color:var(--muted-l)}.lim li b{color:var(--ink);font-weight:400}
.faq details{border-top:1px solid var(--rule-l);padding:18px 0}.faq details:last-child{border-bottom:1px solid var(--rule-l)}.faq summary{cursor:pointer;font-size:19px;letter-spacing:-.012em;color:var(--ink);list-style:none}.faq summary::-webkit-details-marker{display:none}.faq summary::after{content:"+";float:right;color:var(--muted-l)}.faq details[open] summary::after{content:"\\2212"}.faq p{margin:12px 0 0;color:var(--muted-l);font-size:16px;line-height:1.6;max-width:62ch}
.cad{font-family:var(--serif);font-weight:300;font-size:clamp(21px,2.2vw,28px);line-height:1.4;color:var(--ink);max-width:40ch;margin:0}
@media (max-width:1000px){.mcards,.task{grid-template-columns:1fr 1fr}}
@media (max-width:820px){.ph{padding:112px var(--gutter) 64px}.ph .t3{grid-template-columns:1fr;gap:28px}.wrap{padding:80px var(--gutter)}.head,.split,.mcards,.task{grid-template-columns:1fr}.lim{columns:1}}
"""

TABS = """<script>(function(){var t=document.querySelector('.tabs');if(!t)return;var ps=document.querySelectorAll('.panel');t.hidden=false;
function show(id){t.querySelectorAll('button').forEach(function(b){b.setAttribute('aria-selected',b.dataset.p===id?'true':'false')});ps.forEach(function(p){p.hidden=p.id!==id})}
t.addEventListener('click',function(e){var b=e.target.closest('button');if(b)show(b.dataset.p)});show(ps[0].id)})();</script>"""


def chart(j):
    cs = j["cycles"]; W, H, l, r, t, b = 1200, 400, 64, 64, 34, 46
    x = lambda i: l + (W - l - r) * (i / max(1, len(cs) - 1))
    y = lambda v: t + (H - t - b) * (1 - v / 100)
    g = "".join(f'<line x1="{l}" x2="{W - r}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="rgba(30,31,43,.10)"/><text x="{l - 10}" y="{y(v) + 4:.1f}" text-anchor="end" class="ax">{v}%</text>' for v in (0, 25, 50, 75))
    goal = f'<line x1="{l}" x2="{W - r}" y1="{y(100)}" y2="{y(100)}" stroke="#1E1F2B" stroke-dasharray="5 5"/><text x="{l - 10}" y="{y(100) + 4}" text-anchor="end" class="ax">100%</text><text x="{W - r}" y="{y(100) - 9}" text-anchor="end" class="gl">Goal: every check</text>'
    xs = "".join(f'<text x="{x(i):.1f}" y="{H - 14}" text-anchor="middle" class="ax">Cycle {c["cycle"]}</text>' for i, c in enumerate(cs))

    # label each point above for the higher arm and below for the lower one, so the two never collide
    def pline(k, other, col):
        pts = " ".join(f"{x(i):.1f},{y(c[k]):.1f}" for i, c in enumerate(cs))
        dots = "".join(f'<circle cx="{x(i):.1f}" cy="{y(c[k]):.1f}" r="4" fill="{col}"/><text x="{x(i):.1f}" y="{y(c[k]) + (-12 if c[k] >= c[other] else 22):.1f}" text-anchor="middle" class="vl" fill="{col}">{c[k]:.1f}%</text>' for i, c in enumerate(cs))
        return f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2"/>{dots}'
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Checks passed per cycle, Praxis platform against the bare model, on a scale to 100 percent">'
           '<style>.ax{font:400 11px "Geist Mono",monospace;fill:#666874;letter-spacing:.04em}.gl{font:400 11px "Geist Mono",monospace;fill:#1E1F2B;letter-spacing:.04em;text-transform:uppercase}.vl{font:500 12px "Inter Tight",sans-serif}</style>'
           f'{g}{goal}{xs}{pline("bare_pct", "platform_pct", "#9A9BA3")}{pline("platform_pct", "bare_pct", "#1E1F2B")}</svg>')
    return (f'<div class="chart"><div class="padi-key"><span>Praxis platform</span><span class="bare">Bare model</span></div><div class="sc">{svg}</div>'
            '<p class="note">Different tasks each cycle, five or six tasks per cycle, so cycles are not like for like.</p></div>')


def tables(j):
    cs = j["cycles"]; C = j["cumulative"]
    f = lambda a, b: f'{pct(a, b):.1f}%'
    pb = lambda d: f'{pct(d["platform"], d["of"]):.1f}% <span class="v">vs {pct(d["bare"], d["of"]):.1f}%</span>'
    rows = "".join(f'<tr><td>Cycle {c["cycle"]}</td><td>{datetime.date.fromisoformat(c["date"]).strftime("%-d %b %Y")}</td><td class="n">{c["tasks"]}</td><td class="n">{c["checks_total"]}</td>'
                   f'<td class="n">{c["platform_pct"]:.1f}%</td><td class="n">{c["bare_pct"]:.1f}%</td>'
                   f'<td class="n">{c.get("platform_ahead_on_tasks", 0)} · {c.get("platform_tied_on_tasks", 0)} · {c.get("platform_behind_on_tasks", 0)}</td><td>{E(c["rubric_version"])}</td></tr>' for c in cs)
    tot = [sum(c.get(k, 0) for c in cs) for k in ("tasks", "platform_ahead_on_tasks", "platform_tied_on_tasks", "platform_behind_on_tasks")]
    rows += (f'<tr class="sum"><td>All cycles</td><td></td><td class="n">{tot[0]}</td><td class="n">{C["checks_total"]}</td><td class="n">{C["platform_pct"]:.1f}%</td><td class="n">{C["bare_pct"]:.1f}%</td>'
             f'<td class="n">{tot[1]} · {tot[2]} · {tot[3]}</td><td></td></tr>')
    t1 = ('<div class="tw"><table><thead><tr><th>Cycle</th><th>Date</th><th>Tasks</th><th>Checks per arm</th><th>Praxis platform</th><th>Bare model</th><th>Tasks: platform ahead · tied · behind</th><th>Rubric</th></tr></thead>'
          f'<tbody>{rows}</tbody></table></div>')
    fam = [x["id"] for x in j["methodology"]["families"]]; flab = {x["id"]: x["label"] for x in j["methodology"]["families"]}
    t2 = ('<div class="tw"><table><thead><tr><th>Cycle</th>' + "".join(f'<th>{E(flab[k])}: Praxis vs bare</th>' for k in fam) + '</tr></thead><tbody>'
          + "".join(f'<tr><td>Cycle {c["cycle"]}</td>' + "".join(f'<td class="n">{pb(c["by_family"][k])}</td>' for k in fam) + '</tr>' for c in cs) + '</tbody></table></div>')
    cn = j["benchmark"]["countries"]
    t3 = ('<div class="tw"><table><thead><tr><th>Cycle</th>' + "".join(f'<th>{E(k)}: Praxis vs bare</th>' for k in cn) + '</tr></thead><tbody>'
          + "".join(f'<tr><td>Cycle {c["cycle"]}</td>' + "".join(f'<td class="n">{pb(c["by_country"][k]) if k in c["by_country"] else ""}</td>' for k in cn) + '</tr>' for c in cs) + '</tbody></table></div>')
    lab = {s["id"]: s["label"] for s in j["sectors"]}
    t4 = ('<div class="tw"><table><thead><tr><th>Industry</th><th>Cycle</th><th>Checks per arm</th><th>Praxis platform</th><th>Bare model</th></tr></thead><tbody>'
          + "".join(f'<tr><td>{E(lab.get(s, s))}</td><td>Cycle {c["cycle"]}</td><td class="n">{v["of"]}</td><td class="n">{f(v["platform"], v["of"])}</td><td class="n">{f(v["bare"], v["of"])}</td></tr>'
                    for s in sorted(lab, key=lambda k: lab[k]) for c in cs for k2, v in c["by_sector"].items() if k2 == s)
          + '</tbody></table></div>')
    panes = [("p-cycle", "By cycle", t1), ("p-ind", "By industry", t4), ("p-fam", "By check family", t2), ("p-cty", "By country", t3)]
    return ('<div class="tabs" role="tablist" hidden>' + "".join(f'<button type="button" role="tab" data-p="{i}">{E(n)}</button>' for i, n, _ in panes) + '</div>'
            + "".join(f'<div class="panel" id="{i}" role="tabpanel"><h3>{E(n)}</h3>{t}</div>' for i, n, t in panes))


def coverage(j):
    def cell(c):
        s = c["status"]
        if s == "measured":
            return f'<span class="m">Cycle {c["cycle"]}</span>'
        if s == "held_out":
            return '<span class="h">Held out</span>'
        return '<span>Not run</span>'
    cn = j["benchmark"]["countries"]
    rows = "".join(f'<tr><td>{E(s["label"])}</td>' + "".join(f'<td><div class="cell">{"".join(cell(c) for c in s["grid"][k]["cells"])}</div></td>' for k in cn) + '</tr>'
                   for s in sorted(j["sectors"], key=lambda x: x["label"]))
    return ('<div class="legend"><div class="cell"><span class="m">Cycle 16</span></div><span class="mono">measured in that cycle</span>'
            '<div class="cell"><span class="h">Held out</span></div><span class="mono">kept for a final blind evaluation</span>'
            '<div class="cell"><span>Not run</span></div><span class="mono">in the bank, not yet measured</span></div>'
            f'<div class="tw grid"><table><thead><tr><th>Industry</th>' + "".join(f'<th>{E(k)}</th>' for k in cn) + f'</tr></thead><tbody>{rows}</tbody></table></div>')


def behind(j):
    lo = [str(c["cycle"]) for c in j["cycles"] if c["bare_pct"] > c["platform_pct"]]
    if not lo:
        return ""
    return f' The bare model scored higher in cycle{"s" if len(lo) > 1 else ""} {", ".join(lo[:-1]) + " and " + lo[-1] if len(lo) > 1 else lo[0]}.'


def page(j):
    B, L, M = j["benchmark"], j["latest"], j["methodology"]
    fams = M["families"]; bank = B["checks_by_family_in_bank"]
    running = f" Cycle {RUNNING} is under way." if RUNNING and RUNNING > L["cycle"] else ""
    asof = datetime.date.fromisoformat(L["date"]).strftime("%-d %B %Y")
    task = (f'<div class="task"><div><p class="mono">1 · The requirement</p><h3>A short pack</h3><p>What a customer would send for one operation: at most two pages, anonymised, '
            'for a site in the United States, Saudi Arabia or Pakistan. Packs leave out facts a good design should ask for.</p></div>'
            '<div><p class="mono">2 · The design</p><h3>Ten headings</h3><p>Both arms get the same pack and the same instruction: produce the first design a customer will argue with, under ten fixed headings.</p>'
            f'<ol>{"".join(f"<li>{E(h)}</li>" for h in HEADINGS)}</ol></div>'
            f'<div><p class="mono">3 · The checks</p><h3>Yes or no</h3><p>{M["checks_per_task"]["min"]} to {M["checks_per_task"]["max"]} checks per task in three families. Illustrative examples, not taken from any task:</p>'
            + "".join(f'<p class="ex"><b>{E(f["label"])}</b>{E(f["example"])}</p>' for f in fams) + '</div></div>')
    arms = "".join(f'<p><strong>{E(a["label"])}</strong> · <code>{E(a["model"])}</code><br>{E(a["description"] if a["id"] == "bare" else "The same model inside the Praxis planner, with its sourced corpus of rules and reference designs and its own quality gate.")}</p>' for a in M["arms"])
    J = M["judge"]
    mc = [("Arms", "Same model, twice", arms),
          ("Judge", "Three lenses", f'<p><code>{E(J["model"])}</code> reads each design and answers every check yes or no through three lenses: {E(", ".join(J["lenses"][:-1]))} and {E(J["lenses"][-1])}.</p><p>A check passes when the majority of the lenses say yes.</p>'),
          ("Families", "Name, flag, never", "".join(f'<p><strong>{E(f["label"])}</strong> · {pct(bank[f["id"]], B["checks_in_bank"]):.0f}% of the bank<br>{E(f["what"])}</p>' for f in fams)),
          ("Fresh tasks", "Never run twice", f'<p>A third of the bank ({B["tasks_held_out"]} of {B["task_bank_size"]} tasks) is held out for a final blind evaluation and never run in a cycle.</p><p>Each cycle picks up to six unused tasks from the rest, two per country where the pool allows. No task or check ever enters the platform\'s corpus or briefs.</p>'),
          ("Score", "Checks passed", '<p>Checks passed divided by checks total, for each arm. No partial credit and no weighting.</p><p>Industry, family and country figures are the same count over their subset. Cycles use different tasks, so compare percentages, not counts.</p>'),
          ("Rubric", "Version 0.2", '<p>Version 0.1 judged cycle 12. Version 0.2 (4 October 2026) judges cycles 13 onward: an open weight model named for self hosting, or a product named with its licence, is not a part number.</p>')]
    mcards = "".join(f'<div class="mcard"><p class="mono">{E(a)}</p><h3>{E(b)}</h3>{c}</div>' for a, b, c in mc)
    lims = "".join(f'<li><b>{E(a)}</b> {E(b)}</li>' for a, b in LIMITS)
    faq = "".join(f'<details{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(FAQ))
    return f"""<section class="ph"><div class="in"><p class="eyebrow">Benchmark · PADI</p><h1>{NAME}</h1><p class="lede">{E(ONE_LINE)}</p>
<div class="t3"><div><b>{L["platform_pct"]:.1f}%<span>vs {L["bare_pct"]:.1f}%</span></b><p>Cycle {L["cycle"]}: Praxis platform vs bare model, checks passed</p></div>
<div><b>{B["sectors_measured"]}<span>of {B["sector_count"]}</span></b><p>Industries measured across three countries</p></div>
<div><b>{j["cumulative"]["checks_total"]}</b><p>Checks judged per arm across {len(j["cycles"])} cycles</p></div></div>
<p class="fr">{E(FRAMING)}</p><div class="cta"><a class="btn" href="#industries">By industry</a><a class="btn" href="#method">Methodology</a><a class="btn" href="#limits">Limitations</a></div></div></section>
<section class="light" id="industries"><div class="wrap"><div class="head"><h2>Industries</h2><p>Checks passed in each industry, all cycles to date, for the Praxis platform and the bare model on the same tasks. Three industries are in the bank and not yet measured.</p></div>{industry_list(j)}</div></section>
<section class="light alt" id="trajectory"><div class="wrap"><div class="head"><h2>Trajectory</h2><p>Every cycle on a scale to 100%, so the distance to the goal stays in view.{behind(j)}</p></div>{chart(j)}</div></section>
<section class="light" id="results"><div class="wrap"><div class="head"><h2>Results</h2><p>Every figure is checks passed as a percentage of checks judged, for each arm.</p></div>{tables(j)}</div></section>
<section class="light alt" id="coverage"><div class="wrap"><div class="head"><h2>Coverage</h2><p>{B["sectors_measured"]} of {B["sector_count"]} industries measured. {B["task_bank_size"]} tasks in the bank, at least one per industry in each country, because the binding rules change with the place.</p></div>{coverage(j)}</div></section>
<section class="light" id="task"><div class="wrap"><div class="head"><h2>A task</h2><p>What one task looks like, described generically. Task text, packs and checks are never published, so the held out set stays clean.</p></div>{task}</div></section>
<section class="light alt" id="method"><div class="wrap"><div class="head"><h2>Methodology</h2><p>Both arms run the same model on the same pack, so the difference between them is the platform, not the model.</p></div><div class="mcards">{mcards}</div></div></section>
<section class="light" id="limits"><div class="wrap"><div class="head"><h2>Limitations</h2><p>What PADI is good for: seeing whether Praxis improves on design judgement from one release to the next, on tasks it has never seen, and where it still misses. What it is not:</p></div><ul class="lim">{lims}</ul></div></section>
<section class="light alt" id="faq"><div class="wrap"><div class="split"><div><h2>Questions</h2></div><div class="faq">{faq}</div></div></div></section>
<section class="light" id="cadence"><div class="wrap"><div class="split"><div><p class="mono">Cadence</p><p class="cad">Updated each Praxis release cycle. Last published: cycle {L["cycle"]}, {asof}.{running}</p></div>
<div><p class="mono">Contact</p><p class="cad" style="font-size:20px">Questions about PADI, or a task from your own operation you would like measured: <a href="mailto:{brand.INBOX}?subject=PADI">{brand.INBOX}</a></p></div></div></div></section>"""


def markdown(j):
    B, L, C = j["benchmark"], j["latest"], j["cumulative"]
    out = [f"# {NAME} (PADI)", "", f"Canonical: {BASE}/padi/", "Publisher: CodeNinja Atoms (https://codeatoms.ai)", "", ONE_LINE, "", FRAMING, "",
           f"Latest cycle {L['cycle']} ({L['date']}): Praxis platform {L['platform_pct']:.1f}%, bare model {L['bare_pct']:.1f}% of checks passed.",
           f"All {len(C['cycles'])} cycles: Praxis platform {C['platform_pct']:.1f}%, bare model {C['bare_pct']:.1f}% over {C['checks_total']} checks per arm.",
           f"Industries measured: {B['sectors_measured']} of {B['sector_count']}.", "", "## Industries", "",
           "| Industry | Praxis platform | Bare model | Cycles |", "|---|---|---|---|"]
    out += [f"| {i['label']} | {i['p']:.1f}% | {i['b']:.1f}% | {', '.join(map(str, i['cycles']))} |" if i["measured"] else f"| {i['label']} | not yet measured | not yet measured | |" for i in j["industries"]]
    out += ["", "## Results by cycle", "", "| Cycle | Date | Tasks | Praxis platform | Bare model | Rubric |", "|---|---|---|---|---|---|"]
    out += [f"| {c['cycle']} | {c['date']} | {c['tasks']} | {c['platform_pct']:.1f}% | {c['bare_pct']:.1f}% | {c['rubric_version']} |" for c in j["cycles"]]
    out += ["", "Different tasks each cycle, so cycles are not like for like.", "", "## Methodology", "",
            f"- Arms: the bare model and the same model inside Praxis, both {j['methodology']['arms'][0]['model']}, on the same pack and instruction.",
            f"- Judge: {j['methodology']['judge']['model']} through three lenses ({', '.join(j['methodology']['judge']['lenses'])}); a check passes on a majority yes.",
            "- Families: must name, must flag, must never.",
            f"- Fresh tasks: {B['tasks_held_out']} of {B['task_bank_size']} tasks held out for a final blind evaluation; no task is run twice.",
            "- Score: checks passed divided by checks total, per arm, no partial credit.", "", "## Limitations", ""]
    out += [f"- **{a}** {b}" for a, b in LIMITS]
    out += ["", "## Questions", ""] + [x for q, a in FAQ for x in (f"### {q}", "", a, "")]
    out += [f"Updated each Praxis release cycle. Last published: cycle {L['cycle']}, {L['date']}." + (f" Cycle {RUNNING} is under way." if RUNNING and RUNNING > L["cycle"] else "")]
    return "\n".join(out) + "\n"


def nav():
    return [("Research", f"{BASE}/#research"), ("Sectors", f"{BASE}/sectors/"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"),
            ("PADI", f"{BASE}/padi/"), ("Developers", f"{BASE}/developer/"), ("Blog", f"{BASE}/blog/"), ("About", f"{BASE}/about/")]


def main():
    j = load()
    if not j:
        print("padi: no export at", SRC, "(page left as it is)"); return
    L = j["latest"]
    title = f"{NAME} (PADI) | CodeNinja Atoms"
    desc = (f"PADI scores physical AI designs across 13 industries in the United States, Saudi Arabia and Pakistan. Cycle {L['cycle']}: "
            f"Praxis platform {L['platform_pct']:.1f}% vs bare model {L['bare_pct']:.1f}% of checks passed.")
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": f"{NAME} (PADI)", "url": f"{BASE}/padi/", "description": desc,
           "dateModified": L["date"], "isPartOf": {"@id": f"{BASE}/#website"}, "publisher": {"@id": f"{BASE}/#org"},
           "about": [{"@type": "Thing", "name": "physical AI"}, {"@type": "Thing", "name": "AI benchmark"}, {"@type": "SoftwareApplication", "name": "Praxis", "url": f"{BASE}/praxis/"}]},
          {"@context": "https://schema.org", "@type": "FAQPage", "url": f"{BASE}/padi/", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/padi/">
<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/padi/">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld) + f"""{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}{PCSS}</style></head>
<body>{brand.header(BASE + "/", nav(), access=brand.SIGNUP)}
<main>{page(j)}</main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}{TABS}</body></html>"""
    out = ROOT / "padi"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(doc, encoding="utf-8")
    (out / "index.md").write_text(markdown(j), encoding="utf-8")
    print(f"padi/: cycle {L['cycle']}, {sum(1 for i in j['industries'] if i['measured'])} of {len(j['industries'])} industries measured")


if __name__ == "__main__":
    main()
