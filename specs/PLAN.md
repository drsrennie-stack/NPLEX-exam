# Case Plan Spec (planner)

You are planning NPLEX Part I case sets for one body system. Writers will write the cases from your plan, so the plan decides coverage.

Read first:
- specs/SPEC.md (section B: case format; NPLEX case = a case summary that states the diagnosis, then 4 questions on its biomedical science)
- nplex-competencies.js (window.NPLEX_COMPETENCIES): your system's units, conditions, and "objectives" (the specific competencies, ids like GI-6.3)
- content/batch1/*.json (diagnostic cases): do not reuse their primary diagnoses
- Any existing cases for your system in content/<sys>/cases-*.json and `python3 tools/coverage.py <SYS>` (what is still untested)

## Output

Write `specs/plans/<SYS>.json` (or the file name you are told):

```json
{
  "system": "GI",
  "cases": [
    {"id": "GI-C01", "dx": "Acute pancreatitis from gallstones", "codes": ["GI-13-B1"],
     "targets": [
       {"obj": "GI-13-B.1", "sea": "X"},
       {"obj": "GI-5.2", "sea": "A"},
       {"obj": "GI-8.4", "sea": "B"},
       {"obj": "GI-11.3", "sea": "M"}
     ]}
  ]
}
```

## Rules

- Exactly the number of cases you are told, ids numbered from the start id you are given, 4 targets each.
- Each case is one patient with one stated diagnosis (realistic, board-typical). Every target must be answerable as a natural question about that patient: normal anatomy, physiology, biochemistry, genetics, microbiology, or immunology that the disease involves, plus pathology of the disease itself.
- Coverage first: use as many different objectives as possible. Do not repeat an objective until every objective in the system has been used (or is impossible to tie to a case). Prefer objectives that are still untested.
- Every NPLEX condition in the system should be the diagnosis (or a clearly tested part) of at least one case when the case count allows; spread across every condition category.
- "sea" per target: the exam area the question will test (A, P, B, M, X), normally the objective's own sea. Across the whole plan aim for about 20% each; every case mixes at least 3 areas.
- "codes": NPLEX condition or unit codes for the case's diagnosis.
- Diagnoses must be distinct within the plan; vary age, sex, and setting across cases (the writers handle details).
- Keep to Part I scope: no pharmacology questions, no management questions.

Validate with `python3 tools/check_plan.py specs/plans/<file>.json` and fix every ERROR.
