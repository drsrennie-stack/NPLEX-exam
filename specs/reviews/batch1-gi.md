Verdict: board-ready after edits; all 32 keys confirmed correct. Keys changed: 0. Items rewritten: 1 (distractor). Facts corrected: 3. Videos removed: 0 (case file, no videos). Exam-voice edits: 8 case summaries, 30 stems.

# Review log: content/batch1/gi.json

Reviewer solved every question before reading the key. All 32 keys matched. No distractor was defensible as a second best answer, except the cross-item cue noted under DX-GI-C06-Q3. All whyNot arrays have "Correct." at the answer index, and every wrong-option entry explains that option. sea, comp, and dok tags all fit; no retags were needed. No item refers to an option by letter or position.

## Coverage of original questions 31 to 60

Every original number 31 to 60 appears in exactly one question's "from" field. 39 and 51 share DX-GI-C03-Q1. DX-GI-C06-Q4, DX-GI-C08-Q2, and DX-GI-C08-Q3 are new items (from: []).

Audit actions checked against specs/batch1-gi.json:
- Keep (32, 36, 41, 42, 43, 45, 46, 47, 53, 56, 57, 58, 60): kept as the same concept, rebuilt into cases (C01-Q1, C08-Q1, C04-Q1, C06-Q3, C03-Q2, C07-Q2, C01-Q3, C04-Q3, C05-Q1, C01-Q2, C01-Q4, C02-Q1, C04-Q4).
- Rewrite as a case (31, 33, 34, 35, 37, 38, 40, 44, 50, 54, 55, 59): done (C02-Q3, C03-Q4, C02-Q2, C05-Q3, C03-Q3, C02-Q4, C04-Q2, C07-Q3, C07-Q4, C06-Q2, C05-Q2, C05-Q4). Recall items now need a two-step link to the case.
- 37 and 38 overlap: resolved. Q37 became the gastrin, ECL cell, histamine pathway (C03-Q3); Q38 became the CCK source cell (C02-Q4).
- 39 retag SEA, merge with 51: done. C03-Q1 is tagged M (GI-12) and tests both gram stain/oxygen use and urease.
- 48 retag system, rewrite as case: done. C08-Q4 uses NE-20-E3 and is set in a case (maternal PKU).
- 49 positive-stem rewrite: done. C07-Q1 asks the expected course; no negative wording.
- 52 tighten option wording: done. C06-Q1 key reads "Removes one adenine from 28S rRNA in the 60S subunit" (N-glycosidase action), no longer "cleaves".
- Notes for 47 (GI-8) and 60 (GI-13-C1): codes used as the audit suggested.

## Changes

### Case summaries (exam-writer voice)
- DX-GI-C01, C02, C04, C05, C06, C07, C08: rewritten into NBME register ("comes to the physician because of", "is brought to the physician", "is evaluated because", "Physical examination shows", "Laboratory studies show"). No facts, numbers, or ranges changed.
- DX-GI-C03: added the "comes to the physician because of" opener and moved the presenting complaint to the front. No facts changed.

### Stems (lead-ins converted to "Which of the following..." single-task questions)
- C01-Q1, Q2, Q3, Q4; C02-Q1, Q2, Q3, Q4; C03-Q1, Q2, Q3, Q4; C04-Q1, Q2, Q3, Q4; C05-Q1, Q3, Q4; C06-Q1, Q2, Q3, Q4; C07-Q1, Q2, Q3, Q4; C08-Q1, Q2, Q3, Q4. Meaning and key unchanged.
- C01-Q3: "Loss of which factor raises the PT first" became "Deficiency of which of the following factors prolongs the prothrombin time (PT) earliest".
- C02-Q3: removed the stem hint "pressure rises in every vein that drains into it" (it pointed toward the answer).
- C05-Q2: lay wording "air bubbles in her urine ... bowel organisms" replaced with "pneumaturia ... enteric organisms"; approach step updated to match.
- C07-Q4: "catch hepatitis D" became "acquire hepatitis D"; "serology" became "serologic results".

### Options
- C02-Q2: key option "Hepatic artery proper, portal vein, bile duct" given "and" to match the grammar of the other three options.
- C08-Q4: distractor "PKU is recessive" changed to "PKU is autosomal recessive" so the options are parallel and the key is not the only one naming the full mode.
- C06-Q3 (item rewritten, distractor): the distractor "Removes an adenine from 28S rRNA, so enterocytes die and slough off" restated the key of C06-Q1 in the same case, giving away that answer. Replaced with "Forms pores in enterocyte membranes, so the cells lyse" (Clostridium perfringens enterotoxin) and rewrote its whyNot entry. Key unchanged.

### Facts corrected
- C01-Q1 why: "the most dangerous complication of portal hypertension" was an unsupported ranking. Changed to "a leading cause of death in cirrhosis".
- C04-Q2 why: "Calcium is also absorbed mainly in the duodenum" is imprecise (most calcium by mass is absorbed passively in the jejunum and ileum). Changed to "Active, calcitriol-driven calcium absorption also happens mainly in the duodenum."
- C08-Q1 approach: the specific timeline "enter the foregut in week 4 ... reach the end of the hindgut by about week 7" could not be confirmed against a single consensus value (sources give weeks 5 to 7 and 7 to 12 by different measures). Replaced with a plain head-to-tail migration statement.

## Checker
python3 tools/check_content.py content/batch1/gi.json: 8 cases, 32 questions, answer letters {'A': 8, 'B': 8, 'C': 8, 'D': 8}; 0 errors, 0 warnings. JSON validated with node.
