Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 9, videos removed 0 (all seven units have empty video lists, left empty for the later pass).

Scope: content/pu/units-3.json, units PU-14-B, PU-14-C, PU-14-D, PU-14-E, PU-14-F, PU-14-G, PU-14-H. Every note bullet, chart cell, trick, high-yield line, pitfall, dump key point, and ref was checked. Coverage was checked against every objective in nplex-competencies.js for each unit; all objectives are already taught, so nothing had to be added for coverage. The one mnemonic marked "mnemonic" in PU-14-C (epiglottitis 4 Ds) and in PU-14-G (VACTERL) are standard and correctly expanded. No em or en dashes found.

## Changes

- PU-14-B, notes "Chronic bronchitis": the bullet placed mucous gland hyperplasia in small airways. Submucosal gland hyperplasia is in the large bronchi; goblet cell metaplasia is in small airways. Reworded to say so.
- PU-14-D, chart "Pleural fluid types", Exudate appearance: "Cloudy or bloody" implied every exudate looks that way. Changed to "Often cloudy, may be bloody".
- PU-14-D, chart "Pleural fluid types", Empyema lab clue: added the standard low glucose and low pH findings ("Many neutrophils, organisms, low glucose and pH").
- PU-14-E, refs: Robbins and Cotran chapter title corrected to "Hemodynamic Disorders, Thromboembolic Disease, and Shock" (the "Thromboembolism" wording is the Robbins Basic Pathology title).
- PU-14-E, chart "Pulmonary hypertension groups": the chart listed groups 1 to 4 only, so it was incomplete for what it claims. Added group 5 (unclear or multiple mechanisms: sarcoidosis, chronic hemolytic anemia such as sickle cell disease, myeloproliferative disorders).
- PU-14-F, pitfalls: vocal fold polyps were described as tied to smoking only. Changed to "tied to voice strain or smoking" to match the notes and the objective.
- PU-14-G, notes "Cystic fibrosis: the defect": the bullet said cAMP and protein kinase A phosphorylate CFTR. cAMP activates PKA; PKA phosphorylates CFTR, and ATP binding then opens it. Reworded.
- PU-14-G, refs: Lippincott Biochemistry "where" narrowed from "cystic fibrosis and the CFTR chloride channel" to "cystic fibrosis and the CFTR mutation", which is how that book treats it (mutation and genetic testing), rather than channel physiology.
- PU-14-H, pitfalls: "lobar pneumonia is the reverse" implied lobar pneumonia patients look worse than their films, which is not a teaching point. Changed to "in lobar pneumonia the patient is acutely ill with dense consolidation."

## Checked and kept (notable)
- Light criteria, chylothorax triglycerides above 110 mg/dL, hemothorax hematocrit at least half of blood.
- Reid index above 0.5 (normal below about 0.4), FEV1/FVC below 0.7, DLCO patterns, asthma PaCO2 warning.
- Rhinovirus at 33 °C (91.4 °F), acid labile, ICAM-1.
- Fat embolism 24 to 72 hours, PH threshold above about 20 mmHg (25 in older sources), BMPR2, HHT.
- Sweat chloride 60 mmol/L or higher, F508del, Bochdalek hernia, sequestration supply.
- Tuberculosis tests, endemic fungi, diphtheria EF-2, pertussis lymphocytosis, zoonoses.

Checker: python3 tools/check_content.py content/pu/units-3.json reports 0 errors, 0 warnings.
