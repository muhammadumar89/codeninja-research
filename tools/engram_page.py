"""Hyper Engram: /hyper-engram/, the agentic memory of the Hyper stack, told the way a research lab would.

Umar, 19 Nov 2026: a training lab's platform page (same day, second ruling: never say we do not train weights;
we train both, context first in this loop, and the first question with a customer is what goes in context and what in weights), in our design system, that tells the world how we train
systems by compression and reinflation without changing weights. Sources: the memo Compression and Reinflation
(10 Oct 2026) and The Recursive Learning Loop (internal). Public rules kept here:
  - results are public, the PADI scoring method never is (numbers come from padi.load(), the same export /padi/ uses)
  - no counts from Engram, never the word "rows", no prompts, judges' rubrics or thresholds
  - no internal names (no coding agent product, no schedules, no collection names), no customer named
  - never "frozen weights", "no weight updates" or "we do not fine tune" on this page
  - "RSI Loop", never "cycle"; no hyphens or dashes in prose; never name another company's product
    python tools/product_pages.py     # writes hyper-engram/index.html with the other product pages
"""
import random
import brand
from ontology_page import BASE, E, MARK, CSS as OCSS, TYPE_JS, shell, sx, head

URL = f"{BASE}/hyper-engram/"
MEMO = f"{BASE}/memos/compression-and-reinflation/"


def bowtie_svg():
    """The hero: experience pours in from the left, is compressed at the waist into one versioned principle,
    and is reinflated on the right into designs for places the memory never saw."""
    r = random.Random(7)
    W, H, wx, wy = 1600, 900, 800, 400
    srcs = [("RUNS", 230), ("CORRECTIONS", 340), ("BENCHMARK MISSES", 450), ("REAL REQUIREMENTS", 560), ("FIELD LEARNINGS", 670)]
    tgts = [("A mine", "Chile", 160), ("A contact centre", "Pakistan", 290), ("A hospital", "Ontario", 420), ("A port", "Saudi Arabia", 550)]
    o = [f'<svg class="bow" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">',
         '<defs><radialGradient id="bwg"><stop offset="0" stop-color="#ffd166" stop-opacity=".55"/><stop offset=".4" stop-color="#5b2bff" stop-opacity=".35"/><stop offset="1" stop-color="#5b2bff" stop-opacity="0"/></radialGradient>'
         '<linearGradient id="bwf" x1="0" x2="1"><stop offset="0" stop-color="#a48fff" stop-opacity=".02"/><stop offset=".5" stop-color="#a48fff" stop-opacity=".16"/><stop offset="1" stop-color="#a48fff" stop-opacity=".02"/></linearGradient></defs>']
    # the bowtie silhouette
    o.append(f'<path class="sil" d="M40,70 C430,80 640,{wy - 40} {wx - 26},{wy - 8} L{wx + 26},{wy - 8} C960,{wy - 40} 1170,80 1560,70 L1560,750 C1170,740 960,{wy + 40} {wx + 26},{wy + 8} L{wx - 26},{wy + 8} C640,{wy + 40} 430,740 40,750 Z"/>')
    for x in range(80, 1560, 80):
        o.append(f'<line class="tick" x1="{x}" y1="808" x2="{x}" y2="816"/>')
    left, right = [], []
    for i in range(54):
        x, y = r.uniform(40, 520), r.uniform(90, 730)
        d = f"M{x:.0f},{y:.0f} C{x + 260:.0f},{y:.0f} {wx - 150},{wy} {wx},{wy}"
        left.append(d)
        o.append(f'<path class="fib" d="{d}"/>')
    for i in range(36):
        _, _, ty = tgts[i % 4]
        tx, ty = 1330 + r.uniform(-30, 10), ty + r.uniform(-34, 34)
        d = f"M{wx},{wy} C{wx + 150},{wy} {tx - 280:.0f},{ty:.0f} {tx:.0f},{ty:.0f}"
        right.append(d)
        o.append(f'<path class="fib r" d="{d}"/>')
    for i, d in enumerate(left):
        o.append(f'<circle class="pt" r="{r.choice([1.6, 2, 2.6])}"><animateMotion dur="{r.uniform(5, 8):.1f}s" begin="-{r.uniform(0, 8):.1f}s" repeatCount="indefinite" path="{d}" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".5 0 .9 .6"/></circle>')
    for i, d in enumerate(right):
        o.append(f'<circle class="pt r" r="{r.choice([1.8, 2.4])}"><animateMotion dur="{r.uniform(4, 6.5):.1f}s" begin="-{r.uniform(0, 6):.1f}s" repeatCount="indefinite" path="{d}" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".1 .4 .5 1"/></circle>')
    for lab, y in srcs:
        o.append(f'<text class="lb" x="64" y="{y - 52}">{lab}</text>')
    o.append(f'<circle cx="{wx}" cy="{wy}" r="120" fill="url(#bwg)" class="halo"/>')
    o.append(f'<g class="waist" transform="translate({wx},{wy})"><rect x="-74" y="-24" width="148" height="48" rx="2"/><text class="w1" y="-3" text-anchor="middle">BRIEF · ROUTING</text><text class="w2" y="14" text-anchor="middle">v7 · supersedes v6</text></g>')
    o.append(f'<text class="hd" x="{wx - 230}" y="{wy - 150}" text-anchor="middle">COMPRESS</text><text class="hd" x="{wx + 230}" y="{wy - 150}" text-anchor="middle">REINFLATE</text>')
    o.append(f'<text class="sub" x="{wx - 230}" y="{wy - 130}" text-anchor="middle">many observations, one principle</text><text class="sub" x="{wx + 230}" y="{wy - 130}" text-anchor="middle">one principle, a new design each time</text>')
    for a, b, y in tgts:
        o.append(f'<g class="tg" transform="translate(1350,{y})"><circle r="5"/><text x="16" y="-2">{a}</text><text class="c" x="16" y="15">{b.upper()}</text></g>')
    o.append(f'<g class="lock" transform="translate({wx},{wy + 92})"><rect x="-96" y="-15" width="192" height="30" rx="15"/><text y="5" text-anchor="middle">THE TRAINING SIGNAL</text></g>')
    o.append('</svg>')
    return "".join(o)


