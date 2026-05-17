# CA Prep

Structured preparation for a Commercial Analyst role focused on enterprise AI, banking, governance, delivery, and executive communication.

## How to Use

1. **Create a module's study material** — prompt the coding agent with `@protocols/write-handbook.md` and pass in source documents or ask it to web-search. It will produce a structured handbook at `modules/<num>-<module>/<num>-<module>-handbook.md`.

2. **Generate a question sheet** — prompt the coding agent with `@protocols/generate-question-sheet.md` and specify an area, difficulty, and focus. The sheet is saved at `modules/<num>-<module>/questions/<num>-<sheet-name>/base.md`. Run `ca-prep create <sheet-path>` to produce a blank attempt file.

3. **Answer the questions** — fill in the attempt file by writing answers under each question block.

4. **Mark the attempt** — prompt the coding agent with `@protocols/mark-attempt.md`. It reads the handbook, base sheet, and learner summary; adds feedback and marks to the attempt; then runs `ca-prep finalise` to aggregate marks and log the result.

5. **Correct based on feedback** — after marking, `ca-prep finalise` inserts the model answer (Correction block) into the attempt. Review the feedback, update your knowledge in `@LEARNER_SUMMARY.md`, and study the gaps before the next sheet.

Track long-term progress in `@LEARNER_SUMMARY.md`. See all past attempts in `@LOG.csv`.

## Structure

- `modules/<num>-<module>/<num>-<module>-handbook.md`: handbook for the module.
- `modules/<num>-<module>/questions/<num>-<sheet>/base.md`: clean question sheet with mark scheme criteria per question and no answers.
- `modules/<num>-<module>/questions/<num>-<sheet>/attempts/<num>-<sheet>-attempt-N.md`: answer sheet with learner responses, feedback, marks, and total result.
- `templates/`: reusable markdown templates for question sheets and attempts.
- `LEARNER_SUMMARY.md`: living document tracking knowledge state, strengths, weaknesses, and progress across all attempts.
- `protocols/`: authoritative protocols for writing handbooks, generating question sheets, and marking attempts.
- `scripts/`: utilities for generating attempts and aggregating marks.
- `LOG.csv`: running log of all marking events, appended to automatically by `ca-prep finalise`.
- `resources/`: source documents and reference material.

## Current Module

- `01-governance`: AI governance, risk, responsible AI, EU AI Act, NIST AI RMF, security, enterprise operating models.

## Common Commands

Create a blank attempt from a base question sheet:

```bash
ca-prep create modules/01-governance/questions/01-core-concepts
```

Aggregate marks for an attempt and write the result block:

```bash
ca-prep finalise modules/01-governance/questions/01-core-concepts/attempts/01-core-concepts-attempt-1.md
```

Preview the current result without editing:

```bash
ca-prep finalise modules/01-governance/questions/01-core-concepts/attempts/01-core-concepts-attempt-1.md --check
```

Extract a clean base question sheet from an answered attempt:

```bash
ca-prep extract modules/01-governance/questions/01-core-concepts/attempts/01-core-concepts-attempt-1.md modules/01-governance/questions/01-core-concepts/base.md
```

## Planned Modules

- `01-governance`: AI governance, responsible AI, model risk, data governance, EU AI Act, NIST AI RMF.
- `commercialisation`: AI opportunity identification, ROI, adoption, pilots, stakeholder mapping.
- `banking-operations`: KYC, AML, onboarding, compliance, fraud, document workflows, contact centres.
- `enterprise-delivery`: pilot-to-production, approvals, rollout, vendor selection, adoption, controls.
- `executive-communication`: concise strategy writing, business cases, risk communication, presentation structure.
- `capstone`: HSBC AI Transformation Workbench.