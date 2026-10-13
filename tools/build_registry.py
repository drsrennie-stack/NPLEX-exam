"""Build the permanent NPLEX Part I identifier registry.
Format: NPLEX-P1-[SUBJECT]-[CHAPTER]-[TOPIC]-C[NN]
  SUBJECT = system subject code; CHAPTER = blueprint competency number within the system (CV-7 -> 07)
  TOPIC   = condition group letter as a number (CV-18-C -> 03); 01 for numbered units without a letter
  C[NN]   = the competency (objective) number within that unit (CV-7.3 -> C03)
Rules: never reuse an identifier for a different concept. Existing entries are frozen; changes are logged.
Usage: python3 tools/build_registry.py
"""
import json, os, csv, datetime, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJ = {"CV": "CARD", "GI": "GAST", "MS": "MUSC", "NE": "NEUR", "RE": "REPR", "UR": "RENL",
        "EN": "ENDO", "IM": "IMMU", "PU": "RESP", "HE": "HEME", "IN": "INTG"}
src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
comps = json.loads(src[src.index("window.NPLEX_COMPETENCIES = ") + 28:].rstrip().rstrip(";"))
reg_path = os.path.join(ROOT, "notes/registry/identifiers.json")
old = json.load(open(reg_path)) if os.path.exists(reg_path) else {"entries": {}, "log": []}

def unit_ids(uid):
    m = re.match(r"^([A-Z]{2})-(\d+)(?:-([A-Z]))?$", uid)
    sysc, ch, let = m.group(1), int(m.group(2)), m.group(3)
    topic = (ord(let) - 64) if let else 1
    return SUBJ[sysc], ch, topic

entries = dict(old["entries"]); log = list(old["log"]); today = datetime.date.today().isoformat()
for c in comps:
    s, ch, tp = unit_ids(c["id"])
    chap = f"NPLEX-P1-{s}-{ch:02d}"; topic = f"{chap}-{tp:02d}"
    for i, o in enumerate(c.get("objectives", []), 1):
        nid = f"{topic}-C{i:02d}"
        rec = {"id": nid, "chapter": chap, "topic": topic, "unit": c["id"], "unitName": c["name"], "obj": o["id"], "text": o["t"]}
        prev = entries.get(nid)
        if prev and prev["obj"] != o["id"]:
            raise SystemExit(f"Identifier {nid} would be reused for a different competency ({prev['obj']} vs {o['id']})")
        if prev and prev["text"] != o["t"]:
            log.append({"date": today, "id": nid, "change": "competency wording revised", "before": prev["text"], "after": o["t"]})
        entries[nid] = rec
json.dump({"format": "NPLEX-P1-[SUBJECT]-[CHAPTER]-[TOPIC]-C[NN]", "subjects": SUBJ, "entries": entries, "log": log},
          open(reg_path, "w"), indent=1, ensure_ascii=False)
with open(os.path.join(ROOT, "notes/registry/identifiers.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["Competency ID", "Chapter ID", "Topic ID", "Course unit", "Unit name", "Course code", "Competency"])
    for k in sorted(entries): e = entries[k]; w.writerow([e["id"], e["chapter"], e["topic"], e["unit"], e["unitName"], e["obj"], e["text"]])
print(len(entries), "identifiers")
