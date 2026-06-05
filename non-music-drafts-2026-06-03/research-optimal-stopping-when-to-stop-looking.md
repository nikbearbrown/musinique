### CHAPTER 1: Optimal Stopping — When to Stop Looking

**Core Claim:** The mathematically optimal strategy for any sequential search problem with a single opportunity to commit is the "look-then-leap" rule: observe without committing for 37% of the search space, then immediately commit to the first option that exceeds all previously seen options. This strategy maximizes the probability of selecting the best option and applies to apartment hunting, hiring, dating, parking, and selling.

**Supporting Evidence:**
- Secretary Problem mathematics: the 37% rule yields exactly a 37% probability of selecting the best candidate from any pool size, vastly outperforming random selection (which yields 1/N probability)
- The symmetry result: the optimal strategy proportion and the probability of success both converge to 1/e ≈ 0.368
- Michael Trick applied the rule to his own dating life (ages 18-40; optimal leap point = 26.1); the application worked by his own account (he eventually married)
- Kepler's 11-woman courtship as a historical case of the "recall allowed" variant
- Full-information variant (when candidates can be ranked absolutely): 58% success rate vs. 37% for ordinal-only information
- Optimal stopping applied to parking: occupancy rate determines when to start looking; 85% occupancy vs. 99% dramatically changes the look distance
- House selling: optimal stopping price = function of search cost; if waiting cost exceeds 50% of expected range, take the first offer
- Burglar problem: optimal number of robberies = chance of escape divided by chance of capture
- Experimental data (Rapaport and Seale): subjects achieved ~31% success rate vs. optimal 37%, consistently stopping early; explained by implicit time costs of search

**Logical Method:** Mathematical derivation from first principles (the secretary problem), then extension to structural analogues in real-world domains.

**Logical Gaps:**
- The Secretary Problem's core assumptions—candidates arrive in random order, decisions are irrevocable, the goal is *only* the single best option—frequently fail in practice. The authors acknowledge variants (recall allowed, rejection possible, full information) but the discussion of these variants is asymmetric: the base case gets mathematical rigor; real-world messiness gets narrative illustration.
- The 37% rule maximizes the probability of getting the *single best* option. If the goal is "get something very good" rather than "get the absolute best," a different threshold applies. The authors do not cleanly distinguish "maximize probability of best outcome" from "maximize expected value"—these are different optimization objectives with different solutions.
- "The empirical evidence suggests people stop too early" is offered; the explanation (implicit time costs) is plausible but not demonstrated directly. Alternative: loss aversion, satisficing psychology, or fear of commitment.
- The dating application (Trick, Kepler) involves recall, which changes the mathematical solution. The authors present this as support for optimal stopping while the mechanism invoked is different from the base case.

**Methodological Soundness:** The mathematical core is sound. The applied extensions are logically plausible but stretch the model's assumptions. The distinction between the formal problem and the naturalistic analogues deserves more explicit treatment.

---
