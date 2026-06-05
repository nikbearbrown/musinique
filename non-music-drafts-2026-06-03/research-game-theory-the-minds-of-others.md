### CHAPTER 11: Game Theory — The Minds of Others

**Core Claim:** Classical game theory's Nash equilibrium, while mathematically guaranteed to exist, is computationally intractable to find in complex real games—undermining its predictive value. Algorithmic game theory quantifies the price of anarchy, resolves the recursion problem in strategic thinking, and identifies mechanism design (changing the game rather than the strategy) as the primary tool for improving outcomes. Dominant strategies, information cascades, and the Vickery auction offer concrete lessons for individual and institutional behavior.

**Supporting Evidence:**
- Nash (1951): every finite two-player game has at least one equilibrium; Nobel Prize 1994
- Papadimitriou et al. (2005-2008): finding Nash equilibrium is computationally intractable (PPAD-complete); therefore market equilibrium cannot be assumed reached by rational agents
- Ruffgarden and Tardosh (2002): selfish routing price of anarchy ≤ 4/3 for Wardrop equilibria
- Prisoner's Dilemma: dominant strategy (defect) leads to Pareto-inferior outcome; intuitively demonstrates that rational individual action can produce collectively irrational outcomes
- Tragedy of the Commons (Hardin 1968): multi-player prisoner's dilemma; fossil fuel / climate change / unlimited vacation policy as examples
- Vickery auction: bidding true value is the dominant strategy; revenue equivalence theorem guarantees same expected price as first-price auction
- Myerson Revelation Principle: any game requiring strategic misrepresentation can be transformed into a truthful-dominant-strategy game
- Information cascades (Bikhchandani et al.): rational agents collectively converge on wrong answer; Amazon textbook ($23M) and flash crash ($1T) as examples
- Robert Frank: emotions as evolutionary mechanism design; love as commitment device that changes game payoffs; anger and revenge as punishment mechanisms stabilizing cooperation
- Unlimited vacation policy → Nash equilibrium = zero vacation (multiple corporate case studies)

**Logical Method:** Formal game theory (Nash, intractability) + experimental economics + evolutionary psychology + algorithmic game theory (price of anarchy, mechanism design).

**Logical Gaps:**
- "Finding Nash equilibrium is intractable → markets may not reach equilibrium" is the book's most important game theory claim. But PPAD-hardness means the worst case is intractable, not that equilibrium is never reached. Many games have easily found equilibria (rock-paper-scissors). The general conclusion is overstated.
- The Prisoner's Dilemma discussion correctly identifies the mechanism but applies it loosely to situations (climate change, vacation policy) where the payoff structures are more complex and the coordination mechanisms available are correspondingly more varied.
- The Frank argument (emotions as evolutionarily designed mechanism design) is speculative evolutionary psychology. The adaptationist claim—that anger, love, and guilt evolved *because* they solve coordination problems—requires much stronger evidence than the book provides. These emotions may have multiple functions or be evolutionary spandrels.
- The Vickery auction is presented as close to utopian. The book does not discuss collusion (which undermines truthfulness), common value settings (where Vickery has different properties), or the substantial practical failures of second-price auctions in real-world deployments (eBay bidding behavior, Google's early AdWords design choices).

**Methodological Soundness:** The formal game theory content (Nash, intractability, Vickery, price of anarchy) is accurate. The evolutionary psychology and prescriptive applications involve substantial speculation presented as established finding.

---
