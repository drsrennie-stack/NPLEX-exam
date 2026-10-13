# Extra Case Plan Spec (second pass, the added 1,000 questions)

Read specs/PLAN.md first; every rule there applies, plus these:

1. Your case ids start after the existing ones (you are told the range). Output file: specs/plans/<SYS>-2.json.
2. Priority order for the targets:
   a. Every competency in your system that no question tests yet. Get the list with `python3 tools/coverage.py <SYS>`. All of them must appear.
   b. Then second (or third) questions on high-yield competencies: core disease mechanisms, classic presentations, DOK 3 integration, anything tagged "Both". Count how often each competency is already tested by reading content/<sys>/cases-*.json ("obj" field) and prefer competencies tested only once. Never pick one already tested 3 or more times.
3. Use diagnoses that are NOT already a case diagnosis in this system (read "dx" in content/<sys>/cases-*.json and content/batch1/*.json). A related but distinct presentation is fine (for example a different complication, age group, or etiology of the same condition category), as long as the "dx" text is different and the questions do not repeat facts already tested.
4. Keep the exam-area mix near 20% each across your plan, with at least 3 areas per case.
