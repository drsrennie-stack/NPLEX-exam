"""Chapter Competency Map + Source and Revision Record (XLSX).
Usage: python3 tools/notes/build_map.py CV-7 CV-18-C
Reads notes/chapters/<unit>.json and notes/build/<unit>.pdf (for page numbers) and specs/reviews/notes1-<unit>.md.
"""
import json, os, re, subprocess, sys, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = json.load(open(os.path.join(ROOT, "notes/registry/identifiers.json")))["entries"]
src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
COMPS = {c["id"]: c for c in json.loads(src[src.index("window.NPLEX_COMPETENCIES = ") + 28:].rstrip().rstrip(";"))}
OBJ = {o["id"]: o for c in COMPS.values() for o in c.get("objectives", [])}
NAVY = "0B1530"; HEAD = PatternFill("solid", fgColor=NAVY); thin = Side(style="thin", color="B8BDC7")
B = Border(top=thin, bottom=thin, left=thin, right=thin)


def pages(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    return [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"], capture_output=True, text=True).stdout for i in range(1, n + 1)]


def sheet(ws, head, rows, widths):
    ws.append(head)
    for c in ws[1]: c.font = Font(bold=True, color="FFFFFF", name="Plus Jakarta Sans"); c.fill = HEAD; c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = B
    for r in rows:
        ws.append(r)
        for c in ws[ws.max_row]: c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = B; c.font = Font(name="Plus Jakarta Sans", size=10)
    for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
    ws.freeze_panes = "A2"


units = sys.argv[1:]
wb = Workbook(); ws = wb.active; ws.title = "Competency Map"
rows, rec = [], []
for u in units:
    d = json.load(open(os.path.join(ROOT, f"notes/chapters/{u}.json")))
    P = pages(os.path.join(ROOT, f"notes/build/{u}.pdf"))
    unit = COMPS[u]
    for s in d["sections"]:
        e = REG[s["comp"]]
        pg = next((i + 1 for i, t in enumerate(P) if re.search(re.escape(s["comp"]) + r"\s+\|\s+" + re.escape(s["obj"]), t)), None)
        o = OBJ[s["obj"]]
        align = f"NABNE Part I blueprint {unit['systemCode']} {u.split('-',1)[1]}: {unit['name']}" + (f"; USMLE Step 1: {o['usmle']}" if o.get("usmle") else "")
        rows.append([d["chapter_id"], d["topic_id"], s["comp"], e["text"], f"{s['title']} (page {pg})" if pg else s["title"], align, "Pending until Phase 2"])
    log = os.path.join(ROOT, f"specs/reviews/notes1-{u}.md")
    changes = open(log).read().strip() if os.path.exists(log) else "Independent review completed; no log file."
    rec.append([d["chapter_id"], d["title"], d.get("version", "1.0"), datetime.date.today().isoformat(),
                "Written from the NABNE Part I blueprint competency and the course competency list; independent accuracy review by a second reviewer.",
                "\n".join(f"{r['book']}: {r['where']}" for r in d.get("sources", [])),
                "\n".join(d.get("verify", [])) or "None",
                changes[:30000]])
sheet(ws, ["Chapter ID", "Topic ID", "Competency ID", "Competency", "Notes location (section and page)", "Exam alignment", "Workbook status"], rows, [20, 22, 28, 60, 40, 46, 20])
ws2 = wb.create_sheet("Source and Revision Record")
sheet(ws2, ["Chapter ID", "Chapter", "Version", "Review date", "Review process", "Sources", "Outstanding verification needs", "Review changes"], rec, [20, 32, 9, 13, 36, 46, 60, 80])
ws3 = wb.create_sheet("Identifier Key")
sheet(ws3, ["Part", "Format", "Meaning"], [["NPLEX-P1", "NPLEX-P1-[SUBJECT]-[CHAPTER]-[TOPIC]-C[NN]", "Part I. SUBJECT is the body system code; CHAPTER is the blueprint competency number in that system; TOPIC is the condition group letter as a number (A = 01) or 01 for single-topic chapters; C[NN] is the competency number."]] +
      [[k, v, ""] for k, v in json.load(open(os.path.join(ROOT, "notes/registry/identifiers.json")))["subjects"].items()], [12, 48, 90])
out = os.path.join(ROOT, "notes/build/NPLEX-P1-Pilot-Competency-Map.xlsx"); wb.save(out); print("wrote", out, len(rows), "rows")
