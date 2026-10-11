# Reviewer instructions: competency objectives

You are an independent reviewer. You did not write this file. Make it accurate, specific, and in scope. The author's rule is "accurate or not generated at all".

Read specs/OBJECTIVES.md first. Then review EVERY objective in your assigned file:

1. Accuracy. Check every fact, number, structure, enzyme, organism, gene, eponym, and mechanism named. Use standard references (Robbins, Guyton and Hall, Moore, Langman, Junqueira, Lippincott Biochemistry, Jawetz, Abbas, First Aid-level consensus). Fix errors. Remove any claim you cannot confirm. Watch for outdated nomenclature (for example renamed organisms or reclassified diseases) and update it.
2. Measurable and specific. Starts with a measurable verb; a question writer would know exactly what to test. Rewrite vague ones.
3. Scope. No pharmacology (except a drug as the cause of a listed condition), behavioral science, biostatistics, or care-of-the-well-patient content. No naturopathic therapeutics.
4. Tags. "sea", "dok", "src" ("NPLEX", "Both", "USMLE") and "cond" must fit. A "USMLE" objective must be a real Step 1 topic not named on the NPLEX blueprint; a "Both" objective must be on both.
5. Coverage. Every NPLEX condition in a condition unit is covered; every element in a numbered competency's blueprint statement is covered by at least one objective.
6. Style. One sentence, under about 40 words, plain language, no dashes, no italics or markdown.

Do not change ids except to keep them sequential if you delete or add an objective (then also update any crosswalk "where" pointing at renumbered ids). Do not add new units.

Edit the JSON in place. If you script it, use a uniquely named script inside /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/rev-obj-<SYS>/ . Never touch any other project file.

Run: cd /home/claude/nplex-part1 && python3 tools/check_objectives.py content/objectives/<SYS>.json  and fix every ERROR.

Write a log at specs/reviews/objectives-<SYS>.md: first line a one-line verdict with counts (facts corrected, objectives rewritten, added, removed, tags changed), then each change: id, what was wrong, what you changed.
