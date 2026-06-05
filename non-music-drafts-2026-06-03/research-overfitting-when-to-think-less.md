### CHAPTER 7: Overfitting — When to Think Less

**Core Claim:** Complex models that fit observed data better will generalize worse when data is noisy, small, or an imperfect proxy for what matters. Regularization—penalizing complexity—and early stopping improve predictive performance. The same principle applies to human decision-making: thinking harder, considering more factors, and pursuing perfection can produce worse outcomes than thinking less. Heuristics can be rational.

**Supporting Evidence:**
- German marriage satisfaction data: one-factor model (time) generalizes better than nine-factor model (which fits data perfectly but makes absurd predictions)
- Lasso regularization (Tibshirani 1996): penalizes sum of factor weights, driving irrelevant factors to zero
- Markowitz paradox: Nobel Prize winner in portfolio optimization used 50/50 stocks/bonds for his own portfolio because uncertainty in parameter estimates makes the formal optimization less reliable than the heuristic
- DeMiguel et al. study: 1/N heuristic (equal allocation) outperforms mean-variance optimization across datasets due to estimation error
- Brain's ~20% of caloric intake: metabolic cost as natural regularization against neural complexity
- Early stopping in machine learning: stopping the fitting process before convergence prevents overfitting; corresponds to Darwin's diary-page constraint on deliberation
- Riddgeway (1956): performance metrics create gaming—placement firms optimize interviews per day at expense of actual placements; factories neglect maintenance for production quotas
- Police training scars: reflexive behavior from drilling can kill (spent casings in pocket, automatic holstering after two shots)
- Gigerenzer and Brighton: "less information, computation, and time can improve accuracy"—fast-and-frugal heuristics literature

**Logical Method:** Machine learning formalism + behavioral experiments (Markowitz paradox, portfolio allocation studies) + cross-domain analogy (sports, military training, corporate incentives).

**Logical Gaps:**
- "Think less to decide better" is an important insight but requires specification: less thinking than *what* baseline? The book establishes that 9-factor models overfit, but does not provide operational guidance on when to stop adding factors for a given problem.
- Early stopping is an optimal strategy when complexity increases monotonically with time. If thinking non-linearly improves (sometimes you need to think longer to get a breakthrough), early stopping fails. The book does not address this.
- The Gigerenzer/Brighton "less is more" research has been contested in the cognitive psychology literature (Newell and Shanks critique, 2003; Shanteau et al.); the book presents it as settled when it is not.
- The training scars examples (police reflexes) are compelling anecdotes but the prescriptive implication—"don't practice too specifically"—is in direct tension with the extensive literature on deliberate practice (Ericsson), which emphasizes highly specific drilling. The book does not address this tension.
- The Markowitz paradox is genuine, but concluding "heuristics beat formal optimization" in finance is too strong. The DeMiguel study covers limited estimation windows; in long-horizon portfolios with better parameter estimates, mean-variance optimization may dominate.

**Methodological Soundness:** The machine learning formalism (overfitting, regularization) is rigorous. The behavioral applications are selectively presented; the literature is more contested than the chapter suggests.

---
