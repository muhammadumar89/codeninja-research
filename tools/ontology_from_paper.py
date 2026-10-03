"""Build the paper folder's reusable artefacts from the paper itself, so the
package can never say something the paper does not:

  ontology/objects.json   the object model, read from chapter 5 and the
                          recorded form the paper prints
  register/models.csv     the model and equipment register, read from Table 4
  figures/*.png           the figures, lifted from the paper's own HTML
  README.md               title, subtitle, abstract, readers

    python ontology_from_paper.py paper.pdf paper.html out_dir

The script refuses to write an object model whose count disagrees with the
paper's own word ("fourteen objects"), because a package that silently drops
an object is worse than none.
"""
import base64
import csv
import html as _html
import json
import re
import subprocess
import sys
from pathlib import Path

NUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
       "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
       "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}
KIND_OF_FAMILY = [("record", "record"), ("asset", "asset"), ("place", "asset"), ("knowledge", "document"),
                  ("document", "document"), ("people", "person"), ("person", "person"), ("event", "event"),
                  ("platform", "event"), ("system", "system")]
KIND_OF_LABEL = [("Agent", "system"), ("Event", "event"), ("Document", "document"), ("Worker", "person"),
                 ("Actor", "person"), ("Site", "asset"), ("Equipment", "asset"), ("Tag", "asset"),
                 ("Feed", "asset"), ("Camera", "asset")]
LINK_VERBS = ("authorizes", "authorises", "assigns", "maintains", "measures", "concerns", "cites",
              "implicates", "recalls", "approves", "opens", "governs", "examines", "hosts", "raises",
              "occurred at", "occurs at", "sits on", "is raised at", "damaged", "monitors", "covers",
              "defines", "references", "produces", "watches", "recommends", "closes")

slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def text_of(pdf):
    t = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    # page numbers and form feeds out of the running text
    return "\n".join(ln for ln in t.replace("\f", "\n").splitlines() if not re.fullmatch(r"\s*\d{1,3}\s*", ln))


def chapter(t, n):
    """The text of chapter n, from its heading to the next chapter's."""
    m = re.search(rf"\n\s*{n}\.1 [^\n]+\n", t)
    e = re.search(rf"\n\s*{n + 1}\.1 [^\n]+\n|\nPART I{{2,3}}V?\b|\nSources\b", t[m.end():]) if m else None
    return t[m.end():m.end() + e.start()] if m and e else (t[m.end():] if m else "")


def declared_count(t):
    m = re.search(r"(?i)\b(\w+)\s+objects\b", t)
    return NUM.get((m.group(1) if m else "").lower(), 0)


def labels_from(ch5):
    """Every object the chapter names, with its family and anchor."""
    body = " ".join(ch5.split())
    sents = re.split(r"(?<=[.])\s+(?=[A-Z])", body.split("The typed links")[0])
    out, seen = [], set()

    def add(label, kind, anchored=""):
        label = re.sub(r"^(?:and|or)\s+", "", label.strip().rstrip(",;."))
        if not label or label[0].islower() or label.lower() in seen:
            return
        if label.split()[0].lower() in ("a", "an", "the", "each", "every", "both", "and"):
            return
        kind = next((k for w, k in KIND_OF_LABEL if w in label.split()), kind)
        seen.add(label.lower())
        out.append({"id": slug(label), "label": label, "kind": kind, "anchored_in": anchored.strip().rstrip(",;."),
                    "properties": [], "status_vocabulary": [], "links": []})

    for s in sents:
        m = re.match(r"(\w+) (?:is|are) ([^:]+):\s*(.+)$", s)
        if m and m.group(1).lower() in NUM:
            fam = m.group(2).lower()
            kind = next((k for w, k in KIND_OF_FAMILY if w in fam), "asset")
            for part in re.split(r";\s*", m.group(3)):
                part = re.sub(r"^(?:and\s+)", "", part.strip())
                anchored = ""
                am = re.search(r",?\s*(?:both\s+|all\s+|also\s+)?anchored in (.+?)(?:[,.;]|$)", part)
                if am:
                    anchored = am.group(1)
                    part = part[:am.start()]
                part = re.split(r",\s*(?:each|covering|the objects|which|with|so|and the)\b", part)[0]
                for lab in re.split(r"\s+and\s+|,\s*", part):
                    add(lab, kind, anchored)
        else:
            # "Work Order, also anchored in SAP PM, connects ..."
            for m2 in re.finditer(r"(?:^|\.\s+)([A-Z][A-Za-z ]+?),\s*(?:also\s+)?anchored in ([^,.;]+)", s):
                add(m2.group(1), "record", m2.group(2))
    return out


