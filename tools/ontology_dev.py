"""Hyper Ontology for developers: the page Start Building opens.

Umar, 13 Nov 2026: a developer portal in the spirit of a platform's developer site (a
terminal hero, a Start Building menu, docs, examples, community, hack, contribute), built
on the four things developers get: the exported source code, src/mcp/manifest.ts, Atlas
and Agentic Studio. Atlas and Agentic Studio are drawn in Hyper Studio's own design system
(header #412356, primary violet, Inter). Every section picks a fight with what other
ontology platforms withhold, without naming one. Code samples are taken from the real
Mining GOLD Copper export (synthetic tenant); no secret from the export is published.
"""
from __future__ import annotations

import html
import re

import brand
from ontology_page import BASE, DEV, E, MARK, onto, shell

C = brand.COMMERCIAL
KW = r"\b(export|const|async|await|return|if|throw|interface|type|import|from|new|function|let|var|of|in|true|false|null|undefined)\b"


def hl(code: str) -> str:
    """Tiny highlighter: comments, strings, keywords. Escapes first, then marks."""
    out = []
    for line in code.split("\n"):
        m = re.match(r"^(\s*)(//.*|#.*|\$ .*)$", line)
        if m and not line.strip().startswith("$"):
            out.append(m.group(1) + f'<span class="c">{E(m.group(2))}</span>')
            continue
        parts = re.split(r"('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\"|`[^`]*`)", line)
        seg = []
        for i, p in enumerate(parts):
            if i % 2:
                seg.append(f'<span class="s">{E(p)}</span>')
            else:
                t = E(p)
                t = re.sub(KW, r'<span class="k">\1</span>', t)
                t = re.sub(r"(//.*)$", r'<span class="c">\1</span>', t)
                seg.append(t)
        out.append("".join(seg))
    return "\n".join(out)


def code(title: str, src: str, lang: str = "ts") -> str:
    return (f'<div class="cpan"><div class="ctl"><i></i><i></i><i></i><span>{E(title)}</span><button type="button" class="cpy" aria-label="Copy">Copy</button></div>'
            f'<pre data-lang="{lang}"><code>{hl(src)}</code></pre></div>')


def fight(*rows) -> str:
    return '<div class="fgt"><b>Elsewhere</b>' + "".join(f"<p>{E(r)}</p>" for r in rows) + "</div>"


QUICK = """# 1. In Hyper Studio: Code, Export project (backend)
$ unzip mining-gold-project-backend.zip && cd mining-gold-project
$ cp .env.sample .env        # your Postgres, your secrets
$ npm install
$ npm run migrate            # create the schema
$ npm run seed               # optional sample records
$ npm run dev
# API     http://localhost:8000
# Agents  http://localhost:8000/mcp
# Docs    http://localhost:8000/api-docs"""

TREE = """mining-gold-project/
  src/
    mcp/
      manifest.ts        // the ontology: objects, links, kinetics, functions
      gateway.ts         // four meta tools agents call
      server.ts
    kinetics/
      maintenanceWorkOrder.ts   // generated state machine, the only write path
      crusherDumpPocket.ts
      runtime.ts
    models/            // one Sequelize model per object
    modules/           // routes, controllers, Zod validation
    migrations/        // umzug, versioned with the schema
  generation-report.json
  Dockerfile
  package.json"""

MANIFEST = """export interface OntologyObject {
  apiName: string;
  displayName: string;
  description: string;
  synonyms?: string[];        // the names the business really uses
  semanticDomain?: string;    // authored business domain
  labelProperty?: string;     // what identifies a record to a person
  properties: OntologyProperty[];
  links: OntologyLink[];
  lifecycles?: OntologyLifecycle[];          // kinetics
  derivedStatuses?: OntologyDerivedStatus[]; // computed on read
  actions?: OntologyAction[];                // business actions
  functions?: OntologyFunction[];            // analytics by name
  sideEffects?: OntologySideEffect[];
  agentAccessible: boolean;
}"""

SEM = """{
  "apiName": "maintenance-work-order",
  "displayName": "Maintenance Work Order",
  "description": "A tracking document for repairing and servicing mining machinery, support vehicles, and safety infrastructure.",
  "synonyms": ["Repair Ticket", "Service Order"],
  "semanticDomain": "Operations and Maintenance",
  "labelProperty": "workOrderNumber",
  "links": [{
    "to": "haul-truck",
    "cardinality": "many-to-one",
    "fkProperty": "haulTruckId",
    "phrase": "belongs to",
    "via": { "tool": "detailHaulTruck", "filter": "id" }
  }]
}"""

KIN = """// src/kinetics/maintenanceWorkOrder.ts (generated, do not edit by hand)
export const transitionMaintenanceWorkOrderAssign = async (params, input = {}, actor = null, opts = {}) => {
  const run = async (t) => {
    const wo = await MaintenanceWorkOrder.findOne({ where: { id: params.id }, transaction: t, lock: t.LOCK.UPDATE });
    if (!wo) throw notFound('MaintenanceWorkOrder', 'INVALID_MAINTENANCE_WORK_ORDER_ID');
    if (wo.orderStatus !== 'unassigned') {
      throw badRequest(`Cannot 'Assign': orderStatus is '${wo.orderStatus}', allowed from: unassigned`, 'KINETICS_INVALID_TRANSITION');
    }
    return wo.update({ orderStatus: 'assigned' }, { transaction: t });
  };
  return opts.transaction ? run(opts.transaction) : sequelize.transaction(run);
};

// ordinary updates can never touch a governed state
export function stripMaintenanceWorkOrderGovernedFields(payload) {
  delete payload.orderStatus;
}"""

FUNC = """export interface OntologyFunction {
  name: string;                    // the MCP tool that computes it
  kind: 'insight' | 'dashboard';
  title: string;
  aggregation?: string;            // count | sum | avg | min | max
  chartType?: string;              // bar | line | pie | table
}

// from the Interaction Event object
{ "name": "dashboardAvgProximityDistancem", "kind": "dashboard",
  "title": "Avg Proximity Distance (m)", "aggregation": "avg" }"""

