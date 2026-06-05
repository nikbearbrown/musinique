### SECTION 6: Data Storytelling — Correlation and Context (Chapter 6)
**Core Claim:** Correlation is powerful and sufficient for many commercial decisions, but its limits are real and dangerous when mistaken for understanding. The progression from correlation → association → cause-and-effect represents a ladder of comprehension that requires both data and theory. Neither alone is adequate.

**Supporting Evidence:**
- Google Flu Trends (2008): accurately predicted H1N1 spread in 2009; overestimated flu prevalence by ~2x in January 2012–13 peak (reported 11% vs. CDC's 6%); a 2014 Science paper found the service "consistently overestimated" across a 2+ year period; even after the 2013 algorithm update, overshot by ~30%
- ZestFinance: machine learning for payday loan underwriting reduced default rates by 50% compared to typical payday lenders; 45,000 data signals; example signals: length of current cell phone number tenure, case style of name entry, "walking dead" borrowers (appear dead in credit bureau records) default at lower rates than average
- Walmart Pop Tarts and Beer case: consumers in hurricane paths bought strawberry Pop Tarts at 7x normal rate; beer was the best-selling pre-hurricane item; inventory adjusted without causal explanation
- Google Flu Trends overestimation attributed to "Big Data Hubris" (Nature, 2013): implicit assumption that big data sets trump traditional data collection
- IBM's Nell (Carnegie Mellon): scanned hundreds of millions of web pages; 2.3M facts accumulated with estimated 87% accuracy; required human correction sessions every few weeks
- Watson initially answered "Who was the first woman astronaut?" with "Wonder Woman" due to inability to separate fictional from historical text references

**Logical Method:** Inductive case studies across domains (public health, consumer credit, retail inventory) + IBM/CMU technology cases + synthesis through Kahneman/Tetlock/Farouci frameworks to build toward the "measurements plus models" conclusion.

**Logical Gaps:**
- The ZestFinance correlations (typing case style, phone number tenure) are presented as effective without examining their disparate impact on protected classes. The book is silent on whether proxy variables in credit scoring that correlate with demographic characteristics constitute legally or ethically problematic discrimination—a live regulatory and civil rights debate at the time of writing.
- The Google Flu Trends case is the chapter's strongest methodological contribution, but the analysis stops at "missed context." The more fundamental problem—that the algorithm was trained on historical search-flu correlations that broke down when media-driven health anxiety decoupled search behavior from actual illness—is described but not used to derive a generalizable principle about when correlation-based systems fail (specifically: when the behavioral substrate generating the signal changes).
- David Ferrucci's claim that "in a purely data-driven approach, there is no real understanding" is presented as wisdom but is contested. The chapter doesn't engage with the opposing view that "understanding" may be an unnecessary theoretical luxury in prediction tasks where calibrated correlations work reliably.

**Methodological Soundness:** The strongest analytical chapter in the book. The Google Flu Trends failure case is handled with appropriate rigor. The Brahe-Kepler analogy (measurements without theory vs. theory without measurements) is apt.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-data-storytelling-correlation-and-context.md`

Key additions: Correlation can be useful when decisions are low-stakes, reversible, and the environment is stable. The failure mode is distribution shift: the signal-generating process changes while the model still trusts old correlations.

Settled: Google Flu Trends is a canonical big-data-hubris case. Contested: how much causal understanding is necessary for high-performing prediction in different domains.

Teaching move: Compare hurricane Pop-Tart stocking with credit scoring. One is a low-stakes inventory correlation; the other requires fairness, explainability, and regulatory scrutiny.
