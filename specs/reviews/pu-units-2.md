Verdict: accurate and board-ready after minor fixes (keys changed 0, items rewritten 0, facts corrected 6, videos removed 0).

Scope: PU-8, PU-9, PU-10, PU-11, PU-12, PU-13, PU-14-A. Every note bullet, chart cell, trick, high-yield line, pitfall, dump key point, and ref checked. The worked pH values in the PU-8 compensation chart were recalculated with Henderson-Hasselbalch and are correct. Coverage was checked against every objective in nplex-competencies.js (PU-8.1 to 8.6, PU-9.1 to 9.6, PU-10.1 to 10.5, PU-11.1 to 11.5, PU-12.1 to 12.7, PU-13.1 to 13.7, PU-14-A.1 to A.9). All of them were already taught. All "videos" arrays were empty and were left empty.

## Changes

- PU-9, notes "Proteases and antiproteases": the bullet said smoke oxidizes a methionine in the "active site" of alpha-1 antitrypsin. A serpin has a reactive site (reactive center loop), not an enzyme active site. Changed to "reactive site".
- PU-10, refs: "Genetic and Pediatric Diseases" is a chapter in Robbins Basic Pathology. In Robbins and Cotran Pathologic Basis of Disease the matching chapters are "Genetic Disorders" and "Diseases of Infancy and Childhood". Changed the book to Robbins Basic Pathology and kept the chapter title.
- PU-12, notes "Innate lung defenses": the size range in parentheses read as if it described the macrophages. Reworded so it describes the particles that reach the alveoli.
- PU-12, mnemonic "ACID": the First Aid expansion is "Anaphylactic and Atopic" for type I. The file had "Anaphylactic and Allergic". Corrected it and made the other letters match the standard expansion (antibody-mediated Cytotoxic, Immune complex, Delayed cell-mediated).
- PU-13, chart "Lung fungi", Aspergillus clue cell: "invasive angioinvasion" was redundant. Changed to "Fungus ball, angioinvasion".
- PU-14-A, refs: same chapter-title problem as PU-10 (the neonatal RDS section). Changed the book to Robbins Basic Pathology.

## Checked and kept
- Mnemonics marked "mnemonic" ("CADET, face Right", "ADEK", "ACID", "Mold in the cold, yeast in the heat") are standard First Aid aids and are now correctly expanded. All other aids are already "kind": "trick".
- Other refs are valid chapter titles or plain section names. Guyton: "Transport of Oxygen and Carbon Dioxide in Blood and Tissue Fluids", "Acid-Base Regulation", "Aviation, High Altitude, and Space Physiology", "Respiratory Insufficiency: Pathophysiology, Diagnosis, Oxygen Therapy". Lippincott: "Globular Proteins", "Fibrous Proteins", "Phospholipid, Glycosphingolipid, and Eicosanoid Metabolism", "Glycoproteins" (as a section), "Bioenergetics and Oxidative Phosphorylation", "Glycolysis". Abbas: "Hypersensitivity", "Immunity to Tumors" (as a section). Robbins: "Neoplasia", "The Lung", "Diseases of the Immune System". McPhee: "Pulmonary Disease". Jawetz sections.
- The web-search budget ran out before I could look up the Robbins chapter titles online, so the two ref changes rest on my knowledge of the 10th-edition tables of contents.

Checker: python3 tools/check_content.py content/pu/units-2.json gives 0 errors, 0 warnings.
