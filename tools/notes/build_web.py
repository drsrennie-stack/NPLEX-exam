"""Build the web notes: notes-web/<SYS>.js (one per system, loaded on demand), notes-web/index.js, and diagram PNGs.
Usage: python3 tools/notes/build_web.py   (run tools/notes/figures.mjs on the chapters first so diagram PNGs exist)
Only chapters with a review log (specs/reviews/notes1-<unit>.md, any case) are published."""
import json, os, glob, shutil, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "notes-web"); os.makedirs(os.path.join(OUT, "fig"), exist_ok=True)
reviewed = {os.path.basename(p)[7:-3].upper() for p in glob.glob(os.path.join(ROOT, "specs/reviews/notes1-*.md"))}
by = {}; idx = {}
for p in sorted(glob.glob(os.path.join(ROOT, "notes/chapters/*.json"))):
    d = json.load(open(p)); u = d["unit"]
    if u.upper() not in reviewed: continue
    d.pop("verify", None)
    n = 0
    for b in [b for s in d["sections"] for b in s["blocks"]] + d.get("integration", []):
        if b.get("type") in ("flow", "cycle", "diagram"):
            n += 1
            if b["type"] == "diagram":
                src = os.path.join(ROOT, f"notes/build/fig/{u}-{n}.png")
                if os.path.exists(src):
                    shutil.copy(src, os.path.join(OUT, "fig", f"{u}-{n}.png")); b["img"] = f"notes-web/fig/{u}-{n}.png"
    sysc = u[:2]; by.setdefault(sysc, {})[u] = d; idx[u] = sysc
for sysc, chs in by.items():
    open(os.path.join(OUT, f"{sysc}.js"), "w").write("window.NPLEX_NOTES=window.NPLEX_NOTES||{};Object.assign(window.NPLEX_NOTES," + json.dumps(chs, ensure_ascii=False, separators=(",", ":")) + ");\n")
open(os.path.join(OUT, "index.js"), "w").write("window.NPLEX_NOTES_INDEX=" + json.dumps(idx, separators=(",", ":")) + ";\n")
print({k: len(v) for k, v in by.items()}, "chapters published")
