### CHAPTER 5: The "Logic" of Orthodox Statistics

**Core Claim:** The standard statistical toolkit—null hypothesis significance testing, p-values, confidence intervals, maximum likelihood estimation—fails logically in a series of demonstrable cases that expose how each method attempts to derive inferential conclusions from sampling probabilities alone.

**Supporting Evidence — Nine Problem Cases:**

**1. Base Rate Neglect / Prosecutor's Fallacy**
Orthodox statistics formally endorses rejecting the null hypothesis of "not diseased" when a test positive (1% false positive rate) is observed. But for rare diseases, most positives are false positives. The rejected null may be correct. Demonstrated for Sally Clark's case and medical testing.

**2. The Malfunctioning Digital Scale**
A scale that adds 100 kg 0.1% of the time produces a reading of 100,001 grams. Orthodox significance testing rejects the hypothesis "mass = 1 gram" at any reasonable significance level. But the correct inference is "the scale malfunctioned." Prior knowledge about the scale's known failure mode cannot enter the frequentist framework.

**3. The Sure-Thing Hypothesis**
A stranger claims a die was predetermined to produce the exact observed sequence of 60,000 rolls. Under this hypothesis, the data is certain (probability 1). The maximum likelihood method—using only sampling probabilities—would endorse this claim over any hypothesis that makes the data merely probable. Only prior probability kills the sure-thing hypothesis; frequentism cannot.

**4. Optional Stopping**
Bill's analysis of an experiment yielding 5 successes in 6 trials gives p = 0.109 (not significant). Charlotte's interpretation of the same data—that the experimenter would have continued until equipment failure—yields p = 0.031 (significant). Same data. Same experiment. Different inference. The difference traces entirely to what "more extreme data" was assumed possible, which is irrelevant to the Bayesian inference.

**5. Divided Data**
Two labs independently test Mozart's Violin Concerto No. 5 on mice. Each finds a non-significant result. Combined, their data would have been significant. The binary yes/no structure of significance testing destroys information that Bayesian updating would preserve.

**6. The German Tank Problem**
Given 4 observed serial numbers with maximum = 313, the unbiased estimator gives ~390 tanks. But the natural 95% confidence interval (using the right tail as rejection region, to guard against underestimation) runs from 318 to *infinity*—a useless result. The choice of which tail region constitutes "extreme" data is arbitrary and not determined by the data itself. Bayesian inference produces a clear posterior distribution.

**7. Testing for Independence (Contingency Tables)**
Omitted from the summary but established through discussion: the choice of test statistic and tail region for a contingency table requires implicit assumptions about alternatives that frequentism cannot formally accommodate.

**8-9.** Additional examples involving regression and model selection.

**The Superfreak Dialogue:**
The chapter includes an extended Socratic dialogue between a student (Jackie Bernoulli) and a statistics AI (Superfreak), which demonstrates in detail the internal inconsistencies of confidence interval interpretation and why users cannot legitimately say "95% probability the true value is in this interval."

**Logical Gaps:**
- The nine "horribles" are deliberately extreme to make the failure modes visible. A practicing scientist could reasonably object that most real problems don't involve sure-thing hypotheses or malfunctioning scales, and that for normal research problems the frequentist methods work adequately.
- The text's demonstration that Fisher's maximum likelihood is secretly Bayesian with uniform priors should lead to a stronger conclusion: frequentist methods are a degenerate case of Bayesian inference, not a separate system. This reframing would strengthen the argument.
- The optional stopping example's conclusion—that Bayesian inference makes stopping rules irrelevant—is true in theory but requires careful verification in practice. The text is correct but the claim sounds stronger than practitioners might accept without more worked examples.

**Methodological Soundness:** Each example is technically correct. The Superfreak dialogue is an unusually effective pedagogical device for exposing confidence interval confusion.

---