def loop_svg():
    """The recursive learning loop as a drawing: one master agent, two daily routines, the planner and the
    benchmark, who never speak to each other directly. They speak through Engram."""
    N = {"m": (190, 120, "Master agent", "runs each RSI Loop, changes the code"),
         "d": (1010, 120, "Distillation routine", "every morning: learnings into briefs"),
         "r": (1010, 500, "Corpus routine", "every morning: measures, lands entries"),
         "p": (600, 560, "Planner", "reads memory the moment it reasons"),
         "b": (190, 500, "Benchmark and premortem", "fresh tasks and blind sets")}
    E_ = [("m", "e", "M308,125 C420,130 480,200 522,258", "gap records, asks, demand"),
          ("e", "d", "M680,262 C760,200 820,120 888,115", "newest episode, open asks"),
          ("d", "e", "M892,140 C820,160 740,250 684,298", "versioned briefs"),
          ("e", "r", "M680,330 C760,360 830,480 888,490", "feedback, open asks"),
          ("r", "e", "M892,515 C800,515 720,430 676,368", "verified entries"),
          ("e", "p", "M582,386 L582,526", "memory, mirrored"),
          ("p", "e", "M618,528 L618,388", "plans, unmet asks"),
          ("m", "b", "M150,152 L150,466", "measures"),
          ("b", "m", "M230,468 L230,154", "misses"),
          ("m", "p", "M72,124 C18,170 18,602 120,602 L478,570", "code, tests, deploys")]
    o = ['<svg class="loop" viewBox="0 0 1200 640" role="img" aria-label="The recursive learning loop: a master agent, two daily routines, the planner and the benchmark, all reading and writing through Engram">',
         '<defs><marker id="la" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0 L8,4 L0,8 z"/></marker></defs>']
    for k, (a, b, d, lab) in enumerate(E_):
        o.append(f'<path id="le{k}" class="le" d="{d}" marker-end="url(#la)"/>')
    for k, (a, b, d, lab) in enumerate(E_):
        o.append(f'<circle class="lp" r="3.6"><animateMotion dur="{3.2 + (k % 4) * .5:.1f}s" begin="-{k * .7:.1f}s" repeatCount="indefinite"><mpath href="#le{k}"/></animateMotion></circle>')
    lp = {0: (440, 160, "middle"), 1: (770, 150, "end"), 2: (800, 236, "start"), 3: (812, 404, "start"), 4: (880, 556, "end"), 5: (570, 450, "end"), 6: (632, 500, "start"), 7: (138, 312, "end"), 8: (242, 312, "start"), 9: (300, 624, "middle")}
    for k, (a, b, d, lab) in enumerate(E_):
        x, y, an = lp[k]
        o.append(f'<text class="el" x="{x}" y="{y}" text-anchor="{an}">{E(lab)}</text>')
    # Engram: a store of strata, not a box
    o.append('<g class="cyl" transform="translate(600,250)"><path class="cb" d="M-80,0 L-80,110 A80,22 0 0 0 80,110 L80,0"/><ellipse class="ct" cx="0" cy="0" rx="80" ry="22"/>')
    for i, s in enumerate(["episodes", "feedback", "gap records", "briefs", "corpus"]):
        y = 26 + i * 18
        o.append(f'<path class="st" d="M-80,{y} A80,22 0 0 0 80,{y}"/><text class="sl" x="0" y="{y + 14}" text-anchor="middle">{s}</text>')
    o.append('<text class="cn" x="0" y="-36" text-anchor="middle">ENGRAM</text></g>')
    for k, (x, y, t, s) in N.items():
        w = 236
        o.append(f'<g class="nd n{k}" transform="translate({x - w / 2:.0f},{y - 30})"><rect width="{w}" height="60"/><rect class="bar" width="4" height="60"/><text class="t" x="16" y="26">{E(t)}</text><text class="s" x="16" y="45">{E(s)}</text></g>')
    o.append('</svg>')
    return "".join(o)


def glyph(k):
    g = {"cap": '<rect x="6" y="8" width="52" height="10"/><rect x="6" y="22" width="52" height="10"/><rect class="v" x="6" y="36" width="52" height="10"/>',
         "cmp": '<path d="M4,6 L28,22 L28,30 L4,46 Z"/><path class="v" d="M36,22 L60,6 L60,46 L36,30 Z"/><circle class="vs" cx="32" cy="26" r="3"/>',
         "rei": '<rect x="6" y="6" width="24" height="18"/><path class="vs" d="M34,15 L44,15 M40,11 L44,15 L40,19"/><rect class="v" x="46" y="6" width="14" height="18"/><path d="M6,32 L58,32 M6,40 L44,40 M6,48 L36,48"/>',
         "rec": '<circle cx="32" cy="26" r="20"/><circle class="v" cx="32" cy="26" r="9"/><path class="vs" d="M32,2 L32,10 M32,42 L32,50 M8,26 L16,26 M48,26 L56,26"/>'}[k]
    return f'<svg class="gly" viewBox="0 0 64 52" aria-hidden="true">{g}</svg>'


LEARN = [("Benchmark miss", "A conveyor design sensed belt misalignment and never said who acts on it.", "k"),
         ("Engineer correction", "The alarm went to the control room, which cannot stop a haul truck. Route it to the pit supervisor.", "k"),
         ("Real requirement", "A tender asks for alerts to reach “the responsible officer” within a minute. Responsible for what?", "k"),
         ("Field learning", "Operators ignore an alert that arrives without a decision attached to it.", "k"),
         ("Benchmark miss", "A gas reading crossed its limit. The design logged it and paged no one.", "k"),
         ("Engineer correction", "Name the reading that starts the clock, not only the threshold.", "k"),
         ("Earlier note", "Send every alert to the shift manager.", "x"),
         ("Earlier note", "Make critical alerts red.", "f")]
