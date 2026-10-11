# Competency Objectives Spec (NPLEX Part I + USMLE Step 1)

Read this whole file before writing. You are writing the specific competencies (learning objectives) a student must be able to do for each NPLEX Part I study unit, at USMLE Step 1 depth.

## Sources

1. NPLEX Part I blueprint (NABNE study guide, revised March 2026). This is the backbone and the exam. The units, their codes, statements, and condition lists are in `/home/claude/nplex-part1/nplex-competencies.js` (window.NPLEX_COMPETENCIES; filter by systemCode). Unit codes must not change.
2. USMLE Step 1 Content Outline (current): https://www.usmle.org/sites/default/files/2022-01/USMLE_Content_Outline_0.pdf and the Step 1 specifications page https://www.usmle.org/exam-resources/step-1-materials/step-1-content-outline-and-specifications . Fetch the PDF with WebFetch and read the section(s) for your system (and the Multisystem Processes & Disorders section for anything that belongs in your system). USMLE removed "General Principles"; foundational science now sits inside the organ systems.

## Scope rules

- Part I is biomedical science only. Do NOT write objectives for: pharmacology and drug adverse effects (except a drug as a cause of a listed condition, e.g. drug-induced nephritis), behavioral health and psychiatry, social sciences and communication, biostatistics and epidemiology, care of the well patient and screening schedules, naturopathic therapeutics. List any such USMLE topics for your system in "excluded" with the reason.
- USMLE topics that are biomedical and high yield but not named on the NPLEX blueprint (for example atrial myxoma, coarctation of the aorta, transposition of the great vessels) are added as objectives inside the closest NPLEX unit, tagged "src": "USMLE". Never create new units.

## What a good objective looks like

- One sentence, starts with a measurable verb: identify, locate, trace, describe, explain, compare, distinguish, predict, calculate, interpret, classify, relate. Never "understand", "know", "learn", "be familiar with", "appreciate".
- Specific enough that a question writer knows exactly what to test, and a student knows exactly what to study. Name the actual structures, enzymes, organisms, values, or findings.
  - Weak: "Describe the conduction system."
  - Strong: "Trace an impulse from the SA node through the AV node, bundle of His, bundle branches, and Purkinje fibers, and explain why the AV node delay allows ventricular filling."
- Under about 40 words. Plain, clear language with correct terminology.
- USMLE depth: include mechanism-to-finding links and interpretation tasks ("Predict the ECG change...", "Interpret a pressure-volume loop..."), matching USMLE's weighting toward applying foundational science and diagnosis.
- Accurate. If you are not certain a fact is standard teaching (Robbins, Guyton and Hall, Moore, Langman, Lippincott, Jawetz, Abbas, First Aid level), leave it out. The author's rule: accurate or not generated at all.
- No em dashes or en dashes anywhere (use commas, "to", parentheses). No italics or markdown. Temperatures in Celsius with Fahrenheit in parentheses.

## How many

- Numbered competency units (kind "competency"): 3 to 7 objectives each, covering every element named in the NPLEX statement. For the shared statements that repeat in every system (biochemistry of proteins, carbohydrates, lipids, vitamins, minerals, co-factors; gene expression and genetic abnormalities; innate and adaptive immune activation; microbial pathogens), make the objectives specific to THIS system (for example in Cardio: lipoprotein metabolism, cardiac fuel use, thiamine and wet beriberi; FH, HCM sarcomere genes, Marfan; rheumatic fever mimicry; organisms of endocarditis and myocarditis).
- Condition units (kind "conditions"): at least one objective per listed condition (closely related conditions may share one objective only if each is named in it), covering pathogenesis, etiology or risk factors, key clinical and lab or histologic findings, and complications as appropriate. Then add USMLE extension objectives for USMLE disorders that fit this category.

## Output format

Write one JSON file: `/home/claude/nplex-part1/content/objectives/<SYS>.json` (SYS is the two-letter system code), valid UTF-8 JSON:

```json
{
  "system": "CV",
  "objectives": {
    "CV-7": [
      {"id": "CV-7.1", "t": "Trace an impulse from ...", "dok": 2, "sea": "A", "src": "Both", "usmle": "Cardiovascular: Dysrhythmias"},
      {"id": "CV-7.2", "t": "...", "dok": 3, "sea": "P", "src": "NPLEX", "usmle": null}
    ],
    "CV-18-C": [
      {"id": "CV-18-C.1", "t": "...", "dok": 3, "sea": "X", "src": "Both", "usmle": "Cardiovascular: Ischemic heart disease", "cond": ["CV-18-C1"]}
    ]
  },
  "crosswalk": [
    {"usmle": "Cardiovascular: Neoplasms: myxoma", "where": "CV-18-J.3", "note": "Added as USMLE extension"},
    {"usmle": "Cardiovascular: Dysrhythmias: Wolff-Parkinson-White syndrome", "where": "CV-7.4", "note": ""}
  ],
  "excluded": [
    {"usmle": "Cardiovascular: Adverse effects of drugs (ACE inhibitors, calcium channel blockers...)", "reason": "Pharmacology is not on NPLEX Part I"}
  ]
}
```

Field rules:
- Every unit for your system appears as a key, in blueprint order, with its objectives.
- "id": unit id + "." + running number from 1.
- "dok": 1 (recall), 2 (apply, explain), or 3 (analyze, predict, integrate). Aim for most at 2 and 3; use 1 only for foundational identification.
- "sea": A Anatomy, P Physiology, B Biochemistry and Genetics, M Microbiology and Immunology, X Pathology. Pick the best single fit for that objective.
- "src": "NPLEX" (required by the NPLEX blueprint wording, not specifically named in the USMLE outline), "Both" (on the NPLEX blueprint and named or clearly covered in the USMLE outline), "USMLE" (USMLE Step 1 topic added as an extension, not named on the NPLEX blueprint).
- "usmle": the USMLE outline heading it maps to, written as "Section: Heading" (and ": topic" when specific), or null.
- "cond": for condition units only, the NPLEX condition codes (e.g. CV-18-C3) the objective covers; [] for a USMLE extension.
- "crosswalk": every disorder or topic named in the USMLE outline for your system's section(s), each with where it landed (an objective id) or "excluded".
- "excluded": USMLE topics left out and why.

## Coverage checks before you finish

Run `python3 /home/claude/nplex-part1/tools/check_objectives.py /home/claude/nplex-part1/content/objectives/<SYS>.json` and fix every ERROR. It checks: every unit present, objective counts, every NPLEX condition covered, ids, verbs, dashes, banned words, field values.

Then reread every objective once as a skeptical board reviewer: is it accurate, specific, measurable, and inside the scope rules?
