### CHAPTER 2: The Titular Fallacy

**Core Claim:** Bernoulli's law of large numbers—his "golden theorem"—was mathematically correct but was used to support a logically invalid inference: that sampling probabilities are sufficient for probabilistic inference about hypotheses. This is "Bernoulli's fallacy."

**Supporting Evidence:**

**The Technical Error:** Bernoulli's theorem establishes:
> *For all f, P(|sample ratio - f| < ε | F = f) is high for large N.*

This is a statement about the probability of the sample *given* the urn fraction. The inference Bernoulli wanted to make is:
> *For observed sample ratio s, P(|F - s| < ε | S = s) is high.*

These are not the same statement. The arrow points in opposite directions. The second requires a prior probability distribution over F.

**The Candy Factory Proof of Failure:**
- Two-hypothesis problem: bin fraction is either 1/3 or 2/3
- Prior: 0.01% chance of mix-up (so 99.99% prior probability that fraction is 2/3)
- Observed sample: 8 green out of 30 (consistent with 1/3 fraction)
- Bernoulli's conclusion: 97% confident the fraction is between 10% and 43%
- Bayesian conclusion: ~62% posterior probability the fraction is 1/3 (depending on exact priors)
- The Bernoulli answer is not just wrong—it is massively wrong in the direction that matters

**When Bernoulli Is Right:**
- With uniform prior over F (total ignorance), Bayesian and Bernoulli inferences converge
- This explains why the fallacy seemed right for the urn problems Bernoulli was considering
- The fallacy surfaces when strong prior information exists—exactly the situation in real science

**Real-World Instances:**
- The Sally Clark case: prosecution computed P(2 SIDS deaths | family characteristics) ≈ 1/73 million. The relevant probability was P(murder | 2 infant deaths), which requires a prior for murder rates. Clark was wrongfully convicted.
- Medical testing: a test with 1% false positive rate does not imply 99% probability of disease given positive test. If disease prevalence is 1 in 10,000, most positives are false positives.

**Logical Gaps:**
- The author correctly distinguishes the two probability statements but presents the distinction as Bernoulli's failure rather than as an institutional failure of the generations that followed him. Bernoulli was writing before conditional probability notation existed (Bayes published posthumously in 1763; Bernoulli died in 1705). The criticism applies more sharply to 20th-century frequentists who had access to Bayes's theorem.
- The "candy factory" example requires strong asymmetric prior information to make the fallacy visibly wrong. The text could be more explicit that the fallacy is invisible—not merely small—when priors are weak.

**Methodological Soundness:** The proof of the fallacy via the candy factory example is rigorous and decisive. The legal and medical examples are well-documented real cases.

---
