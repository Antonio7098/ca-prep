# Protocol: Write A Better Handbook

Use this when creating or revising a module handbook.

The goal is a handbook that is structured, memorable, and useful without feeling like it has been forced into a visible template. The structure should guide the writer, not announce itself to the reader.

---

## Core Mindset

Every major section should balance three layers:

1. **Big Picture** — the underlying principle, strategic theme, or system-level pattern.
2. **Little Picture** — concrete examples, analogies, scenarios, outcomes, and impacts.
3. **Analysis** — tradeoffs, limitations, compromises, failure modes, and tensions.

The hidden writing loop is:

```text
Principle -> Mechanism -> Reality -> Implication
```

Example:

```text
AI governance is sociotechnical.
Models fail because organisational systems fail around them.
A hiring AI trained on biased history may automate discrimination.
Therefore governance needs accountability, monitoring, data controls, and human oversight.
```

Do not use `Big Picture`, `Little Picture`, or `Analysis` as mandatory headings. They are authoring checks, not visible scaffolding.

---

## What A Good Section Does

A strong section should:

- open with why the topic matters
- explain the mechanism clearly
- ground the concept in reality
- state the business, operational, regulatory, or strategic implication
- link to related ideas where useful
- avoid sounding like a transcript, podcast, or lecture script

The tone should be formal enough for a handbook, vivid enough to remember, and practical enough for interview preparation.

---

## Markdown Structure

Use this hierarchy:

```md
# Handbook Title

Short subtitle or purpose statement.

## 1. Major Section

Opening paragraph: principle, context, or stakes.

### 1.1 Subtopic

Core explanation.

> **Example:** Concrete real-world scenario.

> **Analyst Lens:** Why this matters in a commercial, governance, or enterprise context.

### 1.2 Subtopic

More detail.

> **Trade-off:** Limitation, compromise, or tension.
```

Rules:

- `#` is for the document title only.
- `##` is for numbered major sections.
- `###` is for subtopics.
- Do not use `####` or deeper nesting.
- Use `---` only between major sections when it helps readability.
- Do not put separators between every small subsection.
- Do not use visible methodology headings such as `Ground`, `Expose`, `Apply`, or `Reinforce`.

---

## Callouts

Use callouts selectively. They should clarify or sharpen the section, not decorate it.

Allowed callouts:

```md
> **Example:** A concrete situation with stakes and outcome.

> **Analogy:** A familiar comparison that clarifies the concept.

> **Analyst Lens:** Why this matters in a commercial, governance, or enterprise context.

> **Trade-off:** The compromise, limitation, or downside.

> **Watch Out:** A common misconception, anti-pattern, or failure pattern.

> **Key Takeaway:** The one thing to remember.
```

Guidance:

- Use at most 1-2 callouts per major section unless the topic genuinely needs more.
- Prefer one strong example over several weak ones.
- Keep analogies short and explicitly map them back to the concept.
- Do not make every subsection follow the same callout rhythm.

---

## Formatting Rules

- Use tables for comparisons, frameworks, roles, obligations, and structured contrasts.
- Use bullet lists for unordered groups.
- Use numbered lists only for sequences, lifecycle stages, or priorities.
- Keep paragraphs short, usually 1-3 sentences.
- Use bold sparingly for labels, key terms, and section-leading ideas.
- Define acronyms on first use.
- Prefer concrete nouns and business consequences over vague emphasis.
- Use British English if the existing module does.

---

## Tone Rules

Keep:

- vivid examples
- business consequences
- useful analogies
- section-to-section links
- memorable framing

Avoid:

- podcast phrasing
- rhetorical back-and-forth
- excessive drama
- filler intensifiers such as "insane", "terrifying", or "massive" unless the claim warrants it
- visible methodology scaffolding
- mechanical repetition across sections

Target style:

> Formal enough to trust. Concrete enough to remember. Practical enough to apply.

---

## Recommended Handbook Architecture

For a governance-style module:

```md
## 1. Why The Topic Exists
Big principle, core tension, opening example.

## 2. Core Mental Model
The governing concept that explains the rest of the module.

## 3. Problem Space
How the topic fails in practice.

## 4. Key Distinctions
Important comparisons and boundaries.

## 5. Frameworks And Regulation
External standards, laws, and structured methods.

## 6. Operating Model
Roles, ownership, accountability, escalation.

## 7. Lifecycle
How the work moves from idea to operation to retirement.

## 8. Controls And Tooling
Practical mechanisms that make the operating model real.

## 9. Strategic Reality
What this means for enterprise value, risk, and execution.
```

Adapt this architecture to the module. Do not force every handbook into the same section list.

---

## Revision Workflow

1. Read the existing handbook and any source material.
2. Identify what is too dry, too conversational, or too mechanically structured.
3. Preserve the best concrete examples and analogies.
4. Replace visible scaffolding with natural headings.
5. Add selective callouts for examples, analyst implications, tradeoffs, and warnings.
6. Check that each major section has Big Picture, Little Picture, and Analysis somewhere in the prose.
7. Check the markdown hierarchy.
8. Remove repeated phrasing and forced transitions.

---

## Final Quality Checklist

- [ ] Does each major section explain why the topic matters?
- [ ] Are examples concrete and realistic?
- [ ] Are outcomes and impacts stated clearly?
- [ ] Are tradeoffs or limitations covered where relevant?
- [ ] Does the markdown hierarchy stay within H1/H2/H3?
- [ ] Are callouts useful rather than repetitive?
- [ ] Is the prose more formal than a transcript but more engaging than notes?
- [ ] Could this source support question generation and interview preparation?
