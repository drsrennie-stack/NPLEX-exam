Verdict: board-ready after minor fixes. Keys changed: 0. Items rewritten: 0. Facts corrected: 4. Videos removed: 0 (case file, no videos).

I solved all 40 questions before looking at the keys, and all 40 keys matched. Every case, stem, option, approach, why, and whyNot was checked for accuracy, lab units and reference ranges, temperature conversions, distractor defensibility, exam-writer voice, whyNot alignment ("Correct." at the key), and sea/comp/obj/dok fit against nplex-competencies.js. Unit-level comp codes (IM-15-D for mixed connective tissue disease, IM-15-E for beta2-microglobulin amyloid) were kept because neither topic has its own condition code.

## Changes

- IM-C21-Q2, option (alternative pathway, the key): The wording "C3 tickover with factor B on bacterial antigens" mixed two separate steps, because tickover is spontaneous C3 hydrolysis in plasma and is not something that happens on bacterial antigens. Changed it to "C3b binding factor B on bacterial antigens". This is accurate, and it keeps the key from being the longest option.
- IM-C23-Q3, whyNot for IL-4: It said flatly that IL-4 does not form epithelioid cells. IL-4 can drive macrophage fusion into giant cells in some settings, such as Th2 and foreign-body granulomas. Reworded it to say IL-4 does not produce the activated epithelioid macrophages of a Th1 granuloma like those in sarcoidosis.
- IM-C24-Q2, why: It said she had started "high-dose glucocorticoids", but the case never gives her dose. Changed it to say that glucocorticoids raise the risk of renal crisis, especially at about 15 mg/day of prednisone or more, so her recent prednisone also matters.
- IM-C30-Q1, whyNot for maternal antibody: It called the cousin "his", but the case never gives the cousin's sex. Reworded it to "a fully vaccinated 5-year-old has already made antibody against the type b capsule."

## Checker
python3 tools/check_content.py content/im/cases-c21.json: 0 errors, 0 warnings.
