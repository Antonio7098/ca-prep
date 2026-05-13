# Protocol: Write A Handbook Using GEAR

Use this when the user asks you to create or revise a handbook or resource guide following the GEAR methodology.

GEAR stands for **Ground, Expose, Apply, Reinforce** — a four-movement rhythm that makes technical handbooks engaging, memorable, and coherent.

---

## What GEAR Solves

Handbooks fail when they:

- dump information without explaining why it matters
- present concepts without concrete examples
- use examples without connecting them back to principles
- treat each section as an island with no cross-links

GEAR solves all four by imposing a consistent section-level structure.

---

## The Four Movements

### G — Ground

**Purpose:** Anchor the reader. Establish why this section matters before delivering content.

Every section must open by answering at least one of:

| Question | Framing |
|---|---|
| What is the current problem or reality? | **As-Is** statement |
| What does success look like? | **To-Be** statement |
| Why should the reader care? | Stakes or consequence |
| How does this fit the bigger picture? | Contextual link |

Ground content is always 1-3 paragraphs. It sets the tension that the rest of the section resolves.

### E — Expose

**Purpose:** Deliver the core content. This is where the substance lives.

Rules:

- Lead each sub-section with the **single most important idea** in bold.
- Use **tables** for comparisons (most scannable format).
- Use **bullet lists** for enumerations and groupings.
- Use **numbered lists** only for sequences or priorities.
- Keep paragraphs short (max 3 sentences).
- One concept per paragraph.

### A — Apply

**Purpose:** Make the content concrete. Use examples and analogies.

Every major section must contain at least one of the following, placed in a blockquote callout:

| Callout Type | Prefix | When to Use |
|---|---|---|
| Scenario | `> **Scenario:**` | A concrete situation with characters, stakes, and outcome. Used for opening hooks or illustrating failure modes. |
| Analogy | `> **Analogy:**` | A comparison from a familiar domain (cars, construction, sports, etc.) that maps onto the concept being taught. |
| Key Idea | `> **Key Idea:**` | The single most important takeaway from the section. Used at the end of an Expose block. |
| Bigger Picture | `> **Bigger Picture:**` | A cross-section connection showing how this topic relates to others in the document or the real world. |
| Watch Out | `> **Watch Out:**` | A common mistake, anti-pattern, or pitfall to avoid. |

**Example structure (Apply block):**

> **Scenario:** A bank deploys an AI to approve small business loans. Within six months, the model has systematically denied 90% of applicants from two postal codes. The bank's only defence: "the algorithm decided." This is the cost of treating AI as a black box.
>
> **Key Idea:** An AI system you cannot explain is a system you cannot defend.

**Analogy pattern:**

1. Start with "Think of X as Y" (familiar → unfamiliar).
2. Extend the comparison for 1-2 specific points.
3. End with "The lesson: [principle]" (maps back to the concept).

### R — Reinforce

**Purpose:** Lock in the learning. Close the loop and transition.

Every section must end with at least one of:

| Element | Example |
|---|---|
| **Cross-link** | "This connects back to the accountability anti-patterns in §12." |
| **Implication** | "For a CTO, this means your monitoring budget should equal your training budget." |
| **Transition** | "With the failure modes understood, we can now examine how regulators respond." |

Reinforce content is always 1-2 sentences. It does not introduce new concepts.

---

## Formatting Rules

### Callouts

All Apply blocks must use blockquote format. Do not use code blocks, admonitions, or custom divs.

```
> **Scenario:** Text here.
```

### Headings

```
# Title (H1 — document title only)

## Section (H2 — major sections)

### Sub-section (H3 — within major sections)
```

Do not nest beyond H3.

### Lists

- Bullets for unordered groups.
- Numbers for sequences, priorities, or lifecycle phases.
- Tables for comparisons, frameworks, or structured data.

### Separators

Use `---` between top-level sections only. Do not use separators between H3 sub-sections.

---

## Handbook-Level Architecture

```
## Opening Section (Ground the entire document)
   G: As-Is nightmare scenario + To-Be promise
   E: What governance is, definition
   A: Scenario (the hiring AI)
   R: "This is what the entire handbook builds toward."

## Core Principle
   G: As-Is misconception (governance is technical)
   E: Sociotechnical principle
   A: Analogy (car crashes aren't just engine failures)
   R: Link to failure modes section

## Problem Space (one sub-section per failure mode)
   Each sub-section follows its own GEAR:
   G: As-Is of this specific failure
   E: Core content (definitions, lists)
   A: Example or scenario callout
   R: Cross-link to related failure modes

## Framework Sections (EU AI Act, NIST, etc.)
   G: As-Is (no framework existed / confusion)
   E: Core framework content
   A: Analogy (EU = traffic laws, NIST = driver's ed)
   R: Compare/contrast with other framework

## Operating Model / Accountability
   G: As-Is (unclear accountability)
   E: Tables, roles, requirements
   A: Scenario (marketing bought AI, IT deployed, legal ignored)
   R: Link to lifecycle section

## Security
   G: As-Is (traditional security doesn't cover AI)
   E: Threats and controls
   A: One scenario per threat
   R: "Security without governance is incomplete" (link back to §4)

## Lifecycle & MLOps
   G: As-Is (models fail to reach production)
   E: Phases, MLOps components
   A: Analogy (F1 car and pit crew)
   R: Link to governance stack

## Final Section (Close the loop)
   G: Reference back to opening scenario
   E: Strategic reality summary
   A: Analogy (brakes enable speed)
   R: Call back to opening hook
```

---

## Section Checklist

- [ ] Opens with Ground (As-Is / To-Be / stakes)?
- [ ] Core content in Expose (tables, lists, bold lead)?
- [ ] Contains at least one Apply callout (Scenario / Analogy / Key Idea / Watch Out)?
- [ ] Ends with Reinforce (cross-link / implication / transition)?
- [ ] No H4+ nesting?
- [ ] No separators between sub-sections?

---

## How This Interoperates With Other Protocols

This protocol produces handbooks that `generate-question-sheet.md` reads as source material. The structured sections and labelled callouts make it easy to identify which topics deserve heavier question weighting.

---

## Workflow

1. Read any existing handbook version before writing.
2. Plan the section architecture using the Handbook-Level Architecture above.
3. Write each section following GEAR, one at a time.
4. After writing, run the Section Checklist against the final document.
