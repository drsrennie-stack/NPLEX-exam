"""Validate an objectives file against specs/OBJECTIVES.md.
Usage: python3 tools/check_objectives.py content/objectives/CV.json [more]
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
COMPS = json.loads(src[src.index("window.NPLEX_COMPETENCIES = ") + len("window.NPLEX_COMPETENCIES = "):].rstrip().rstrip(";"))
DASH = re.compile("[–—]")
WEAK = re.compile(r"^(understand|know|learn|be familiar|appreciate|recognize the importance)", re.I)
BANNED = ["given not googled", "it's worth noting", "delve"]
VERB = re.compile(r"^[A-Z][a-z]+")


def main(paths):
    errs, warns = [], []
    total = 0
    for p in paths:
        d = json.load(open(p, encoding="utf-8"))
        sysc = d.get("system")
        units = [c for c in COMPS if c["systemCode"] == sysc]
        if not units:
            errs.append(f"{p}: unknown system {sysc}")
            continue
        obj = d.get("objectives", {})
        order = [k for k in obj]
        want = [u["id"] for u in units]
        for uid in want:
            if uid not in obj:
                errs.append(f"{uid}: missing")
        for k in obj:
            if k not in want:
                errs.append(f"{k}: not a unit in {sysc}")
        if [k for k in order if k in want] != [w for w in want if w in obj]:
            warns.append(f"{p}: units not in blueprint order")
        ids = set()
        for u in units:
            L = obj.get(u["id"], [])
            total += len(L)
            if u["kind"] == "competency" and not (3 <= len(L) <= 8):
                warns.append(f"{u['id']}: {len(L)} objectives (want 3 to 7)")
            covered = set()
            for i, o in enumerate(L, 1):
                oid = o.get("id", "")
                if oid != f"{u['id']}.{i}":
                    errs.append(f"{u['id']}: objective {i} id is {oid}, expected {u['id']}.{i}")
                if oid in ids:
                    errs.append(f"duplicate id {oid}")
                ids.add(oid)
                t = o.get("t", "")
                if not t:
                    errs.append(f"{oid}: empty text")
                if DASH.search(t):
                    errs.append(f"{oid}: en/em dash")
                if WEAK.search(t):
                    errs.append(f"{oid}: weak verb: {t[:40]}")
                if not VERB.match(t):
                    warns.append(f"{oid}: should start with a capitalized verb")
                if len(t.split()) > 48:
                    warns.append(f"{oid}: {len(t.split())} words")
                if any(b in t.lower() for b in BANNED):
                    errs.append(f"{oid}: banned phrase")
                if "*" in t or "_" in t:
                    errs.append(f"{oid}: markdown characters")
                if o.get("dok") not in (1, 2, 3):
                    errs.append(f"{oid}: bad dok")
                if o.get("sea") not in list("APBMX"):
                    errs.append(f"{oid}: bad sea")
                if o.get("src") not in ("NPLEX", "Both", "USMLE"):
                    errs.append(f"{oid}: bad src")
                if o.get("src") in ("Both", "USMLE") and not o.get("usmle"):
                    errs.append(f"{oid}: src {o.get('src')} needs a usmle heading")
                if u["kind"] == "conditions":
                    cs = o.get("cond")
                    if cs is None:
                        errs.append(f"{oid}: condition unit objective needs cond")
                    else:
                        valid = {x["code"] for x in u.get("conditions", [])}
                        for c in cs:
                            if c not in valid:
                                errs.append(f"{oid}: cond {c} not in {u['id']}")
                            covered.add(c)
                        if o.get("src") == "USMLE" and cs:
                            warns.append(f"{oid}: USMLE extension lists NPLEX conditions")
            if u["kind"] == "conditions":
                for x in u.get("conditions", []):
                    if x["code"] not in covered:
                        errs.append(f"{u['id']}: condition {x['code']} {x['name']} not covered")
        for cw in d.get("crosswalk", []):
            w = cw.get("where", "")
            if w != "excluded" and w not in ids:
                errs.append(f"crosswalk '{cw.get('usmle','')[:50]}' points to unknown objective {w}")
        if not d.get("crosswalk"):
            errs.append(f"{p}: crosswalk is empty")
        n_src = {}
        for L in obj.values():
            for o in L:
                n_src[o.get("src")] = n_src.get(o.get("src"), 0) + 1
        print(f"{p}: {sum(len(v) for v in obj.values())} objectives in {len(obj)} units; src {n_src}; crosswalk {len(d.get('crosswalk', []))}; excluded {len(d.get('excluded', []))}")
    for e in errs:
        print("ERROR", e)
    for w in warns:
        print("WARN ", w)
    print(f"{len(errs)} errors, {len(warns)} warnings")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
