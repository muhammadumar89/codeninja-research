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


CSS = r"""
.dv{--bg:#121019;--bg2:#1a1724;--ln:rgba(155,133,255,.35);--vi:#7c5cff;--vi2:#a996ff;--tx:#ece9f5;--mu:#a49db6;background:var(--bg);color:var(--tx);font:400 16px/1.55 var(--sans)}
.dv a{color:inherit}.dv .w{max-width:1180px;margin:0 auto;padding:0 clamp(16px,3vw,40px)}
.dv .mono{font-family:var(--mono)}
.dsub{position:sticky;top:var(--hdr,64px);z-index:5;background:rgba(18,16,25,.92);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--ln)}
.dsub .w{display:flex;align-items:center;gap:26px;height:52px;font:500 12.5px var(--mono);letter-spacing:.08em}.dsub b{margin-right:auto;font-weight:500;letter-spacing:0;font-family:var(--sans);font-size:14px}.dsub b i{font-style:normal;color:var(--vi2)}
.dsub a{text-decoration:none;color:var(--mu)}.dsub a:hover{color:var(--tx)}
.dh{min-height:92vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:150px 0 70px}
.term{width:min(640px,92vw);text-align:left;border:1px solid var(--ln);background:#0d0b13;box-shadow:10px 10px 0 var(--vi);border-radius:4px}
.term .tb{display:flex;gap:8px;padding:12px 14px;border-bottom:1px solid var(--ln)}.term .tb i{width:11px;height:11px;border-radius:50%;background:var(--tx);opacity:.9}
.term pre{margin:0;display:grid;grid-template-columns:44px 1fr;font:400 clamp(15px,1.9vw,22px)/1.65 var(--mono);min-height:9.9em}
.term .ln{border-right:1px solid var(--ln);text-align:center;color:var(--mu);padding:12px 0}.term code{padding:12px 16px;white-space:pre-wrap}.term .g{color:var(--vi2)}.term .cu{display:inline-block;width:.55em;height:1.1em;background:var(--vi2);vertical-align:-3px;animation:dblink 1s steps(2) infinite}
@keyframes dblink{50%{opacity:0}}
.dh .now{margin:46px 0 8px;font:400 14px var(--mono)}.pix{width:34px;height:34px;margin:6px auto 30px;display:grid;grid-template-columns:repeat(5,1fr);gap:0}.pix i{background:var(--vi)}.pix i.x{background:none}
.dact{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;position:relative}
.dact .b1{font:500 14px var(--mono);padding:14px 30px;border-radius:99px;background:var(--tx);color:var(--bg);text-decoration:none}
.sb{position:relative}.sb>button{font:500 14px var(--mono);padding:14px 22px 14px 30px;border-radius:99px;border:1px solid var(--tx);background:none;color:var(--vi2);cursor:pointer;display:flex;align-items:center;gap:18px}
.sb>button span{border-left:1px solid var(--tx);padding-left:16px;display:inline-block;transition:transform .25s}.sb.open>button span{transform:rotate(180deg)}
.sb .dd{position:absolute;left:0;right:0;top:calc(100% + 8px);background:#0d0b13;border:1px solid var(--ln);border-radius:14px;padding:6px;text-align:left;display:none;z-index:4;min-width:290px}
.sb.open .dd{display:block}.sb .dd a{display:block;padding:11px 14px;border-radius:9px;text-decoration:none;font:400 14px var(--sans)}.sb .dd a:hover{background:var(--bg2);color:var(--vi2)}.sb .dd small{display:block;color:var(--mu);font-size:12px}
.sec{padding:90px 0;border-top:1px solid rgba(255,255,255,.06)}.sec.lt{background:#f7f6fb;color:#17131f}.sec.lt .mu{color:#5f5873}
.shd{font:400 18px var(--mono);padding:18px 0;border-top:1px dashed var(--ln);border-bottom:1px dashed var(--ln);margin:0 0 40px}.sec.lt .shd{border-color:rgba(23,19,31,.25)}
.big3{font:300 clamp(32px,4vw,56px)/1.07 var(--sans);letter-spacing:-.035em;margin:0 0 16px;max-width:20ch}.big3 em{font-style:normal;color:var(--vi2)}.sec.lt .big3 em{color:#5b2bff}
.mu{color:var(--mu)}
/* the fight */
.vs{display:grid;grid-template-columns:1.1fr 1fr 1fr;border:1px solid var(--ln);border-radius:6px;overflow:hidden;margin-top:34px}
.vs div{padding:15px 18px;border-bottom:1px solid rgba(155,133,255,.18);font-size:15px}.vs .hd{font:500 11.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--mu);background:var(--bg2)}
.vs .q{color:var(--tx);font-weight:500}.vs .no{color:#d9a0a8}.vs .no::before{content:"✕  ";color:#e5484d}.vs .yes{color:var(--tx);background:rgba(124,92,255,.08)}.vs .yes::before{content:"✓  ";color:#2bd98f}
/* docs */
.docs{display:grid;grid-template-columns:230px 1fr;gap:50px}.docs>div,.ex>div,.dsec{min-width:0}.drl{position:sticky;top:calc(var(--hdr,64px) + 70px);align-self:start;display:flex;flex-direction:column;border-left:1px solid var(--ln)}
.drl a{padding:7px 14px;text-decoration:none;color:var(--mu);font:400 14px var(--sans);border-left:2px solid transparent;margin-left:-1px}.drl a.on,.drl a:hover{color:var(--tx);border-left-color:var(--vi)}
.dsec{padding:0 0 70px;scroll-margin-top:140px}.dsec h3{font:400 30px/1.15 var(--sans);letter-spacing:-.02em;margin:0 0 6px}.dsec h3 small{display:block;font:500 12px var(--mono);letter-spacing:.1em;color:var(--vi2);margin-bottom:10px}
.dsec>p{color:var(--mu);max-width:68ch}.dsec ol{color:var(--mu);padding-left:20px}.dsec ol li{margin:6px 0}.dsec ol b,.dsec p b{color:var(--tx);font-weight:500}.dsec code{font:400 .88em var(--mono);color:var(--vi2)}
.cpan{border:1px solid var(--ln);border-radius:8px;overflow:hidden;background:#0d0b13;margin:18px 0}.ctl{display:flex;align-items:center;gap:7px;padding:9px 12px;border-bottom:1px solid var(--ln);font:400 12px var(--mono);color:var(--mu)}
.ctl i{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.25)}.ctl span{margin-left:8px}.cpy{margin-left:auto;font:500 11px var(--mono);background:none;border:1px solid var(--ln);color:var(--mu);border-radius:6px;padding:4px 9px;cursor:pointer}.cpy:hover{color:var(--tx)}
.cpan pre{margin:0;padding:16px 18px;overflow:auto;font:400 13px/1.62 var(--mono);color:#e9e4ff;max-height:520px}.cpan .k{color:#b69cff}.cpan .s{color:#7ee2b8}.cpan .c{color:#8a809f}
.fgt{border-left:2px solid #e5484d;background:rgba(229,72,77,.07);padding:12px 16px;margin:18px 0;border-radius:0 6px 6px 0}.fgt b{font:500 11px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#f08a8f}.fgt p{margin:6px 0 0;color:var(--tx);font-size:15px}
.pts{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}.pts div{border:1px solid var(--ln);border-radius:8px;padding:14px;font-size:14px;color:var(--mu)}.pts b{display:block;color:var(--tx);font:500 13px var(--mono);margin-bottom:6px}
/* studio screens, in Hyper Studio's design */
.sty{border-radius:10px;overflow:hidden;background:#fff;color:#1b1626;font:400 13px/1.45 Inter,var(--sans);margin:18px 0;box-shadow:0 20px 60px rgba(0,0,0,.35)}
.sth{display:flex;align-items:center;gap:18px;background:#412356;color:#fff;padding:0 14px;height:44px}.sth b{display:flex;align-items:center;gap:8px;font-weight:600;white-space:nowrap}.sth svg{width:18px;fill:#fff}
.stt{display:flex;gap:4px;overflow:hidden;font-size:12.5px}.stt span{padding:5px 10px;border-radius:7px;color:rgba(255,255,255,.75);white-space:nowrap}.stt span.on{background:#5b2bff;color:#fff}.pub{margin-left:auto;background:#fff;color:#412356;font-weight:600;padding:6px 12px;border-radius:7px}
.stb{padding:16px;background:#fff}.stl{display:flex;align-items:center;gap:8px;font-weight:600;margin:0 0 10px}.stl span{font-weight:400;color:#6b6380;background:#f1eef8;border-radius:99px;padding:1px 8px;font-size:11.5px}.stl .ok{background:#e3f6ee;color:#0f8a5f}
.sty table{width:100%;border-collapse:collapse;font-size:12.5px}.sty th{text-align:left;font-weight:500;color:#6b6380;padding:7px 8px;border-bottom:1px solid #ece8f4}.sty td{padding:8px;border-bottom:1px solid #f2eff8}.sty code{font:400 12px var(--mono);color:#1b1626}
.sty .ob{background:#efe9ff;color:#5b2bff;border-radius:6px;padding:2px 8px;font-size:12px}.sty i.g{display:inline-block;width:7px;height:7px;border-radius:50%;background:#0f8a5f;margin-right:8px}.sty i.a{display:inline-block;width:7px;height:7px;border-radius:50%;background:#b0740f}
.atl{display:grid;grid-template-columns:240px 1fr;gap:16px}.srcs{border-right:1px solid #ece8f4;padding-right:14px}.src{display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:8px;margin-bottom:4px}.src.on{background:#f3efff}
.src div{flex:1;min-width:0}.src b{display:block;font-weight:500}.src span{font-size:11.5px;color:#6b6380}.src em{font-style:normal;font-size:11px;color:#6b6380;white-space:nowrap}.src i{flex:none;width:7px;height:7px;border-radius:50%;background:#0f8a5f}.src i.a{background:#b0740f}
.sbtn{margin-top:10px;font:500 12.5px Inter,sans-serif;border:1px dashed #c9bff0;color:#5b2bff;background:#fff;border-radius:8px;padding:8px 10px;width:100%}.sbtn.r{margin:0 0 0 auto;width:auto;border-style:solid;background:#5b2bff;color:#fff}
.stn{margin:12px 0 0;color:#6b6380;font-size:12.5px}.sty td.sc{font-weight:600;color:#5b2bff}
.exp{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:16px}.exp .stl{grid-column:1/-1;margin:0}.tg{border:1px solid #ece8f4;border-radius:10px;padding:12px;position:relative}.tg.on{border-color:#5b2bff;background:#faf8ff}
.tg b{display:block}.tg span{font-size:12px;color:#6b6380}.tg i{position:absolute;right:10px;top:10px;width:18px;height:18px;border-radius:50%;border:1px solid #c9bff0;font-style:normal;font-size:11px;display:grid;place-items:center}.tg.on i{background:#5b2bff;border-color:#5b2bff;color:#fff}
/* examples */
.ex{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center;padding:40px 0;border-bottom:1px dashed rgba(23,19,31,.2)}
.ex h4{font:400 32px/1.15 var(--sans);letter-spacing:-.02em;margin:0 0 12px}.ex .mu{margin:0 0 16px}.ex .exf{font:500 13px var(--mono);color:#5b2bff;text-decoration:none;letter-spacing:.06em}
.chk{display:flex;flex-direction:column;gap:10px;margin:22px 0}.chk div{display:flex;align-items:center;border:1px solid rgba(23,19,31,.2);border-radius:4px;background:#fff}.chk i{width:46px;align-self:stretch;border-right:1px solid rgba(23,19,31,.2);display:grid;place-items:center;font-style:normal}.chk span{padding:12px 14px;font-size:15px}
.pill{display:inline-block;border:1px solid #17131f;border-radius:99px;padding:10px 18px;font:500 13px var(--mono);letter-spacing:.06em;text-decoration:none;color:#5b2bff}
.mon{display:flex;flex-direction:column;align-items:center}.mon .scr{width:100%;max-width:440px;aspect-ratio:16/10;border:9px solid #17131f;border-radius:8px;background:#fff;overflow:hidden}.mon .neck{width:70px;height:70px;background:linear-gradient(90deg,#c9c8ce,#e9e8ec,#c9c8ce)}.mon .foot{width:200px;height:6px;border-radius:3px;background:#d9d8de;box-shadow:0 10px 24px rgba(0,0,0,.18)}
.mon .scr svg{width:100%;height:100%;display:block}
/* community */
.cards4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px}.cards4 a{display:flex;flex-direction:column;justify-content:space-between;min-height:220px;border:1px solid var(--ln);border-radius:6px;padding:20px;text-decoration:none;transition:border-color .25s,background .25s}
.cards4 a:hover{border-color:var(--vi);background:var(--bg2)}.cards4 h4{font:400 24px/1.15 var(--sans);margin:0}.cards4 p{margin:0;color:var(--mu);font-size:14.5px}.cards4 span{font:500 12px var(--mono);color:var(--vi2);letter-spacing:.08em}
.rc{display:grid;grid-template-columns:200px 1fr;gap:40px;align-items:center;border:1px solid var(--ln);border-radius:6px;padding:30px 34px;text-decoration:none;margin-top:40px}.rc:hover{background:var(--bg2)}
.rc .pa{display:grid;grid-template-columns:repeat(5,22px);grid-auto-rows:22px}.rc .pa i{background:var(--vi)}.rc .pa i.x{background:none}.rc h4{font:400 34px/1.1 var(--sans);margin:0 0 10px}.rc p{margin:0;font:300 26px/1.2 var(--sans);color:var(--mu)}
@media (max-width:980px){.docs{grid-template-columns:1fr}.drl{display:none}.vs{grid-template-columns:1fr 1fr 1fr;font-size:13px}.ex{grid-template-columns:1fr}.cards4{grid-template-columns:1fr 1fr}.pts{grid-template-columns:1fr}.atl{grid-template-columns:1fr}.srcs{border-right:0}.exp{grid-template-columns:1fr}.rc{grid-template-columns:1fr}}
@media (max-width:620px){.cards4{grid-template-columns:1fr}.vs div{padding:10px;font-size:13px}.dsub .w{gap:14px;font-size:11px;overflow-x:auto}.dsub b{display:none}.sty{font-size:12px}.sty table{display:block;overflow-x:auto}}
"""

