### CHAPTER 4: Confounding and Deconfounding — Slaying the Lurking Variable

**Core Claim:** Confounding is a causal concept, not a statistical one, and therefore the century-long effort to define and solve it using purely statistical methods was doomed from the start. The backdoor criterion, derived from causal diagrams, provides the first complete and operational solution to the confounding problem.

**Supporting Evidence:**
- The Daniel experiment (oldest controlled experiment) as illustration of confounding awareness before statistical vocabulary
- The walking study (Abbott 1998): casual walkers have 2x death rate over 12 years, but researchers decline to make causal claims after controlling for confounders
- RCT as "skillful interrogation of nature" via Joan Fisher-Box quotation
- The five backdoor "games" (Weinberg's examples + Forbes' asthma example) demonstrating how causal diagrams uniquely identify what to control for
- M-bias as proof that controlling for a pre-treatment variable can introduce bias

**Logical Method:** Conceptual + operational. Pearl shows the inadequacy of traditional definitions (declarative and procedural), then provides the backdoor criterion as a complete replacement.

**Logical Gaps:**
- The backdoor criterion requires a correct causal diagram. If the diagram is wrong — wrong edges, missing variables — the criterion gives the wrong answer. Pearl acknowledges this but doesn't dwell on it.
- M-bias: Pearl claims the seat belt example illustrates this in real data. The claim is plausible; it is not fully validated.
- The dismissal of "controlling for everything" is correct in principle but doesn't address the legitimate concern of researchers who simply don't know which variables to include. The backdoor criterion requires a model; most researchers don't have one.

**Methodological Soundness:** The backdoor criterion is mathematically proven (not just claimed). The five games are genuine worked examples. The critique of prior confounding definitions is historically accurate.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-confounding-and-deconfounding-slaying-the-lurking-variable.md`

Key additions: confounding is causal, not merely statistical. Backdoor adjustment works under a causal graph; colliders and M-bias show why controlling for everything can make bias worse.

Settled: graph-based criteria clarify adjustment under causal assumptions. Contested: how to build credible graphs in messy applied domains.

Teaching move: draw paths and mark whether each variable blocks, transmits, or opens association.
