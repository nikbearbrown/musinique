### CONCLUSION: Computational Kindness

**Core Claim:** The book's algorithms collectively point toward a meta-principle: computation is expensive. Designing human interactions and institutions to minimize the computational burden on participants—computational kindness—is both a practical ethical principle and an extension of good algorithm design. The Spanish interview scheduling example (specific time offer vs. open-ended availability) illustrates that constraining options can be kinder than maximizing them.

**Supporting Evidence:**
- Interview scheduling: "Next Tuesday 1-2 pm" gets faster acceptance than "whenever you're free"—verification (accepting a time) is easier than search (finding a time)
- Coin denomination optimal design: Jeffrey Schallet (2003)—18-cent piece is mathematically optimal for minimizing coin count but makes change-making intractable; 2-cent or 3-cent piece is near-optimal and computationally kind
- Helical parking garage: first available space, no game theory required—O(1) decision
- Restaurant seating: spinning (wait without confirmed time) vs. blocking (estimated wait and paged when ready)—spinning consumes user CPU cycles
- Bus stop display: "next bus in 10 minutes" converts continuous re-decision into one-time decision

**Logical Method:** Empirical observation (interview scheduling) + formal coin design analysis + structural analogies.

**Logical Gaps:**
- "Computational kindness" as a principle is introduced only in the conclusion. As a unifying principle it arrives too late to have been tested against the book's full analysis.
- The interview scheduling observation is a single anecdote. Whether it generalizes to all constraint-offering contexts (some people genuinely prefer flexibility; some offered times are impossible) is not examined.
- The coin denomination example is charming but minor; 18-cent vs. 2-cent piece affects cashiers, not strategic decision-making. The use of this as a conclusion example undersells the chapter's ambitions.

**Methodological Soundness:** The conclusion functions as synthesis and advocacy rather than empirical argument. Its claims are plausible but underdeveloped as a closing statement.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-conclusion-computational-kindness.md`

Key additions: computational kindness is a cognitive-load ethics principle: reduce unnecessary search, monitoring, and uncertainty. Constraint can be kinder than choice when users retain meaningful opt-out or correction.

Settled: cognitive load and choice overload can impair decisions. Contested: when defaults become manipulation or remove useful agency.

Teaching move: redesign a scheduling, checkout, or waiting-room interaction to reduce unnecessary search.
