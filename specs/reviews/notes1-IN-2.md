# Review log: notes/chapters/IN-2.json (Phase 1 comprehensive notes)

Reviewer pass. Checked every fact, number, mechanism, table cell, flow step, and worked example against Langman, Moore, Junqueira, Robbins, Lippincott Biochemistry, and First Aid-level consensus. Competency text read from notes/registry/identifiers.json (NPLEX-P1-INTG-02-01-C01 through C05).

## Accuracy corrections
- C01 table, neural crest row: "pia and arachnoid" narrowed to "pia and arachnoid over the forebrain"; lineage studies restrict the crest contribution to the forebrain leptomeninges, with the remainder mesodermal.
- C02 table, cranial crest row: same narrowing applied for consistency.
- C04, port-wine stain: added "unilateral" to the V1 Sturge-Weber association, since the risk attaches to a unilateral segmental stain, not to any pink patch in that area.
- C04, port-wine stain: added nevus simplex (faint midline glabella, eyelid, or nape patch that fades) as the common mimic, so the section does not teach that any forehead or eyelid pink patch raises Sturge-Weber concern.
- C04 STOP prompt stem rewritten to describe a unilateral red patch over one side of the forehead and upper eyelid, matching the corrected text; the prompt remains answerable from the section and the check line still points to the right table.
- C03 timeline table: lanugo row now notes that the first hairs appear on brow and upper lip near the end of month 3, before body lanugo at about weeks 17 to 20; previously the earliest facial hair was omitted.
- C03, lanugo sentence: "shed late in gestation, some into the amniotic fluid where they are swallowed" simplified to shedding into amniotic fluid, removing an unsourced detail about swallowing.
- Summary line 2: "skin and mammary glands" corrected to "cutaneous and mammary glands" (the original read as if skin itself were a gland).

## Clarity and terminology
- C01 flow step "Border cells undergo EMT and leave as neural crest" rewritten without the abbreviation EMT, which was never introduced in the prose.
- C01 table, neural crest row: stray cross-reference "(C02)" after "thyroid C cells" removed; it read as part of the cell name.
- C05 opening sentence rewritten so each of the three mechanisms is named with its disorder in place, instead of the first, third, second ordering the reader had to decode.
- C02: removed the filler opener "Origin has practical consequences."
- C01: removed "and these are favorite exam items" from the adjacent-structures paragraph.

## Scope
- No treatment or management content found; nothing removed on scope grounds. Drug content: none present.

## Length control
- Chapter was 4,196 words before review and is 4,199 after, so the corrections were offset by cutting duplication rather than by adding length.
- C04 crossed the 650-word section ceiling after the nevus simplex correction; the three-lesion paragraph, the Tyndall paragraph, and the ancestry sentence were tightened to bring it back under without losing any fact.
- C02 worked example and C03 epidermal stratification paragraph trimmed of sentences that restated the adjacent tables.

## Items added to verify
- Added one entry recording that review-level sources list pia and arachnoid as neural crest without qualification while lineage studies restrict it to the forebrain, and that the restricted wording is used here.
- Existing verify entries retained and confirmed honest: fetal skin timings varying between texts, crest dermis described as face versus face and neck, the questioned neural crest origin of thyroid C cells, qualitative handling of dermal melanocytosis prevalence and fade age, unstated week of first fetal melanin production, and the request for a neural-crest-routes diagram name.

## Facts verified without change
BMP inhibition by noggin, chordin, and follistatin around day 18 to 19; neural fold fusion beginning in the cervical region; crest border transcription factors SNAI2, SOX10, PAX3; rostral sclerotome ventral route and dorsolateral melanoblast route; regional dermal origins (cranial crest, somite dermatome, lateral plate); craniopharyngioma from Rathke pouch remnants; enamel from surface ectoderm and dentin from crest odontoblasts; microglia from yolk sac precursors; EDA in X-linked hypohidrotic ectodermal dysplasia; mammary ridge and polythelia; definitive four-layer epidermis by about the end of month 4 and stratum corneum barrier at about 32 to 34 weeks; dermal papilla induction of the hair shaft, sebaceous bud, bulge, and arrector pili attachment; vernix composition and function; spindle-shaped deep reticular dermal melanocytes and the Tyndall explanation of blue-gray color; bruise versus patch distinction; GLUT1-positive infantile hemangioma versus GNAQ capillary malformation; KIT and stem cell factor in melanoblast survival and migration; autosomal dominant piebaldism with ventral and mid-limb patches sparing back, hands, and feet; autosomal recessive oculocutaneous albinism with normal melanocyte numbers, tyrosinase in type 1, OCA2 P protein in other types; tyrosine to DOPA to dopaquinone pathway; foveal hypoplasia, chiasmal misrouting, nystagmus, iris transillumination, and squamous cell carcinoma risk in albinism; Waardenburg genes PAX3, MITF, SOX10 with heterochromia and deafness from crest-derived iris stromal and stria vascularis melanocytes; SOX10 and EDNRB linking pigment loss, deafness, and Hirschsprung disease; phenylketonuria hypopigmentation.

## Checker
`python3 tools/check_notes.py notes/chapters/IN-2.json`: 5 sections, 4,199 words, 11 figures and tables, 0 errors, 0 warnings.
