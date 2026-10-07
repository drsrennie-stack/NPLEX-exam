# NPLEX Part I Board Review

MedMasters Collaborative. By Dr. Sharilyn Rennie.

A 12-week NPLEX Part I Biomedical Science course built on the NABNE blueprint (study guide revised March 2026). One body system per week, then a final week of full-length exams.

## What students do

For every one of the 236 study units:

1. Brain dump before studying (blank paper)
2. Study notes, charts, mnemonics, videos, textbook pointers
3. Case questions (NPLEX format: case summary with diagnosis, then 4 questions)
4. Brain dump after studying
5. Spaced recall brings the unit back on a schedule

The app tracks every unit as Not started, In progress, Due, Blind spot, or Mastered, so nothing on the blueprint gets skipped.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app: path, study units, brain dumps, practice, full exams, dashboard, diagnostic |
| `nplex-competencies.js` | The blueprint: 152 numbered competencies, 95 condition groups, 423 conditions, weights |
| `nplex-content.js` | GENERATED. Study units, cases, diagnostic. Rebuild, never hand-edit |
| `content/` | Source content as JSON, one file per writer batch |
| `specs/SPEC.md` | The content spec every writer follows |
| `specs/REVIEW.md` | The independent review checklist |
| `specs/reviews/` | Review logs, one per content file |
| `tools/check_content.py` | Validator: run on every content file |
| `tools/balance_keys.py` | Re-randomizes answer letters: even counts, no runs, no A-B-C-D patterns |
| `tools/build_bundle.py` | Builds `nplex-content.js` from `content/` |
| `compliance-notes.md` | Accessibility compliance notes |

## Rebuild after content changes

```
python3 tools/check_content.py content/*/*.json
python3 tools/build_bundle.py
```

## Student progress

Saved in the browser (localStorage keys `nplex-state`, `nplex-progress`, `nplex-theme`). `nplex-progress` uses the Mastery OS recall format, keyed by unit id.

## Status (Oct 7, 2026)

- Cardiovascular: complete. 28 study units, 60 cases, 240 questions, each independently reviewed.
- Diagnostic: Batch 1 rebuilt as 16 cases (64 questions, CV and GI).
- Other 10 systems: to be built on the same pipeline.
