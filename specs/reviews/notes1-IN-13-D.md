# Review log: notes/chapters/IN-13-D.json (Blistering Diseases)

Reviewer pass, Phase 1. Checked against Robbins, Junqueira, Abbas, Lange Pathophysiology of Disease, Boron and Boulpaep, and First Aid level consensus.

## Changes made
- Overview term "Nikolsky sign": removed "indicating an intraepidermal split", which contradicted the later (correct) statement that the sign is positive in staphylococcal scalded skin syndrome and in toxic epidermal necrolysis; replaced with loss of cohesion in skin that still looks intact.
- Section IN-13-D.2: deleted the unsupported causal claim that simplex disease improves "as skin thickens"; now states that localized disease in particular tends to become less troublesome after childhood.
- Section IN-13-D.2: corrected "albinotic papules" in dominant dystrophic epidermolysis bullosa to albopapuloid lesions, with a plain description (pale firm papules over the trunk).
- Section IN-13-D.3, pemphigoid cycle step: "C3a and C5a recruit eosinophils, neutrophils, and mast cells" was mechanistically wrong for mast cells, which are resident and degranulate rather than being recruited; changed to C5a and mast cell degranulation recruiting eosinophils and neutrophils.
- Section IN-13-D.3: removed the invented explanation that mucous membrane pemphigoid scars "because the plane of separation there carries greater dermal injury"; replaced with fibrosis of the mucosal lamina propria at the same split level.
- Section IN-13-D.4: softened "Most patients carry HLA-DRB1*04:02 or DQB1*05:03" to a disease association, since allele frequency is population dependent (matching the existing verify entry).
- Section IN-13-D.6: replaced "essentially all patients have some degree of gluten-sensitive enteropathy" with the actual range of biopsy findings, from increased intraepithelial lymphocytes to villous atrophy, since texts differ on the proportion with frank atrophy.
- Integration: reworded "it answers to removing a dietary antigen" so the point stays biomedical (deposits depend on continued dietary antigen exposure) rather than reading as management, keeping the chapter inside Part I scope.
- verify: added an entry on the disagreement between texts over the proportion of dermatitis herpetiformis patients with villous atrophy.

## Verified as correct, no change
- Adhesion architecture: desmoglein 1 and 3 with plakoglobin, plakophilin, desmoplakin and keratins; hemidesmosome on integrin alpha-6 beta-4 with BP180 (collagen XVII) and BP230; laminin 332 in the lamina lucida; type IV collagen in the lamina densa; type VII collagen anchoring fibrils.
- Epidermolysis bullosa table: KRT5 and KRT14 with intrabasal split and dominant inheritance; LAMA3, LAMB3, LAMC2 and COL17A1 with lamina lucida split and recessive inheritance; COL7A1 with sublamina densa split, dominant or recessive.
- Herlitz level junctional disease features (periorificial granulation tissue, airway involvement, enamel defects, infant mortality) and recessive dystrophic features (pseudosyndactyly, milia, esophageal stricture, microstomia, corneal scarring, anemia, cardiomyopathy).
- Recessive dystrophic squamous cell carcinoma: sun-protected sites, young adults, well differentiated yet early metastasis, leading cause of death.
- Bullous pemphigoid: age over about 60, IgG against the BP180 NC16A ectodomain with BP230 intracellular, classical complement activation, eosinophil rich infiltrate, tense bullae with negative Nikolsky sign, urticarial prodrome, linear IgG and C3, epidermal roof labeling on 1 M sodium chloride split skin, no scarring.
- Pemphigoid gestationis and mucous membrane pemphigoid antigens.
- Pemphigus vulgaris: IgG4 against desmoglein 3 with or without desmoglein 1, complement independent, neonatal transplacental disease as proof of pathogenicity, p38 MAPK signaling and desmoglein internalization, suprabasal split with tombstone basal row, Tzanck preparation, oral onset, positive Nikolsky and Asboe-Hansen signs, net-like intercellular IgG, monkey esophagus substrate, paraneoplastic pemphigus with envoplakin and periplakin plus Castleman disease or non-Hodgkin lymphoma.
- Desmoglein compensation as the explanation for mucosal versus superficial blistering; pemphigus foliaceus subcorneal split, seborrheic distribution, no mucosal disease, fogo selvagem.
- Worked example: exfoliative toxins A and B as proteases cleaving desmoglein 1, giving the same plane as pemphigus foliaceus with negative immunofluorescence.
- Dermatitis herpetiformis: HLA-DQ2 and DQ8, deamidated gliadin, IgA against TG2 then TG3, granular IgA in papillary tips, neutrophilic papillary microabscesses, extensor distribution, iodine as a provoking exposure, thyroid autoimmunity and lymphoma risk.
- Subepidermal immunofluorescence table, including LAD-1 as a shed BP180 fragment in linear IgA bullous dermatosis and dermal floor labeling in epidermolysis bullosa acquisita.

## Structure and rules
- Six sections, one per registry competency (NPLEX-P1-INTG-13-04-C01 through C06), in order, objectives IN-13-D.1 through IN-13-D.6; every competency element in the registry text is taught.
- Length unchanged in substance: prose about 2,330 words across six competencies (383, 366, 439, 446, 384, 307) plus 259 words of integration, all inside the 250 to 450 per competency target and well under the 3,500 word ceiling. Edits were substitutions, not additions, apart from one verify line.
- Overview intro 104 words, 5 prerequisites, 5 connections, 12 terms. Nine tables and figures, including five flow or cycle figures. One worked example, three STOP prompts, 10 summary lines, 5 sources, no "diagram" block (two new schematics requested in verify).
- STOP prompts all answerable from their own sections and their "check" lines point to the right table or paragraph.
- No em or en dashes, no italics, no banned phrases. No treatment or management content; the one historical mortality statement is natural history.
- python3 tools/check_notes.py notes/chapters/IN-13-D.json: 0 errors, 0 warnings.
