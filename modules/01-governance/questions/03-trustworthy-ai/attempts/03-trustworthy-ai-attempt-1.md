# Enterprise AI Governance & Commercialisation — Trustworthy AI - Attempt 1

## Attempt Metadata

- Module: governance
- Sheet: trustworthy-ai
- Attempt: 1
- Date: 2026_05_13
- Handbook: `modules/01-governance/01-governance-handbook.md`

---


# SECTION 1 — Trustworthy AI

## NIST Trustworthiness Principles

### 1. What characteristics define trustworthy AI according to NIST?

```markdown
Trustworthy AI is AI that is properly governed. It is safe, explainable, governable, reliable, and transparent. Low trust systems risk reputational loss and legal exposure.
```

**Feedback:**
> Strengths: Correctly identifies safe, explainable, reliable, and transparent as key NIST characteristics, and connects the outcome to reputational loss and legal exposure. Gap Analysis: "Governable" is not a NIST characteristic — the handbook lists Valid & Reliable, Safe, Secure & Resilient, Explainable, Privacy-Enhancing, Fair, and Accountable & Transparent (§11). Misses privacy-enhancing, fairness, secure & resilient, and accountable dimensions entirely. Actionable Direction: Memorise all seven NIST trustworthiness characteristics from the handbook §11 table and list each one with a one-sentence definition.

**Correction:**
```markdown
NIST defines the following characteristics for trustworthy AI: Valid and Reliable, Safe, Secure and REsilient, Explainable, Privacy-Enhancing, Fair, and Accountable and Transparent.
```
**Marks: 3/5**

---

### 2. Why must trustworthy AI be explainable?

```markdown
AI must be explainable because if we do not understand why it made a decision, we cannot validate its accuracy, trace the decision making, or justify it to regulators. For example, a loan model that cannot explain why it denied a loan to a person would be unnaceptable to regulators. Furthermore, it would make it hard to track the source of bias in the model. This would lead ro leagal exposure and reputational loss.
```

**Feedback:**
> Strengths: Strong enterprise-relevant answer with a concrete lending-model example and clear regulatory, legal, and reputational implications. Gap Analysis: None on content — this covers the required depth for 3 marks. Watch spelling: *unnaceptable*, *leagal*, *ro*. Actionable Direction: Run a proofreading pass before submitting — these typos erode professionalism in a regulated-enterprise context.

**Marks: 3/3**

---

### 3. What does privacy-enhancing AI mean?

```markdown
Privacy enhancing AI does not increase the risk of pvivate data being exposed.
```

**Feedback:**
> Strengths: The core idea — protecting data from exposure — is directionally correct. Gap Analysis: This is a single sentence for a 3-mark question. The handbook (§3, Privacy & Data Leakage) identifies specific risk types: customer data, internal IP, regulated information, confidential documents; and attack vectors: prompt leakage, data exfiltration, training-data exposure, insecure integrations. None of these are mentioned. No enterprise example or implication. Actionable Direction: Elaborate using the handbook categories — list the types of protected data and at least one specific risk vector (e.g. prompt leakage exposing customer PII) with a regulatory consequence.

**Correction:**
```markdown
Privacy enhancing AI does not increase the risk of pvivate data being exposed. Private data could come in the form of customer data, internal IP, regulated information, or confidential documents. The attack vectors are prompt leakage, data exfiltration, training-data exposure, insecure integrations. For example, an llm trained on confidential documents could be prompted to regurgitate the exact document. This would lead to leagal liability and loss of customer trust.
```

**Marks: 1/3**

---

### 4. Why is fairness critical in enterprise AI systems?

```markdown
Fairness is criticla in enterprise AI systems because it protects the company from legal and regulatory risk. Unfairness stems from bias, where models unjustly skew towards/away from certain populations. For example, a medival vision model that performs worse on darker skin. This will lead to legal action, reputational damage, and customer loss.
```

**Feedback:**
> Strengths: Strong D-E-C-A structure — defines fairness as legal/regulatory protection, explains bias mechanism, gives a specific medical-vision example with skin-tone disparity, and applies implications (legal, reputational, customer loss). Gap Analysis: Spelling (*criticla*, *medival*, *skew*). The handbook (§3, Bias & Fairness Failures) lists specific bias sources — historical bias, incomplete representation, discriminatory patterns, skewed incentives — touching on at least one would strengthen the answer. Actionable Direction: Proofread, and consider naming one additional bias type from the handbook to show breadth.

**Correction:**
```markdown
Sources of bias include historical bias, incomplete representation, discriminatory patterns, and skewed incentives.
```

**Marks: 3/3**

---

### 5. What is the relationship between transparency and trust?

```markdown
Transparency is necessary for trust. If it is not clear how a system works, how it was developed, and why it produces the outputs that it does, it is impossibel to fully trust it.
```

