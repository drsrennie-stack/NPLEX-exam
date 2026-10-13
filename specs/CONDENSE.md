# Condense a comprehensive notes chapter

The chapter in your file was written far too long. Rewrite it IN PLACE to the length rules now in specs/NOTES-P1.md (read the whole spec first), keeping it complete and accurate.

- Keep every section, every competency ID, the JSON schema, and the order.
- Target about 250 to 450 words of prose per competency. Total prose rarely above 3,500 words.
- Cut repetition, restatement, warm-up sentences, and anything another section already teaches. Keep every mechanism and fact a board question on that competency needs.
- Move lists, comparisons, and sequences into tables or flows rather than paragraphs. Merge overlapping tables. Keep at most about 6 tables and 2 to 5 flow or cycle figures per chapter. Keep any "diagram" blocks that teach something.
- Overview: intro at most 120 words, 3 to 5 prerequisites, 3 to 5 connections, 8 to 12 key terms. Summary 6 to 10 lines. Worked examples 1 or 2, each under 150 words. STOP prompts at most 3. Integration 1 or 2 short paragraphs.
- Do not add new facts. If you notice an error while condensing, fix it and add a line about it to specs/reviews/notes1-<unit>.md.
- Writing rules from specs/SPEC.md still apply (no em or en dashes, no italics, smooth professional prose).
- Run `python3 tools/check_notes.py <file>`; fix every ERROR and every word-count WARN.
Scripts only in /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/cond-<unit>/.
Reply with ONE line: file, words before, words after, checker errors.
