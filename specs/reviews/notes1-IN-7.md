# Reviewer log: notes/chapters/IN-7.json (Skin Genetics)

Independent review against Robbins, Lippincott Biochemistry, Junqueira, Lange Pathophysiology of Disease, and First Aid level consensus. Competency text read from notes/registry/identifiers.json (C01 to C07, objectives IN-7.1 to IN-7.7).

## Facts corrected
- C01: UV damage response attributed to "the kinases ATR and ATM" without weighting. Corrected to chiefly ATR (replication fork and transcription stalling), with ATM contributing when breaks form.
- C02: NER flow step said only that XPG cuts "on one side" and XPF with ERCC1 "on the other". Specified the polarity: XPG cuts 3 prime, XPF with ERCC1 cuts 5 prime.
- C02: repair pathway table listed ataxia-telangiectasia as the representative disease of nonhomologous end joining failure. A-T is a defect of ATM damage signaling, not of end joining. Replaced with DNA ligase IV and Artemis deficiency (radiosensitive immunodeficiency) and stated the A-T distinction in the same cell.
- C02: "Every sun exposure leaves dimers that persist in every cell of the epidermis" overstated the defect. Changed to dimers persisting in epidermal cells instead of being excised.
- C02: albinism contrast said skin cancer risk rises "moderately". Corrected to severe burning with squamous cell carcinoma common in sun-exposed skin, the distinction being adult rather than childhood onset.
- C02: XP variant description now names POLH as the gene for polymerase eta and states that it copies past a dimer with relatively few errors rather than "accurately".
- C02: table cell wording for antigen receptor gene rearrangement made specific (was "receptor gene rearrangement").

## Verified without change (spot list)
- G1 to S switch: cyclin D with CDK4 and CDK6, Rb and E2F, cyclin E with CDK2, p16, p53 to p21, BAX and PUMA, sunburn cells.
- UV signature chemistry: cyclobutane dimer, accelerated cytosine deamination, C to T and CC to TT; TP53 as earliest driver in sun-damaged epidermis; later CDKN2A, NOTCH1, RAS in cSCC.
- NER two modes (XPC global genome, CSA and CSB transcription coupled), TFIIH with XPB and XPD, XPA verification, 25 to 30 nucleotide patch; XPA and XPD neurologic groups.
- Hedgehog: PTCH1 inhibits Smoothened, SUFU holds GLI, activating SMO minority; Gorlin features including odontogenic keratocysts, palmar and plantar pits, falx calcification, medulloblastoma.
- Melanocytic drivers: BRAF V600E with oncogene-induced senescence through p16, CDKN2A escape, TERT promoter, PTEN and TP53 late; NRAS in large congenital nevi and mutual exclusivity with BRAF; KIT in acral and mucosal melanoma; CDKN2A encoding p16 and p14ARF with pancreatic adenocarcinoma risk; CDK4 R24 type families.
- Pedigree reasoning and every cell of the recurrence risk table; the 2 in 3 carrier figure; worked example arithmetic (2/3 x 1/300 x 1/4, about 1 in 1,800).
- NF1 on chromosome 17, neurofibromin as RAS GAP, café-au-lait size thresholds (over 5 mm prepubertal, over 15 mm postpubertal), axillary and inguinal freckling, Lisch nodules, plexiform risk of MPNST, pheochromocytoma and renal artery stenosis.
- TSC1 hamartin and TSC2 tuberin, tuberin as Rheb GAP, mTORC1 and cell size explaining hamartoma rather than carcinoma; ash-leaf macules, angiofibromas, shagreen patch, periungual fibromas, cortical tubers with infantile spasms, SEGA, cardiac rhabdomyoma, angiomyolipoma, lymphangioleiomyomatosis, retinal astrocytic hamartoma.
- FLG on chromosome 1, profilaggrin in keratohyalin granules, NMF with pyrrolidone carboxylic acid and urocanic acid, surface pH, semidominant inheritance, reduced granular layer, IL-4 and IL-13 suppression of filaggrin.
- STS on the short arm of the X, cholesterol sulfate retention hyperkeratosis, corneal opacities in males and carrier mothers, cryptorchidism, placental route from DHEAS to estriol with low maternal estriol, contiguous gene deletion syndromes.
- Melanin switch: dopaquinone branch point, cysteine and glutathione to cysteinyldopa and pheomelanin, MC1R through Gs, cAMP, PKA, CREB, MITF, tyrosinase, TYRP1 and dopachrome tautomerase, keratinocyte POMC induced by p53, agouti signaling protein antagonism; three-mechanism melanoma risk in variant carriers; OCA1 versus MC1R variant versus vitiligo in the worked example.

## Teaching quality and writing
- C03 opening replaced a vague metaphor ("held open by a specific stuck signal") with a literal statement that one pathway is stuck in the on position.
- C06 opening restated the two requirements of the stratum corneum literally (internal rigidity, cohesion until surface enzymes release the cells) and defined ichthyosis as persistent visible scale.
- C05 and C06 each had paragraphs running well past the 2 to 5 sentence rule. Split the NF1 paragraph, the tuberous sclerosis paragraph, and the X-linked ichthyosis paragraph into two each. No content removed.
- Trimmed redundant wording in C02 and C06 (clinical sequence sentence, mutation-rate sentence, contiguous deletion sentence) so both sections stay inside the per-section word limit after the corrections above.

## Scope, STOP prompts, sources
- Scope: no treatment or management content present or added. Drugs appear nowhere; Wood lamp examination is a diagnostic observation, not management, and is retained.
- Both STOP prompts are answerable from their own sections and their check lines point to the right table or paragraph. Verified the X-linked STOP answer against the recurrence risk table.
- Sources: six entries, all from allowed books, named by chapter or plain section name. No invented chapter numbers or page numbers. Left unchanged.
- No em or en dashes, no italics, no banned phrases. Byline and brand present.

## Items moved to or added in verify
- Added: the ultraviolet B waveband convention (290 to 320 nm in dermatology and pathology texts versus 280 to 315 nm in photobiology), since the chapter states the former.
- Retained all nine existing verify entries, including the four requested diagram names, after confirming each is genuinely source-variable rather than a fixable error.

## Checker
`python3 tools/check_notes.py notes/chapters/IN-7.json` gives 7 sections, 6,132 words counted (2,954 words of prose), 12 figures and tables, 0 errors, 0 warnings. Chapter length is unchanged in substance; the two length warnings introduced by the corrections were cleared by trimming redundancy rather than by removing teaching.
