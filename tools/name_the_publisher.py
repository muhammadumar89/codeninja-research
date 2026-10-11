"""One-time migration (ep11, 11 Oct 2026): the published design pages never named the
publisher of the series on their first screen. They read 'a CodeNinja series of system
designs ... designed on Praxis, CodeNinja's platform', and the only brand text above it
was the bare word 'Atoms', which Google resolves to another company. The platform
(~/hijrah-demo/paper.py) now writes the full names for new papers; this rewrites the
series line in the already published web editions and paper copies. HTML and Markdown
only: the PDFs, DOCX and Zenodo records of record keep the line they were published with.
Idempotent."""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAIRS = [
    ("Vertical-Driven Architectures is a CodeNinja series of system designs.",
     "Vertical-Driven Architectures is a CodeNinja Atoms series of system designs."),
    ("designed on Praxis, CodeNinja's platform for designing physical AI systems",
     "designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems"),
    ("designed on Praxis, CodeNinja\u2019s platform for designing physical AI systems",
     "designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems"),
    ("designed on Praxis, CodeNinja&#x27;s platform for designing physical AI systems",
     "designed on CodeNinja Praxis, the CodeNinja Atoms platform for designing physical AI systems"),
]

def run():
    changed = []
    for p in sorted(ROOT.glob("*/index.html")) + sorted(ROOT.glob("*/index.md")) + sorted(ROOT.glob("*/paper/*.html")):
        t = p.read_text(encoding="utf-8")
        o = t
        for a, b in PAIRS:
            t = t.replace(a, b)
        if t != o:
            p.write_text(t, encoding="utf-8")
            changed.append(str(p.relative_to(ROOT)))
    for c in changed:
        print("  " + c)
    print(f"named the publisher in {len(changed)} files")
    return changed

if __name__ == "__main__":
    sys.exit(0 if run() is not None else 1)
