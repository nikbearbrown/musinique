### CHAPTER 10: Big Data, Artificial Intelligence, and The Big Questions

**Core Claim:** Big data without causal models cannot answer causal questions, but causal models + big data together open up transportability (can results from Boston be applied in Arkansas?), recovery from selection bias, and eventually strong AI. Strong AI requires the do-calculus, counterfactual reasoning, and something functionally equivalent to free will — the ability to observe one's own intent and act differently.

**Supporting Evidence:**
- Transportability framework (Pearl & Barranboim): complete criterion for when study results can be transported to new populations, proven via do-calculus
- AlphaGo: works in the narrow domain of Go (which has an adequate causal model built in: the rules of the game) but cannot explain its own play or communicate about its reasoning
- The vacuum cleaner example: "You shouldn't have woken me up" requires a machine to understand cause, effect, intent, and counterfactual
- Free will as functionally valuable illusion: robot teams that communicate "as if" they have free will would play better soccer

**Logical Method:** Argumentative extrapolation from established results to future possibilities. More speculative than prior chapters.

**Logical Gaps:**
- The transportability results are proven for the case where we have correct causal diagrams of both environments. In practice, we rarely know the causal structure of a new environment. The algorithm is complete given the model; the model is the hard part.
- The strong AI argument is largely visionary. Pearl does not demonstrate that the three-component software package (causal model of world, causal model of self, memory of intents) is sufficient for human-like reasoning — only that it is necessary.
- The free will discussion is philosophically engaged but doesn't resolve the hard problem. Pearl's compatibilism is stated as a position, not argued from first principles.

**Methodological Soundness:** Transportability and selection bias recovery are proven results. The strong AI and free will sections are thoughtful speculation, appropriately labeled as such.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-big-data-artificial-intelligence-and-the-big-questions.md`

Key additions: big data is not causal knowledge. Transportability and selection-bias recovery are powerful only when the causal model and selection assumptions are credible. The strong-AI/free-will discussion should be framed as necessary ingredients for richer agency, not a demonstrated sufficient architecture.

Settled: prediction, intervention, and counterfactual explanation are different tasks. Contested: whether causal modeling is the central missing ingredient for general AI or one ingredient among representation, embodiment, memory, planning, and social learning.

Teaching move: contrast predicting who takes medicine with estimating what medicine would do if assigned.
