### CHAPTER 3: The Bottom of the Bowl
**Core Claim:** Gradient descent—specifically Widrow and Hoff's Least Mean Squares (LMS) algorithm—provides the first practical method for training an adaptive neuron using calculus rather than hard-coded convergence logic.

**Supporting Evidence:**
- Rice paddy terrace analogy for gradient descent: find steepest path down from any starting point
- Derivative of y = x² equals 2x; gradient descent update: x_new = x_old - η × gradient
- Widrow-Hoff (1959) LMS algorithm: estimate gradient from a *single* data point rather than computing the full expectation; update rule: w_new = w_old + η × error × input
- Widrow's admission: "You take the single value of the error squared, swallow hard because you are going to tell a lie and you say that's the mean squared error"
- LMS algorithm is the basis of every modem ever made and ancestor of modern neural network training algorithms

**Logical Method:** Physical analogy → calculus formalization → approximation argument → empirical validation.

**Logical Gaps:**
- The Widrow-Hoff update rule is presented as "it works" via anecdote (Hoff running it on an analog computer in half an hour). The theoretical justification—that under sufficiently small step sizes, the stochastic approximation converges to the true minimum—is mentioned only in passing (Widrow's insight "on a United Airlines ticket"). The reader is left with the empirical fact of convergence but not the theoretical basis for when and why it holds.
- The distinction between the LMS algorithm (for adaptive filters) and the perceptron convergence procedure (for classification) is introduced but not crisply drawn. Both are gradient-like update rules, but they optimize different objectives (minimum squared error vs. linearly separable boundary). The book conflates them pedagogically without noting the conflation—a choice that aids narrative flow but papers over a meaningful distinction.

**Methodological Soundness:** The chapter is honest about the approximation being made ("tell a lie"). The core claim—that LMS is the ancestral algorithm for training neural networks—is historically accurate.

---
