Verdict: board-ready after minor fixes. Counts: keys changed 0 (study-unit file, no keys), items rewritten 1, facts corrected 2, videos removed 0 (5 video titles corrected to exact oEmbed titles).

# Review log: content/cv/units-u3.json

Units reviewed: CV-15, CV-16, CV-17, CV-18-A, CV-18-B, CV-18-C, CV-18-D. Every note bullet, chart cell, high-yield line, pitfall, trick, dump key point, reference, and video was checked.

## Facts corrected
- CV-18-D, tricks, "Bacteria FROM JANE" (kind mnemonic): the expansion dropped the leading "B". The established First Aid mnemonic starts with Bacteremia. Added "Bacteremia" so every letter is expanded.
- CV-18-A, highYield, primary aldosteronism line: "often low potassium" overstated it; most patients with primary aldosteronism are normokalemic. Changed to "high blood pressure, high aldosterone, low renin, and sometimes low potassium."

## Items rewritten
- CV-18-A, tricks, "Order of PH groups" (kind trick): the original text said "follow the blood backward from the arteries" and then listed left heart before lung tissue, which does not follow the direction of blood flow and would confuse a student. Rewrote as a plain list of the five WHO groups, noting group 2 is the most common.

## Videos
All 26 videos were fetched through the YouTube oEmbed endpoint with WebFetch. All returned successfully, every author_name matched the stated channel (Khan Academy entries return "khanacademymedicine"), and every title matched in content. None removed. Titles corrected to the exact oEmbed string:
- CV-16, ivIE8ARRIgM: trailing emoji was stethoscope (U+1FA7A); oEmbed has anatomical heart (U+1FAC0). Corrected.
- CV-16, NKnAXcM5Ly0: oEmbed title has two spaces after "causes,". Corrected to match exactly.
- CV-17, lyiLcpxa2FU: trailing emoji stethoscope corrected to anatomical heart (U+1FAC0).
- CV-18-C, oQ235E1gvrU: trailing emoji stethoscope corrected to anatomical heart (U+1FAC0).
- CV-18-D, Df-FzR7S4SM: trailing emoji microbe (U+1F9A0) corrected to anatomical heart (U+1FAC0).

## References
All references use books from the SPEC list and chapter titles or plain section names that exist in recent editions (Guyton and Hall chapter titles, Abbas "Hypersensitivity: Disorders Caused by Immune Responses", Jawetz chapter titles, McPhee and Hammer "Cardiovascular Disorders: Heart Disease / Vascular Disease" and "Pulmonary Disease", Robbins sections). No changes.

## Checked and left unchanged
- Mnemonics marked "mnemonic" (ACID, HACEK, SAD, J♥NES, TIPS, Bacteria FROM JANE) are established First Aid mnemonics and are correctly expanded after the fix above. Original memory aids are already marked "trick".
- Numbers checked against Guyton and Hall and Robbins: pulmonary pressures, capillary pressures (7 and 17 mmHg), 28 mmHg edema threshold, V/Q 3, 0.6, 0.8, coronary artery infarct percentages, troponin and CK-MB kinetics, infarct timeline, 20 to 40 minute irreversibility, PH cutoff over 20 mmHg, ACC/AHA 2017 stages, HF ejection fraction cutoffs.

## Checker
python3 tools/check_content.py content/cv/units-u3.json: 7 study units, 0 errors, 0 warnings.
