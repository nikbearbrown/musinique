### CHAPTER 3: From Evidence to Causes — Reverend Bayes Meets Mr. Holmes

**Core Claim:** Bayesian networks are the computational infrastructure that allows machines to reason under uncertainty, and they represent the closest existing approximation to how the human brain processes evidence. But Bayesian networks, as originally conceived, cannot answer causal questions — they confuse the causal direction with the statistical direction. They are, as Pearl says, Wrong 1 machines.

**Supporting Evidence:**
- Bonaparte DNA identification software for MH17: 294 of 298 victims identified using Bayesian networks
- Turbo codes in cell phones: belief propagation independently discovered by engineering, validating the algorithm's generality
- The three junction types (chain, fork, collider) as sufficient to characterize all conditional independence patterns in any network
- Mammogram example: P(cancer | positive test) ≈ 1/116 for a 40-year-old woman, contrary to most patients' intuitions

**Logical Method:** Historical narrative + formal exposition + worked examples. The chapter makes the strongest possible case for Bayesian networks before demonstrating their limitation.

**Logical Gaps:**
- The mammogram calculation is internally consistent but uses specific prior and likelihood values from the BCSC. The point is valid; the specific numbers are contingent on population.
- Pearl claims that Bayesian networks "cannot tell what the causal direction is" — but this conflates the network's statistical properties with its causal content. A Bayesian network *drawn* causally (arrows from causes to effects) does encode causal structure. Pearl's real point is that the arrows' causal content isn't enforced by the mathematics.
- The claim that "conditional independence gives the machine a license to focus on relevant information and disregard the rest" implies robustness that only holds if the model is correct.

**Methodological Soundness:** The Bayesian network exposition is technically accurate. The three junction types (chain, fork, collider) are a genuine theoretical contribution. The transition from "Bayesian networks are great" to "Bayesian networks are insufficient for causation" is the chapter's real payoff.

---
