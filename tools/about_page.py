"""The About page: the mission of CodeNinja Atoms, then the executive leadership, one row per
person (name panel beside a black and white portrait), then the ownership line.
    python tools/about_page.py
Portraits live in about/img/ (greyscale, 6:5). Founders come from codeninjaconsulting.com/about;
Ibrar Hussain's title and degree come from his public profiles.
"""
import html, json, datetime
from pathlib import Path
import brand
ROOT = Path(__file__).resolve().parent.parent
BASE = "https://codeatoms.ai"
E = lambda s: html.escape(str(s), quote=True)

MISSION = [
    "The most important assets of nation-states, governments, and enterprises — our defense institutions, our energy grids, our border controls, our oil and gas facilities — all exist in the physical world.",
    "While we are passionate about optimizing all this physical infrastructure using AI, we cannot simply outsource these critical assets to one or two extremely centralized AI companies. The only way to defend these institutions and this critical infrastructure is to build a Sovereign AI operating system for the physical world.",
    "And that is the mission of CodeNinja Atoms.",
]

# Order fixed by Umar: Mukhtar, Adil, Umar, Ibrar.
LEADERS = [
    {"slug": "mukhtar-ahmad-baig", "name": "Mukhtar Ahmad Baig", "title": "Co-Founder and Chief Executive Officer",
     "bio": "Mr. Baig is one of the co-founders of CodeNinja and serves as its Chief Executive Officer. CodeNinja began as an engineering firm in Lahore in 2014 and now builds systems for enterprises, governments and critical operations across the United States and the Gulf.",
     "link": "https://www.linkedin.com/in/mukhtarahmadbaig/"},
    {"slug": "adil-khalil", "name": "Adil Khalil", "title": "Co-Founder and Chief Technology Officer",
     "bio": "Mr. Khalil is one of the co-founders of CodeNinja and serves as its Chief Technology Officer, responsible for the engineering behind CodeNinja's sovereign systems.",
     "link": "https://www.linkedin.com/in/adilkhalil/"},
    {"slug": "muhammad-umar-bilal", "name": "Muhammad Umar Bilal", "title": "Co-Founder and Chief Operating Officer",
     "bio": "Mr. Bilal is one of the co-founders of CodeNinja and serves as its Chief Operating Officer. He works on Hyper Anthologies, the memory and interpretability layer underneath CodeNinja's enterprise AI deployments, and is the author of the Own the Loop research series.",
     "link": "https://www.linkedin.com/in/muhammadumargiki/"},
    {"slug": "ibrar-hussain", "name": "Ibrar Hussain", "title": "Co-Founder and Chief Product Officer",
     "bio": "Mr. Hussain is one of the co-founders of CodeNinja and serves as its Chief Product Officer. Mr. Hussain holds a B.S. in Computer Science from the University of the Punjab.",
     "link": "https://pk.linkedin.com/in/helloibrar"},
]

CSS = """
.about{max-width:var(--max);margin:0 auto;padding:148px var(--gutter) 120px}
.about h1{font-weight:300;font-size:clamp(40px,5.4vw,76px);line-height:1.02;letter-spacing:-.034em;margin:0 0 56px;color:var(--ink)}
.mission{display:grid;grid-template-columns:220px 1fr;gap:24px 48px;border-top:1px solid var(--ink);padding-top:28px;margin-bottom:120px}
.mission p.stmt{font-family:var(--serif);font-weight:300;font-size:clamp(22px,2.4vw,32px);line-height:1.36;letter-spacing:-.012em;color:var(--ink);margin:0 0 28px;max-width:34ch}
.mission p.stmt:last-child{margin-bottom:0;font-weight:400}
.leaders-h{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--ink);padding-top:28px;margin-bottom:40px}
.leaders-h h2{font-size:clamp(30px,3.6vw,48px);margin:0;color:var(--ink);max-width:none}
.leader{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:8px}
.leader .panel{background:var(--paper2);padding:36px 40px;display:flex;flex-direction:column}
.leader .panel h3{font-family:var(--sans);font-weight:300;font-size:clamp(26px,2.5vw,36px);line-height:1.1;letter-spacing:-.025em;color:var(--ink);margin:0 0 14px}
.leader .panel .role{font-size:16px;line-height:1.45;color:var(--ink);margin:0 0 auto;padding-bottom:40px}
.leader .panel .bio{font-size:15.5px;line-height:1.62;color:var(--muted-l);margin:0;max-width:52ch}
.leader .panel a.in{font-family:var(--mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted-l);text-decoration:none;margin-top:18px}
.leader .panel a.in:hover{color:var(--ink)}
.leader figure{margin:0;background:#d9d9d6;aspect-ratio:6/5;overflow:hidden}
.leader figure img{width:100%;height:100%;object-fit:cover;display:block;filter:grayscale(1)}
.owner{border-top:1px solid var(--ink);margin-top:112px;padding-top:28px;font-family:var(--serif);font-weight:300;font-size:clamp(20px,2vw,26px);line-height:1.4;color:var(--ink)}
.owner a{text-decoration-thickness:1px;text-underline-offset:4px}
@media (max-width:820px){.about{padding:112px var(--gutter) 80px}.mission{grid-template-columns:1fr;margin-bottom:80px}
.leader{grid-template-columns:1fr}.leader figure{order:-1}.leader .panel{padding:24px 20px}.leader .panel .role{padding-bottom:20px}.leaders-h{flex-direction:column;gap:8px}}
"""


