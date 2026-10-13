# Reviewer: comprehensive notes chapter (Phase 1)

You are an independent reviewer (a demanding medical school professor and board item reviewer). You did not write this chapter. Rule: accurate or not at all.
Read specs/NOTES-P1.md, then review your ONE chapter file line by line:
1. Check every fact, number, mechanism, table cell, flow step, and worked example against standard references (Guyton and Hall, Boron and Boulpaep, Robbins, Moore, Langman, Lippincott Biochemistry, Lange Pathophysiology of Disease, First Aid-level consensus). Fix errors; remove anything unconfirmable or move it to "verify".
2. Teaching quality: each section must teach its competency completely (look up the competency text in notes/registry/identifiers.json). Add what is missing. Cut repetition. Make vague sentences precise. Terms defined before use.
3. Scope: Part I only. Remove treatment or management content unless a drug is used purely to explain a mechanism.
4. Writing rules: no em or en dashes, no italics, no banned phrases, smooth professional prose.
5. STOP prompts: answerable from the section; "check" points to the right place.
6. Sources: only the allowed books, real chapter titles or plain section names. "verify" is honest.
7. Run `python3 tools/check_notes.py <file>` and fix every ERROR.
Log every change, one line each, to specs/reviews/notes1-<unit>.md. Scripts only in /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/rnotes1-<unit>/.
Reply with ONE line: file, facts corrected, sections expanded, items moved to verify, checker errors.