MCP = """// The gateway registers four meta tools, whatever the size of the ontology:
//   describe-project   what every object IS, how objects link, kinetics, functions
//   search-tools       the tools this caller may use, filtered by role
//   get-tool-schema    the JSON input schema of one tool
//   invoke-tool        validate the arguments and run the tool

// an agent, before it acts
{ "method": "tools/call", "params": { "name": "describe-project" } }
{ "method": "tools/call", "params": { "name": "search-tools", "arguments": { "query": "work order" } } }
{ "method": "tools/call", "params": { "name": "invoke-tool",
  "arguments": { "tool": "assignMaintenanceWorkOrder", "args": { "id": "…" } } } }"""

DEPLOY = """$ npm run build && npm start          # or: docker build -t mining-ontology .
# Postgres of your choice, inside your network
# one instance behind /mcp until a shared token store is configured
# no call leaves your walls: models, agents and data stay where you run them"""


def studio_frame(tab: str, inner: str, project: str = "Mining_Gold_Project") -> str:
    tabs = "".join(f'<span class="{"on" if t == tab else ""}">{t}</span>' for t in ["Collections", "Roles", "Areas", "Automation", "Atlas", "Agents", "Settings", "Code", "Interface"])
    return (f'<div class="sty"><div class="sth"><b><svg viewBox="0 0 38 30" aria-hidden="true"><path d="{MARK}"/></svg>{E(project)}</b><div class="stt">{tabs}</div><span class="pub">Publish</span></div>'
            f'<div class="stb">{inner}</div></div>')


def atlas_screen() -> str:
    srcs = [("Maintenance ERP", "SAP PM · OData", "Live", "g"), ("Fleet management", "Dispatch · SQL Server", "Every 15 min", "g"), ("Collision avoidance", "CAS · MQTT", "Live", "g"),
            ("Video management", "VMS · REST", "On event", "g"), ("Permit register", "permits.xlsx · SharePoint", "Nightly", "a")]
    left = "".join(f'<div class="src{" on" if i == 0 else ""}"><i class="{d}"></i><div><b>{a}</b><span>{b}</span></div><em>{c}</em></div>' for i, (a, b, c, d) in enumerate(srcs))
    rows = [("AUFNR", "maintenance-work-order", "workOrderNumber"), ("QMTXT", "maintenance-work-order", "faultDescription"), ("PRIOK", "maintenance-work-order", "priorityLevel"),
            ("EQUNR", "haul-truck", "link: belongs to"), ("ERDAT", "maintenance-work-order", "reportedAt")]
    tbl = "".join(f"<tr><td><code>{a}</code></td><td>→</td><td><span class='ob'>{b}</span></td><td><code>{c}</code></td></tr>" for a, b, c in rows)
    inner = (f'<div class="atl"><div class="srcs"><p class="stl">Sources <span>5</span></p>{left}<button type="button" class="sbtn">+ Connect source</button></div>'
             f'<div class="map"><p class="stl">Maintenance ERP → ontology <span class="ok">in step · 4 s ago</span></p><table><tr><th>Source field</th><th></th><th>Object</th><th>Property</th></tr>{tbl}</table>'
             '<p class="stn">Records stay in the source system. Atlas maps them onto objects, keeps them in step and writes approved changes back.</p></div></div>')
    return studio_frame("Atlas", inner)


def agents_screen() -> str:
    rows = [("fault-to-work-order", "Maintenance Work Order", "hourly", "+1.00"), ("critical-escalation", "Supervisor Alert", "every 30 min", "new"),
            ("evidence-attach", "Evidence Clip", "hourly", "new"), ("sla-watch", "Supervisor Alert", "hourly", "new")]
    tr = "".join(f"<tr><td><i class='g'></i><b>{a}</b></td><td><span class='ob'>{b}</span></td><td>{c}</td><td>memory on</td><td class='sc'>{d}</td></tr>" for a, b, c, d in rows)
    inner = (f'<div class="agt"><p class="stl">Managed agents <span>4</span><span class="sbtn r">+ New agent</span></p>'
             f'<table><tr><th>Agent</th><th>Bound to</th><th>Runs</th><th>Self Improving Memory</th><th>Last grade</th></tr>{tr}</table>'
             '<div class="exp"><p class="stl">Export targets</p><div class="tg on"><b>Backend</b><span>API, models, routes, manifest.ts</span><i>✓</i></div>'
             '<div class="tg"><b>Frontend</b><span>Components, pages, hooks</span><i></i></div><div class="tg on"><b>Agentic Studio</b><span>Managed agents, their memory and schedules</span><i>✓</i></div></div></div>')
    return studio_frame("Agents", inner)


def monitor(inner: str) -> str:
    return f'<div class="mon"><div class="scr">{inner}</div><div class="neck"></div><div class="foot"></div></div>'


from ontology_page import TYPE_CSS, TYPE_JS

DIFF = """--- other ontology platforms
+++ hyper ontology
@@ where your ontology lives @@
- in the vendor's cloud, behind a console
+ in your repository: src/mcp/manifest.ts
@@ export @@
- none, or a partial schema dump
+ the full source, regenerated on every publish
@@ how rules are enforced @@
- settings inside a screen you cannot read
+ generated code, in locked transactions
@@ how agents connect @@
- a proprietary SDK and a service account that sees everything
+ an MCP endpoint, four tools, filtered by role
@@ your existing systems @@
- migrate the data into their platform
+ Atlas connects them in place
@@ your models @@
- the vendor's choice
+ any model you host, air gapped if you want
@@ leaving @@
- rebuild from nothing
+ you already own the code"""

