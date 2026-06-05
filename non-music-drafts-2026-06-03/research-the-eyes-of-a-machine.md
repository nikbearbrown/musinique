### CHAPTER 11: The Eyes of a Machine
**Core Claim:** Convolutional Neural Networks (CNNs) implement the hierarchical visual processing structure proposed by Hubel-Wiesel, and training CNNs with backpropagation allows them to *learn* edge-detecting kernels rather than having them hand-designed.

**Supporting Evidence:**
- Hubel-Wiesel (1960s): edge-detecting simple cells → translation-invariant complex cells → hyper-complex cells; receptive fields grow larger up the hierarchy
- Fukushima's Neocognitron (1980): S-cells and C-cells model simple and complex cells; learned translation invariance; training algorithm was Hebbian, not backprop
- LeCun's LeNet (late 1980s/early 1990s): convolutional layers + max-pooling + fully connected output; trained with backprop on USPS handwritten digits
- Convolution operation: kernel slides across image; each position computes a dot product → output map; multiple kernels detect multiple features
- Max-pooling: reduces spatial resolution; increases receptive field of subsequent neurons; provides translation invariance

**Logical Method:** Biological motivation → computational architecture → learning algorithm → empirical application.

**Logical Gaps:**
- The chapter claims CNNs "implement" Hubel-Wiesel hierarchy but does not quantify the degree of correspondence. Chapter 12 addresses this in the neuroscience context (Yamins 2014 Ventral Stream study), but here the biological claim is architectural, not functional. Simple and complex cells in the brain are *not* exactly convolutional layers—they have lateral inhibition, top-down feedback, and other properties CNNs lack. The analogy is informative but the chapter presents it as more literal than the neuroscience supports.
- The transition from LeNet's success on USPS digits to its failure to scale to high-resolution images is mentioned but not fully analyzed. The author says "there were signs that there was an issue of scale"—but the mechanism (insufficient compute for large matrix multiplications, insufficient training data) is gestured at rather than explained. This creates a narrative ellipsis before Chapter 12's AlexNet discussion.

**Methodological Soundness:** The convolution operation is mathematically accurate. LeCun's historical contributions are documented. The Hubel-Wiesel work is Nobel Prize-winning science.

---
