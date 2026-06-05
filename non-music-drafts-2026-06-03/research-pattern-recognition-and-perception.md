### CHAPTER 6: PATTERN RECOGNITION AND PERCEPTION

**Core Claim:** The three-operation framework (dimensionality expansion, sparse coding via lateral inhibition, recurrent auto-associative completion) is the conserved vertebrate solution to the discrimination-generalization-invariance trade-off, present in essentially modern form in the lamprey 500 million years ago. CNNs copied the feedforward hierarchy and left out the recurrent completion and sparse coding—which explains their specific failure modes.

**Supporting Evidence:**
- Suryanarayana et al. 2017 lamprey pallium comparative anatomy
- DeLong et al. goldfish object rotation recognition
- Archerfish 81% accuracy on 44-person face lineup (University of Queensland 2016)
- Yamins & DiCarlo CNN top-layer prediction of IT neuron firing
- Geirhos texture-bias finding (shape vs. texture in ImageNet-trained networks)
- Betty's Brain / Leelawong & Biswas 2008 concept map learning (briefly mentioned)

**Logical Gaps:**
- The goldfish faster-on-upside-down asymmetry is honestly flagged as not-fully-understood—excellent ISE practice. But the chapter proceeds without proposing a testable mechanism, which weakens the pedagogical payoff.
- The claim that standard CNNs fail on relational reasoning because they "encode features of parts but not relations between parts" is stated but not mechanistically unpacked. Relational reasoning is an entire subfield; the dismissal in one paragraph risks misleading readers into thinking the problem is well-understood when it is contested.
- The three-operation framework is presented as both describing the vertebrate system and explaining the CNN gap. These are two different claims: the first is descriptive biology, the second is a causal engineering claim. The causal claim would require showing that adding recurrent completion and sparse coding to CNNs *actually closes the performance gap*—which some work suggests (capsule networks, predictive coding models) but which is not settled.

**Methodological Soundness:** Good for the biological description. The engineering-gap claim is underdetermined by the evidence presented.

---
