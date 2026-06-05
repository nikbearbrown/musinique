### CHAPTER 2: Algorithms and Turing Machines
**Core Claim:** A Turing machine is the correct formal model of mechanical computation. The Church–Turing thesis asserts that any effectively computable function can be computed by a Turing machine. The halting problem is unsolvable: no algorithm can decide, for all Turing machines and inputs, whether the machine will stop.

**Supporting Evidence:**
- Detailed construction of Turing machines (UN+1, UN×2, Euclidean algorithm machine).
- Cantor's diagonal argument adapted to show that no Turing machine H can decide whether an arbitrary Turing machine Tn halts on input M.
- Church's lambda calculus and Post's formulation shown to be equivalent to Turing computability—reinforcing the universality of the concept.

**Logical Method:** Formal mathematical proof of the halting problem via reductio. The diagonal argument is made explicit.

**Logical Gaps:**
- The Church–Turing thesis is presented as almost certainly correct but acknowledged as a *thesis*, not a theorem. The gap between "all known models of computation are equivalent" and "this is all that computation can ever be" is real and acknowledged briefly.
- The proof of the halting problem's unsolvability is presented as establishing that humans can "outdo" any specific algorithm—but this conflates "for any given algorithm, we can construct a case it cannot handle" with "human reasoning is non-algorithmic." Penrose uses this conflation as the bridge to Chapter 4, but it does not yet support the conclusion he draws there.

**Methodological Soundness:** The formal content is sound. The informal glosses—particularly the anthropomorphic language around algorithms "knowing" things—introduce equivocations that will become significant in Chapter 10.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-algorithms-and-turing-machines.md`

Key additions: Turing machines formalize effective procedure; the Church-Turing thesis is a thesis supported by convergence among formal systems, not a theorem; the halting problem proves a limit on algorithms, not human transcendence.

Settled: standard computability and halting result. Contested: philosophical scope for minds and physical computation.

Teaching move: use a tiny machine first, then diagonalization; avoid anthropomorphic language like "the machine knows."
