### CHAPTER 2: Neural Networks and the Ascent of Machine Learning

**Core Claim:** Multi-layer neural networks trained via back-propagation—the approach Minsky and Papert dismissed as likely sterile—became the foundation of modern AI, but only after decades of dormancy due to insufficient data and compute. The perceptron's architecture, including the key distinction between symbolic and sub-symbolic AI, remains essential scaffolding for understanding everything that follows.

**Supporting Evidence:**
- Frank Rosenblatt's perceptron: each unit sums weighted inputs and fires above a threshold, inspired by McCulloch-Pitts neurons; perceptron learning algorithm adjusts weights on errors
- Demonstration: a two-layer neural network with 50 hidden units achieves 94% accuracy on handwritten digit recognition vs. 80% for a simple perceptron—same data, same task
- The connectionist revival of the 1980s (Rumelhart and McClelland's *Parallel Distributed Processing*) and the key insight: knowledge in sub-symbolic systems resides in weighted connections, not human-interpretable rules
- The 1980s DARPA AI official declares neural networks "more important than the atom bomb"—another premature proclamation

**Logical Method:** Technical exposition embedded in narrative. Mitchell makes the architecture tangible through the eight-detector example (18×18 pixel grid → 324 inputs → perceptron output) before generalizing.

**Logical Gaps:**
- The transition from "perceptron learning algorithm works" to "back-propagation works for multi-layer networks" is described as having occurred in the late 1970s and early 1980s, but Mitchell is appropriately circumspect about the mechanism: why did this work when applied at scale? The answer (it usually doesn't without enormous data and compute) is deferred to later chapters.
- The symbolic vs. sub-symbolic distinction is framed as an unresolved philosophical debate, which it is, but the chapter does not yet flag the most important asymmetry: symbolic systems are interpretable; sub-symbolic systems are not. That becomes a central problem in Chapter 7.

**Methodological Soundness:** The perceptron as concrete worked example is pedagogically sound and technically accurate.

---