def main():
    nav = [("Research", f"{BASE}/#research"), ("Praxis", f"{BASE}/praxis/"), ("Hyper Ontology", f"{BASE}/hyper-ontology/"), ("Data", f"{BASE}/#data"), ("About", f"{BASE}/about/")]
    desc = "CodeNinja Atoms is building a sovereign AI operating system for the physical world. Its mission and its executive leadership."
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "CodeNinja Atoms", "url": BASE,
           "parentOrganization": {"@type": "Organization", "name": "CodeNinja", "url": brand.PARENT},
           "founder": [{"@type": "Person", "name": p["name"], "jobTitle": p["title"], "sameAs": p["link"]} for p in LEADERS]}
    page_ld = {"@context": "https://schema.org", "@type": "AboutPage", "name": "About CodeNinja Atoms", "url": f"{BASE}/about/", "description": desc}
    mission = "".join(f'<p class="stmt">{E(p)}</p>' for p in MISSION)
    rows = "".join(f"""<article class="leader" id="{p['slug']}"><div class="panel"><h3>{E(p['name'])}</h3><p class="role">—{E(p['title'])}</p><p class="bio">{E(p['bio'])}</p><a class="in" href="{p['link']}" rel="noopener">LinkedIn</a></div>
<figure><img src="img/{p['slug']}.jpg" alt="{E(p['name'])}" width="900" height="750" loading="{'eager' if i == 0 else 'lazy'}"></figure></article>
""" for i, p in enumerate(LEADERS))
    out = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>About CodeNinja Atoms</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{BASE}/about/">
<meta property="og:type" content="website"><meta property="og:title" content="About CodeNinja Atoms"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{BASE}/about/">
<meta property="og:image" content="{BASE}/about/img/{LEADERS[0]['slug']}.jpg">
<script type="application/ld+json">{json.dumps(page_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(org, ensure_ascii=False)}</script>
{brand.FONTS}{brand.JS_FLAG}<style>{brand.CSS}{CSS}body{{background:var(--paper)}}html.js header.top:not(.solid):not(.open){{background:rgba(11,12,16,.94);border-bottom-color:var(--rule-d);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}}</style></head>
<body>{brand.header(BASE + "/", nav, access=f"{BASE}/praxis/#access")}
<main class="light"><div class="about">
<h1>About</h1>
<section class="mission" aria-labelledby="mission-h"><p class="eyebrow" id="mission-h">Our mission</p><div>{mission}</div></section>
<section aria-labelledby="leaders-h"><div class="leaders-h"><h2 id="leaders-h">Executive Leadership</h2><p class="eyebrow">CodeNinja founders</p></div>
{rows}</section>
<p class="owner">CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a>.</p>
</div></main>
<footer class="site"><div class="wrapf">{brand.footer_brand(BASE + "/")}<span>CodeNinja Atoms is a fully owned subsidiary of <a href="{brand.PARENT}">CodeNinja</a> · Updated {datetime.date.today().isoformat()}</span></div></footer>
{brand.SCRIPT}</body></html>"""
    (ROOT / "about").mkdir(exist_ok=True)
    (ROOT / "about" / "index.html").write_text(out, encoding="utf-8")
    print("about/index.html", len(out))


if __name__ == "__main__":
    main()
