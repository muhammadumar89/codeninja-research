"""Hyper Ontology product page (decision makers) and its developer portal (Start Building).

Umar, 13 Nov 2026: the main page is for the people who decide, rich and drawn, with
ontology images (an isometric stack, the living ontology of an operation, a kinetics
state machine), not a forward demo. Start Building opens the developer portal
(ontology_dev.py): ontology as code, semantics, kinetics, Atlas and Agentic Studio,
and every section there picks a fight with what other ontology platforms withhold.

Data: hyper-ontology/mining-ontology.json, trimmed from the generated src/mcp/manifest.ts
of the Mining GOLD Copper project in Hyper Studio (synthetic demo tenant). Never names a
competitor, never says "world's first", never says anything is missing.

    python tools/product_pages.py      (calls build() and ontology_dev.build())
"""
from __future__ import annotations

import html
import json
import math
from pathlib import Path

import brand

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)
MARK = "M15.6261 0H28.0897L18.3451 11.4995H24.6264L24.6265 11.4994H37.09L21.4126 30.0001H9.00037L22.5148 13.9996H16.2265L12.4123 18.5007H0L15.6261 0Z"
DEV = f"{BASE}/hyper-ontology/developers/"


def onto():
    return json.loads((ROOT / "hyper-ontology" / "mining-ontology.json").read_text())


# ------------------------------------------------------------------ drawing helpers
C30, S30 = math.cos(math.pi / 6), 0.5


class Iso:
    def __init__(self, ox, oy):
        self.ox, self.oy = ox, oy

    def p(self, x, y, z=0):
        return (self.ox + (x - y) * C30, self.oy + (x + y) * S30 - z)

    def pts(self, *xyz):
        return " ".join(f"{a:.1f},{b:.1f}" for a, b in (self.p(*q) for q in xyz))

    def slab(self, x, y, w, d, z, t, cls):
        top = self.pts((x, y, z), (x + w, y, z), (x + w, y + d, z), (x, y + d, z))
        left = self.pts((x, y + d, z), (x + w, y + d, z), (x + w, y + d, z - t), (x, y + d, z - t))
        right = self.pts((x + w, y, z), (x + w, y + d, z), (x + w, y + d, z - t), (x + w, y, z - t))
        return (f'<polygon class="{cls} sl" points="{left}"/><polygon class="{cls} sr" points="{right}"/>'
                f'<polygon class="{cls} st" points="{top}"/>')

    def box(self, x, y, z, s, h, cls="cube"):
        return self.slab(x, y, s, s, z + h, h, cls)


def hero_svg():
    """The stack: Atlas sources at the bottom, governance, kinetics, the ontology of objects and links on top,
    and the applications and agents that work on it floating above."""
    I = Iso(470, 420)
    W = 400
    o = []
    # bottom to top
    o.append('<g class="ly l0">' + I.slab(0, 0, W, W, 0, 16, "slab"))
    for i in range(6):
        for j in range(6):
            o.append(I.box(30 + i * 60, 30 + j * 60, 0, 22, 10 + ((i * 7 + j * 3) % 4) * 6, "cube"))
    o.append("</g>")
    o.append('<g class="ly l1">' + I.slab(0, 0, W, W, 74, 14, "slab"))
    for i in range(13):
        for j in range(13):
            a, b = I.p(20 + i * 30, 20 + j * 30, 74)
            on = (i * 5 + j * 11) % 7 in (0, 3)
            o.append(f'<ellipse class="dot{" on" if on else ""}" cx="{a:.1f}" cy="{b:.1f}" rx="5.2" ry="2.6"/>')
    o.append("</g>")
    o.append('<g class="ly l2">' + I.slab(0, 0, W, W, 142, 14, "slab"))
    for k, inset in enumerate((40, 80, 120)):
        o.append(f'<polygon class="track t{k}" points="{I.pts((inset, inset, 142), (W - inset, inset, 142), (W - inset, W - inset, 142), (inset, W - inset, 142))}"/>')
    o.append("</g>")
    # the ontology plane
    o.append('<g class="ly l3">' + I.slab(0, 0, W, W, 226, 16, "slab top"))
    nodes = {"Haul Truck": (70, 80), "Shovel Loader": (60, 210), "Person on Foot": (80, 330), "Interaction Event": (200, 150),
             "Collision Alert": (320, 70), "Work Order": (200, 290), "Fixed Camera": (330, 200), "Evidence Clip": (320, 320), "Work Permit": (190, 40)}
    links = [("Haul Truck", "Interaction Event"), ("Shovel Loader", "Interaction Event"), ("Person on Foot", "Interaction Event"), ("Interaction Event", "Collision Alert"),
             ("Interaction Event", "Evidence Clip"), ("Fixed Camera", "Evidence Clip"), ("Haul Truck", "Work Order"), ("Fixed Camera", "Work Order"),
             ("Work Permit", "Haul Truck"), ("Collision Alert", "Fixed Camera")]
    for k, (a, b) in enumerate(links):
        p1, p2 = I.p(*nodes[a], 226), I.p(*nodes[b], 226)
        o.append(f'<line class="lk" x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}"/>'
                 f'<line class="lk fl" style="animation-delay:{k * .7:.1f}s" x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}"/>')
    for k, (n, (x, y)) in enumerate(nodes.items()):
        a, b = I.p(x, y, 226)
        o.append(f'<g class="nd" style="animation-delay:{k * .9:.1f}s"><ellipse class="pk" cx="{a:.1f}" cy="{b:.1f}" rx="27" ry="13.5"/>'
                 + I.box(x - 9, y - 9, 226, 18, 16, "ncube") + f'<text x="{a:.1f}" y="{b + 28:.1f}">{E(n)}</text></g>')
    o.append("</g>")
    # applications and agents floating above
    cards = [("ANALYTICS", 40, 150), ("WORKFLOWS", 150, 10), ("AGENTS", 270, 130)]
    targets = ["Work Order", "Haul Truck", "Interaction Event"]
    for k, ((lab, x, y), tg) in enumerate(zip(cards, targets)):
        tx, ty = nodes[tg]
        a1, b1 = I.p(x + 45, y + 45, 380)
        a2, b2 = I.p(tx, ty, 244)
        o.append(f'<path class="drop" d="M{a1:.1f},{b1:.1f} C{a1:.1f},{(b1 + b2) / 2:.1f} {a2:.1f},{(b1 + b2) / 2:.1f} {a2:.1f},{b2:.1f}"/>')
        o.append(f'<g class="card c{k}">' + f'<polygon class="cd" points="{I.pts((x, y, 380), (x + 90, y, 380), (x + 90, y + 90, 380), (x, y + 90, 380))}"/>')
        for r in range(4):
            o.append(f'<polyline class="cl" points="{I.pts((x + 12, y + 18 + r * 16, 380), (x + 12 + (60 - r * 9), y + 18 + r * 16, 380))}"/>')
        tx2, ty2 = I.p(x + 92, y - 2, 380)
        o.append(f'<text class="ct" x="{tx2:.1f}" y="{ty2 - 6:.1f}">{lab}</text></g>')
    return f'<svg class="iso" viewBox="0 90 940 770" role="img" aria-label="Hyper Ontology as a stack: Atlas sources, governance, kinetics, the ontology of objects and links, and the applications and agents on top">{"".join(o)}</svg>'


