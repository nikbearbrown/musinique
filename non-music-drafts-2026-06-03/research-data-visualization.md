### CHAPTER 7: Data Visualization
**Core Claim:** Data graphics can mislead through duck ornamentation (prettiness over clarity), glass slippers (forcing data into inappropriate visual forms), axis manipulation, and violations of the principle of proportional ink—even when the underlying data are accurate.

**Supporting Evidence:**
- Reuters inverted y-axis graph (Florida gun deaths): axis inversion made rising murders appear to fall after Stand Your Ground legislation; designer stated she preferred "negative" representation of deaths—not deliberate deception
- USA Today data ducks: lipstick bars, ice cream cone pie charts
- Periodic tables of everything: co-opt Mendeleev's structure without the structural logic that makes it meaningful
- Subway map metaphors: misapplied to scientists, Shakespeare plays, philosophy
- Quebec trust levels: truncated y-axis exaggerated differences; corrected after reader complaints
- Clinton Instagram wage gap: bars visually misrepresent stated percentages
- Tennessee job growth bar chart: proportional ink violation
- College football recruiting budget vs. success: correlation r=0.78; but causality unclear (does money buy wins or do wins generate revenue?)
- 3D bar charts, donut charts: geometric properties violate proportional ink principle
- Autism/MMR double y-axis chart: axes scaled to force visual correlation

**Logical Method:** Principle of proportional ink as master framework: the amount of ink representing a value should be proportional to that value. Most visualization errors are applications or violations of this principle.

**Logical Gaps:**
- The authors establish "never assume malice when incompetence explains it" as a principle but do not apply it consistently. The Reuters graph is charitably explained; the autism/MMR chart is presented without equivalent charity. The asymmetry is not justified.
- The principle of proportional ink is stated clearly but its application to line graphs (where ink use is not proportional to value) requires additional justification. The authors provide it but the reasoning is more complex than they acknowledge: position, not area, encodes value in line graphs.
- The chapter conflates aesthetic failures (ducks) with epistemic failures (axis manipulation). These are meaningfully different: ducks obscure data through distraction; manipulated axes actively deceive. The moral weight is different; the analytical treatment should distinguish them more clearly.

**Methodological Soundness:** The principle of proportional ink is a genuinely useful analytical framework. The chapter's examples are well-chosen. The Reuters case study demonstrates admirable intellectual charity.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-data-visualization.md`

Key additions: A chart is an argument made through encodings. The chapter should distinguish decorative distraction, accidental design error, and deliberate visual persuasion rather than treating all bad charts as the same kind of failure.

Settled: Scale, baseline, encoding choice, and omitted context can change interpretation even when the underlying data are real.

Teaching move: Give students an ugly accurate chart and a polished misleading chart, then ask which one better supports truth and why.