CSS = r"""
.dv{--bg:#100d16;--bg2:#181421;--ln:rgba(164,143,255,.28);--vi:#7c5cff;--vi2:#b3a1ff;--yl:#ffd166;--tx:#ece9f5;--mu:#a39cb5;background:var(--bg);color:var(--tx);font:400 16px/1.55 var(--sans)}
.dv a{color:inherit}.dv .w{max-width:1200px;margin:0 auto;padding:0 clamp(16px,3vw,40px)}
/* the path you are on */
.dsub{position:sticky;top:var(--hdr,64px);z-index:5;background:rgba(16,13,22,.92);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--ln)}
.dsub .w{display:flex;align-items:center;gap:6px;height:50px;font:400 13px var(--mono);overflow-x:auto;white-space:nowrap}.dsub .pth{color:var(--mu);margin-right:auto}.dsub .pth b{color:var(--tx);font-weight:400}
.dsub a{text-decoration:none;color:var(--mu);padding:5px 9px;border-radius:6px}.dsub a:hover{color:var(--tx);background:var(--bg2)}
/* hero: studio writes it, you own it */
.dh{padding:clamp(130px,16vh,170px) 0 70px}
.dh h1{font:300 clamp(44px,6.4vw,96px)/.98 var(--sans);letter-spacing:-.045em;margin:0;max-width:13ch}.dh h1 em{color:var(--yl)}
.dh .hl{display:grid;grid-template-columns:1fr 360px;gap:40px;align-items:end;margin-bottom:40px}.dh .hl p{margin:0;color:var(--mu);font:300 19px/1.5 var(--sans)}.dh .hl p.kk{font:400 13px var(--mono);color:var(--yl);margin:0 0 14px}
.dh .acts{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.dh .b1{font:500 14px var(--sans);padding:13px 20px;background:var(--yl);color:#17131f;text-decoration:none}
.sb{position:relative}.sb>button{font:500 14px var(--sans);padding:12px 18px;border:1px solid var(--tx);background:none;color:var(--tx);cursor:pointer;display:flex;align-items:center;gap:14px}
.sb>button span{transition:transform .25s}.sb.open>button span{transform:rotate(180deg)}
.sb .dd{position:absolute;left:0;top:calc(100% + 6px);background:#0c0a11;border:1px solid var(--ln);padding:6px;display:none;z-index:6;min-width:300px}
.sb.open .dd{display:block}.sb .dd a{display:block;padding:11px 14px;text-decoration:none;font:400 14px var(--sans)}.sb .dd a:hover{background:var(--bg2);color:var(--yl)}.sb .dd small{display:block;color:var(--mu);font-size:12px}
/* the playground */
.pg2{display:grid;grid-template-columns:420px 1fr;border:1px solid var(--ln);background:#0c0a11;min-height:470px}
.pgl{background:#fff;color:#1b1626;font:400 13px/1.45 Inter,var(--sans);display:flex;flex-direction:column}
.pgl .ph{background:#412356;color:#fff;height:42px;display:flex;align-items:center;gap:8px;padding:0 14px;font-weight:600}.pgl .ph svg{width:16px;fill:#fff}.pgl .ph span{font-weight:400;color:rgba(255,255,255,.7);margin-left:auto;font-size:12px}
.pgl .obs{display:flex;gap:4px;padding:10px 12px;border-bottom:1px solid #ece8f4;flex-wrap:wrap}.pgl .obs button{font:500 12.5px Inter,sans-serif;border:1px solid #e1dcef;background:#fff;border-radius:7px;padding:6px 10px;cursor:pointer;color:#1b1626}.pgl .obs button.on{background:#5b2bff;border-color:#5b2bff;color:#fff}
.pgl .ctl{padding:14px;display:flex;flex-direction:column;gap:9px;flex:1}.pgl .ctl p{text-align:left;margin:0 0 2px;font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:#6b6380}
.tgl{display:flex;align-items:center;gap:12px;padding:11px 12px;border:1px solid #ece8f4;border-radius:10px;cursor:pointer;text-align:left;background:#fff;font:400 13.5px Inter,sans-serif;color:#1b1626;width:100%}
.tgl i{display:block;flex:none;width:34px;height:20px;border-radius:99px;background:#e1dcef;position:relative;transition:background .2s}.tgl i::after{content:"";position:absolute;left:3px;top:3px;width:14px;height:14px;border-radius:50%;background:#fff;transition:transform .2s}
.tgl[aria-pressed=true]{border-color:#5b2bff;background:#faf8ff}.tgl[aria-pressed=true] i{background:#5b2bff}.tgl[aria-pressed=true] i::after{transform:translateX(14px)}.tgl b{font-weight:500}.tgl small{display:block;color:#6b6380;font-size:12px}
.pgl .pub{margin:4px 14px 14px;font:600 13.5px Inter,sans-serif;background:#5b2bff;color:#fff;border:0;border-radius:8px;padding:11px;cursor:pointer}
.pgr{display:flex;flex-direction:column;min-width:0}.pgr .rh{display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--ln);font:400 12.5px var(--mono);color:var(--mu)}.pgr .rh b{color:var(--tx);font-weight:400}.pgr .rh .st{margin-left:auto;color:#7ee2b8}
.pgr pre{margin:0;padding:14px 0;flex:1;overflow:auto;font:400 13px/1.7 var(--mono);color:#e9e4ff}.pgr pre div{padding:0 16px 0 40px;position:relative;white-space:pre}.pgr pre div::before{content:attr(data-g);position:absolute;left:16px;color:var(--mu)}
.pgr pre .add{background:rgba(43,217,143,.12);color:#bdf5dc}.pgr pre .add::before{color:#2bd98f}.pgr pre .del{background:rgba(229,72,77,.12);color:#f4b7ba;text-decoration:line-through}.pgr pre .del::before{color:#e5484d}
.pgr pre .k{color:#b69cff}.pgr pre .s{color:#7ee2b8}.pgr .stat{border-top:1px solid var(--ln);padding:10px 14px;font:400 12.5px var(--mono);color:var(--mu)}.pgr .stat .p{color:#2bd98f}.pgr .stat .m{color:#e5484d}
.sec{padding:90px 0;border-top:1px solid rgba(255,255,255,.06)}.sec.lt{background:#f1efe9;color:#17131f}
.kk{font:400 13px var(--mono);color:var(--yl);margin:0 0 14px}.sec.lt .kk{color:#5b2bff}
.big3{font:300 clamp(32px,4vw,56px)/1.07 var(--sans);letter-spacing:-.035em;margin:0 0 16px;max-width:20ch}.big3 em{font-style:normal;color:var(--yl)}.sec.lt .big3 em{color:#5b2bff}
.mu{color:var(--mu)}.sec.lt .mu{color:#5f5873}
/* the fight, as a diff */
.dfw{display:grid;grid-template-columns:1fr 1.25fr;gap:44px;align-items:start}.dfw>div,.dh .hl>div,.pgr{min-width:0}
.dfp{border:1px solid var(--ln);background:#0c0a11}.dfp .rh{padding:10px 14px;border-bottom:1px solid var(--ln);font:400 12.5px var(--mono);color:var(--mu)}
.dfp pre{margin:0;padding:12px 0;font:400 13.5px/1.75 var(--mono);overflow:auto}.dfp pre span{display:block;padding:0 16px;white-space:pre}.dfp .m{background:rgba(229,72,77,.1);color:#f4b7ba}.dfp .p{background:rgba(43,217,143,.1);color:#bdf5dc}.dfp .h{color:#b69cff;margin-top:6px}.dfp .f{color:var(--mu)}
/* docs as a repository */
.docs{display:grid;grid-template-columns:270px 1fr;gap:50px}.docs>div,.dsec{min-width:0}
.tree{position:sticky;top:calc(var(--hdr,64px) + 70px);align-self:start;border:1px solid var(--ln);background:#0c0a11;font:400 13px/1.4 var(--mono);padding:10px 0}
.tree .rt{padding:6px 14px 10px;color:var(--tx)}.tree a{display:grid;grid-template-columns:18px 1fr;gap:4px;padding:6px 14px;text-decoration:none;color:var(--mu);border-left:2px solid transparent}
.tree a small{grid-column:2;font:400 11.5px var(--sans);color:var(--mu);opacity:.75}.tree a.on,.tree a:hover{color:var(--tx);background:var(--bg2);border-left-color:var(--yl)}.tree a.sd{color:var(--vi2)}
.dsec{padding:0 0 70px;scroll-margin-top:140px}.dsec .fp{font:400 12.5px var(--mono);color:var(--yl);margin:0 0 8px}.dsec .fp.sd{color:var(--vi2)}
.dsec h3{font:400 32px/1.15 var(--sans);letter-spacing:-.02em;margin:0 0 10px}
.dsec>p{color:var(--mu);max-width:68ch}.dsec ol{color:var(--mu);padding-left:20px}.dsec ol li{margin:6px 0}.dsec ol b,.dsec p b{color:var(--tx);font-weight:500}.dsec code{font:400 .88em var(--mono);color:var(--vi2)}
.cpan{border:1px solid var(--ln);overflow:hidden;background:#0c0a11;margin:18px 0}.ctl{display:flex;align-items:center;gap:7px;padding:9px 12px;border-bottom:1px solid var(--ln);font:400 12px var(--mono);color:var(--mu)}
.ctl i{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.22)}.ctl span{margin-left:8px}.cpy{margin-left:auto;font:500 11px var(--mono);background:none;border:1px solid var(--ln);color:var(--mu);padding:4px 9px;cursor:pointer}.cpy:hover{color:var(--tx)}
.cpan pre{margin:0;padding:16px 18px;overflow:auto;font:400 13px/1.62 var(--mono);color:#e9e4ff;max-height:520px}.cpan .k{color:#b69cff}.cpan .s{color:#7ee2b8}.cpan .c{color:#8a809f}
.fgt{border-left:2px solid #e5484d;background:rgba(229,72,77,.07);padding:12px 16px;margin:18px 0}.fgt b{font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#f08a8f}.fgt p{margin:6px 0 0;color:var(--tx);font-size:15px}
.pts{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}.pts div{border:1px solid var(--ln);padding:14px;font-size:14px;color:var(--mu)}.pts b{display:block;color:var(--tx);font:500 13px var(--mono);margin-bottom:6px}
/* studio screens */
.sty{border-radius:10px;overflow:hidden;background:#fff;color:#1b1626;font:400 13px/1.45 Inter,var(--sans);margin:18px 0;box-shadow:0 20px 60px rgba(0,0,0,.35)}
.sth{display:flex;align-items:center;gap:18px;background:#412356;color:#fff;padding:0 14px;height:44px}.sth b{display:flex;align-items:center;gap:8px;font-weight:600;white-space:nowrap}.sth svg{width:18px;fill:#fff}
.stt{display:flex;gap:4px;overflow:hidden;font-size:12.5px}.stt span{padding:5px 10px;border-radius:7px;color:rgba(255,255,255,.75);white-space:nowrap}.stt span.on{background:#5b2bff;color:#fff}.sth .pub{margin-left:auto;background:#fff;color:#412356;font-weight:600;padding:6px 12px;border-radius:7px}
.stb{padding:16px;background:#fff}.stl{display:flex;align-items:center;gap:8px;font-weight:600;margin:0 0 10px}.stl span{font-weight:400;color:#6b6380;background:#f1eef8;border-radius:99px;padding:1px 8px;font-size:11.5px}.stl .ok{background:#e3f6ee;color:#0f8a5f}
.sty table{width:100%;border-collapse:collapse;font-size:12.5px}.sty th{text-align:left;font-weight:500;color:#6b6380;padding:7px 8px;border-bottom:1px solid #ece8f4}.sty td{padding:8px;border-bottom:1px solid #f2eff8}.sty code{font:400 12px var(--mono);color:#1b1626}
.sty .ob{background:#efe9ff;color:#5b2bff;border-radius:6px;padding:2px 8px;font-size:12px}.sty i.g{display:inline-block;width:7px;height:7px;border-radius:50%;background:#0f8a5f;margin-right:8px}
.atl{display:grid;grid-template-columns:240px 1fr;gap:16px}.srcs{border-right:1px solid #ece8f4;padding-right:14px}.src{display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:8px;margin-bottom:4px}.src.on{background:#f3efff}
.src div{flex:1;min-width:0}.src b{display:block;font-weight:500}.src span{font-size:11.5px;color:#6b6380}.src em{font-style:normal;font-size:11px;color:#6b6380;white-space:nowrap}.src i{flex:none;width:7px;height:7px;border-radius:50%;background:#0f8a5f}.src i.a{background:#b0740f}
.sbtn{margin-top:10px;font:500 12.5px Inter,sans-serif;border:1px dashed #c9bff0;color:#5b2bff;background:#fff;border-radius:8px;padding:8px 10px;width:100%}.sbtn.r{margin:0 0 0 auto;width:auto;border-style:solid;background:#5b2bff;color:#fff}
.stn{margin:12px 0 0;color:#6b6380;font-size:12.5px}.sty td.sc{font-weight:600;color:#5b2bff}
.exp{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:16px}.exp .stl{grid-column:1/-1;margin:0}.tg{border:1px solid #ece8f4;border-radius:10px;padding:12px;position:relative}.tg.on{border-color:#5b2bff;background:#faf8ff}
.tg b{display:block}.tg span{font-size:12px;color:#6b6380}.tg i{position:absolute;right:10px;top:10px;width:18px;height:18px;border-radius:50%;border:1px solid #c9bff0;font-style:normal;font-size:11px;display:grid;place-items:center}.tg.on i{background:#5b2bff;border-color:#5b2bff;color:#fff}
/* starter repositories */
.repos{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:30px}
.repo{background:#fff;border:1px solid rgba(23,19,31,.18);padding:22px;display:flex;flex-direction:column;gap:12px;transition:border-color .25s,transform .25s}.repo:hover{border-color:#5b2bff;transform:translateY(-3px)}
.repo .rn{display:flex;align-items:center;gap:9px;font:500 15px var(--mono);color:#5b2bff}.repo .rn svg{width:16px;fill:none;stroke:#17131f;stroke-width:1.5}
.repo p{margin:0;color:#5f5873;font-size:15px}.repo .tags{display:flex;flex-wrap:wrap;gap:6px}.repo .tags span{font:500 11.5px var(--mono);background:#f1efe9;border:1px solid rgba(23,19,31,.12);padding:3px 8px}
.repo .cnt{font:400 12.5px var(--mono);color:#5f5873;border-top:1px dashed rgba(23,19,31,.2);padding-top:12px}.repo .ra{display:flex;gap:8px;margin-top:auto}.repo .ra a{font:500 13px var(--sans);text-decoration:none;padding:9px 13px;border:1px solid #17131f}.repo .ra a.p{background:#17131f;color:#fff}
.repo.you{border-style:dashed;background:transparent}
/* community, as a git log */
.glog{border:1px solid var(--ln);background:#0c0a11;margin-top:30px}.glog .rh{padding:10px 16px;border-bottom:1px solid var(--ln);font:400 13px var(--mono);color:var(--mu)}.glog .rh b{color:var(--yl);font-weight:400}
.glog a{display:grid;grid-template-columns:90px 120px 1fr auto;gap:16px;align-items:center;padding:16px;border-bottom:1px solid rgba(164,143,255,.12);text-decoration:none;font:400 14.5px var(--sans);transition:background .2s}.glog a:last-child{border-bottom:0}
.glog a:hover{background:var(--bg2)}.glog .hsh{font:400 13px var(--mono);color:var(--yl)}.glog .ty{font:500 12.5px var(--mono);color:var(--vi2)}.glog .go{font:400 13px var(--mono);color:var(--mu)}.glog a:hover .go{color:var(--tx)}
.fin{margin-top:60px;display:flex;justify-content:space-between;align-items:flex-end;gap:30px;flex-wrap:wrap}.fin h2{font:300 clamp(40px,5.4vw,80px)/1 var(--sans);letter-spacing:-.045em;margin:0}.fin h2 em{font-style:normal;color:var(--yl)}
@media (max-width:980px){.docs,.dfw,.dh .hl{grid-template-columns:1fr}.tree{display:none}.pg2{grid-template-columns:1fr}.repos{grid-template-columns:1fr}.pts{grid-template-columns:1fr}.atl{grid-template-columns:1fr}.srcs{border-right:0}.exp{grid-template-columns:1fr}.glog a{grid-template-columns:80px 1fr}.glog .ty,.glog .go{display:none}}
@media (max-width:620px){.sty{font-size:12px}.sty table{display:block;overflow-x:auto}}
""" + TYPE_CSS

