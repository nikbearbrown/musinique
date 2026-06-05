### CHAPTER 5 (Chapter 6 in audio): A Closer Look at Machines That Learn

**Core Claim:** Deep learning does not "learn on its own" in any meaningful sense—it requires massive human labor for data curation, hyperparameter tuning, and architectural design. The learning it does is also fundamentally different from human learning: it overfits to statistical patterns in training data, creates brittle classifiers vulnerable to adversarial examples, and produces systems that cannot explain their decisions.

**Supporting Evidence:**
- The "blurry background" example: Will Landecker's network learned to classify images with blurry backgrounds as "contains animal" because nature photographers focus on animals and blur backgrounds—not because it recognized animals
- Will's network's learned association holds until you give it an animal in a non-blurry context, then performance plummets
- Adversarial examples (Szegedy et al., 2013): pixel-level perturbations imperceptible to humans cause AlexNet to classify a school bus as an ostrich at high confidence
- The Wyoming group: genetic algorithm evolves images that look like random noise to humans but that AlexNet classifies as recognizable objects with >99% confidence
- Google's Photos app (2015): classified two African Americans as gorillas
- Kate Crawford's finding: widely used face recognition training datasets are 77.5% male and 83.5% white

**Logical Method:** Controlled demonstration of failure modes + documented real-world consequences.

**Logical Gaps:**
- The chapter correctly identifies overfitting and adversarial vulnerability as distinct problems (the first is about generalization; the second is about manipulation), but does not fully develop the connection: both stem from networks learning *correlates* rather than *causes*.
- The "explainable AI" research direction is introduced but not evaluated. As of 2019, no deep learning system had successfully explained itself in human terms—but Mitchell does not explore whether such explanation is even possible in principle.

**Methodological Soundness:** This is the book's analytically strongest chapter. The distinction between performance on a benchmark and learning the underlying concept is made with evidence, not assertion.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-5-a-closer-look-at-machines-that-learn.md`

Key additions: deep learning is human-designed around data, labels, architecture, objectives, and tuning. Shortcut learning, adversarial examples, fooling images, and biased datasets all show that confidence and benchmark performance are not understanding.

Settled: deep networks are vulnerable to shortcut learning, adversarial examples, and dataset bias. Contested: how much robustness, interpretability, and causal representation can be achieved with current methods.

Teaching move: ask what evidence would prove the model learned the target concept rather than a shortcut.
