Verdict: board-ready after minor edits; all 40 keys confirmed correct. Keys changed: 0. Items rewritten: 1 option (exam voice). Facts corrected: 3. Explanations clarified: 4. Videos removed: 0 (not applicable to case files).

# Review log: content/en/cases-c21.json

I solved every question from the case and stem before reading the key, and all 40 keys matched. No distractor can be defended as correct from the wording. Every whyNot entry at the key reads exactly "Correct.", and each other entry explains its own option. No text refers to an option by letter or position, and there are no en or em dashes. Every obj code exists in nplex-competencies.js, belongs to the unit named in comp, and is actually tested by its question. Each case mixes at least three SEAs. Lab values that students must judge carry units and reference ranges. The sea, comp, obj, and dok tags fit, so I left them unchanged.

## Facts corrected
- EN-C24-Q1 why: said hypertension and cardiomyopathy are "the main causes" of excess mortality in acromegaly. Cardiovascular disease is a leading cause, alongside respiratory disease and cancer. Changed to "a leading cause of its excess mortality".
- EN-C27-Q1 why: said craniopharyngioma is "most common in children". Its age distribution is bimodal. Changed to "It has a peak in childhood and a second peak in older adults."
- EN-C27-Q3 approach step 3: blamed delayed bone age partly on low sex steroids, which does not apply to a prepubertal 9-year-old. Changed to "GH deficiency (and any accompanying central hypothyroidism) slows skeletal maturation, so bone age is delayed."

## Items rewritten
- EN-C23-Q1 option (delayed diagnosis): "Low libido is subtle, so diagnosis is often delayed" changed to "Decreased libido is subtle, delaying diagnosis" (clinical term; also keeps the key from being the longest option). Approach step 3 "erectile problems" changed to "erectile dysfunction".

## Explanations clarified
- EN-C22-Q2 whyNot (surface ectoderm option): the entry talked about oral ectoderm instead of the option given. Now explains what surface ectoderm forms (epidermis, lens, Rathke pouch via oral ectoderm) and that sympathetic ganglia and the medulla come from neural crest.
- EN-C22-Q3 whyNot (dopamine beta-hydroxylase option): fixed grammar to "whose breakdown products are normetanephrine and VMA".
- EN-C27-Q2 whyNot (neural crest into third pouch option): the entry covered only the pouch's endoderm. Added that neural crest cells reaching the ultimobranchial body form thyroid C cells, not pituitary tissue.

## Checked and left as is
- EN-C29-Q4 keys thyroid C cells as neural crest. Some lineage-tracing work in mice suggests an endodermal origin, but the standard references and the EN-2.5 competency both teach neural crest, so the key stands.
- EN-C26-Q2 and EN-C28-Q3 are tagged sea P while their obj codes default to X. Both test physiological reasoning (loss of prolactin's action; renal response to desmopressin), and retagging would drop each case below three SEAs, so the tags stay.

Checker: python3 tools/check_content.py content/en/cases-c21.json reports 0 errors, 0 warnings.
