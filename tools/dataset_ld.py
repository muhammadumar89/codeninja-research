"""Add schema.org Dataset markup so Google Dataset Search (and agents reading JSON-LD) find the
object models and the cumulative dataset. Idempotent: replaces the block tagged id="dataset-ld".

    python tools/dataset_ld.py        # every design folder, after web_edition.py and site_index.py
"""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
BASE = "https://muhammadumar89.github.io/codeninja-research"
HF = "https://huggingface.co/datasets/CodeNinjatools"
ORG = {"@type": "Organization", "name": "CodeNinja", "url": "https://codeninjaconsulting.com"}
LIC = "https://creativecommons.org/licenses/by/4.0/"
TAG = re.compile(r'<script type="application/ld\+json" id="dataset-ld">.*?</script>\n?', re.S)


def put(page: Path, ld: dict):
    h = TAG.sub("", page.read_text(encoding="utf-8"))
    block = f'<script type="application/ld+json" id="dataset-ld">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    page.write_text(h.replace("</head>", block + "</head>", 1), encoding="utf-8")


def main():
    n = 0
    for d in sorted(ROOT.iterdir()):
        f = d / "ontology" / "objects.json"
        if not f.exists() or not (d / "index.html").exists():
            continue
        h = (d / "index.html").read_text(encoding="utf-8")
        g = lambda k: (re.search(rf'<meta name="{k}" content="([^"]*)"', h) or [None, ""])[1]
        pkg = json.loads(f.read_text(encoding="utf-8")); objs = pkg["objects"]
        title = g("citation_title"); short = title.split(":")[0]
        labels = ", ".join(o["label"] for o in objs)
        desc = (f"The object model and model and equipment register from {title}, a reference architecture for physical AI "
                f"in {pkg.get('sector', '').replace('-', ' ')} ({pkg.get('country', '')}). {len(objs)} typed objects ({labels}) with properties, "
                f"status vocabularies, anchor systems and {sum(len(o.get('links', [])) for o in objs)} typed links, in the hyper-ontology/1 format: "
                "designed with Praxis, implemented with Hyper Ontology.")
        ld = {"@context": "https://schema.org", "@type": "Dataset", "name": f"{short} ontology and model register",
              "description": desc, "url": f"{BASE}/{d.name}/", "sameAs": f"{HF}/{d.name}-ontology",
              "license": LIC, "creator": ORG, "publisher": ORG, "isAccessibleForFree": True,
              "keywords": [k.strip() for k in g("citation_keywords").split(";") if k.strip()] + ["ontology", "hyper-ontology/1"],
              "spatialCoverage": {"@type": "Place", "name": pkg.get("country", "")},
              "isBasedOn": f"https://doi.org/{g('citation_doi')}" if g("citation_doi") else f"{BASE}/{d.name}/",
              "datePublished": g("citation_publication_date").replace("/", "-"),
              "includedInDataCatalog": {"@type": "DataCatalog", "name": "Vertical-Driven Architectures", "url": f"{HF}/vertical-driven-architectures"},
              "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": f"{BASE}/{d.name}/ontology/objects.json"}]
              + ([{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": f"{BASE}/{d.name}/register/models.csv"}] if (d / "register" / "models.csv").exists() else [])}
        put(d / "index.html", ld); n += 1
    designs = [json.loads(l) for l in (ROOT / "dataset" / "designs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    cat = {"@context": "https://schema.org", "@type": "Dataset", "name": "Vertical-Driven Architectures: reference architectures for physical AI",
           "description": (f"{len(designs)} complete system designs for physical AI in physical operations ("
                           + "; ".join(sorted({f"{x['sector']} in {x['country']}" for x in designs}))
                           + "), as five tables: designs, ontology objects, model and hardware choices, three-year cost lines, and full text. "
                           "Every design was reasoned on Praxis and ships an object model for Hyper Ontology. CC BY 4.0."),
           "url": f"{BASE}/#data", "sameAs": f"{HF}/vertical-driven-architectures", "license": LIC, "creator": ORG, "publisher": ORG,
           "isAccessibleForFree": True, "keywords": ["physical AI", "sovereign AI", "reference architecture", "ontology", "system design", "open-weight models"],
           "hasPart": [{"@type": "Dataset", "name": x["title"].split(":")[0], "url": x["canonical_url"] or f"{BASE}/{x['design_id']}/"} for x in designs],
           "distribution": [{"@type": "DataDownload", "encodingFormat": "application/x-ndjson",
                             "contentUrl": f"https://raw.githubusercontent.com/muhammadumar89/codeninja-research/main/dataset/{t}.jsonl"}
                            for t in ("designs", "objects", "models", "costs", "fulltext")]}
    put(ROOT / "index.html", cat)
    print(f"dataset markup: {n} designs + catalog")


if __name__ == "__main__":
    main()
