# BOOKMAP: Causal Inference
**Paul R. Rosenbaum (2020) | MIT Press Essential Knowledge Series**

---

## PART 1: CHAPTER-BY-CHAPTER LOGICAL MAPPING

---

### CHAPTER 1: Introduction — The Question of Causation

**Core Claim:** Causal inference is fundamentally a problem of comparing potential outcomes in worlds that cannot both be observed. The question "did X cause Y?" for a single individual is insoluble; the question "does X cause Y, on average?" has a rigorous solution.

**Supporting Evidence:**
- George Washington's case: he was bled, he died. Whether bleeding caused his death is unknowable because we cannot observe the counterfactual world where he was not bled.
- The notation of potential outcomes (R_T and R_C for treated and control conditions) formalizes the comparison of two possible worlds for each individual.
- Kim and James thought experiment: even with a treatment group and a control group, naive comparison of two different people estimates no one's causal effect — it conflates person-level differences with treatment effects.
- The single fair coin flip over Kim and James is *unbiased* in expectation but useless in practice — either outcome yields the wrong answer.

**Logical Method:** Rosenbaum proceeds by progressive formalization: a historical case (Washington), a common-sense counterfactual, a notation system (Neyman-Rubin potential outcomes), and then a demonstration of why a control group alone is insufficient.

**Logical Gaps:**
- The chapter establishes that a control group is necessary but not sufficient without yet specifying what makes a control group adequate. The reader is left in suspense about the solution until Chapter 2.
- The casino-vs.-gambler analogy is deployed to suggest that repeated coin flips solve the estimation problem, but the chapter stops short of proving this. The argument is intuitive, not yet rigorous.
- The chapter asserts that for individual-level causal effects "this is and will remain a matter of speculation" without defending the asymmetry between population-level solvability and individual-level insolubility. The argument is correct but would benefit from more explicit treatment of what changes when you aggregate.

**Methodological Soundness:** The potential outcomes notation is a genuine methodological contribution, not just a pedagogical device. The chapter correctly identifies the fundamental identification problem. The Washington example is epistemically honest: it acknowledges that even had 18th-century physicians possessed the experimental habit of mind, the causal effect on Washington specifically would remain unknowable.

---

### CHAPTER 2: Randomized Experiments

**Core Claim:** Randomized treatment assignment solves the causal inference problem by ensuring that the actual world is a random draw from the space of possible worlds — making certain population averages in the observed world close to averages over all possible worlds.

**Supporting Evidence:**
- The PALM Trial (Democratic Republic of Congo, 2018–2019): 343 patients with Ebola virus disease randomized to ZMapp (n=169) or MAB114 (n=174).
- Survival rate: MAB114: 113/174 = 64.9%; ZMapp: 85/169 = 50.3%. Estimated ATE: +14.6 percentage points.
- Balance table: mean age 27.4 vs. 29.7 years; 51.5% vs. 56.3% female — differences attributable to chance, not systematic allocation.
- The probability of observing a survival difference as large as 14.6% under the null hypothesis of no effect: p = 0.0083 (less than 1 in 100).
- The coin-flip argument: over many pairs, the estimated ATE is unbiased; its variance decreases with sample size by the law of large numbers.

**Logical Method:** Two parallel arguments establish the value of randomization: (1) it balances observed covariates (demonstrated in the PALM balance table), and more importantly (2) it balances *unobserved* covariates, including those not yet discovered — because the coin knows nothing about person attributes. A third argument establishes randomization as the basis for testing the null hypothesis of no effect, converting an insoluble metaphysical question into a calculable probability.

**Logical Gaps:**
- The chapter proves the *unbiasedness* of the ATE estimator under randomization but does not discuss power explicitly — the sample size needed to achieve a given probability of detecting a true effect. The 343-patient PALM trial was underpowered to detect small effects, a limitation not addressed.
- The data-safety monitoring board's early termination of two arms is mentioned without analyzing the statistical implications of interim analyses. Interim stopping inflates Type I error if not pre-specified and adjusted for — a genuine methodological issue the chapter glosses.
- The proof that randomization balances unobserved covariates is argued by analogy (the coin knows nothing about attributes) rather than by formal proof. The argument is correct but could be made more precise.

