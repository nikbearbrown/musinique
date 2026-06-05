### CHAPTER 7: The Great Kernel Trick
**Core Claim:** Support Vector Machines (SVMs) find the *optimal* linearly separating hyperplane (maximum margin), and the kernel trick allows this to be done in infinite-dimensional spaces without ever computing in those spaces.

**Supporting Evidence:**
- Vapnik's 1964 optimal margin classifier: minimizes ||w||²/2 subject to yi(w·xi + b) ≥ 1 for all training points; solved via Lagrange multipliers
- Support vectors: only data points on the margin margins affect the hyperplane; all alphas for other points are zero
- Kernel trick: k(a,b) = φ(a)·φ(b), where φ maps to higher dimensions; one can compute the dot product in high-dimensional space using only low-dimensional inputs
- RBF kernel: k(a,b) = exp(-||a-b||²/2σ²); equivalent to dot product in *infinite*-dimensional space; universal function approximator
- Isabelle Guyon's insight (1991): instead of explicitly constructing high-dimensional features, replace all dot products in Vapnik's algorithm with kernel evaluations

**Logical Method:** Perceptron limitation → optimal margin formalization → Lagrangian analysis → kernel extension → infinite-dimensional universality.

**Logical Gaps:**
- The Lagrange multiplier derivation is the most technically dense section in the book. The author provides the setup correctly (minimize ||w||²/2 subject to margin constraint) but the derivation of why the support vectors suffice—that alphas for non-support-vector points are zero—is stated as a "key insight arising from the mathematical analysis" without showing the step. Readers who do not already know this result cannot verify it.
- The claim that "in infinite-dimensional space, you can always find a separating hyperplane" is stated but not qualified. The existence of a separating hyperplane in an RKHS depends on the kernel and the data; it does not hold in pathological cases. The claim is broadly true for the RBF kernel given the data it is trained on, but "always" overstates.

**Methodological Soundness:** SVMs are mathematically well-understood. The kernel trick derivation, while abbreviated, is directionally correct. The chapter accurately attributes authorship (Boser, Guyon, Vapnik; Cortes-Vapnik soft margin).

---
