### CHAPTER 8: Counterfactuals — Mining Worlds That Could Have Been

**Core Claim:** Counterfactuals — the third rung of the ladder — can be computed algorithmically from structural causal models using a three-step procedure (Abduction, Action, Prediction). The Rubin causal model's potential outcomes framework captures counterfactuals but without causal diagrams is navigated blind, unable to test assumptions or identify ignorability.

**Supporting Evidence:**
- Alice/salary example: structural equations predict Alice's counterfactual salary under hypothetical education level, revealing that matching on experience (Bert vs. Caroline) produces wrong answers because experience is a mediator, not a confounder
- But-for causation and probability of necessity (PN): firing squad, falling piano examples
- Climate change: Hannart's analysis of 2003 European heat wave, P(necessity) = 0.9 for greenhouse gases; P(sufficiency) for a 200-year window = 80%
- Potential outcomes' limitation: ignorability is "usually made because it justifies available statistical methods, not because it is truly believed" (Jaffe, cited)

**Logical Method:** Formal definition of counterfactuals via structural models + critique of the Rubin approach + worked applications in law and climate.

**Logical Gaps:**
- The salary example requires fully specified linear structural equations. Pearl acknowledges that in practice models are "partially specified," but the three-step procedure's power depends on knowing the functional form. The climate example uses a simulation model, not structural equations estimated from data — this is a somewhat different epistemic situation.
- The critique of Rubin is pointed and largely accurate on the ignorability problem. But Rubin's defenders would argue that potential outcomes and structural models are mathematically equivalent (which Pearl acknowledges) and that the choice is pedagogy, not epistemology.
- PN and PS for climate: Pearl presents Hannart's numbers (PN = 0.9, PS = 0.0072) as if they are measurements. They are model outputs. The model is a climate simulation with millions of lines of code — a complex response function accepted on faith that it correctly represents climate dynamics.

**Methodological Soundness:** The three-step (abduction/action/prediction) procedure is formally correct. The climate PN/PS analysis is directionally sound even if the numbers are model-dependent. The critique of Rubin is fair.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-counterfactuals-mining-worlds-that-could-have-been.md`

Key additions: counterfactuals require a causal model. Abduction, action, prediction is formally clean, but climate and legal applications depend on model specification, assumptions, and communication of PN/PS/PNS distinctions.

Settled: SCMs provide a formal counterfactual calculus. Contested: model specification, functional-form assumptions, and how to communicate attribution probabilities.

Teaching move: specify whether a claim is about necessity, sufficiency, or probability of necessity and sufficiency.
