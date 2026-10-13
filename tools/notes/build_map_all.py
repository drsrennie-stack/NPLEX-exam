"""Full competency map for every published notes chapter (no PDFs needed).
Usage: python3 tools/notes/build_map_all.py
Writes notes/build/NPLEX-P1-Competency-Map.xlsx with three sheets:
  Competency Map     one row per competency: identifier, unit, chapter, section, objective
  Source Record      one row per chapter: version, sources, reviewer log, open verify items
  Identifier Key     how the permanent identifier is built
"""
import json, os, glob
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = json.load(open(os.path.join(ROOT, "notes/registry/identifiers.json")))["entries"]
NAVY = "0B1530"
HEAD = PatternFill("solid", fgColor=NAVY)
thin = Side(style="thin", color="B8BDC7")
B = Border(top=thin, bottom=thin, left=thin, right=thin)
SYS = {"CV": "Cardiovascular", "GI": "Gastrointestinal", "MS": "Musculoskeletal", "NE": "Neurological",
       "RE": "Reproductive", "UR": "Renal and urinary", "EN": "Endocrine", "IM": "Immune and lymphatic",
       "PU": "Respiratory", "HE": "Hematologic", "IN": "Integumentary"}


def sheet(ws, head, rows, widths):
    ws.append(head)
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF", name="Plus Jakarta Sans")
        c.fill = HEAD
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = B
    for r in rows:
        ws.append(r)
        for c in ws[ws.max_row]:
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = B
            c.font = Font(name="Plus Jakarta Sans", size=10)
    for i, w in enumerate(widths):
        ws.column_dimensions[chr(65 + i)].width = w
    ws.freeze_panes = "A2"


def flat(x):
    """Sources and verify items are either plain strings or {book, where} records."""
    if isinstance(x, dict):
        book = x.get("book") or x.get("title") or ""
        where = x.get("where") or x.get("chapter") or ""
        return f"{book}, {where}".strip(", ") if (book or where) else json.dumps(x)
    return str(x)


def unit_sort(u):
    sys_code = u.split("-")[0]
    parts = u.split("-")
    num = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    letter = parts[2] if len(parts) > 2 else ""
    return (list(SYS).index(sys_code) if sys_code in SYS else 99, num, letter)


units = sorted((os.path.basename(p)[:-5] for p in glob.glob(os.path.join(ROOT, "notes/chapters/*.json"))), key=unit_sort)
rows, rec = [], []
for u in units:
    d = json.load(open(os.path.join(ROOT, f"notes/chapters/{u}.json")))
    reviewed = os.path.exists(os.path.join(ROOT, f"specs/reviews/notes1-{u}.md"))
    for i, s in enumerate(d["sections"], 1):
        e = REG.get(s["comp"], {})
        rows.append([s["comp"], SYS.get(u.split("-")[0], ""), u, d.get("title", ""),
                     f"Section {i}. {s.get('title','')}", e.get("obj", ""), e.get("text", "") or s.get("obj", "")])
    rec.append([u, d.get("title", ""), d.get("version", ""), len(d["sections"]),
                "Reviewed" if reviewed else "Not reviewed",
                "; ".join(flat(x) for x in d.get("sources", []))[:1500],
                "; ".join(flat(x) for x in d.get("verify", []))[:1500]])

wb = Workbook()
ws = wb.active
ws.title = "Competency Map"
sheet(ws, ["Competency identifier", "System", "Course unit", "Chapter", "Where it is taught", "Blueprint code", "Learning objective"],
      rows, [30, 20, 14, 34, 40, 14, 90])
sheet(wb.create_sheet("Source Record"), ["Course unit", "Chapter", "Version", "Sections", "Review status", "Sources", "Open verify items"],
      rec, [14, 34, 10, 10, 14, 70, 70])
sheet(wb.create_sheet("Identifier Key"), ["Part", "Meaning", "Example"], [
    ["NPLEX", "Examination family", "NPLEX"],
    ["P1", "Part I, biomedical science", "P1"],
    ["SUBJ", "Four letter subject code", "CARD for cardiovascular"],
    ["CH", "Blueprint chapter number, two digits", "07"],
    ["TOPIC", "Condition or topic within the chapter, two digits", "01"],
    ["CNN", "Competency number within the topic", "C03"],
    ["Full identifier", "Never reused, even if a chapter is rewritten", "NPLEX-P1-CARD-07-01-C03"],
], [22, 60, 34])
out = os.path.join(ROOT, "notes/build/NPLEX-P1-Competency-Map.xlsx")
wb.save(out)
print(f"wrote {out} {len(rows)} competencies across {len(units)} chapters")
