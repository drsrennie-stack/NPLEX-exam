Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 5, videos removed 0.

# Review log: content/im/units-1.json (IM-1 to IM-7)

Reviewer read specs/SPEC.md and specs/REVIEW.md, then checked every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, and reference in all seven units, and checked coverage against every objective in nplex-competencies.js (IM-1.1 to IM-7.5). All "videos" arrays were empty and were left empty.

## Changes

| Unit | Field | What was wrong | Change |
|---|---|---|---|
| IM-1 | highYield, adult thymectomy line | "No clinically important T cell deficiency" overstated the point; large cohort data link adult thymectomy to later health effects. The defensible teaching point is that no overt immunodeficiency results. | Now: adult thymectomy does not cause an overt T cell immunodeficiency like DiGeorge syndrome, because peripheral T cells persist. |
| IM-3 | notes "HLA genetics", parent and child bullet | "Always share exactly one haplotype" is wrong when the parents share a haplotype; the child can then match a parent on both. | Now "at least one haplotype (at least a half match)". |
| IM-3 | dumps "HLA inheritance and matching", key point | Same fact as above. | Now "share at least one haplotype". |
| IM-3 | highYield, red cell line | Said NK cells spare red cells because they lack class I. Lacking class I would remove the NK brake; red cells are spared because they also lack activating stress ligands. | Rewritten to state that reason. |
| IM-5 | notes "B cell help and class switching", CD40L bullet | Hyper-IgM syndrome has normal or high IgM, not always high (matches the corrected IM-12.4 objective). | Now "normal or high IgM". |
| IM-5 | highYield, CD40L line | Same fact. | Now "A normal or high IgM". |
| IM-7 | pitfalls, C3a and C3b line | "The b fragment stays on the surface" is not true for C2 under the C4b2a naming the unit uses (C2a is the bound piece). | Limited the rule to C3 and C5. |

(Seven edits; the IM-3 haplotype fact and the IM-5 hyper-IgM fact are each fixed in two places, giving 5 distinct facts corrected.)

## Checked and kept (no change needed)

- IM-1: third pouch ventral thymus and dorsal inferior parathyroids, fourth pouch superior parathyroids and ultimobranchial body, neural crest capsule and septa, fetal liver and marrow precursors, Hassall corpuscles, DiGeorge findings, involution timing, mediastinal location, anterior mediastinal mass chart. CATCH-22 and the 4 Ts are established mnemonics.
- IM-2: lymph node zones and lymph path, DiGeorge and XLA node patterns, follicular hyperplasia (RA, early HIV) versus paracortical hyperplasia (viral, vaccine, phenytoin), splenic white and red pulp and blood path, marginal zone, thymic cortex versus medulla and blood thymus barrier, MALT, M cells, IgA switching and pIgR transport.
- IM-3: class I and II structure, distribution, peptide length, CD8 to alpha3 and CD4 to beta2 binding, both processing pathways, cross-presentation, HLA on 6p, 25/50/25 sibling matching, beta2-microglobulin off chromosome 6, NK missing self, hyperacute rejection and crossmatch, HLA and disease chart. PAIR is an established mnemonic.
- IM-4: cisterna chyli at L1 to L2, thoracic duct course and crossing at about T4 to T5, venous angles, right duct territory, palpable node territories, first nodal spread chart, Virchow node and Troisier sign, chylothorax (triglyceride above 110 mg/dL, side by level of injury, MCT diet).
- IM-5: antibody structure and papain or pepsin fragments, isotype chart, CD40L and AID, T independent responses and conjugate vaccines, Th1, Th2, Th17, Treg induction and products, perforin, granzyme, Fas to caspase-8, primary versus secondary curves, active versus passive immunity, maternal IgG waning at about 6 months.
- IM-6: TLR ligands and signaling, NLRP3 and caspase-1, extravasation molecules and LAD types 1 and 2, fever through PGE2, acute phase reactants, hepcidin, Chediak-Higashi (LYST), foreign body versus immune granuloma, sepsis mechanism, SIRS criteria with temperatures in Celsius and Fahrenheit, superantigens. Clean up on aisle 8 and Hot T-bone stEAK are established First Aid mnemonics.
- IM-7: three pathway starts and convertases, effector fragments, C1 inhibitor targets, DAF and CD59, hereditary angioedema, PNH (PIGA), deficiency patterns, eculizumab and meningococcal risk, C3 and C4 patterns.
- References: all books are on the SPEC list; chapter titles (Langman "Head and Neck"; Junqueira "Immune System and Lymphoid Organs"; Moore "Thorax", "Pelvis and Perineum"; Abbas "Introduction to the Immune System", "Innate Immunity", "Antigen Capture and Presentation to Lymphocytes", "Humoral Immune Responses", "Effector Mechanisms of T Cell-Mediated Immunity", "Effector Mechanisms of Humoral Immunity", "Immune Responses Against Tumors and Transplants", "Congenital and Acquired Immunodeficiencies"; Robbins "Inflammation and Repair", "Diseases of the Immune System", "Diseases of White Blood Cells, Lymph Nodes, Spleen, and Thymus"; Guyton "Resistance of the Body to Infection: II. Immunity and Allergy") exist in recent editions; the rest are plain section names.
- Coverage: every objective IM-1.1 through IM-7.5 is taught in the notes, charts, or high-yield lines.

Checker: python3 tools/check_content.py content/im/units-1.json reports 0 errors, 0 warnings.
