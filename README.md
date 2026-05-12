# CA Prep

Structured preparation for a Commercial Analyst role focused on enterprise AI, banking, governance, delivery, and executive communication.

The working loop is:

> Learn -> Analyse -> Build -> Present

## Structure

- `modules/<num>-<module>/<num>-<module>-handbook.md`: handbook for the module.
- `modules/<num>-<module>/questions/<num>-<sheet>/base.md`: clean question sheet with no answers.
- `modules/<num>-<module>/questions/<num>-<sheet>/attempts/attempt-N.md`: answer sheet with learner responses, feedback, marks, and total result.
- `templates/`: reusable markdown templates for question sheets and attempts.
- `LEARNER_SUMMARY.md`: living document tracking knowledge state, strengths, weaknesses, and progress across all attempts.
- `protocols/`: LLM workflows for marking attempts and generating question sheets.
- `scripts/`: utilities for generating attempts and aggregating marks.
- `LOG.csv`: running log of all marking events, appended to automatically by `summarise_attempt_marks.py`.
- `resources/`: source documents and reference material.

## Current Module

- `01-governance`: AI governance, risk, responsible AI, EU AI Act, NIST AI RMF, security, enterprise operating models.

## Common Commands

Create a blank attempt from a base question sheet:

```bash
python3 scripts/create_blank_attempt.py modules/01-governance/questions/01-core-concepts/base.md
```

Aggregate marks for an attempt and write the result block:

```bash
python3 scripts/summarise_attempt_marks.py modules/01-governance/questions/01-core-concepts/attempts/attempt-1.md
```

Preview the current result without editing:

```bash
python3 scripts/summarise_attempt_marks.py modules/01-governance/questions/01-core-concepts/attempts/attempt-1.md --check
```

Extract a clean base question sheet from an answered attempt:

```bash
python3 scripts/extract_base_from_attempt.py modules/01-governance/questions/01-core-concepts/attempts/attempt-1.md modules/01-governance/questions/01-core-concepts/base.md
```

## LLM Workflows

Use `protocols/mark-attempt.md` when asking an LLM to mark an attempt. The LLM should read the module notes, base sheet, and learner summary first, edit feedback and marks in the attempt, run the mark aggregation script, then update the learner summary.

Use `protocols/generate-question-sheet.md` when asking an LLM to generate a new question sheet from a module's notes and a requested area, difficulty, focus, or target role.

## Planned Modules

- `01-governance`: AI governance, responsible AI, model risk, data governance, EU AI Act, NIST AI RMF.
- `commercialisation`: AI opportunity identification, ROI, adoption, pilots, stakeholder mapping.
- `banking-operations`: KYC, AML, onboarding, compliance, fraud, document workflows, contact centres.
- `enterprise-delivery`: pilot-to-production, approvals, rollout, vendor selection, adoption, controls.
- `executive-communication`: concise strategy writing, business cases, risk communication, presentation structure.
- `capstone`: HSBC AI Transformation Workbench.