JS = r"""<script>(function(){
var hb=document.querySelector('.topwrap')||document.querySelector('header.top');function hdr(){if(hb)document.documentElement.style.setProperty('--hdr',Math.round(hb.getBoundingClientRect().bottom)+'px')}hdr();addEventListener('resize',hdr);
/* the playground: change the object in Studio, watch manifest.ts regenerate as a diff */
var D=window.HYPER_ONTOLOGY||{objects:[]},O={};D.objects.forEach(function(o){O[o.id]=o});
var X={'maintenance-work-order':{syn:'Job Card',link:['work-permit','requires','many-to-one']},'crusher-dump-pocket':{syn:'Ore Bin',link:['shift','scheduled in','many-to-one']},'haul-truck':{syn:'Dump Truck',link:['shift','assigned to','many-to-one']}};
var cur='maintenance-work-order',opt={syn:false,link:false,hide:false},pre=document.getElementById('pgcode'),stat=document.getElementById('pgstat'),st=document.getElementById('pgst');
function q(s){return '<span class="s">"'+String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')+'"</span>'}function k(s){return '<span class="k">'+s+'</span>'}
function lines(id,o2){var o=O[id],x=X[id],L=[];if(!o)return L;var syn=o.syn.slice();if(o2.syn)syn.push(x.syn);
 L.push('{');L.push('  '+k('apiName')+': '+q(o.id)+',');L.push('  '+k('displayName')+': '+q(o.name)+',');L.push('  '+k('synonyms')+': ['+syn.map(q).join(', ')+'],');
 L.push('  '+k('semanticDomain')+': '+q(o.domain)+',');L.push('  '+k('agentAccessible')+': '+(o2.hide?'false':'true')+',');L.push('  '+k('links')+': [');
 var ls=o.links.slice(0,3);if(o2.link)ls=ls.concat([x.link]);ls.forEach(function(l){L.push('    { '+k('to')+': '+q(l[0])+', '+k('phrase')+': '+q(l[1])+', '+k('cardinality')+': '+q(l[2])+' },')});
 if(o.links.length>3)L.push('    <span style="color:#8a809f">// '+(o.links.length-3)+' more links</span>');L.push('  ],');
 if(o.lifecycles.length){var lc=o.lifecycles[0];L.push('  '+k('lifecycles')+': [{ '+k('stateField')+': '+q(lc.field)+', '+k('transitions')+': '+lc.transitions.length+' }],')}
 L.push('}');return L}
function render(){var base=lines(cur,{syn:false,link:false,hide:false}),now=lines(cur,opt),out=[],a=0,d=0,i=0,j=0;
 while(i<base.length||j<now.length){if(i<base.length&&j<now.length&&base[i]===now[j]){out.push('<div data-g=" ">'+now[j]+'</div>');i++;j++}
  else if(j<now.length&&base.indexOf(now[j],i)<0){out.push('<div class="add" data-g="+">'+now[j]+'</div>');a++;j++}
  else{out.push('<div class="del" data-g="-">'+base[i]+'</div>');d++;i++}}
 pre.innerHTML=out.join('');stat.innerHTML=(a||d)?('src/mcp/manifest.ts | '+(a+d)+' <span class="p">'+'+'.repeat(a)+'</span><span class="m">'+'-'.repeat(d)+'</span>'):'src/mcp/manifest.ts | in step with Studio';
 st.textContent=(a||d)?'unpublished changes':'published'}
var obs=[].slice.call(document.querySelectorAll('.pgl .obs button')),tg=[].slice.call(document.querySelectorAll('.tgl'));
function labels(){var x=X[cur];document.getElementById('tsyn').textContent='Add the synonym “'+x.syn+'”';document.getElementById('tlink').textContent='Link it to '+(O[x.link[0]]?O[x.link[0]].name:x.link[0])+' ('+x.link[1]+')'}
obs.forEach(function(b){b.addEventListener('click',function(){cur=b.getAttribute('data-id');obs.forEach(function(c){c.classList.toggle('on',c===b)});opt={syn:false,link:false,hide:false};tg.forEach(function(t){t.setAttribute('aria-pressed','false')});labels();render()})});
tg.forEach(function(t){t.addEventListener('click',function(){var key=t.getAttribute('data-k');opt[key]=!opt[key];t.setAttribute('aria-pressed',opt[key]);render()})});
var pub=document.getElementById('pgpub');if(pub)pub.addEventListener('click',function(){st.textContent='published · manifest.ts regenerated';pre.querySelectorAll('.add,.del').forEach(function(e){e.classList.remove('add');e.setAttribute('data-g',' ');if(e.classList.contains('del'))e.remove()});stat.innerHTML='src/mcp/manifest.ts | committed with this publish'});
if(pre){labels();render()}
/* Start Building opens by who you are building for */
var sb=document.querySelector('.sb');if(sb){var bt=sb.querySelector('button');bt.addEventListener('click',function(e){e.stopPropagation();var o=sb.classList.toggle('open');bt.setAttribute('aria-expanded',o)});document.addEventListener('click',function(){sb.classList.remove('open');bt.setAttribute('aria-expanded','false')})}
[].forEach.call(document.querySelectorAll('.cpy'),function(b){b.addEventListener('click',function(){var c=b.closest('.cpan').querySelector('code').innerText;if(navigator.clipboard)navigator.clipboard.writeText(c).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1400)})})});
/* the repository tree follows the reader */
var ra=[].slice.call(document.querySelectorAll('.tree a')),hs=ra.map(function(a){return document.getElementById(a.getAttribute('href').slice(1))});
function spy(){var y=innerHeight*.35,k2=0;hs.forEach(function(h,j){if(h&&h.getBoundingClientRect().top<y)k2=j});ra.forEach(function(a,j){a.classList.toggle('on',j===k2)})}if(ra.length){addEventListener('scroll',spy,{passive:true});spy()}
})();</script>""" + TYPE_JS