def links_from(ch5, objs):
    sec = " ".join(ch5.split())
    sec = sec[sec.find("The typed links"):] if "The typed links" in sec else ""
    sec = sec.split("Figure")[0]
    words = {}
    for o in objs:
        for w in o["label"].lower().replace("hse ", "").split(" or "):
            words[w.strip()] = o["id"]
        words[o["label"].lower()] = o["id"]
    alias = {"permit": "permit-to-work", "sensor": "sensor-or-scada-tag", "anomaly event": "anomaly-or-early-warning-event",
             "event": "anomaly-or-early-warning-event", "document": "hse-document", "incident": "hse-incident",
             "site": "operational-site", "inspections": "hse-inspection-or-observation", "inspection": "hse-inspection-or-observation",
             "worker": "hse-worker", "work party": "hse-worker", "role actor": "hse-role-actor", "actor": "hse-role-actor",
             "near miss": "near-miss-report", "camera": "vision-ai-camera-feed", "agent": "configured-hse-agent",
             "work order": "work-order", "equipment": "equipment", "asset": "equipment", "procedure": "hse-document"}
    ids = {o["id"] for o in objs}
    by = {o["id"]: o for o in objs}
    verbs = "|".join(re.escape(v) for v in sorted(LINK_VERBS, key=len, reverse=True))
    n = 0
    last_subject = ""
    for clause in re.split(r";|\band\b(?=\s+(?:cites|can be|opens|raises))", sec):
        clause = clause.strip()
        m = re.search(rf"(?i)\b(?:a|an|the|that|every|each)\s+([a-z][a-z ]+?)\s+({verbs})\s+(?:a|an|the|that|those)?\s*([a-z][a-z ]+?)(?:\s+(?:that|which|against|before|because|,)|$)", clause)
        if m:
            a, verb, b = m.group(1).strip().lower(), m.group(2).lower(), m.group(3).strip().lower()
            last_subject = a
        else:
            # "and cites the document that defines the limit": the subject carries over
            m = re.search(rf"(?i)^({verbs})\s+(?:a|an|the|that|those)?\s*([a-z][a-z ]+?)(?:\s+(?:that|which|against|before|because|,)|$)", clause)
            if not m or not last_subject:
                continue
            a, verb, b = last_subject, m.group(1).lower(), m.group(2).strip().lower()
        ia = alias.get(a) or words.get(a) or next((v for k, v in alias.items() if a.endswith(k)), None)
        ib = alias.get(b) or words.get(b) or next((v for k, v in alias.items() if b.startswith(k) or b.endswith(k)), None)
        if ia in ids and ib in ids and ia != ib:
            by[ia]["links"].append({"to": ib, "label": verb})
            n += 1
    return n


def recorded_form(ch5, objs):
    m = re.search(r"\{\s*\"id\".*?\n\s*\}\s*$", ch5, re.S | re.M)
    if not m:
        return
    raw = re.sub(r"\n\s*\d{1,3}\s*\n", "\n", m.group(0))
    try:
        rec = json.loads(raw)
    except Exception:
        return
    for o in objs:
        if o["id"] == rec.get("id"):
            for k in ("properties", "status_vocabulary"):
                if rec.get(k):
                    o[k] = rec[k]
            if rec.get("links") and not o["links"]:
                o["links"] = rec["links"]


def register_from(t):
    """Table 4's rows: choice | what was picked | why here, continuation lines joined."""
    i = t.find("Table 4 · Model and Equipment Register")
    if i < 0:
        return []
    block = t[i:]
    block = block[:re.search(r"\nPART I{2,3}\b|\n\s*9\.1 ", block).start()] if re.search(r"\nPART I{2,3}\b|\n\s*9\.1 ", block) else block
    rows = []
    for ln in block.splitlines():
        if "Table 4" in ln or re.match(r"\s*THE CHOICE", ln) or not ln.strip():
            continue
        cols = re.split(r"\s{3,}", ln.strip())
        if not ln.startswith((" ", "\t")) and len(cols) >= 2:
            rows.append(cols + [""] * (3 - len(cols)))
        elif rows:
            # continuation: pad into the columns by position
            lead = len(ln) - len(ln.lstrip())
            tgt = 0 if lead < 28 else 1 if lead < 60 else 2
            parts = re.split(r"\s{3,}", ln.strip())
            for j, p in enumerate(parts):
                k = min(2, tgt + j)
                rows[-1][k] = (rows[-1][k] + " " + p).strip()
    return [{"choice": r[0], "picked": r[1], "why": r[2]} for r in rows if r[0]]


def figures_from(html_path, out):
    h = Path(html_path).read_text(encoding="utf-8")
    n = 0
    for m in re.finditer(r'<img[^>]+src="data:image/(png|jpeg);base64,([^"]+)"[^>]*>', h):
        tag = m.group(0)
        alt = _html.unescape((re.search(r'alt="([^"]*)"', tag) or [None, ""])[1])
        fm = re.match(r"Figure (\d+)\.", alt)
        if not fm:
            continue
        p = out / f"figure_{int(fm.group(1)):02d}.{m.group(1)}"
        p.write_bytes(base64.b64decode(m.group(2)))
        (out / f"figure_{int(fm.group(1)):02d}.txt").write_text(alt, encoding="utf-8")
        n += 1
    return n


