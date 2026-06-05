### CHAPTER 8 (Chapter 9 in audio): Game On

**Core Claim:** DeepMind's Deep Q-learning systems (Atari games) and AlphaGo represent genuine achievements in combining reinforcement learning with deep neural networks, but these systems learn specific contingencies rather than generalizable concepts, and their superhuman game-playing cannot transfer even to minor variations of the same game—let alone to other domains.

**Supporting Evidence:**
- DQN on Atari games: input = current frame + 3 prior frames → output = estimated values for each action; trained over thousands of episodes; outperformed professional human game tester on more than half of 49 games
- Breakout: DQN discovered the "tunneling" strategy (carve a channel through brick edge to bounce ball off ceiling) without being programmed to do so
- AlphaGo Zero: learned Go from scratch via self-play (5 million games); won 100/100 games against AlphaGo Lee; combined Monte Carlo tree search with deep ConvNets
- Kopp et al.'s finding in the AutoTutor context (noted elsewhere): mixing intense/minimal interaction outperformed exclusive intense interaction—directly relevant to the question of whether more interaction is always better

**Logical Method:** Progressive complexity: simple RL (Rosie) → Atari (DQN) → Go (AlphaGo) → evaluation of what was actually learned.

**Logical Gaps:**
- The "DQN discovered tunneling" claim is anthropomorphic in exactly the way Mitchell elsewhere warns against. She does cite Gary Marcus's correction: "The system has learned no such thing. It doesn't really understand what a tunnel or what a wall is." But the correction appears late and briefly.
- The Uber AI Labs finding that random search matched DQN on 5 of 13 Atari games is a devastating methodological challenge: if random weight assignment can match trained Q-learning on some games, those games may not be testing what we think they are testing. Mitchell notes this but does not develop the implication that benchmark design may be systematically misleading the field.

**Methodological Soundness:** The paddle-shift experiment (performance plummets when paddle is moved a few pixels after training) is well-chosen: it directly falsifies the claim that DQN learned "the concept of paddle."

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-8-game-on.md`

Key additions: DQN and AlphaGo are genuine achievements inside rule-bounded environments, but "discovered strategy" language should be translated into learned policy behavior. Benchmark design, weak baselines, and transfer tests are essential.

Settled: deep RL can achieve superhuman game performance. Contested: how much game success predicts open-world intelligence.

Teaching move: replace "the model discovered a tunnel" with "the model learned an action policy that scores under this screen distribution."