JS = r"""<script>(function(){
var hb=document.querySelector('.topwrap')||document.querySelector('header.top');function hdr(){if(hb)document.documentElement.style.setProperty('--hdr',Math.round(hb.getBoundingClientRect().bottom)+'px')}hdr();addEventListener('resize',hdr);
/* the terminal types the four lines that stand an exported ontology up */
var t=document.getElementById('tcode'),L=['<span class="g">npm</span> install','<span class="g">npm run</span> migrate','<span class="g">npm run</span> dev','<span class="g">→</span> /mcp ready'],plain=L.map(function(x){return x.replace(/<[^>]+>/g,'')});
if(t&&!matchMedia('(prefers-reduced-motion: reduce)').matches){var li=0,ci=0;(function ty(){var done=L.slice(0,li).join('\n'),cur=plain[li]||'';t.innerHTML=done+(li?'\n':'')+cur.slice(0,ci).replace(/^(npm run|npm|→)/,'<span class="g">$1</span>')+'<span class="cu"></span>';
 if(li>=L.length){setTimeout(function(){li=0;ci=0;ty()},3200);return}if(ci<cur.length){ci++;setTimeout(ty,55)}else{li++;ci=0;setTimeout(ty,500)}})()}else if(t){t.innerHTML=L.join('\n')}
/* Start Building opens by who you are building for */
var sb=document.querySelector('.sb');if(sb){var bt=sb.querySelector('button');bt.addEventListener('click',function(e){e.stopPropagation();var o=sb.classList.toggle('open');bt.setAttribute('aria-expanded',o)});document.addEventListener('click',function(){sb.classList.remove('open');bt.setAttribute('aria-expanded','false')})}
/* copy buttons */
[].forEach.call(document.querySelectorAll('.cpy'),function(b){b.addEventListener('click',function(){var c=b.closest('.cpan').querySelector('code').innerText;if(navigator.clipboard)navigator.clipboard.writeText(c).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1400)})})});
/* docs rail follows the reader */
var ra=[].slice.call(document.querySelectorAll('.drl a')),hs=ra.map(function(a){return document.getElementById(a.getAttribute('href').slice(1))});
function spy(){var y=innerHeight*.35,k=0;hs.forEach(function(h,j){if(h&&h.getBoundingClientRect().top<y)k=j});ra.forEach(function(a,j){a.classList.toggle('on',j===k)})}if(ra.length){addEventListener('scroll',spy,{passive:true});spy()}
})();</script>"""


