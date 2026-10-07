# NPLEX Part I Course: Content Spec

Read this whole file before writing anything. Every content file in this course follows it.

## Who it is for

Naturopathic medical students preparing for NPLEX Part I Biomedical Science. Course author and byline: Dr. Sharilyn Rennie (never add a credential suffix). Level: USMLE Step 1 depth, aligned to the NABNE NPLEX Part I blueprint (see `nplex-competencies.js`; your unit list is in `specs/cv-units.json`). Part I is strictly biomedical. Do NOT include botanical medicine, homeopathy, or naturopathic therapeutics (that is Part II).

## Accuracy comes first

- Never invent facts, values, eponyms, mnemonics, URLs, or references. If you are not sure, leave it out.
- Use the standard values and mechanisms taught in Robbins, Guyton and Hall, Moore, Langman, and First Aid-level review. Where sources differ (for example a timeline or a cutoff), use the consensus value and say "about".
- Every keyed answer must be the single best answer. No distractor may also be defensible from the wording.
- Before you finish, re-read every question and ask: would a board reviewer accept the key, and is there any second answer they could argue for? Fix anything that fails.

## Writing rules (everywhere)

- Never use em dashes (the long dash) or en dashes as punctuation. Use commas, periods, parentheses, or the word "to" for ranges (60 to 100 bpm).
- No italics anywhere. No markdown emphasis inside strings except plain text.
- Plain, human, student-friendly language. Short sentences. Correct terminology with quick explanations. No filler, no motivational talk, no "Great question", no "It's worth noting", no "Remember:" openers, no "not X, but Y" constructions.
- Temperatures: Celsius first with Fahrenheit in parentheses, e.g. 38.5 °C (101.3 °F).
- Lab values: give units and, for any value a student must judge as high or low, the reference range in parentheses the first time it appears in a case.
- Never write the phrase "Given not Googled".

## Two voices: exam writer for items, teacher for explanations

Case summaries, stems, and options are written the way a physician item writer for a licensing exam (NBME, NPLEX) writes them:
- Clinical register: "A 54-year-old man comes to the physician because of...", "is brought to the emergency department", "Physical examination shows...", "Laboratory studies show:", "Which of the following is the most likely cause of...", "...most likely explains these findings?", "...is most likely to be found?". Vital signs in standard order (temperature, pulse, respirations, blood pressure).
- Lead-ins are complete questions ending in a question mark and pose one clear task. Prefer "Which of the following..." lead-ins.
- Use precise medical terminology in stems and options, no lay paraphrase, no slang, no hints in parentheses.
- Options are short noun phrases or brief statements, parallel in grammar, and numeric options are listed in ascending order. Other option orders are randomized at build time to balance answer letters, so never refer to another option by position.
- Patient descriptions are neutral and factual.

Explanations ("approach", "why", "whyNot", "study") are written by a teacher to a student: plain, clear, short sentences that explain the reasoning.

## Output format

Write JSON only (UTF-8, valid, no comments, no trailing commas). Validate it yourself by running `node -e "JSON.parse(require('fs').readFileSync('FILE','utf8'))"` before you finish.

### A. Study unit (one object per competency unit)

```json
{
  "id": "CV-1",
  "summary": "Two or three plain sentences: what this unit is about and why it shows up on the exam.",
  "notes": [
    {"h": "Short heading", "points": ["Short bullet", "Short bullet"]}
  ],
  "charts": [
    {"title": "Chart title", "cols": ["Col A", "Col B", "Col C"], "rows": [["...", "...", "..."]]}
  ],
  "tricks": [
    {"kind": "mnemonic", "label": "The mnemonic itself", "text": "What each letter or part stands for, in one or two lines."},
    {"kind": "trick", "label": "Short name", "text": "A study trick, comparison, or way to reason it out."}
  ],
  "highYield": ["Exam-favorite fact or link, one line each (4 to 8)"],
  "pitfalls": ["Common mix-up and how to tell them apart (2 to 5)"],
  "dumps": [
    {"t": "Short title", "p": "Brain dump prompt (draw and label, trace, compare, or explain)", "l": ["Key point a good answer includes", "..."]},
    {"t": "...", "p": "...", "l": ["..."]}
  ],
  "refs": [
    {"book": "Guyton and Hall Textbook of Medical Physiology", "where": "Chapter title or section name"}
  ],
  "videos": [
    {"channel": "Ninja Nerd", "title": "Exact video title as shown on YouTube", "url": "https://www.youtube.com/watch?v=..."}
  ],
  "related": ["CV-18-C"]
}
```

