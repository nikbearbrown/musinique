### BRIDGE: Synthesizing the Logical Architecture

The book's argument moves from axiom to method to limit — a deductive structure that earns its uncertainty rather than evading it.

**The central logical spine:** Causal inference requires comparing potential outcomes in two worlds that cannot both be observed. Randomization solves this by making the observed world a random draw from all possible worlds. When randomization is infeasible, the investigator must work backward: adjust for measured confounds, quantify sensitivity to unmeasured confounds, seek natural experiments that introduce genuine randomness, and triangulate across designs with different vulnerabilities. None of this achieves the certainty of randomization. It achieves credibility proportional to the diversity and independence of evidence.

**Three tensions that run across all chapters:**

*Tension 1: Individual causation vs. population causation.* The book opens with Washington and closes with an individual smoker's glass of wine. In between, all inferential machinery operates at the population level. The individual causal question — "did this drug kill this patient?" — is declared permanently insoluble in Chapter 1 and never revisited. This is methodologically honest but leaves a philosophical gap: courts, clinicians, and policymakers routinely must make causal attributions for specific cases. The book's tools are adequate for policy; they are insufficient for liability.

*Tension 2: The enemy of good is perfect.* The book consistently argues that demanding randomization as the only valid basis for causal inference is epistemically wrong — it would require ignoring the causal link between smoking and cancer. But the book also insists that observational evidence is always potentially contaminated by unmeasured confounding. The resolution proposed (Γ sensitivity, diverse replications) is the right one, but the boundary between "good enough" observational evidence and "not good enough" is never formalized.

*Tension 3: The selection problem and its solutions.* Every chapter from 3 through 9 is a variation on a single theme: the people who receive a treatment differ systematically from those who do not. Each chapter offers a partial solution — matching, sensitivity analysis, quasi-experimental devices, natural experiments, genetic instruments. But these solutions are cumulative, not substitutable. A Γ analysis does not replace good matching; a natural experiment does not replace sensitivity analysis. The book's implicit claim is that the most credible observational studies deploy all of these tools simultaneously, but this is never stated as a formal checklist.

**The book's most proven claims:**
- Randomization eliminates unmeasured confounding — by construction, not by statistical correction.
- The potential outcomes framework is the correct formalization of causal questions.
- The Γ sensitivity framework correctly quantifies how large a confound must be to explain an association.
- The smoking-lung cancer association meets extremely high standards of robustness (Γ > 5 across multiple methodologies).

**The book's most significant unproven claims:**
- That the Γ framework is routinely adequate for general observational inference (limitations of the original Cornfield method are acknowledged; the generality of modern methods is asserted more than proven).
- That comparing estimates across "independent" evidence factors from the same dataset is statistically valid (deferred to references throughout).
- That the EITC counterpart method provides credible causal evidence (the critical assumption — that counterpart trends proxy the treated group's counterfactual trend — is stated, not tested).

**The book's deepest acknowledged limitation:**
The entire inferential apparatus presupposes that the investigator knows which confounders are plausible. The selection of covariates to measure, the construction of propensity scores, the choice of which counterclaims to anticipate — all require domain knowledge that no statistical method can supply. The book explicitly acknowledges this at multiple points ("the study of CTLA4 requires knowing that CTLA4 is worth studying") but offers no guidance on how to build that knowledge. This is not a flaw in the book; it is an honest description of the limit of the discipline.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-bridge-synthesizing-the-logical-architecture-causal-inference-rosenbaum-2020.md`

Key additions: observational inference earns credibility through design plus sensitivity, not adjustment alone. Gamma sensitivity asks how strong hidden bias would need to be, while matching, evidence factors, natural experiments, and domain knowledge do separate jobs.

Settled: potential outcomes, randomization, matching, and sensitivity analysis are central to modern causal inference. Contested: thresholds for "good enough" observational evidence and how to combine dependent evidence factors.

Teaching move: require students to state design assumption, likely hidden confounder, Gamma threshold, and replication strategy.
