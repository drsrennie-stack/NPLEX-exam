# Review log: notes/chapters/CV-18-C.json (Phase 1 notes)
- FACT C03 flow step 5: time to loss of contraction changed from "about 60 seconds" to "about 1 to 2 minutes" (Robbins: less than 2 minutes).
- FACT C03 ischemic myocyte paragraph: "within about a minute" changed to "within about 1 to 2 minutes" to match.
- FACT summary line 8: same correction to "about 1 to 2 minutes".
- FACT C07 Laplace worked example: result restated as wall stress rather than tension (the calculation is P x r / h, which is stress), and the 0.8 cm wall described as an average wall thinned by dilation and scarring rather than scar alone (scar does not generate tension).
- FACT integration paragraph 3: Kawasaki disease removed from microbiology (cause unknown) and placed under immunology as an acute childhood vasculitis that can leave coronary aneurysms.
- FACT C04 biomarker table: CK-MB peak changed from "About 24 h" to "About 24 h (up to 48 h in some sources)" to reflect Robbins.
- TEACHING overview term "Acute coronary syndrome": NSTEMI and STEMI abbreviations defined at first use.
- TEACHING C01: "LV" abbreviation defined at first use in prose.
- TEACHING C03: CK-MB defined (MB isoenzyme of creatine kinase) at first use.
- EXPANDED C01 risk factors: hyperhomocysteinemia added to the associated risk factors (Robbins).
- VERIFY added: CK-MB peak timing varies (about 16 to 24 vs 24 to 48 hours).
- VERIFY added: time to loss of contraction (under 2 minutes vs about 60 seconds).
- CHECKED without change: coronary flow and extraction values, Poiseuille arithmetic, ST vector physiology, territory and lead table, Q wave criteria, troponin and myoglobin kinetics, Robbins morphologic timeline and TTC timing, mechanical complications and papillary muscle supply, true aneurysm vs pseudoaneurysm, Dressler, chronic IHD morphology, all 6 STOP prompts (answerable and correctly pointed), sources (real chapter titles), scope (nitroglycerin used only as mechanism).
- CHECKER: python3 tools/check_notes.py, 0 errors, 0 warnings.

## Re-review of condensed version (2026-10-13)
- CUT C03 "Inside the ischemic myocyte": removed "Coagulative necrosis preserves cell outlines for several days" (repeated in C05); C03 prose now 448 words, within the 250 to 450 limit.
- CHECKED without change: all 7 sections against competency text (each taught completely after condensing), overview (intro 110 words, 5 prerequisites, 5 connections, 12 terms), coronary flow and extraction values, Laplace and Poiseuille arithmetic, ST vector physiology, territory and lead table, Q wave criteria, biomarker kinetics, Robbins morphologic timeline, mechanical complications, Dressler, chronic IHD morphology and remodeling, both worked examples (57 and 110 words), 3 STOP prompts (answerable, correctly pointed), 5 flow/cycle figures, sources, verify list, scope (nitroglycerin as mechanism only), no dashes or italics.
- LENGTH: section prose 2,448 words total plus 196 integration; no section lengthened.
- CHECKER: python3 tools/check_notes.py, 0 errors, 0 warnings.
