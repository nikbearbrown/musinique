### CHAPTER 9: Cognition — AI and the Computational Blind Spot
**Core Claim:** AI systems, particularly machine learning, do not realize relevance — the capacity to determine what matters in an open-ended situation — because relevance is not a computational property. The frame problem reveals an intractable limitation of any computational approach. AlphaGo does not "master Go" — it detects statistical patterns in Go-shaped data without knowing it is playing a game. The computational blind spot is a case of surreptitious substitution: computational models substituted for the lived world they represent.

**Supporting Evidence:**
- Dennett's frame problem story: a robot trying to retrieve a battery fails to realize the bomb on the same wagon will also move. Any attempt to computationally specify relevance reintroduces the problem of determining which information is relevant
- AlphaGo's dependence on human knowledge (Monte Carlo tree search, the rules of Go, human expert training data) is documented; the claim that it "mastered Go without human knowledge" is shown to be factually inaccurate
- Marcus and Davis on AlphaGo: the system cannot transfer knowledge between domains, cannot understand that it is playing a game, has no access to the semantics of its data structures
- Self-driving cars as illustration: functions only in geofenced areas with extensive infrastructure — we are remaking the world to fit the limitations of the devices
- Crawford on AI's material and social dependencies: AI requires mineral extraction, cheap labor, and encoded human biases — it does not transcend nature or culture

**Logical Method:** Conceptual analysis of AI limitations combined with documented empirical cases. The argument proceeds from the frame problem (theoretical), through AlphaGo (empirical), to self-driving cars (design choice), to conclude that the computational blind spot generates both bad science and socially harmful technology.

**Logical Gaps:**
- The argument against computational approaches to cognition is strong for current AI systems but may prove too much. The claim that relevance realization "cannot be reduced to heuristic rules and symbolic representations" is plausible for first-wave AI but is being generalized to all computational approaches. Future architectures may address some of these limitations without resolving the deeper philosophical issue.
- The authors endorse inactive cognitive science (enactivism) as a move beyond the computational blind spot but do not specify what a non-computational account of relevance realization would actually look like mechanistically. "Cognition is sense-making in precarious conditions" is a framing, not a mechanism.
- Crawford's political economy critique of AI is valid and important but slightly off-center from the epistemological argument. The two strands (AI's failure to realize relevance, AI's dependence on material extraction and encoded bias) are related but require separate analysis that the chapter does not fully provide.

**Methodological Soundness:** Strong on the frame problem and AlphaGo cases. The general claim that large language models "have no conceptual understanding of the outside world" is defensible but somewhat underspecified — what would "conceptual understanding" look like in a non-biological system, and how would we test for it?

---

## Extended Research Notes

**Pantry note:** `pantry/notes-cognition-ai-and-the-computational-blind-spot.md`

Key additions: the frame problem is best taught as relevance realization: what changes, what stays fixed, and what matters. The chapter's strongest critique applies to current AI; the stronger claim that relevance cannot be computationally solved needs careful defense.

Settled: current AI systems can fail at relevance and transfer. Contested: whether relevance realization is impossible for computation or merely unsolved by current architectures.

Teaching move: ask what the system treated as relevant, what it ignored, and who arranged the environment so that worked.
