### CHAPTER 12: Terra Incognita
**Core Claim:** Modern overparameterized deep neural networks violate classical bias-variance tradeoff theory—they can interpolate noisy training data and still generalize well to test data, a phenomenon called "double descent" that standard ML theory cannot explain.

**Supporting Evidence:**
- Neyshabur et al. (2015): increasing hidden layer neurons past the interpolation threshold does not increase test error; test error continues *decreasing*
- Zhang et al. (2016): "Understanding Deep Learning Requires Rethinking Generalization"; networks large enough to memorize training data still generalize; explicitly introduced random label noise
- Belkin et al. (double descent): test error follows a U-curve (classical regime), reaches a maximum at the interpolation threshold, then *descends again* in the overparameterized regime
- Grokking (Power et al., OpenAI): network trained on modular addition *long past* zero training error suddenly generalizes—as if "understanding" the operation with delayed onset
- Self-supervised learning (LeCun lineage → MAE): masks portions of training images; network learns to reconstruct; no human labels required; Masked Autoencoders (He et al., 2021) outperform supervised RCNN on object detection after fine-tuning

**Logical Method:** Empirical anomalies → catalog of violations → theoretical frameworks → open questions.

**Logical Gaps:**
- The chapter catalogs empirical violations of classical theory extensively but offers no confirmed theoretical explanation for any of them. "Implicit regularization by stochastic gradient descent" is proposed as a hypothesis for why overparameterized networks don't overfit, but the author notes this remains unproven. The chapter's title—"Terra Incognita"—is honest about this, but the reader is left in a frustrating explanatory vacuum.
- Grokking is presented as an intriguing phenomenon but its mechanistic explanation remains entirely open. The OpenAI team's speculation that the network "internalized" an operation is phenomenological, not mechanistic. The chapter treats it as suggestive evidence of something interesting without being able to say what.
- The double descent curve is presented as a "unifying principle" but the author does not show that the mechanism producing double descent in kernel machines is the same as the mechanism in neural networks. The unification claim is empirical, not theoretical.

**Methodological Soundness:** All cited results (Neyshabur, Zhang, Belkin, Power) are documented peer-reviewed work. The chapter is appropriately honest about theoretical uncertainty. The framing as "Terra Incognita" is accurate.

---
