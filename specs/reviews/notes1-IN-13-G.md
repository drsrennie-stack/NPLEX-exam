# Reviewer log: notes/chapters/IN-13-G.json (Malignant Skin Neoplasms)

Reviewed line by line against Robbins and Cotran, Lange Pathophysiology of Disease, Abbas, Junqueira, and First Aid level consensus. All six competencies in notes/registry/identifiers.json (NPLEX-P1-INTG-13-07-C01 to C06) were checked against their registry text; each is taught completely, so no section needed expansion.

## Facts corrected
- C04 somatic drivers: "most of the rest carry NRAS mutations" was an overstatement (TCGA and comparable series put BRAF at about half, NRAS at about a quarter, with NF1 and triple wild type making up the remainder). Changed to "roughly another quarter carry NRAS mutations".
- C01: "PTCH1 encodes a receptor whose job is inhibitory" was imprecise about what PTCH1 binds. Changed to "encodes the hedgehog receptor, and its signaling role is inhibitory".
- C01: "the lesion does not occur on true mucosa or on palms and soles" was absolute; rare palmoplantar cases are reported. Softened to "is essentially never seen on".
- Sources: Abbas "where" field changed from "T cell migration and tissue homing" to "leukocyte circulation and migration into tissues", which is the actual chapter name.

## Scope (Part I, no treatment or management)
- C05: "a melanoma confined to this phase is cured by complete excision" rewritten to "has not yet left its site of origin" (biology, not management).
- C05 worked example: "so complete excision is very likely curative" rewritten to "so the tumor is almost certainly still confined to the site of origin".
- Sentinel nodal basin sampling retained: it is diagnostic staging, not treatment.

## Verify list
- Moved to verify / expanded: the BRAF entry now also carries the NRAS share (about 20 to 30 percent) so both quoted proportions are flagged as source-dependent.
- Remaining eleven verify entries checked for honesty and kept: basal cell and squamous cell metastatic rates, transplant squamous cell carcinoma risk multiple, AJCC thickness cutoffs including the 0.8 mm T1 subdivision, mitotic rate status in AJCC eighth edition, Sezary cell numeric threshold, keratoacanthoma classification, cutaneous horn malignancy proportion, eponym expectations, requested new diagram names, and the family history and ABCDE diameter figures.

## Length
- Prose held at about 2,730 words across six competencies (250 to 450 per competency excluding worked examples), well under the 3,500 word ceiling. Nothing lengthened.
- Trimmed C05 by ten words (ocular micrometer clause, redundant "epidermal environment", "considerably") to clear the section length warning my scope rewrites introduced.

## Checked and found correct, no change made
- Hedgehog mechanism and flow figure, Gorlin syndrome features, nodular and morpheaform morphology, peripheral palisading and retraction clefts, stroma dependence as the reason metastasis is exceptional.
- UVB wavelength range, cyclobutane pyrimidine dimers, C to T and CC to TT signature, nucleotide excision repair, TP53 early then NOTCH and CDKN2A, xeroderma pigmentosum, transplant immunosuppression reversing the squamous to basal ratio, beta and mucosal HPV with E6 on p53 and E7 on Rb, arsenic, Marjolin ulcer, lower lip site reasoning.
- Keratin pearls, intercellular bridges as desmosomes, Bowen disease and erythroplasia of Queyrat, keratoacanthoma architecture and tempo, squamous metastatic risk factors including size over about 2 cm and depth over about 2 mm, lymphatic then hematogenous spread.
- Melanoma intermittent intense exposure, pheomelanin phenotype, dysplastic nevi as risk markers, CDKN2A and p16, acral and mucosal KIT enrichment, subtype table, ABCDE with evolution weighted highest, subungual pigment onto the cuticle, amelanotic presentation.
- Radial to vertical growth, E-cadherin to N-cadherin switch, dermal lymphatics, Breslow measurement landmarks and ulcer base rule, ulceration and mitotic rate as prognostic, Clark level reproducibility, S-100 sensitivity against HMB-45, Melan-A and SOX10 specificity with their stated limitations.
- Mycosis fungoides CD4 memory phenotype with cutaneous lymphocyte antigen, CCR4 and CCR10, sun-protected patch distribution, Pautrier microabscesses without spongiosis, CD7 and CD26 loss, T cell receptor clonality, Sezary syndrome criteria and the erythroderma physiology (insensible water and heat loss, shivering, high output failure, hypoalbuminemia, Staphylococcus aureus sepsis).

## Writing rules and structure
- No em or en dashes, no italics, no markdown emphasis, no banned phrases: verified by search over the whole file.
- Overview within limits: intro 105 words, 5 prerequisites, 5 connections, 12 terms, all terms defined before use.
- Two STOP prompts, both answerable from their own section with a correct "check" pointer. Two worked examples, 124 and 108 words. Four flow figures plus five tables, all steps at most 11 words and all readable in grayscale. Summary 10 lines. Sources 5 entries, all from the allowed books.
- `python3 tools/check_notes.py notes/chapters/IN-13-G.json`: 0 errors, 0 warnings.
