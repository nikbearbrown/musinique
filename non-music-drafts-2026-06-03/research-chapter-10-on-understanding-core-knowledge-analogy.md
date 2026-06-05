### CHAPTER 10 (Chapters 14–16 in audio): On Understanding / Core Knowledge / Analogy

**Core Claim:** Human understanding rests on three foundations that no current AI system possesses: (1) core intuitive knowledge (intuitive physics, biology, psychology), built up from infancy through embodied experience; (2) the ability to simulate mental models of situations; and (3) the capacity for abstraction and analogy-making, which underlies all concept formation. Without these, AI systems will remain brittle and fundamentally unreliable.

**Supporting Evidence:**
- Lakoff and Johnson's *Metaphors We Live By*: abstract concepts are grounded in physical metaphors ("time is money," "sadness is down")—providing evidence that even abstract thought depends on embodied physical experience
- Barcalou's simulation hypothesis: understanding a text involves constructing and running simulations using mental models, not extracting symbolic propositions
- The "hot coffee" experiment: subjects who held a warm cup rated a fictional person as more warm (socially) than subjects who held an iced cup—physical and social temperature activate overlapping neural representations
- Bongard problems: visual puzzles requiring recognition of concepts like "large vs. small" or "objects with a constriction/neck"—humans solve them with 12 examples; ConvNets fail to learn "same vs. different" even with 20,000 training examples, performing barely above random guessing
- Hofstadter's Copycat program: solves letter-string analogy problems (ABC→ABD; PQRS→?) via active symbols and conceptual slippage
- Karpathy's analysis of what it would take to understand a photo of Obama stepping on someone's scale: theory of mind, 3D inference from 2D image, causal reasoning about the scale's readings, prediction of emotional reactions, interpretation of facial expressions

**Logical Method:** Convergent evidence from developmental psychology, cognitive linguistics, experimental psychology, and AI performance benchmarks—all pointing to the same missing capability.

**Logical Gaps:**
- Barcalou's simulation hypothesis is empirically supported but not universally accepted in cognitive science. Mitchell presents it as established without flagging the ongoing debate.
- The Copycat program is described as a success within its micro-world but is explicitly acknowledged as far from general: it cannot handle the two example problems Mitchell herself provides (double-successorship sequences; interpolated extra letters). The gap between "works in micro-world" and "constitutes a path toward general AI" is not bridged.
- The embodiment argument at the chapter's close (Karpathy: "we may need embodiment") is presented as "increasingly compelling" but is not analyzed as a testable hypothesis. What evidence would falsify it?

**Methodological Soundness:** The Bongard problem performance data (barely above random guessing at 20,000 training examples for "same vs. different") is the chapter's single most important empirical result—it directly falsifies the implicit claim that enough data will solve abstraction.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-10-on-understanding-core-knowledge-analogy.md`

Key additions: keep embodiment and simulation theories as plausible but contested, not settled. Bongard/same-different tasks are valuable because they test abstraction and relational generalization rather than classification alone.

Settled: AI systems can be brittle outside training distributions, and human cognition uses rich prior knowledge. Contested: whether embodiment is necessary for general intelligence or whether multimodal/interactive training can substitute.

Teaching move: use a Bongard problem and ask what concept is inferred, not what label is predicted.
