# Protocol: Generate A Question Sheet

Use this when an LLM is asked to generate a new base question sheet.

## Inputs

- Module notes: `modules/<num>-<module>/<num>-<module>-handbook.md`
- Template: `templates/base-question-sheet.md`
- User parameters:
- Area
- Difficulty
- Focus
- Number of questions
- Question style
- Target role or business context

## Required Process

1. Read the module notes before generating questions.
2. Identify the concepts most relevant to the requested area, difficulty, and focus.
3. Generate questions from the notes rather than external general knowledge unless the user explicitly requests expansion.
4. Prefer practical enterprise prompts over academic definitions.
5. Include scenario questions for commercial analyst preparation where appropriate.
6. Preserve the base sheet format: sections, subsections, numbered `###` questions, with answer code blocks and `---` separators.
7. Save the result as `modules/<num>-<module>/questions/<num>-<descriptive-sheet-name>/base.md`.
   - **Use descriptive kebab-case sheet names** that reflect the section content (e.g. `core-concepts`, `risk-and-failure-modes`, `eu-ai-act`, `trustworthy-ai`). Never use generic names like `sheet-1` or `questions-set`.
   - The name should make it immediately obvious what topic the sheet covers.
8. If the user wants an attempt file, run `python3 scripts/create_blank_attempt.py <base.md>`. The script auto-detects the attempts directory and next attempt number.

## Question Design Guidance

- Easy: definitions, distinctions, simple examples.
- Medium: compare concepts, explain governance tradeoffs, identify risks.
- Hard: apply concepts to banking workflows, design controls, critique operating models.
- Commercial analyst focus: ask about value, stakeholders, rollout risk, KPIs, governance, adoption, and executive communication.

## Marks Guidance

Each question has a **max marks** field (e.g. `**Marks: /5**`) in the base sheet. Determine the max marks per question based on:

- **Complexity** — how many distinct concepts or sub-parts the handbook covers for that topic.
- **Difficulty** — easy questions (1-3 marks), medium (3-5 marks), hard (5-8 marks).
- **Handbook depth** — if the handbook dedicates significant content to a topic, the question should carry more marks.
- **Enterprise scope** — questions requiring commercial or operational judgment should have higher weight.

This field is set at sheet creation time so learners see what each question is worth before they answer. The marking protocol uses `/5` by default; adjust the denominator when a question warrants more or less weight.

## Output Contract

Each generated base sheet must include:

- Clear title.
- Sheet metadata.
- One or more named sections.
- Numbered markdown question headings.
- No answers or feedback. Each question includes a **Marks** field showing max marks available.
