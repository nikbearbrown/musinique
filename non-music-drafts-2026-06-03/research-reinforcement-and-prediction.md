### CHAPTER 8: REINFORCEMENT AND PREDICTION

**Core Claim:** Phasic dopamine encodes temporal-difference prediction error ($\delta_t = r_{t+1} + \gamma V(s_{t+1}) - V(s_t)$), not pleasure. The biological architecture—basal ganglia as actor-critic system with dopamine as teaching signal—is conserved from lamprey onward and is the source code for modern reinforcement learning. The structural vulnerability is reward specification: any optimizer maximizes what it is given, and almost any proxy can be maximized in ways that diverge from the actual goal.

**Supporting Evidence:**
- Schultz, Dayan & Montague 1997: exact correspondence between TD prediction error and dopamine firing in macaques
- Adams & Dickinson devaluation: overtrained rats press lever for aversive food (model-free vs. model-based dissociation)
- Berridge wanting/liking dissociation: dopamine necessary for wanting, not for hedonic response
- The 2010 Flash Crash as documented instance of multi-agent reward-hacking
- Kirkpatrick et al. EWC as biological-consolidation-inspired engineering

**Logical Gaps:**
- The Flash Crash is used as evidence for "what happens when many powerful optimizers act on each other's outputs without modeling the shared system." This is a plausible narrative but the causal attribution is contested in the economics literature—algorithmic trading amplified the crash but did not cause it; the originating sell order was human. Using it as a clean example of multi-agent reward hacking overstates what the evidence shows.
- The Berridge wanting/liking dissociation is described as showing "dopamine is necessary for wanting, not for liking." But the dissociation is established by μ-opioid and dopamine lesion studies in rodents—the cross-species inference to the chapter's macaque discussion is not explicitly flagged.
- The chapter states the basal ganglia appear "in essentially modern form in the lamprey"—a claim supported by Suryanarayana et al. and Stephenson-Jones et al. but presented without acknowledging that "essentially modern form" is a functional claim that rests on behavioral rather than strict structural homology.

**Methodological Soundness:** Good. The TD-dopamine correspondence is presented as strong evidence rather than confirmed mechanism—appropriate given that it is indeed a model-fit result, not a causal proof.

---
