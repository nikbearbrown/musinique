### INTRODUCTION: A New Vocabulary for Human Problems

**Core Claim:** The algorithmic solutions computer scientists have developed for computationally hard problems constitute a practical and empirically grounded guide to human decision-making—not a metaphor, but a direct transfer of provably optimal methods.

**Supporting Evidence:**
- The 37% rule for optimal stopping is derived mathematically and produces a provably highest-probability outcome for finding the best option under serial search conditions
- Historical framing: algorithms predate computers (Al-Khwarizmi, 9th century; Sumerian division algorithms, 4,000 years ago)
- The authors cite behavioral economics literature (implied) and cognitive science suggesting that many apparent human irrationalities may reflect the intrinsic difficulty of the problems, not deficient brains
- Carl Sagan quoted: "science is a way of thinking much more than it is a body of knowledge"

**Logical Method:** Analogical argument from isomorphism—human decision problems share the same formal structure as classical computational problems, therefore optimal computational solutions translate directly.

**Logical Gaps:**
- The claim that human problems are *isomorphic* to computational ones is asserted rather than proven at the outset. The authors acknowledge that "life is too messy for strict numerical analysis" while simultaneously claiming the algorithms apply—these two claims require more careful reconciliation than the introduction provides.
- "Four-year-olds are better than supercomputers at vision, language, and causal reasoning" is offered as evidence that human cognition is not simply deficient, but the inference from this to "our errors reveal problem difficulty, not brain deficiency" is incomplete. These are different cognitive domains.
- The "backed up by proofs" claim in the introduction applies precisely to the formal versions of the problems; whether real-world human instances satisfy the assumptions of those formal versions is exactly the question the book must address but does not settle definitively.

**Methodological Soundness:** The introduction functions as advocacy for a thesis whose full warrant requires the subsequent chapters. It is intellectually honest about the limits ("in cases where life is too messy...") but buries those qualifications quickly. Treat as framing, not as established finding.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-a-new-vocabulary-for-human-problems.md`

### Conceptual Foundations

1. **Computer science as diagnostic vocabulary.** The introduction should teach that computer-science problems can name recurring structures in human life: optimal stopping, explore/exploit, sorting, caching, scheduling, and game theory. The value is diagnostic before it is prescriptive.

2. **Algorithms are older than computers.** Britannica traces the word to Latin renderings of al-Khwarizmi. Students need the formal sense: a finite procedure for a class of problems, not merely a recommendation feed or AI model.

3. **Bounded rationality reframes apparent error.** Herbert Simon's bounded rationality and later resource-rational analysis support the idea that apparent irrationality may reflect limited information, time, and computation rather than defective brains.

4. **Isomorphism is the hard claim.** The chapter must not let analogy do all the work. Formal results transfer only when the human situation satisfies the relevant assumptions: arrival order, reversibility, information, payoff, costs, and objective.

### Domain Examples and Cases

- **Apartment hunting / secretary problem:** useful for showing look-then-leap logic and its assumptions.
- **Explore/exploit:** trying new restaurants versus returning to favorites.
- **Sorting/caching:** closets, files, memory, and retrieval.
- **Scheduling/thrashing:** productivity collapse under overload.

Failure cases:

- Applying the 37% rule when options can be revisited.
- Optimizing for "the best" when the real goal is good-enough, fairness, low regret, or relationship preservation.
- Treating a theorem as portable without checking model assumptions.

### Connections and Dependencies

Readers need the difference between algorithm, model, implementation, and real-world situation. They also need basic probability intuition and the idea that optimization requires an objective function.

This introduction unlocks later sections by establishing the repeated method: name the formal problem, explain the formal result, check assumptions, then decide how much transfers.

### Current State of the Field

Settled: algorithms can illuminate non-computing decision structures; the classical secretary problem has a 1/e result under strict assumptions; bounded rationality and resource-rationality are serious cognitive-science frames.

Contested: how far formal algorithms should be treated as practical life advice; whether popular treatments overstate the fit between life and formal models; whether "optimal" is useful when human goals are plural and social.

Recent-change note: generative AI has made "algorithm" even fuzzier in public discourse. This chapter should actively separate algorithm, model, AI system, data, and deployment.

Key sources:

- Brian Christian and Tom Griffiths, *Algorithms to Live By*.
- Herbert Simon on bounded rationality.
- Lieder and Griffiths on resource-rational analysis.
- Secretary-problem / optimal-stopping literature.
- Carl Sagan's science-as-way-of-thinking frame.

### Teaching Considerations

Students often either reject the analogy as too abstract or overapply it as life advice. Good framings: algorithms as tools in a toolbox; formal models as maps; assumptions as recipe ingredients.

Exercises:

1. Match human decisions to possible computer-science problem types.
2. List the formal assumptions and mark which ones real life violates.
3. Rewrite overconfident algorithmic advice into a careful model-based claim.
4. Compare "maximize chance of the best option" with "get a good option quickly."
