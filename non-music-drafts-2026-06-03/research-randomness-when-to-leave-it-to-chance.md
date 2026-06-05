### CHAPTER 9: Randomness — When to Leave It to Chance

**Core Claim:** Randomized algorithms solve important problems that deterministic algorithms cannot solve efficiently. The Monte Carlo method, the Miller-Rabin primality test, and simulated annealing all use randomness not as a fallback but as a deliberate and theoretically justified strategy. Hill climbing with random restarts or jitter, and the metropolis algorithm, are practical tools for escaping local optima in optimization problems.

**Supporting Evidence:**
- Stan Ulam: Monte Carlo method (1946) applied to nuclear physics; solitaire win probability the motivating thought experiment
- Miller-Rabin primality test: probabilistic; after 40 applications, probability of false prime < 1 in 10^24; used in all modern cryptography (every HTTPS connection)
- AKS deterministic primality (2002): exists but Miller-Rabin is still used because randomized is faster
- Polynomial identity testing: no known efficient deterministic algorithm; randomized sampling provides practical solution
- Give Directly charity: random recipient stories published verbatim—Monte Carlo sampling for donor transparency
- Simulated annealing (Kirkpatrick et al., 1983, *Science*, 32,000 citations): maps physical annealing process to optimization; starts hot (random), cools gradually toward pure hill climbing; outperformed IBM's best chip layout expert
- Raw data: Luria's 1943 slot machine observation → bacterial mutation experiment → Nobel Prize
- Jorge Cockcroft's lived experiment with dice: annealing schedule eventually converged to a stable local maximum (lake house in upstate New York)

**Logical Method:** Formal algorithm analysis (Miller-Rabin false positive rate) + historical case (simulated annealing scientific validation) + biological parallel (Luria) + philosophical argument (randomness as anti-local-maximum device).

**Logical Gaps:**
- The Miller-Rabin treatment is correct but the implication ("you are never fully certain") is presented somewhat paradoxically against the book's overall thrust of algorithmic confidence. The book uses this uncertainty to endorse probabilistic algorithms, but doesn't distinguish between tolerable uncertainty (10^-24 error rate in cryptography) and intolerable uncertainty (similar error rates in medical diagnosis).
- The simulated annealing temperature schedule—the most critical implementation parameter—is discussed qualitatively. In practice, finding the right annealing schedule is an unsolved sub-problem; the book implies it's simply a matter of starting hot and cooling slowly without addressing this.
- "Introduce randomness into your life" (Wikipedia random article, CSA boxes, oblique strategies) follows conceptually from local-maxima theory but the book doesn't examine the possibility that one's life is already well-optimized and random perturbations are costly. Not every life is stuck in a poor local maximum.
- The Rawls/veil of ignorance section, while intellectually interesting, drifts significantly from the chapter's algorithmic content. The claim that Monte Carlo sampling solves the computational problem of evaluating policy proposals is a very long inferential leap that is not formalized.

**Methodological Soundness:** The formal algorithm content (Miller-Rabin, simulated annealing) is rigorous. The prescriptive lifestyle applications are speculative but intellectually stimulating.

---
