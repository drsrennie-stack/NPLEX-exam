# Notes upgrade: explanations and flow diagrams

This is graduate-level, medical-professional course material (naturopathic medical students preparing for NPLEX Part I at USMLE Step 1 depth). Write for future physicians: precise terminology, mechanism-level reasoning, no oversimplification. Read specs/SPEC.md first; every accuracy and writing rule there applies (no em or en dashes, no italics, plain clear sentences, accurate or not at all, Celsius first with Fahrenheit in parentheses).

You upgrade the study units in ONE assigned file, content/<sys>/units-<n>.json. Do not change any existing field except as described here. Do not touch "videos".

## 1. "why" on every notes section
For each object in "notes", add a field "why": 2 to 4 sentences that explain the mechanism behind that section's bullets, at graduate depth. Teach the reasoning a strong student needs to answer a two-step board question: cause to mechanism to finding, structure to function, or the molecular step that explains the clinical picture. Do not repeat the bullets; connect them. Use correct terminology and explain it briefly in plain words.

Example: notes section "Preload and afterload" might get: "Preload stretches sarcomeres toward their optimal overlap, so a larger end-diastolic volume produces a stronger contraction (the Frank-Starling mechanism). Afterload is the wall stress the ventricle must overcome to eject, which by the law of Laplace rises with pressure and chamber radius and falls with wall thickness. This is why chronic pressure overload thickens the wall (concentric hypertrophy) while volume overload dilates the chamber (eccentric hypertrophy)."

## 2. "flows": 1 to 3 step diagrams per unit
Add "flows": [{"title": "...", "steps": ["...", "..."]}].
- Each flow is a real sequence: a physiologic pathway, a signaling or biochemical cascade, a developmental sequence, the pathogenesis chain of a disease, or a path of flow (blood, urine, nerve signal, lymph).
- 3 to 7 steps, each at most about 14 words, in true order. Each step follows from the one before.
- Choose the sequences the exam tests most for this unit's competencies (see the unit's "objectives" in nplex-competencies.js). For a conditions unit, prefer pathogenesis chains for the key conditions.
- Every step must be accurate. If a step is debated or varies, leave that flow out.

## 3. Check and finish
- Run `python3 tools/check_content.py <your file>` and fix every ERROR.
- Re-read every "why" and every flow step as a hostile board reviewer. Fix anything doubtful.
- Scripts only in /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/notes-<sys>-<n>/ with unique names. Edit no other file.
- Reply with ONE line only: file, units upgraded, flows added, checker errors.
