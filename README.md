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
6. Flashcards for quick recall, built from each unit's charts and memory aids

Every question rates confidence (Sure, Fairly sure, Not sure) and shows a confidence score. Teaching mode explains every option and links to the exact notes, chart, or mnemonic that teaches it.

The app tracks every unit as Not started, In progress, Due, Blind spot, or Mastered, so nothing on the blueprint gets skipped.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app: path, study units, brain dumps, practice, full exams, dashboard, diagnostic |
| `nplex-competencies.js` | GENERATED. The blueprint (152 numbered competencies, 95 condition groups, 423 conditions, weights) plus 1,687 specific competencies at USMLE Step 1 depth and the USMLE crosswalk |
| `nplex-competencies.html` | Searchable competency viewer with the USMLE crosswalk |
| `NPLEX-Part-I-Competencies.pdf` | Print version of the viewer |
| `content/objectives/` | Source competencies by system (JSON), reviewed |
| `specs/OBJECTIVES.md` | How competencies are written and tagged |
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
python3 tools/check_objectives.py content/objectives/*.json
cd tools && python3 build_competencies.py ../NPLEX_Master_Blueprint_Scaffold.xlsx .. && cd ..
python3 tools/build_competency_pages.py .
python3 tools/check_content.py content/*/*.json
python3 tools/build_bundle.py
```

## Student progress

Saved in the browser (localStorage keys `nplex-state`, `nplex-progress`, `nplex-theme`). `nplex-progress` uses the Mastery OS recall format, keyed by unit id.

## Status (Oct 12, 2026)

- All 11 systems complete: 236 study units, 750 cases, 3,000 questions, each file independently reviewed.
- Every one of the 1,687 competencies is tested by at least one question.
- Diagnostic: 16 cases (64 questions, CV and GI).
- Next: video pass for units that do not have videos yet.