**Methodological Soundness:** The PALM trial is a well-chosen example: a controlled trial with genuine equipoise, an external safety monitoring board, and a clear primary outcome. The treatment of ethics (equipoise, informed consent) is more rigorous than most causal inference textbooks. The statistical argument for testing the null hypothesis via permutation is mathematically sound.

---

### CHAPTER 3: Observational Studies — The Problem

**Core Claim:** When individuals select their own treatments (rather than being assigned by a fair coin), comparisons between treated and control groups may reflect differences in the people rather than differences in the treatments. The degree of selection bias can be measured and is often enormous.

**Supporting Evidence:**
- NHANES 2011–2012 periodontal disease study: 441 daily smokers vs. 1,506 never-smokers.
- Sex imbalance: 16.4% of women smoked vs. 30.4% of men — probability of a fair lottery producing this imbalance: 3.2 × 10⁻¹³ (functionally impossible by chance).
- Education: 7.1% of college graduates were smokers vs. 29.9% of non-graduates.
- Income: 12.1% of individuals with income ≥3× poverty level were smokers vs. 29.8% below that threshold.
- Combined: among women ≥60 with college degrees, 4.3% smoked; among men <60 without college degrees, 42.3% smoked — a nearly tenfold difference from just three covariates cut coarsely.
- Propensity score range: 3.2% to 64.5% probability of smoking across individuals — a more-than-twentyfold difference.

**Logical Method:** The chapter demonstrates the failure of naive observational comparison by progressively disaggregating the data: first one covariate at a time, then all together via propensity scores, to show that smokers and non-smokers are radically different before any outcome is considered.

**Logical Gaps:**
- The chapter establishes that smokers and non-smokers differ substantially on measured covariates, but does not yet ask whether these differences fully explain the observed outcome difference. This is deferred to Chapter 4.
- The propensity score is introduced without yet explaining how it is estimated or why matching on it works. The concept is deployed before being justified.
- The chapter frames selection bias as a problem requiring statistical solution, but does not discuss design-based alternatives (e.g., restricting the sample to a more homogeneous population) that might reduce unmeasured confounding structurally.

