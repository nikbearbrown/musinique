### CHAPTER 1: Desperately Seeking Patterns
**Core Claim:** Machine learning is the algorithmic discovery of correlations between inputs and outputs in labeled data; the Perceptron is the first device that could learn such correlations from data rather than having them hard-coded.

**Supporting Evidence:**
- Konrad Lorenz's duckling imprinting as biological precedent for pattern learning
- McCulloch-Pitts (1943) neuron model as first computational neuron—can implement Boolean logic but cannot learn its threshold theta from data
- Rosenblatt's Mark I Perceptron (1958): learned to recognize letters of the alphabet by being updated on errors; trained on 400 inputs (20×20 pixel image)
- Perceptron convergence theorem (proven by Block, Minsky-Papert): algorithm will always find a linearly separating hyperplane in finite time *if one exists*
- House price example: y = w1x1 + w2x2 illustrates supervised regression as foundational ML operation

**Logical Method:** Biological analogy → computational model → algorithmic learning → convergence proof.

**Logical Gaps:**
- The author describes Rosenblatt's key achievement as learning from data, then immediately notes that commercially available optical character recognition systems could already recognize letters by the mid-1950s. The distinction being argued—that the Mark I *learned* to recognize letters rather than being *programmed* to—is real, but the author does not fully develop why this distinction matters for capability rather than just for method.
- The convergence proof is described as guaranteeing a solution "if the data are linearly separable." This conditional is introduced but its significance—that much real-world data *is not* linearly separable—is not yet flagged as a problem. That tension is deferred to Chapter 2 (XOR). The logical structure is correct; noting it as deliberate narrative architecture.

**Methodological Soundness:** Strong. Mathematical claims (y = w1x1 + w2x2, convergence) are accurate and appropriately scoped.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-desperately-seeking-patterns.md`

Key additions: The perceptron is best taught as a linear classifier whose convergence theorem is conditional: it learns a separator if one exists. That conditional is the conceptual bridge to XOR and later model-limit chapters.

Settled: Linear separability is the core limitation of a single-layer perceptron. Nuanced: simplified histories overstate XOR as the sole cause of the AI winter.

Teaching move: Plot AND, OR, and XOR on a 2D grid and make students physically try to separate the labels with one line.
