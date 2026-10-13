# Review log: notes/chapters/IN-13-H.json (Infectious Skin Diseases)

Reviewer pass, Phase 1. Checked all 21 competency sections against the registry text in notes/registry/identifiers.json and against Robbins, Jawetz, Abbas, Guyton and Hall, and Lange Pathophysiology of Disease consensus. Chapter was not lengthened: prose fell from 9,430 to about 9,370 words and the checker total from 14,706 to 14,680.

## Facts corrected
- C07 (IN-13-H.7): poststreptococcal glomerulonephritis latency was given as "one to six weeks after impetigo (longer than the one to three weeks after pharyngitis)", which understates the difference; corrected to about three to six weeks after impetigo versus one to two weeks after pharyngitis.
- C05 (IN-13-H.5): erythema nodosum granulomas were placed "around the septal vessels"; corrected to small histiocytic granulomas within the widened septa, which is where they sit.
- C10 (IN-13-H.10): the flat claim that Malassezia "does not digest keratin" was replaced with the confirmable mechanism, that it lacks fatty acid synthase and therefore depends on sebum rather than on keratin.
- C17 (IN-13-H.17): removed the unsupported mechanism "Because the epidermis is injured but not killed" as the explanation for scarlet fever desquamation; the desquamation statement itself was kept.
- C21 (IN-13-H.21): "high nasal and total mite counts" in crusted scabies replaced with "enormous mite counts"; nasal mite counts are not a standard finding.

## Scope corrections (Part I, no treatment or management)
- C03: "treating the fungus is what stops the bacterial recurrences" rewritten as the mechanistic statement that episodes recur while the interdigital fissure stays open.
- C04: abscess paragraph rewritten from antibiotic penetration to the pathophysiology of an avascular, acidic, hypoxic cavity cut off from circulating defenses.
- C06: same change in the cutaneous abscess paragraph, and the table cell "Fluctuance; requires drainage" changed to "Fluctuance; pus sealed off from the blood supply".
- C08: nasal decolonization as an intervention replaced with the nares as the reservoir that sustains recurrent disease.
- C08: penicillinase sentence reworded so the bulky side chain explains enzyme resistance rather than describing drug development.
- C10: removed "where topical agents cannot reach it" as the reason scalp and nail disease differ.
- C11: deleted "on calcineurin inhibitors" from the list of causes of impaired cellular immunity.
- C12: "vaccination status is the first thing established after an exposure" replaced with the mechanistic statement about recipient immunity.
- C21: deleted "why treatment relieves itch slowly".

## Sections expanded
- None. Every registry competency (IN-13-H.1 to IN-13-H.21) already had exactly one section in order, and each covered the full text of its objective, so the pass tightened wording instead of adding content.

## Repetition and wording trimmed (no facts lost)
- C10, C11, C16, C17, C18, C21: redundant modifiers and duplicated clauses removed to bring the longest sections back toward the per-competency target; C10 was brought back under the checker's per-section word ceiling after the edits above.

## Items moved to verify
- None added. The existing six verify entries (needle stick per exposure estimates, impetigo organism frequency, anthrax mortality and cutaneous share, nasal carriage prevalence, whether rheumatic fever can follow skin infection, and the NABNE blueprint question for IN-13-H.15 to IN-13-H.21, plus the request for two new diagram names) are honest and were left as written. Nothing else was unconfirmable; the two shaky claims found were corrected rather than deferred.

## Checked and left unchanged
- Toxin biochemistry (exfoliative toxin and desmoglein 1, alpha toxin lecithinase, tetanospasmin and synaptobrevin, botulinum at cholinergic terminals, protective antigen with edema factor and lethal factor, streptococcal pyrogenic exotoxin as superantigen) verified correct.
- Numbers verified: needle stick risks, HPV type assignments, SJS and TEN surface area cutoffs, roseola and Mycobacterium marinum and Mycobacterium leprae temperatures with correct Celsius to Fahrenheit conversions, scabies mite size, burrow rate, egg number, and mite burden.
- Overview is within limits (109 word intro, 5 prerequisites, 5 connections, 12 terms). Three STOP prompts, two worked examples, ten summary lines, six sources from the allowed books. No em or en dashes, no italics, no banned phrases.

## Note for the writer spec, not an error
The chapter carries eleven flow figures and one cycle figure against a stated guide of two to five. For a 21 competency chapter this reads as one figure per topic rather than excess, and the checker accepts it, so the figures were kept; flag it if the cap is meant to be absolute.

## Checker
`python3 tools/check_notes.py notes/chapters/IN-13-H.json` gives 0 errors, 0 warnings.
