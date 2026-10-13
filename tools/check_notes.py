"""Validate a comprehensive notes chapter (specs/NOTES-P1.md).
Usage: python3 tools/check_notes.py notes/chapters/CV-7.json [more]
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = json.load(open(os.path.join(ROOT, "notes/registry/identifiers.json")))["entries"]
DASH = re.compile("[–—]")
BANNED = ["given not googled", "it's worth noting", "delve"]
DIAGRAMS = {"ecg-waveform", "conduction-pathway", "pacemaker-ap", "ventricular-ap"}
TYPES = {"p", "h", "bullets", "table", "flow", "cycle", "diagram", "example", "stop"}


def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, list):
        for x in o: yield from strings(x)
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)


def words(o): return sum(len(s.split()) for s in strings(o))


def main(paths):
    errs, warns = [], []
    for p in paths:
        d = json.load(open(p, encoding="utf-8"))
        u = d.get("unit")
        want = sorted([e for e in REG.values() if e["unit"] == u], key=lambda e: e["id"])
        if not want: errs.append(f"{p}: unknown unit {u}"); continue
        if d.get("chapter_id") != want[0]["chapter"]: errs.append(f"{p}: chapter_id should be {want[0]['chapter']}")
        if d.get("topic_id") != want[0]["topic"]: errs.append(f"{p}: topic_id should be {want[0]['topic']}")
        secs = d.get("sections", [])
        got = [s.get("comp") for s in secs]
        if got != [e["id"] for e in want]: errs.append(f"{p}: sections must be exactly {[e['id'] for e in want]} in order, got {got}")
        for s in secs:
            e = REG.get(s.get("comp"))
            if e and s.get("obj") != e["obj"]: errs.append(f"{s.get('comp')}: obj should be {e['obj']}")
            nstop = 0
            for b in s.get("blocks", []):
                t = b.get("type")
                if t not in TYPES: errs.append(f"{s.get('comp')}: bad block type {t}")
                if t == "table":
                    n = len(b.get("cols", []))
                    for r in b.get("rows", []):
                        if len(r) != n: errs.append(f"{s.get('comp')}: table '{b.get('title')}' row width {len(r)} != {n}")
                if t in ("flow", "cycle") and not (3 <= len(b.get("steps", [])) <= 9): errs.append(f"{s.get('comp')}: {t} '{b.get('title')}' needs 3 to 9 steps")
                if t == "diagram" and b.get("name") not in DIAGRAMS: errs.append(f"{s.get('comp')}: unknown diagram {b.get('name')}")
                if t == "stop": nstop += 1
            if nstop > 1: warns.append(f"{s.get('comp')}: {nstop} STOP prompts (max 1)")
            w = words(s.get("blocks", []))
            if w < 150: warns.append(f"{s.get('comp')}: only {w} words")
            if w > 650: warns.append(f"{s.get('comp')}: {w} words (target 250 to 450)")
        ov = d.get("overview", {})
        for k, lo in [("prerequisites", 3), ("connections", 3), ("terms", 6)]:
            if len(ov.get(k, [])) < lo: warns.append(f"{p}: overview {k} has {len(ov.get(k, []))} (want {lo}+)")
        allb = [b for s in secs for b in s.get("blocks", [])]
        if sum(1 for b in allb if b.get("type") in ("flow", "cycle", "diagram")) < 3: warns.append(f"{p}: fewer than 3 figures")
        if sum(1 for b in allb if b.get("type") == "example") < 1: warns.append(f"{p}: no worked example")
        if sum(1 for b in allb if b.get("type") == "stop") > 3: warns.append(f"{p}: more than 3 STOP prompts")
        if not (6 <= len(d.get("summary", [])) <= 10): warns.append(f"{p}: summary has {len(d.get('summary', []))} lines")
        for st in strings(d):
            if DASH.search(st): errs.append(f"{p}: en/em dash: ...{st[max(0, DASH.search(st).start()-30):DASH.search(st).start()+30]}...")
            if any(b in st.lower() for b in BANNED): errs.append(f"{p}: banned phrase in: {st[:60]}")
            if re.search(r"(?<![*\w])\*[^*\s][^*]*\*(?!\*)|<i>|<em>|_[A-Za-z]+_", st): errs.append(f"{p}: italic markup in: {st[:60]}")
        print(f"{p}: {len(secs)} sections, {words(d)} words, {sum(1 for b in allb if b.get('type') in ('flow','cycle','diagram','table'))} figures and tables")
    for e in errs: print("ERROR", e)
    for w in warns: print("WARN ", w)
    print(f"{len(errs)} errors, {len(warns)} warnings")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
