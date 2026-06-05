### BRIDGE: THE LOGICAL ARCHITECTURE OF THE BOOK

**The book's central thesis:** Human intelligence and its distinctive features are the cumulative product of five evolutionary breakthroughs, each made possible by the prior breakthrough, each representing a specific computational solution to a specific survival problem. AI has recapitulated breakthrough 2 (TD learning), partially breakthrough 3 (generative models), but has not yet achieved breakthrough 4 (mentalizing) or breakthrough 5's genuine form.

**Three master tensions:**

*Tension 1: Description vs. Prescription.* Bennett's framework is evolutionary and descriptive—he reconstructs what happened. But his use of the framework to evaluate AI treats the evolutionary path as normative—as if the way brains evolved these capacities is the right or only way to achieve them. An AI that achieves planning without a hippocampus, or mentalizing without a GPFC, would not refute the evolutionary account but would refute the design prescription. Bennett does not draw this distinction.

*Tension 2: Five Clean Breakthroughs vs. Messy Biology.* The five-breakthrough framework is pedagogically powerful but imposes retrospective clarity on a process that was neither clean nor linear. Birds independently evolved simulation; arthropods independently evolved some reward-prediction error signals; cephalopods independently evolved episodic memory. The framework is explicitly an approximation—but the substantive chapters consistently present it as more than that.

*Tension 3: What LLMs Can and Cannot Do.* The book's core practical argument—that LLMs lack world models and mentalizing—is well-motivated but temporally unstable. The argument was written when GPT-3 failed on the basement question; by publication, GPT-4 passed it. The deeper claim (scale cannot compensate for architectural gaps) may be right, but the specific evidence keeps moving.

**The book's most proven claims:**
- Dopamine functions as a TD error signal (one of the most replicated findings in computational neuroscience)
- The vertebrate brain template is conserved from lamprey to human
- Nematode valence, affect, and associative learning are implemented in ancient, phylogenetically conserved mechanisms
- Berridge: dopamine = wanting, not liking
- Hippocampal place cells in rats replay future path sequences during decision points

**The book's most undervalidated claims:**
- The gossip-altruism feedback loop as the origin of language
- Theory of mind is *necessary* (not just *sufficient*) for primate imitation learning of novel skills
- Scale cannot close the gap between LLMs and human-level language understanding
- The specific mechanisms by which warm-bloodedness enabled the neocortex

**The book's most important acknowledged gaps:**
- How fish avoid catastrophic forgetting is "not understood"
- How the neocortical microcircuit implements a generative model is "still a mystery"
- The exact evolutionary path of language emergence "may never be known"
- Whether any non-mammalian animals have genuine episodic memory remains contested

---

## Extended Research Notes

**Pantry note:** `pantry/notes-bridge-the-logical-architecture-of-the-book.md`

Key additions: keep the evolutionary sequence descriptive rather than prescriptive. AI systems may achieve similar functions through non-biological architectures. Static LLM failure examples age quickly; grounding, agency, mentalizing, and robustness tests are more durable.

Settled: brains contain mechanisms analogous to reinforcement learning and predictive/generative processing. Contested: whether current AI lacks essential architecture or mainly lacks interaction, embodiment, memory, and task grounding.

Teaching move: for each breakthrough, ask what function biology solved and what non-biological architecture could solve the same function differently.