PRINCIPLE = "Every sensed warning names three things: the role that can act in time, the reading that starts the clock, and the options of the decision."
PLACES = {"mine": ("A mine in Chile", [("Warning", "A haul truck and a person on foot inside the proximity zone"), ("Who acts", "The pit supervisor on shift, never only the control room"),
                                       ("Clock starts", "At the first proximity warning, not at the second"), ("Options", "Stop the truck · reroute it · send an escort")]),
          "call": ("A contact centre in Pakistan", [("Warning", "Callers waiting longer than the service level allows"), ("Who acts", "The floor supervisor on duty"),
                                                   ("Clock starts", "When the first caller passes the agreed wait"), ("Options", "Open overflow · offer a callback · move agents from outbound")]),
          "ward": ("A hospital in Ontario", [("Warning", "A ward patient's early warning score rising"), ("Who acts", "The charge nurse, then the rapid response team"),
                                            ("Clock starts", "At the second rising score inside the hour"), ("Options", "Reassess at the bedside · call rapid response · escalate to the physician")])}


def bench():
    cards = "".join(f'<li class="lc {c}" style="--i:{i}"><span>{E(s)}</span>{E(t)}</li>' for i, (s, t, c) in enumerate(LEARN))
    chips = "".join(f'<button type="button" class="pc" data-p="{k}">{E(v[0])}</button>' for k, v in PLACES.items())
    return (f'<div class="bench" id="bench"><div class="bl"><div class="bh"><b>Experience</b><span>8 learnings · 4 sources</span></div><ul class="lcs">{cards}</ul>'
            '<button type="button" class="go" id="bcmp">Compress →</button></div>'
            '<div class="bm"><div class="bh"><b>Brief</b><span id="bver">routing · v6</span></div><div class="pr" id="bpr"><p class="wait">Press Compress. Six learnings become one principle, one contradiction is resolved and one note fades because it never mattered.</p></div>'
            f'<div class="bh t2"><b>Reinflate into</b><span>the model reads it here</span></div><div class="pcs">{chips}</div></div>'
            '<div class="br"><div class="bh"><b>Design</b><span id="bplace">no place yet</span></div><dl class="out" id="bout"><dt>Waiting</dt><dd>Compress, then pick a place. The same principle becomes a different design in each one, because the world it lands in is different.</dd></dl></div></div>'
            '<p class="note">Illustrative. The principle is one the platform learned this way; the learnings and places are drawn for this page.</p>')


def chart(j):
    cy = j["cycles"]
    bl = j.get("blind")
    pts = [(c["cycle"], c["platform_pct"], c["bare_pct"]) for c in cy]
    W, H, l, rr, t, b = 960, 340, 54, 120, 20, 44
    n = len(pts) + (1 if bl else 0)
    X = lambda i: l + i * (W - l - rr) / (n - 1)
    Y = lambda v: t + (100 - v) / 100 * (H - t - b)
    o = [f'<svg class="tr" viewBox="0 0 {W} {H}" role="img" aria-label="PADI by RSI Loop: Praxis platform against frontier AI on its own">']
    for v in (0, 25, 50, 75, 100):
        o.append(f'<line class="g" x1="{l}" x2="{W - rr + 30}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/><text class="ax" x="{l - 10}" y="{Y(v) + 4:.1f}" text-anchor="end">{v}%</text>')
    for k, col in ((1, "p"), (2, "f")):
        d = " ".join(f'{"M" if i == 0 else "L"}{X(i):.1f},{Y(p[k]):.1f}' for i, p in enumerate(pts))
        o.append(f'<path class="ln {col}" d="{d}"/>')
        o.extend(f'<circle class="dt {col}" cx="{X(i):.1f}" cy="{Y(p[k]):.1f}" r="3.4"/>' for i, p in enumerate(pts))
    for i, p in enumerate(pts):
        o.append(f'<text class="ax" x="{X(i):.1f}" y="{H - 18}" text-anchor="middle">{p[0]}</text>')
    if bl:
        i = len(pts)
        x0 = (X(i - 1) + X(i)) / 2
        o.append(f'<line class="sep" x1="{x0:.1f}" x2="{x0:.1f}" y1="{t}" y2="{H - b}"/><text class="ax" x="{X(i):.1f}" y="{H - 18}" text-anchor="middle">{bl["cycle"]} blind</text>')
        for k, col, v in ((1, "p", bl["platform_pct"]), (2, "f", bl["bare_pct"])):
            o.append(f'<circle class="dt {col} big" cx="{X(i):.1f}" cy="{Y(v):.1f}" r="6"/><text class="vl {col}" x="{X(i) + 14:.1f}" y="{Y(v) + 5:.1f}">{v}%</text>')
    o.append(f'<text class="ax" x="{l}" y="{H - 2}">RSI LOOP</text></svg>')
    return "".join(o)


