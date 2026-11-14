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


def twin_svg():
    """The digital twin: the mine in plan view on the left, mirrored into its ontology on the right.
    Trucks run the haul road; what the site does flows across the mirror into the objects that mean it."""
    o = []
    W, H = 1440, 820
    # survey grid: crosses every 80 units, coordinates on the top edge
    for x in range(80, W, 80):
        for y in range(120, H, 80):
            o.append(f'<path class="gx" d="M{x - 4},{y} h8 M{x},{y - 4} v8"/>')
        o.append(f'<text class="gc" x="{x}" y="112" text-anchor="middle">E{4000 + x * 2}</text>')
    # pit contours
    cx, cy = 330, 330
    for k, r in enumerate(range(54, 300, 34)):
        pts = []
        for a in range(0, 361, 8):
            t = math.radians(a)
            rr = r * (1 + .07 * math.sin(3 * t + k * .4) + .045 * math.cos(5 * t - k * .3))
            pts.append(f"{cx + rr * math.cos(t):.1f},{cy + .66 * rr * math.sin(t):.1f}")
        o.append(f'<polygon class="ct{" ct2" if k % 3 == 2 else ""}" points="{" ".join(pts)}"/>')
    o.append(f'<text class="lb" x="{cx}" y="{cy + 6}" text-anchor="middle">PIT 3 · RL 1140</text>')
    road = "M330,352 C390,420 470,300 540,372 S600,500 650,520"
    o.append(f'<path class="road" d="{road}"/><path class="road2" d="{road}"/>')
    o.append('<text class="lb" x="560" y="330">HAUL ROAD</text>')
    # shovel at the pit face, crusher at the road's end, camera on the road, a person on foot
    o.append('<g class="gl"><rect x="300" y="362" width="26" height="14" rx="2"/><path d="M326,366 l16,-10 l8,6"/><text class="lb" x="262" y="396">SHOVEL 02</text></g>')
    o.append('<g class="gl"><rect x="648" y="508" width="40" height="30" rx="2"/><path d="M652,508 l8,-14 h20 l8,14"/><text class="lb" x="640" y="556">CRUSHER</text></g>')
    o.append('<g class="gl"><polygon class="cone" points="486,446 560,384 586,420"/><circle cx="486" cy="446" r="7"/><text class="lb" x="430" y="470">CAM 07</text></g>')
    o.append('<g class="gl"><circle cx="604" cy="430" r="4"/><path d="M604,434 v10 M598,438 h12 M604,444 l-5,8 M604,444 l5,8"/><text class="lb" x="616" y="446">PERSON</text></g>')
    for k in range(3):
        o.append(f'<g class="trk"><rect x="-11" y="-6" width="22" height="12" rx="2"/><rect class="cab" x="5" y="-6" width="6" height="12" rx="1"/>'
                 f'<animateMotion dur="15s" begin="{-k * 5}s" repeatCount="indefinite" rotate="auto" path="{road}"/></g>')
    o.append('<text class="lb hd" x="80" y="160">THE OPERATION</text>')
    # the mirror
    o.append('<path class="mir" d="M720,140 V640"/><text class="lb hd" x="736" y="160">THE TWIN · HYPER ONTOLOGY</text>')
    # the ontology side
    N = {"Shovel Loader": (900, 240), "Haul Truck": (1100, 220), "Person on Foot": (1300, 260), "Fixed Camera": (880, 380), "Interaction Event": (1100, 360),
         "Collision Alert": (1300, 410), "Evidence Clip": (1060, 460), "Crusher Dump Pocket": (900, 520), "Maintenance Work Order": (1250, 515)}
    E2 = [("Shovel Loader", "Interaction Event"), ("Haul Truck", "Interaction Event"), ("Person on Foot", "Interaction Event"), ("Interaction Event", "Collision Alert"),
          ("Interaction Event", "Evidence Clip"), ("Fixed Camera", "Evidence Clip"), ("Haul Truck", "Maintenance Work Order"), ("Fixed Camera", "Maintenance Work Order"), ("Haul Truck", "Crusher Dump Pocket")]
    for a, b in E2:
        (x1, y1), (x2, y2) = N[a], N[b]
        o.append(f'<path class="oe" d="M{x1},{y1} C{(x1 + x2) / 2},{y1} {(x1 + x2) / 2},{y2} {x2},{y2}"/>')
    # what the site does crosses the mirror
    feeds = [((340, 368), "Shovel Loader"), ((520, 360), "Haul Truck"), ((604, 430), "Person on Foot"), ((486, 446), "Fixed Camera"), ((668, 522), "Crusher Dump Pocket")]
    for k, ((x, y), n) in enumerate(feeds):
        tx, ty = N[n]
        d = f"M{x},{y} C{x + 160},{y - 40} {tx - 200},{ty} {tx - 96},{ty}"
        o.append(f'<path class="feed" d="{d}"/><circle class="pk" r="3"><animateMotion dur="{3.2 + k * .45:.2f}s" begin="{k * .6:.1f}s" repeatCount="indefinite" path="{d}"/></circle>')
    for k, (n, (x, y)) in enumerate(N.items()):
        w = max(150, len(n) * 8 + 40)
        hot = " hot" if n in ("Interaction Event", "Collision Alert") else ""
        o.append(f'<g class="on{hot}" style="animation-delay:{k * .4:.1f}s"><rect x="{x - w / 2}" y="{y - 17}" width="{w}" height="34" rx="6"/>'
                 f'<circle cx="{x - w / 2 + 16}" cy="{y}" r="4"/><text x="{x - w / 2 + 28}" y="{y + 4.5}">{E(n)}</text></g>')
    return (f'<svg class="twin" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMin slice" role="img" '
            f'aria-label="A digital twin: a mine in plan view, with haul trucks on the road, mirrored into the ontology objects that describe it">{"".join(o)}</svg>')


