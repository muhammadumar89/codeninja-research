"""Rebuild the crawlable index for every paper in this repository: the research
index page (index.html at the repo root, served by GitHub Pages), sitemap.xml
and llms.txt. Run after adding or changing a paper folder.

    python tools/site_index.py
"""
import datetime
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://muhammadumar89.github.io/codeninja-research"


def papers():
    out = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and (p / "index.html").exists() and not p.name.startswith(".")):
        h = (d / "index.html").read_text(encoding="utf-8")
        g = lambda name: (re.search(rf'<meta name="{name}" content="([^"]*)"', h) or [None, ""])[1]
        pdf = next(iter(sorted((d / "paper").glob("*.pdf"))), None) if (d / "paper").exists() else None
        out.append({"slug": d.name, "title": html.unescape(g("citation_title")),
                    "description": html.unescape((re.search(r'<meta property="og:description" content="([^"]*)"', h) or [None, ""])[1]),
                    "date": g("citation_publication_date").replace("/", "-"), "doi": g("citation_doi"),
                    "pdf": f"{BASE}/{d.name}/paper/{pdf.name}" if pdf else "",
                    "ontology": f"{BASE}/{d.name}/ontology/objects.json" if (d / "ontology" / "objects.json").exists() else ""})
    return sorted(out, key=lambda p: p["date"], reverse=True)


def main():
    ps = papers()
    today = datetime.date.today().isoformat()
    rows = "\n".join(
        f'<li><a href="{p["slug"]}/"><strong>{html.escape(p["title"])}</strong></a><br>'
        f'<span>{html.escape(p["description"])}</span><br>'
        f'<small>{p["date"]} · <a href="{p["pdf"]}">PDF</a>'
        + (f' · <a href="{p["ontology"]}">ontology JSON</a>' if p["ontology"] else "")
        + (f' · DOI <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>' if p["doi"] else "")
        + "</small></li>" for p in ps)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "CodeNinja Research",
          "description": "Open reference architectures for sovereign AI in physical operations.",
          "url": f"{BASE}/", "publisher": {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"},
          "hasPart": [{"@type": "TechArticle", "headline": p["title"], "url": f"{BASE}/{p['slug']}/"} for p in ps]}
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CodeNinja Research: open reference architectures for sovereign AI in physical operations</title>
<meta name="description" content="Open reference architectures for sovereign AI in physical operations: designs an operator can run on its own hardware, under open-weight licences, with no data leaving the country.">
<link rel="canonical" href="{BASE}/"><link rel="alternate" type="application/atom+xml" href="{BASE}/feed.xml">
<script type="application/ld+json">{json.dumps(ld)}</script>
<style>body{{margin:0;font:16px/1.6 Arial,Helvetica,sans-serif;color:#222;background:#fff}}main{{max-width:760px;margin:0 auto;padding:40px 20px}}h1{{color:#1F3348}}li{{margin:0 0 22px}}span{{color:#555}}small{{color:#6B7683}}a{{color:#1F3348}}</style></head>
<body><main><p style="letter-spacing:.18em;color:#B7791F;font-weight:700;font-size:11px">CODENINJA RESEARCH</p>
<h1>Open reference architectures for sovereign AI in physical operations</h1>
<p>Every design here runs on the operator's own hardware, under open-weight licences, with no data leaving the country. Each paper ships with its object model as JSON, its model register and a cost appendix. Text, figures and data are CC BY 4.0.</p>
<ul style="list-style:none;padding:0">{rows}</ul>
<p><small>Source files: <a href="https://github.com/muhammadumar89/codeninja-research">github.com/muhammadumar89/codeninja-research</a> · Updated {today}</small></p></main></body></html>"""
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    urls = [f"{BASE}/"] + [f"{BASE}/{p['slug']}/" for p in ps] + [p["pdf"] for p in ps if p["pdf"]]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    entries = "".join(f"""  <entry><title>{html.escape(p['title'])}</title><link href="{BASE}/{p['slug']}/"/><id>{BASE}/{p['slug']}/</id><updated>{p['date']}T00:00:00Z</updated><summary>{html.escape(p['description'])}</summary></entry>\n""" for p in ps)
    (ROOT / "feed.xml").write_text(f'<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom"><title>CodeNinja Research</title><link href="{BASE}/"/><link rel="self" href="{BASE}/feed.xml"/><id>{BASE}/</id><updated>{today}T00:00:00Z</updated>\n{entries}</feed>\n', encoding="utf-8")
    llms = ["# CodeNinja Research", "",
            "> Open reference architectures for sovereign AI in physical operations: designs an operator can run on its own hardware, under open-weight licences, with no data leaving the country. CC BY 4.0.", "",
            "## Papers", ""]
    for p in ps:
        llms.append(f"- [{p['title']}]({BASE}/{p['slug']}/): {p['description']}" + (f" DOI {p['doi']}." if p["doi"] else ""))
        if p["ontology"]:
            llms.append(f"  - [Object model as JSON]({p['ontology']})")
    (ROOT / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
    print(f"{len(ps)} paper(s): index.html, sitemap.xml, feed.xml, llms.txt")


if __name__ == "__main__":
    main()
