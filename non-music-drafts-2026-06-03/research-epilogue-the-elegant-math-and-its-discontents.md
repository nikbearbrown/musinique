### EPILOGUE: The Elegant Math and Its Discontents
**Core Claim:** LLMs are trained as next-token predictors over probability distributions on language; their apparent cognitive abilities (theory of mind, math reasoning) are empirically impressive but theoretically unexplained; risks of bias and overconfidence are documented and serious.

**Supporting Evidence:**
- GPT-4 theory of mind demonstration: correctly infers Alice will use wrong glasses because Bob switched them without her knowledge
- Self-supervised training: mask word → predict word → calculate loss → backprop; scales to internet corpus
- Emergent behavior: GPT-2 (1.5B parameters) lacks theory of mind; GPT-3 (175B parameters) shows hints; scaling produces qualitative capability changes not predictable from smaller models
- AI bias cases: Google Photos (2015) mislabeled Black users as gorillas; ProPublica COMPAS recidivism algorithm; Amazon hiring AI penalizing female applicants; health care algorithm underestimated Black patient risk
- Yamins-DiCarlo (2014): CNN layers predict ventral visual stream activity in macaques; "anatomical consistency" between artificial and biological hierarchies

**Logical Method:** Demonstration → mechanistic explanation → capability assessment → risk inventory → neuroscience correspondence.

**Logical Gaps:**
- The theory of mind demonstration with GPT-4 is cherry-picked. The author acknowledges LLMs "often spit out wrong answers, sometimes obviously wrong," but does not provide a rigorous failure-mode analysis. A single successful case followed by a caveat is not a measurement of capability.
- The "emergent behavior" discussion conflates two claims: (1) behaviors appear at scale that were not present at smaller scale, and (2) those behaviors represent qualitatively different cognitive capacities. Claim (1) is empirically documented. Claim (2) is contested. The Epilogue presents both with similar confidence.
- The neuroscience correspondence (Yamins et al.) is presented in the strongest possible terms ("shocking specificity in the functional match" per Kanwisher). But the author also includes the caveat "we should take all these correspondences...with a huge dose of salt." The chapter is appropriately uncertain but the organization oscillates between enthusiasm and qualification without resolving the tension.

**Methodological Soundness:** Bias examples are documented peer-reviewed and journalistic investigations. The Yamins result is published in a peer-reviewed journal. The LLM training description is accurate.

---
