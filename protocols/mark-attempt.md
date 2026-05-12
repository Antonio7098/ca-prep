# Protocol: Mark A Study Attempt

Use this when an LLM is asked to mark an attempt file.

## Inputs

- Module notes: `modules/<module>/study-notes.md`
- Base question sheet: `modules/<module>/questions/<sheet>/base.md`
- Attempt file: `modules/<module>/questions/<sheet>/attempts/attempt-N.md`

## Required Process

1. Read the module notes first. Treat them as the marking source of truth unless the user provides newer source material.
2. Read the base sheet to understand the intended scope of each question.
3. Read the attempt and mark each answer independently.
4. For each question, edit only the feedback and marks block unless the user explicitly asks for model answers.
5. Award marks out of 5 using the rubric below.
6. Be strict about enterprise relevance, not just generic AI knowledge.
7. Run `python3 scripts/summarise_attempt_marks.py <attempt-file>` after marking to update the total result.

## Marking Rubric

- 5/5: Accurate, complete, specific, and commercially/operationally relevant.
- 4/5: Mostly correct with one meaningful omission or weak example.
- 3/5: Partially correct but generic, incomplete, or missing enterprise implications.
- 2/5: Some relevant ideas but important misconceptions or major omissions.
- 1/5: Minimal correct content.
- 0/5: Incorrect, blank, or not answering the question.

## Feedback Style

- Start with the strongest useful observation.
- Name the missing concepts directly.
- Prefer concise correction over long explanation.
- When useful, mention how to phrase the answer in an HSBC or regulated-enterprise context.
- Do not rewrite the learner's answer unless requested.

## Output Contract

The attempt file should retain this repeated structure:

````markdown
### N. Question text?

```markdown
Learner answer.
```

**Feedback:**
> Concise feedback.

**Marks: X/5**
````
