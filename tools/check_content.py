"""Validate NPLEX content files against specs/SPEC.md.
Usage: python3 tools/check_content.py <file.json> [more files]
Exit code 1 if any ERROR. WARN lines are advisory.
"""
import json, re, sys, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_codes():
    src = open(os.path.join(ROOT, "nplex-competencies.js"), encoding="utf-8").read()
    arr = src[src.index("window.NPLEX_COMPETENCIES = ") + len("window.NPLEX_COMPETENCIES = "):].rstrip().rstrip(";")
    comps = json.loads(arr)
    codes = set()
    for c in comps:
        codes.add(c["id"])
        for x in c.get("conditions", []):
            codes.add(x["code"])
    return codes, {c["id"] for c in comps}


CODES, UNITS = load_codes()
DASH = re.compile("[–—]")
NEG = re.compile(r"\b(NOT|EXCEPT|LEAST)\b")
BANNED = ["all of the above", "none of the above", "both a and b", "given not googled", "it's worth noting", "great question"]
ITAL = re.compile(r"(?<![*\w])\*[^*\s][^*]*\*(?!\*)|<i>|<em>")


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from strings(x)
    elif isinstance(o, dict):
        for v in o.values():
            yield from strings(v)


def check_text(obj, where, err):
    for s in strings(obj):
        if DASH.search(s):
            err(f"{where}: en/em dash in text: ...{s[max(0, DASH.search(s).start()-25):DASH.search(s).start()+25]}...")
        low = s.lower()
        for b in BANNED:
            if b in low:
                err(f"{where}: banned phrase '{b}'")
        if ITAL.search(s):
            err(f"{where}: italic markup")


def check_unit(u, err, warn):
    w = u.get("id", "?")
    if w not in UNITS:
        err(f"{w}: unknown unit id")
    for k in ["summary", "notes", "charts", "tricks", "highYield", "pitfalls", "dumps", "refs", "videos", "related"]:
        if k not in u:
            err(f"{w}: missing {k}")
    if len(u.get("dumps", [])) != 2:
        err(f"{w}: needs exactly 2 dumps")
    for d in u.get("dumps", []):
        if not (5 <= len(d.get("l", [])) <= 9):
            warn(f"{w}: dump '{d.get('t')}' has {len(d.get('l', []))} key points (want 5 to 9)")
    nb = sum(len(s.get("points", [])) for s in u.get("notes", []))
    if not (12 <= nb <= 40):
        warn(f"{w}: {nb} note bullets (want 12 to 35)")
    for c in u.get("charts", []):
        n = len(c.get("cols", []))
        for r in c.get("rows", []):
            if len(r) != n:
                err(f"{w}: chart '{c.get('title')}' row has {len(r)} cells, header has {n}")
    for v in u.get("videos", []):
        url = v.get("url", "")
        if not re.match(r"^https://(www\.)?(youtube\.com/watch\?v=[\w-]{11}|youtu\.be/[\w-]{11}|www\.khanacademy\.org/)", url):
            warn(f"{w}: unusual video url {url}")
    for r in u.get("refs", []):
        if re.search(r"\b(ch(apter)?\.?\s*\d+|p\.?\s*\d+|page \d+)", r.get("where", ""), re.I):
            err(f"{w}: reference uses a chapter or page number: {r.get('where')}")
    for c in u.get("related", []):
        if c not in CODES:
            err(f"{w}: unknown related code {c}")
    check_text(u, w, err)


def check_case(c, err, warn, positions):
    w = c.get("id", "?")
    for k in ["id", "system", "dx", "codes", "case", "questions"]:
        if k not in c:
            err(f"{w}: missing {k}")
    for code in c.get("codes", []):
        if code not in CODES:
            err(f"{w}: unknown code {code}")
    nw = len(c.get("case", "").split())
    if not (50 <= nw <= 170):
        warn(f"{w}: case summary {nw} words (want 60 to 140)")
    qs = c.get("questions", [])
    if len(qs) != 4:
        err(f"{w}: has {len(qs)} questions, needs 4")
    seas = set()
    pos_in_case = collections.Counter()
    for q in qs:
        qi = q.get("id", "?")
        for k in ["stem", "options", "answer", "sea", "comp", "dok", "approach", "why", "whyNot", "study"]:
            if k not in q:
                err(f"{qi}: missing {k}")
        opts = q.get("options", [])
        if len(opts) != 4:
            err(f"{qi}: needs 4 options")
            continue
        a = q.get("answer")
        if not isinstance(a, int) or not 0 <= a <= 3:
            err(f"{qi}: bad answer index")
            continue
        positions.append(a)
        pos_in_case[a] += 1
        L = [len(o) for o in opts]
        if L[a] == max(L) and L.count(max(L)) == 1 and max(L) > 1.25 * sorted(L)[-2]:
            err(f"{qi}: correct option is clearly the longest")
        elif L[a] == max(L) and L.count(max(L)) == 1:
            warn(f"{qi}: correct option is the longest")
        wn = q.get("whyNot", [])
        if len(wn) != 4:
            err(f"{qi}: whyNot needs 4 entries")
        elif wn[a].strip() != "Correct.":
            err(f"{qi}: whyNot[{a}] must be exactly 'Correct.'")
        elif any(x.strip() == "Correct." for i, x in enumerate(wn) if i != a):
            err(f"{qi}: 'Correct.' on a wrong option")
        if NEG.search(q.get("stem", "")):
            err(f"{qi}: negative stem")
        if q.get("sea") not in list("APBMX"):
            err(f"{qi}: bad sea {q.get('sea')}")
        seas.add(q.get("sea"))
        if q.get("comp") not in CODES:
            err(f"{qi}: unknown comp {q.get('comp')}")
        if q.get("dok") not in (2, 3):
            err(f"{qi}: dok must be 2 or 3")
        if not (2 <= len(q.get("approach", [])) <= 4):
            warn(f"{qi}: approach should be 2 to 4 steps")
        for s in q.get("study", {}).get("comps", []):
            if s not in CODES:
                err(f"{qi}: unknown study comp {s}")
        if len(set(o.strip().lower() for o in opts)) < 4:
            err(f"{qi}: duplicate options")
    if len(seas) < 3:
        warn(f"{w}: only {len(seas)} SEAs across its questions")
    if pos_in_case and max(pos_in_case.values()) > 2:
        warn(f"{w}: one answer position used {max(pos_in_case.values())} times in this case")
    check_text(c, w, err)


def main(paths):
    errors, warns = [], []
    for p in paths:
        data = json.load(open(p, encoding="utf-8"))
        positions = []
        for o in data:
            if "questions" in o:
                check_case(o, errors.append, warns.append, positions)
            else:
                check_unit(o, errors.append, warns.append)
        if positions:
            cnt = collections.Counter(positions)
            n = len(positions)
            dist = {"ABCD"[k]: cnt.get(k, 0) for k in range(4)}
            print(f"{p}: {len(data)} cases, {n} questions, answer letters {dist}")
            if n >= 12 and (max(cnt.values()) - min(cnt.get(k, 0) for k in range(4))) > max(3, n // 8):
                warns.append(f"{p}: answer letters uneven {dist} (the balancer will fix stored keys)")
            run = 1
            for i in range(1, n):
                run = run + 1 if positions[i] == positions[i - 1] else 1
                if run >= 3:
                    warns.append(f"{p}: run of {run} identical answer positions ending at question {i+1}")
        else:
            print(f"{p}: {len(data)} study units")
    for e in errors:
        print("ERROR", e)
    for w in warns:
        print("WARN ", w)
    print(f"{len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
