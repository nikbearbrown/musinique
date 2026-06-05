### CHAPTER 7: Beyond Adjustment — The Conquest of Mount Intervention

**Core Claim:** The backdoor criterion is sufficient for many but not all causal estimation problems. The frontdoor criterion (1993) extended this to cases with unobservable confounders, provided there is a shielded mediator. The do-calculus (three rules) is the complete machinery for all causal effect estimation from observational data, proven complete by Schpitzer (2006). Instrumental variables extend this further.

**Supporting Evidence:**
- Front door criterion: smoking → tar → cancer, with smoking gene as unobservable confounder. Tar deposits, if measurable and shielded from the gene, allow estimation of the smoking-cancer effect without data on the gene.
- Glenn and Cation (2014) JTPA job training study: front door estimates match the experimental RCT benchmark; back door estimates (controlling for observed confounders like age and race) are wildly off — hundreds to thousands of dollars wrong.
- John Snow/cholera: water company as instrumental variable — water company → water purity → cholera, with no direct path from water company to cholera.
- Mendelian randomization: genes as natural instruments — HDL/LDL cholesterol and heart disease.
- Do-calculus completeness: Huang-Valtorta and Schpitzer independently proved (2006) that if do-calculus can't solve it, no solution exists.

**Logical Method:** Cumulative constructive argument. Each new method (front door, do-calculus, IV) solves problems left unsolvable by the previous one. The completeness proof caps the argument.

**Logical Gaps:**
- The front door criterion requires two key assumptions (no arrow from gene to tar; smoking affects cancer only through tar). David Friedman's objections — both biologically plausible — show that the assumptions can fail in ways experts would dispute. Pearl acknowledges this but uses the example anyway as a proof of principle.
- Instrumental variables require the instrument to be independent of confounders, have no direct effect on the outcome, and affect the outcome only through the treatment. These are three strong assumptions, and in practice the third (exclusion restriction) is often untestable.
- The do-calculus completeness result is beautiful but narrow: it tells you whether the causal effect is *identifiable*, not whether it can be *estimated accurately from finite data*.

**Methodological Soundness:** The front door formula derivation is correct. The Glenn/Cation JTPA validation is the strongest empirical confirmation of the front door approach in the book. The do-calculus completeness is mathematically proven.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-beyond-adjustment-the-conquest-of-mount-intervention.md`

Key additions: distinguish identification from estimation. Frontdoor, do-calculus, and instrumental variables can identify causal effects under explicit assumptions, but they do not guarantee correct graphs, valid instruments, adequate sample size, or easy finite-data estimation.

Settled: graphical causal models give precise identification criteria under assumptions. Contested: how often real problems have causal diagrams reliable enough for the formal machinery to settle the empirical question.

Teaching move: use three DAGs - confounder, mediator, collider - and ask what happens if students "adjust for everything."
