Verdict: board-ready after voice and tagging fixes; all 24 keys verified correct. Keys changed: 0 (1 key index moved by option reorder, same answer). Items rewritten: 0. Facts corrected: 0. Videos removed: 0 (case file).

# Review log: content/cv/cases-w6.json

Every question was solved before checking the key. All 24 keys matched my answer and are supported by standard references (Moore, Guyton and Hall, Robbins, Langman, Jawetz, Abbas). No distractor was defensible as correct. Every whyNot[answer] is exactly "Correct." and every other entry explains its own option. No text refers to an option by letter or position.

## Case summaries (exam-writer voice)
- CV-C31 to CV-C36: rewrote each case summary into NBME/NPLEX register ("comes to the physician because of", "is brought to the emergency department", "Physical examination shows", "An ECG shows"). Replaced lay terms (neck veins distended, small thumbs, lies flat, hole in his heart) with clinical terms (jugular venous distention, hypoplastic thumbs, supine, congenital heart defect). Put vital signs in standard order (temperature, pulse, respirations, blood pressure) and used "pulse" instead of "heart rate". No facts, values, or reference ranges changed. Word counts 110 to 137.

## Stems (exam-writer voice)
- All 24 stems: recast lead-ins as complete "Which of the following..." questions in clinical register. Content of each stem unchanged except as noted below.
- CV-C32-Q3: removed the hinting sentence "which is one reason his low CD4 count matters" from the stem (the point stays in the explanation).
- CV-C33-Q1: removed "explaining why it is referred to that area of skin" so the lead-in poses one task.

## Options
- CV-C32-Q1: the keyed option was the only one not starting with "Inspiration", a grammatical cue. Reworded to "Inspiration adds right ventricular filling that bows the septum leftward" (same meaning).
- CV-C32-Q2: numeric options reordered in ascending order (by RA pressure) per SPEC. whyNot entries moved with their options; key index changed from 1 to 3, same correct answer (RA 19, RV 34/19, wedge 19).

## Tags
- CV-C34-Q4: comp CV-2 changed to CV-18-G1. The item tests the pathology of bicuspid valve aortopathy (medial degeneration), a disease feature, not normal histology.
- CV-C35-Q4: sea X changed to A. The item is answered from the anatomy of the ductus insertion relative to the aortic arch branches (comp CV-9 kept).
- All other sea, comp, and dok tags checked and fit. Each case still mixes at least three SEAs.

## Checker
python3 tools/check_content.py content/cv/cases-w6.json: 0 errors, 0 warnings.
