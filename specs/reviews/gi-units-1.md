Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 8, videos removed 0.

# Review log: content/gi/units-1.json (GI-1 to GI-6)

Reviewer read specs/SPEC.md and specs/REVIEW.md, then checked every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, reference, and video in all six units, and checked coverage against every objective in nplex-competencies.js (GI-1.1 to GI-6.7).

## Changes

| Unit | Field | What was wrong | Change |
|---|---|---|---|
| GI-1 | highYield, annular pancreas and duodenal atresia line | Said both lesions always cause bilious vomiting. Vomiting is bilious only when the block is below the major papilla (the usual case). | Now states the vomiting is bilious when the block lies below the major papilla, as it usually does. |
| GI-1 | pitfalls, foregut boundary line | "The first half of the duodenum" is imprecise; the boundary is the major papilla in the middle of the second part. | Now "the duodenum above the papilla" versus "below it". |
| GI-3 | notes "Intraperitoneal or retroperitoneal", bullet 2 | Listed "the lower rectum" as retroperitoneal; the lower third is below the peritoneum (subperitoneal), and the middle third is the retroperitoneal part. | Now "part of the rectum", matching objective GI-3.2. |
| GI-3 | dumps "Peritoneal status table", rectum key point | "Upper part covered in front" misstated the rectal peritoneal covering. | Now "upper and middle thirds covered in front, lower third below the peritoneum". |
| GI-4 | notes "Tongue innervation", bullet 4 | Atrophy and fasciculations occur only with a lower motor neuron lesion; an upper motor neuron lesion deviates the tongue away from the lesion side without atrophy. | Now specifies a lower motor neuron CN XII lesion. |
| GI-4 | highYield, FAST line | "Looked for first" in the hepatorenal recess is not a fixed rule (FAST view order varies). | Now: in a supine trauma patient, free fluid most often shows up first in the hepatorenal recess. |
| GI-6 | notes "Gastric acid control", intestinal phase bullet | Called the 10% "stimulation" but then described only inhibition, which blurred the phase. | Now: protein in the duodenum releases a little gastrin (the 10%), while acid and fat mainly inhibit acid through secretin, GIP, and nerve reflexes. |
| GI-6 | tricks "Letters match the hormone" | Label claimed the letters match the hormones, but K (GIP) and I (CCK) do not. | Relabeled "Cell letters and their hormones"; text says G, S, M match and K, I need extra practice. |
| GI-6 | highYield, incretin line | Credited the oral glucose effect to GIP alone; GLP-1 is the other main incretin. | Now "gut incretins (GIP and GLP-1)". |

(Nine edits; the GI-3 rectum note and dump point are one fact fixed in two places, giving 8 distinct facts corrected.)

## Checked and kept (no change needed)

- Embryology: week 6 herniation, 270 degree counterclockwise rotation around the SMA (90 in the cord, 180 on return), return by about week 10, tracheoesophageal septum, hepatic diverticulum, dorsal and ventral pancreatic buds, neural crest migration, duodenal recanalization, and all defect associations (Down syndrome, VACTERL, trisomies 13 and 18, Beckwith-Wiedemann).
- Histology: wall layers and plexuses, epithelia, gastric gland cells and products, segment identifiers, lobule and acinus, zone 1 to 3 injury patterns (First Aid consensus), salivary acinus types.
- Gross anatomy: duodenal parts and relations, peritoneal status, liver landmarks, bile path, taeniae and McBurney point, salivary ducts and parasympathetic supply, facial nerve in the parotid.
- Cavities: esophageal course and narrowings, tongue nerves and lingual nerve lesion levels, sacs, omenta, hepatoduodenal ligament layout, ligament contents, inguinal canal, Hesselbach triangle, hernia types, dependent spaces.
- Blood supply: celiac, SMA, IMA levels and branches, watershed zones, portal vein formation, three portosystemic anastomoses, pectinate line comparison, liver blood flow about 75% portal and 25% arterial with about half the oxygen from each, bile duct dependence on the hepatic artery.
- Physiology: slow wave rates (about 3 per minute stomach, about 12 per minute duodenum), MMC about every 90 minutes, parietal cell receptors, phase percentages (about 30, 60, 10, Guyton), hormone chart, digestion and absorption transporters, defecation reflex and incontinence patterns, CTZ receptors, vomiting acid-base and potassium.
- Mnemonics marked "mnemonic" are all well-established (First Aid level): VACTERL, SAD PUCKER, I 8 10 EGGs AT 12, MDs don't LIe. Original aids are marked "trick" and are correct.
- References: all books are on the SPEC list. Chapter titles confirmed in recent editions: Langman "Digestive System"; Robbins "The Gastrointestinal Tract" and "Liver and Gallbladder"; Junqueira "Digestive Tract" and "Organs Associated with the Digestive Tract"; Moore "Abdomen", "Thorax", "Head"; Lange Pathophysiology "Liver Disease"; Guyton "Propulsion and Mixing of Food in the Alimentary Tract", "Secretory Functions of the Alimentary Tract", "Digestion and Absorption in the Gastrointestinal Tract". The Guyton hepatic blood flow entry is a plain section name. No chapter or page numbers.
- Coverage: every objective GI-1.1 to GI-6.7 is taught in the notes, charts, or high-yield lines. Nothing added.

## Videos (all 19 re-verified by YouTube oEmbed via WebFetch)

Every video returned successfully, author_name matched the stated channel (Khan Academy entries return "khanacademymedicine"), and every stored title matched the oEmbed title exactly. None removed, no titles changed.

- GI-1: 4it-uI9e_I8 (Ninja Nerd), PAMaaKocIsk (Ninja Nerd)
- GI-2: 9CTyKLefn9E (Ninja Nerd), QEY_hCx-t4w (Dr. Najeeb Lectures), UgnF1w-H8vw (Khan), nJfB32MtqBA (Khan)
- GI-3: 1-m3z_d531E (Armando Hasudungan), EYZPE5-7vZ8 (Armando), jmfcACEGW-0 (Khan), Lzr9GGjh6YQ (Khan)
- GI-4: BZ0JBiPeek8 (Armando), wU9_daCwr_w (Khan)
- GI-5: CqtQALXskDU (Ninja Nerd), rDjWrNRKfvg (Khan)
- GI-6: NIbclTo3duU (Ninja Nerd), DXPwCphPsmU (Ninja Nerd), Rcb6I7gsl-Y (Armando), pWGhGx_mNXc (Najeeb), nLCNoT79_-o (Khan)

## Checker

python3 tools/check_content.py content/gi/units-1.json: 6 study units, 0 errors, 0 warnings.
