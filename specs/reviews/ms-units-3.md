Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 6, videos removed 0.

# Review log: content/ms/units-3.json (MS-13-C to MS-13-H)

Reviewer read specs/SPEC.md and specs/REVIEW.md, then checked every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, reference, and video in all six units, and checked coverage against every objective in nplex-competencies.js.

## Changes

| Unit | Field | What was wrong | Change |
|---|---|---|---|
| MS-13-C | chart "Lab patterns in bone disease", Osteopetrosis PTH | Said "Normal" while the calcium cell says calcium can be low in the infantile form; PTH rises appropriately when calcium is low, so the row was internally inconsistent. | Now "Usually normal (can rise if calcium is low)". |
| MS-13-C | chart "Osteopetrosis forms", Example genes (infantile column) | Placed carbonic anhydrase II deficiency under the infantile malignant form without qualification; CA II deficiency is autosomal recessive but an intermediate, milder form. | Now "carbonic anhydrase II in a milder recessive variant with renal tubular acidosis". |
| MS-13-D | notes "Duchenne and Becker", bullet 2 | Said only frameshift deletions cause absent dystrophin; nonsense mutations are also a common cause. | Now "frameshift deletions or nonsense mutations give absent dystrophin". |
| MS-13-D | chart, Duchenne "Gene and protein" | Same omission. | Now "DMD, dystrophin absent (frameshift or nonsense)". |
| MS-13-F | dump "Sarcoma marker table", chondrosarcoma key point | Prompt asks where each tumor spreads; the chondrosarcoma key point gave no spread site. | Added "lung" (hematogenous spread to lung). |
| MS-13-H | notes "Compartment syndrome", bullet 5 | "Clawed wrist and fingers" misdescribes Volkmann contracture; the wrist is flexed and the fingers are clawed. | Now "fibrosed forearm flexors, flexed wrist, and clawed fingers". |

## Checked and kept (no change needed)

- Coverage: every objective in MS-13-C (.1 to .4), MS-13-D (.1 to .8), MS-13-E (.1 to .11), MS-13-F (.1 to .11), MS-13-G (.1 to .8), and MS-13-H (.1 to .6) is taught in the notes, charts, or high-yield lines.
- Mnemonics marked "mnemonic" are established First Aid-level aids, correctly expanded: Patients can't BITE (osteogenesis imperfecta), LOSS (osteoarthritis x-ray), CASTS Bend LEGS (avascular necrosis), the 6 Ps (acute limb ischemia and compartment syndrome). All original aids are marked "trick" and are correct.
- Facts confirmed against Robbins and First Aid consensus: osteopetrosis genes (CA2, CLCN7, TCIRG1) and complications; bone lab table; renal osteodystrophy chain including FGF23 and tertiary hyperparathyroidism; FBN1 on chromosome 15 and TGF-beta; lens dislocation directions; DMD CK range; Becker in-frame deletions; OI glycine substitutions and dominant-negative effect; EDS collagen types; FGFR3 and paternal age; OA, osteoporosis T-score cutoffs, Paget phases and complications; pediatric hip and adolescent knee disorders; L4 to L5 disc and L5 root; bone tumor sites, markers, translocations, and IDH1/2; metastasis patterns; synovial fluid cutoffs and crystals; osteomyelitis organisms and x-ray lag; necrotizing fasciitis types; gangrene types and C. perfringens alpha toxin; trichinellosis; fracture healing stages; scaphoid, femoral neck, supracondylar, and fat embolism complications; rhabdomyolysis labs; myositis ossificans zoning.
- References: all books are on the SPEC list; "where" entries are real chapter titles in recent editions (Robbins and Cotran "Bones, Joints, and Soft Tissue Tumors", "Peripheral Nerves and Skeletal Muscles", "Neoplasia", "Cell Injury, Cell Death, and Adaptations"; Robbins Basic Pathology "Genetic and Pediatric Diseases", "Bones, Joints, and Soft Tissue Tumors"; Guyton and Hall "Parathyroid Hormone, Calcitonin, Calcium and Phosphate Metabolism, Vitamin D, Bone, and Teeth"; Lippincott Biochemistry "Fibrous Proteins"; Jawetz "The Staphylococci"; Moore "Lower Limb", "Back", "Upper Limb"; Junqueira "Bone") or plain section names. No chapter or page numbers.
- Videos: all nine links re-verified by YouTube oEmbed on 2026-10-12. Each returned successfully with the stated channel and an exact title match, so none were removed or retitled:
  - MS-13-C: Ninja Nerd "Calcium Disorders | Clinical Medicine", "Parathyroid Disorders | Clinical Medicine", "Chronic Kidney Disease (CKD) | Clinical Medicine"
  - MS-13-D: Armando Hasudungan "Muscular Dystrophy - Duchenne, Becker and Mytonic" (the misspelling is the channel's own title)
  - MS-13-E: Armando Hasudungan "Osteoporosis (Part I)", "Paget's Disease of the bone"
  - MS-13-G: Armando Hasudungan "Septic Arthritis - Overview (causes, pathophysiology, treatment)", "Bone Fracture - Types, Fracture Repair and Osteomyelitis"
  - MS-13-H: Armando Hasudungan "Bone Fracture - Types, Fracture Repair and Osteomyelitis", "Acute Compartment Syndrome"
  - MS-13-F: videos list is empty and was left empty for the later pass.
- Writing rules: no em or en dashes, no italics or markdown emphasis, plain student language.

## Checker

`python3 tools/check_content.py content/ms/units-3.json`: 6 study units, 0 errors, 0 warnings.
