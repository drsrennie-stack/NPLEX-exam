# Review log: notes/chapters/IN-8.json (Phase 1, comprehensive notes)

Reviewer pass against specs/NOTES-P1.md. Chapter length held at the pre-review level (no net lengthening); every section stays inside the checker word band.

## Facts corrected
- C02 table, irreversible plasma membrane row: "enzymes such as troponin leak into blood" corrected to "intracellular proteins such as troponin"; troponin is a structural myofibrillar protein, not an enzyme.
- C02 prose: same correction, and the troponin claim narrowed to "becomes detectable once myocytes are irreversibly injured rather than during brief reversible ischemia" so it is defensible against high-sensitivity assay data.
- C03 prose: coagulative necrosis described as "a wedge-shaped pale infarct in heart, kidney, spleen, or liver" corrected; wedge shape follows segmental arterial supply (kidney, spleen, lung), while a myocardial infarct is regional in shape.
- C03 table, coagulative row: removed liver from the classic coagulative infarct list (dual hepatic blood supply makes liver infarction atypical as a teaching example).
- C03 worked example: "firm pale wedge" at two days corrected to "pale and mottled" with neutrophils at the margin, matching gross and histologic findings at that interval rather than the later firm pale-tan stage.
- C04 prose: "a DNase" named as caspase-activated DNase.
- C04 table, energy row: necrosis "None; passive collapse" corrected to "Follows ATP depletion; unregulated collapse"; necrosis is an ATP-depleted collapse, not an energy-free event.
- C05 table, melanin identifying feature: "bleaches with melanin bleach; positive for S100 and melan-A in cells" corrected to Fontana-Masson silver for the pigment, with S100 and melan-A named as melanocyte markers rather than pigment stains.
- C05 prose: tattoo hypersensitivity attributed to "red mercury-based inks" made specific as red inks containing mercury sulfide.
- C06 prose: "granulomatous disease that converts vitamin D" corrected to sarcoidosis and other granulomatous disease in which macrophages activate vitamin D.
- C08 prose: oncogene dominance explanation corrected; the reason is that the mutant protein signals regardless of the normal allele, not that one allele "already makes a signaling protein".
- Summary line 10: non sequitur removed; stage outweighing grade is now attributed to how far the tumor has already spread, with the hallmark list stated as what reaching that point requires.
- Sources: Junqueira "the integument" changed to "skin"; Abbas entry completed to "immunity to tumors and transplants"; Lippincott entry changed to plain section names (bioenergetics and oxidative phosphorylation; pentose phosphate pathway, NADPH, and reactive oxygen species) rather than an uncertain chapter title.

## Precision and teaching quality
- C01: "permanent cells ... can only enlarge" replaced with adaptation by change in cell size rather than cell number, which is accurate for neurons as well as myocytes.
- C01 table caption: reworded to state that the adaptations persist while the stimulus does and regress once it is withdrawn.
- C02: hypoxia versus ischemia rewritten as prose rather than a "note the distinction" aside, and the mechanism completed by stating that ischemia also cuts glucose delivery and so exhausts glycolysis sooner.
- C07: "listed in the table below" cross-reference removed.
- C08: BRAF substitution stated as glutamate for valine at position 600; RB, p16, cyclin D and TP53 paragraph tightened; genomic instability reworded as "an accelerator"; immune evasion list reordered to antigen loss, MHC class I downregulation, regulatory T cells, PD-L1.
- C06 flow step: "reversible with abstinence" reworded to "reversible if ethanol exposure stops" to keep the step a statement of natural history rather than management.

## Scope, writing rules, STOP prompts, sources
- Part I scope confirmed: no treatment or management content; drugs and stains appear only as mechanism or as the biomedical basis of a finding.
- No em or en dashes, no italics, no banned phrases (checker clean on all three).
- All three STOP prompts are answerable from their own sections, and each "check" field points to the correct block.
- Competency coverage verified item by item against notes/registry/identifiers.json for IN-8.1 through IN-8.8; every element named in the competency text is taught, including ribosome detachment and mitochondrial densities (IN-8.2), all six necrosis patterns with settings (IN-8.3), the three killing routes (IN-8.4), all four endogenous and both exogenous pigments (IN-8.5), xanthoma and Congo red birefringence (IN-8.6), naming rules with grade and stage (IN-8.7), and all eight named hallmarks (IN-8.8). Nothing missing, so nothing added.

## Items moved to verify
- None. The eight existing verify entries were checked and all remain honest and necessary (cytosolic calcium range, myocardial infarct timing, diffusion limit before angiogenesis, BRAF V600E frequency, eponym expectations, necroptosis and related death pathways in scope, nuclear to cytoplasmic ratios, requested new diagram names). No statement in the chapter was left unconfirmable.

## Checker
`python3 tools/check_notes.py notes/chapters/IN-8.json` : 8 sections, 6618 words, 14 figures and tables, 0 errors, 0 warnings.
