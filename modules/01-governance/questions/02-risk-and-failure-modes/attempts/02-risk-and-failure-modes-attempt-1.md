# Enterprise AI Governance & Commercialisation — AI Risk & Failure Modes - Attempt 1

## Attempt Metadata

- Module: governance
- Sheet: risk-and-failure-modes
- Attempt: 1
- Date: 2026_05_12
- Handbook: `modules/01-governance/01-governance-handbook.md`

---



# SECTION 1 — AI Risk & Failure Modes

## Understanding Risk

### 1. What is model drift?

```markdown
Model drift is where a model becomes less accurate over time due to shifting inputs or needs.
```

**Feedback:**
> Correct but minimal. Model drift typically spans concept drift, data drift, and environmental change. An enterprise answer would mention that without monitoring, retraining pipelines, and drift detection, risk increases silently.

**Correction:**
```markdown
Model drift is where a model looses accuracy over time due to concept drift, data drift, and environmental change. Without monitoring, retraining pipelines, and drift detection, risk increases silenty.
```

**Marks: 3/5**

---

### 2. Why can model performance deteriorate over time?

```markdown
Because of shifting data and requirements.
```

**Feedback:**
> Too vague. The handbook specifies behaviours change, environments evolve, and data distributions shift. In an enterprise setting you'd also note that model decay can go undetected without continuous monitoring and automated retraining.

**Correction:**
```markdown
Model performance deteriorates over time because behaviours change, environments evolve, and data istributions shift. Decay can go undetected without continuous monitoring and continuous retraining.
```

**Marks: 2/5**

---

### 3. What is hallucination risk?

```markdown
The risk that the model will make something up that is untrue.
```

**Feedback:**
> Correct as a starting point. The handbook notes that hallucinations include fabricated information, false citations, and misleading recommendations — all of which create operational and reputational risk in an enterprise context.

**Correction:**
```markdown
Hallucination risk is the risk that a model will make something up that is untrue. This can include fabricated information, false citations, and misleading reccomendations. These all create operational risk in an enterprise context.
```

**Marks: 3/5**

---

### 4. What is bias in AI systems?

```markdown
Where a models outputs may be shifted/unrepresentative due to bias in the training data/methods.
```

**Feedback:**
> Captures the core idea. The handbook stresses that human data often contains historical bias, incomplete representation, and discriminatory patterns, which models can amplify. Enterprise examples (hiring, lending, insurance pricing) would strengthen this significantly.

**Correction:**
```markdown
Bias in an AI system is where model outputs may be shifted/unrepresentative due to bias in the data/methods. Human data often contains historical bias, incomplete representation, and discriminatory patterns, which models can amplify. For example, a model that was trained to sift cv's that saw mostly male cv's may be biased against women. This would incur legal and reputational risks.
```

**Marks: 3/5**

---

### 5. How can training data introduce bias into models?

```markdown
If there are inaccuracies or imbalances in the data the same inaccuracies may be learned by the model.
```

**Feedback:**
> Inaccuracies and imbalances are part of it. The handbook also identifies historical bias, incomplete representation, discriminatory patterns, and skewed incentives as sources — and notes models may amplify these patterns. Enterprise context (e.g. a lending model trained on historically biased loan data) would improve the answer.

**Correction:**
```markdown
Training data can introduce bias though inaccuracies, imbalances, historical bias, incomplete representations, and discriminatory pattersns and skewed incentives int he data. Models may amplify these patterns. For example, a lending model trained on historically biased loan data would lead to loan approval biases and legal and reputaitonal risks.
```

**Marks: 3/5**

---

### 6. Why are black-box models difficult from a governance perspective?

```markdown
Because you canno explin why they made a certain decision, making it hard to validate, justify, or track what went wrong.
```

**Feedback:**
> The core point is right despite typos ("canno explin"). The handbook adds that opacity reduces trust, auditability, and regulatory defensibility. An enterprise answer should connect this to specific obligations like EU AI Act high-risk documentation or NIST AI RMF explainability requirements.

**Correction:**
```markdown
Black box models are difficult from a governance perspective because you canno explin why they made a certain decision, making it hard to validate, justify, or track what went wrong. Opacity reduces trust, auditability, and regulatoru defensibility. The EU AI Act requires that high risk AI systems maintain a standard of auditability and traceability.
```

**Marks: 3/5**

---

### 7. What is adversarial testing?

```markdown
???
```

**Feedback:**
> No answer provided. Adversarial testing means crafting inputs specifically designed to confuse or break a model, used to evaluate robustness. The handbook flags it as a requirement for systemic-risk GPAI providers under the EU AI Act.

**Correction:**
```markdown
Adversarial testing measn testing your system as if you are an adversary, crafting inputs designed to confure or break a model, evaulating robustness. This is a requirement for systemic-risk GPAI providers under the EU AI Act.
```

