Verdict: board-ready after one precision fix. Counts: keys changed 0 (study-unit file, no keys), items rewritten 0, facts corrected 1, videos removed 0.

# Review log: content/cv/units-u4.json

Reviewed all 7 units (CV-18-E, CV-18-F, CV-18-G, CV-18-H, CV-18-I, CV-18-J, CV-18-K): every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, reference and video.

## Changes

- CV-18-G, pitfalls: "PDA with Eisenmenger causes cyanosis of the toes only, because the shunt enters the aorta beyond the arm branches." The phrase "toes only" was too narrow, because the whole lower body is cyanotic, and the landmark was vague. Changed to: "PDA with Eisenmenger causes cyanosis of the lower body (blue toes, pink fingers), because the ductus enters the aorta beyond the left subclavian artery."

## Checked and left as written

- Condition coverage: every condition listed in specs/cv-units.json for each unit has a row in that unit's core chart (E1 and E2, F1 to F3, G1 to G4, H1 to H6, I1 to I12, J1 and J2, K1 to K6).
- Mnemonics marked "mnemonic" are all established First Aid mnemonics and are expanded correctly: ABCCCD (DCM causes), PROVe (TOF), eaRLy versus LateR cyanosis, FAT BAT (emboli), CRASH and Burn (Kawasaki), Bacteria FROM JANE (endocarditis), FAKE a Key Lyme pie, CARS (palms and soles rash). Original memory aids are already marked "trick" and are accurate.
- Numbers checked against Robbins, Guyton and First Aid-level consensus: DCM about 90 percent of cardiomyopathies; pericardial fluid 15 to 50 mL; pulsus paradoxus over 10 mmHg; bicuspid aortic valve 1 to 2 percent; fat embolism 1 to 3 days; petechiae 1 to 2 mm and purpura 3 mm or more; acute loss over about 20 percent of blood volume; FH heterozygote about 1 in 250, LDL over 190 mg/dL, homozygote over 500 mg/dL; ABI 0.90 or lower (normal 1.0 to 1.4); Chagas chronic disease in 20 to 30 percent; infantile hemangioma regression by about age 7 (Robbins figure).
- Shock hemodynamics chart (CO, SVR, PCWP, skin) matches the standard First Aid table, including the obstructive PCWP split (high in tamponade, low in massive PE).
- References: all books are on the SPEC list, and every "where" is a real chapter title in a recent edition or a plain section name. Robbins: The Heart; Hemodynamic Disorders, Thromboembolic Disease, and Shock; Blood Vessels. Guyton: Cardiac Failure; Heart Valves and Heart Sounds; Valvular and Congenital Heart Defects; Circulatory Shock and Physiology of Its Treatment; The Microcirculation and Lymphatic System; Hemostasis and Blood Coagulation. McPhee: Cardiovascular Disorders: Heart Disease / Vascular Disease. Langman: Cardiovascular System. Lippincott: Cholesterol, Lipoprotein, and Steroid Metabolism. Jawetz: Herpesviruses; Spirochetes and Other Spiral Microorganisms; Arthropod-Borne and Rodent-Borne Viral Diseases; medical parasitology section. No chapter or page numbers appear.

## Videos (all re-verified with YouTube oEmbed on 2026-10-07)

All 23 links returned successfully. Each one has the stated channel (Ninja Nerd, khanacademymedicine / Khan Academy, Armando Hasudungan, Dr. Najeeb Lectures) and a title that exactly matches the oEmbed title. No titles needed correction. The Khan Academy "Heatlh" misspelling and the Dr. Najeeb title ending in a brain emoji are both exactly as YouTube shows them.

- CV-18-E: -Miz9kvrrqk, ou3a7Htbrvw, VtqrKxJmBn4, INSa4QQcwFo
- CV-18-F: dQDd9OgwSV4, 9FgpLaCi_KE, Ij_ERo1Ashc
- CV-18-G: orjnzBGSNx4, m-PdQwT8mPU, Be3tuYMgA9I, U2fGKvbir24
- CV-18-H: 07N42Ragqas, NqkdqJtxIfs, hvoYD2Qu_ms, AvtS_IrlbYk, h0207xMD6b8
- CV-18-I: 4QvHj5wXdWA, 0SVP95BOUNI, YwW_Wwkhxnk, ck8W4GcYYe8
- CV-18-K: iaO8110iSzI, INSa4QQcwFo, xL98lBuAn1A

CV-18-J has no videos. Web searches for Kaposi sarcoma, HHV-8 and hemangioma videos from the four approved channels turned up no URL that could be verified, so none were added (SPEC: "If a channel has nothing verifiable for this unit, skip it").

## Checker

python3 tools/check_content.py content/cv/units-u4.json: 7 study units, 0 errors, 0 warnings.
