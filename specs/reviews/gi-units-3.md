Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 1, facts corrected 1, videos removed 0.

# Review log: content/gi/units-3.json

Units reviewed: GI-13-A, GI-13-B, GI-13-C, GI-13-D, GI-13-E, GI-13-F.

## Changes

- GI-13-C, notes "Cirrhosis: findings from liver failure", coagulopathy bullet: ungrammatical ("less factors") and left out factor V, which falls in liver failure and helps separate it from vitamin K deficiency. Rewritten as "Coagulopathy: the liver makes fewer clotting factors (II, V, VII, IX, X), so PT and INR rise and vitamin K does not correct them."
- GI-13-D, trick "Add one finding, change one diagnosis": the logic did not hold (it said cholecystitis plus jaundice is a duct stone, then added fever to reach cholangitis although fever was already present). Rewritten so each step is correct: colic under 6 hours with normal labs, cholecystitis over 6 hours with fever and leukocytosis, jaundice for a common bile duct stone, and fever with jaundice and right upper quadrant pain for cholangitis.

## Checked and left unchanged

- All notes, charts, high-yield lines, pitfalls, and brain dump key points in all six units were checked against standard references. No other errors found.
- Mnemonics: "POM-POMs" (mumps, First Aid), "I GET SMASHED" (pancreatitis), and "4 Fs" (cholesterol gallstones) are established and correctly expanded. All other aids are already marked "trick".
- References: all books are on the SPEC list and every "where" is a known chapter title or a plain section name. No chapter or page numbers.
- Coverage: every objective in GI-13-A.1 to A.2, B.1 to B.4, C.1 to C.11, D.1 to D.5, E.1 to E.6, and F.1 to F.7 is taught in the notes, charts, or high-yield lines.
- Videos: all 17 links were checked with YouTube oEmbed. Each returned successfully, with the stated channel (Ninja Nerd, Armando Hasudungan, Dr. Najeeb Lectures, or khanacademymedicine for Khan Academy Medicine) and a title that matches the stored one exactly. None removed and no titles changed.

## Checker

python3 tools/check_content.py content/gi/units-3.json: 0 errors, 0 warnings.
