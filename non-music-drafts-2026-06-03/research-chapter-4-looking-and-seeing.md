### CHAPTER 4 (Chapter 2 in audio numbering): Looking and Seeing

**Core Claim:** Object recognition—once assumed to be tractable—is one of AI's hardest problems. Convolutional neural networks (ConvNets) have produced stunning gains, but their performance involves learning *different things* from what humans learn, which is why they fail in ways humans don't.

**Supporting Evidence:**
- The Summer Vision Project (1966): Minsky assigns an undergraduate to "solve" vision in a summer; it wasn't solved in fifty years
- The ImageNet challenge: 1.2 million labeled training images, 1,000 categories; best support-vector-machine performance in 2011 was 74% top-5 accuracy
- AlexNet (2012): 85% top-5 accuracy, a 15-point jump, using a ConvNet with ~60 million learned weights
- ConvNet architecture derived from Hubel and Wiesel's Nobel Prize-winning discovery of hierarchical organization in the mammalian visual cortex: edge detectors → shape detectors → object detectors
- "Convolution" defined precisely: each unit multiplies input pixels by its weights and sums; the same weights slide across the entire input map

**Logical Method:** Technical exposition of ConvNet architecture anchored in neuroscience derivation; empirical performance benchmarks.

**Logical Gaps:**
- The chapter establishes that ConvNets work without yet establishing *why* they learn differently from humans. The mechanism—that they pick up statistical correlates in training data rather than causal structure—is introduced but not yet foregrounded.
- ImageNet's category taxonomy (1,000 categories, many obscure: "hussar monkey," "ready-turned stone") biases the comparison: human performance was measured on a single human (Andrej Karpathy), and he studied only 1,500 images after training on 500.

**Methodological Soundness:** The "machines surpass humans at ImageNet" claim is properly deconstructed: top-5 accuracy (not top-1), one human tester, restricted domain, artificial conditions.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-4-looking-and-seeing.md`

Key additions: ImageNet success was real but benchmark-specific. Top-5 accuracy, category design, single-human baselines, and artificial task conditions must be explained before saying machines surpassed humans at vision.

Settled: CNNs and successor architectures transformed computer vision. Contested: how similar machine visual representations are to human perception and how robust they are out of distribution.

Teaching move: ask which humans, which task, what metric, what categories, and what failure distribution.
