### CHAPTER 2: Randomized Experiments

**Core Claim:** Randomized treatment assignment solves the causal inference problem by ensuring that the actual world is a random draw from the space of possible worlds — making certain population averages in the observed world close to averages over all possible worlds.

**Supporting Evidence:**
- The PALM Trial (Democratic Republic of Congo, 2018–2019): 343 patients with Ebola virus disease randomized to ZMapp (n=169) or MAB114 (n=174).
- Survival rate: MAB114: 113/174 = 64.9%; ZMapp: 85/169 = 50.3%. Estimated ATE: +14.6 percentage points.
- Balance table: mean age 27.4 vs. 29.7 years; 51.5% vs. 56.3% female — differences attributable to chance, not systematic allocation.
- The probability of observing a survival difference as large as 14.6% under the null hypothesis of no effect: p = 0.0083 (less than 1 in 100).
- The coin-flip argument: over many pairs, the estimated ATE is unbiased; its variance decreases with sample size by the law of large numbers.

**Logical Method:** Two parallel arguments establish the value of randomization: (1) it balances observed covariates (demonstrated in the PALM balance table), and more importantly (2) it balances *unobserved* covariates, including those not yet discovered — because the coin knows nothing about person attributes. A third argument establishes randomization as the basis for testing the null hypothesis of no effect, converting an insoluble metaphysical question into a calculable probability.

**Logical Gaps:**
- The chapter proves the *unbiasedness* of the ATE estimator under randomization but does not discuss power explicitly — the sample size needed to achieve a given probability of detecting a true effect. The 343-patient PALM trial was underpowered to detect small effects, a limitation not addressed.
- The data-safety monitoring board's early termination of two arms is mentioned without analyzing the statistical implications of interim analyses. Interim stopping inflates Type I error if not pre-specified and adjusted for — a genuine methodological issue the chapter glosses.
- The proof that randomization balances unobserved covariates is argued by analogy (the coin knows nothing about attributes) rather than by formal proof. The argument is correct but could be made more precise.

**Methodological Soundness:** The PALM trial is a well-chosen example: a controlled trial with genuine equipoise, an external safety monitoring board, and a clear primary outcome. The treatment of ethics (equipoise, informed consent) is more rigorous than most causal inference textbooks. The statistical argument for testing the null hypothesis via permutation is mathematically sound.

---