**Feedback:**
> Strengths: Correctly states the causal relationship — transparency enables trust — and lists three dimensions (how it works, development, output reasoning). Gap Analysis: Stops at definition; no enterprise example (e.g. a bank's credit-scoring model that must disclose its logic to regulators and customers) and no implications (reduced auditability, regulatory defensibility — see handbook §3, Explainability & Transparency Failures). Actionable Direction: Add a regulated-industry example showing how opacity undermines regulatory trust, and connect to auditability and defensibility outcomes.

**Correction:**
```markdown
For example, 
```

**Marks: 2/3**

---

### 6. Why must AI systems be resilient?

```markdown
AI systems must be resilient because environments change over time.
```

**Feedback:**
> Strengths: Recognises that environmental change is a reason for resilience — this is one component of the answer. Gap Analysis: For 3 marks this needs much more. The handbook (§3, Model Drift and Security Threats) identifies specific failure modes: model drift (concept drift, data drift), adversarial attacks, data poisoning, prompt injection. Missing entirely: connection to operational continuity, security threats, and enterprise impact (e.g. system downtime, customer-facing failures). Actionable Direction: Cover at least two specific resilience threats (e.g. model drift + adversarial attack) with a concrete operational example and business impact.

**Correction:**
```markdown
AI must be resilient
```

**Marks: 1/3**

---

### 7. Why is accountability necessary for trustworthy AI?

```markdown
Accountability is necessary for trustworthy AI because it forces responsible practices. If no one is held accountable whe something goes wrong, there is no incentive to practice responsible AI and therefore no reason to trust.
```

**Feedback:**
> Strengths: Correctly links accountability to incentives and trust — the core logic is sound. Gap Analysis: Stops at concept; no enterprise specifics. The handbook (§14, Accountability) identifies concrete mechanisms: named accountability, governance ownership, escalation authority, documented responsibility. Missing anti-patterns (*nobody owns AI*, *everyone owns AI*). No real-world example (e.g. who owns an automated lending decision when a model denies credit). Actionable Direction: Reference specific accountability mechanisms from §14 and give a regulated-industry example where unclear ownership caused governance failure.

**Correction:**
```markdown

```

**Marks: 2/3**

---

### 8. What does validity and reliability mean in AI systems?

```markdown
Validity means how accurate and trustworthy the outputs of a model are. Reliability is wether you can rely on the model to perform consistently over time. These are key attributes for any system to have in order to be trusted.
```

**Feedback:**
> Strengths: Distinguishes between accuracy (validity) and consistency over time (reliability) — the core distinction is correct. Gap Analysis: Definitions are generic. The handbook (§3, Hallucinations & Reliability Failures) connects reliability to specific failure modes: fabrication, false citations, misleading recommendations, inconsistent outputs. No enterprise example (e.g. an LLM-powered customer-facing chatbot hallucinating regulatory guidance) and no operational implications. Actionable Direction: Add at least one specific reliability failure (hallucination, drift) with a concrete enterprise scenario and the business impact.

**Correction:**
```markdown

```

**Marks: 2/3**

---

### 9. Why is safety considered a trustworthiness requirement?

```markdown
Safety is considered a trustworthiness requirement becasuse of the risks associated with unsafe systems. Uou cannot trust a system that might leak your personal information, expose secrets, or open you up to malicious attacks. A safe system will expose you to minimal risk and can therefore be trusted.
```

**Feedback:**
> Strengths: Connects safety to risk exposure and identifies specific harms — data leakage, secret exposure, malicious attacks. Gap Analysis: The answer leans heavily into security (malicious attacks) rather than safety (avoiding harmful outcomes per §11). Missing enterprise-specific safety concerns: operational failures causing customer harm, regulatory penalties, model-induced business disruption. The handbook §3 section on Safety should be distinguished from Security. Actionable Direction: Distinguish safety (harmful outcomes from normal use) from security (malicious attacks), and give a regulated-enterprise example where unsafe outputs caused customer or regulatory harm.

**Correction:**
```markdown

```

**Marks: 2/3**

---

### 10. How can organizations operationalize fairness?

```markdown
Organisations can operationalise fairness throuh standard checks and procedures.
```

**Feedback:**
> Strengths: Directionally correct — fairness does require standardised procedures. Gap Analysis: This is too vague for 4 marks. The handbook (§12, MEASURE function) specifies concrete fairness operationalisation: fairness analysis, bias testing, validation, monitoring, diverse training data, impact assessments. No mention of any specific method, metric, or process. No enterprise example (e.g. a bank running differential impact analysis on a lending model before deployment). Actionable Direction: Name at least three specific fairness operationalisation techniques from the handbook (bias testing, diverse data, impact assessments) with a concrete financial-services example.

**Correction:**
```markdown

```

**Marks: 1/4**
---

## Attempt Result

- Marked questions: 10
- Total marks: 20/33
- Percentage: 60.6%
