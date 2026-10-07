"""Re-randomize answer positions across a list of cases.

Goals (from the author's exam rules):
  - equal counts of A, B, C, D across the bank
  - no run of 3 or more identical letters in question order
  - no A-B-C-D or D-C-B-A sequence of four in a row
  - no "every letter exactly once in each case" pattern
Numeric option sets (every option starts with a number) keep ascending order and
their natural key; the other questions are balanced around them.

Deterministic: the same seed and input always give the same output.
"""
import random, re

NUMERIC = re.compile(r"^\s*[<>~≈]?\s*-?\d")


def is_numeric(q):
    return all(NUMERIC.match(o) for o in q["options"])


def bad_window(seq, i):
    """True if placing seq[i] creates a forbidden pattern ending at i."""
    if i >= 2 and seq[i] == seq[i - 1] == seq[i - 2]:
        return True
    if i >= 3:
        w = seq[i - 3:i + 1]
        if w in ([0, 1, 2, 3], [3, 2, 1, 0]):
            return True
    return False


def all_distinct_cases(seq, sizes):
    pos, n = 0, 0
    for s in sizes:
        block = seq[pos:pos + s]
        if s == 4 and len(set(block)) == 4:
            n += 1
        pos += s
    return n


def plan(fixed, sizes, rng):
    """fixed: list of None or a forced position. Returns target positions."""
    n = len(fixed)
    free = [i for i in range(n) if fixed[i] is None]
    counts = [sum(1 for f in fixed if f == k) for k in range(4)]
    target = n / 4
    need = [max(0, round(target - counts[k])) for k in range(4)]
    while sum(need) < len(free):
        need[min(range(4), key=lambda k: counts[k] + need[k])] += 1
    while sum(need) > len(free):
        need[max(range(4), key=lambda k: need[k])] -= 1
    for attempt in range(4000):
        left = need[:]
        seq = list(fixed)
        ok = True
        for i in range(n):
            if seq[i] is not None:
                if bad_window(seq, i):
                    ok = False
                    break
                continue
            choices = [k for k in range(4) if left[k] > 0]
            rng.shuffle(choices)
            # prefer letters with the most quota left so the tail stays solvable
            choices.sort(key=lambda k: -left[k] + rng.random() * 1.5)
            for k in choices:
                seq[i] = k
                if not bad_window(seq, i):
                    left[k] -= 1
                    break
            else:
                ok = False
                break
        if not ok:
            continue
        # allow at most a quarter of 4-question cases to use all four letters
        if all_distinct_cases(seq, sizes) > max(1, len(sizes) // 4):
            continue
        return seq
    raise RuntimeError("could not find a balanced key plan")


def apply(q, new_pos, rng):
    a = q["answer"]
    if new_pos == a:
        order = list(range(4))
    else:
        others = [i for i in range(4) if i != a]
        rng.shuffle(others)
        order = others[:]
        order.insert(new_pos, a)
    q["options"] = [q["options"][i] for i in order]
    q["whyNot"] = [q["whyNot"][i] for i in order]
    q["answer"] = new_pos


def balance(cases, seed=2026):
    rng = random.Random(seed)
    qs = [q for c in cases for q in c["questions"]]
    sizes = [len(c["questions"]) for c in cases]
    fixed = [q["answer"] if is_numeric(q) else None for q in qs]
    seq = plan(fixed, sizes, rng)
    for q, p in zip(qs, seq):
        if not is_numeric(q):
            apply(q, p, rng)
    return [q["answer"] for q in qs]


if __name__ == "__main__":
    import json, sys, collections
    data = json.load(open(sys.argv[1]))
    keys = balance(data)
    print(collections.Counter("ABCD"[k] for k in keys), "".join("ABCD"[k] for k in keys))
