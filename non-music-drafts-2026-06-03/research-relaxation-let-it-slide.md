### CHAPTER 8: Relaxation — Let It Slide

**Core Claim:** Combinatorial optimization problems—of which the most famous is the Traveling Salesman Problem—are provably intractable (NP-hard). The correct response is not to give up or compute forever but to relax the problem: loosen constraints, convert discrete choices to continuous ones, or turn impossibilities into costly violations (Lagrangian relaxation). These techniques yield near-optimal solutions in polynomial time and translate directly to human problem-solving.

**Supporting Evidence:**
- TSP: Merrill Flood, Karl Menger (1930s); intractable since Karp (1972); best known algorithms achieve within <0.05% of optimal for all cities on Earth
- Constraint relaxation: Minimum Spanning Tree as relaxed lower bound on TSP; within-2x guarantee via double-tree algorithm
- Continuous relaxation: discrete fire truck placement problem → fractional solution → rounding → guaranteed ≤2x optimal
- Lagrangian relaxation: penalty for constraint violation enables progress; Michael Trick's MLB/NCAA scheduling uses Lagrangian relaxation precisely because "fractional games" aren't useful (continuous relaxation fails here)
- Megan Bellos's wedding seating = protein design problem; same algorithm; 36 hours of computation still didn't find optimal; but found a good solution
- "What would you do if you weren't afraid?" as human constraint relaxation
- Rock bands playing past curfew = knapsack problem with Lagrangian relaxation (pay the fine)
- Boltzmann vs. Voltera quote: "the perfect is the enemy of the good"

**Logical Method:** Formal complexity theory (NP-hardness) + approximation algorithm guarantees + case studies + conceptual analogies.

**Logical Gaps:**
- The approximation ratio guarantees (≤2x optimal for continuous relaxation) are mathematical theorems. The book presents them as reassuring; whether 2x worse than optimal is acceptable for any given human decision problem depends on stakes. For medical triage or safety engineering, 2x worse may be unacceptable. The chapter doesn't discuss this dependency.
- The "what if you won the lottery" thought experiment as constraint relaxation is evocative but operationally vague. The formal technique requires the relaxed solution to provide a starting point or bound for the real problem. Wishful thinking that cannot be systematically mapped back to the constrained problem does not satisfy the mathematical definition.
- The Bellos wedding seating case is presented as a success despite not finding the optimal solution. This validates the heuristic approach, but it is an anecdote—there's no evidence that the algorithm outperformed a skilled human event planner who might have used domain knowledge that the algorithm lacked.

**Methodological Soundness:** The formal content (TSP intractability, approximation ratios) is accurate. The human analogies are structurally sound at the conceptual level but lose precision in application.

---
