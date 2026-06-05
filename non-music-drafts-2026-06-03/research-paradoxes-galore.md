### CHAPTER 6: Paradoxes Galore

**Core Claim:** Probabilistic paradoxes — Monty Hall, Berkson's, Simpson's — are not puzzles about mathematics. They are collisions between causal intuition and statistical logic. They are resolved, cleanly and definitively, by causal diagrams. Their persistence as "paradoxes" reflects the absence of causal thinking in statistical education.

**Supporting Evidence:**
- Monty Hall: collider bias (door opened is a collider of your door and car location) — when you condition on Monty's opening, a spurious dependence between your door and car location is created
- Berkson's paradox: hospital admission is a collider of two independent diseases, creating spurious correlation
- Simpson's paradox: drug D appears good for the aggregate population but bad for both men and women — resolved by identifying gender as a confounder (not mediator), requiring stratification not aggregation
- Drug B example: same data structure, blood pressure as mediator — requires aggregation not stratification. Same data, opposite correct answer.
- Lord's paradox: diet vs. initial weight — resolved by identifying whether initial weight is a confounder or mediator depending on the causal story

**Logical Method:** Formal analysis of paradoxes + causal diagram resolution. The contribution is demonstrating that the direction of resolution (stratify vs. aggregate, control vs. don't control) is determined by causal structure, not by data properties.

**Logical Gaps:**
- The claim that the BBG drug is impossible follows from the Sure Thing Principle. Pearl is correct that this requires a causal assumption (the drug doesn't change gender ratio). The derivation is valid; the presentation slightly undersells the assumption's importance.
- Simpson's paradox resolution in the blood pressure example depends on blood pressure being a *mediator*, not a confounder — a causal judgment, not a statistical one. Pearl is right that this requires the diagram. But the practical problem remains: how do we get the right diagram?
- Jeter vs. Justice batting average: Pearl uses this as an example of "not a paradox" (just uneven sample sizes). This is fine, but the line between "numerical reversal" and "genuine paradox" is not fully operationalized.

**Methodological Soundness:** All the paradox resolutions are mathematically correct. The unified framework (collider bias as the mechanism behind Monty Hall, Berkson, and parts of Simpson's) is a genuine theoretical contribution.

---
