Verdict: board-ready after minor fixes (keys changed 0, items rewritten 0, facts corrected 4, references corrected 2, mnemonics corrected 1, videos removed 0).

Reviewed all 7 study units (IN-1 to IN-7): every note bullet, chart cell, high-yield line, pitfall, trick, brain dump key point, and reference, and checked coverage against every objective in nplex-competencies.js. Coverage is complete for all 7 units. "videos" was empty in every unit and was left empty, as REVIEW.md says.

## Changes

- IN-1, notes "Histology terms": acanthosis example "acanthosis nigricans" was misleading (Robbins describes acanthosis nigricans as hyperkeratosis and papillomatosis with only minimal acanthosis). Changed the example to seborrheic keratosis.
- IN-2, chart "Ectoderm derivatives", surface ectoderm nervous system cell: said "None", but ectodermal placodes give some cranial sensory ganglion neurons as well as inner ear and olfactory epithelium. Rewrote the cell to "Placodes: inner ear and olfactory epithelium, some cranial sensory ganglion neurons".
- IN-3, notes "Membrane potential": Nernst constant changed from 61.5 to 61 to match Guyton and the stated results (61 x log(4/140) = -94 mV; 61 x log(142/14) = +61 mV). With 61.5 the K+ value is -95 mV.
- IN-3, dump "Resting potential and potassium": same constant fix in the key point (61.5 changed to 61).
- IN-3, refs: "Genetic and Pediatric Diseases" is a chapter of Robbins Basic Pathology, not Robbins and Cotran (where the chapters are "Genetic Disorders" and "Diseases of Infancy and Childhood"). Changed the book to Robbins Basic Pathology.
- IN-7, refs: same correction for "Genetic and Pediatric Diseases" (book changed to Robbins Basic Pathology).
- IN-4, tricks: the item marked "mnemonic" used a loose paraphrase ("Anterior is A/C, posterior is a poikilotherm"). Changed it to the established First Aid form: "A/C = Anterior Cooling; zap the Posterior and become a Poikilotherm", with a plain explanation.

## Checked and left as is

- All other facts checked against standard references, including: blister split levels and target proteins; Langerhans cell markers; gland control; hair cycle timing; Langman fetal skin timeline (periderm in month 2, adult layers by end of month 4); dermis origin by region; Na+/K+-ATPase, tonicity and urea; sweat chloride cutoffs (60 mmol/L or higher, under 30 unlikely); hypothalamic control, 0.58 kcal per gram of sweat, fever cytokines and PGE2, heat stroke cutoffs and classic versus exertional features, RYR1 and malignant hyperthermia, hypothermia stages and Osborn waves; collagen synthesis steps and disorders; pellagra causes; deficiency rashes; vitamin D pathway; xanthoma types; porphyria cutanea tarda; ROS formation and enzymes; UVA versus UVB; CGD organisms and tests; G1 to S checkpoint; xeroderma pigmentosum; PTCH1, BRAF, NRAS, CDKN2A; inheritance and recurrence risks; NF1 and tuberous sclerosis; filaggrin and steroid sulfatase; MC1R signaling.
- Mnemonics marked "mnemonic" ("Californians Like Girls in String Bikinis", 3 Ds of pellagra, "UVA is Aging, UVB is Burning") are established and correctly expanded.
- All other reference chapter titles confirmed (Junqueira "Skin"; Robbins "The Skin", "Environmental and Nutritional Diseases", "Cell Injury, Cell Death, and Adaptations", "Neoplasia"; Langman "Integumentary System"; Guyton "Transport of Substances Through Cell Membranes", "Membrane Potentials and Action Potentials", "Body Temperature Regulation and Fever"; Lippincott "Fibrous Proteins", "Pentose Phosphate Pathway and Nicotinamide Adenine Dinucleotide Phosphate"; Abbas "Congenital and Acquired Immunodeficiencies").

Checker: python3 tools/check_content.py content/in/units-1.json reports 0 errors, 0 warnings.
