### CHAPTER 5: Birds of a Feather
**Core Claim:** The K-Nearest Neighbor (KNN) algorithm—inspired by Al-Hazen's 11th-century theory of visual recognition—can classify data with error approaching the Bayes Optimal Classifier's lower bound as sample size grows, without making any distributional assumptions.

**Supporting Evidence:**
- John Snow's 1854 cholera map: Voronoi cells as early nearest-neighbor analysis
- Al-Hazen (~1000 CE): "when sight perceives some visible object, the faculty of discrimination immediately seeks its counterpart among the forms persisting in the imagination"
- Cover-Hart (1967) proof: 1-NN rule's error is bounded above by 2× Bayes error; KNN as K increases and K/N remains small approaches Bayes optimal
- Non-parametric property: KNN stores all training data; no fixed parameter count; grows with data
- Curse of Dimensionality (Bellman 1957): in high-dimensional spaces, data becomes sparse; the fraction of the unit hypercube covered by any fixed volume shrinks exponentially with dimension

**Logical Method:** Historical example → algorithmic formalization → theoretical bounds → limitation analysis.

**Logical Gaps:**
- The Cover-Hart proof bound (1-NN error ≤ 2× Bayes error) is stated but the factor of 2 is presented without intuition. The underlying reason—that the 1-NN algorithm is effectively flipping a biased coin rather than always choosing the most likely class—is sketched but not fully developed. A reader cannot reconstruct why the bound is 2× rather than some other multiple.
- The curse of dimensionality section correctly identifies the problem but the proposed solution—"increase sample size exponentially with dimensions"—is noted as impractical without discussing the empirical observation that deep neural networks *seem to circumvent this curse*. This sets up Chapter 12, but the gap is felt here.

**Methodological Soundness:** The Cover-Hart convergence result is a documented mathematical finding. The curse of dimensionality is a real and documented phenomenon.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-birds-of-a-feather.md`

Key additions: KNN is memory-based classification whose success depends on representation and metric. Cover-Hart gives the classic asymptotic guarantee, while the curse of dimensionality explains why "nearest" can become meaningless in raw high-dimensional spaces.

Settled: KNN is theoretically well understood and nonparametric. Contested: how high-dimensional learning succeeds in practice, since learned representation and intrinsic dimension often matter more than raw feature count.

Teaching move: classify examples in one dimension, two dimensions, and then a high-dimensional space where all points become similarly distant.
