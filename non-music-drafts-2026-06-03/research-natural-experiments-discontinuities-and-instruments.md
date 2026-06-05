### CHAPTER 7: Natural Experiments, Discontinuities, and Instruments

**Core Claim:** In contexts where treatment assignment is not controlled by the investigator but is influenced by a process with genuine randomness (a lottery, a discontinuity, a genetic coin flip), causal inference can proceed using the random element as if it were a designed experiment — sometimes estimating effects for a specific sub-population (compliers) rather than the whole population.

**Supporting Evidence:**
- Florida Fantasy 5 lottery: large winners ($50K–$150K) and small winners (<$10K) compared for bankruptcy rates. Large winners had lower bankruptcy rates in years 0–2 but higher rates in years 3–5; aggregate rates similar. Conclusion: a cash windfall does not durably reduce bankruptcy risk.
- Chicago Housing Authority voucher lottery: offers randomized via waiting list position; 18,100 families offered vouchers by 2003. Small but statistically notable decline in employment among households offered vouchers (effect of the offer, not acceptance).
- CTLA4 gene and Graves' disease: siblings differ by which version of the gene (A or a) they received from a heterozygous parent, a difference determined by which egg cell met which sperm — genuinely random. The sibling with Graves' disease systematically carried an excess of the A allele.
- Transmission Disequilibrium Test (TDT): diseased children compared not to other children but to their *hypothetical siblings* — all possible children the parents could have produced given their genotypes. Requires only parental genotype data, not comparison to unaffected siblings.
- Encouragement to quit smoking: ATEQ = 31% − 6% = 25% more quitters under mindfulness training (MT) vs. FFS. Complier Average Causal Effect (CACE) = ATE / ATEQ = 4 × ATE, under the exclusion restriction (encouragement affects lung function only through quitting).
- Housing voucher acceptance (Jacob and Ludwig): CACE for accepting a voucher is 2–3× larger than the intent-to-treat estimate (effect of the offer), reflecting that only a fraction of those offered vouchers accepted.

**Logical Method:** Three distinct identification strategies are presented:
1. Lotteries — true randomization of a relevant variable (or a closely related variable)
2. Genetic randomization — Mendelian random assortment as nature's lottery
3. Instrumental variables — when a randomized variable (encouragement) affects only some individuals' behavior (compliers), and the instrument affects outcomes only through behavior (exclusion restriction)

**Logical Gaps:**
- The exclusion restriction — that encouragement affects outcomes only through behavior, not directly — is the load-bearing assumption for CACE estimation. Rosenbaum identifies this correctly ("talk without quitting does nothing for lung function") but acknowledges the restriction may not hold for contentment measures. What is missing is any guidance on *when* the restriction is plausible versus implausible beyond the single pair of examples given.
- The chapter defines compliers (quit only if encouraged) but not the other three subgroups (always-takers, never-takers, defiers). Excluding defiers (the "no perversity" assumption, stated as the first small assumption) is necessary for the CACE proof, but the chapter does not discuss whether this assumption can be tested or what its violation would imply.
- Discontinuity designs are presented informally (the concert ticket door analogy) without addressing the key assumption: that individuals near the threshold are similar except for treatment assignment. This is the design's central identifying assumption and receives no discussion.

**Methodological Soundness:** The CACE derivation is the chapter's most technically rigorous passage — the two-paragraph proof that ATE/ATEQ is the complier-average effect under the exclusion restriction is correct and clearly presented. The genetic applications (sibling comparison, TDT) are well-chosen: they make the abstract randomization argument concrete and show that "natural" randomness can be as rigorous as designed randomness.

---
