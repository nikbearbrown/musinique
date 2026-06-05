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
