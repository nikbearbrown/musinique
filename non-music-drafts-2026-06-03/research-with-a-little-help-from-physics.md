### CHAPTER 8: With a Little Help from Physics
**Core Claim:** Hopfield networks—artificial neural networks with symmetric bidirectional weights—are dynamical systems that store memories as energy minima, and their energy landscape provides the first rigorous model of associative memory in neural networks.

**Supporting Evidence:**
- Ising model of ferromagnetism: spins aligned → minimum energy; Hamiltonian H = -Σij J·σi·σj - Σi h·σi
- Hopfield's 1982 PNAS paper: symmetric weights → stable states guaranteed; energy function defined analogously to Ising Hamiltonian
- Hebbian learning rule: Wij = Yi·Yj (outer product of stored pattern); proven to make stored patterns stable states
- Storage capacity: network of N neurons can store at most 0.14N memories without interference
- Demonstration: 784-neuron network trained on images of digits 5 and 8; given noisy input, retrieves stored pattern

**Logical Method:** Physics analogy → mathematical formalization → stability proof → demonstrated application.

**Logical Gaps:**
- The storage capacity bound (0.14N) is stated as Hopfield's result without derivation or source citation. This is the key quantitative claim in the chapter and it is presented without support. The author notes "modern Hopfield networks" have increased this capacity but does not explain the mechanism.
- Hopfield networks are one-shot learners. The chapter acknowledges this but does not connect it to the broader training problem. The segue from "Hopfield networks can store a memory given one presentation" to "we need incremental learning for real-world tasks" is stated, not argued. The narrative gap is small but the conceptual gap is not.

**Methodological Soundness:** The energy function, stability proof, and Hebbian learning rule are mathematically accurate. The Ising model analogy is sound. The 784-neuron demonstration is a standard educational illustration.

---
