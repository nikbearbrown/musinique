### CHAPTER 2: We Are All Just Numbers Here
**Core Claim:** Vectors and the dot product provide the geometric language for understanding what a Perceptron actually does: it finds a weight vector orthogonal to a hyperplane that divides data into two classes.

**Supporting Evidence:**
- Hamilton's 1843 discovery of quaternions as historical origin of the terms scalar and vector
- Dot product geometric interpretation: for a unit vector, dot product with any vector equals the projection of that vector onto the line defined by the unit vector
- Formal vector notation for Perceptron: output = sign(w^T x), where w is weight vector and x is data vector
- Minsky-Papert convergence proof: establishes upper bound on number of updates needed before finding linearly separating hyperplane
- XOR problem: single-layer Perceptron cannot solve it—data not linearly separable in two dimensions

**Logical Method:** Mathematical formalization → geometric interpretation → proof sketch → refutation of single-layer sufficiency.

**Logical Gaps:**
- The convergence proof is described elegantly but the author's chosen level of detail leaves its central move (the dot product of W and W* increasing faster than W dot W) as assertion rather than derivation. Readers are told to trust the proof structure without being able to verify its key step. This is an appropriate pedagogical tradeoff but should be flagged.
- The XOR problem is presented as Minsky-Papert's "first big chill" to the field, but the author does not immediately distinguish between *proving single-layer perceptrons cannot solve XOR* and *claiming multi-layer networks also cannot*. The second claim was not proved; it was *conjectured*. Ananthaswami returns to this distinction in Chapter 10 with Hinton's critique. The deferral is narratively clean but creates a gap here.

**Methodological Soundness:** The math is accurate. The proof structure is correct. The chapter's claim that Minsky-Papert's results were "devastating" is historically documented and not overstated.

---
