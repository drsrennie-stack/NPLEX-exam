# Physiology practice workbook template

This is the same active recall format as the NPLEX workbook, set at undergraduate physiology level and built in colour. PHYS-MEMB-1 (membrane potentials and the action potential) is a complete worked example you can copy for any other topic.

## What is in a chapter

Every competency gets two brain dumps. The first asks students to rebuild the foundation from memory. The second asks them to use it on something new, so they cannot pass by recognising words. Each page also carries a confidence rating before checking, three short questions for after they check, and a next retrieval date, because the second pass is where the learning sticks.

Each chapter also carries a comparison table, a prediction exercise, a clinical application on the six step frame (recognize, explain, differentiate, investigate, decide, justify), and two multiple choice questions. Answers live only in the separate key, so a student can work a page without seeing the answer beside it.

## Making a new topic

1. Copy `PHYS-MEMB-1.json` to a new file, for example `PHYS-CARDIO-1.json`.
2. Change `unit`, `chapter_id`, `title`, `subject` and `course` at the top.
3. Give each competency an id in the same shape: `PHYS-UG-<TOPIC>-01-C01`, then `C02` and so on. Activity ids are the competency id plus `-BD1`, `-BD2`, `-RT01`, `-CP01`, `-PR01`, `-CA01`, `-Q01`, `-Q02`. Keep the ids stable once students have used them.
4. Write the activities and a key entry for every one.
5. Build it:

```
cd nplex-part1
THEME=color node tools/wb/build_docx.js workbook/templates/PHYS-CARDIO-1.json
```

That writes `workbook/build/PHYS-CARDIO-1-workbook.docx` and `-key.docx`. Convert to PDF with LibreOffice, or open the DOCX and export.

To bind several topics into one volume for printing:

```
THEME=color node tools/wb/build_docx.js --master PHYS-Workbook "Human Physiology" \
  workbook/templates/PHYS-MEMB-1.json workbook/templates/PHYS-CARDIO-1.json
```

Leave `THEME=color` off and you get the grayscale version, which is cheaper to print in volume.

## Field guide

| Field | What it does |
|---|---|
| `space` | `third`, `half` or `full`. How much writing room the activity wants. The builder fits it to the page so one activity stays on one page. |
| `prompt` | The instruction the student reads. Say exactly what to put on the page. |
| `cols` and `rows` | Comparison table. The header row and the first column print, the rest is blank for the student. |
| `changes` | Prediction exercise. Each line becomes a row with blank columns for direction and reasoning. |
| `stem` and `asks` | Clinical application. One ask per reasoning step. |
| `options` and `answer` | Multiple choice. Options stack vertically, the answer index is 0 to 3 and never prints in the workbook. |
| `key` | One entry per activity: `essentials`, `distinctions`, `misconceptions`, `where`. Questions also take `why_right` and `why_wrong`. |

## Page design

US Letter portrait, one activity per page, open white space with no ruled lines or boxes so students can draw as easily as write, page numbers, and a running header with the chapter name. The colour theme uses the MedMasters palette: deep navy for text, terracotta for activity labels and titles, warm sand for table headers and rules. It prints cleanly in grayscale as well.