def living_svg():
    """The living ontology of an operation, drawn the way the command centre draws it: applications and agents above,
    the ontology plane in the middle, Atlas sources and models below, with data moving between them."""
    o = []
    mons = [("Analytics", 120), ("Workflows", 470), ("Agents on Hyper Pragma", 820)]
    for lab, x in mons:
        o.append(f'<g class="mon"><text class="h" x="{x + 130}" y="34" text-anchor="middle">{E(lab)}</text>'
                 f'<rect x="{x}" y="50" width="260" height="150" rx="8"/><rect class="sc" x="{x + 10}" y="60" width="240" height="130" rx="4"/>'
                 f'<path d="M{x + 110},200 v24 M{x + 150},200 v24"/><rect x="{x - 26}" y="224" width="312" height="14" rx="3"/></g>')
    # analytics screen
    o.append('<text class="s" x="140" y="82">Open work orders, high priority</text><polyline class="spark" points="140,160 170,150 200,156 230,132 260,140 290,118 320,124 350,104"/>'
             '<line class="lim" x1="140" y1="122" x2="350" y2="122"/><text class="s r" x="350" y="182" text-anchor="end">7 open</text>')
    # workflows screen
    o.append('<g class="wf"><rect class="pu" x="490" y="96" width="62" height="24" rx="4"/><text x="521" y="112" text-anchor="middle" class="w">Record</text>'
             '<rect class="pu" x="570" y="96" width="70" height="24" rx="4"/><text x="605" y="112" text-anchor="middle" class="w">Ontology</text>'
             '<rect x="658" y="96" width="56" height="24" rx="4"/><text x="686" y="112" text-anchor="middle">Agent</text>'
             '<rect x="570" y="140" width="70" height="24" rx="4"/><text x="605" y="156" text-anchor="middle">Write back</text>'
             '<path d="M552,108 h18 M640,108 h18 M605,120 v20"/></g>')
    # agents screen
    for k, t in enumerate(["fault-to-work-order", "critical-escalation", "sla-watch"]):
        o.append(f'<rect class="ag" x="845" y="{70 + k * 32}" width="210" height="24" rx="12"/><text x="860" y="{86 + k * 32}">{t}</text>')
    o.append('<text class="s" x="845" y="178">10 agents scheduled</text>')
    # ontology plane
    o.append('<polygon class="plane" points="230,300 970,300 1110,560 90,560"/><polygon class="pedge" points="90,560 1110,560 1110,572 90,572"/>')
    rows = [[("Work Permit", "doc"), ("Haul Truck", "cube"), ("Shovel Loader", "cube"), ("Light Vehicle", "cube"), ("Shift", "doc")],
            [("Person on Foot", "cube"), ("Interaction Event", "doc"), ("Collision Alert", "doc"), ("Supervisor Alert", "doc"), ("Model Version", "doc")],
            [("Haul Road", "doc"), ("Evidence Clip", "doc"), ("Fixed Camera", "cam"), ("Work Order", "doc"), ("Crusher Pocket", "cube")]]
    pos = {}
    for r, row in enumerate(rows):
        y = 340 + r * 80
        x0, x1 = 300 - r * 52, 900 + r * 52
        for c, (n, ic) in enumerate(row):
            x = x0 + (x1 - x0) * c / 4
            pos[n] = (x, y)
    edges = [("Haul Truck", "Interaction Event", "involved in"), ("Person on Foot", "Interaction Event", ""), ("Interaction Event", "Collision Alert", "raises"),
             ("Collision Alert", "Supervisor Alert", "escalates"), ("Interaction Event", "Evidence Clip", "recorded in"), ("Fixed Camera", "Evidence Clip", "films"),
             ("Fixed Camera", "Work Order", "repaired by"), ("Work Permit", "Haul Truck", "authorises"), ("Shovel Loader", "Interaction Event", "")]
    for k, (a, b, lab) in enumerate(edges):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        o.append(f'<line class="e{" hot" if lab else ""}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
        if lab:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            o.append(f'<g class="el"><rect x="{mx - len(lab) * 3.4 - 8}" y="{my - 10}" width="{len(lab) * 6.8 + 16}" height="18" rx="9"/><text x="{mx}" y="{my + 3}" text-anchor="middle">{lab}</text></g>')
    for n, (x, y) in pos.items():
        ic = {nm: i for row in rows for nm, i in row}[n]
        icon = (f'<path d="M{x - 9},{y - 18} l9,-5 l9,5 v11 l-9,5 l-9,-5 z M{x - 9},{y - 18} l9,5 l9,-5 M{x},{y - 13} v11"/>' if ic == "cube" else
                f'<rect x="{x - 10}" y="{y - 22}" width="20" height="18" rx="3"/><circle cx="{x}" cy="{y - 13}" r="4"/>' if ic == "cam" else
                f'<rect x="{x - 8}" y="{y - 24}" width="16" height="20" rx="2"/><path d="M{x - 4},{y - 18} h8 M{x - 4},{y - 14} h8 M{x - 4},{y - 10} h6"/>')
        o.append(f'<g class="on"><ellipse cx="{x}" cy="{y}" rx="20" ry="6"/>{icon}<text x="{x}" y="{y + 20}" text-anchor="middle">{E(n)}</text></g>')
    o.append('<text class="h" x="600" y="600" text-anchor="middle">Ontology</text>')
    # atlas and models
    srcs = ["Fleet management", "Collision avoidance", "Maintenance ERP", "Video management", "Permit register", "Plant historian"]
    o.append('<g class="base"><rect x="190" y="640" width="470" height="150" rx="6"/><text class="h" x="425" y="812" text-anchor="middle">Atlas: your systems, connected in place</text>')
    for k, s in enumerate(srcs):
        x, y = 222 + (k % 3) * 150, 660 + (k // 3) * 64
        o.append(f'<rect x="{x}" y="{y}" width="34" height="26" rx="3"/><path d="M{x + 7},{y + 8} h20 M{x + 7},{y + 13} h20 M{x + 7},{y + 18} h14"/><text x="{x + 42}" y="{y + 17}">{s}</text>')
    o.append('</g><g class="base"><rect x="720" y="640" width="300" height="150" rx="6"/><text class="h" x="870" y="812" text-anchor="middle">Models, inside your walls</text>')
    for k, s in enumerate(["GLM 5.3", "Detection model", "Forecast"]):
        x = 742 + k * 92
        o.append(f'<rect x="{x}" y="672" width="40" height="34" rx="3"/><polyline points="{x + 6},{698} {x + 15},{688} {x + 24},{694} {x + 34},{680}"/><text x="{x + 20}" y="724" text-anchor="middle">{s}</text>')
    o.append("</g>")
    # moving data
    paths = []
    for k in range(6):
        x = 239 + (k % 3) * 150
        paths.append(f"M{x},{660 + (k // 3) * 64} C{x},{600} {300 + k * 90},{620} {300 + k * 100},{572}")
    for k, x in enumerate((800, 880, 960)):
        paths.append(f"M{x},640 C{x},{610} {x - 40},{600} {x - 60},572")
    for k, (x, tx) in enumerate(((250, 360), (560, 600), (950, 900))):
        paths.append(f"M{tx},300 C{tx},{270} {x + 20},{262} {x + 20},238")
    for k, d in enumerate(paths):
        o.append(f'<path class="wire" d="{d}"/><circle class="pk2" r="3.4"><animateMotion dur="{2.6 + (k % 4) * .5:.1f}s" begin="{k * .37:.2f}s" repeatCount="indefinite" path="{d}"/></circle>')
    return f'<svg class="living" viewBox="0 0 1200 830" role="img" aria-label="A living ontology: applications and agents above, the ontology of a mine in the middle, Atlas sources and models below">{"".join(o)}</svg>'


def explorer(data):
    """Every object in the Mining GOLD Copper ontology, by business domain. Click one, or ask by any name it is known by."""
    cols = ["Fleet and assets", "Safety Events and Collision Avoidance", "Safety & Compliance", "Mine Infrastructure and Spatial Zones", "Operations and Maintenance"]
    heads = ["Fleet and assets", "Safety events", "Compliance", "Infrastructure", "Operations"]
    objs = data["objects"]
    pos = {}
    for ci, c in enumerate(cols):
        group = [o for o in objs if o["domain"] == c]
        for ri, o in enumerate(group):
            pos[o["id"]] = (100 + ci * 200, 84 + ri * 66 + (0 if len(group) > 3 else 50))
    lines, seen = [], set()
    for o in objs:
        for to, phrase, card in o["links"]:
            k = tuple(sorted((o["id"], to)))
            if to not in pos or k in seen:
                continue
            seen.add(k)
            (x1, y1), (x2, y2) = pos[o["id"]], pos[to]
            lines.append(f'<path class="xe" data-a="{o["id"]}" data-b="{to}" d="M{x1},{y1} C{(x1 + x2) / 2},{y1} {(x1 + x2) / 2},{y2} {x2},{y2}"/>')
    heads_svg = "".join(f'<text class="xh" x="{100 + i * 200}" y="34" text-anchor="middle">{E(h.upper())}</text>' for i, h in enumerate(heads))
    nodes = "".join(f'<g class="xn{" lc" if o["lifecycles"] else ""}" data-id="{o["id"]}" tabindex="0" role="button" aria-label="{E(o["name"])}"><rect x="{pos[o["id"]][0] - 82}" y="{pos[o["id"]][1] - 19}" width="164" height="38" rx="19"/>'
                    f'<text x="{pos[o["id"]][0]}" y="{pos[o["id"]][1] + 5}" text-anchor="middle">{E(o["name"])}</text></g>' for o in objs)
    svg = f'<svg class="xsvg" viewBox="0 0 1000 400" role="img" aria-label="The objects of the Mining GOLD Copper ontology and their links">{heads_svg}{"".join(lines)}{nodes}</svg>'
    return ('<div class="xbox"><div class="xmap"><div class="xq"><label for="xq">Ask by any name the business uses</label><input id="xq" type="search" placeholder="Try: repair ticket, CCTV camera, zone breach, pedestrian" autocomplete="off"><p id="xr"></p></div>'
            f'{svg}<p class="xleg"><i class="a"></i>Has a lifecycle <i class="b"></i>Linked to the selection</p></div><aside class="xd" id="xd" aria-live="polite"></aside></div>'
            f'<script>window.HYPER_ONTOLOGY={json.dumps(data, ensure_ascii=False)};</script>')


def kinetics_box(data):
    wo = next(o for o in data["objects"] if o["id"] == "maintenance-work-order")
    lc = wo["lifecycles"][0]
    P = {"unassigned": (300, 60), "assigned": (500, 160), "waiting_on_parts": (120, 160), "in_progress": (330, 260), "completed": (500, 370), "cancelled": (140, 370)}
    arcs = []
    for lab, frm, to, tool in lc["transitions"]:
        for f in frm:
            (x1, y1), (x2, y2) = P[f], P[to]
            arcs.append(f'<path class="ke" data-t="{E(tool)}" d="M{x1},{y1 + 18} Q{(x1 + x2) / 2 + (30 if x2 > x1 else -30)},{(y1 + y2) / 2} {x2},{y2 - 18}" marker-end="url(#ar)"/>')
    st = "".join(f'<g class="ks{" init" if init else ""}{" term" if term else ""}" data-s="{v}"><rect x="{P[v][0] - 78}" y="{P[v][1] - 18}" width="156" height="36" rx="8"/><text x="{P[v][0]}" y="{P[v][1] + 5}" text-anchor="middle">{v}</text></g>'
                 for v, init, term in lc["states"])
    svg = (f'<svg class="ksvg" viewBox="0 0 640 410" role="img" aria-label="The orderStatus lifecycle of a maintenance work order"><defs><marker id="ar" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z"/></marker></defs>'
           f'{"".join(arcs)}{st}<circle id="ktok" r="9" cx="300" cy="60"/></svg>')
    btns = "".join(f'<button type="button" class="kb" data-tool="{E(tool)}" data-from="{E(" ".join(frm))}" data-to="{E(to)}" data-label="{E(lab)}">{E(lab)}</button>' for lab, frm, to, tool in lc["transitions"])
    return ('<div class="kbox"><div class="kl"><div class="kh"><b>Maintenance Work Order</b><span>lifecycle on orderStatus</span></div>'
            f'{svg}</div><div class="kr"><p class="kk">Move work order <b>MFS 115</b></p><div class="kbs">{btns}</div>'
            '<button type="button" class="kb raw" id="kraw">Edit orderStatus directly</button><button type="button" class="kb rs" id="krs">Reset</button>'
            '<ol class="klog" id="klog" aria-live="polite"><li class="ok">MFS 115 created in <b>unassigned</b>, the lifecycle\'s initial state</li></ol></div></div>')


CSS = r"""
.og{--plum:#140d1f;--plum2:#1d1430;--vi:#5b2bff;--vi2:#9b85ff;--lav:#efecfa;--lav2:#e4dff8;--ink:#17131f;--mut:#5f5873;--rl:rgba(23,19,31,.12);background:#f7f6fb;color:var(--ink)}
.og a{color:inherit}
.og .wrap3{max-width:1240px;margin:0 auto;padding:0 clamp(16px,3vw,40px)}
.og .eb{display:inline-flex;align-items:center;gap:8px;font:500 11.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}.og .eb::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--ink)}
.og h2.big{font:300 clamp(34px,4.4vw,64px)/1.06 var(--sans);letter-spacing:-.035em;margin:16px auto 0;max-width:21ch}.og h2.big em{font-style:normal;color:var(--vi)}
.og .lead2{font:300 clamp(18px,1.5vw,21px)/1.5 var(--sans);color:var(--mut);max-width:56ch;margin:18px 0 0}
/* hero */
.oh{position:relative;overflow:hidden;min-height:100vh;background:radial-gradient(60% 60% at 68% 36%,rgba(91,43,255,.28),rgba(20,13,31,0) 70%),linear-gradient(180deg,#0d0816,var(--plum) 60%,#0b0712);color:#fff;display:flex;flex-direction:column;justify-content:flex-end}
.oh .iso{position:absolute;right:max(-40px,calc(50% - 720px));top:clamp(104px,13vh,140px);width:min(58vw,880px,calc((100vh - 150px) * 1.22));height:auto}
.oh .hc{position:relative;display:flex;justify-content:space-between;align-items:flex-end;gap:30px;padding:0 clamp(16px,3vw,44px) clamp(20px,3.2vw,44px)}
.oh .wm{display:flex;align-items:center;gap:clamp(12px,1.5vw,24px);margin:0;font:300 clamp(70px,12.5vw,214px)/.8 var(--sans);letter-spacing:-.06em}.oh .wm svg{height:.64em;width:auto;fill:#fff}
.oh .side{max-width:320px;display:flex;flex-direction:column;gap:14px;padding-bottom:8px;font:400 11px/1.45 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.85)}
.oh .side p{margin:0;padding-left:12px;border-left:1px solid rgba(255,255,255,.4)}.oh .side .dim{color:rgba(255,255,255,.55)}.oh .side .lk{border-left-color:var(--vi2)}.oh .side a{text-decoration:none;color:#fff}.oh .side a:hover{color:var(--vi2)}
.oh .shade{position:absolute;inset:0;pointer-events:none;background:linear-gradient(0deg,rgba(11,7,18,.9) 0,rgba(11,7,18,.2) 34%,rgba(11,7,18,0) 50%)}
.iso .slab{stroke:rgba(205,190,255,.55);stroke-width:1;stroke-linejoin:round}.iso .slab.st{fill:rgba(40,26,66,.92)}.iso .slab.sl{fill:rgba(26,17,44,.95)}.iso .slab.sr{fill:rgba(33,22,55,.95)}
.iso .top.st{fill:rgba(56,36,98,.95);stroke:rgba(190,170,255,.8)}
.iso .cube{stroke:rgba(190,170,255,.45);stroke-width:.8}.iso .cube.st{fill:#2e2050}.iso .cube.sl{fill:#1c1332}.iso .cube.sr{fill:#251a41}
.iso .dot{fill:none;stroke:rgba(190,170,255,.4);stroke-width:.8}.iso .dot.on{fill:#cfc3ff;stroke:none}
.iso .track{fill:none;stroke:rgba(190,170,255,.45);stroke-dasharray:3 6;animation:odash 6s linear infinite}.iso .track.t1{animation-duration:9s;animation-direction:reverse}.iso .track.t2{stroke:#9b85ff;stroke-dasharray:14 10}
.iso .lk{stroke:rgba(200,185,255,.45);stroke-width:1.1}.iso .lk.fl{stroke:#b6a4ff;stroke-width:2;stroke-dasharray:10 160;animation:odash 4.5s linear infinite}
.iso .pk{fill:rgba(91,43,255,.18);stroke:rgba(200,185,255,.6)}.iso .ncube.st{fill:#cfc3ff}.iso .ncube.sl{fill:#7b62e8}.iso .ncube.sr{fill:#9b85ff}.iso .ncube{stroke:#fff;stroke-width:.6}
.iso text{font:500 10.5px var(--mono);fill:rgba(255,255,255,.82);text-anchor:middle;letter-spacing:.02em}
.iso .nd{animation:oglow 8s ease-in-out infinite}.iso .nd .pk{transition:fill .4s}
.iso .card{animation:obob 6s ease-in-out infinite}.iso .card.c1{animation-delay:-2s}.iso .card.c2{animation-delay:-4s}
.iso .cd{fill:rgba(244,240,255,.95);stroke:#fff}.iso .cl{fill:none;stroke:#7b62e8;stroke-width:2}.iso .ct{font:600 10px var(--mono);fill:#fff;letter-spacing:.14em;text-anchor:start}
.iso .drop{fill:none;stroke:rgba(200,185,255,.55);stroke-dasharray:2 4}
@keyframes odash{to{stroke-dashoffset:-170}}@keyframes obob{50%{transform:translateY(-8px)}}@keyframes oglow{0%,70%,100%{opacity:.82}80%{opacity:1;filter:drop-shadow(0 0 8px #9b85ff)}}
/* statement */
.ost{background:#fff;padding:clamp(90px,12vw,170px) 0;text-align:center}.ost p{font:300 clamp(30px,3.9vw,58px)/1.14 var(--sans);letter-spacing:-.03em;max-width:24ch;margin:0 auto}.ost em{font-style:normal;color:var(--vi)}
.ost .sub{font:300 clamp(17px,1.4vw,20px)/1.5 var(--sans);color:var(--mut);max-width:58ch;margin:28px auto 0;letter-spacing:0}
/* lavender panels */
.opan{padding:clamp(60px,7vw,100px) 0}.opan .pbox{background:var(--lav);border-radius:6px;padding:clamp(40px,5vw,70px) clamp(18px,4vw,60px) clamp(30px,4vw,50px);text-align:center;
 background-image:linear-gradient(30deg,rgba(91,43,255,.05) 1px,transparent 1px),linear-gradient(150deg,rgba(91,43,255,.05) 1px,transparent 1px);background-size:38px 22px}
.living{width:100%;height:auto;margin-top:34px}
.living text{font:400 12px var(--sans);fill:var(--ink)}.living .h{font:600 14px var(--sans)}.living .s{font:400 11px var(--sans);fill:var(--mut)}
.living .mon rect,.living .mon path{fill:#fff;stroke:var(--ink);stroke-width:1.2}.living .mon .sc{fill:#fbfaff;stroke:rgba(23,19,31,.3)}
.living .spark{fill:none;stroke:#e5484d;stroke-width:2}.living .lim{stroke:#e5484d;stroke-dasharray:4 4}
.living .wf rect{fill:#fff;stroke:var(--ink)}.living .wf .pu{fill:var(--vi);stroke:var(--vi)}.living .wf .w{fill:#fff}.living .wf path{stroke:var(--ink);fill:none}.living .wf text{font-size:11px}
.living .ag{fill:#fff;stroke:rgba(23,19,31,.25)}.living text.s.r{font-weight:600;fill:#e5484d}
.living .plane{fill:rgba(255,255,255,.7);stroke:var(--ink);stroke-width:1.3}.living .pedge{fill:url(#none);fill:rgba(23,19,31,.1);stroke:var(--ink)}
.living .e{stroke:rgba(23,19,31,.18);stroke-width:1.2}.living .e.hot{stroke:var(--vi);stroke-width:1.8}
.living .el rect{fill:#ebe6ff;stroke:rgba(91,43,255,.35)}.living .el text{font:500 10px var(--sans);fill:var(--vi)}
.living .on ellipse{fill:#ebe6ff;stroke:rgba(91,43,255,.4)}.living .on path,.living .on rect,.living .on circle{fill:#fff;stroke:var(--ink);stroke-width:1.1}.living .on text{font-size:11.5px}
.living .base rect,.living .base path,.living .base polyline{fill:#fff;stroke:var(--ink);stroke-width:1.1}.living .base polyline{fill:none}.living .base text{font-size:11px}
.living .wire{fill:none;stroke:rgba(23,19,31,.28);stroke-dasharray:2 4}.living .pk2{fill:var(--vi)}
.olg{display:flex;justify-content:center;flex-wrap:wrap;gap:22px;margin-top:20px;font:400 12.5px var(--sans);color:var(--mut)}.olg i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:7px;vertical-align:0}
/* cards */
.ocards{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:24px}.ocards.c3{grid-template-columns:repeat(3,1fr)}
.ocard{background:#fff;border-radius:6px;padding:26px 26px 22px;display:flex;flex-direction:column;min-height:220px}
.ocard h3{font:400 21px/1.25 var(--sans);letter-spacing:-.01em;color:var(--vi);margin:0 0 10px}.ocard p{font:400 15px/1.5 var(--sans);color:var(--mut);margin:0}
.ocard .more{margin-top:auto;padding-top:20px;font:500 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;color:var(--ink)}.ocard .more:hover{color:var(--vi)}
.ohead{background:#fff;border-radius:6px;padding:clamp(60px,7vw,100px) 20px;text-align:center}
.ochips{display:flex;flex-wrap:wrap;justify-content:center;gap:12px 14px;margin:0 auto;max-width:900px}.ochips span{border:1px solid var(--ink);padding:7px 14px;font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;background:#fff;transition:background .3s,color .3s}
.ochips span.on{background:var(--ink);color:#fff}
/* explorer */
.xbox{display:grid;grid-template-columns:1fr 360px;gap:0;background:#fff;border-radius:6px;overflow:hidden;margin-top:34px;text-align:left;border:1px solid var(--rl)}
.xmap{padding:22px 22px 14px;border-right:1px solid var(--rl);min-width:0}.xq label{display:block;font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--mut);margin-bottom:8px}
.xq input{width:100%;font:400 16px var(--sans);padding:12px 14px;border:1px solid var(--rl);border-radius:8px;background:#fbfaff;color:var(--ink)}.xq input:focus{outline:2px solid var(--vi);outline-offset:0}
.xq p{min-height:20px;margin:8px 0 0;font:400 13px var(--sans);color:var(--vi)}
.xsvg{width:100%;height:auto;margin-top:6px}.xh{font:500 10px var(--mono);letter-spacing:.12em;fill:var(--mut)}
.xe{fill:none;stroke:rgba(23,19,31,.13);stroke-width:1.2;transition:stroke .3s,stroke-width .3s}.xe.on{stroke:var(--vi);stroke-width:2.2}
.xn{cursor:pointer}.xn rect{fill:#fff;stroke:rgba(23,19,31,.3);transition:fill .25s,stroke .25s}.xn text{font:500 13px var(--sans);fill:var(--ink);pointer-events:none}
.xn.lc rect{stroke:var(--vi);stroke-width:1.5}.xn:hover rect,.xn:focus rect{stroke:var(--vi);outline:none}.xn.nb rect{fill:#efeaff}.xn.sel rect{fill:var(--vi);stroke:var(--vi)}.xn.sel text{fill:#fff}.xn.dim text{opacity:.4}.xn.dim rect{stroke-opacity:.35}
.xleg{display:flex;gap:18px;font:400 12px var(--sans);color:var(--mut);margin:4px 0 0}.xleg i{display:inline-block;width:16px;height:10px;border-radius:5px;margin-right:6px;vertical-align:-1px;border:1.5px solid var(--vi)}.xleg i.b{background:#efeaff;border-color:rgba(23,19,31,.3)}
.xd{padding:24px 22px;background:#fbfaff;font:400 14px/1.5 var(--sans);overflow:auto;max-height:640px}
.xd h4{font:500 22px/1.2 var(--sans);margin:0 0 4px;letter-spacing:-.01em}.xd .dm{font:500 10.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--vi)}.xd p{color:var(--mut);margin:10px 0 0}
.xd h5{font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin:20px 0 8px;padding-top:14px;border-top:1px solid var(--rl)}
.xd .sy{display:flex;flex-wrap:wrap;gap:6px}.xd .sy span{padding:4px 10px;border-radius:99px;background:#ebe6ff;color:var(--vi);font-size:12.5px}
.xd ul{list-style:none;margin:0;padding:0}.xd li{display:flex;justify-content:space-between;gap:12px;padding:5px 0;border-bottom:1px dashed var(--rl);font-size:13px}.xd li code{font:400 12px var(--mono);color:var(--ink)}.xd li span{color:var(--mut);font:400 11.5px var(--mono)}
.xd li a{color:var(--vi);text-decoration:none;cursor:pointer}
/* kinetics */
.kbox{display:grid;grid-template-columns:1.25fr 1fr;background:#fff;border-radius:6px;overflow:hidden;border:1px solid var(--rl);margin-top:34px;text-align:left}
.kl{border-right:1px solid var(--rl)}.kh{display:flex;gap:10px;align-items:baseline;padding:14px 18px;background:#412356;color:#fff;font:400 13px var(--sans)}.kh span{color:rgba(255,255,255,.65);font:400 12px var(--mono)}
.ksvg{width:100%;height:auto;display:block;padding:10px;background-image:radial-gradient(rgba(23,19,31,.12) 1px,transparent 1px);background-size:16px 16px}
.ks rect{fill:#fff;stroke:rgba(23,19,31,.4);stroke-width:1.2;transition:fill .3s,stroke .3s}.ks.init rect{stroke:var(--vi);stroke-width:2}.ks.term rect{stroke-width:2}.ks text{font:500 13px var(--mono);fill:var(--ink)}
.ks.cur rect{fill:var(--vi);stroke:var(--vi)}.ks.cur text{fill:#fff}
.ke{fill:none;stroke:rgba(23,19,31,.3);stroke-width:1.2;transition:stroke .3s}.ke.fire{stroke:var(--vi);stroke-width:2.4}#ar path{fill:rgba(23,19,31,.45)}
#ktok{fill:#ffd166;stroke:#17131f;stroke-width:1.5;opacity:0}
.kr{padding:22px}.kk{margin:0 0 12px;font:400 15px var(--sans)}.kbs{display:flex;flex-wrap:wrap;gap:8px}
.kb{font:500 13px var(--sans);padding:9px 14px;border-radius:8px;border:1px solid rgba(23,19,31,.2);background:#fff;color:var(--ink);cursor:pointer;transition:background .2s,border-color .2s}.kb:hover{border-color:var(--vi)}
.kb.ok{background:#ebe6ff;border-color:var(--vi)}.kb.raw{margin-top:10px;border-style:dashed}.kb.rs{margin:10px 0 0 8px;color:var(--mut)}
.klog{list-style:none;margin:16px 0 0;padding:0;font:400 12.5px/1.45 var(--mono);max-height:260px;overflow:auto}.klog li{padding:8px 10px;border-radius:6px;margin-bottom:6px;background:#f5f3fb}
.klog li.ok{border-left:3px solid #0f8a5f}.klog li.no{border-left:3px solid #e5484d;background:#fff4f4}.klog li.lock{border-left:3px solid #b0740f;background:#fffaf0}
/* atlas and agentic studio */
.otwo{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:24px}.ofig{background:#fff;border-radius:6px;padding:26px;display:flex;flex-direction:column}
.ofig svg{width:100%;height:auto;margin:6px 0 18px}.ofig h3{font:400 24px/1.2 var(--sans);letter-spacing:-.02em;margin:0 0 8px}.ofig h3 em{font-style:normal;color:var(--vi)}.ofig p{margin:0;color:var(--mut);font:400 15px/1.55 var(--sans)}
.ofig svg text{font:400 11px var(--sans);fill:var(--ink)}.ofig svg .m{font:500 9.5px var(--mono);letter-spacing:.1em;fill:var(--mut)}
.ofig svg rect,.ofig svg path,.ofig svg circle{fill:#fff;stroke:var(--ink);stroke-width:1.1}.ofig svg .v{fill:var(--vi);stroke:var(--vi)}.ofig svg .vt{fill:#fff}.ofig svg .w{fill:none;stroke:rgba(23,19,31,.3);stroke-dasharray:2 4}
.ofig svg .lv{fill:#ebe6ff;stroke:rgba(91,43,255,.45)}.ofig svg .g{fill:#0f8a5f;stroke:none}
/* code teaser */
.ocode{display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:center;background:var(--plum);color:#fff;border-radius:6px;padding:clamp(30px,5vw,64px);margin-top:24px;text-align:left}
.ocode h3{font:300 clamp(28px,3vw,42px)/1.1 var(--sans);letter-spacing:-.03em;margin:0 0 16px}.ocode h3 em{font-style:normal;color:var(--vi2)}.ocode p{color:rgba(255,255,255,.72);font:400 16px/1.55 var(--sans);margin:0 0 12px}
.ocode pre{margin:0;background:#0b0712;border:1px solid rgba(255,255,255,.12);border-radius:8px;padding:18px 20px;overflow:auto;font:400 12.5px/1.6 var(--mono);color:#e9e4ff}
.ocode .k{color:#b69cff}.ocode .s{color:#7ee2b8}.ocode .c{color:#8a809f}.ocode a.btn{display:inline-block;margin-top:10px;background:#fff;color:var(--ink);text-decoration:none;font:500 14px var(--sans);padding:12px 18px;border-radius:2px}
/* call to action */
.octa{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:20px 0 90px}.octa a{display:flex;justify-content:space-between;align-items:flex-start;min-height:150px;padding:20px 22px;text-decoration:none;font:300 clamp(30px,3.2vw,46px)/1 var(--sans);letter-spacing:-.03em;transition:background .25s}
.octa a.t{background:#dcdae3;color:var(--ink)}.octa a.t:hover{background:#cfccd9}.octa a.s{background:var(--ink);color:#fff}.octa a.s:hover{background:#2a2335}.octa a span{font-size:.8em}
/* in depth */
.odep{background:#fff;border-top:1px solid var(--rl);padding:90px 0 110px}.odep .dg{display:grid;grid-template-columns:280px 1fr;gap:60px}.odep .doc{font:400 17px/1.65 var(--sans);color:#2a2533;max-width:760px}
.odep .doc h1{display:none}.odep .doc h2{max-width:none;font:400 28px/1.2 var(--sans);letter-spacing:-.02em;margin:46px 0 14px;color:var(--ink)}.odep .doc table{width:100%;border-collapse:collapse;font-size:15px}.odep .doc td,.odep .doc th{border-bottom:1px solid var(--rl);padding:10px 8px;text-align:left;vertical-align:top}
.odep .doc .eyebrow{display:none}.odep .doc .box{background:var(--lav);padding:16px 18px;border-radius:6px}.odep .doc a{color:var(--vi)}
.odep aside{position:sticky;top:110px;align-self:start}.odep aside h2{font:300 34px/1.05 var(--sans);letter-spacing:-.03em;margin:10px 0 0}
@media (max-width:1000px){.xbox,.kbox,.ocode,.otwo{grid-template-columns:1fr}.xmap,.kl{border-right:0;border-bottom:1px solid var(--rl)}.ocards.c3{grid-template-columns:1fr}.odep .dg{grid-template-columns:1fr}.odep aside{position:static}}
@media (max-width:760px){.ocards,.octa{grid-template-columns:1fr}.oh .iso{width:118vw;right:-12vw;top:120px}.oh .hc{flex-direction:column;align-items:flex-start}.oh .side{max-width:none}.living{min-width:760px}.opan .scrollx{overflow-x:auto}}
@media (prefers-reduced-motion:reduce){.iso *,.living *{animation:none!important}}
"""

JS = r"""<script>(function(){
var D=window.HYPER_ONTOLOGY||{objects:[]},O={};D.objects.forEach(function(o){O[o.id]=o});
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')}
/* explorer: pick an object, see what it means, what it links to, how it may change */
var xd=document.getElementById('xd'),nodes=[].slice.call(document.querySelectorAll('.xn')),edges=[].slice.call(document.querySelectorAll('.xe'));
function show(id){var o=O[id];if(!o||!xd)return;var nb={};edges.forEach(function(e){var a=e.getAttribute('data-a'),b=e.getAttribute('data-b'),on=a===id||b===id;e.classList.toggle('on',on);if(on){nb[a]=1;nb[b]=1}});
 nodes.forEach(function(n){var k=n.getAttribute('data-id');n.classList.toggle('sel',k===id);n.classList.toggle('nb',k!==id&&!!nb[k]);n.classList.toggle('dim',k!==id&&!nb[k])});
 var h='<span class="dm">'+esc(o.domain)+'</span><h4>'+esc(o.name)+'</h4><p>'+esc(o.desc)+'</p>';
 if(o.syn.length)h+='<h5>Also known as</h5><div class="sy">'+o.syn.map(function(s){return '<span>'+esc(s)+'</span>'}).join('')+'</div>';
 h+='<h5>Properties</h5><ul>'+o.props.slice(0,9).map(function(p){return '<li><code>'+esc(p[0])+'</code><span>'+esc(p[1])+'</span></li>'}).join('')+(o.props.length>9?'<li><span>and '+(o.props.length-9)+' more</span></li>':'')+'</ul>';
 if(o.links.length)h+='<h5>Links</h5><ul>'+o.links.map(function(l){var t=O[l[0]];return '<li><span>'+esc(l[1])+'</span><a data-go="'+l[0]+'">'+esc(t?t.name:l[0])+'</a></li>'}).join('')+'</ul>';
 o.lifecycles.forEach(function(lc){h+='<h5>Kinetics · '+esc(lc.field)+'</h5><ul>'+lc.transitions.map(function(t){return '<li><code>'+esc(t[0])+'</code><span>'+esc(t[1].join(', '))+' → '+esc(t[2])+'</span></li>'}).join('')+'</ul>'});
 if(o.functions.length)h+='<h5>Functions</h5><ul>'+o.functions.map(function(f){return '<li><code>'+esc(f[0])+'</code><span>'+esc(f[2]||f[1])+'</span></li>'}).join('')+'</ul>';
 xd.innerHTML=h;[].forEach.call(xd.querySelectorAll('[data-go]'),function(a){a.addEventListener('click',function(){show(a.getAttribute('data-go'))})})}
nodes.forEach(function(n){var go=function(){show(n.getAttribute('data-id'))};n.addEventListener('click',go);n.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}})});
if(nodes.length)show('maintenance-work-order');
var xq=document.getElementById('xq'),xr=document.getElementById('xr');if(xq)xq.addEventListener('input',function(){var q=xq.value.trim().toLowerCase();if(!q){xr.textContent='';return}
 var hit=D.objects.filter(function(o){return o.name.toLowerCase().indexOf(q)>=0||o.syn.some(function(s){return s.toLowerCase().indexOf(q)>=0})});
 if(!hit.length){xr.textContent='No object answers to that name yet.';return}var o=hit[0],via=o.syn.filter(function(s){return s.toLowerCase().indexOf(q)>=0})[0];
 xr.textContent=via?('“'+via+'” resolves to '+o.name+', through its synonyms.'):('Found '+o.name+'.');show(o.id)});
/* kinetics: transitions are the only way a governed state changes */
var cur='unassigned',log=document.getElementById('klog'),tok=document.getElementById('ktok');
function paint(){[].forEach.call(document.querySelectorAll('.ks'),function(g){g.classList.toggle('cur',g.getAttribute('data-s')===cur)});
 [].forEach.call(document.querySelectorAll('.kb[data-from]'),function(b){b.classList.toggle('ok',b.getAttribute('data-from').split(' ').indexOf(cur)>=0)})}
function add(c,t){var li=document.createElement('li');li.className=c;li.innerHTML=t;log.insertBefore(li,log.firstChild)}
[].forEach.call(document.querySelectorAll('.kb[data-from]'),function(b){b.addEventListener('click',function(){var from=b.getAttribute('data-from').split(' '),to=b.getAttribute('data-to'),lab=b.getAttribute('data-label'),tool=b.getAttribute('data-tool');
 if(from.indexOf(cur)<0){add('no','<b>KINETICS_INVALID_TRANSITION</b> Cannot \''+esc(lab)+'\': orderStatus is \''+cur+'\', allowed from: '+esc(from.join(', ')));return}
 [].forEach.call(document.querySelectorAll('.ke'),function(e){e.classList.toggle('fire',e.getAttribute('data-t')===tool)});
 add('ok','<b>'+esc(tool)+'</b> '+cur+' → '+esc(to)+'. Row locked, moved and committed in one transaction.');cur=to;paint()})});
var raw=document.getElementById('kraw');if(raw)raw.addEventListener('click',function(){add('lock','<b>update</b> orderStatus stripped from the payload. A governed state only changes through a transition.')});
var rs=document.getElementById('krs');if(rs)rs.addEventListener('click',function(){cur='unassigned';log.innerHTML='';add('ok','MFS 115 created in <b>unassigned</b>, the lifecycle\'s initial state');[].forEach.call(document.querySelectorAll('.ke'),function(e){e.classList.remove('fire')});paint()});
if(log)paint();
/* the chips light up one after another, the way the platform's parts work together */
var ch=[].slice.call(document.querySelectorAll('.ochips span')),ci=0;if(ch.length&&!matchMedia('(prefers-reduced-motion: reduce)').matches)setInterval(function(){ch.forEach(function(c,j){c.classList.toggle('on',j===ci)});ci=(ci+1)%ch.length},900);
})();</script>"""


def atlas_svg():
    srcs = [("Maintenance ERP", "SAP PM"), ("Fleet management", "dispatch"), ("Collision avoidance", "CAS feed"), ("Video management", "VMS"), ("Spreadsheets", "permits.xlsx")]
    o = ['<text class="m" x="20" y="18">YOUR SYSTEMS</text><text class="m" x="250" y="18">ATLAS</text><text class="m" x="420" y="18">ONE SET OF OBJECTS</text>']
    for k, (a, b) in enumerate(srcs):
        y = 34 + k * 46
        o.append(f'<rect x="20" y="{y}" width="160" height="34" rx="4"/><text x="32" y="{y + 15}">{a}</text><text class="m" x="32" y="{y + 27}">{b.upper()}</text>'
                 f'<path class="w" d="M180,{y + 17} C215,{y + 17} 215,140 250,140"/>')
    o.append('<rect class="v" x="250" y="96" width="120" height="88" rx="8"/><text class="vt" x="310" y="134" text-anchor="middle">map · sync</text><text class="vt" x="310" y="152" text-anchor="middle">in place</text>')
    for k, n in enumerate(["Work Order", "Haul Truck", "Collision Alert", "Evidence Clip", "Work Permit"]):
        y = 34 + k * 46
        o.append(f'<path class="w" d="M370,140 C400,140 395,{y + 17} 420,{y + 17}"/><rect class="lv" x="420" y="{y}" width="150" height="34" rx="17"/><text x="495" y="{y + 21}" text-anchor="middle">{n}</text>')
    return f'<svg viewBox="0 0 590 270" role="img" aria-label="Atlas connects legacy systems in place to one set of objects">{"".join(o)}</svg>'


def studio_svg():
    agents = [("fault-to-work-order", "Maintenance Work Order", "+1.00"), ("critical-escalation", "Supervisor Alert", "new"), ("evidence-attach", "Evidence Clip", "new")]
    o = ['<rect x="0" y="0" width="590" height="28" rx="6" style="fill:#412356;stroke:#412356"/><text x="14" y="18" style="fill:#fff">Agentic Studio</text><text x="190" y="18" style="fill:rgba(255,255,255,.7)">Agents</text><text x="250" y="18" style="fill:rgba(255,255,255,.7)">Memory</text><text x="318" y="18" style="fill:rgba(255,255,255,.7)">Export</text>']
    for k, (n, ob, s) in enumerate(agents):
        y = 46 + k * 70
        o.append(f'<rect x="12" y="{y}" width="566" height="58" rx="8"/><circle class="g" cx="32" cy="{y + 20}" r="5"/><text x="46" y="{y + 24}" style="font-weight:600">{n}</text>'
                 f'<text class="m" x="46" y="{y + 44}">BOUND TO {ob.upper()}</text><rect class="lv" x="380" y="{y + 14}" width="104" height="28" rx="14"/><text x="432" y="{y + 32}" text-anchor="middle">memory on</text>'
                 f'<text x="560" y="{y + 33}" text-anchor="end" style="font-weight:600;fill:#5b2bff">{s}</text>')
    o.append('<text class="m" x="12" y="268">EACH RUN GRADED · LESSONS KEPT · EXPORTED WITH THE APP</text>')
    return f'<svg viewBox="0 0 590 280" role="img" aria-label="Agentic Studio: managed agents bound to ontology objects, each with memory">{"".join(o)}</svg>'


def depth_block(depth_html: str) -> str:
    return (f'<section class="odep"><div class="wrap3 dg"><aside><span class="eb">In depth</span><h2>How Hyper Ontology works</h2></aside>'
            f'<div class="doc">{depth_html}</div></div></section>')


def build(depth_html: str, faq_ld: dict) -> str:
    data = onto()
    objs = data["objects"]
    n_obj, n_link = len(objs), sum(len(o["links"]) for o in objs)
    n_syn = sum(len(o["syn"]) for o in objs)
    n_lc = sum(len(o["lifecycles"]) for o in objs)
    chips = ["Objects", "Properties", "Links", "Synonyms", "Lifecycles", "Transitions", "Functions", "Roles", "MCP tools", "Atlas sources", "Agents", "Export as code"]
    hero = ('<section class="oh">' + hero_svg() + '<div class="shade"></div><div class="hc">'
            f'<h1 class="wm" aria-label="Hyper Ontology"><svg viewBox="0 0 38 30" aria-hidden="true"><path d="{MARK}"/></svg><span>Ontology</span></h1>'
            '<div class="side"><p>Hyper Ontology<br><span class="dim">The digital twin of your organization</span></p>'
            '<p>One model of your operation that people and agents decide on, inside your walls</p>'
            f'<p class="dim">Exported as code you own</p><p class="lk"><a href="{DEV}">Start building →</a></p><p class="lk"><a href="{brand.COMMERCIAL}">{brand.TALK} →</a></p></div></div></section>')
    statement = ('<section class="ost"><div class="wrap3"><span class="eb">Hyper Ontology</span>'
                 '<p style="margin-top:22px"><em>Hyper Ontology</em> encodes the data, logic, actions and rules of your operation, so every person and every agent works on one reality.</p>'
                 '<p class="sub">Not a diagram on a wall. A running system: objects that mean the same thing in every application, state that only changes through governed transitions, and an endpoint every agent reads before it acts.</p></div></section>')
    living = ('<section class="opan"><div class="wrap3"><div class="pbox"><span class="eb">Overview</span><h2 class="big">Run your operation as <em>one living model.</em></h2>'
              '<p class="lead2" style="margin-left:auto;margin-right:auto">Your systems feed it from below. Analytics, workflows and agents act on it from above. What one of them changes, every other one sees.</p>'
              '<div class="scrollx">' + living_svg() + '</div><div class="olg"><span><i style="background:#5b2bff"></i>An agent or a person acted</span><span><i style="background:#e5484d"></i>Something drifted past its limit</span><span><i style="background:rgba(23,19,31,.3)"></i>Data moving</span></div></div></div></section>')
    model = ('<section class="opan" style="padding-top:0"><div class="wrap3"><div class="ohead"><span class="eb">Ontology language</span><h2 class="big">Model the parts of every <em>decision.</em></h2></div>'
             '<div class="ocards">'
             '<div class="ocard"><h3>Semantics: encode what everything means.</h3><p>Every object, property and link written down once, with the names the business really uses. A repair ticket and a service order resolve to the same Maintenance Work Order, for a person and for an agent.</p><a class="more" href="#explore">Explore the ontology</a></div>'
             '<div class="ocard"><h3>Kinetics: model how the operation moves.</h3><p>Lifecycles say which states a record can be in and which moves are allowed between them. The server enforces them: no screen, script or agent can skip a step.</p><a class="more" href="#kinetics">Move a work order</a></div>'
             '<div class="ocard"><h3>Functions: capture the logic.</h3><p>The numbers the operation runs on, computed in one place: insights, dashboard measures and statuses derived on read, each callable by name by any application or agent.</p><a class="more" href="' + DEV + '#functions">Read more</a></div>'
             '<div class="ocard"><h3>Governance: one rulebook for people and agents.</h3><p>Roles decide who sees which object, which property and which action. An agent sees exactly what its role allows, and nothing it was never granted.</p><a class="more" href="' + DEV + '#agents">Read more</a></div>'
             '</div><div class="pbox" style="margin-top:24px;padding:46px 20px"><div class="ochips">' + "".join(f"<span>{c}</span>" for c in chips) + '</div></div></div></section>')
    explore = (f'<section class="opan" id="explore" style="padding-top:0"><div class="wrap3"><div class="pbox"><span class="eb">Semantics</span><h2 class="big">One mine. <em>{n_obj} objects.</em> One meaning each.</h2>'
               f'<p class="lead2" style="margin-left:auto;margin-right:auto">This is the Mining GOLD Copper ontology, built in Hyper Studio: {n_obj} objects, {n_link} links and {n_syn} business synonyms across five domains. Click any object, or ask for it by the name your teams use.</p>'
               + explorer(data) + '</div></div></section>')
    kin = (f'<section class="opan" id="kinetics" style="padding-top:0"><div class="wrap3"><div class="pbox"><span class="eb">Kinetics</span><h2 class="big">State only moves the way <em>you allow.</em></h2>'
           '<p class="lead2" style="margin-left:auto;margin-right:auto">A maintenance work order can only be assigned when it is unassigned, and only completed when work is in progress. Try a move that breaks the rule. The platform refuses it, the same way it refuses an agent.</p>'
           + kinetics_box(data) + '</div></div></section>')
    engine = ('<section class="opan" style="padding-top:0"><div class="wrap3"><div class="ohead"><span class="eb">Ontology engine</span><h2 class="big"><em>Connect what you have.</em> Put agents to work on it.</h2></div>'
              '<div class="otwo"><div class="ofig"><h3><em>Atlas</em> connects the systems you already run.</h3>' + atlas_svg() +
              '<p>Maintenance, fleet, safety and video systems stay where they are. Atlas maps their records onto the ontology\'s objects and keeps them in step, so the model is the operation and not a copy of it.</p></div>'
              '<div class="ofig"><h3><em>Agentic Studio</em> runs the agents that work on it.</h3>' + studio_svg() +
              f'<p>Managed agents bound to objects, governed by the same roles and kinetics as people. Every run is graded and the agent keeps what it learned. They ship with your application, and they get better with every run, the way <a href="{BASE}/hyper-pragma/">Hyper Pragma</a> does.</p></div></div>'
              '<div class="ocards c3"><div class="ocard"><h3>One reality for every reader and writer.</h3><p>Applications, analytics and agents read and write the same objects, through the same rules, so a decision made in one place is true everywhere.</p></div>'
              '<div class="ocard"><h3>Inside your walls.</h3><p>The ontology, its data and its agents run where your data lives: on premises, in your private cloud or air gapped, on models you host yourself.</p></div>'
              '<div class="ocard"><h3>Yours to keep.</h3><p>Publish and the whole system exports as code: the ontology, its kinetics, its endpoint for agents and its applications. Nothing about your operation is locked in anyone else\'s cloud.</p></div></div></div></section>')
    code = ('<section class="opan" style="padding-top:0"><div class="wrap3"><div class="ocode"><div><span class="eb" style="color:rgba(255,255,255,.6)">Ontology toolchain</span>'
            '<h3 style="margin-top:14px">Treat your ontology <em>as a codebase.</em></h3><p>Every Hyper application exports its ontology as a typed manifest beside the code that enforces it. Your engineers review it, version it and run it like any other part of the stack.</p>'
            f'<a class="btn" href="{DEV}">Start building →</a></div>'
            '<pre><span class="c">// src/mcp/manifest.ts, generated by Hyper Studio</span>\n{\n  <span class="k">apiName</span>: <span class="s">"maintenance-work-order"</span>,\n  <span class="k">synonyms</span>: [<span class="s">"Repair Ticket"</span>, <span class="s">"Service Order"</span>],\n'
            '  <span class="k">semanticDomain</span>: <span class="s">"Operations and Maintenance"</span>,\n  <span class="k">links</span>: [{ <span class="k">to</span>: <span class="s">"haul-truck"</span>, <span class="k">phrase</span>: <span class="s">"belongs to"</span> }],\n'
            '  <span class="k">lifecycles</span>: [{\n    <span class="k">stateField</span>: <span class="s">"orderStatus"</span>,\n    <span class="k">transitions</span>: [{ <span class="k">label</span>: <span class="s">"Assign"</span>,\n      <span class="k">from</span>: [<span class="s">"unassigned"</span>], <span class="k">to</span>: <span class="s">"assigned"</span>,\n      <span class="k">tool</span>: <span class="s">"assignMaintenanceWorkOrder"</span> }]\n  }]\n}</pre></div></div></section>')
    cta = f'<section><div class="wrap3 octa"><a class="t" href="{brand.COMMERCIAL}">Talk to us <span>→</span></a><a class="s" href="{DEV}">Start Building <span>→</span></a></div></section>'
    body = f'<main class="og">{hero}{statement}{living}{model}{explore}{kin}{engine}{code}{cta}{depth_block(depth_html)}</main>'
    title = "Hyper Ontology: The Digital Twin of Your Organization, Exported as Code | CodeNinja Atoms"
    desc = "Hyper Ontology encodes the data, logic, actions and rules of an operation, so people and agents work on one reality inside their own walls. Semantics, kinetics, Atlas and Agentic Studio, exported as code you own."
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Ontology", "applicationCategory": "DeveloperApplication",
           "description": desc, "url": f"{BASE}/hyper-ontology/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "featureList": ["Semantics: objects, properties, typed links, synonyms", "Kinetics: lifecycles and governed transitions enforced on the server",
                           "Functions: insights and dashboard measures", "Atlas: legacy sources connected in place", "Agentic Studio: managed agents with memory",
                           "Ontology as code: generated manifest.ts and full source export", "MCP endpoint for agents"],
           "isRelatedTo": [{"@type": "SoftwareApplication", "name": "Hyper Pragma", "url": f"{BASE}/hyper-pragma/"}, {"@type": "WebPage", "name": "Hyper Ontology for developers", "url": DEV}]}, faq_ld]
    return shell(title, desc, f"{BASE}/hyper-ontology/", ld, CSS, body, JS)


def shell(title, desc, url, ld, css, body, js, extra_head=""):
    nav = brand.nav(BASE + "/")
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}">'
            '<meta name="codeninja:kind" content="product">' + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
            + f'{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{css}</style>{extra_head}</head><body>{brand.header(BASE + "/", nav)}{body}'
            f'<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is part of <a href="{brand.PARENT}">CodeNinja</a></span></div></footer>'
            f'{js}{brand.SCRIPT}</body></html>')