CSS = r"""
.eg{--amb:#ffd166}
.oh.eh{background:radial-gradient(38% 50% at 50% 44%,rgba(91,43,255,.26),rgba(18,11,28,0) 70%),#0d0815}
.oh .bow{position:absolute;left:0;top:0;width:100%;height:100%}
.bow .sil{fill:url(#bwf);stroke:rgba(200,185,255,.22);stroke-width:1}.bow .tick{stroke:rgba(200,185,255,.3)}
.bow .fib{fill:none;stroke:rgba(190,170,255,.07);stroke-width:1}.bow .fib.r{stroke:rgba(255,209,102,.08)}
.bow .pt{fill:#c8b9ff}.bow .pt.r{fill:#ffd166}
.bow .lb{font:500 10.5px var(--mono);letter-spacing:.16em;fill:rgba(225,215,255,.55)}
.bow .hd{font:500 12px var(--mono);letter-spacing:.3em;fill:#fff}.bow .sub{font:400 13px var(--sans);fill:rgba(255,255,255,.55)}
.bow .halo{animation:ehalo 4s ease-in-out infinite;transform-origin:800px 400px}
.bow .waist rect{fill:#0d0815;stroke:#ffd166;stroke-width:1.2}.bow .w1{font:600 11px var(--mono);letter-spacing:.14em;fill:#fff}.bow .w2{font:400 10px var(--mono);fill:#ffd166}
.bow .tg circle{fill:#ffd166}.bow .tg text{font:400 17px var(--sans);fill:#fff}.bow .tg text.c{font:500 10px var(--mono);letter-spacing:.14em;fill:rgba(255,255,255,.5)}
.bow .lock rect{fill:rgba(13,8,21,.8);stroke:rgba(255,255,255,.3)}.bow .lock text{font:500 10px var(--mono);letter-spacing:.16em;fill:rgba(255,255,255,.75)}
@keyframes ehalo{50%{opacity:.55;transform:scale(1.12)}}
/* the loop sheet */
.loop{width:100%;height:auto;display:block;min-width:820px}
.loop .le{fill:none;stroke:rgba(23,19,31,.32);stroke-width:1.3}.loop marker path{fill:rgba(23,19,31,.6)}.loop .lp{fill:var(--vi)}
.loop .el{font:400 11px var(--mono);fill:var(--mut)}
.loop .nd rect{fill:#fff;stroke:var(--ink);stroke-width:1.1}.loop .nd .bar{fill:var(--vi);stroke:none}.loop .nd .t{font:600 15px var(--sans);fill:var(--ink)}.loop .nd .s{font:400 12px var(--sans);fill:var(--mut)}
.loop .nb .bar,.loop .nm .bar{fill:var(--ink)}
.loop .cyl .cb{fill:#ebe6ff;stroke:var(--vi);stroke-width:1.3}.loop .cyl .ct{fill:#fff;stroke:var(--vi);stroke-width:1.3}.loop .cyl .st{fill:none;stroke:rgba(91,43,255,.35)}
.loop .cyl .sl{font:500 10px var(--mono);letter-spacing:.06em;fill:var(--vi)}.loop .cyl .cn{font:600 12px var(--mono);letter-spacing:.3em;fill:var(--ink)}
.rail{display:grid;grid-template-columns:repeat(8,1fr);margin-top:26px;border-top:2px solid var(--ink)}
.rail div{padding:14px 12px 4px 0;font:400 13.5px/1.45 var(--sans);color:var(--mut)}.rail div+div{padding-left:12px;border-left:1px solid var(--rl)}
.rail b{display:block;font:500 11px var(--mono);letter-spacing:.1em;color:var(--vi);margin-bottom:6px}.rail strong{display:block;font:500 15px var(--sans);color:var(--ink);margin-bottom:4px}
/* overnight: how a later reader changes tomorrow's run */
.night{display:grid;grid-template-columns:1.05fr 1fr;gap:0;border:1px solid rgba(23,19,31,.35);background:#fff}
.steps{list-style:none;margin:0;padding:8px 0;counter-reset:s}.steps li{display:grid;grid-template-columns:86px 1fr;gap:16px;padding:18px 24px;border-bottom:1px solid var(--rl)}.steps li:last-child{border-bottom:0}
.steps time{font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--vi);padding-top:3px}.steps h3{font:500 17px/1.3 var(--sans);margin:0 0 4px}.steps p{margin:0;color:var(--mut);font:400 14.5px/1.55 var(--sans)}
.gap{background:var(--plum);color:#e9e4ff;padding:26px;display:flex;flex-direction:column;gap:14px}
.gap .sx{color:rgba(255,255,255,.6)}.gap .sx b{color:var(--vi2)}
.gap pre{margin:0;background:#0b0712;border:1px solid rgba(255,255,255,.12);padding:16px 18px;overflow:auto;font:400 12.5px/1.65 var(--mono);white-space:pre-wrap}
.gap .k{color:#b69cff}.gap .s{color:#7ee2b8}.gap .c{color:#8a809f}.gap p{margin:0;font:400 14.5px/1.55 var(--sans);color:rgba(255,255,255,.72)}
.parts{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid rgba(255,255,255,.18)}.parts div{padding:10px 12px;font:400 12.5px/1.45 var(--sans);color:rgba(255,255,255,.7)}.parts div+div{border-left:1px solid rgba(255,255,255,.18)}.parts b{display:block;font:500 10px var(--mono);letter-spacing:.12em;color:#ffd166;margin-bottom:4px}
/* the compression bench */
.bench{display:grid;grid-template-columns:1.15fr 1fr 1fr;background:#fff;border:1px solid rgba(23,19,31,.35);min-height:520px}
.bench>div{padding:20px;display:flex;flex-direction:column;gap:12px;min-width:0}.bench>div+div{border-left:1px solid var(--rl)}
.bh{display:flex;justify-content:space-between;align-items:baseline;gap:10px;font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}.bh b{font-weight:500;color:var(--ink)}.bh.t2{margin-top:auto;padding-top:14px;border-top:1px solid var(--rl)}
.lcs{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.lc{padding:8px 11px;background:#f5f3fb;border-left:3px solid rgba(91,43,255,.4);font:400 13.5px/1.42 var(--sans);transition:opacity .5s calc(var(--i)*70ms),transform .6s calc(var(--i)*70ms),background .4s,border-color .4s}
.lc span{display:block;font:500 9.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--vi);margin-bottom:2px}
.bench.done .lc.k{transform:translateX(18px);opacity:.38}.bench.done .lc.x{border-color:#e5484d;background:#fff4f4;opacity:.55;text-decoration:line-through}.bench.done .lc.f{opacity:.12;transform:translateX(-10px)}
.go{align-self:flex-start;font:500 14px var(--sans);padding:11px 18px;border:0;background:var(--ink);color:#fff;cursor:pointer;border-radius:2px}.go:hover{background:var(--vi)}.go[disabled]{background:#cfcadb;cursor:default}
.pr{flex:1;display:flex;flex-direction:column;justify-content:center}.pr .wait{color:var(--mut);font:400 14.5px/1.55 var(--sans);margin:0}
.pr .pp{font:400 20px/1.4 var(--sans);letter-spacing:-.01em;margin:0;padding:18px;border:1.5px solid var(--vi);background:#f7f5ff;animation:ein .6s cubic-bezier(.3,.7,.2,1)}
.pr ul{list-style:none;margin:12px 0 0;padding:0;font:400 12px/1.5 var(--mono);color:var(--mut)}.pr li::before{content:"· ";color:var(--vi)}
.pcs{display:flex;flex-direction:column;gap:6px}.pc{text-align:left;font:400 14.5px var(--sans);padding:10px 12px;border:1px solid var(--rl);background:#fff;color:var(--ink);cursor:pointer;border-radius:2px;transition:border-color .2s,background .2s}
.pc:hover{border-color:var(--vi)}.pc.on{background:var(--vi);border-color:var(--vi);color:#fff}.pc[disabled]{opacity:.45;cursor:default}
.out{margin:0;display:grid;gap:0}.out dt{font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--vi);padding-top:14px}.out dd{margin:4px 0 0;padding-bottom:12px;border-bottom:1px dashed var(--rl);font:400 15px/1.45 var(--sans)}
.out.in dd,.out.in dt{animation:ein .5s both}.out dd:nth-of-type(2),.out dt:nth-of-type(2){animation-delay:.12s}.out dd:nth-of-type(3),.out dt:nth-of-type(3){animation-delay:.24s}.out dd:nth-of-type(4),.out dt:nth-of-type(4){animation-delay:.36s}
.note{font:400 13px var(--sans);color:var(--mut);margin:12px 0 0}
@keyframes ein{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
/* weights against context */
.cwt{width:100%;border-collapse:collapse;background:var(--paper);font:400 15.5px/1.45 var(--sans)}
.cwt th{text-align:left;font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut);padding:12px 14px;border-bottom:2px solid var(--ink)}.cwt th:last-child{color:var(--vi)}
.cwt td{padding:15px 14px;border-bottom:1px solid var(--rl);vertical-align:top}.cwt td:first-child{font:500 13px var(--sans);color:var(--ink);width:24%}.cwt td:nth-child(2){color:var(--mut)}.cwt td:last-child{background:#f7f5ff}
.cwt tr{transition:background .2s}.cwt tbody tr:hover td:not(:last-child){background:#fff}
/* evidence */
.ev{display:grid;grid-template-columns:300px 1fr;gap:0;border:1px solid rgba(23,19,31,.35);background:#fff}
.tiles{border-right:1px solid var(--rl)}.tiles div{padding:20px 22px;border-bottom:1px solid var(--rl)}.tiles div:last-child{border-bottom:0}
.tiles b{display:block;font:300 46px/1 var(--sans);letter-spacing:-.04em;color:var(--ink);font-variant-numeric:tabular-nums}.tiles b span{font-size:.42em;color:var(--mut);letter-spacing:0;margin-left:4px}.tiles b.v{color:var(--vi)}
.tiles p{margin:8px 0 0;font:500 10.5px/1.5 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
.chartw{padding:22px;min-width:0}.chartw .sc{overflow-x:auto}.tr{width:100%;min-width:640px;height:auto;display:block}
.tr .g{stroke:rgba(23,19,31,.1)}.tr .ax{font:400 11px var(--mono);fill:var(--mut)}.tr .ln{fill:none;stroke-width:2}.tr .ln.p{stroke:var(--vi)}.tr .ln.f{stroke:rgba(23,19,31,.35)}
.tr .dt.p{fill:var(--vi)}.tr .dt.f{fill:#b9b4c6}.tr .sep{stroke:var(--ink);stroke-dasharray:3 4}.tr .vl{font:600 15px var(--sans)}.tr .vl.p{fill:var(--vi)}.tr .vl.f{fill:var(--mut)}
.key{display:flex;gap:18px;font:500 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin-bottom:10px}.key i{display:inline-block;width:14px;height:3px;margin-right:7px;vertical-align:3px;background:var(--vi)}.key i.f{background:rgba(23,19,31,.35)}
.chartw p{font:400 14px/1.55 var(--sans);color:var(--mut);margin:12px 0 0;max-width:70ch}.chartw p a{color:var(--vi)}
/* laws */
.laws{display:grid;grid-template-columns:repeat(4,1fr);border-top:2px solid var(--ink)}.laws div{padding:20px 20px 24px 0;border-bottom:1px solid var(--rl)}.laws div:not(:nth-child(4n+1)){padding-left:20px;border-left:1px solid var(--rl)}
.laws b{display:block;font:500 11px var(--mono);letter-spacing:.1em;color:var(--vi);margin-bottom:8px}.laws h3{font:400 20px/1.25 var(--sans);letter-spacing:-.01em;margin:0 0 6px}.laws p{margin:0;color:var(--mut);font:400 14.5px/1.55 var(--sans)}
/* research */
.res{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid rgba(23,19,31,.35);background:var(--paper)}
.res a{display:flex;flex-direction:column;gap:10px;padding:22px;text-decoration:none;min-height:230px;transition:background .25s}.res a+a{border-left:1px solid var(--rl)}.res a:hover{background:#fff}
.res .ty{font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--vi)}.res h3{font:400 22px/1.2 var(--sans);letter-spacing:-.015em;margin:0}.res p{margin:0;color:var(--mut);font:400 14.5px/1.5 var(--sans)}.res .dt{margin-top:auto;font:400 12px var(--mono);color:var(--mut)}
@media (max-width:1000px){.night,.ev,.bench{grid-template-columns:1fr}.bench>div+div{border-left:0;border-top:1px solid var(--rl)}.tiles{border-right:0;border-bottom:1px solid var(--rl)}.rail{grid-template-columns:repeat(4,1fr)}.rail div:nth-child(5){border-left:0;padding-left:0}.laws,.res{grid-template-columns:1fr 1fr}.laws div:not(:nth-child(4n+1)){padding-left:0;border-left:0}.laws div:nth-child(even){padding-left:20px;border-left:1px solid var(--rl)}.res a:nth-child(3){border-left:0}.res a:nth-child(n+3){border-top:1px solid var(--rl)}}
@media (max-width:760px){.rail,.laws,.res,.parts{grid-template-columns:1fr}.rail div+div,.parts div+div{border-left:0;padding-left:0;border-top:1px solid var(--rl)}.laws div:nth-child(even){padding-left:0;border-left:0}.res a+a{border-left:0;border-top:1px solid var(--rl)}.oh .bow{width:230%;left:-65%}.cwt td:first-child{width:auto}.cwt{font-size:14px}.steps li{grid-template-columns:1fr;gap:4px}}
@media (prefers-reduced-motion:reduce){.bow *,.loop *{animation:none!important}}
"""

