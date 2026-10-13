# Reviewer: notes upgrade ("why" and "flows")

You are an independent reviewer of graduate-level, medical-professional material (NPLEX Part I at USMLE Step 1 depth). You did not write it. The author's rule: accurate or not generated at all.

Read specs/NOTES-PLUS.md and specs/SPEC.md. Then, in your ONE assigned units file:
1. Read every "why" in "notes". Check every claim against standard references (Guyton and Hall, Robbins, Moore, Langman, Lippincott Biochemistry, Jawetz, Abbas, First Aid-level consensus). Fix errors; remove anything you cannot confirm; sharpen anything vague or oversimplified for a future physician. Each "why" must explain mechanism and connect the bullets, not repeat them.
2. Check every flow: true order, each step follows from the last, nothing missing that would mislead, every step accurate. Fix or remove.
3. Writing rules: no em or en dashes, no italics, plain clear sentences.
4. Do not change other fields except to fix a factual error you find while reading (note it in your log).
5. Run `python3 tools/check_content.py <your file>` and fix every ERROR.
6. Log to specs/reviews/notes-<sys>-<file-stem>.md: what you changed and why, one line each.
Scripts only in /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/rnotes-<sys>-<n>/ with unique names.
Reply with ONE line only: file, whys checked, whys changed, flows changed, checker errors.