def ex_screen(kind: str) -> str:
    if kind == "graph":
        n = [("Haul Truck", 70, 50), ("Interaction Event", 220, 90), ("Collision Alert", 360, 50), ("Work Order", 120, 170), ("Fixed Camera", 300, 170), ("Evidence Clip", 380, 120)]
        e = [(0, 1), (1, 2), (0, 3), (4, 3), (4, 5), (1, 5)]
        s = "".join(f'<line x1="{n[a][1]}" y1="{n[a][2]}" x2="{n[b][1]}" y2="{n[b][2]}" stroke="#5b2bff" stroke-width="1.4"/>' for a, b in e)
        s += "".join(f'<rect x="{x - 52}" y="{y - 13}" width="104" height="26" rx="13" fill="#fff" stroke="#5b2bff"/><text x="{x}" y="{y + 4}" font-size="10" text-anchor="middle" font-family="Inter Tight, Inter, sans-serif" fill="#17131f">{t}</text>' for t, x, y in n)
        return f'<svg viewBox="0 0 440 250"><rect width="440" height="22" fill="#412356"/><text x="10" y="15" font-size="10" fill="#fff" font-family="Inter Tight, Inter, sans-serif">Mining_Gold_Project · ERD</text>{s}</svg>'
    if kind == "kin":
        st = [("unassigned", 220, 55), ("assigned", 340, 110), ("waiting_on_parts", 100, 110), ("in_progress", 220, 160), ("completed", 340, 215), ("cancelled", 100, 215)]
        s = "".join(f'<rect x="{x - 56}" y="{y - 13}" width="112" height="26" rx="6" fill="{"#5b2bff" if t == "in_progress" else "#fff"}" stroke="#412356"/><text x="{x}" y="{y + 4}" font-size="10" text-anchor="middle" font-family="monospace" fill="{"#fff" if t == "in_progress" else "#17131f"}">{t}</text>' for t, x, y in st)
        return f'<svg viewBox="0 0 440 250"><rect width="440" height="22" fill="#412356"/><text x="10" y="15" font-size="10" fill="#fff" font-family="Inter Tight, Inter, sans-serif">Kinetics · orderstatus</text><path d="M220,68 L330,97 M330,123 L230,147 M220,173 L330,202 M150,123 L210,147 M200,173 L120,202" stroke="#bbb" fill="none"/>{s}</svg>'
    return ('<svg viewBox="0 0 440 250"><rect width="440" height="250" fill="#f7f6fb"/><text x="220" y="112" font-size="20" text-anchor="middle" font-family="Inter Tight, Inter, sans-serif" fill="#17131f">Your operation</text>'
            '<text x="220" y="140" font-size="11" text-anchor="middle" font-family="Inter Tight, Inter, sans-serif" fill="#5f5873">objects · links · kinetics · agents</text></svg>')