JS = r"""<script>(function(){
var P=window.ENGRAM_PLACES||{},b=document.getElementById('bench');if(!b)return;
var go=document.getElementById('bcmp'),pr=document.getElementById('bpr'),ver=document.getElementById('bver'),out=document.getElementById('bout'),pl=document.getElementById('bplace'),cs=[].slice.call(b.querySelectorAll('.pc'));
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
cs.forEach(function(c){c.disabled=true});
go.addEventListener('click',function(){b.classList.add('done');go.disabled=true;go.textContent='Compressed';
 setTimeout(function(){ver.textContent='routing · v7';pr.innerHTML='<p class="pp">'+esc(window.ENGRAM_PRINCIPLE)+'</p><ul><li>distilled from 6 learnings, each one cited</li><li>1 contradiction resolved: one role cannot own every warning</li><li>1 note faded: it never changed a design</li><li>supersedes v6, which stays readable</li></ul>';
  cs.forEach(function(c){c.disabled=false});cs[0].click()},700)});
cs.forEach(function(c){c.addEventListener('click',function(){if(c.disabled)return;cs.forEach(function(x){x.classList.toggle('on',x===c)});var p=P[c.getAttribute('data-p')];pl.textContent=p[0];
 out.classList.remove('in');void out.offsetWidth;out.innerHTML=p[1].map(function(r){return '<dt>'+esc(r[0])+'</dt><dd>'+esc(r[1])+'</dd>'}).join('');out.classList.add('in')})});
})();</script>"""


