Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 3, videos removed 0.

# Review log: content/cv/units-u1.json (CV-1 to CV-7)

Reviewer read specs/SPEC.md and specs/REVIEW.md, then checked every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, reference, and video in all seven units.

## Changes

| Unit | Field | What was wrong | Change |
|---|---|---|---|
| CV-5 | notes "Energy", bullet 1 | "Strictly aerobic" overstates it; myocardium has limited anaerobic glycolysis (relevant in ischemia). | Now "depends almost entirely on aerobic metabolism and burns mostly fatty acids at rest." |
| CV-6 | notes "Afterload", bullet 2 | Wording implied aortic pressure is raised in aortic stenosis. In AS the LV afterload rises, while aortic pressure is normal or low. | Now "For the LV it mostly tracks aortic pressure; it rises in hypertension and in aortic stenosis." |
| CV-4 | highYield, c wave line | "c wave and x descent reflect tricuspid valve motion" was incomplete; the x descent is mainly atrial relaxation plus the tricuspid ring pulled down. | Rewritten to state each component correctly, matching the unit's own notes. |

## Checked and kept (no change needed)

- Mnemonics marked "mnemonic" are all well-established (First Aid-level): aortic arch derivatives, 5 Ts of early cyanosis, C3-4-5 keeps the diaphragm alive, All Physicians Take Money, Kentucky/Tennessee, Park AT VENtura AVenue. Original aids are all marked "trick" and are correct.
- Numbers confirmed against Guyton and Hall / First Aid consensus: EDV, ESV, SV, EF, PA pressure, conduction velocities (atria about 0.3 m/s, ventricles 0.3 to 0.5 m/s, Purkinje 1.5 to 4 m/s), pacemaker rates, nodal artery percentages (60% and 80%), lead angles, QRS axis, ECG intervals, mean systemic filling pressure about 7 mmHg, intrinsic SA rate about 100 bpm, PFO prevalence about 1 in 4.
- References: all books are on the SPEC list; all "where" entries are real chapter titles in recent editions (Langman "Cardiovascular System"; Guyton "Fetal and Neonatal Physiology", "Cardiac Muscle; The Heart as a Pump and Function of the Heart Valves", "Heart Valves and Heart Sounds; Valvular and Congenital Heart Defects", "Cardiac Output, Venous Return, and Their Regulation", "Nervous Regulation of the Circulation and Rapid Control of Arterial Pressure", "Rhythmical Excitation of the Heart", "Fundamentals of Electrocardiography"; Junqueira "The Circulatory System", "Muscle Tissue") or plain section names. No chapter or page numbers.

## Videos (all 26 re-verified by YouTube oEmbed)

Every video returned successfully, author_name matched the stated channel (Khan Academy entries return "khanacademymedicine"), and every stored title matched the oEmbed title exactly. None removed, no titles changed.

- CV-1: RjiPx6Xi-68 (Ninja Nerd), rYVGjbzmAtg (Dr. Najeeb Lectures), -IRkisEtzsk (Khan Academy Medicine)
- CV-2: UiMHnNHmgHM (Najeeb), dgAbpwp9gF8 (Ninja Nerd), bm65xCS5ivo (Khan), 7b6LRebCgb4 (Khan)
- CV-3: jU9w6w8LwqM (Ninja Nerd), HYr2NiOvjZE (Armando Hasudungan)
- CV-4: xamYVlNF5Zo (Ninja Nerd), -4kGMI-qQ3I (Khan), XbivIaFPoQI (Najeeb), IdRb3OjFAtQ (Najeeb)
- CV-5: rIVCuC-Etc0 (Khan), vv6WBeqw2Nc (Khan), FlyKXrY5ak0 (Armando), o7L0W3Xb5Eg (Armando)
- CV-6: 0O3FfHPE9PU (Ninja Nerd), hpQFToprlH8 (Armando), jVvQaqFOJpY (Najeeb)
- CV-7: 1kX6Tp8CWFw (Ninja Nerd), 2L4FbEEsy1s (Ninja Nerd), 7K2icszdxQc (Khan), eOX_NmYLKOE (Armando), Ku96IY27CE0 (Najeeb)

## Checker

python3 tools/check_content.py content/cv/units-u1.json: 7 study units, 0 errors, 0 warnings.