def build() -> str:
    data = onto()
    objs = data["objects"]
    n_obj, n_link, n_syn = len(objs), sum(len(o["links"]) for o in objs), sum(len(o["syn"]) for o in objs)
    sub = ('<nav class="dsub" aria-label="Developers"><div class="w"><b>Hyper Ontology <i>for developers</i></b>'
           '<a href="#docs">DOCS</a><a href="#examples">EXAMPLES</a><a href="#community">COMMUNITY</a><a href="#hack">HACK</a><a href="#contribute">CONTRIBUTE</a></div></nav>')
    pix = '<div class="pix" aria-hidden="true">' + "".join(f'<i class="{"" if c == "1" else "x"}"></i>' for c in "00100" "00100" "10101" "01110" "00100") + "</div>"
    hero = ('<section class="dh"><div class="term"><div class="tb"><i></i><i></i><i></i></div><pre><span class="ln">1<br>2<br>3<br>4</span><code id="tcode"><span class="g">npm</span> install</code></pre></div>'
            f'<p class="now">Build on Hyper Ontology now</p>{pix}<div class="dact"><a class="b1" href="#docs">Read the docs</a>'
            '<div class="sb"><button type="button" aria-expanded="false" aria-haspopup="true">Start Building<span>⌄</span></button><div class="dd">'
            f'<a href="{C}">I am an enterprise builder<small>Studio access for your team, inside your walls</small></a>'
            f'<a href="{C}">I am a public sector or defence builder<small>Air gapped deployments on hardware you control</small></a>'
            f'<a href="#quickstart">I already have an export<small>Stand it up in a few commands</small></a>'
            f'<a href="{BASE}/hyper-ontology/#explore">I want to see one first<small>Explore the Mining GOLD Copper ontology</small></a></div></div></div></section>')
    vs_rows = [("Where your ontology lives", "In the vendor's cloud", "In your repository"),
               ("Export it as code", "No, or a partial schema dump", "manifest.ts and the full source, on every publish"),
               ("How rules are enforced", "Settings inside a screen", "Generated code you can read, in locked transactions"),
               ("How agents connect", "A proprietary SDK", "An MCP endpoint, filtered by role"),
               ("Your existing systems", "Migrate the data in", "Atlas connects them in place"),
               ("Your models", "The vendor's choice", "Any model you host, air gapped if you want"),
               ("Leaving", "Rebuild from nothing", "You already own the code")]
    vs = ('<div class="vs"><div class="hd">&nbsp;</div><div class="hd">Other ontology platforms</div><div class="hd">Hyper Ontology</div>'
          + "".join(f'<div class="q">{E(a)}</div><div class="no">{E(b)}</div><div class="yes">{E(c)}</div>' for a, b, c in vs_rows) + "</div>")
    why = ('<section class="sec" id="why"><div class="w"><p class="shd">0&gt; Why build here</p><h2 class="big3">Other ontology platforms <em>rent you your own operation.</em></h2>'
           '<p class="mu" style="max-width:62ch">They hold the model of your business on their side, enforce its rules in places you cannot read, and sell your agents access to it. Hyper Ontology gives you the ontology the way engineers expect to own anything: as code, in your repository, running where you choose.</p>'
           f'{vs}</div></section>')
    rail = [("quickstart", "Quickstart"), ("as-code", "Ontology as code"), ("semantics", "Semantics"), ("kinetics", "Kinetics"), ("functions", "Functions and actions"),
            ("agents", "Agents over MCP"), ("atlas", "Atlas"), ("agentic-studio", "Agentic Studio"), ("deploy", "Run it anywhere")]
    D = []
    D.append('<div class="dsec" id="quickstart"><h3><small>1.1</small>Quickstart</h3><p>Model your operation in Hyper Studio, publish, and export. What you download is a complete, typed backend with the ontology inside it. A few commands stand it up.</p>'
             + code("terminal", QUICK, "sh") + fight("You click through a hosted console and never see the system your ontology runs on.") + "</div>")
    D.append('<div class="dsec" id="as-code"><h3><small>1.2</small>Ontology as code</h3><p>The ontology is a file, <code>src/mcp/manifest.ts</code>, generated beside the code that enforces it. Diff it in a pull request, review it like any other change, and roll it back with git.</p>'
             + code("project tree", TREE, "txt") + code("src/mcp/manifest.ts · the shape of every object", MANIFEST)
             + '<div class="pts"><div><b>Generated, never hand edited</b>Studio is the source of truth for what things mean. The manifest is its derived layer, rebuilt on every publish.</div>'
               '<div><b>Typed end to end</b>Objects, links, lifecycles and functions are TypeScript types your editor and your agents both understand.</div>'
               '<div><b>A report on every build</b><code>generation-report.json</code> lists every decision the generator made and why.</div></div>'
             + fight("The ontology is a configuration in someone else's database. There is no file to review, and no history you control.") + "</div>")
    D.append(f'<div class="dsec" id="semantics"><h3><small>1.3</small>Semantics</h3><p>Semantics write down what every object means, in the words the business uses. The Mining GOLD Copper ontology carries {n_obj} objects, {n_link} typed links and {n_syn} synonyms, so an agent asked about a <b>repair ticket</b> finds the <b>Maintenance Work Order</b> without a lookup table.</p>'
             + "<ol><li><b>Object</b>: an <code>apiName</code>, a display name, a description and a <code>labelProperty</code> people recognise.</li>"
               "<li><b>Synonyms and domain</b>: <code>synonyms</code> for every other name, <code>semanticDomain</code> for where it belongs.</li>"
               "<li><b>Links</b>: a cardinality, the property that stores it, a phrase that reads as a sentence, and <code>via</code>, the tool that walks it.</li></ol>"
             + code("maintenance-work-order, from the generated manifest", SEM, "json") + fight("Synonyms live in a separate search index, if at all, and links are join keys with no meaning attached.") + "</div>")
    D.append('<div class="dsec" id="kinetics"><h3><small>1.4</small>Kinetics</h3><p>Kinetics model how the operation moves. A lifecycle names the states a record can be in and the transitions between them. Each transition is generated as its own function: it locks the row, checks the move is allowed, and commits in one transaction. Ordinary updates are stripped of the governed field, so a transition is the only way the state can change.</p>'
             + code("src/kinetics/maintenanceWorkOrder.ts", KIN)
             + '<div class="pts"><div><b>Initial and terminal states</b>A new work order starts <code>unassigned</code>. <code>completed</code> and <code>cancelled</code> end it.</div>'
               '<div><b>Role gated</b>Every transition carries a permission. A person and an agent pass the same check.</div>'
               '<div><b>One error for every bad move</b><code>KINETICS_INVALID_TRANSITION</code>, with the states it was allowed from.</div></div>'
             + f'<p>Try it: <a href="{BASE}/hyper-ontology/#kinetics">move a work order</a> through its lifecycle.</p>'
             + fight("Actions are buttons wired in a hosted builder. Nothing stops a script that writes the field directly.") + "</div>")
    D.append('<div class="dsec" id="functions"><h3><small>1.5</small>Functions and actions</h3><p>Functions are the numbers the operation runs on, computed once on the server and callable by name: collection insights and dashboard measures. Actions are business operations that are neither plain edits nor lifecycle moves, each fired by a named tool, with a precondition and a flag for the ones that need a person to confirm. Derived statuses are computed on read and arrive on every row as <code>_derived.&lt;key&gt;</code>.</p>'
             + code("functions in the manifest", FUNC) + fight("Every dashboard recomputes the same number its own way, and agents compute a third version.") + "</div>")
    D.append('<div class="dsec" id="agents"><h3><small>1.6</small>Agents over MCP</h3><p>Every export serves the ontology to agents at <code>/mcp</code>. The gateway registers four meta tools however large the ontology grows, so an agent discovers what it needs instead of loading hundreds of tools. Access is fail closed: search results and manifest objects are filtered by the caller\'s role, and properties a role cannot see are hidden from the ontology too.</p>'
             + code("what an agent calls", MCP, "json")
             + f'<p>Hyper Pragma\'s agents work exactly this way: they call <code>describe-project</code> before they act. See them <a href="{BASE}/hyper-pragma/">at work</a>.</p>'
             + fight("Agents get a vendor SDK and a service account that sees everything.") + "</div>")
    D.append('<div class="dsec" id="atlas"><h3><small>1.7</small>Atlas</h3><p>Atlas connects the systems you already run to the ontology, in place. Add a source, map its fields to objects and properties, choose how it stays in step, and approved changes write back. Nothing is migrated, and the source system stays the system of record.</p>'
             + atlas_screen()
             + "<ol><li><b>Connect a source</b>: databases, ERP and maintenance systems, message streams, file shares and spreadsheets.</li>"
               "<li><b>Map</b>: each source field to an object property, or to a link between objects.</li>"
               "<li><b>Keep in step</b>: live, on a schedule, or on event, per source.</li>"
               "<li><b>Write back</b>: a transition approved in the ontology is written to the system that owns the record.</li></ol>"
             + fight("Connecting a legacy system means a migration project, a copy of your data in their cloud, and a second source of truth.") + "</div>")
    D.append(f'<div class="dsec" id="agentic-studio"><h3><small>1.8</small>Agentic Studio</h3><p>Agentic Studio is where you build the agents that work on the ontology: bind each one to the objects it serves, give it a schedule and a role, and turn on Self Improving Memory, so every run is graded against its own instructions and the agent keeps what it learned. When you publish, the agents export with the application, beside <code>manifest.ts</code>, and you run them yourself.</p>'
             + agents_screen()
             + f'<p>The memory loop is the one behind <a href="{BASE}/hyper-pragma/">Hyper Pragma</a>: a judge on an open weight model, one lesson per run, and a person who can retire any lesson.</p>'
             + fight("Agents are hosted features you configure, not software you own. Their memory, if they have one, stays with the vendor.") + "</div>")
    D.append('<div class="dsec" id="deploy"><h3><small>1.9</small>Run it anywhere</h3><p>The export is a standard Node.js service on Postgres, with a Dockerfile, migrations and an OpenAPI description. Run it on premises, in your private cloud or air gapped, beside models you host yourself.</p>'
             + code("production", DEPLOY, "sh") + fight("Air gapped is a separate product line, if it exists at all.") + "</div>")
    rail_html = "".join(f'<a href="#{a}">{t}</a>' for a, t in rail)
    docs = (f'<section class="sec" id="docs"><div class="w"><p class="shd">1&gt; Docs</p><div class="docs"><nav class="drl" aria-label="Docs">{rail_html}</nav>'
            f'<div>{"".join(D)}</div></div></div></section>')
    exs = [("Mining GOLD Copper safety ontology", f"Collision avoidance, maintenance and evidence for an open pit mine: {n_obj} objects, two lifecycles and the agents that run on them, built in Hyper Studio.",
            ["Explore every object and its synonyms", "Move a work order through its lifecycle", "See the agents that work on it"], f"{BASE}/hyper-ontology/#explore", "graph"),
           ("Maintenance kinetics", "The orderStatus lifecycle of a work order, from unassigned to completed, generated as a state machine that refuses every move it does not allow.",
            ["Read the generated transition code", "Trigger a refused move", "Gate a transition by role"], "#kinetics", "kin"),
           ("Your operation", "Bring one operation and its systems. We build its first ontology with you, export it, and hand you the repository.",
            ["Model it in Hyper Studio", "Connect your systems with Atlas", "Ship agents with Agentic Studio"], C, "you")]
    exh = "".join(f'<div class="ex"><div>{monitor(ex_screen(k))}</div><div><h4>{E(t)}</h4><p class="mu">{E(d)}</p><a class="exf" href="{u}">EXPLORE →</a>'
                  f'<div class="chk">{"".join(f"<div><i>✓</i><span>{E(c)}</span></div>" for c in cs)}</div><a class="pill" href="{u}">START BUILDING</a></div></div>' for t, d, cs, u, k in exs)
    examples = f'<section class="sec lt" id="examples"><div class="w"><p class="shd">2&gt; Hyper Examples</p>{exh}</div></section>'
    arrow = '<div class="pa" aria-hidden="true">' + "".join(f'<i class="{"" if c == "1" else "x"}"></i>' for c in "00100" "00010" "11111" "00010" "00100") + "</div>"
    comm = (f'<section class="sec" id="community"><div class="w"><p class="shd">3&gt; Ready to get started?</p><h2 class="big3">Build with the people <em>who build Hyper.</em></h2>'
            '<div class="cards4">'
            f'<a href="#docs"><span>READ</span><div><h4>Read the docs</h4><p>Ontology as code, semantics, kinetics, Atlas and Agentic Studio.</p></div></a>'
            f'<a id="hack" href="{C}"><span>HACK</span><div><h4>Book a build day</h4><p>Bring one operation. Leave with its ontology exported to your repository.</p></div></a>'
            f'<a href="{C}"><span>COMMUNITY</span><div><h4>Talk to an engineer</h4><p>Ask the team that writes the generator, not a sales script.</p></div></a>'
            f'<a href="https://github.com/muhammadumar89/codeninja-research/tree/main/hyper-ontology-py"><span>CODE</span><div><h4>Read the loader</h4><p>Inspect, validate and convert ontology packages in Python.</p></div></a></div>'
            f'<a class="rc" id="contribute" href="https://github.com/muhammadumar89/codeninja-research/blob/main/ONTOLOGY_PACKAGE.md">{arrow}<div><h4>Ready to contribute?</h4><p>Publish an ontology package, or improve the format every package follows.</p></div></a></div></section>')
    body = f'<main class="dv">{sub}{hero}{why}{docs}{examples}{comm}</main>'
    title = "Hyper Ontology for Developers: Ontology as Code, Kinetics, Atlas and Agentic Studio | CodeNinja Atoms"
    desc = "Build on Hyper Ontology: export your ontology as code (manifest.ts and the full source), model semantics and kinetics, connect legacy systems with Atlas, ship managed agents with Agentic Studio, and serve it all to agents over MCP."
    ld = [{"@context": "https://schema.org", "@type": "TechArticle", "headline": "Hyper Ontology for developers", "description": desc, "url": DEV,
           "author": {"@type": "Organization", "name": "CodeNinja"}, "about": {"@type": "SoftwareApplication", "name": "Hyper Ontology", "url": f"{BASE}/hyper-ontology/"}}]
    return shell(title, desc, DEV, ld, CSS, body, JS)