def build():
    import json, padi
    j = padi.load()
    bl = (j or {}).get("blind") or (j or {}).get("latest") or {}
    hero = ('<section class="oh eh">' + bowtie_svg() + '<div class="shade"></div><div class="hc">'
            f'<div class="wmb"><h1 class="wm" aria-label="Hyper Engram"><svg viewBox="0 0 38 30" aria-hidden="true"><path d="{MARK}"/></svg><span>Engram</span></h1><p class="wtag">Dedicated inference for your sovereign AI models.</p></div>'
            '<div class="tblk"><span>Product</span><span>Hyper Engram</span><span>Method</span><span>Compression and reinflation</span>'
            '<span>Trains</span><span>Context and weights</span><span>Memory</span><span>Inside your walls</span>'
            f'<div class="acts"><a href="{brand.COMMERCIAL}">{brand.TALK} →</a><a href="#research">Read the research →</a></div></div></div></section>')
    statement = ('<section class="ost"><div class="wrap3"><div>' + sx(0, "The thesis") + '</div><div>'
                 '<p class="st" data-type>Every operation has something to teach its AI. The first question we ask is <em>what belongs in context and what belongs in the weights.</em> We train both.</p>'
                 '<p class="sub" data-after>Hyper Engram is the agentic memory of the Hyper stack. It is the loop that trains a system run after run: every run, outcome and correction is written back, compressed into versioned principles every morning, and reinflated by the model into the next problem it meets. A lesson learned today changes tomorrow\'s behaviour.</p></div></div></section>')
    loop = ('<section class="osec"><div class="wrap3">' + head(1, "The learning loop", "A system that improves itself, <em>one loop at a time.</em>",
            "One master agent runs each RSI Loop. Two routines learn on their own every morning. None of them speak to each other directly: they read and write one memory, and that memory is what the planner reasons over.")
            + '<div class="sheet"><div class="scrollx">' + loop_svg() + '</div><div class="tb"><span>Sheet 01</span><span>Recursive learning loop</span><span>Hyper Engram</span></div></div>'
            '<div class="rail">'
            + "".join(f'<div data-after><b>{a}</b><strong>{h}</strong>{t}</div>' for a, h, t in [
                ("A", "Read", "Where the last loop left the platform and both routines."), ("B", "Plan", "A short ranked list of changes, each with its measure."),
                ("C", "Build", "Small commits, every release tagged and reversible."), ("D", "Real requirements", "Designs on documents nobody wrote for a test."),
                ("E", "Benchmark", "Fresh tasks against frontier AI on its own."), ("F", "Premortem", "Would the design have caught a real incident?"),
                ("G", "Feed the routines", "Every finding written into memory for its owner."), ("H", "Close", "What the loop learned, read first by the next one.")])
            + '</div></div></section>')
    stages = [("01", "cap", "Capture", "Every run is training data.", "Every run is kept as an episode: what it did, what it measured, and what went wrong with how it worked. Nothing is thrown away."),
              ("02", "cmp", "Compress", "Distillation, every morning.", "Every morning a routine distils raw learnings into versioned principles. Many observations become one. Contradictions are resolved. What never mattered fades."),
              ("03", "rei", "Reinterpret", "A second reader, every time.", "A later reader, usually the master agent, finds what a run missed and writes a rule for next time onto that run's own episode. An adversarial verifier checks every writer."),
              ("04", "rec", "Reinflate", "Context at inference.", "When a new problem arrives the model reads the compressed memory and expands it into this place, these laws, these people. The same lesson becomes a different design each time.")]
    stage_html = ('<div class="specs">' + "".join(f'<div class="spec"><span class="no">{no}</span>{glyph(g)}<h3>{h}</h3><p><strong>{E(s)}</strong> {E(t)}</p></div>' for no, g, h, s, t in stages) + '</div>')
    platform = ('<section class="osec"><div class="wrap3">' + head(2, "Platform", "Four stages. <em>One training loop.</em>",
                "Data, training, evaluation and serving, rebuilt for systems that work in the real world: capture, compression, reinterpretation and reinflation. The training signal lands where the model reads it, so a lesson is in use the next morning.")
                + stage_html + '</div></section>')
    night = ('<section class="osec"><div class="wrap3">' + head(3, "Reinterpretation", "Learned tonight. <em>Used tomorrow morning.</em>",
             "Every routine begins its run by reading the feedback and gap records on its newest episodes, before it does anything else. That intake is the whole trick: behaviour changes without anyone touching the code.")
             + '<div class="night"><ol class="steps">'
             + "".join(f'<li data-after><time>{a}</time><div><h3>{h}</h3><p>{t}</p></div></li>' for a, h, t in [
                 ("Day 1", "A run misses something", "A design senses the warning a real incident would have started with, and never says who must act on it."),
                 ("Evening", "A later reader finds it", "The master agent reads the run and files a gap record on its episode: what was missed, the fix, and a rule for next time, written in the routine's own terms."),
                 ("Day 2, first thing", "The routine reads before it acts", "Its intake lists every rule in force. The rule is now part of how it works, with no change to its code."),
                 ("Next loop", "The record closes, or it does not", "The next RSI Loop checks whether the gap closed. A record still open is the first item of the next plan.")])
             + '</ol><div class="gap">' + sx(3, "One gap record") +
             '<pre><span class="c">// filed on the routine\'s newest episode</span>\n{\n  <span class="k">gap</span>: <span class="s">"designs sense the warning but never name who acts"</span>,\n'
             '  <span class="k">fix</span>: <span class="s">"brief a routing principle from general practice"</span>,\n  <span class="k">found_by</span>: <span class="s">"master agent"</span>,\n  <span class="k">status</span>: <span class="s">"open"</span>,\n'
             '  <span class="k">rule_for_next_time</span>: <span class="s">"every sensed warning names the role\n    that acts, the reading that starts the clock\n    and the options of the decision"</span>\n}</pre>'
             '<div class="parts"><div><b>EPISODE</b>What the run did and measured.</div><div><b>FEEDBACK</b>What was wrong with how it worked, with a verdict.</div><div><b>GAP RECORDS</b>What a later reader found it missed.</div></div>'
             '<p>Every learner in the system, from the routines to the fleet, keeps its episodes in this one shape, so any reader can correct any writer.</p></div></div></div></section>')
    bench_s = ('<section class="osec" id="bench-s"><div class="wrap3">' + head(4, "Compression bench", "Compress once. <em>Reinflate anywhere.</em>",
               "Try it. Eight raw learnings become one principle, and the principle becomes a design for a mine, a contact centre or a hospital it never saw.")
               + '<div class="sheet">' + bench() + '<div class="tb"><span>Sheet 04</span><span>Compression and reinflation</span><span>Illustrative</span></div></div></div></section>')
    rows = [("Best for", "Stable skills used at high volume", "Knowledge that changes every month"),
            ("A new regulation arrives", "Joins the next training run", "One new entry, verified and live within hours"),
            ("Reading what was learned", "Measured through evaluation", "Every principle lists the learnings it came from"),
            ("A stronger base model arrives", "The training run is repeated on it", "The memory carries over on day one"),
            ("Undoing a lesson", "Roll back to an earlier checkpoint", "Retire one versioned principle"),
            ("Where it runs", "Inside your perimeter, on models you host", "Inside your perimeter, on your infrastructure")]
    vs = ('<section class="osec"><div class="wrap3">' + head(5, "Context and weights", "Two places to train. <em>We decide per lesson.</em>",
          "On every engagement we first work out how much of what the system must learn belongs in context and how much in the weights, then train each where it pays. This loop is the context side, and it runs every day.")
          + '<table class="cwt"><thead><tr><th></th><th>Trained into the weights</th><th>Trained into context, with Engram</th></tr></thead><tbody>'
          + "".join(f'<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in rows) + '</tbody></table></div></section>')
    ev = ""
    if j:
        tasks_ahead = bl.get("platform_ahead_on_tasks")
        n_t = bl.get("tasks")
        tile_ahead = f'<div><b>{tasks_ahead}<span>of {n_t}</span></b><p>Unseen tasks where Praxis came out ahead</p></div>' if tasks_ahead is not None and n_t else ""
        ev = ('<section class="osec"><div class="wrap3">' + head(6, "Evidence", "Measured <em>every loop.</em>",
              "Praxis, the platform Engram trains, is measured on PADI, our benchmark for physical AI system design, against frontier AI on its own, on fresh tasks every RSI Loop.")
              + '<div class="ev"><div class="tiles">'
              f'<div><b class="v">{bl.get("platform_pct")}%</b><p>Praxis, RSI Loop {bl.get("cycle")}, blind</p></div>'
              f'<div><b>{bl.get("bare_pct")}%</b><p>Frontier AI on its own, same tasks</p></div>' + tile_ahead +
              f'<div><b>{j["benchmark"]["sectors_measured"]}</b><p>Industries measured, in three countries</p></div></div>'
              '<div class="chartw"><div class="key"><span><i></i>Praxis platform</span><span><i class="f"></i>Frontier AI on its own</span></div><div class="sc">' + chart(j) + '</div>'
              f'<p>Checks passed as a share of checks judged, each RSI Loop. Loop {bl.get("cycle")} is a blind evaluation on tasks the platform had never seen; earlier loops reused some tasks and show the trend. Results are public; the method stays private. <a href="{BASE}/padi/">Every figure on PADI →</a></p></div></div></div></section>')
    laws = [("Every lesson in its place", "Each lesson is trained where it does the most good: into the context the model reads, or into the weights when a skill is stable and used at volume."),
            ("Meaning, never keywords", "Any decision about what a sentence means is put to a model and stored. Keyword scoring is banned."),
            ("Every claim stands on a source", "An entry needs a dated source. A principle needs the learnings it was distilled from."),
            ("Evaluation stays blind", "Held out tasks are never shown to the planner. Incident cases never feed the memory."),
            ("Two agents, two views", "Every writer has an adversarial verifier. Nothing verifies its own output."),
            ("The record is the context", "Commits, episodes and gap records carry the why. A session that lost its memory reads the log first."),
            ("Every release is reversible", "Each RSI Loop is tagged. A bad change is reverted by its own commit, a bad principle by its own version."),
            ("The memory is yours", "It lives in your perimeter, on models you host, and it survives every model you replace.")]
    laws_s = ('<section class="osec"><div class="wrap3">' + head(7, "Laws", "Eight rules <em>no loop may break.</em>", "They hold across every phase and every agent. A change that would bend one stops and waits for a person.")
              + '<div class="laws">' + "".join(f'<div data-after><b>{k + 1:02d}</b><h3>{E(h)}</h3><p>{E(t)}</p></div>' for k, (h, t) in enumerate(laws)) + '</div></div></section>')
    res = [(MEMO, "Memo", "Compression and Reinflation", "Compression, reinflation, and why what a system learns should survive the next model.", "Muhammad Umar · 10 Oct 2026"),
           (f"{BASE}/agentic-memory-architecture/", "Architecture", "Agentic Memory Architecture", "Memory told as a bow tie: experience, a waist of nightly distillation, and context assembled for each design.", "23 Oct 2026"),
           (f"{BASE}/padi/", "Benchmark", "Physical AI Design Index", "Fresh tasks across 13 industries in three countries, Praxis against frontier AI on its own.", "Updated every RSI Loop"),
           (f"{BASE}/hyper-pragma/", "Product", "Memory at work in Hyper Pragma", "The same memory inside a product: every run graded, every lesson visible, every lesson revocable.", "Hyper stack")]
    res_s = ('<section class="osec" id="research"><div class="wrap3">' + head(8, "Research", "Read how <em>it works.</em>", "The argument, the architecture, the measurements and the product, each on its own page.")
             + '<div class="res">' + "".join(f'<a href="{u}"><span class="ty">{t}</span><h3>{E(h)}</h3><p>{E(p)}</p><span class="dt">{E(d)} →</span></a>' for u, t, h, p, d in res) + '</div></div></section>')
    cta = (f'<section><div class="wrap3"><div class="octa"><div>Project<b>Hyper Engram</b></div><div>Trains<b>Every run</b></div>'
           f'<a class="t" href="{brand.COMMERCIAL}">{brand.TALK} <span>→</span></a><a class="s" href="{MEMO}">Read the memo <span>→</span></a></div></div></section>')
    faq = [("What is Hyper Engram?", "Hyper Engram is the agentic memory of CodeNinja's Hyper stack. It keeps every run, outcome and correction, compresses them into versioned principles, and gives them back to the model as context when it reasons. It is the loop that trains Praxis and Hyper Pragma, run after run."),
           ("How does Hyper Engram train a system?", "Runs are captured as episodes, daily routines compress them into principles that cite their sources, later readers file what a run missed as rules for next time, and at inference the model reinterprets the compressed memory for the problem in front of it."),
           ("What is compression and reinflation?", "Compression turns many observations into one small principle, resolving contradictions and dropping what never mattered. Reinflation is the model expanding that principle into a new situation: a different country, operation or set of people. The idea follows Michael Levin's work on self improvising memory in living systems."),
           ("Do you also train model weights?", "Yes, where it pays. On every engagement we first decide how much of what the system must learn belongs in context and how much in the weights. Engram trains the context side every day; stable skills used at high volume are trained into the weights of models the customer hosts."),
           ("What happens when a better model is released?", "It is swapped in. What Engram holds is not stored in the model, so it carries over and the new model starts with everything the system learned in context."),
           ("Where does the memory live?", "Inside the customer's perimeter, on their infrastructure, under their control, including air gapped deployments on models they host themselves.")]
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    depth = ('<section class="odep"><div class="wrap3 dg"><aside>' + sx(9, "In depth") + '<h2 data-type>Questions about Hyper Engram</h2></aside><div class="doc">'
             + "".join(f'<h2>{E(q)}</h2><p>{E(a)}</p>' for q, a in faq) + '</div></div></section>')
    data = f'<script>window.ENGRAM_PRINCIPLE={json.dumps(PRINCIPLE)};window.ENGRAM_PLACES={json.dumps(PLACES)};</script>'
    body = f'<main class="og eg">{hero}{statement}{loop}{platform}{night}{bench_s}{vs}{ev}{laws_s}{res_s}{cta}{depth}</main>{data}'
    title = "Hyper Engram: How We Train AI Systems, Run After Run | CodeNinja Atoms"
    desc = "Hyper Engram is the loop that trains AI systems by compression and reinflation: every run is captured, distilled and reinflated into the next one."
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Engram", "applicationCategory": "DeveloperApplication", "description": desc, "url": URL,
           "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "featureList": ["Episodes with feedback and gap records", "Daily distillation into versioned principles", "Adversarial verification of every writer",
                           "Context and weight training, decided per lesson", "Memory carried across model upgrades", "Runs inside the customer's perimeter"],
           "isRelatedTo": [{"@type": "SoftwareApplication", "name": "Hyper Pragma", "url": f"{BASE}/hyper-pragma/"}, {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"},
                           {"@type": "Article", "name": "Compression and Reinflation", "url": MEMO}]}, faq_ld]
    return shell(title, desc, URL, ld, OCSS + CSS, body, JS + TYPE_JS)
