# Protocol: Generate A Question Sheet

Use this when an LLM is asked to generate a new base question sheet.

## Inputs

- Module notes: `modules/<module>/study-notes.md`
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
6. Preserve the base sheet format: sections, subsections, numbered `###` questions, and no answer blocks.
7. Save the result as `modules/<module>/questions/<sheet-id>/base.md`.
8. If the user wants an attempt file, run `python3 scripts/create_blank_attempt.py <base> <attempt>`.

## Question Design Guidance

- Easy: definitions, distinctions, simple examples.
- Medium: compare concepts, explain governance tradeoffs, identify risks.
- Hard: apply concepts to banking workflows, design controls, critique operating models.
- Commercial analyst focus: ask about value, stakeholders, rollout risk, KPIs, governance, adoption, and executive communication.

## Output Contract

Each generated base sheet must include:

- Clear title.
- Sheet metadata.
- One or more named sections.
- Numbered markdown question headings.
- No answers, feedback, or marks.
