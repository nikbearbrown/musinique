### CHAPTER 5: Scheduling — First Things First

**Core Claim:** Single-machine scheduling theory provides provably optimal algorithms for human time management, contingent on which metric you are optimizing. Earliest Due Date minimizes maximum lateness. Shortest Processing Time minimizes total wait (sum of completion times). Weighted SPT minimizes weighted completion time. Preemption and uncertainty don't eliminate optimal strategies but change their form. Most scheduling problems are, however, intractable—and most human scheduling failures can be explained by thrashing, context switching costs, and priority inversion rather than laziness.

**Supporting Evidence:**
- Selmer Johnson (1954): first formal optimal scheduling algorithm (two-machine book-binding)
- Moore's Algorithm: minimizes number of late tasks (not total lateness)
- Weighted SPT: divide task importance by duration, work in descending order—analogous to animal foraging caloric-return-per-time optimization
- Debt avalanche (highest interest rate first) vs. debt snowball (smallest debt first) as scheduling variants
- Mars Pathfinder priority inversion (1997): real-world catastrophic failure caused by low-priority task blocking high-priority resource; fix = priority inheritance
- Jan Karel Lenstra (1978) and Eugene Lawler: mapping of scheduling problem complexity; only 9% of scheduling problem classes are efficiently solvable; 84% are provably intractable
- Context switching costs: programmers, writers—"nothing less than 90 minutes" is useful; context switches produce 60-second level human delays
- Thrashing: adding one more program can cause complete system collapse; human equivalent = paralysis from too many open loops
- Interrupt coalescing: Donald Knuth's email-free lifestyle; postal mail as natural coalescing; weekly meetings as institutional coalescing
- Pomodoro/time-boxing as minimum slice implementation

**Logical Method:** Formal complexity theory (Lenstra/Lawler mapping) + controlled analogies to human time management + case study (Pathfinder).

**Logical Gaps:**
- The move from formal single-machine scheduling to human task management requires the assumption that human "machines" are single-threaded in the relevant sense. Humans multitask imperfectly—the degree to which single-machine scheduling applies vs. multi-machine scheduling is not resolved.
- "Most human scheduling failures are thrashing or priority inversion" is a compelling narrative but not demonstrated empirically. Procrastination, avoidance, affective interference, and cognitive load have extensive empirical literatures; the chapter does not engage them.
- The SPT recommendation ("always do the quickest task") is optimal for minimizing sum of completion times but actively harmful for minimizing weighted completion times if the quick tasks are low-importance. The book notes this but not prominently enough—the pop-psychology takeaway "do quick things first" is a distortion of the actual recommendation.
- The intractability finding (84% of scheduling problems have no efficient solution) is used to normalize human scheduling failure—a reasonable conclusion—but also potentially license to stop trying. The prescriptive message is underdeveloped.

**Methodological Soundness:** The complexity mapping is rigorous. The Pathfinder case is documented. The prescriptive recommendations are occasionally oversimplified relative to the formal results.

---
