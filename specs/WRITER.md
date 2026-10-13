# Writer instructions (read fully)

Read specs/SPEC.md completely first. Follow every accuracy, writing, and format rule there, including the section "Two voices": case summaries, stems, and options in the NBME/NPLEX physician item-writer voice; explanations in a plain teaching voice. Accurate or not generated at all.

## If you are writing CASES
- Your plan is in specs/plans/<SYS>.json. Write exactly the cases in your assigned id range, keeping each case's id, dx, and codes.
- Each case has 4 questions, one per target, in the target order. Question i must test exactly its target competency: set "obj" to the target obj and "sea" to the target sea. Look up the competency text in nplex-competencies.js (the "objectives" lists) and make the question test that skill at USMLE depth.
- "comp": the unit the obj belongs to, or the specific NPLEX condition code when the question is about one listed condition (for example obj GI-13-B.1 with comp GI-13-B1). It must be consistent with obj.
- Two-step reasoning, DOK 2 or 3, homogeneous options, correct option never the longest, no negative stems, full approach, why, whyNot for every option, and study fields.
- Numbers: give units and reference ranges for anything the student must judge. Temperatures in Celsius with Fahrenheit in parentheses.
- Output: content/<sys>/cases-<firstid-lowercase-suffix>.json, for example content/gi/cases-c01.json for GI-C01 to GI-C10.

## If you are writing STUDY UNITS
- Write study units (SPEC section A) for exactly your assigned unit ids.
- The notes, charts, tricks, and high-yield lines must teach every competency in that unit's "objectives" list in nplex-competencies.js.
- Videos: set "videos": [] for now. A separate video pass will add verified links later. Do not search for videos.
- References: only the books listed in SPEC.md, by chapter title you are sure of, or by plain section name.
- Output: content/<sys>/units-<n>.json as you are told.

## Both
- Run `python3 tools/check_content.py <your file>` and fix every ERROR and every longest-option warning.
- Then reread every item once as a hostile board reviewer and fix anything doubtful.
- Scripts only inside your own scratch folder /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/<your-file-name-without-ext>-<sys>/ with a unique name. Never run a script you did not write. Edit no project file except your own output.
- Reply with ONE line only: output path, item count, and the checker's error count.
