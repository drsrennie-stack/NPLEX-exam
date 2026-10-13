Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 9, videos removed 0.

# Review log: content/gi/units-2.json (GI-7 to GI-12)

I reviewed all 6 units: every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, reference, and video. I also checked coverage against every objective in nplex-competencies.js.

## Changes

| Unit | What was wrong | Change |
|---|---|---|
| GI-7 | The osmotic gap cutoff for osmotic diarrhea was given as only "above about 100". Standard references use 100 to 125 (often 125). | Note and chart now say "above about 100 to 125" (mOsm/kg in the chart) |
| GI-8 | Vitamin A toxicity was called "idiopathic intracranial hypertension". When vitamin A causes it, it is not idiopathic. | Now "raised intracranial pressure (pseudotumor cerebri)" |
| GI-8 | Lippincott ref "Vitamins": recent editions title it "Micronutrients: Vitamins", so the exact title was uncertain | Now "Section on vitamins" |
| GI-9 | Said urobilinogen "reaches the urine as urobilin". Urobilinogen is what gets excreted, and it oxidizes to urobilin in the urine. | Bullet now states the excretion and oxidation steps correctly |
| GI-10 | Called CFTR a "cAMP-gated" Cl- channel. CFTR is ATP-gated and is opened by cAMP through PKA phosphorylation. | Now "a Cl- channel opened by cAMP and protein kinase A" |
| GI-11 | Listed IL-23 as a Th17 product. IL-23 sustains Th17 cells; it is not made by them. | Now "Th17 (IL-17, sustained by IL-23)" |
| GI-11 | Robbins ref "The Gastrointestinal Tract": the 10th edition titles it "Gastrointestinal Tract", so the exact title was uncertain | Now "Section on the gastrointestinal tract" |
| GI-12 | Pitfall said "Shigella" makes Shiga-type toxin. Shiga toxin comes from S. dysenteriae type 1, not from most Shigella species. | Now "Shigella dysenteriae and EHEC both make Shiga or Shiga-like toxin" |

The GI-7 cutoff fix touched two places (note and chart), which is why the counts show 9 facts corrected across 8 rows.

## Checked and kept

- Mnemonics marked "mnemonic" (Iron Fist, Bro; PVT TIM HaLL; Kwashiorkor protein-poor MEAL; 3 Ds of pellagra; The vowels hit your bowels) are all standard First Aid mnemonics and are expanded correctly. All other memory aids are already marked "trick".
- Coverage: notes, charts, and high-yield lines teach every objective in GI-7.1 to 7.6, GI-8.1 to 8.7, GI-9.1 to 9.7, GI-10.1 to 10.6, GI-11.1 to 11.7, and GI-12.1 to 12.7. Nothing was added.
- References: these chapter titles were kept as real recent-edition titles: Guyton "Digestion and Absorption in the Gastrointestinal Tract" and "Secretory Functions of the Alimentary Tract"; Robbins "Liver and Gallbladder", "Genetic Disorders", and "Environmental and Nutritional Diseases"; Jawetz "Hepatitis Viruses". The others are plain section names. There are no chapter or page numbers.
- Videos: all 21 were re-checked through YouTube oEmbed with WebFetch. Curl to YouTube was blocked by the proxy, so WebFetch was used. Every video returned the stated channel (Ninja Nerd or Armando Hasudungan) and a title identical to the one in the file. None were removed and no titles changed.
- Temperatures are in Celsius with Fahrenheit (42 °C (107.6 °F)). The file has no en or em dashes, no italics, and no banned phrases.
- Checker: 0 errors, 0 warnings.
