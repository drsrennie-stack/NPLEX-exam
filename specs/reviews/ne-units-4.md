Verdict: board-ready after four precision fixes. Counts: keys changed 0 (study-unit file, no keys), items rewritten 0, facts corrected 4, videos removed 0.

# Review log: content/ne/units-4.json

Reviewed all 6 units (NE-19, NE-20-A, NE-20-B, NE-20-C, NE-20-D, NE-20-E): every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, and reference.

## Changes

- NE-19, mnemonic "Please SHiNE my SKiS": said "Asplenia raises risk from all of them." Overstated (Pseudomonas, for example, is not a classic post-splenectomy organism). Now says asplenia raises the risk of severe infection with encapsulated bacteria, especially S. pneumoniae, Hib, and N. meningitidis.
- NE-20-A, notes (Intracranial hemorrhage): vasospasm after SAH given as "about days 3 to 10". The consensus window is about days 3 to 14 (peak near day 7). Changed to "about days 3 to 14".
- NE-20-A, trick "Front of the cord": "The anterior spinal artery feeds everything except the dorsal columns" was imprecise, since the posterior spinal arteries also supply the back of the dorsal horns. Now says it feeds the front two-thirds of the cord, which is everything except the dorsal columns and the back of the dorsal horns.
- NE-20-B, refs: Abbas chapter title spelled "Immunological Tolerance and Autoimmunity"; the actual chapter title is "Immunologic Tolerance and Autoimmunity". Corrected.

## Checked and left as written

- Coverage: every objective in nplex-competencies.js for NE-19 (.1 to .7), NE-20-A (.1 to .11), NE-20-B (.1 to .13), NE-20-C (.1 to .4), NE-20-D (.1 to .7), and NE-20-E (.1 to .10) is taught in the notes, charts, or high-yield lines. Every listed condition has a row in its unit's core condition chart.
- Mnemonics marked "mnemonic" are established First Aid ones and correctly expanded: SHiNE SKiS, TRAP, SIN (Charcot triad), Wet wobbly wacky (NPH), From low to high your pons will die, Hunters see clearly and aim for the X, I Love Vermont maple syrup, CGG Chin Giant Gonads. Original aids are already marked "trick" and are accurate.
- Facts checked against Robbins, Guyton, Jawetz, Lippincott, and First Aid-level consensus, including: Hib factors X and V; GBS bacitracin resistance; Listeria listeriolysin O and ActA; botulinum and tetanospasmin SNARE targets (tetanospasmin cleaves synaptobrevin) and Renshaw cell inhibition; herpesvirus nuclear envelope; rabies nicotinic receptor binding and dynein transport; Mucor versus Aspergillus hyphae; VDRL false positives; infarct time course (red neurons 12 to 24 hours, neutrophils 1 to 3 days, macrophages from about day 3); CA1, Purkinje, and cortical layers 3, 5, 6 vulnerability; epidural and subdural features; Charcot-Bouchard sites; spinal artery territories; Alzheimer genetics; Huntington paternal anticipation; Friedreich frataxin and cardiomyopathy; GBS albuminocytologic dissociation; edema types; herniation syndromes and Cushing triad; IIH opening pressure above about 25 cm H2O; ammonia and glutamine in astrocytes; aldose reductase and sorbitol; B12 enzymes and subacute combined degeneration; thiamine enzymes; osmotic demyelination at more than about 8 to 10 mEq/L per 24 hours; CMT1A PMP22 duplication; X-ALD, MLD, Krabbe; PKU and maternal PKU; MSUD; OTC deficiency versus UMP synthase deficiency; sphingolipidoses and MPS enzymes and inheritance; AIP; Wilson disease.
- References: all books are on the SPEC list and every "where" is a real chapter title in a recent edition or a plain section name (Jawetz: The Neisseriae, Herpesviruses, Medical Mycology, section on spore-forming gram-positive bacilli; Robbins and Cotran: The Central Nervous System, Peripheral Nerves and Skeletal Muscles; Robbins Basic: Genetic and Pediatric Diseases; Guyton: Cerebral Blood Flow, Cerebrospinal Fluid, and Brain Metabolism; McPhee: Nervous System Disorders; Lippincott and Moore sections). No chapter or page numbers.
- No em or en dashes, italics, or banned phrases.

## Videos

All six units have an empty "videos" array; left empty per REVIEW.md (a later pass adds them).

## Checker

python3 tools/check_content.py content/ne/units-4.json: 0 errors, 0 warnings.