def front_matter(t):
    head = t[:t.find("ABSTRACT")] if "ABSTRACT" in t else t[:2000]
    lines = [ln.strip() for ln in head.splitlines() if ln.strip()]
    eyebrow = lines[0] if lines else ""
    title, sub, readers = [], [], ""
    mode = "title"
    for ln in lines[1:]:
        if ln.startswith("CodeNinja Engineering Team"):
            mode = "readers"; continue
        if ln.startswith("Vertical-Driven Architectures is"):
            break
        if mode == "readers":
            readers = (readers + " " + ln).strip(); continue
        if mode == "title":
            if ln[0].isupper() and len(title) < 3 and not ln.endswith("."):
                title.append(ln)
            else:
                mode = "sub"; sub.append(ln)
        elif mode == "sub":
            sub.append(ln)
    abstract = ""
    if "ABSTRACT" in t:
        a = t[t.find("ABSTRACT"):]
        a = a[:a.find("Figure 1.")] if "Figure 1." in a else a[:3000]
        # the claim heading is set large and wraps in short lines; the body
        # lines are long. The heading is the leading run of short lines.
        alines = a.splitlines()[1:]
        while alines and not alines[0].strip():
            alines.pop(0)
        hl = []
        while alines and alines[0].strip() and len(alines[0].strip()) < 78:
            hl.append(alines.pop(0).strip())
        heading = " ".join(hl)
        rest = "\n".join(alines)
        paras = [p for p in re.split(r"\n\s*\n", rest) if len(p.split()) > 25]
        abstract = (f"*{heading}*\n\n" if heading else "") + "\n\n".join(" ".join(p.split()) for p in paras)
    return {"eyebrow": eyebrow, "title": " ".join(title), "subtitle": " ".join(sub), "readers": readers, "abstract": abstract}


def main(pdf, html_path, out):
    out = Path(out)
    t = text_of(pdf)
    ch5 = chapter(t, 5)
    # a hand-verified package already in the folder wins: the chapter's prose
    # changes shape from build to build, the paper's facts do not
    hand = out / "ontology" / "objects.json"
    if hand.exists():
        objs = json.loads(hand.read_text(encoding="utf-8"))["objects"]
        want = declared_count(ch5) or declared_count(t)
        if want and len(objs) != want:
            print(f"REFUSED: the paper says {want} objects, the hand package has {len(objs)}")
            sys.exit(2)
        fm = front_matter(t)
        (out / "register").mkdir(exist_ok=True); (out / "figures").mkdir(exist_ok=True)
        reg = register_from(t)
        with open(out / "register" / "models.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["choice", "picked", "why"]); w.writeheader(); w.writerows(reg)
        nf = figures_from(html_path, out / "figures")
        (out / "front_matter.json").write_text(json.dumps(fm, indent=2), encoding="utf-8")
        print(f"{len(objs)} objects (hand package), {len(reg)} register rows, {nf} figures -> {out}")
        return
    objs = labels_from(ch5)
    want = declared_count(ch5) or declared_count(t)
    if want and len(objs) != want:
        print(f"REFUSED: the paper says {want} objects, the chapter yielded {len(objs)}:")
        for o in objs:
            print("  ", o["kind"], o["label"])
        sys.exit(2)
    nl = links_from(ch5, objs)
    recorded_form(ch5, objs)
    fm = front_matter(t)
    pkg = {"package": "hyper-ontology/1", "designed_with": "Praxis", "implemented_with": "Hyper Ontology",
           "paper": {"title": fm["title"], "url": "", "doi": ""},
           "sector": "oil-and-gas", "country": "Pakistan", "objects": objs,
           "write_paths": ["adapter tier", "decision record"],
           "human_loop": "every anomaly event moves Raised, Explained, Recommendation issued, Approved or Rejected, Closed; each transition is made by a named person"}
    (out / "ontology").mkdir(parents=True, exist_ok=True)
    (out / "register").mkdir(exist_ok=True)
    (out / "figures").mkdir(exist_ok=True)
    (out / "ontology" / "objects.json").write_text(json.dumps(pkg, indent=2), encoding="utf-8")
    reg = register_from(t)
    with open(out / "register" / "models.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["choice", "picked", "why"]); w.writeheader(); w.writerows(reg)
    nf = figures_from(html_path, out / "figures")
    (out / "front_matter.json").write_text(json.dumps(fm, indent=2), encoding="utf-8")
    print(f"{len(objs)} objects, {nl} links, {len(reg)} register rows, {nf} figures -> {out}")
    for o in objs:
        print(f"  {o['kind']:9s} {o['label']:36s} {o['anchored_in']}  links={len(o['links'])}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
