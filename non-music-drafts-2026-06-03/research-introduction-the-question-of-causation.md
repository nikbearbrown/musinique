### CHAPTER 1: Introduction — The Question of Causation

**Core Claim:** Causal inference is fundamentally a problem of comparing potential outcomes in worlds that cannot both be observed. The question "did X cause Y?" for a single individual is insoluble; the question "does X cause Y, on average?" has a rigorous solution.

**Supporting Evidence:**
- George Washington's case: he was bled, he died. Whether bleeding caused his death is unknowable because we cannot observe the counterfactual world where he was not bled.
- The notation of potential outcomes (R_T and R_C for treated and control conditions) formalizes the comparison of two possible worlds for each individual.
- Kim and James thought experiment: even with a treatment group and a control group, naive comparison of two different people estimates no one's causal effect — it conflates person-level differences with treatment effects.
- The single fair coin flip over Kim and James is *unbiased* in expectation but useless in practice — either outcome yields the wrong answer.

**Logical Method:** Rosenbaum proceeds by progressive formalization: a historical case (Washington), a common-sense counterfactual, a notation system (Neyman-Rubin potential outcomes), and then a demonstration of why a control group alone is insufficient.

**Logical Gaps:**
- The chapter establishes that a control group is necessary but not sufficient without yet specifying what makes a control group adequate. The reader is left in suspense about the solution until Chapter 2.
- The casino-vs.-gambler analogy is deployed to suggest that repeated coin flips solve the estimation problem, but the chapter stops short of proving this. The argument is intuitive, not yet rigorous.
- The chapter asserts that for individual-level causal effects "this is and will remain a matter of speculation" without defending the asymmetry between population-level solvability and individual-level insolubility. The argument is correct but would benefit from more explicit treatment of what changes when you aggregate.

**Methodological Soundness:** The potential outcomes notation is a genuine methodological contribution, not just a pedagogical device. The chapter correctly identifies the fundamental identification problem. The Washington example is epistemically honest: it acknowledges that even had 18th-century physicians possessed the experimental habit of mind, the causal effect on Washington specifically would remain unknowable.

---
