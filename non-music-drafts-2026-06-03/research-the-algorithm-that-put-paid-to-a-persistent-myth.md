### CHAPTER 10: The Algorithm That Put Paid to a Persistent Myth
**Core Claim:** The backpropagation algorithm, combining the chain rule of calculus with gradient descent, provides a scalable method for training multi-layer neural networks—and the key insight is that it requires only differentiable activation functions and random (not symmetric) initial weights.

**Supporting Evidence:**
- Rosenblatt (1961): explicitly described "back-propagating error correction procedures" in *Principles of Neurodynamics*; recognized symmetry as a problem
- Rumelhart-Hinton-Williams (1986, Nature): published systematic demonstration; used sigmoid activation (differentiable) and random initial weights (breaks symmetry)
- Chain rule: ∂L/∂W1 = (∂L/∂ŷ)·(∂ŷ/∂a2)·(∂a2/∂z2)·(∂z2/∂W1); all quantities computed during forward pass
- Delta rule for single neuron: ΔW = η·(d-y)·x; gradient of MSE loss
- XOR solved: two-layer network with sigmoid neurons correctly classifies XOR data; architecture includes two hidden neurons

**Logical Method:** Historical genealogy → mathematical formalization → implementation → demonstrated application.

**Logical Gaps:**
- The chapter's central historical claim—that Minsky and Papert "killed" neural network research—is actively contested by the author quoting Hinton ("a con job"). But the author does not fully arbitrate between the two narratives. Did Minsky-Papert cause the AI winter, or did computational and data limitations? The evidence offered is anecdotal (Hinton's difficulty getting interviews in Britain). The causal question is left open.
- The symmetry problem and its fix (random initial weights) is one of the chapter's most important conceptual points, but it is introduced briefly and not returned to. The reader is told that random initialization breaks symmetry, which enables different hidden neurons to learn different features. Why this is true—that identical initial weights produce identical gradients and hence identical updates throughout training—is stated but not proven even informally.

**Methodological Soundness:** The chain rule derivation is accurate. The Rumelhart-Hinton-Williams paper is a documented landmark. Rosenblatt's Chapter 13 description of "back-propagating error correction" is a documented historical priority claim.

---
