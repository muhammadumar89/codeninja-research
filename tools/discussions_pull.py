"""Write developer/discussions.json: the latest threads from the repository's GitHub Discussions,
read with the gh CLI (authenticated as Umar). The developer hub shows them. Run before
site_index.py on a routine day; without gh, the hub shows a 'start the first thread' link.
    python tools/discussions_pull.py
"""
import json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
Q = """{repository(owner:"muhammadumar89",name:"codeninja-research"){discussions(first:8,orderBy:{field:UPDATED_AT,direction:DESC}){nodes{title url updatedAt category{name} author{login} comments{totalCount}}}}}"""


def main():
    r = subprocess.run(["gh", "api", "graphql", "-f", f"query={Q}"], capture_output=True, text=True)
    if r.returncode:
        print("discussions: gh failed, keeping the previous file"); return
    nodes = json.loads(r.stdout)["data"]["repository"]["discussions"]["nodes"]
    out = [{"title": n["title"], "url": n["url"], "date": n["updatedAt"][:10], "category": n["category"]["name"],
            "author": (n["author"] or {}).get("login", ""), "comments": n["comments"]["totalCount"]} for n in nodes]
    (ROOT / "developer").mkdir(exist_ok=True)
    (ROOT / "developer" / "discussions.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"discussions: {len(out)} threads")


if __name__ == "__main__":
    main()
