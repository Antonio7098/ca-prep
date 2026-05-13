# Protocol: Mark A Study Attempt

Use this when an LLM is asked to mark an attempt file.

## Inputs

- Module notes: `modules/<num>-<module>/<num>-<module>-handbook.md`
- Base question sheet: `modules/<num>-<module>/questions/<num>-<descriptive-sheet-name>/base.md`
- Attempt file: `modules/<num>-<module>/questions/<num>-<descriptive-sheet-name>/attempts/attempt-N.md`
- Learner summary: `LEARNER_SUMMARY.md`

## Required Process

1. Read the module notes first. Treat them as the marking source of truth unless the user provides newer source material.
2. Read the base sheet to understand the intended scope of each question and its **Mark Scheme** (criteria breakdown). Use the mark scheme as the primary reference for what each answer must cover to earn full marks.
3. Read the learner summary to understand the learner's knowledge state, recurring weaknesses, and progress trajectory.
4. Read the attempt and mark each answer independently.
5. For each question, edit only the feedback and marks block unless the user explicitly asks for model answers. The blank attempt contains no **Feedback:** section — you must add it. It also contains a **Total Marks:** line showing the denominator — change it to **Marks: X/N** with the score you award. Do NOT add a **Correction:** section (it is inserted by `ca-prep finalise` from the base sheet answers).
6. Award marks against the Mark Scheme in the base sheet. Each criterion is worth 1 mark; the total equals the denominator shown in **Marks: X/N**.
7. Be strict about enterprise relevance, not just generic AI knowledge.
8. Run `ca-prep finalise <attempt-file>` after marking to update the total result. This automatically appends a row to `LOG.csv` at the project root with the timestamp, module, sheet, attempt number, marks, and percentage.
9. Update `LEARNER_SUMMARY.md` to reflect the new attempt. The overview stats and quantitative progress table are updated automatically by the script — do not edit them manually. You are responsible for the qualitative sections only:
   - Refresh the knowledge state by topic based on the new results.
   - Update recurring weaknesses, learning habits, and growth trend.
   - Bump the "Last updated" date.
10. Commit and push all changes. The commit message must follow this format:

    ```
    mark <module>/<sheet> attempt <N>: <score>/<total> (<percentage>)

    Attempt metadata captured in LOG.csv. LEARNER_SUMMARY.md updated with
    refreshed knowledge state, weaknesses, and growth trends.
    ```

    Example for a governance core-concepts attempt scoring 28/50 (56%):

    ```
    mark governance/01-core-concepts attempt 1: 28/50 (56%)

    Attempt metadata captured in LOG.csv. LEARNER_SUMMARY.md updated with
    refreshed knowledge state, weaknesses, and growth trends.
    ```

    Use `git add` to stage the attempt file, LOG.csv, and LEARNER_SUMMARY.md. Do not stage unrelated files.

## Marking Rubric (Proportional)

The rubric below scales to any denominator. For a question worth N marks, map the fraction earned to the closest grade:

- **N/N**: Accurate, complete, specific, and commercially/operationally relevant.
- **~(N-1)/N**: Mostly correct with one meaningful omission or weak example.
- **~N/2**: Partially correct but generic, incomplete, or missing enterprise implications.
- **< N/2**: Some relevant ideas but important misconceptions or major omissions.
- **1/N**: Minimal correct content.
- **0/N**: Incorrect, blank, or not answering the question.

## Feedback Requirements

Each feedback block must include exactly these three elements, in order:

1. **Strengths** – One sentence naming what was handled well (or "The answer addresses the core question but…" if partial).
2. **Gap Analysis** – Name missing or incorrect concepts directly. Reference the relevant handbook section heading(s) so the learner knows exactly where to re-read.
3. **Actionable Direction** – One concrete suggestion the learner can apply next attempt (e.g. "Cover cloud resilience patterns from §Cloud Architecture", "Provide a financial-services example").

### Feedback Tone
- Be direct, not dismissive.
- Do not rewrite the learner's answer unless requested.
- Use regulated-enterprise phrasing where applicable.

## Output Contract

The blank attempt starts with this structure per question:

````markdown
### N. Question text?

```markdown

```

**Total Marks: N**
````

After the LLM marks, before `ca-prep finalise` adds the **Correction:** section:

````markdown
### N. Question text?

```markdown
Learner answer.
```

**Feedback:**
> Concise feedback.

**Marks: X/N**
````

After `ca-prep finalise` runs, the **Correction:** section is inserted from the base sheet answers:

```markdown
**Correction:**
```markdown
Model answer.
```
```