**Methodological Soundness:** The box plot introduction (Tukey's method) is genuinely pedagogically valuable — it gives the reader a tool to visualize selection bias before the inferential machinery is presented. The probability calculation (3.2 × 10⁻¹³) that a fair lottery would produce the observed sex imbalance is methodologically sound and persuasive.

---

### CHAPTER 4: Adjustments for Measured Covariates

**Core Claim:** Matching treated individuals to controls with similar observed covariates can remove visible differences between groups, thereby enabling more credible causal comparisons — though only for differences that are measured.

**Supporting Evidence:**
- After matching 441 smokers to 441 controls on propensity scores (derived from sex, age, income, education, race):
  - Sex balance: 50.8% male smokers vs. 49.9% male controls (consistent with random assignment, p=0.63).
  - The tenfold difference in smoking rates across demographic strata (4.3% vs. 42.3%) was eliminated: matched groups were approximately 50% smokers within every subgroup.
  - Propensity score distributions: before matching, medians far apart; after matching, virtually identical.
- Outcome comparison after matching: smokers still had substantially more periodontal disease than matched controls — median 12.4% vs. 1.2% disease locations in the unmatched comparison; the difference persisted post-matching.
- Propensity score theorem (informal): matching on the propensity score — a single derived variable — tends to balance all covariates used in computing it.

**Logical Method:** The chapter proves the propensity score's balancing property by an informal argument about coin vs. die people: if two individuals have the same propensity score but different raw covariate values, knowing the covariates does not help predict which received treatment — the propensity score has absorbed all the relevant information.

**Logical Gaps:**
- The propensity score is estimated from data; estimation error is acknowledged ("terrible estimation may not do what the true probabilities would") but not formally quantified. In practice, model misspecification of the propensity score is a major source of error that receives minimal treatment here.
- The chapter proves that matching balances covariates *included in the propensity score* but cannot balance unmeasured covariates — this critical limitation is stated but not formally bounded. How large could unmeasured imbalances be? Chapter 5 addresses this, but the gap is real here.
- The matched controls have slightly more periodontal disease than unmatched controls. The chapter acknowledges this without fully explaining it; the likely explanation is that higher-propensity-score controls were matched, and higher propensity scores may correlate with other disease risk factors. The observation matters because it shows matching is not variance-free.

**Methodological Soundness:** The propensity score argument is informally but correctly presented. The coin-people/die-people analogy is the book's most pedagogically effective analytical device. The matching result is genuine: the achieved balance is documented and credible.

---

### CHAPTER 5: Sensitivity to Unmeasured Covariates

**Core Claim:** Observational studies can never prove causation with the certainty of a randomized trial, but a sensitivity analysis can quantify how large an unmeasured confound would need to be to explain away an observed association — turning a qualitative objection into a falsifiable claim.

**Supporting Evidence:**
- Cornfield et al. (1959) — first sensitivity analysis: to explain away the 9× elevated lung cancer risk in smokers, an unmeasured covariate would need to be at least 9× more prevalent in smokers than non-smokers. No such covariate was found despite diligent search.
- Periodontal disease: a bias of Γ=2 (coin odds up to 2:1 in favor of treatment for any pair) would still yield p < 0.00018 for the observed association. A Γ=2 bias requires an unmeasured covariate that simultaneously increases odds of smoking 3-fold and odds of greater periodontal disease 5-fold.
- Smoking and lung cancer: insensitive to Γ=5 (a far larger implied confound than almost any plausible biological mechanism).
- Seatbelts: also insensitive to Γ=5.
- A contrasting unnamed study: sensitive to Γ=1.05 (a trivial bias would explain the finding), subsequently refuted by randomized trials.

**Logical Method:** The sensitivity parameter Γ is defined as the ratio of odds of treatment between the two members of a matched pair, allowing for arbitrary within-pair variation. If Γ=1, the study is randomized. At any Γ>1, the maximum p-value under the null hypothesis can be computed — this bounds how much the p-value could worsen if an unmeasured confounder of that magnitude existed.

**Logical Gaps:**
- The chapter establishes *what* a Γ sensitivity analysis says but does not derive *why* a 5-fold odds confound corresponds to Γ=2 via the specific formula (a confound that increases odds of smoking 3-fold and disease 5-fold produces Γ=2). The derivation is stated but not provided.
- The sensitivity analysis is applied to the matched comparison — it assumes the matching was successful on measured covariates. If the propensity score model was misspecified, the Γ values may be understated.
- The text compares insensitivity to bias as a proxy for "credibility" across studies (smoking/cancer vs. the unnamed sensitive study). This is correct as a heuristic but could mislead readers into thinking high Γ alone establishes causation. Large Γ means confounding is implausible; it does not mean causation is proven.

**Methodological Soundness:** The Γ framework is a genuine methodological contribution. Bross's argument that scientific criticism must meet the same standards as scientific claims — the "ground rules for statistical criticism" — is a substantive point about philosophy of science that this chapter handles with unusual care.

---

### CHAPTER 6: Quasi-Experimental Devices

**Core Claim:** When the most plausible counterclaims to an observational study can be anticipated, the study can be designed to resist them by including additional comparisons that undermine those counterclaims empirically.

**Supporting Evidence:**
- Azithromycin cardiac death study (Ray et al.): used two control groups — (1) untreated patients and (2) patients on amoxicillin. A single control (untreated) could not distinguish drug-induced cardiac death from infection-induced cardiac death. Adding the amoxicillin group, which shares the infection but not the drug, allowed that distinction. Azithromycin showed excess cardiac deaths compared to *both* control groups.
- EITC evaluation (Eissa and Liebman): 1.8% increase in workforce participation for eligible women (unmarried, less than high school, with children) after 1986 expansion. Counterparts (ineligible women) showed -2.3% and +0.9% — the treated group's increase substantially exceeded the counterpart trend, undermining the "general economic trend" counterclaim.
- Lead exposure / children's blood lead (Morton et al.): three separate comparisons — factory worker vs. control children, children by father's exposure level, children by father's hygiene. Each panel is individually fallible; all three together require three separate confounding mechanisms to explain away, rather than one.

**Logical Method:** Control-by-systematic-variation (Bitterman/Campbell): rather than measuring a suspected confounder and adjusting for it, the investigator finds two control groups that differ dramatically on that confounder. If the two control groups produce similar outcomes despite differing on the suspected confounder, the confounder loses explanatory power.

**Logical Gaps:**
- The chapter does not provide a formal framework for determining *which* counterclaims are most plausible before a study is designed. The analysis proceeds from intuition ("confounding by indication is common") rather than from a principled method for ranking anticipated confounders.
- The EITC counterpart analysis uses women who are explicitly *not comparable* to the treated group as comparison cases. The chapter calls them "counterparts" rather than "controls" to signal this. But the method's validity depends on the assumption that whatever general economic trend affected counterparts also affected the treated group — and this assumption is stated rather than tested.
- The "evidence factors" discussed at the chapter's end (Morton lead study) are described as yielding approximately independent comparisons from one dataset. The chapter acknowledges "technical aspects" that are deferred to references. This is a genuine conceptual gap in the exposition.

**Methodological Soundness:** The two-control-group design and the counterpart design are well-established methods, appropriately described. The azithromycin example is particularly clean because the two control groups directly address two alternative explanations simultaneously.

---

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

### CHAPTER 8: Replication, Resolution, and Evidence Factors

**Core Claim:** Scientific claims about causation are not resolved by repeating the same study with new data — they are resolved by demonstrating that the association holds across different study designs that are vulnerable to *different* biases.

**Supporting Evidence:**
- Drug addiction treatment (DARP, TOPS, DATOS): three large data collections, 10,000+ patients each, spanning 1969–2000. All found treatment reduces addiction. National Academy of Sciences critique: all three compared completers to dropouts — a fundamental selection problem. Repeating the same design, however many times, cannot resolve a structural bias.
- Smoking and lung cancer: association established across (1) case-control studies of smokers, (2) animal carcinogenicity studies of tobacco tars, (3) autopsy studies showing pre-cancerous lesions in smokers' lungs, (4) population-level correspondence between smoking uptake and lung cancer rates (including the 20-year lag in women after advertising campaigns). No single alternative explanation can account for all four types of evidence simultaneously.
- Morton lead study: three sequential comparisons from one dataset — worker vs. control children; high vs. medium vs. low paternal exposure; high-exposure fathers with good vs. poor hygiene. Technically structured so the three comparisons are approximately independent (evidence factors) despite sharing subjects. Three separate confounding mechanisms would be needed to explain all three findings.

**Logical Method:** The distinction between repetition and replication: repetition accumulates evidence under the same design vulnerability; replication changes the design to be vulnerable to different biases. If results persist across designs with different vulnerabilities, the probability that a single hidden bias explains all of them simultaneously decreases.

**Logical Gaps:**
- The chapter does not provide a formal criterion for how different two studies must be to count as "independent" replications. The intuition that smoke/cancer needed "unrelated explanations" to have multiple confounded origins is correct but informal.
- Evidence factors are described as approximately independent from the same dataset — the chapter defers to references for the formal proof. This is the chapter's most significant technical gap: readers cannot evaluate the independence claim without understanding the underlying structure.
- The drug addiction example is used as a cautionary tale about bad replication, but the chapter does not say what an *adequate* replication of addiction treatment studies would look like. What alternative designs would address the completer/dropout selection problem?

**Methodological Soundness:** The smoking/lung cancer example is genuinely persuasive: the diversity of evidence types, including epidemiological, laboratory, autopsy, and natural experiment approaches, is well-documented and the argument from that diversity is logically sound.

---

### CHAPTER 9: Uncertainty and Complexity

**Core Claim:** The question of whether low daily alcohol consumption is beneficial or harmful illustrates the full complexity of causal inference in observational settings: effect sizes are small, confounding is plausible, Mendelian randomization yields a different answer than adjusted observational analyses, and the honest answer is that the matter is unresolved.

**Supporting Evidence:**
- Meta-analyses and large studies have "failed to show an all-cause mortality benefit for low-volume alcohol use compared with abstinence" (LaCante et al., Journal of Clinical Oncology, 2018).
- Mendelian randomization (Holmes et al.): carriers of the ALDH1B1 gene variant associated with lower alcohol consumption had more favorable cardiovascular profiles. Conclusion: even light-to-moderate alcohol increases cardiovascular risk.
- The J-curve controversy: Panel A (monotone harm) vs. Panel B (J-curve benefit at low doses). The panels differ only at low doses — precisely where effect sizes are small and sensitivity to confounding is highest.
- Swedish study (Peterson et al., 1982): Swedish men who abstained had high mortality, but most abstainers had chronic disease *as the reason for abstention* — sick quitters bias the abstainer mortality rate upward, creating an artifactual apparent benefit of drinking.
- Seventh-day Adventists: healthy abstainers but confounded by non-smoking and vegetarian diet — not a clean comparison to drinkers.

**Logical Method:** Rosenbaum uses the alcohol case to demonstrate the full logical structure of a hard observational problem: the confound is plausible (sick quitters), the effect is small and thus highly sensitive to small biases (Chapter 5 logic applied implicitly), different methodologies yield conflicting answers (observational studies vs. Mendelian randomization), and genetic heterogeneity may mean the "true" causal effect varies across people.

**Logical Gaps:**
- The chapter does not apply the Γ sensitivity analysis from Chapter 5 to the alcohol case. This is a missed opportunity: quantifying how large a confound would be needed to explain the J-curve would integrate the book's analytical machinery with its final empirical puzzle.
- The Mendelian randomization result (Holmes et al.) is discussed as yielding a "different answer" from adjusted observational studies, but the chapter does not explain *which assumptions* must be wrong for the two methods to disagree. If both are valid instruments, they should agree; they don't, which implies at least one identifying assumption is violated.
- The Peterson (1982) finding — that sick quitters contaminate the abstainer category — is stated as an important insight but is not followed through to its implication: it would require a study that separately analyzes "voluntary healthy abstainers" vs. "medically forced abstainers." The chapter does not report whether such a study exists or what it found.

**Methodological Soundness:** The chapter is admirably honest about uncertainty. The conclusion — "time will tell, or maybe not" — is intellectually appropriate for a genuinely unresolved question. The sentence "our sentiments can infect our evidence" is the book's most important epistemological claim, and the alcohol example illustrates it concretely: the beverage carries cultural weight that clouds dispassionate analysis.

---

### BRIDGE: Synthesizing the Logical Architecture

The book's argument moves from axiom to method to limit — a deductive structure that earns its uncertainty rather than evading it.

**The central logical spine:** Causal inference requires comparing potential outcomes in two worlds that cannot both be observed. Randomization solves this by making the observed world a random draw from all possible worlds. When randomization is infeasible, the investigator must work backward: adjust for measured confounds, quantify sensitivity to unmeasured confounds, seek natural experiments that introduce genuine randomness, and triangulate across designs with different vulnerabilities. None of this achieves the certainty of randomization. It achieves credibility proportional to the diversity and independence of evidence.

**Three tensions that run across all chapters:**

*Tension 1: Individual causation vs. population causation.* The book opens with Washington and closes with an individual smoker's glass of wine. In between, all inferential machinery operates at the population level. The individual causal question — "did this drug kill this patient?" — is declared permanently insoluble in Chapter 1 and never revisited. This is methodologically honest but leaves a philosophical gap: courts, clinicians, and policymakers routinely must make causal attributions for specific cases. The book's tools are adequate for policy; they are insufficient for liability.

*Tension 2: The enemy of good is perfect.* The book consistently argues that demanding randomization as the only valid basis for causal inference is epistemically wrong — it would require ignoring the causal link between smoking and cancer. But the book also insists that observational evidence is always potentially contaminated by unmeasured confounding. The resolution proposed (Γ sensitivity, diverse replications) is the right one, but the boundary between "good enough" observational evidence and "not good enough" is never formalized.

*Tension 3: The selection problem and its solutions.* Every chapter from 3 through 9 is a variation on a single theme: the people who receive a treatment differ systematically from those who do not. Each chapter offers a partial solution — matching, sensitivity analysis, quasi-experimental devices, natural experiments, genetic instruments. But these solutions are cumulative, not substitutable. A Γ analysis does not replace good matching; a natural experiment does not replace sensitivity analysis. The book's implicit claim is that the most credible observational studies deploy all of these tools simultaneously, but this is never stated as a formal checklist.

**The book's most proven claims:**
- Randomization eliminates unmeasured confounding — by construction, not by statistical correction.
- The potential outcomes framework is the correct formalization of causal questions.
- The Γ sensitivity framework correctly quantifies how large a confound must be to explain an association.
- The smoking-lung cancer association meets extremely high standards of robustness (Γ > 5 across multiple methodologies).

**The book's most significant unproven claims:**
- That the Γ framework is routinely adequate for general observational inference (limitations of the original Cornfield method are acknowledged; the generality of modern methods is asserted more than proven).
- That comparing estimates across "independent" evidence factors from the same dataset is statistically valid (deferred to references throughout).
- That the EITC counterpart method provides credible causal evidence (the critical assumption — that counterpart trends proxy the treated group's counterfactual trend — is stated, not tested).

**The book's deepest acknowledged limitation:**
The entire inferential apparatus presupposes that the investigator knows which confounders are plausible. The selection of covariates to measure, the construction of propensity scores, the choice of which counterclaims to anticipate — all require domain knowledge that no statistical method can supply. The book explicitly acknowledges this at multiple points ("the study of CTLA4 requires knowing that CTLA4 is worth studying") but offers no guidance on how to build that knowledge. This is not a flaw in the book; it is an honest description of the limit of the discipline.

---

## PART 2: LITERARY REVIEW ESSAY

---

# The One World We Got

There is a thought experiment at the center of Paul Rosenbaum's *Causal Inference* that most readers will pass through in under five minutes, then spend years thinking about. George Washington, December 1799. A sore throat. Physicians bleed him, twice, three times, until he has lost approximately half his blood volume. He dies. The question Rosenbaum poses is simple: did the bleeding cause his death?

The answer, he argues, is that we cannot know. Not because our biology is inadequate, though it was. Not because the historical record is incomplete, though it is. But because answering that question requires comparing the world in which Washington was bled to the world in which he was not — and we have only one of those worlds. We saw the one where he was bled. The other is gone.

What follows is a 200-page argument about how to reason carefully when you only have one world to work with. It is, quietly, one of the more philosophically serious books in quantitative social science.

---

Rosenbaum belongs to a tradition that traces its formal lineage to Jerzy Neyman's 1923 dissertation and Donald Rubin's subsequent development of the potential outcomes framework. The notation is deceptively simple: R_T is the outcome a person would experience if treated, R_C is the outcome if not treated, and the causal effect is R_T − R_C. The simplicity conceals a conceptual depth that has taken the field decades to absorb. The causal effect is defined *for a specific individual*, as the difference between two worlds that person would inhabit. But every individual inhabits only one world. We observe R_T or R_C, never both.

This is the fundamental problem of causal inference, which Rosenbaum calls the problem of missing data — the most consequential missing data problem in all of science. The data we need to compute a causal effect are, in principle, impossible to observe for any individual. The data we need to estimate average causal effects *across individuals* are sometimes obtainable, under specific conditions, through methods that Rosenbaum develops with unusual clarity.

The central solution — randomization — works by making the world we observe a random draw from all possible worlds. In the PALM trial for Ebola treatments, 343 patients were assigned to two drugs by coin flip. Because the coin ignored everything about each patient (age, severity, sex, genetics, luck), the patients who received MAB114 and those who received ZMapp were, in expectation, identical in every respect. Any difference in survival could therefore be attributed to the drugs. MAB114's 14.6 percentage point survival advantage — and the p-value of 0.0083 against the null hypothesis of no difference — is not "suggestive" or "consistent with" effectiveness. It is, within the framework Rosenbaum has built, a legitimate estimate of the average treatment effect.

The precision of this claim matters. Rosenbaum is doing something unusual for a methods book: he is not just teaching statistical techniques, he is arguing that some methods *license* causal conclusions and others do not. The randomized trial licenses a causal conclusion because the identification problem is solved by design. The observational study does not solve it by design — it attempts to solve it by analysis, and the solution is always partial.

---

The book's most philosophically interesting moment comes not in the chapter on experiments but in the chapter on sensitivity analysis.

By Chapter 5, Rosenbaum has established that observational studies face an inevitable objection: you adjusted for observed confounders, but what about the ones you didn't measure? This objection, if accepted uncritically, implies that no observational study can ever establish causation — a conclusion that would require rejecting the overwhelming evidence that smoking causes lung cancer, for instance. Rosenbaum is not willing to accept this.

His response is the Cornfield-Γ framework. Instead of asking whether unmeasured confounding *could* explain an association, the framework asks how *large* an unmeasured confound would need to be to explain it. For the lung cancer association (smokers have 9× the risk of non-smokers), any unmeasured confound would need to be at least 9× more prevalent in smokers — a requirement that no proposed genetic or behavioral factor has met after 70 years of searching. The association is, in Rosenbaum's terminology, *insensitive* to large biases.

I find this framework genuinely powerful, and its philosophical implications are undervalued in the book's presentation. What the Γ analysis establishes is not that smoking *definitely* causes lung cancer — that conclusion requires the full weight of evidence from multiple methodologies. What it establishes is a *standard for the critic*. A critic who claims the observational association is spurious must identify a specific unmeasured confound at least 9× more prevalent in smokers. Generalized skepticism — "there might be some unmeasured factor" — is no longer an adequate objection. The burden of proof has shifted.

This is, implicitly, a contribution to the epistemology of science that extends well beyond causal inference. Irwin Bross put it precisely in a passage Rosenbaum cites: "Since the counterhypothesis is essential in the logical structure of criticism, it facilitates debate when it is explicitly stated. The critic has the responsibility for showing that his counterhypothesis is tenable." Rosenbaum endorses this standard and operationalizes it through Γ. Scientific objections must earn their credibility, just as scientific claims must. The tobacco industry's decades of manufactured doubt were epistemically illegitimate not because they were untrue — the evidence was genuinely probabilistic — but because they raised unspecified objections while simultaneously knowing that specific objections did not survive scrutiny. The Γ framework makes this bad faith visible.

---

The book's structural conceit is a progressive relaxation of the randomization assumption. Chapter 2 gives you the ideal world: coins, equipoise, ethics committees, data safety monitoring boards. Chapter 3 takes it away. Chapters 4 through 8 give you increasingly sophisticated methods for recovering some of what was lost.

What is recovered, and what is not, deserves careful accounting.

Propensity score matching (Chapter 4) removes visible differences between treated and control groups on measured covariates. This is valuable — the demonstration that 441 smokers and 441 matched non-smokers become nearly exchangeable on five covariates is methodologically clean. But the residual periodontal disease difference (smokers still have dramatically more disease than matched controls) could reflect unmeasured confounding. Matching on the observed propensity score does not bound the size of unmeasured confounding; it merely removes the confounding we can see.

Sensitivity analysis (Chapter 5) then quantifies how large that residual confounding would need to be. For the periodontal data, even a Γ=2 bias (2:1 odds advantage for smokers in receiving the "treatment" of being a smoker) would yield p < 0.00018 under the null hypothesis. This is an extremely demanding threshold for confounding — a residual factor that simultaneously tripled the odds of being a smoker *and* substantially increased periodontal disease would still not explain the observed association.

Natural experiments and instrumental variables (Chapter 7) take a different path entirely. When a lottery randomly assigns housing vouchers, the randomization is partial — it randomizes the offer, not the acceptance. The complier average causal effect (CACE) framework recovers the effect of acceptance by restricting attention to the subset of people whose behavior was actually changed by the offer. This is a precise and valid estimation strategy, but it estimates the effect for a specific sub-population (compliers) who may differ systematically from the broader population. The generalizability of CACE estimates is a limitation that Rosenbaum acknowledges without fully quantifying.

Evidence factors (Chapter 8) attempt to achieve through design what matching achieves through analysis: multiple comparisons that are approximately independent, so that a single unmeasured confound cannot explain all of them. The Morton lead-exposure study — worker vs. control children, then children stratified by paternal exposure level, then children stratified by paternal hygiene — is the book's best illustration of this principle. Three separate patterns, each individually fallible, together requiring three independent explanations to dismiss. The probability that all three share the same unmeasured source of bias is substantially lower than the probability for any one.

---

There is one question the book raises but does not answer: when is the full toolkit sufficient?

Rosenbaum's smoking-lung cancer case passes every test he has developed. The association is enormous. It is insensitive to bias at Γ=5. It replicates across five distinct methodological traditions, each with different vulnerabilities. No specific alternative explanation has survived scrutiny. The scientific community has, correctly, concluded that the causal claim is established.

But the alcohol case — the book's concluding example — does not. The association is small and inconsistent across methods. The J-curve benefit at low doses is sensitive to modest biases (the sick-quitter confound is plausible and quantitatively adequate to explain the finding). Mendelian randomization yields the opposite conclusion from adjusted observational analyses. The honest conclusion, which Rosenbaum reaches, is that the causal question remains open.

What the book does not give us is a formalized criterion for the middle ground — for the many scientific questions where evidence is stronger than the alcohol case but weaker than the smoking case. In practice, this is where most important policy questions live. The causal effect of preschool education on adult outcomes. The causal effect of social media on adolescent mental health. The causal effect of minimum wage increases on employment. These questions have received serious observational, quasi-experimental, and (where possible) experimental attention. They are not unresolved like alcohol, nor settled like tobacco. They occupy a space for which the book's toolkit provides tools but no decision rule.

This is not a criticism of the book so much as an honest description of where the discipline stands. Causal inference has made enormous methodological progress in the past half-century. It has produced frameworks that make the identification problem precise, that separate credible from incredible observational evidence, that bound the role of unmeasured confounding. What it has not produced — and perhaps cannot — is an algorithm for certainty. The space between "suggestive" and "definitive" must still be navigated by judgment: judgment about which confounds are plausible, which methodologies are applicable, which replications are sufficiently independent.

Rosenbaum closes with the admission that the alcohol question may never be resolved. This is not defeatism. It is the experimental habit of mind, honestly applied. Some questions have answers we can reach; some do not. The value of the framework is that it tells us which is which.

We got one world. The question is how carefully we can read it.

---

**Tags:** causal inference potential outcomes, Neyman-Rubin framework observational studies, propensity score matching confounding, sensitivity analysis Gamma framework, natural experiments instrumental variables
