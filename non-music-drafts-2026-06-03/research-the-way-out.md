### CHAPTER 7: The Way Out

**Core Claim:** Fixing statistics requires (1) abandoning the frequentist interpretation of probability, (2) abandoning the associated eugenics-descended terminology, (3) adopting Bayesian inference, and (4) accepting that approximate answers are acceptable given modern computational tools.

**Supporting Evidence and Prescriptions:**

**On Abandoning Frequentism:**
- The frequency interpretation doesn't work for rare events, past events, or one-time events (the "probability the election is already decided" cannot be a frequency)
- The reference class problem makes supposedly objective frequentist probabilities as judgment-dependent as Bayesian priors
- The notation P(A|X) should replace P(A) everywhere—all probability is conditional

**On Abandoning Eugenics Terminology:**
- "Standard deviation" → "uncertainty"
- "Variance/covariance" → "second central moment"
- "Linear regression" → "linear modeling"
- "Significant difference" → not applicable; report a full probability distribution
- "Unbiased estimator" as a normative ideal → meaningless if what we care about is inference from a single dataset

**On Bayesian Inference:**
- Prior probabilities are unavoidable. Refusing to state them doesn't eliminate them; it conceals them.
- Pre-registration of priors (analogous to pre-registration of methods) is possible and would expose motivated reasoning
- Cox's theorem guarantees that any internally consistent set of plausibilities satisfying common-sense constraints can be rescaled to satisfy the probability axioms—the logical structure is not optional
- Bayes factors as a "friendly middle ground" for those uncomfortable with stated priors

**On Approximation:**
- Modern computational methods (MCMC, Stan, R) make previously intractable Bayesian calculations routine
- Exact answers are not required; Bayesian inference with approximate posteriors is more honest than exact answers from the wrong framework
- Overfitting is automatically controlled by Bayesian inference: more parameters require more data before posterior distributions narrow, and the posterior widths communicate remaining uncertainty

**Logical Gaps:**
- The call to "abandon frequentism and its terminology" underestimates the institutional inertia documented in the chapter. The prescription is correct but the book provides no theory of how the change happens.
- The claim that eliminating significance testing would eliminate the replication crisis conflates the statistical methodology with the incentive structure. Publication pressure, career advancement, and funding create demand for positive results; Bayesian methods with pre-registered priors would still be subject to manipulation.
- The proposed terminology replacements ("linear modeling" instead of "linear regression") are sensible but do not address the eugenics legacy argument made in Chapter 4, which was about scientific authority rather than vocabulary.

**Methodological Soundness:** The prescriptions are technically correct and consistent with the argument developed across the book.

---