**Marks: 0/5**

---

### 8. What is prompt injection?

```markdown
Where maliscious instructions are injected into a system prompt that instruct the model to do something harmful.
```

**Feedback:**
> Correct concept but narrowly framed. The handbook says prompt injection attacks override instructions, bypass controls, or extract information — not just "instructions to do something harmful." Also relevant: prompt injection can come via user input or grounded context, not just the system prompt. Note spelling: "malicious."

**Correction:**
```markdown
Prompt injection is where malicious instructions are in inserted into a models context. It could instruct the model to override instructions, byass controls, or ectract information. Promot injections can come via the user input or gounrded context.
```

**Marks: 3/5**

---

### 9. What is data poisoning?

```markdown
Where maliscious/unwanted data included in the training data "poisins" the model, affecting its accuracy or alignment.
```

**Feedback:**
> Correct idea. The handbook calls this "model poisoning" — training data is manipulated to corrupt outputs. Note spelling: "malicious", "poisons." An enterprise answer would also flag that poisoned models can produce harmful or non-compliant outputs that bypass standard quality checks.

**Correction:**
```markdown
Data poisoning is where the training data is manipulated to corrupt outputs. Poisoned models can produce harmful or non-compliant outputs that bypass standard quality checks. For example, corrupting images of stop signs used fo train a self driving vision model, cuasing it to not recognise them. This could result in significant damage and liability, legal and reputational risk.
```

**Marks: 3/5**

---

### 10. What is shadow AI?

```markdown
AI used within organisations that is not tracked or subject to governance.
```

**Feedback:**
> Correct and well-stated. An enterprise answer could add that shadow AI systems operate outside formal oversight, approval, and security controls, which creates undetected risk exposure. The handbook lists it alongside prompt injection and data poisoning as a key security threat.

**Marks: 4/5**

---

### 11. What is data exfiltration in AI systems?

```markdown
???
```

**Feedback:**
> No answer provided. Data exfiltration is the unauthorised transfer of sensitive data, which in AI systems can leak through outputs, prompts, integrations, or embeddings. The handbook calls this a key privacy risk alongside prompt leakage and training-data exposure.

**Correction:**
```markdown
Data exfiltration si the unauthorised transfer of sensitive data, which in AI systems can leak through outputs, prompts, integrations, or embaddings. This is a key privacy risk, leading to legal and regulatory exposure. For example, using a model to gain a users session token and gain access to private data.
```

**Marks: 0/5**

---

### 12. Why are LLMs particularly susceptible to prompt injection attacks?

```markdown
Because they are often passed a prompt from the user or information from various sources for grounding, any of which could contain a prompt injection. 
```

**Feedback:**
> Good — correctly identifies that LLMs process untrusted input as part of the prompt. Stronger if you added the architectural reason: LLMs cannot reliably distinguish between instructions and data, so injected text in any input channel can override the system prompt. This blurred boundary is what makes them uniquely vulnerable.

**Marks: 4/5**

---

### 13. What are the reputational risks associated with AI?

```markdown
Innacurate or unsafe ai models can degrade an oganisations reputation if they perform badly.
```

**Feedback:**
> "Perform badly" is too vague to demonstrate enterprise awareness. The handbook connects reputational risk to biased outcomes, hallucinations, privacy violations, copyright infringement, and regulatory exposure — each of which can trigger public scandal, customer churn, or regulatory sanction. Note spelling: "Inaccurate", "organisations."

**Correction:**
```markdown
Reputational risk can come from biased outcomes, hallucinations, privacy violations, copyright infringemenr, and regulatoru exposure, each of whuich can trigger public scandal, customer churn, or regulatory sanction.
```

**Marks: 2/5**

---

### 14. Why is copyright risk becoming important in generative AI?

```markdown
Because models have the ability to memorise data and regurgitate it, potentially memorising copyright information. 
```

**Feedback:**
> Correct on memorisation risk. Could also note ongoing litigation, regulatory attention, and the EU AI Act requirement for GPAI providers to disclose training data summaries and comply with copyright law. These make it a live compliance issue, not just a theoretical one.

**Correction:**
```markdown

```

**Marks: 3/5**

---

### 15. What operational risks can arise from deploying AI too early?

```markdown
The model may not be properly evaluated or understood. It could contain bias, be innacurate, insafe, ect...
```

**Feedback:**
> The direction is right but the answer is mostly a list of general model problems without operational specificity. Enterprise operational risks include system downtime, customer-facing failures, regulatory non-compliance, inability to explain decisions to regulators, and costly remediation. Note spelling: "inaccurate", "unsafe", "etc."

**Marks: 3/5**
---

## Attempt Result

- Marked questions: 15
- Total marks: 39/75
- Percentage: 52.0%