FOLDER = '<svg viewBox="0 0 16 16"><path d="M1.5 3.5h5l1.5 2h6.5v8h-13z"/></svg>'


def build() -> str:
    import json as _json
    data = onto()
    objs = data["objects"]
    n_obj, n_link, n_syn = len(objs), sum(len(o["links"]) for o in objs), sum(len(o["syn"]) for o in objs)
    sub = ('<nav class="dsub" aria-label="Developers"><div class="w"><span class="pth">codeatoms.ai / hyper-ontology / <b>developers</b></span>'
           '<a href="#playground">playground/</a><a href="#docs">docs/</a><a href="#repos">repos/</a><a href="#community">community/</a></div></nav>')
    choose = [("maintenance-work-order", "Work Order"), ("crusher-dump-pocket", "Crusher Pocket"), ("haul-truck", "Haul Truck")]
    play = ('<div class="pg2" id="playground"><div class="pgl"><div class="ph"><svg viewBox="0 0 38 30"><path d="' + MARK + '"/></svg>Hyper Studio<span>Mining_Gold_Project</span></div>'
            '<div class="obs">' + "".join(f'<button type="button" data-id="{i}" class="{"on" if k == 0 else ""}">{t}</button>' for k, (i, t) in enumerate(choose)) + '</div>'
            '<div class="ctl"><p>Change the object</p>'
            '<button type="button" class="tgl" data-k="syn" aria-pressed="false"><i></i><span><b id="tsyn">Add a synonym</b><small>Semantics: one more name the business uses</small></span></button>'
            '<button type="button" class="tgl" data-k="link" aria-pressed="false"><i></i><span><b id="tlink">Add a link</b><small>Semantics: a typed link that reads as a sentence</small></span></button>'
            '<button type="button" class="tgl" data-k="hide" aria-pressed="false"><i></i><span><b>Hide it from agents</b><small>Governance: the MCP gateway stops serving it</small></span></button></div>'
            '<button type="button" class="pub" id="pgpub">Publish</button></div>'
            '<div class="pgr"><div class="rh"><b>src/mcp/manifest.ts</b>generated · do not edit by hand<span class="st" id="pgst">published</span></div><pre id="pgcode" aria-live="polite"></pre><div class="stat" id="pgstat"></div></div></div>')
    hero = ('<section class="dh"><div class="w"><div class="hl"><div><p class="kk">$ hyper-ontology --for developers</p><h1 data-type>Studio writes it. <em>You own it.</em></h1></div>'
            '<div data-after><p>Model your operation in Hyper Studio. Every change regenerates your ontology as typed code in your repository. Try it below.</p>'
            '<div class="acts"><a class="b1" href="#docs">Read the docs</a><div class="sb"><button type="button" aria-expanded="false" aria-haspopup="true">Start building <span>⌄</span></button><div class="dd">'
            f'<a href="{C}">I am an enterprise builder<small>Studio access for your team, inside your walls</small></a>'
            f'<a href="{C}">I am a public sector or defence builder<small>Air gapped deployments on hardware you control</small></a>'
            '<a href="#quickstart">I already have an export<small>Stand it up in a few commands</small></a>'
            f'<a href="{BASE}/hyper-ontology/#explore">I want to see one first<small>Explore the Mining GOLD Copper ontology</small></a></div></div></div></div></div>'
            f'{play}</div></section>')
    diff = "".join(f'<span class="{ {"-": "m", "+": "p", "@": "h"}.get(l[:1], "f") if not l.startswith(("---", "+++")) else "f"}">{E(l)}</span>' for l in DIFF.split("\n"))
    why = ('<section class="sec" id="why"><div class="w dfw"><div><p class="kk">$ git diff other-platforms hyper</p><h2 class="big3" data-type>Other ontology platforms <em>rent you your own operation.</em></h2>'
           '<p class="mu" data-after>They hold the model of your business on their side, enforce its rules in places you cannot read, and sell your agents access to it. Here is the difference, the way engineers read differences.</p></div>'
           f'<div class="dfp"><div class="rh">why-hyper.diff</div><pre>{diff}</pre></div></div></section>')
    tree = [("quickstart", "▢", "README.md", "Quickstart", ""), ("as-code", "▢", "src/mcp/manifest.ts", "Ontology as code", ""), ("semantics", "·", "  synonyms · links", "Semantics", ""),
            ("kinetics", "▸", "src/kinetics/", "Kinetics", ""), ("functions", "·", "  functions · actions", "Functions and actions", ""), ("agents", "▢", "src/mcp/gateway.ts", "Agents over MCP", ""),
            ("atlas", "◆", "Studio · Atlas", "Legacy sources", "sd"), ("agentic-studio", "◆", "Studio · Agents", "Agentic Studio", "sd"), ("deploy", "▢", "Dockerfile", "Run it anywhere", "")]
    tree_html = '<nav class="tree" aria-label="Docs"><div class="rt">mining-gold-project/</div>' + "".join(f'<a href="#{a}" class="{c}"><span>{i}</span>{E(p)}<small>{E(t)}</small></a>' for a, i, p, t, c in tree) + "</nav>"
    fp = {a: (p.strip(), c) for a, i, p, t, c in tree}
    def sec(aid, title, inner):
        p, c = fp[aid]
        return f'<div class="dsec" id="{aid}"><p class="fp {c}">{E(p)}</p><h3>{title}</h3>{inner}</div>'
    D = [sec("quickstart", "Quickstart", '<p>Model your operation in Hyper Studio, publish, and export. What you download is a complete, typed backend with the ontology inside it. A few commands stand it up.</p>'
             + code("terminal", QUICK, "sh") + fight("You click through a hosted console and never see the system your ontology runs on.")),
         sec("as-code", "Ontology as code", '<p>The ontology is a file, <code>src/mcp/manifest.ts</code>, generated beside the code that enforces it. Diff it in a pull request, review it like any other change, and roll it back with git.</p>'
             + code("project tree", TREE, "txt") + code("src/mcp/manifest.ts · the shape of every object", MANIFEST)
             + '<div class="pts"><div><b>Generated, never hand edited</b>Studio is the source of truth for what things mean. The manifest is its derived layer, rebuilt on every publish.</div>'
               '<div><b>Typed end to end</b>Objects, links, lifecycles and functions are TypeScript types your editor and your agents both understand.</div>'
               '<div><b>A report on every build</b><code>generation-report.json</code> lists every decision the generator made and why.</div></div>'
             + fight("The ontology is a configuration in someone else's database. There is no file to review, and no history you control.")),
         sec("semantics", "Semantics", f'<p>Semantics write down what every object means, in the words the business uses. The Mining GOLD Copper ontology carries {n_obj} objects, {n_link} typed links and {n_syn} synonyms, so an agent asked about a <b>repair ticket</b> finds the <b>Maintenance Work Order</b> without a lookup table.</p>'
             + "<ol><li><b>Object</b>: an <code>apiName</code>, a display name, a description and a <code>labelProperty</code> people recognise.</li>"
               "<li><b>Synonyms and domain</b>: <code>synonyms</code> for every other name, <code>semanticDomain</code> for where it belongs.</li>"
               "<li><b>Links</b>: a cardinality, the property that stores it, a phrase that reads as a sentence, and <code>via</code>, the tool that walks it.</li></ol>"
             + code("maintenance-work-order, from the generated manifest", SEM, "json") + fight("Synonyms live in a separate search index, if at all, and links are join keys with no meaning attached.")),
         sec("kinetics", "Kinetics", '<p>Kinetics model how the operation moves. A lifecycle names the states a record can be in and the transitions between them. Each transition is generated as its own function: it locks the row, checks the move is allowed, and commits in one transaction. Ordinary updates are stripped of the governed field, so a transition is the only way the state can change.</p>'
             + code("src/kinetics/maintenanceWorkOrder.ts", KIN)
             + '<div class="pts"><div><b>Initial and terminal states</b>A new work order starts <code>unassigned</code>. <code>completed</code> and <code>cancelled</code> end it.</div>'
               '<div><b>Role gated</b>Every transition carries a permission. A person and an agent pass the same check.</div>'
               '<div><b>One error for every bad move</b><code>KINETICS_INVALID_TRANSITION</code>, with the states it was allowed from.</div></div>'
             + f'<p>Try it: <a href="{BASE}/hyper-ontology/#kinetics">move a work order</a> through its lifecycle.</p>'
             + fight("Actions are buttons wired in a hosted builder. Nothing stops a script that writes the field directly.")),
         sec("functions", "Functions and actions", '<p>Functions are the numbers the operation runs on, computed once on the server and callable by name: collection insights and dashboard measures. Actions are business operations that are neither plain edits nor lifecycle moves, each fired by a named tool, with a precondition and a flag for the ones that need a person to confirm. Derived statuses are computed on read and arrive on every row as <code>_derived.&lt;key&gt;</code>.</p>'
             + code("functions in the manifest", FUNC) + fight("Every dashboard recomputes the same number its own way, and agents compute a third version.")),
         sec("agents", "Agents over MCP", '<p>Every export serves the ontology to agents at <code>/mcp</code>. The gateway registers four meta tools however large the ontology grows, so an agent discovers what it needs instead of loading hundreds of tools. Access is fail closed: search results and manifest objects are filtered by the caller\'s role, and properties a role cannot see are hidden from the ontology too.</p>'
             + code("what an agent calls", MCP, "json") + f'<p>Hyper Pragma\'s agents work exactly this way: they call <code>describe-project</code> before they act. See them <a href="{BASE}/hyper-pragma/">at work</a>.</p>'
             + fight("Agents get a vendor SDK and a service account that sees everything.")),
         sec("atlas", "Atlas", '<p>Atlas connects the systems you already run to the ontology, in place. Add a source, map its fields to objects and properties, choose how it stays in step, and approved changes write back. Nothing is migrated, and the source system stays the system of record.</p>'
             + atlas_screen() + "<ol><li><b>Connect a source</b>: databases, ERP and maintenance systems, message streams, file shares and spreadsheets.</li>"
               "<li><b>Map</b>: each source field to an object property, or to a link between objects.</li><li><b>Keep in step</b>: live, on a schedule, or on event, per source.</li>"
               "<li><b>Write back</b>: a transition approved in the ontology is written to the system that owns the record.</li></ol>"
             + fight("Connecting a legacy system means a migration project, a copy of your data in their cloud, and a second source of truth.")),
         sec("agentic-studio", "Agentic Studio", '<p>Agentic Studio is where you build the agents that work on the ontology: bind each one to the objects it serves, give it a schedule and a role, and turn on Self Improving Memory, so every run is graded against its own instructions and the agent keeps what it learned. When you publish, the agents export with the application, beside <code>manifest.ts</code>, and you run them yourself.</p>'
             + agents_screen() + f'<p>The memory loop is the one behind <a href="{BASE}/hyper-pragma/">Hyper Pragma</a>: a judge on an open weight model, one lesson per run, and a person who can retire any lesson.</p>'
             + fight("Agents are hosted features you configure, not software you own. Their memory, if they have one, stays with the vendor.")),
         sec("deploy", "Run it anywhere", '<p>The export is a standard Node.js service on Postgres, with a Dockerfile, migrations and an OpenAPI description. Run it on premises, in your private cloud or air gapped, beside models you host yourself.</p>'
             + code("production", DEPLOY, "sh") + fight("Air gapped is a separate product line, if it exists at all."))]
    docs = (f'<section class="sec" id="docs"><div class="w"><p class="kk">$ tree mining-gold-project</p><h2 class="big3" data-type>Read the docs <em>like a repository.</em></h2>'
            f'<p class="mu" data-after style="max-width:60ch;margin-bottom:44px">Every page of the docs is a file you will find in your own export, or a screen in Hyper Studio. Nothing here describes a system you cannot open.</p>'
            f'<div class="docs">{tree_html}<div>{"".join(D)}</div></div></div></section>')
    repos = [("mining-gold-copper-safety", f"Collision avoidance, maintenance and evidence for an open pit mine, with the agents that run on it.", ["TypeScript", "Postgres", "MCP", "Kinetics"],
              f"{n_obj} objects · {n_link} links · 2 lifecycles · 4 agent tools", f"{BASE}/hyper-ontology/#explore", "Explore", ""),
             ("maintenance-kinetics", "The orderStatus lifecycle of a work order, generated as a state machine that refuses every move it does not allow.", ["TypeScript", "Kinetics"],
              "6 states · 5 transitions · 1 error code", f"{BASE}/hyper-ontology/#kinetics", "Try it", ""),
             ("your-operation", "Bring one operation and its systems. We build its first ontology with you, export it, and hand you the repository.", ["Studio", "Atlas", "Agentic Studio"],
              "one build day · your repository", C, "Start one", " you")]
    repo_html = "".join(f'<div class="repo{y}"><div class="rn">{FOLDER}{E(n)}</div><p>{E(d)}</p><div class="tags">{"".join(f"<span>{E(t)}</span>" for t in tg)}</div>'
                        f'<div class="cnt">{E(c)}</div><div class="ra"><a class="p" href="{u}">{a} →</a>{"" if y else f'<a href="{C}">Request the repo</a>'}</div></div>' for n, d, tg, c, u, a, y in repos)
    examples = (f'<section class="sec lt" id="repos"><div class="w"><p class="kk">$ ls starters/</p><h2 class="big3" data-type>Start from a <em>real ontology.</em></h2>'
                f'<p class="mu" data-after style="max-width:60ch">Each starter is a Hyper Studio project and the repository it exports.</p><div class="repos">{repo_html}</div></div></section>')
    log = [("a1f3e2c", "docs", "Read the docs, from ontology as code to Agentic Studio", "#docs"),
           ("7c9d014", "hack", "Book a build day: bring one operation, leave with its ontology exported", C),
           ("3e8b5a1", "talk", "Ask the engineers who write the generator, not a sales script", C),
           ("9b02f6d", "code", "Read the ontology package loader, in Python", "https://github.com/muhammadumar89/codeninja-research/tree/main/hyper-ontology-py"),
           ("c55e7a0", "contribute", "Publish an ontology package, or improve the format every package follows", "https://github.com/muhammadumar89/codeninja-research/blob/main/ONTOLOGY_PACKAGE.md")]
    glog = ('<div class="glog"><div class="rh">$ git log --oneline <b>community</b></div>'
            + "".join(f'<a href="{u}"><span class="hsh">{h}</span><span class="ty">{t}:</span><span>{E(m)}</span><span class="go">open →</span></a>' for h, t, m, u in log) + "</div>")
    comm = (f'<section class="sec" id="community"><div class="w"><p class="kk">$ hyper community</p><h2 class="big3" data-type>Build with the people <em>who build Hyper.</em></h2>{glog}'
            f'<div class="fin"><h2 data-type>Studio writes it. <em>You own it.</em></h2><div class="acts" style="display:flex;gap:10px"><a class="b1" href="{C}" style="font:500 14px var(--sans);padding:13px 20px;background:#ffd166;color:#17131f;text-decoration:none">Start building</a>'
            f'<a href="{BASE}/hyper-ontology/" style="font:500 14px var(--sans);padding:12px 18px;border:1px solid #ece9f5;text-decoration:none">See the platform</a></div></div></div></section>')
    body = (f'<main class="dv">{sub}{hero}{why}{docs}{examples}{comm}</main>'
            f'<script>window.HYPER_ONTOLOGY={_json.dumps(data, ensure_ascii=False)};</script>')
    title = "Hyper Ontology for Developers: Ontology as Code, Kinetics, Atlas and Agentic Studio | CodeNinja Atoms"
    desc = "Build on Hyper Ontology: Studio writes your ontology, you own it as code (manifest.ts and the full source). Semantics, kinetics, Atlas for legacy systems, Agentic Studio for managed agents, and an MCP endpoint for every agent."
    ld = [{"@context": "https://schema.org", "@type": "TechArticle", "headline": "Hyper Ontology for developers", "description": desc, "url": DEV,
           "author": {"@type": "Organization", "name": "CodeNinja"}, "about": {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"}}]
    return shell(title, desc, DEV, ld, CSS, body, JS)
