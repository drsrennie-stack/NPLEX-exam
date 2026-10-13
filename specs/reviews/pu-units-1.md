# Review: content/pu/units-1.json (PU-1 to PU-7)

Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 5, videos removed 0 (all "videos" arrays were empty and left empty).

Every note bullet, chart cell, high-yield line, pitfall, trick, brain dump key point, and reference was checked against Langman, Junqueira, Moore, Guyton and Hall, Robbins, and First Aid-level consensus. All objectives for PU-1 to PU-7 in nplex-competencies.js are taught; no coverage gaps found. Mnemonics marked "mnemonic" (Every Pulmonologist Can See Alveoli, LEGS, I 8 10 Eggs At 12, RALS, the 4 Ts, C3 4 5 keeps the diaphragm alive) are established First Aid-level aids. All reference chapter titles were confirmed as real chapter titles or given as plain sections.

## Changes

- PU-4, tricks (diaphragm mnemonic): the expansion "10 EGGS: Esophagus and vaGus" bent the standard mnemonic into a forced letter match. Rewrote it to the standard form ("I ate ten eggs at twelve": IVC T8, esophagus with vagal trunks T10, aorta with thoracic duct and azygos T12) and normalized the label to "I 8 10 Eggs At 12".
- PU-5, notes "Two blood supplies" and chart "Pulmonary versus bronchial circulation": stated that bronchial arteries come straight from the aorta. The right bronchial artery usually arises from a posterior intercostal artery. Changed to "thoracic aorta, directly or through an intercostal artery".
- PU-6, notes "Chemoreceptors": the bullet implied that oxygen-induced hypercapnia in CO2 retainers comes from loss of hypoxic drive. Rewrote it to give the accepted main mechanisms (worse V/Q matching from released hypoxic vasoconstriction, and the Haldane effect). Bullet count kept at 35.
- PU-7, trick "Which number is low": it put CO poisoning under "only content low", which contradicted the unit's own chart (true SaO2 is low in CO poisoning). Rewrote it to separate anemia (SaO2 normal) from CO (true SaO2 low).
- PU-7, pitfalls: "a high PaCO2 with a widened gradient means two problems at once" was wrong, because severe V/Q mismatch (for example COPD) can raise PaCO2 and widen the gradient by itself. Rewrote it to say lung disease is present, alone or on top of hypoventilation.

Checker: python3 tools/check_content.py content/pu/units-1.json gives 0 errors, 0 warnings.
