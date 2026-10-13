# Review log: notes/chapters/IN-12.json (Skin Pathogens)

Reviewer pass against specs/NOTES-P1.md and specs/REVIEW-NOTES-P1.md. Every competency in the registry (IN-12.1 through IN-12.8) has exactly one section in order, with the correct IDs.

## Facts corrected
- IN-12.2: "PYR positive (it hydrolyzes pyrrolidonyl arylamidase substrate)" was circular and wrong in naming; changed to "PYR positive (it produces the enzyme pyrrolidonyl arylamidase)".
- IN-12.2: immune complexes were said to deposit "in the subepithelial glomerular basement membrane", which conflates two locations; corrected to accumulation on the subepithelial side of the glomerular capillary wall, named as the subepithelial humps seen on electron microscopy.
- IN-12.2: matching flow step corrected from "Immune complexes deposit in glomerular basement membrane" to "Complexes deposit subepithelially in glomerular capillary walls".
- IN-12.3: "finely scaling macules that fluoresce or scale when scraped" merged two separate findings into one vague clause; corrected to macules that release fine scale when scraped and that may fluoresce yellow-green under a Wood lamp.
- IN-12.4: "chlamydospores" corrected to the current term "chlamydoconidia (chlamydospores)".
- IN-12.4: table cell for Th17, IL-17 receptor, CARD9 and AIRE defects said disease is "rarely invasive"; CARD9 deficiency does permit invasive candidiasis, so the cell now reads "Chronic mucocutaneous candidiasis of skin and nails; CARD9 defects can also permit invasive disease".
- IN-12.4: table caption changed from "Loss of T cell help" to "Loss of IL-17 driven epithelial defense usually keeps disease at the surface" so it is consistent with the corrected row.
- IN-12.6: nectin-1 was presented as the entry receptor for all three alphaherpesviruses; it is the herpes simplex receptor, so the sentence now reads "an entry receptor (nectin-1 for herpes simplex)".

## Teaching quality and structure
- IN-12.8: the 296-word single paragraph covering four organisms was split into three paragraphs (Borrelia; Rickettsia rickettsii; Leishmania and cutaneous larva migrans) to meet the 2 to 5 sentence paragraph rule. No content added.
- Checked every other fact, number, mechanism, table cell, flow step, worked example and STOP prompt in all eight sections against standard reference consensus and confirmed them: coagulase and staphylothrombin, protein A and IgG Fc, Panton-Valentine leukocidin, exfoliative toxin cleavage of desmoglein 1, TSST-1 superantigen bridging, mecA and PBP2a versus penicillinase, M protein binding factor H, hyaluronic acid capsule, streptokinase, streptolysin O versus S, pyrogenic exotoxins, the 1 to 3 week and 3 to 6 week latent intervals, dermatophyte keratinases and the genus by tissue table, Malassezia lipid dependence and azelaic acid inhibition of tyrosinase, Candida germ tube and dectin-1 to CARD9 to Th17 axis, HPV genome size and E6 to E6AP to p53 and E7 to Rb to E2F, molluscum cytoplasmic replication and Henderson-Patterson bodies, retrograde dynein transport and latency-associated transcripts, sites of latency for HSV-1, HSV-2 and varicella zoster, 5-alpha-reductase and the microcomedone, TLR2 to NLRP3 cytokine release, Pseudomonas oxidase and pigments and the hot tub exposure window, Ixodes attachment time and OspC switch, Rickettsia endothelial infection with acral onset, Leishmania amastigotes in macrophages, and hookworm larvae trapped above the basement membrane. No further errors found, nothing removed as unconfirmable.
- Confirmed every term in the overview is defined before use, each STOP prompt is answerable from its own section, and each "check" line points to the correct paragraph or table.

## Scope and writing rules
- Confirmed Part I scope throughout: no treatment or management content. Drugs appear only mechanistically (beta-lactam acylation of penicillin-binding proteins, nafcillin steric hindrance, glucocorticoid and antibiotic effects as predisposing changes to host defense).
- No em or en dashes, no italics, no banned phrases; prose reads as connected professional sentences.

## Sources
- Removed the Lippincott Illustrated Reviews: Biochemistry entry ("keratin and disulfide cross-linking"), which is not a section of that book; five verified sources remain, within the 3 to 6 rule.
- Jawetz "where" field corrected to real chapter names: The Staphylococci; The Streptococci; Medical Mycology; Herpesviruses; Papillomaviruses; Poxviruses; Rickettsia and related genera; Spirochetes.

## Items moved to verify
- None. The ten existing verify entries were each checked and are honest and correctly scoped (nasal carriage range, superantigen T cell fraction, dermatophyte tissue exceptions, tinea versicolor pigment mechanisms, the skin versus throat rheumatic fever model, Ixodes attachment and erythema migrans intervals, hot tub folliculitis onset, candidalysin and CARD9 currency, the Cutibacterium versus Propionibacterium naming, and the two requested diagram names). Nothing in the chapter needed to be downgraded into the list.

## Length and checker
- Prose 3,399 words (limit about 3,500), per competency 431, 445, 415, 378, 448, 452, 439, 392. Chapter was not lengthened: net change is about plus 20 words of corrected wording, offset by the removed source entry.
- `python3 tools/check_notes.py notes/chapters/IN-12.json`: 0 errors, 0 warnings.