def glyph(kind):
    g = {"sem": '<rect x="6" y="10" width="40" height="28" rx="4"/><path d="M12,20 h20 M12,27 h14"/><rect class="v" x="34" y="4" width="22" height="10" rx="5"/><rect class="v" x="40" y="34" width="20" height="10" rx="5"/>',
         "kin": '<circle cx="10" cy="24" r="7"/><circle cx="32" cy="24" r="7"/><circle class="v" cx="54" cy="24" r="7"/><path d="M17,24 h8 M39,24 h8"/>',
         "fun": '<path d="M6,40 h54 M6,40 V6"/><rect class="v" x="12" y="26" width="8" height="14"/><rect class="v" x="26" y="16" width="8" height="24"/><rect class="v" x="40" y="22" width="8" height="18"/>',
         "gov": '<path d="M32,4 l22,8 v12 c0,12 -10,20 -22,24 c-12,-4 -22,-12 -22,-24 v-12 z"/><path class="vs" d="M22,26 l7,7 l13,-14"/>'}[kind]
    return f'<svg class="gly" viewBox="0 0 64 50" aria-hidden="true">{g}</svg>'


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


TYPE_CSS = r"""
html.js [data-type] .tc{opacity:0}html.js [data-type] .tc.v,[data-type] .tc.v{opacity:1;transition:opacity .14s}[data-type] .tw{display:inline-block;white-space:nowrap}
.tcu{display:inline-block;width:.07em;height:.86em;margin-left:.05em;vertical-align:-.04em;background:currentColor;animation:tblink .7s steps(2) infinite}
@keyframes tblink{50%{opacity:0}}
[data-type] em{font-style:normal;background:linear-gradient(currentColor,currentColor) 0 96%/0 .06em no-repeat;transition:background-size .8s cubic-bezier(.3,.7,.2,1) .1s}[data-type].done em{background-size:100% .06em}
html.js [data-after]{opacity:0;transform:translateY(10px);transition:opacity .6s,transform .6s}html.js [data-after].in{opacity:1;transform:none}
"""

TYPE_JS = r"""<script>(function(){var still=matchMedia('(prefers-reduced-motion: reduce)').matches;
/* headings type themselves in, a caret riding the last letter; highlighted words are underlined once typed; the text under them follows */
function split(h){h.setAttribute('aria-label',h.textContent);(function walk(n){[].slice.call(n.childNodes).forEach(function(c){
 if(c.nodeType===3){var f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(document.createTextNode(w));return}
  var ws=document.createElement('span');ws.className='tw';ws.setAttribute('aria-hidden','true');w.split('').forEach(function(ch){var s=document.createElement('span');s.className='tc';s.textContent=ch;ws.appendChild(s)});f.appendChild(ws)});c.parentNode.replaceChild(f,c)}
 else if(c.nodeType===1)walk(c)})})(h)}
var hs=[].slice.call(document.querySelectorAll('[data-type]'));hs.forEach(split);
function after(h){var sec=h.closest('section')||document;[].forEach.call(sec.querySelectorAll('[data-after]'),function(e,i){setTimeout(function(){e.classList.add('in')},i*140)})}
function run(h){if(h._r)return;h._r=1;var cs=[].slice.call(h.querySelectorAll('.tc'));if(still){cs.forEach(function(c){c.classList.add('v')});h.classList.add('done');after(h);return}
 var cu=document.createElement('i');cu.className='tcu';cu.setAttribute('aria-hidden','true');var i=0,sp=cs.length>60?3:2;
 (function tick(){var n=Math.min(cs.length,i+sp);for(;i<n;i++)cs[i].classList.add('v');var last=cs[i-1];if(last&&last.parentNode)last.parentNode.insertBefore(cu,last.nextSibling);
  if(i<cs.length)setTimeout(tick,32);else{h.classList.add('done');after(h);setTimeout(function(){cu.remove()},900)}})()}
if(!('IntersectionObserver' in window)){hs.forEach(run);return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io.unobserve(e.target)}})},{threshold:0,rootMargin:'0px 0px -18% 0px'});hs.forEach(function(h){io.observe(h)})})();</script>"""

