# Reviewer instructions

You are an independent reviewer. You did not write this file. Your job is to make it board-ready and fully accurate. The author's rule is "accurate or not generated at all".

Read specs/SPEC.md first (including the section "Two voices"). Then review EVERY item in your assigned file.

## For case files (questions)
For each question:
1. Solve it yourself from the case and stem BEFORE looking at the key. If your answer differs from the key, decide which is right using standard references (Robbins, Guyton and Hall, Moore, Langman, Lippincott Biochemistry, Jawetz, Abbas, First Aid-level consensus). Fix the key or the item.
2. Check that no distractor is defensible as correct from the wording. If one is, rewrite that distractor.
3. Check every fact and number in the case, stem, why, whyNot, and approach. Lab values must have units and, where a student must judge them, reference ranges. Fix errors; remove claims you cannot confirm.
4. Apply the exam-writer voice to the case summary, stem, and options (NBME/NPLEX style: "comes to the physician because of", "Physical examination shows", "Which of the following is the most likely..."). Keep explanations in the plain teaching voice.
5. Confirm whyNot[answer] is exactly "Correct." and each other entry explains that specific option.
6. Confirm "sea", "comp", "dok" tags fit. Fix mis-tags.
Do not rewrite good items for taste. Do not change the number of cases or questions. Do not worry about answer-letter balance (a build step re-randomizes positions later), but never refer to an option by its letter or position anywhere in the text.

## For study-unit files
1. Check every note bullet, chart cell, high-yield line, pitfall, trick, and brain dump key point for accuracy. Fix or remove anything wrong or unconfirmable.
2. Mnemonics marked "mnemonic" must be well-established ones, correctly expanded. Anything original must be "kind": "trick".
3. References: book must be one of those listed in SPEC.md; "where" must be a chapter title you are confident exists in a recent edition, or a plain section/topic name. No chapter or page numbers.
4. Videos: re-verify EVERY video by fetching https://www.youtube.com/oembed?url=<the video url>&format=json with WebFetch. Keep it only if it returns successfully, the "author_name" is the stated channel (Ninja Nerd, Khan Academy / Khan Academy Medicine, Armando Hasudungan, Dr. Najeeb Lectures), and the title matches. Correct the title to the exact oEmbed title. Remove any that fail. If the fetch tool is rate-limited, retry once after other work; if it still fails, keep only links whose ID you have independently seen in a search result for that title.
5. Plain student language in notes; brief bullets.

## How to edit
Edit the JSON file in place. If you use a script, give it a unique name inside your own folder (for example /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/review-<yourfile>/fix.py). Never write or run a generically named script such as build.py, and never touch any file except your assigned one and your review log.

Afterward run: cd /home/claude/nplex-part1 && python3 tools/check_content.py <your file>  and fix every ERROR.

## Review log
Write specs/reviews/<your file name without .json>.md listing every change: item id, what was wrong, what you changed. Start it with a one-line verdict and counts (keys changed, items rewritten, facts corrected, videos removed).
