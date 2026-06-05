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
