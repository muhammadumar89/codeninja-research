"""Render the cost appendix (a small Markdown subset) as PDF pages in the
paper's house style, and merge them into the platform's PDF before its
Source Register page.

    python appendix_pdf.py appendix.md paper.pdf out.pdf
"""
import io
import re
import sys

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

NAVY, AMBER, GREY, INK = (colors.HexColor(c) for c in ("#1F3348", "#B7791F", "#6B7683", "#222222"))
TINT, ALINE, CLINE = (colors.HexColor(c) for c in ("#FBF4E7", "#E8D4AE", "#D9DEE4"))
F, FB, FI = "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"
S = {
    "eyebrow": ParagraphStyle("eyebrow", fontName=FB, fontSize=8, leading=11, textColor=AMBER, spaceAfter=6),
    "h1": ParagraphStyle("h1", fontName=F, fontSize=20, leading=25, textColor=NAVY, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName=F, fontSize=12, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=4),
    "body": ParagraphStyle("body", fontName=F, fontSize=10, leading=12.5, textColor=INK, spaceAfter=7),
    "bullet": ParagraphStyle("bullet", fontName=F, fontSize=10, leading=12.5, textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=4),
    "small": ParagraphStyle("small", fontName=F, fontSize=8.5, leading=11, textColor=INK, spaceAfter=3),
    "cell": ParagraphStyle("cell", fontName=F, fontSize=8, leading=10, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName=FB, fontSize=8, leading=10, textColor=NAVY),
    "th": ParagraphStyle("th", fontName=FB, fontSize=6.5, leading=9, textColor=AMBER),
}
CW = letter[0] - 2 * inch


def esc(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`(.+?)`", r"<font face='Courier'>\1</font>", s)


def spaced(t):
    return "&nbsp;".join(esc(t.upper()))


def table(rows, n_title):
    head, body = rows[0], rows[2:]
    n = len(head)
    widths = [CW * 0.24] + [CW * 0.76 / (n - 1)] * (n - 1) if n > 2 else [CW * 0.3, CW * 0.7]
    data = [[Paragraph(spaced(c), S["th"]) for c in head]]
    for r in body:
        data.append([Paragraph(esc(r[i] if i < len(r) else ""), S["cellb"] if i == 0 else S["cell"]) for i in range(n)])
    tb = Table(data, colWidths=widths, repeatRows=1)
    tb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), TINT), ("BOX", (0, 0), (-1, -1), 0.8, ALINE),
                            ("INNERGRID", (0, 0), (-1, -1), 0.4, ALINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7)]))
    return [tb, Spacer(1, 10)]


def story_from(md):
    story, rows, in_sources = [], [], False
    lines = md.splitlines() + [""]
    for ln in lines:
        if ln.startswith("|"):
            rows.append([c.strip() for c in ln.strip().strip("|").split("|")])
            continue
        if rows:
            story += table(rows, None)
            rows = []
        if ln.startswith("# "):
            title = ln[2:]
            eyebrow, _, head = title.partition(" · ")
            story += [Paragraph(spaced(eyebrow), S["eyebrow"]), Paragraph(esc(head or title), S["h1"])]
        elif ln.startswith("## "):
            in_sources = "Sources" in ln
            story.append(Paragraph(esc(ln[3:]), S["h2"]))
        elif ln.startswith("- "):
            story.append(Paragraph(esc(ln[2:]), S["small"] if in_sources else S["bullet"],
                                   bulletText=None if in_sources else "•"))
        elif ln.strip():
            story.append(Paragraph(esc(ln), S["body"]))
    return story


def footer(canvas, doc, start):
    canvas.saveState()
    canvas.setFont(F, 8)
    canvas.setFillColor(GREY)
    canvas.drawRightString(letter[0] - inch, 0.6 * inch, str(start + doc.page))
    canvas.restoreState()


def main(md_path, paper_pdf, out_pdf):
    reader = PdfReader(paper_pdf)
    at = next((i for i, p in enumerate(reader.pages) if "Source Register" in (p.extract_text() or "")), len(reader.pages))
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter, leftMargin=inch, rightMargin=inch, topMargin=inch, bottomMargin=0.9 * inch)
    doc.build(story_from(open(md_path, encoding="utf-8").read()),
              onFirstPage=lambda c, d: footer(c, d, at), onLaterPages=lambda c, d: footer(c, d, at))
    app = PdfReader(io.BytesIO(buf.getvalue()))
    w = PdfWriter()
    for p in reader.pages[:at]:
        w.add_page(p)
    for p in app.pages:
        w.add_page(p)
    for p in reader.pages[at:]:
        w.add_page(p)
    w.add_metadata({k: v for k, v in (reader.metadata or {}).items()})
    with open(out_pdf, "wb") as f:
        w.write(f)
    print(f"inserted {len(app.pages)} appendix page(s) before page {at + 1}; total {len(w.pages)}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
