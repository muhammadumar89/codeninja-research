"""hyper-ontology CLI.

    hyper-ontology list                         the designs published in the CodeNinja research index
    hyper-ontology show <path|url|slug>         a summary of one package
    hyper-ontology validate <path|url|slug>     exit 1 and print problems if the package is invalid
    hyper-ontology mermaid <path|url|slug>      a Mermaid class diagram
    hyper-ontology cypher <path|url|slug>       Cypher that loads the model into a graph database
    hyper-ontology jsonld <path|url|slug>       the model as JSON-LD
    hyper-ontology reach <path|url|slug> <id>   the typed paths one object reaches, two hops out
"""
import json
import re
import sys
import urllib.request
from .core import INDEX, load, validate, summary, to_mermaid, to_cypher, to_jsonld, traverse


def _list():
    with urllib.request.urlopen(INDEX + "llms.txt", timeout=30) as r:
        text = r.read().decode("utf-8")
    for m in re.finditer(r"\(" + re.escape(INDEX) + r"([a-z0-9-]+)/ontology/objects\.json\)", text):
        print(m.group(1))


def main(argv=None):
    a = list(sys.argv[1:] if argv is None else argv)
    if not a or a[0] in ("-h", "--help", "help"):
        print(__doc__); return 0
    cmd = a[0]
    if cmd == "list":
        _list(); return 0
    if len(a) < 2:
        print(__doc__); return 2
    pkg = load(a[1])
    if cmd == "show":
        print(summary(pkg))
    elif cmd == "validate":
        probs = validate(pkg)
        for p in probs: print("problem:", p)
        print("valid" if not probs else f"{len(probs)} problem(s)")
        return 1 if probs else 0
    elif cmd == "mermaid":
        print(to_mermaid(pkg))
    elif cmd == "cypher":
        print(to_cypher(pkg))
    elif cmd == "jsonld":
        print(json.dumps(to_jsonld(pkg), indent=2, ensure_ascii=False))
    elif cmd == "reach":
        if len(a) < 3: print("reach needs an object id"); return 2
        for p in traverse(pkg, a[2]): print(p)
    else:
        print(__doc__); return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
