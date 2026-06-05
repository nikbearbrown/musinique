### CHAPTER 17: AI AS DATA POINT

**Core Claim:** AI occupies a novel shape in cognitive space—not a rung on the biological ladder but an entry on the extension-technology shelf. The shape is characterized by extreme Rung 1 capacity and near-zero Rung 2 and 3 capacity, no stakes, and no embodiment. The Geirhos texture-bias result and the Ullman perturbation result are the cleanest diagnostics: benchmark accuracy and underlying computation have come apart.

**Supporting Evidence:**
- Geirhos et al. 2018 texture-bias in ImageNet networks
- Yamins & DiCarlo CNN top-layer IT neuron prediction
- Ullman 2023 false-belief perturbation failures in GPT-4
- Frontier model calibration improvements (GPT-3.5 to GPT-4) acknowledged but not treated as evidence of genuine metacognition
- Hampton cross-check for metacognition proposed as the appropriate test

**Logical Gaps:**
- The "stakes absent" argument is the chapter's most original contribution and its most philosophically ambitious claim. The claim is that the absence of evolutionary stakes produces a structurally different kind of Rung 1 system—one that optimizes the training distribution without having been shaped by the cost of getting the world wrong. This is compelling. But the chapter does not address whether gradient descent on a loss function that approximates the consequences of real-world errors is meaningfully different from evolutionary selection—both are optimization processes with external feedback, differentiated primarily by timescale and directness of consequence.
- The "novel shape" argument—that AI is neither a rung on the biological ladder nor a gap—is asserted rather than demonstrated. The argument would be stronger with an explicit comparison: what would it look like if AI *were* a rung, and how do the data distinguish the two readings?
- The claim that AI is "extreme high on in-distribution pattern detection at scale, dropping sharply under distribution shift" is correct but understates the degree to which the drop is domain-specific. Medical imaging systems trained on specific imaging protocols degrade very differently from language models under perturbation. The uniform characterization papers over important variation.

**Methodological Soundness:** Good. The Geirhos and Ullman diagnostics are the chapter's most important empirical contributions.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-ai-as-data-point.md`

Key additions: AI should be framed as an engineered cognitive artifact, not a biological rung. Benchmark success can hide nonhuman strategies. Texture-bias and false-belief perturbation studies are diagnostic because they separate performance from mechanism. The "stakes absent" argument should compare gradient descent and evolutionary selection explicitly.

Settled: AI systems can solve tasks via nonhuman strategies; distribution shift matters; benchmarks are incomplete evidence. Contested: texture-bias interpretation, LLM theory-of-mind robustness, and artificial/biological cognition comparisons.

Teaching move: compare two systems with equal accuracy but different cues, then ask what perturbation reveals the strategy.
