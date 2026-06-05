### CHAPTER 4: Adjustments for Measured Covariates

**Core Claim:** Matching treated individuals to controls with similar observed covariates can remove visible differences between groups, thereby enabling more credible causal comparisons — though only for differences that are measured.

**Supporting Evidence:**
- After matching 441 smokers to 441 controls on propensity scores (derived from sex, age, income, education, race):
  - Sex balance: 50.8% male smokers vs. 49.9% male controls (consistent with random assignment, p=0.63).
  - The tenfold difference in smoking rates across demographic strata (4.3% vs. 42.3%) was eliminated: matched groups were approximately 50% smokers within every subgroup.
  - Propensity score distributions: before matching, medians far apart; after matching, virtually identical.
- Outcome comparison after matching: smokers still had substantially more periodontal disease than matched controls — median 12.4% vs. 1.2% disease locations in the unmatched comparison; the difference persisted post-matching.
- Propensity score theorem (informal): matching on the propensity score — a single derived variable — tends to balance all covariates used in computing it.

**Logical Method:** The chapter proves the propensity score's balancing property by an informal argument about coin vs. die people: if two individuals have the same propensity score but different raw covariate values, knowing the covariates does not help predict which received treatment — the propensity score has absorbed all the relevant information.

**Logical Gaps:**
- The propensity score is estimated from data; estimation error is acknowledged ("terrible estimation may not do what the true probabilities would") but not formally quantified. In practice, model misspecification of the propensity score is a major source of error that receives minimal treatment here.
- The chapter proves that matching balances covariates *included in the propensity score* but cannot balance unmeasured covariates — this critical limitation is stated but not formally bounded. How large could unmeasured imbalances be? Chapter 5 addresses this, but the gap is real here.
- The matched controls have slightly more periodontal disease than unmatched controls. The chapter acknowledges this without fully explaining it; the likely explanation is that higher-propensity-score controls were matched, and higher propensity scores may correlate with other disease risk factors. The observation matters because it shows matching is not variance-free.

**Methodological Soundness:** The propensity score argument is informally but correctly presented. The coin-people/die-people analogy is the book's most pedagogically effective analytical device. The matching result is genuine: the achieved balance is documented and credible.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-adjustments-for-measured-covariates.md`

### Conceptual Foundations

1. **Matching is design, not magic.** Matching attempts to make treated and control groups comparable before outcome analysis. It does not create randomization.

2. **The propensity score is a balancing score.** Rosenbaum and Rubin define it as the probability of treatment conditional on observed covariates. Conditional on the true score, observed covariates are balanced across treatment groups.

3. **Balance matters more than prediction accuracy.** A useful propensity-score procedure is judged by covariate balance and overlap, not by how well the treatment model predicts treatment.

4. **Only measured covariates are adjusted.** Propensity scores cannot remove hidden confounding, omitted severity, unmeasured motivation, unrecorded access differences, or measurement error unless additional assumptions/sensitivity analyses are used.

### Domain Examples and Cases

- **Smoking and periodontal disease:** chapter's central worked case.
- **Medical treatment comparisons:** treatment choice often depends on baseline severity and comorbidities.
- **Education program evaluation:** intervention students may differ systematically before treatment.
- **Policy evaluation:** adopting jurisdictions can be matched to similar non-adopting jurisdictions, but time-varying confounding remains.

Failure cases:

- Including post-treatment variables.
- Poor overlap/common support.
- Reporting only p-values, not balance.
- Treating the matched estimand as if it represented everyone.

### Connections and Dependencies

Readers need confounding, pre-treatment versus post-treatment variables, potential outcomes, and exchangeability. This section sets up sensitivity analysis: once measured differences are balanced, the next question is how large an unmeasured difference would need to be.

### Current State of the Field

Settled: propensity scores balance observed covariates under the Rosenbaum/Rubin framework; design should be separated from outcome analysis; unmeasured confounding remains.

Contested: when propensity-score matching is preferable to weighting, full matching, covariate matching, doubly robust methods, or causal machine-learning estimators; which variables belong in the propensity score; how to combine matching with outcome regression.

Recent-change note: recent work emphasizes balance, overlap, and design-stage diagnostics, with propensity scores increasingly discussed alongside causal machine learning and balancing weights.

Key sources:

- Rosenbaum and Rubin (1983), "The Central Role of the Propensity Score."
- Peter Austin (2011), propensity-score methods introduction.
- Hernán and Robins, *Causal Inference: What If*.
- Rosenbaum, *Design of Observational Studies*.
- Biometrika review on propensity scores in observational-study design.

### Teaching Considerations

Students often think propensity scores are outcome-risk scores or that matching proves causality. Use "apples-to-apples, but only on recorded labels" and the coin/die analogy.

Exercises:

1. Identify pre-treatment confounders, mediators, instruments, and colliders.
2. Build before/after balance tables and plots.
3. Diagnose lack of overlap.
4. Write an unmeasured-confounding limitation paragraph.
