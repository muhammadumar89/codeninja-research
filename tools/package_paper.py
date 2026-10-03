"""Assemble one paper folder from the platform's three files and the cost
appendix, in one command, so every paper ships the same way:

    python package_paper.py <folder> <paper.pdf> <paper.html> <paper.docx> <appendix.md> <site-slug>

Writes: paper/<slug>.pdf (with the appendix merged), paper/<slug>.html,
paper/<slug>.docx, paper/appendix_a_cost.md, ontology/, register/, figures/,
README.md. Refuses if the extractor refuses.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main(folder, pdf, html, docx, appendix, slug):
    f = Path(folder)
    (f / "paper").mkdir(parents=True, exist_ok=True)
    py = sys.executable
    r = subprocess.run([py, str(HERE / "ontology_from_paper.py"), pdf, html, str(f)])
    if r.returncode:
        sys.exit(r.returncode)
    subprocess.run([py, str(HERE / "appendix_pdf.py"), appendix, pdf, str(f / "paper" / f"{slug}.pdf")], check=True)
    shutil.copy(html, f / "paper" / f"{slug}.html")
    shutil.copy(docx, f / "paper" / f"{slug}.docx")
    shutil.copy(appendix, f / "paper" / "appendix_a_cost.md")
    fm = json.loads((f / "front_matter.json").read_text(encoding="utf-8"))
    pkg = json.loads((f / "ontology" / "objects.json").read_text(encoding="utf-8"))
    pkg["paper"]["url"] = f"https://codeninjaconsulting.com/research/{slug}"
    (f / "ontology" / "objects.json").write_text(json.dumps(pkg, indent=2), encoding="utf-8")
    objs = pkg["objects"]
    kinds = {}
    for o in objs:
        kinds.setdefault(o["kind"], []).append(o["label"])
    readme = f"""# {fm['title']}

*{fm['eyebrow']}*

{fm['subtitle']}

{fm['readers']}

**Canonical page:** https://codeninjaconsulting.com/research/{slug}
**Paper:** [PDF](paper/{slug}.pdf) · [HTML](paper/{slug}.html) · [Word](paper/{slug}.docx) · [Appendix A, what ownership costs over three years](paper/appendix_a_cost.md)
**Licence:** CC BY 4.0. Cite the DOI on the release, or the canonical page.

## Abstract

{fm['abstract']}

## The object model

`ontology/objects.json` holds the {len(objs)} objects as Hyper Ontology input (format `hyper-ontology/1`, see [ONTOLOGY_PACKAGE.md](../ONTOLOGY_PACKAGE.md)). Designed with Praxis, implemented with Hyper Ontology.

| Kind | Objects |
|---|---|
""" + "\n".join(f"| {k} | {', '.join(v)} |" for k, v in kinds.items()) + f"""

## The model and equipment register

`register/models.csv`, read from the paper's Table 4: every model, its licence and weight, every hardware class and sizing rule.

## Figures

`figures/figure_01.png` to `figure_09.png`, each with its caption in the matching `.txt`. The operator is described by class, never by name.

## How it was built

Designed on Praxis, CodeNinja's platform for designing physical AI systems. The platform scrubs the operator from text and figures and refuses to publish a file that still carries the operator's words. The country is the FDE's statement of where the design is written to run.
"""
    (f / "README.md").write_text(readme, encoding="utf-8")
    (f / "front_matter.json").unlink(missing_ok=True)
    print(f"packaged {slug}: {len(objs)} objects")


if __name__ == "__main__":
    main(*sys.argv[1:7])