Rules for study units:
- Brief. Students will not read paragraphs. Bullets of one line each, 3 to 7 notes sections, 12 to 35 bullets total.
- At least one chart per unit where a comparison or sequence exists (most units). Charts must be accurate and complete for what they claim to show.
- Tricks: 2 to 4. Use well-established mnemonics where they exist (for example the classic ones taught in First Aid). If you create an original memory aid, set "kind": "trick" and make sure it is correct. Never present an invented mnemonic as a standard one.
- For condition-category units (kind "conditions", e.g. CV-18-C), cover every listed condition: a chart with one row per condition (columns such as Cause or risk factors, Key mechanism, Classic findings, Complications) is the expected core.
- dumps: exactly two prompts. Most should ask the student to draw and label something, trace a pathway, or build a comparison table on blank paper. Each has 5 to 9 key points that a self-grader can check off. Prompt wording is plain and direct ("Draw the fetal heart at week 5 and label..."), never a clever abstraction.
- refs: 2 to 4 entries, chosen from these books only, pointing to a chapter TITLE or section name, never a chapter or page number:
  - Moore, Clinically Oriented Anatomy (gross anatomy)
  - Langman's Medical Embryology (embryology)
  - Guyton and Hall Textbook of Medical Physiology (physiology)
  - Lange: Pathophysiology of Disease (McPhee and Hammer) (pathophysiology)
  - Robbins and Cotran Pathologic Basis of Disease, or Robbins Basic Pathology (pathology)
  - Junqueira's Basic Histology (histology)
  - Lippincott Illustrated Reviews: Biochemistry (biochemistry, genetics, nutrition)
  - Jawetz, Melnick, and Adelberg's Medical Microbiology (a Lange text) (microbiology)
  - Abbas, Basic Immunology (immunology)
  Only cite a chapter title you are confident exists in a recent edition. If unsure of the title, name the topic as the section ("section on fetal circulation") rather than inventing a chapter name.
- videos: search the web for real videos on this unit from these channels: Ninja Nerd, Khan Academy (including Khan Academy Medicine), Armando Hasudungan, Dr. Najeeb Lectures. Use WebSearch, then confirm each URL with WebFetch (the page must load and its title must match). Include only verified links, one or two per channel at most, 2 to 5 total. If a channel has nothing verifiable for this unit, skip it. Dr. Najeeb's full library is on drnajeeblectures.com behind a paywall; link his YouTube uploads only. Never construct or guess a video ID.

### B. Case (NPLEX cluster: one case summary plus exactly four questions)

```json
{
  "id": "CV-C01",
  "system": "CV",
  "dx": "The diagnosis named in the case",
  "codes": ["CV-18-C3"],
  "case": "Case summary in NPLEX style: age, sex, setting, history, key exam and lab findings with units and reference ranges, and the diagnosis stated plainly. 60 to 140 words.",
  "questions": [
    {
      "id": "CV-C01-Q1",
      "stem": "The question. May add new information. Ends with a clear single-best-answer question.",
      "options": ["A text", "B text", "C text", "D text"],
      "answer": 2,
      "sea": "A",
      "comp": "CV-8",
      "dok": 2,
      "approach": ["Step 1 of how to work it", "Step 2", "Step 3 (2 to 4 steps)"],
      "why": "Why the correct answer is correct, teaching the concept (2 to 5 sentences).",
      "whyNot": ["Why option A is wrong, and when it would be right", "Why B is wrong...", "For the correct option, write: Correct.", "Why D is wrong..."],
      "study": {"topics": ["Short study topic", "..."], "comps": ["CV-8", "CV-3"]}
    }
  ]
}
```

Rules for cases and questions:
- NPLEX format: the case summary states the diagnosis. The four questions ask about the biomedical science around it: anatomy and blood supply, normal physiology, biochemistry and genetics, organisms and immunology, pathogenesis, complications. Each question should be answerable from the case summary plus its own stem.
- USMLE depth means two-step reasoning: the student must connect a finding to a mechanism, structure, or consequence, not just recall a label. Pure one-line recall ("Which wave is ventricular depolarization?") is not allowed. DOK 2 or 3 only; aim for about half and half.
- "sea" is one of A (Anatomy), P (Physiology), B (Biochemistry and Genetics), M (Microbiology and Immunology), X (Pathology). Each case should mix at least three SEAs across its four questions.
- "comp" is the single best-fitting code from specs/cv-units.json: a numbered competency (CV-8) or a condition code (CV-18-C3). Use numbered competencies for normal structure, function, biochemistry, genetics, immunology, and microbiology questions; use condition codes for pathogenesis, risk factors, complications, and clinical features of the listed disease.
- Options: four, homogeneous (all the same kind of thing), similar length (the correct answer must NOT be the longest option; check this), no "all of the above", "none of the above", or "both A and B". No negative stems ("NOT", "EXCEPT", "LEAST"). No grammatical or word-repetition clues pointing to the key.
- "answer" is the 0-based index of the correct option. Spread correct positions evenly across your file: within each case of four questions use each position at most twice, and across your whole file each of 0, 1, 2, 3 should be within two of an even share. No runs of three of the same position in a row.
- "whyNot" has exactly four entries aligned with "options"; the entry at the answer index is exactly "Correct." Each wrong-option entry says why it is wrong here and, where useful, the situation in which it would be the right answer.
- "approach" shows the problem-solving path a strong student uses (identify the key clue, name the principle, apply it).
- "study.topics": 1 to 3 short topic names to review if missed; "study.comps": 1 to 3 related codes.
- Vary patients: ages, sexes, settings. Avoid stereotypes. Use realistic, internally consistent numbers.
- Within one file, do not test the same fact twice.

## File naming

- Study units: `content/cv/units-<writer>.json` as a JSON array of study unit objects.
- Cases: `content/cv/cases-<writer>.json` as a JSON array of case objects.
- Batch 1 rebuild: `content/batch1/<cv|gi>.json` as a JSON array of case objects, with an extra field on each question: "from": [original Q# numbers it replaces or keeps].

## Self-check before finishing

Run: `python3 tools/check_content.py <your file>` and fix every error it reports. Then re-read every keyed answer once more for correctness.
