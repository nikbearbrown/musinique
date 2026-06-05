### CHAPTER 7 (Chapter 8 in audio): Rewards for Robots

**Core Claim:** Reinforcement learning—agents learning by performing actions and occasionally receiving rewards—offers a path toward AI that learns without labeled data, but current implementations require extensive human design choices, work primarily in simulated environments, and cannot transfer what they learn to related tasks.

**Supporting Evidence:**
- Q-learning demonstrated via "Rosie the Robo Dog": state (distance from ball), actions (forward/backward/kick), Q-table updated at reward events; convergence after ~300 episodes
- Temporal difference learning: learning a "guess from a better guess"—the network's outputs at the current iteration are assumed closer to correct than at the previous iteration
- Key limitations enumerated: continuous state spaces (self-driving car faces infinite states, not a Q-table entry); real-world episodes are too slow and risky; simulation-to-real-world transfer often fails

**Logical Method:** Worked example at low complexity → generalizations → failure modes.

**Logical Gaps:**
- The exploration/exploitation tradeoff is named but not analyzed: how much of reinforcement learning's success is in selecting the right balance, and how well do current algorithms do this? The answer—imperfectly, requiring extensive hyperparameter tuning—is implied but not stated.
- Q-learning convergence guarantees are not discussed. The guarantee is real but limited: it applies under specific conditions (finite state and action spaces, sufficient exploration) that do not hold in most practical applications.

**Methodological Soundness:** The Rosie example is pedagogically effective and technically accurate for tabular Q-learning. The limitations are honestly stated.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-7-rewards-for-robots.md`

Key additions: tabular Q-learning has real but narrow convergence guarantees: finite states/actions, sufficient exploration, and suitable learning rates. Exploration/exploitation and sim-to-real transfer should be treated as central limitations rather than implementation details.

Settled: RL is powerful in simulated or well-defined environments. Contested: how reliably RL transfers to open real-world domains.

Teaching move: use reward-hacking examples to separate reward from intended goal.
