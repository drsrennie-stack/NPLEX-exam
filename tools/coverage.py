"""Competency coverage by questions.
Usage: python3 tools/coverage.py [SYS]   -> summary for all systems, or uncovered list for one system (JSON to stdout with --json)
"""
import json, os, sys, glob, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
comps = json.loads(src[src.index("window.NPLEX_COMPETENCIES = ") + len("window.NPLEX_COMPETENCIES = "):].rstrip().rstrip(";"))
objs = {o["id"]: (c["systemCode"], o) for c in comps for o in c.get("objectives", [])}
hits = collections.Counter()
nq = collections.Counter()
for f in glob.glob(os.path.join(ROOT, "content", "*", "cases-*.json")):
    try:
        for c in json.load(open(f, encoding="utf-8")):
            for q in c.get("questions", []):
                nq[c.get("system")] += 1
                if q.get("obj"): hits[q["obj"]] += 1
    except Exception as e:
        print("skip", f, e, file=sys.stderr)
args = [a for a in sys.argv[1:] if not a.startswith("--")]
if args:
    sysc = args[0]
    un = [o for i, (s, o) in objs.items() if s == sysc and hits[i] == 0]
    if "--json" in sys.argv:
        print(json.dumps([{"id": o["id"], "t": o["t"], "sea": o["sea"], "dok": o["dok"], "src": o["src"]} for o in un], indent=1))
    else:
        for o in un: print(o["id"], o["t"][:90])
        print(len(un), "uncovered")
else:
    tot = cov = 0
    for s in ["CV","GI","MS","NE","RE","UR","EN","IM","PU","HE","IN"]:
        ids = [i for i, (x, _) in objs.items() if x == s]; c = sum(1 for i in ids if hits[i]); tot += len(ids); cov += c
        print(f"{s}: {nq[s]:4d} questions, {c:3d} of {len(ids):3d} competencies tested")
    print(f"ALL: {sum(nq.values())} questions, {cov} of {tot} competencies tested")
