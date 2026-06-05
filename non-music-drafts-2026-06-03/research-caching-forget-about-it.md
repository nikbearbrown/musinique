### CHAPTER 4: Caching — Forget About It

**Core Claim:** Memory management is universal across computers, libraries, closets, and human brains. The optimal eviction policy is Least Recently Used (LRU), which provably comes within a constant factor of the clairvoyant optimal (Belady's algorithm). The Noguchi filing system, self-organizing lists, and the human forgetting curve are all instantiations of LRU. Cognitive decline in aging may be a computational artifact of larger memory stores rather than a neural failure.

**Supporting Evidence:**
- Maurice Wilkes (1962, Atlas computer): first implementation of cache concept
- Belady (1966): clairvoyant algorithm (evict what will be needed furthest in future) is theoretically optimal; LRU beats FIFO and random eviction in practice
- Temporal locality: recently accessed information is most likely to be needed again—a structural property of both computation and human cognition
- Slator and Tarjan (1985): LRU (move-to-front) rule in self-organizing lists comes within a constant factor of clairvoyance in worst-case analysis
- Noguchi filing system: insert retrieved files at left = move-to-front = LRU; independently discovered optimal structure
- John Anderson and Lael Schooler (1991): human forgetting curve mirrors the statistical decay of references to words in NYT headlines, parent speech, and email—suggesting the brain is optimally tuned to its environment
- Amazon CDN logistics: anticipatory package shipping = geographic caching
- Ramscar et al. (University of Tübingen): cognitive "decline" in aging is partly a computational consequence of larger memory stores, not degraded processing

**Logical Method:** Theoretical optimality proof (Slator and Tarjan) + structural convergence of independent systems (brain, Noguchi, computer cache) + empirical linguistic analysis (Anderson and Schooler).

**Logical Gaps:**
- The Anderson/Schooler result is elegant but rests on the claim that the statistical structure of human *environment* matches the forgetting curve. This requires the strong assumption that their three sample environments (NYT headlines, parental speech, one person's email) are representative of the human environment generally. This is a significant sampling assumption.
- LRU is proven optimal within a constant factor for self-organizing lists; this is a worst-case competitive analysis result. It does not guarantee that LRU is best on average for any specific real-world distribution. The authors conflate competitive ratio (worst-case) with general optimality.
- The Ramscar aging argument is presented as if it settles the question of cognitive decline; the actual literature is considerably more contested. Memory retrieval slowing in aging has multiple established causes; the computational argument explains *some* variance, not all.
- The prescriptive recommendation (keep recently used items closest to hand, apply LRU to closets) follows logically from the theory but assumes that the time cost of retrieval is the dominant cost. In many human contexts, organizational clarity or aesthetics also matter.

**Methodological Soundness:** The theoretical core (Slator-Tarjan, Belady) is rigorous. The psychological applications (Anderson/Schooler, Ramscar) are empirically plausible but oversimplified in presentation.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-caching-forget-about-it.md`

Key additions: separate Belady's clairvoyant optimum, LRU's temporal-locality heuristic, and Sleator/Tarjan worst-case competitive bounds. LRU is foundational but not universally optimal, and human memory analogies depend on sampling and workload assumptions.

Settled: temporal locality is powerful, and LRU is a useful baseline. Contested: how far cache theory explains human forgetting and age-related cognitive change.

Teaching move: ask which criterion is meant by "optimal": offline optimum, worst-case competitive, average-case, or practical under a specific workload.
