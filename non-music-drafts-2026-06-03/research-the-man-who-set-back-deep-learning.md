### CHAPTER 9: The Man Who Set Back Deep Learning (Not Really)
**Core Claim:** A single hidden layer neural network with a sufficiently large number of sigmoid neurons can approximate any continuous function to arbitrary accuracy—the Universal Approximation Theorem (Cybenko 1989).

**Supporting Evidence:**
- Intuition via integral calculus: rectangles approximate area under curve; more rectangles → better approximation; sigmoidal neurons can each produce an approximately rectangular output
- Visual demonstration: 10 → 20 → 100 → 300 neurons progressively improve approximation of y = x²
- Cybenko's proof: reductio ad absurdum; assumes there exists a function not approximatable by single-hidden-layer sigmoid networks; derives contradiction
- Functions as vectors: function f(x) evaluated at N discrete points is a vector in N-dimensional space; as N→∞, functions become points in infinite-dimensional space
- Consequence: universal approximation does not prescribe architecture; it proves existence of a solution, not a method for finding it

**Logical Method:** Visual intuition → function-as-vector formalism → existence proof → scope qualification.

**Logical Gaps:**
- Cybenko's proof is described as a proof by contradiction but its specific steps—Jensen's inequality and the dominated convergence theorem—are mentioned by Peter Hart in passing (in the KNN context in Chapter 5) and not revisited here. The proof's logical core is asserted without reconstruction: "he started by assuming...and ended up showing that the proposition was false." This is correct as description but leaves the reader unable to interrogate the argument.
- The "set back deep learning" framing occupies much of the chapter's narrative. The claim is that Cybenko's result caused researchers to use single hidden layers when multiple hidden layers are empirically better. But the chapter does not establish that this theoretical result was actually causally responsible for that research behavior, as opposed to computational limitations (insufficient compute and data) being the more direct cause. This is acknowledged implicitly but not resolved.

**Methodological Soundness:** The Universal Approximation Theorem is a documented mathematical result. The caution about astronomical numbers of neurons required is from Cybenko's actual paper.

---
