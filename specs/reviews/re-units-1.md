Verdict: board-ready after minor fixes. Keys changed 0, items rewritten 0, facts corrected 5, videos removed 0.

# Review log: content/re/units-1.json (RE-1 to RE-6)

Reviewer read specs/SPEC.md and specs/REVIEW.md, then checked every note bullet, chart cell, trick, high-yield line, pitfall, brain dump key point, and reference in all six units, and checked coverage against every objective in nplex-competencies.js (RE-1.1 to RE-6.7). All six units have empty "videos" arrays, so they were left empty for the later video pass.

## Changes

| Unit | Field | What was wrong | Change |
|---|---|---|---|
| RE-1 | highYield, milk line line | "Always lie along the milk line" overstates it; rare ectopic nipples off the line are reported. | Removed "always". |
| RE-3 | notes "Making gametes", bullet 3 | Said all oogonia become primary oocytes; most oogonia and oocytes degenerate (atresia) before birth. | Now "those that survive become primary oocytes". |
| RE-4 | highYield, round ligament line | Called the round ligament the female counterpart of the spermatic cord; its embryologic counterpart is the gubernaculum. It only occupies the same canal. | Now says it fills the place the spermatic cord takes in the male. |
| RE-5 | pitfalls, erection and emission line | "Mixing them up is the most common error" is an unconfirmable claim. | Removed that sentence; the fact itself is kept. |
| RE-6 | notes "Menstrual cycle", bullet 2 | "Ovulation follows about 1.5 days later" did not say later than what (onset versus peak of the surge differ by about a day). | Now "about 36 hours after the surge begins". |

## Checked and kept (no change needed)

- RE-1: SRY on Yp and testis-determining factor, indifferent gonad until about week 7, Swyer syndrome and 46,XX SRY translocation phenotypes, AMH, testosterone, DHT roles, Wolffian and Mullerian derivatives and remnants (Gartner duct, appendix testis), urogenital sinus derivatives, external genitalia homologs, hypospadias and epispadias, Mullerian fusion defects chart, gubernaculum and processus vaginalis, indirect hernia versus communicating hydrocele, placenta layers and cord vessels, single umbilical artery, mammary ridge. SEED is an established First Aid mnemonic, correctly expanded.
- RE-2: Sertoli and Leydig cell functions and FSH and LH control, blood-testis barrier, heat sensitivity in cryptorchidism, sperm pathway, epididymal epithelium, female tract epithelia and transformation zone, follicle stage chart, two-cell theory, corpus luteum cells, TDLU and myoepithelial layer, fibroadenoma origin, prostate zones and basal cell loss in carcinoma. SEVEN UP is established and correctly expanded.
- RE-3: gamete chart and arrest points, spermiogenesis, capacitation and acrosome reaction, cortical reaction, timeline (morula day 3 to 4, implantation about day 6, hCG detectable about 1 week after fertilization), ectopic and previa risks, bilaminar and trilaminar discs, all-or-none period, weeks 3 to 8 teratogen window, partial mole triploidy. "An egg MET a sperm" is the First Aid mnemonic.
- RE-4: broad ligament parts, pouches and posterior fornix, ligament chart and contents, pelvic floor and prolapse types, scrotal layers and origins, cord contents, breast position (rib 2 to 6, sternal edge to midaxillary line), Cooper ligaments and peau d'orange, penile anatomy and fracture, perineal boundaries and triangles, prostate on rectal exam.
- RE-5: gonadal vessels and left varicocele, uterine artery origin and ureter relation, lymph drainage chart, male sexual response chart (hypogastric T11 to L2, pelvic splanchnic and pudendal S2 to S4), pudendal nerve course and block landmark, breast arteries and lymph. "Point, Squeeze, and Shoot" and "S2, 3, 4 keeps the penis off the floor" are established mnemonics, correctly expanded.
- RE-6: cycle phases and fixed luteal phase, basal body temperature rise 0.3 to 0.5 °C (0.5 to 0.9 °F), NO and cGMP in erection, PDE5 and nitrates, luteal-placental shift, placental lack of 17-alpha-hydroxylase and fetal DHEA-S to estriol path, hPL and gestational diabetes, maternal adaptation numbers (plasma volume 40 to 50 percent, red cell mass 20 to 30 percent, GFR about 50 percent, PaCO2 about 30 mm Hg), hypercoagulability, lactation hormones, Sheehan syndrome, Ferguson reflex.
- References: all Langman, Junqueira, Moore, Robbins Basic Pathology, and Guyton chapter titles confirmed as existing in recent editions or given as plain section names.
- Coverage: every objective RE-1.1 to RE-6.7 is taught in the notes, charts, or high-yield lines. No additions needed.

Checker: python3 tools/check_content.py content/re/units-1.json reports 0 errors, 0 warnings.
