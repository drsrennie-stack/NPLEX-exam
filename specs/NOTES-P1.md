# Comprehensive Board Review Notes, Part I (Phase 1) — writer spec

These notes are the PRIMARY instructional resource for NPLEX Part I (Biomedical Science). Audience: naturopathic medical students, graduate and medical-professional level, USMLE Step 1 depth. The notes must TEACH: a learner should be able to understand the science, explain the mechanisms, and apply them to board questions using these notes alone. Do not write a high-yield outline or a list of isolated facts. Explain why things happen, not only what happens.

Author byline: Dr. Sharilyn Rennie (no credential suffix). Brand: MedMasters Collaborative.

## Accuracy first
- Accurate or not at all. Use the consensus of standard references (Guyton and Hall, Boron and Boulpaep, Robbins, Moore, Langman, Junqueira, Lippincott Biochemistry, Jawetz, Abbas, Lange Pathophysiology of Disease). Where sources differ, give the consensus value and say "about".
- Never invent citations, values, eponyms, or mnemonics. Anything you are not certain is current, or that needs checking against official NABNE material, goes in "verify" instead of being stated as fact.
- Numbers carry units; give reference ranges when a learner must judge a value. Temperature in Celsius with Fahrenheit in parentheses.

## Writing rules
- Clear, precise, professional prose. Define a term the first time it is used, then rely on it. Smooth connected sentences, not choppy fragments. Short paragraphs (2 to 5 sentences).
- No em dashes or en dashes anywhere (use commas, parentheses, colons, or "to" for ranges). No italics, no markdown emphasis in text. Never write "Given not Googled". No filler or motivational talk.
- Part I is biomedical. Teach normal structure and function, mechanisms, regulation, pathophysiology, clinical manifestations explained by mechanism, and the biomedical basis of diagnostic findings (for example what an ECG change or lab value means mechanistically). Do NOT teach treatment or clinical management (that is Part II). A drug may appear only when it explains a mechanism (for example how blocking a channel changes the action potential), never as a treatment recommendation.

## Identifiers (permanent)
Use the registry in notes/registry/identifiers.json. Chapter ID example: NPLEX-P1-CARD-07. Competency IDs: NPLEX-P1-CARD-07-01-C01 and so on; each maps to one course competency (CV-7.1). Every competency in your unit gets exactly one section, in order, headed by its ID. Never invent an ID.

## Output: notes/chapters/<UNIT>.json (for example notes/chapters/CV-7.json)
```json
{
  "unit": "CV-7",
  "chapter_id": "NPLEX-P1-CARD-07",
  "topic_id": "NPLEX-P1-CARD-07-01",
  "title": "Conduction System and the Electrocardiogram",
  "subject": "Cardiovascular System (CARD)",
  "version": "1.0",
  "overview": {
    "intro": "One or two paragraphs: what this chapter covers and why it matters for the exam and for practice.",
    "prerequisites": ["Short item", "..."],
    "connections": [{"to": "Discipline or chapter", "how": "One sentence on the link"}],
    "terms": [{"term": "Automaticity", "def": "One-sentence definition"}]
  },
  "sections": [
    {
      "comp": "NPLEX-P1-CARD-07-01-C01",
      "obj": "CV-7.1",
      "title": "Short section title",
      "blocks": [
        {"type": "p", "text": "Teaching paragraph."},
        {"type": "h", "text": "Subheading inside the section"},
        {"type": "bullets", "items": ["Use sparingly, for true lists"]},
        {"type": "table", "title": "Table title", "cols": ["A", "B"], "rows": [["...", "..."]], "caption": "What the table shows"},
        {"type": "flow", "title": "Figure title", "steps": ["Step", "Step", "Step"], "caption": "Descriptive caption"},
        {"type": "cycle", "title": "Feedback loop title", "steps": ["Stimulus", "Sensor", "Response", "Effect that feeds back"], "caption": "Descriptive caption"},
        {"type": "diagram", "name": "ecg-waveform", "caption": "Descriptive caption"},
        {"type": "example", "title": "Worked example", "text": "A worked example that walks through a difficult relationship step by step."},
        {"type": "stop", "predict": "What would happen if ...?", "explain": "Why?", "check": "Which part of this section to compare against."}
      ]
    }
  ],
  "integration": [{"type": "p", "text": "Part I integration across anatomy, physiology, biochemistry, microbiology and immunology, and pathology. Explain the reasoning, alternatives, and limits."}],
  "summary": ["Concise statement of an essential mechanism, relationship, or distinction"],
  "sources": [{"book": "Guyton and Hall Textbook of Medical Physiology", "where": "Section or chapter title (no chapter or page numbers)"}],
  "verify": ["Anything that needs checking against current official NABNE materials or that varies between sources"]
}
```

## Content requirements per chapter
- Overview: intro of at most 120 words, 3 to 5 prerequisites, 3 to 5 connections, 8 to 12 key terms.
- One section per competency, in registry order. Each section: logical progression (normal structure and function, molecular mechanism, regulation, pathophysiology, manifestations explained by mechanism, important exceptions and distinctions, links to related systems), as applicable.
- Length: write tightly. About 250 to 450 words of prose per competency, plus the tables and flows it needs. Put lists, comparisons, and sequences in tables and flows instead of paragraphs. Every competency must still be taught completely and accurately; cut repetition, restatement, and anything another section already covers. Total chapter prose should rarely exceed 3,500 words.
- Visuals: use comparison tables and 2 to 5 flow or cycle figures where a pathway, feedback loop, or causal chain exists. Flow and cycle steps are short (at most about 12 words). Use "diagram" only with a name from the list below. Visuals must be accurate and readable in grayscale.
- Worked examples: 1 or 2 per chapter, on the hardest relationships, each under 150 words.
- STOP prompts: at most 3 per chapter, after the most important concepts.
- Integration: 1 or 2 short paragraphs.
- Summary: 6 to 10 lines, after the teaching.
- Sources: 3 to 6 entries from the listed books, by chapter title you are sure of or plain section name.
- verify: honest list; empty only if nothing needs checking.

Available "diagram" names: ecg-waveform (labeled P wave, PR interval, QRS, ST segment, T wave, QT interval), conduction-pathway (SA node to Purkinje fibers), pacemaker-ap (phases 4, 0, 3 of the SA nodal action potential), ventricular-ap (phases 0 to 4 of the ventricular myocyte action potential). Request a new name in "verify" if you need another schematic.

## Finish
- Validate JSON: `python3 tools/check_notes.py notes/chapters/<UNIT>.json` and fix every ERROR.
- Re-read the whole chapter as a hostile board reviewer and a demanding professor. Fix anything inaccurate, vague, or oversimplified.
- Scripts only in /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/notes1-<unit>/ with unique names. Edit no other file.
- Reply with ONE line: file, sections, words, figures, checker errors.