CSS = r"""
.og{--plum:#120b1c;--vi:#5b2bff;--vi2:#a48fff;--ink:#17131f;--mut:#5f5873;--rl:rgba(23,19,31,.13);--paper:#fbfaf7;background:#f1efe9;color:var(--ink)}
.og a{color:inherit}.og .wrap3{max-width:1240px;margin:0 auto;padding:0 clamp(16px,3vw,40px)}
/* section index, the way a drawing set is indexed */
.og .sx{display:flex;align-items:center;gap:12px;font:500 11.5px var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}.og .sx b{font-weight:500;color:var(--vi)}.og .sx::after{content:"";flex:0 0 64px;height:1px;background:currentColor;opacity:.5}
.og .hh{display:grid;grid-template-columns:1.25fr 1fr;gap:40px;align-items:end;margin-bottom:34px}
.og h2.big{font:300 clamp(34px,4.3vw,62px)/1.05 var(--sans);letter-spacing:-.035em;margin:18px 0 0;max-width:17ch}.og h2.big em{color:var(--vi)}
.og .lead2{font:300 clamp(17px,1.4vw,20px)/1.55 var(--sans);color:var(--mut);margin:0;max-width:46ch}
/* hero: the digital twin */
.oh{position:relative;overflow:hidden;min-height:100vh;background:radial-gradient(50% 60% at 78% 40%,rgba(91,43,255,.22),rgba(18,11,28,0) 70%),radial-gradient(40% 50% at 22% 36%,rgba(164,143,255,.10),rgba(18,11,28,0) 70%),var(--plum);color:#fff;display:flex;flex-direction:column;justify-content:flex-end}
.oh .twin{position:absolute;left:0;top:0;width:100%;height:100%}
.twin .gx{stroke:rgba(200,185,255,.22);stroke-width:1}.twin .gc{font:400 9px var(--mono);fill:rgba(200,185,255,.35);letter-spacing:.06em}
.twin .ct{fill:none;stroke:rgba(169,139,255,.28);stroke-width:1}.twin .ct2{stroke:rgba(169,139,255,.5)}
.twin .road{fill:none;stroke:rgba(255,255,255,.18);stroke-width:12;stroke-linecap:round}.twin .road2{fill:none;stroke:rgba(255,255,255,.55);stroke-width:1;stroke-dasharray:6 6}
.twin .lb{font:500 10px var(--mono);fill:rgba(225,215,255,.7);letter-spacing:.12em}.twin .hd{fill:#fff;font-size:11px;letter-spacing:.18em}
.twin .gl rect,.twin .gl path,.twin .gl circle{fill:none;stroke:#e9e4ff;stroke-width:1.3}.twin .cone{fill:rgba(164,143,255,.16)!important;stroke:rgba(164,143,255,.5)!important;animation:ocone 3s ease-in-out infinite}
.twin .trk rect{fill:#ffd166;stroke:#120b1c;stroke-width:1}.twin .trk .cab{fill:#fff}
.twin .mir{stroke:rgba(255,255,255,.45);stroke-dasharray:2 6}
.twin .oe{fill:none;stroke:rgba(190,170,255,.4);stroke-width:1.2}.twin .feed{fill:none;stroke:rgba(255,209,102,.28);stroke-dasharray:3 5}.twin .pk{fill:#ffd166}
.twin .on rect{fill:rgba(255,255,255,.05);stroke:rgba(200,185,255,.55)}.twin .on circle{fill:#a48fff}.twin .on text{font:500 13px var(--sans);fill:#fff}
.twin .on.hot rect{animation:ohot 7s ease-in-out infinite}.twin .on.hot circle{fill:#ffd166}
@keyframes ohot{0%,62%,100%{fill:rgba(255,255,255,.05);stroke:rgba(200,185,255,.55)}70%,84%{fill:rgba(91,43,255,.75);stroke:#c8b9ff}}
@keyframes ocone{50%{opacity:.55}}
.oh .hc{position:relative;display:flex;justify-content:space-between;align-items:flex-end;gap:30px;padding:0 clamp(16px,3vw,44px) clamp(20px,3.2vw,44px)}
.oh .wm{display:flex;align-items:center;gap:clamp(12px,1.5vw,24px);margin:0;font:300 clamp(70px,12.5vw,214px)/.8 var(--sans);letter-spacing:-.06em}.oh .wtag{margin:clamp(12px,1.4vw,20px) 0 0 .2em;font:400 clamp(14px,1.2vw,18px)/1.4 var(--sans);letter-spacing:.005em;color:rgba(255,255,255,.72)}.oh .wm svg{height:.64em;width:auto;fill:#fff}
.oh .tblk{display:grid;grid-template-columns:auto auto;border:1px solid rgba(255,255,255,.4);font:400 10.5px/1.35 var(--mono);letter-spacing:.08em;text-transform:uppercase;min-width:330px;margin-bottom:8px;background:rgba(18,11,28,.55)}
.oh .tblk>*{padding:8px 11px;border-bottom:1px solid rgba(255,255,255,.25)}.oh .tblk>:nth-child(odd){border-right:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.5)}.oh .tblk>:nth-last-child(-n+2){border-bottom:0}
.oh .tblk a{text-decoration:none;color:#fff}.oh .tblk a:hover{color:#ffd166}.oh .tblk .acts{grid-column:1/-1;display:grid;grid-template-columns:1fr 1fr;padding:0;border-right:0!important;color:#fff!important}.oh .tblk .acts a{padding:11px;text-align:center}.oh .tblk .acts a+a{border-left:1px solid rgba(255,255,255,.25);background:#fff;color:var(--plum)}
.oh .shade{position:absolute;inset:0;pointer-events:none;background:linear-gradient(0deg,rgba(18,11,28,.95) 0,rgba(18,11,28,.35) 30%,rgba(18,11,28,0) 46%)}
/* statement */
.ost{background:var(--paper);padding:clamp(90px,12vw,170px) 0;border-bottom:1px solid var(--rl)}.ost .wrap3{display:grid;grid-template-columns:200px 1fr;gap:40px}
.ost p.st{font:300 clamp(30px,3.8vw,56px)/1.12 var(--sans);letter-spacing:-.03em;margin:0;max-width:22ch}.ost p.st em{color:var(--vi)}
.ost .sub{font:300 clamp(17px,1.4vw,20px)/1.55 var(--sans);color:var(--mut);max-width:56ch;margin:26px 0 0}
/* drawing sheets */
.osec{padding:clamp(56px,6vw,90px) 0 0}
.sheet{position:relative;background:var(--paper);border:1px solid rgba(23,19,31,.5);padding:clamp(28px,4vw,54px) clamp(16px,3.4vw,48px) 70px;
 background-image:linear-gradient(rgba(91,43,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(91,43,255,.045) 1px,transparent 1px);background-size:24px 24px}
.sheet::before,.sheet::after{content:"";position:absolute;width:18px;height:18px;border:2px solid var(--ink)}.sheet::before{left:-6px;top:-6px;border-right:0;border-bottom:0}.sheet::after{right:-6px;bottom:-6px;border-left:0;border-top:0}
.sheet .tb{position:absolute;right:0;bottom:0;display:flex;border-top:1px solid rgba(23,19,31,.5);border-left:1px solid rgba(23,19,31,.5);font:500 10px var(--mono);letter-spacing:.12em;text-transform:uppercase;background:var(--paper)}
.sheet .tb span{padding:8px 12px;border-right:1px solid rgba(23,19,31,.25)}.sheet .tb span:last-child{border-right:0;color:var(--vi)}
.living{width:100%;height:auto;margin-top:10px}
.living text{font:400 12px var(--sans);fill:var(--ink)}.living .h{font:600 14px var(--sans)}.living .s{font:400 11px var(--sans);fill:var(--mut)}
.living .mon rect,.living .mon path{fill:#fff;stroke:var(--ink);stroke-width:1.2}.living .mon .sc{fill:#fbfaff;stroke:rgba(23,19,31,.3)}
.living .spark{fill:none;stroke:#e5484d;stroke-width:2}.living .lim{stroke:#e5484d;stroke-dasharray:4 4}
.living .wf rect{fill:#fff;stroke:var(--ink)}.living .wf .pu{fill:var(--vi);stroke:var(--vi)}.living .wf .w{fill:#fff}.living .wf path{stroke:var(--ink);fill:none}.living .wf text{font-size:11px}
.living .ag{fill:#fff;stroke:rgba(23,19,31,.25)}.living text.s.r{font-weight:600;fill:#e5484d}
.living .plane{fill:rgba(255,255,255,.75);stroke:var(--ink);stroke-width:1.3}.living .pedge{fill:rgba(23,19,31,.1);stroke:var(--ink)}
.living .e{stroke:rgba(23,19,31,.18);stroke-width:1.2}.living .e.hot{stroke:var(--vi);stroke-width:1.8}
.living .el rect{fill:#ebe6ff;stroke:rgba(91,43,255,.35)}.living .el text{font:500 10px var(--sans);fill:var(--vi)}
.living .on ellipse{fill:#ebe6ff;stroke:rgba(91,43,255,.4)}.living .on path,.living .on rect,.living .on circle{fill:#fff;stroke:var(--ink);stroke-width:1.1}.living .on text{font-size:11.5px}
.living .base rect,.living .base path,.living .base polyline{fill:#fff;stroke:var(--ink);stroke-width:1.1}.living .base polyline{fill:none}.living .base text{font-size:11px}
.living .wire{fill:none;stroke:rgba(23,19,31,.28);stroke-dasharray:2 4}.living .pk2{fill:var(--vi)}
.olg{display:flex;flex-wrap:wrap;gap:22px;margin-top:14px;font:400 12.5px var(--sans);color:var(--mut)}.olg i{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:7px}
/* spec sheets */
.specs{display:grid;grid-template-columns:repeat(4,1fr);border-top:2px solid var(--ink);border-bottom:1px solid var(--rl)}
.spec{padding:22px 20px 24px;border-right:1px solid var(--rl);display:flex;flex-direction:column;gap:10px;position:relative;transition:background .3s}.spec:last-child{border-right:0}.spec:hover{background:#fff}
.spec .no{font:500 11px var(--mono);color:var(--mut);letter-spacing:.1em}.spec .ct2{position:absolute;right:18px;top:18px;font:500 11px var(--mono);color:var(--vi);background:#ebe6ff;padding:3px 8px;border-radius:99px}
.spec h3{font:400 22px/1.2 var(--sans);letter-spacing:-.015em;margin:4px 0 0}.spec p{margin:0;color:var(--mut);font:400 15px/1.55 var(--sans)}.spec a{margin-top:auto;font:500 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;text-decoration:none;color:var(--vi)}
.gly{width:64px;height:50px}.gly rect,.gly circle,.gly path{fill:none;stroke:var(--ink);stroke-width:1.5}.gly .v{fill:#ebe6ff;stroke:var(--vi)}.gly .vs{stroke:var(--vi);stroke-width:2.2}
/* bill of materials */
.bom{width:100%;border-collapse:collapse;margin-top:30px;font:400 14.5px var(--sans);background:var(--paper)}.bom th{text-align:left;font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut);padding:10px 12px;border-bottom:2px solid var(--ink)}
.bom td{padding:12px;border-bottom:1px solid var(--rl)}.bom td.q{font:500 22px var(--sans);color:var(--vi);font-variant-numeric:tabular-nums;width:90px}.bom td.f{font:400 12.5px var(--mono);color:var(--mut)}.bom td.i{font:500 12px var(--mono);color:var(--mut);width:46px}
.bom tr{transition:background .25s}.bom tr:hover{background:#fff}
/* explorer */
.xbox{display:grid;grid-template-columns:1fr 360px;background:#fff;overflow:hidden;margin-top:10px;border:1px solid rgba(23,19,31,.35)}
.xmap{padding:22px 22px 14px;border-right:1px solid var(--rl);min-width:0}.xq label{display:block;font:500 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--mut);margin-bottom:8px}
.xq input{width:100%;font:400 16px var(--sans);padding:12px 14px;border:1px solid var(--rl);border-radius:2px;background:var(--paper);color:var(--ink)}.xq input:focus{outline:2px solid var(--vi);outline-offset:0}
.xq p{min-height:20px;margin:8px 0 0;font:400 13px var(--sans);color:var(--vi)}
.xsvg{width:100%;height:auto;margin-top:6px}.xh{font:500 10px var(--mono);letter-spacing:.12em;fill:var(--mut)}
.xe{fill:none;stroke:rgba(23,19,31,.13);stroke-width:1.2;transition:stroke .3s,stroke-width .3s}.xe.on{stroke:var(--vi);stroke-width:2.2}
.xn{cursor:pointer}.xn rect{fill:#fff;stroke:rgba(23,19,31,.3);transition:fill .25s,stroke .25s}.xn text{font:500 13px var(--sans);fill:var(--ink);pointer-events:none}
.xn.lc rect{stroke:var(--vi);stroke-width:1.5}.xn:hover rect,.xn:focus rect{stroke:var(--vi);outline:none}.xn.nb rect{fill:#efeaff}.xn.sel rect{fill:var(--vi);stroke:var(--vi)}.xn.sel text{fill:#fff}.xn.dim text{opacity:.4}.xn.dim rect{stroke-opacity:.35}
.xleg{display:flex;gap:18px;font:400 12px var(--sans);color:var(--mut);margin:4px 0 0}.xleg i{display:inline-block;width:16px;height:10px;border-radius:5px;margin-right:6px;vertical-align:-1px;border:1.5px solid var(--vi)}.xleg i.b{background:#efeaff;border-color:rgba(23,19,31,.3)}
.xd{padding:24px 22px;background:var(--paper);font:400 14px/1.5 var(--sans);overflow:auto;max-height:640px}
.xd h4{font:500 22px/1.2 var(--sans);margin:0 0 4px;letter-spacing:-.01em}.xd .dm{font:500 10.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--vi)}.xd p{color:var(--mut);margin:10px 0 0}
.xd h5{font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin:20px 0 8px;padding-top:14px;border-top:1px solid var(--rl)}
.xd .sy{display:flex;flex-wrap:wrap;gap:6px}.xd .sy span{padding:4px 10px;border-radius:99px;background:#ebe6ff;color:var(--vi);font-size:12.5px}
.xd ul{list-style:none;margin:0;padding:0}.xd li{display:flex;justify-content:space-between;gap:12px;padding:5px 0;border-bottom:1px dashed var(--rl);font-size:13px}.xd li code{font:400 12px var(--mono);color:var(--ink)}.xd li span{color:var(--mut);font:400 11.5px var(--mono)}
.xd li a{color:var(--vi);text-decoration:none;cursor:pointer}
/* kinetics */
.kbox{display:grid;grid-template-columns:1.25fr 1fr;background:#fff;overflow:hidden;border:1px solid rgba(23,19,31,.35);margin-top:10px}
.kl{border-right:1px solid var(--rl)}.kh{display:flex;gap:10px;align-items:baseline;padding:14px 18px;background:#412356;color:#fff;font:400 13px var(--sans)}.kh span{color:rgba(255,255,255,.65);font:400 12px var(--mono)}
.ksvg{width:100%;height:auto;display:block;padding:10px;background-image:radial-gradient(rgba(23,19,31,.12) 1px,transparent 1px);background-size:16px 16px}
.ks rect{fill:#fff;stroke:rgba(23,19,31,.4);stroke-width:1.2;transition:fill .3s,stroke .3s}.ks.init rect{stroke:var(--vi);stroke-width:2}.ks.term rect{stroke-width:2}.ks text{font:500 13px var(--mono);fill:var(--ink)}
.ks.cur rect{fill:var(--vi);stroke:var(--vi)}.ks.cur text{fill:#fff}
.ke{fill:none;stroke:rgba(23,19,31,.3);stroke-width:1.2;transition:stroke .3s}.ke.fire{stroke:var(--vi);stroke-width:2.4}#ar path{fill:rgba(23,19,31,.45)}#ktok{display:none}
.kr{padding:22px}.kk{margin:0 0 12px;font:400 15px var(--sans)}.kbs{display:flex;flex-wrap:wrap;gap:8px}
.kb{font:500 13px var(--sans);padding:9px 14px;border-radius:2px;border:1px solid rgba(23,19,31,.25);background:#fff;color:var(--ink);cursor:pointer;transition:background .2s,border-color .2s}.kb:hover{border-color:var(--vi)}
.kb.ok{background:#ebe6ff;border-color:var(--vi)}.kb.raw{margin-top:10px;border-style:dashed}.kb.rs{margin:10px 0 0 8px;color:var(--mut)}
.klog{list-style:none;margin:16px 0 0;padding:0;font:400 12.5px/1.45 var(--mono);max-height:260px;overflow:auto}.klog li{padding:8px 10px;margin-bottom:6px;background:#f5f3fb}
.klog li.ok{border-left:3px solid #0f8a5f}.klog li.no{border-left:3px solid #e5484d;background:#fff4f4}.klog li.lock{border-left:3px solid #b0740f;background:#fffaf0}
/* atlas and agentic studio */
.otwo{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid rgba(23,19,31,.35);background:#fff}.ofig{padding:26px;display:flex;flex-direction:column}.ofig+.ofig{border-left:1px solid var(--rl)}
.ofig svg{width:100%;height:auto;margin:6px 0 18px}.ofig h3{font:400 24px/1.2 var(--sans);letter-spacing:-.02em;margin:0 0 8px}.ofig h3 em{font-style:normal;color:var(--vi)}.ofig p{margin:0;color:var(--mut);font:400 15px/1.55 var(--sans)}
.ofig svg text{font:400 11px var(--sans);fill:var(--ink)}.ofig svg .m{font:500 9.5px var(--mono);letter-spacing:.1em;fill:var(--mut)}
.ofig svg rect,.ofig svg path,.ofig svg circle{fill:#fff;stroke:var(--ink);stroke-width:1.1}.ofig svg .v{fill:var(--vi);stroke:var(--vi)}.ofig svg .vt{fill:#fff}.ofig svg .w{fill:none;stroke:rgba(23,19,31,.3);stroke-dasharray:2 4}
.ofig svg .lv{fill:#ebe6ff;stroke:rgba(91,43,255,.45)}.ofig svg .g{fill:#0f8a5f;stroke:none}
.engine{display:grid;grid-template-columns:repeat(3,1fr);margin-top:24px;border-top:2px solid var(--ink)}.engine div{padding:22px 22px 0 0}.engine div+div{padding-left:22px;border-left:1px solid var(--rl)}
.engine h3{font:400 21px/1.25 var(--sans);margin:0 0 8px}.engine h3 b{display:block;font:500 11px var(--mono);color:var(--vi);letter-spacing:.1em;margin-bottom:8px}.engine p{margin:0;color:var(--mut);font:400 15px/1.55 var(--sans)}
/* code teaser */
.ocode{display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:center;background:var(--plum);color:#fff;padding:clamp(30px,5vw,64px)}
.ocode h3{font:300 clamp(28px,3vw,42px)/1.1 var(--sans);letter-spacing:-.03em;margin:14px 0 16px}.ocode h3 em{color:var(--vi2)}.ocode p{color:rgba(255,255,255,.72);font:400 16px/1.55 var(--sans);margin:0 0 12px}
.ocode .sx{color:rgba(255,255,255,.6)}.ocode .sx b{color:var(--vi2)}
.ocode pre{margin:0;background:#0b0712;border:1px solid rgba(255,255,255,.12);padding:18px 20px;overflow:auto;font:400 12.5px/1.6 var(--mono);color:#e9e4ff}
.ocode .k{color:#b69cff}.ocode .s{color:#7ee2b8}.ocode .c{color:#8a809f}.ocode a.btn{display:inline-block;margin-top:10px;background:#ffd166;color:var(--ink);text-decoration:none;font:500 14px var(--sans);padding:12px 18px}
/* the closing title block */
.octa{margin:clamp(56px,6vw,90px) auto 90px;display:grid;grid-template-columns:1fr 1fr 1.2fr 1.2fr;border:1.5px solid var(--ink);background:var(--paper)}
.octa>div{padding:16px 18px;border-right:1px solid var(--rl);font:500 10.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}.octa>div b{display:block;margin-top:8px;font:400 18px var(--sans);letter-spacing:0;text-transform:none;color:var(--ink)}
.octa a{display:flex;justify-content:space-between;align-items:flex-end;min-height:130px;padding:18px 20px;text-decoration:none;font:300 clamp(28px,2.8vw,40px)/1 var(--sans);letter-spacing:-.03em;transition:background .25s}
.octa a.t{color:var(--ink)}.octa a.t:hover{background:#fff}.octa a.s{background:var(--ink);color:#fff}.octa a.s:hover{background:var(--vi)}
/* in depth */
.odep{background:var(--paper);border-top:1px solid var(--rl);padding:90px 0 110px}.odep .dg{display:grid;grid-template-columns:280px 1fr;gap:60px}.odep .doc{font:400 17px/1.65 var(--sans);color:#2a2533;max-width:760px}
.odep .doc h1{display:none}.odep .doc h2{max-width:none;font:400 28px/1.2 var(--sans);letter-spacing:-.02em;margin:46px 0 14px;color:var(--ink)}.odep .doc table{width:100%;border-collapse:collapse;font-size:15px}.odep .doc td,.odep .doc th{border-bottom:1px solid var(--rl);padding:10px 8px;text-align:left;vertical-align:top}
.odep .doc .eyebrow{display:none}.odep .doc .box{background:#fff;border:1px solid var(--rl);padding:16px 18px}.odep .doc a{color:var(--vi)}
.odep aside{position:sticky;top:110px;align-self:start}.odep aside h2{font:300 34px/1.05 var(--sans);letter-spacing:-.03em;margin:14px 0 0}
@media (max-width:1000px){.xbox,.kbox,.ocode,.otwo,.og .hh,.ost .wrap3{grid-template-columns:1fr}.ofig+.ofig{border-left:0;border-top:1px solid var(--rl)}.xmap,.kl{border-right:0;border-bottom:1px solid var(--rl)}.specs{grid-template-columns:1fr 1fr}.spec:nth-child(2){border-right:0}.engine{grid-template-columns:1fr}.engine div+div{padding-left:0;border-left:0;border-top:1px solid var(--rl)}.odep .dg{grid-template-columns:1fr}.odep aside{position:static}.octa{grid-template-columns:1fr 1fr}}
@media (max-width:760px){.specs,.octa{grid-template-columns:1fr}.spec{border-right:0;border-bottom:1px solid var(--rl)}.oh .twin{width:200%;left:-8%}.oh .hc{flex-direction:column;align-items:flex-start}.oh .tblk{min-width:0;width:100%}.living{min-width:760px}.scrollx{overflow-x:auto}.sheet .tb span:nth-child(2){display:none}.bom td.f{display:none}}
@media (prefers-reduced-motion:reduce){.twin *,.living *{animation:none!important}}
""" + TYPE_CSS

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
/* the bill of materials counts itself up when it comes into view */
var bom=document.querySelector('.bom');if(bom&&'IntersectionObserver' in window){var bo=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;bo.disconnect();
 [].forEach.call(bom.querySelectorAll('td.q'),function(td,k){var n=+td.getAttribute('data-n'),t0=performance.now()+k*90;td.textContent='0';(function f(t){var p=Math.min(1,Math.max(0,(t-t0)/900));td.textContent=Math.round(n*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(t0)})},{threshold:.3});bo.observe(bom)}
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
    return (f'<section class="odep"><div class="wrap3 dg"><aside>{sx(7, "In depth")}<h2 data-type>How Hyper Ontology works</h2></aside>'
            f'<div class="doc">{depth_html}</div></div></section>')


def sx(n, label):
    return f'<span class="sx"><b>§{n:02d}</b>{E(label)}</span>'


def sheet(inner, no, title):
    return f'<div class="sheet">{inner}<div class="tb"><span>Sheet {no:02d}</span><span>{E(title)}</span><span>Mining GOLD Copper</span></div></div>'


def head(n, label, h2, lead):
    return f'<div class="hh"><div>{sx(n, label)}<h2 class="big" data-type>{h2}</h2></div><p class="lead2" data-after>{lead}</p></div>'


def build(depth_html: str, faq_ld: dict) -> str:
    data = onto()
    objs = data["objects"]
    n_obj, n_link = len(objs), sum(len(o["links"]) for o in objs)
    n_syn = sum(len(o["syn"]) for o in objs)
    n_prop = sum(len(o["props"]) for o in objs)
    n_lc = sum(len(o["lifecycles"]) for o in objs)
    n_tr = sum(len(l["transitions"]) for o in objs for l in o["lifecycles"])
    n_fn = sum(len(o["functions"]) for o in objs)
    hero = ('<section class="oh">' + twin_svg() + '<div class="shade"></div><div class="hc">'
            f'<div class="wmb"><h1 class="wm" aria-label="Hyper Ontology"><svg viewBox="0 0 38 30" aria-hidden="true"><path d="{MARK}"/></svg><span>Ontology</span></h1><p class="wtag">Dedicated inference for your sovereign AI models.</p></div>'
            '<div class="tblk"><span>Product</span><span>Hyper Ontology</span><span>Drawing</span><span>The digital twin of your organization</span>'
            '<span>Runs</span><span>Inside your walls</span><span>Delivered</span><span>As code you own</span>'
            f'<div class="acts"><a href="{brand.COMMERCIAL}">{brand.TALK} →</a><a href="{DEV}">Start building →</a></div></div></div></section>')
    statement = ('<section class="ost"><div class="wrap3"><div>' + sx(0, "The idea") + '</div><div>'
                 '<p class="st" data-type>Every operation already has a twin. It is scattered across a dozen systems and a hundred heads. <em>Hyper Ontology</em> writes it down once.</p>'
                 '<p class="sub" data-after>The data, the logic, the actions and the rules of your operation, in one model that people and agents decide on. Not a diagram on a wall: a running system, exported as code you own.</p></div></div></section>')
    living = ('<section class="osec"><div class="wrap3">' + head(1, "Overview", "Run your operation as <em>one living model.</em>",
              "Your systems feed it from below. Analytics, workflows and agents act on it from above. What one of them changes, every other one sees.")
              + sheet('<div class="scrollx">' + living_svg() + '</div><div class="olg"><span><i style="background:#5b2bff"></i>An agent or a person acted</span><span><i style="background:#e5484d"></i>Something drifted past its limit</span><span><i style="background:rgba(23,19,31,.3)"></i>Data moving</span></div>', 1, "Living ontology")
              + '</div></section>')
    specs = [("01", "sem", f"{n_syn} synonyms", "Semantics", "Every object, property and link written down once, in the words the business uses. A repair ticket and a service order resolve to the same Maintenance Work Order, for a person and for an agent.", "#explore", "Explore the objects"),
             ("02", "kin", f"{n_tr} transitions", "Kinetics", "Lifecycles say which states a record can be in and which moves are allowed. The server enforces them: no screen, script or agent can skip a step.", "#kinetics", "Move a work order"),
             ("03", "fun", f"{n_fn} functions", "Functions", "The numbers the operation runs on, computed in one place and callable by name by any application or agent.", DEV + "#functions", "Read the docs"),
             ("04", "gov", "4 agent tools", "Governance", "Roles decide who sees which object, property and action. An agent sees exactly what its role allows, through four tools, and nothing it was never granted.", DEV + "#agents", "Read the docs")]
    spec_html = '<div class="specs">' + "".join(f'<div class="spec"><span class="no">{no}</span><span class="ct2">{E(c)}</span>{glyph(g)}<h3>{h}</h3><p>{E(t)}</p><a href="{u}">{a} →</a></div>' for no, g, c, h, t, u, a in specs) + "</div>"
    bom_rows = [("Objects", n_obj, "src/mcp/manifest.ts"), ("Properties", n_prop, "src/models/*.ts"), ("Typed links", n_link, "manifest.ts · links"),
                ("Business synonyms", n_syn, "manifest.ts · synonyms"), ("Lifecycles", n_lc, "src/kinetics/*.ts"), ("Governed transitions", n_tr, "src/kinetics/*.ts"),
                ("Functions", n_fn, "manifest.ts · functions"), ("Agent meta tools", 4, "src/mcp/gateway.ts")]
    bom = ('<table class="bom"><thead><tr><th>Item</th><th>Part</th><th>Qty</th><th>Where it lives in your repository</th></tr></thead><tbody>'
           + "".join(f'<tr><td class="i">{k + 1:02d}</td><td>{E(a)}</td><td class="q" data-n="{b}">{b}</td><td class="f">{E(c)}</td></tr>' for k, (a, b, c) in enumerate(bom_rows)) + "</tbody></table>")
    model = ('<section class="osec"><div class="wrap3">' + head(2, "Ontology language", "Model every part of <em>a decision.</em>",
             "Four layers, each one a part you can point at in your own code. Below is the bill of materials of one real ontology, counted from its export.")
             + spec_html + bom + '</div></section>')
    explore = ('<section class="osec" id="explore"><div class="wrap3">' + head(3, "Semantics", f"One mine. {n_obj} objects. <em>One meaning each.</em>",
               f"The Mining GOLD Copper ontology, built in Hyper Studio: {n_obj} objects, {n_link} links and {n_syn} business synonyms across five domains. Click an object, or ask for it by the name your teams use.")
               + sheet(explorer(data), 3, "Semantics") + '</div></section>')
    kin = ('<section class="osec" id="kinetics"><div class="wrap3">' + head(4, "Kinetics", "State only moves <em>the way you allow.</em>",
           "A work order can only be assigned while it is unassigned, and only completed while work is in progress. Try a move that breaks the rule: the platform refuses it, the same way it refuses an agent.")
           + sheet(kinetics_box(data), 4, "Kinetics") + '</div></section>')
    engine = ('<section class="osec"><div class="wrap3">' + head(5, "Ontology engine", "Connect what you have. <em>Put agents to work on it.</em>",
              "Atlas brings the systems you already run onto the ontology. Agentic Studio runs the agents that work on it. Both export with your application.")
              + '<div class="otwo"><div class="ofig"><h3><em>Atlas</em> connects the systems you already run.</h3>' + atlas_svg() +
              '<p>Maintenance, fleet, safety and video systems stay where they are. Atlas maps their records onto the ontology\'s objects and keeps them in step, so the model is the operation and not a copy of it.</p></div>'
              '<div class="ofig"><h3><em>Agentic Studio</em> runs the agents that work on it.</h3>' + studio_svg() +
              f'<p>Managed agents bound to objects, governed by the same roles and kinetics as people. Every run is graded and the agent keeps what it learned, the way <a href="{BASE}/hyper-pragma/">Hyper Pragma</a> does.</p></div></div>'
              '<div class="engine"><div><h3><b>ONE REALITY</b>For every reader and writer.</h3><p>Applications, analytics and agents read and write the same objects through the same rules, so a decision made in one place is true everywhere.</p></div>'
              '<div><h3><b>SOVEREIGN</b>Inside your walls.</h3><p>The ontology, its data and its agents run where your data lives: on premises, in your private cloud or air gapped, on models you host yourself.</p></div>'
              '<div><h3><b>YOURS</b>To keep.</h3><p>Publish and the whole system exports as code: the ontology, its kinetics, its endpoint for agents and its applications. Nothing about your operation is held in anyone else\'s cloud.</p></div></div></div></section>')
    code = ('<section class="osec"><div class="wrap3"><div class="ocode"><div>' + sx(6, "Ontology toolchain") +
            '<h3 data-type>Treat your ontology <em>as a codebase.</em></h3><p data-after>Every Hyper application exports its ontology as a typed manifest beside the code that enforces it. Your engineers review it, version it and run it like any other part of the stack.</p>'
            f'<a class="btn" href="{DEV}">Start building →</a></div>'
            '<pre><span class="c">// src/mcp/manifest.ts, generated by Hyper Studio</span>\n{\n  <span class="k">apiName</span>: <span class="s">"maintenance-work-order"</span>,\n  <span class="k">synonyms</span>: [<span class="s">"Repair Ticket"</span>, <span class="s">"Service Order"</span>],\n'
            '  <span class="k">semanticDomain</span>: <span class="s">"Operations and Maintenance"</span>,\n  <span class="k">links</span>: [{ <span class="k">to</span>: <span class="s">"haul-truck"</span>, <span class="k">phrase</span>: <span class="s">"belongs to"</span> }],\n'
            '  <span class="k">lifecycles</span>: [{\n    <span class="k">stateField</span>: <span class="s">"orderStatus"</span>,\n    <span class="k">transitions</span>: [{ <span class="k">label</span>: <span class="s">"Assign"</span>,\n      <span class="k">from</span>: [<span class="s">"unassigned"</span>], <span class="k">to</span>: <span class="s">"assigned"</span>,\n      <span class="k">tool</span>: <span class="s">"assignMaintenanceWorkOrder"</span> }]\n  }]\n}</pre></div></div></section>')
    cta = (f'<section><div class="wrap3"><div class="octa"><div>Project<b>Hyper Ontology</b></div><div>Approved by<b>Your engineers</b></div>'
           f'<a class="t" href="{brand.COMMERCIAL}">{brand.TALK} <span>→</span></a><a class="s" href="{DEV}">Start building <span>→</span></a></div></div></section>')
    body = f'<main class="og">{hero}{statement}{living}{model}{explore}{kin}{engine}{code}{cta}{depth_block(depth_html)}</main>'
    title = "Hyper Ontology: The Digital Twin of Your Organization, Exported as Code | CodeNinja Atoms"
    desc = "Hyper Ontology encodes the data, logic, actions and rules of an operation, so people and agents work on one reality inside their own walls. Semantics, kinetics, Atlas and Agentic Studio, exported as code you own."
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Hyper Ontology", "applicationCategory": "DeveloperApplication",
           "description": desc, "url": f"{BASE}/hyper-ontology/", "creator": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
           "featureList": ["Semantics: objects, properties, typed links, synonyms", "Kinetics: lifecycles and governed transitions enforced on the server",
                           "Functions: insights and dashboard measures", "Atlas: legacy sources connected in place", "Agentic Studio: managed agents with memory",
                           "Ontology as code: generated manifest.ts and full source export", "MCP endpoint for agents"],
           "isRelatedTo": [{"@type": "SoftwareApplication", "name": "Hyper Pragma", "url": f"{BASE}/hyper-pragma/"}, {"@type": "WebPage", "name": "Hyper Ontology for developers", "url": DEV}]}, faq_ld]
    return shell(title, desc, f"{BASE}/hyper-ontology/", ld, CSS, body, JS + TYPE_JS)


def shell(title, desc, url, ld, css, body, js, extra_head=""):
    nav = brand.nav(BASE + "/")
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}">'
            '<meta name="codeninja:kind" content="product">' + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
            + f'{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{css}</style>{extra_head}</head><body>{brand.header(BASE + "/", nav)}{body}'
            f'<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}{brand.footer_links(BASE + "/")}<span>CodeNinja Atoms is part of <a href="{brand.PARENT}">CodeNinja</a></span></div></footer>'
            f'{js}{brand.SCRIPT}</body></html>')
