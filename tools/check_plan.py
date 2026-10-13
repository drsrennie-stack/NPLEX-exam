"""Validate a case plan. Usage: python3 tools/check_plan.py specs/plans/GI.json"""
import json, os, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
comps = json.loads(src[src.index("window.NPLEX_COMPETENCIES = ") + len("window.NPLEX_COMPETENCIES = "):].rstrip().rstrip(";"))
OBJ = {o["id"]: c["systemCode"] for c in comps for o in c.get("objectives", [])}
CODES = {c["id"] for c in comps} | {x["code"] for c in comps for x in c.get("conditions", [])}
errs = []; warns = []
for p in sys.argv[1:]:
    d = json.load(open(p, encoding="utf-8")); s = d["system"]; cases = d["cases"]
    used = collections.Counter(); seas = collections.Counter(); dx = collections.Counter()
    for c in cases:
        dx[c["dx"].strip().lower()] += 1
        t = c.get("targets", [])
        if len(t) != 4: errs.append(f"{c['id']}: {len(t)} targets")
        if len({x['obj'] for x in t}) != len(t): errs.append(f"{c['id']}: repeated objective")
        if len({x['sea'] for x in t}) < 3: warns.append(f"{c['id']}: fewer than 3 areas")
        for x in t:
            if x["obj"] not in OBJ: errs.append(f"{c['id']}: unknown obj {x['obj']}")
            elif OBJ[x["obj"]] != s: errs.append(f"{c['id']}: {x['obj']} is not in {s}")
            if x.get("sea") not in list("APBMX"): errs.append(f"{c['id']}: bad sea")
            used[x["obj"]] += 1; seas[x.get("sea")] += 1
        for k in c.get("codes", []):
            if k not in CODES: errs.append(f"{c['id']}: unknown code {k}")
    for k, v in dx.items():
        if v > 1: errs.append(f"duplicate diagnosis: {k}")
    total = sum(1 for o, x in OBJ.items() if x == s)
    rep = sum(1 for v in used.values() if v > 1)
    print(f"{p}: {len(cases)} cases, {len(used)} distinct objectives of {total} in {s}, {rep} repeated, areas {dict(seas)}")
for e in errs: print("ERROR", e)
for w in warns: print("WARN ", w)
print(f"{len(errs)} errors, {len(warns)} warnings"); sys.exit(1 if errs else 0)
