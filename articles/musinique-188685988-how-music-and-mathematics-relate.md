---
title: "How Music and Mathematics Relate"
subtitle: "David Kung (Great Courses) | 12 Lectures"
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: "188685988.how-music-and-mathematics-relate"
post_date: "2026-02-21T04:39:06.696Z"
is_published: "true"
source_zip: "Y0r_0oGOSoWMD3iEcEhVnA.zip"
source_html: "posts/188685988.how-music-and-mathematics-relate.html"
source_file: "musinique-188685988-how-music-and-mathematics-relate.md"
cover_image: "https://substack-post-media.s3.amazonaws.com/public/images/2bcc597d-97c1-46f9-8b45-8ff61d9c0464_1500x1500.jpeg"
---
![](https://substack-post-media.s3.amazonaws.com/public/images/2bcc597d-97c1-46f9-8b45-8ff61d9c0464_1500x1500.jpeg)

## PART 1: SECTION-BY-SECTION LOGICAL MAPPING

---

### LECTURE 1: Overtones — Symphony in a Single Note

**Core Claim:** A single vibrating string produces not one frequency but a symphony of frequencies (overtones) in arithmetic sequence; differential equations predict this result quantitatively.

**Supporting Evidence:**

- Spectrum analyzer on a 440A violin string shows peaks at 440, 880, 1320, 1760 Hz—multiples of the fundamental
- Jump rope demonstration physically instantiates the modes (fundamental, 2nd harmonic, 3rd harmonic) showing nodes and antinodes
- Formula f = (1/2L)√(T/ρ) derived from the wave equation (Newton’s second law + boundary conditions) and confirmed: lower G string is ~10× heavier than E string, approximately matching observed frequency ratio
- Timpani contrasted: two-dimensional membrane produces non-harmonic overtone series; poppy seed demonstration visualizes nodal lines
- Wonderpipe 4000: vibrating tube demonstrates same additive overtone structure

**Logical Method:** Physical observation → mathematical model (partial differential equation) → derived solution (Fourier series) → empirical confirmation via spectrum.

**Logical Gaps:**

- The formula f = (1/2L)√(T/ρ) is stated as a result “from differential equations” but the derivation is deferred. The audience must accept the formula on authority before the logical chain is closed.
- Kung claims the jump rope “exactly” models a violin string. This is stated with more confidence than warranted; real strings have finite stiffness that causes inharmonicity at higher overtones, which Kung briefly acknowledges in Lecture 6 but does not flag here.
- The 7th harmonic is noted as “not on our scale” without explanation—this is an unresolved loose end that Lecture 4 will partially address.

**Methodological Soundness:** The physical-to-mathematical pipeline is pedagogically sound. Kung is transparent that solving the PDE is beyond lecture scope. The model makes falsifiable predictions (frequency ratios) that are confirmed with demonstration instruments.

---

### LECTURE 2: Timbre — Why Each Instrument Sounds Different

**Core Claim:** Timbre is determined by the spectrum—the relative amplitudes of overtones—which the Fourier transform extracts from a waveform; the human ear performs this transform physically via cochlear resonance.

**Supporting Evidence:**

- Spectrum comparisons: violin, trumpet, clarinet show distinct overtone height patterns
- Clarinet produces predominantly odd harmonics (due to closed-end boundary condition)—confirmed by spectrum
- Banjo experiment: removing the attack makes a banjo sound like a piano, confirming that the attack portion of the spectrum is critical to perceived timbre
- Violin harmonics experiment: stopping string at midpoint eliminates odd overtones (confirmed by spectrum showing only even peaks)
- Stopping at 1/3 and 2/3 up the string produces identical spectra—confirmed by measurement
- Piano hammer placement at 1/7 of string length to suppress the 7th harmonic: stated as established piano construction practice

**Logical Method:** Fourier analysis as diagnostic tool → spectrum comparison across instruments → physical mechanism (cochlear resonance as mechanical Fourier analyzer) → compositional implications (Air on the G string).

**Logical Gaps:**

- The claim that cochlea “does a Fourier transform” is a useful analogy but not a precise description. The cochlea performs a kind of frequency decomposition via place theory, but with significant nonlinearities, compression, and bandwidth-limited resolution that diverge from mathematical Fourier analysis. Kung acknowledges “it’s a little bit more complicated” but does not quantify the divergence.
- The piano hammer placement claim (1/7th) is presented as established fact without citing measurement data confirming that production pianos actually follow this. Kung notes tuners are “a little bit surprised” and some hammers are at 2/7ths—this hedge undermines the confident framing.
- The Banjo attack experiment is a compelling demonstration but relies on a single prepared example. Whether this generalizes across instruments is asserted, not tested.

**Methodological Soundness:** The Fourier framework is rigorously introduced. The cochlea-as-Fourier-analyzer analogy is appropriately labeled as analogy. Demonstrations are well-chosen but anecdotal.

---

### LECTURE 3: Pitch and Auditory Illusions

**Core Claim:** Pitch is a perceptual attribute distinct from frequency; the missing fundamental illusion, the scale illusion, Shepard tones, and the tritone paradox demonstrate that the brain constructs pitch via pattern-matching overtone series rather than reading off fundamental frequency.

**Supporting Evidence:**

- Cell phone demonstration: speaker cutoff at ~350 Hz means male voice fundamentals (~100 Hz) are not transmitted; listeners still perceive male pitch because the overtone pattern matches a 100 Hz template
- Missing fundamental explained neurologically: firing pattern of neurons encodes the overtone series, and removing lower harmonics still activates a near-complete pattern
- Scale illusion (Diana Deutsch, 1973): left and right channels play disjoint half-scales; brain recombines them into ascending/descending lines—used compositionally by Tchaikovsky in 6th Symphony
- Organ builders’ 10⅔-foot pipe trick: two pipes at 2X and 3X harmonics generate virtual 32-foot pipe fundamental—mathematically verified (3X comes from fundamental of 10⅔-foot pipe)
- Shepard tones: tones composed of multiple octaves with amplitude envelope; circular structure in 12-note space makes “endlessly rising” perception formally consistent
- Tritone paradox: tritone = 6 half-steps = across the circle from any starting note; neither direction is definitively “up” or “down”

**Logical Method:** Perceptual phenomena → acoustic analysis → neural mechanism → compositional application.

**Logical Gaps:**

- The missing fundamental explanation via neuron firing rates is presented as established fact, but the claim that “there’s a neuron that’s firing 100 times per second” for a 100 Hz tone is a simplification of a complex pitch-coding debate (rate coding vs. place coding). Kung is teaching to the correct intuition but overstates the certainty of mechanism.
- The organ pipe calculation is correct but Kung uses approximate numbers throughout (”roughly 16.4 Hz”). A precise derivation would be: fundamental of 32-foot pipe ≈ 340/(2 × 9.75m) ≈ 17.4 Hz. The rounding affects the demonstration without being flagged.
- Shepard tones are explained correctly but the “amplitude envelope” mechanism—which is essential to why they don’t sound discontinuous—is described only vaguely.

**Methodological Soundness:** This lecture has the highest evidence density in the course. Deutsch’s work is real and replicable. The organ pipe mathematics is verifiable. The neurological claims are plausible but stated with more precision than current neuroscience warrants.

---

### LECTURE 4: How Scales Are Constructed

**Core Claim:** Scale construction is fundamentally constrained by two incompatible mathematical structures: overtones are additive (arithmetic sequences) while intervals are multiplicative (geometric sequences). Two strategies—just tuning (overtones of the fundamental) and Pythagorean bootstrapping (fifths from one note to the next)—each solve part of the problem while creating different contradictions.

**Supporting Evidence:**

- Equally-spaced (additive) scales demonstrated to be unworkable: bass, tenor, soprano octaves would contain 5, 10, 20 notes respectively—no transposability
- Multiplicative structure: putting a 3/2 note in bass at 150 Hz requires 300 Hz for tenor, 600 Hz for soprano—preserves octave relationships
- Just pentatonic scale: derived from harmonics 1, 3, 5, 9 of A (with octave reduction); B-F# problem: B’s overtones include F# at 1485 Hz, but just F# is at 1540 Hz—27/16 vs. 5/3
- Pythagorean scale: generated by 12 stacked fifths; demonstrates that (3/2)^12 ≠ 2^7 (129.74 ≠ 128)—the Pythagorean comma
- Gamelan: bars (2D vibrators) produce non-harmonic overtones → Indonesian music contains no perfect fifth → cultural scale choice reflects physical instrument’s overtone structure

**Logical Method:** The additive/multiplicative incompatibility is the load-bearing logical structure. Both just and Pythagorean tuning are shown as principled responses to this incompatibility, each with demonstrated failure modes.

**Logical Gaps:**

- The B-F# problem in just tuning is stated cleanly: B’s third harmonic produces F# at 27/8, divide by 4 octaves gives 27/16 ≈ 1.688, while just F# = 5/3 ≈ 1.667. These differ by ~22 cents. This is proven. However, Kung then states that “no instrument can make it work”—this is correct as a mathematical theorem but is presented as a simple consequence of the demonstration rather than a proven impossibility result. The argument would be stronger with an explicit proof by contradiction.
- The gamelan claim—that Indonesian music has no perfect fifth because gamelon bars have non-harmonic overtones—is presented as direct causation. This is plausible but is a musicological hypothesis, not a proven causal chain. Cultural and historical factors also influence scale choice.
- Just tuning for bagpipes and Indian music is described as “perfect.” In practice, bagpipe intonation is notoriously imprecise due to temperature, reed variation, and player technique.

**Methodological Soundness:** The mathematical argument (additive/multiplicative incompatibility) is rigorous and the central insight of the course. The cultural application claims require more hedging.

---

### LECTURE 5: How Scale Tunings and Composition Co-Evolved

**Core Claim:** The Pythagorean comma cannot be eliminated—it can only be distributed across fifths in different ways; equal temperament (each half-step = 2^(1/12)) is the unique solution that enables full transposability but requires irrational frequency ratios; this mathematical change in tuning systems co-evolved with the progressive abandonment of tonality in Western music from Baroque to 20th century.

**Supporting Evidence:**

- Pythagorean comma = 23 cents; demonstrated aurally (440 Hz vs. 446.39 Hz simultaneously producing audible beats)
- Equal temperament solution: R^12 = 2^7 → R = 2^(7/12) ≈ 1.4983, irrational
- Why 12 notes: trial-and-error comparison shows that 12 equally-spaced notes approximate major third (1.25), fourth (1.333), and fifth (1.5) more closely than 2, 3, 5, 7, 8, 10, 11 notes; 12 is the smallest n achieving acceptable approximation of all three
- Continued fraction derivation: log₂(3) ≈ 1.58496; continued fraction [1; 1, 1, 2, 2, 3, 1, ...] truncated at [1; 1, 1, 2] gives 19/12 → confirms 12-note system; next truncation gives 65/41 → 41-note system
- Co-evolution narrative: tunings from Pythagorean (comma in one fifth) → meantone variants → Werckmeister III → equal tempered; compositions from single-key Baroque → chromatic Romantic → atonal 20th century
- Guitar forced equal temperament since ~1500 (frets across all strings); piano joined only ~1900; explains absence of guitar-piano repertoire 1500-1900

**Logical Method:** Mathematical necessity (irrational R) → historical consequence (tuning evolution) → compositional implication (style change). The continued fraction argument is the most rigorous piece of mathematics in the course.

**Logical Gaps:**

- The co-evolution claim is presented as causal (”tunings changed → composition changed”) but Kung explicitly acknowledges the chicken-and-egg problem. The claim remains correlation supported by timeline. No mechanism is specified by which a composer in 1750 would consciously adapt their style to tuning changes rather than responding to aesthetic and cultural pressures independently.
- The 12-note “why 12” argument via trial-and-error is correct but incomplete. Kung shows that 12 approximates major third, fourth, and fifth well. He does not address why those three intervals are the target, which depends on their prominence in the overtone series—a circular argument that is not flagged.
- The guitar-piano repertoire absence is an interesting empirical claim. Whether it is entirely attributable to tuning incompatibility versus stylistic, economic, or instrumental factors is not examined.

**Methodological Soundness:** The continued fraction argument is the mathematical high point of the course—rigorous, elegant, and surprising. The historical co-evolution narrative is plausible but speculative as a causal claim.

---

### LECTURE 6: Dissonance and Piano Tuning

**Core Claim:** Dissonance arises from beats—amplitude modulation produced when two close frequencies are played simultaneously—which the beat equation (sin A + sin B = 2·sin((A+B)/2)·cos((A-B)/2)) predicts with precision; piano tuning uses controlled beat rates to achieve equal temperament.

**Supporting Evidence:**

- Beat demonstration on violin: two D strings tuned slightly apart; beats slow as pitches converge, disappear when matched
- Beat equation derivation given in full: uses sum-of-angles formula for sine, confirms graphically that left and right sides are equal
- Beat frequency = |A - B| derived (not A-B/2, because each cosine cycle produces two beats)
- Octave tuning example: 220 Hz + 442 Hz produces beats at 2/second (from 880 Hz first overtone of 220 vs. 882 Hz fundamental of 442)
- Fifth tuning: D should be at 293.33 Hz (just) but equal tempered D is 293.66 Hz; beats between D’s third harmonic (880.99) and A’s first overtone (880) = ~1 beat/second
- Live piano tuning demonstration confirms beat rate targeting
- Copland Fanfare for the Common Man: open intervals (fourths, fifths, octaves) require precise tuning; dissonance audible if out of tune

**Logical Method:** Physical phenomenon (beats) → trigonometric derivation (beat equation) → practical application (piano tuning by ear) → compositional implication (open vs. close intervals).

**Logical Gaps:**

- The beat equation proof is complete and rigorous—this is the most mathematically airtight section of the course.
- The piano tuning demonstration involves tightening/loosening strings by ear; Kung acknowledges that real piano tuners don’t calculate beat rates analytically for each fifth. The “1 beat per second” rule is a teaching simplification. Actual piano tuning involves stretch tuning, different beat rates for different intervals at different registers, and cross-checking—all briefly acknowledged but not integrated into the mathematical framework.
- The claim that octaves must be tuned perfectly while other intervals can be approximate is stated categorically. In practice, piano tuners deliberately stretch octaves (tune them slightly wide) to compensate for inharmonicity. This is mentioned but not reconciled with the “tune octaves perfectly” claim.

**Methodological Soundness:** The beat equation derivation is exemplary. The practical applications are honest about their simplifications. This is the course’s most rigorous single lecture.

---

### LECTURE 7: Rhythm — From Numbers to Patterns

**Core Claim:** Rhythm is structured by number theory—Fibonacci numbers arise from Sanskrit poetry, hemiolas exploit the prime factorization of 6, polyrhythms require least common multiples, and competing melodic/rhythmic cycles produce tension that resolves at their LCM.

**Supporting Evidence:**

- Pingala’s Sanskrit poetry problem: ways to arrange short (1) and long (2) syllables in n-beat line = Fibonacci(n+1); first 6 values (1, 2, 3, 5, 8, 13) confirmed
- Geometric series proof: replacing last note with two half-length notes, iterated to infinity, proves 1/2 + 1/4 + 1/8 + ... = 1 via musical notation
- Hemiola in Handel Water Music: 6-beat phrase switches from 2×3 to 3×2 grouping; counted and demonstrated
- Polyrhythm 3 vs. 2 demonstrated physically; requires 6 = LCM(2,3) subdivisions
- Tchaikovsky Piano Concerto: 3-against-2 between piano and strings demonstrated and counted
- Chopin Fantasy Impromptu: 3-against-4 polyrhythm; right hand 16th notes (4/beat), left hand triplets (3/beat); LCM = 12, demonstrated on computer playback
- Gershwin Rhapsody in Blue: 5-note rhythm in 4-beat bars repeats every LCM(5,4)=20 notes; 8-note scale in 6-beat bars repeats every LCM(8,6)=24 notes

**Logical Method:** Mathematical property (prime factorization, LCM) → musical technique → perceptual consequence (tension, instability).

**Logical Gaps:**

- The Fibonacci-poetry connection is proven for short/long syllable combinations with n up to 6, then generalized by induction (each n-beat phrase = (n-1)-beat phrase plus one short + (n-2)-beat phrase plus one long). The proof is sound but Kung states it as a puzzle rather than completing the argument.
- The geometric series proof (1/2 + 1/4 + ... = 1) is correct and elegant but proves convergence for this specific ratio. Kung does not clarify that this is a special case of geometric series ∑r^n = 1/(1-r) for |r| < 1. The proof is valid; its generality is understated.
- “This is how composers create tension” is a repeated claim connecting mathematical structure to perceptual/emotional effect. The mechanism—why LCM misalignment produces the perception of tension and resolution—is asserted, not derived.

**Methodological Soundness:** The combinatorics (Fibonacci) and the geometric series proof are rigorous. The connection between rhythmic complexity and emotional perception is plausible but not proven.

---

### LECTURE 8: Transformations and Symmetry

**Core Claim:** Musical transformations (identity, inversion, retrograde, retrograde inversion, transposition, augmentation/diminution) form mathematical groups; Bach’s use of these transformations in the 14 Canons on the Goldberg Ground is structurally identical to group theory, which would not be formalized for another century.

**Supporting Evidence:**

- Geometric transformations (reflections over x- and y-axes, 180° rotation) form Klein-4 group Z₂×Z₂—table shown
- Musical transformations (I, inversion, retrograde, retrograde inversion) satisfy same group table as Klein-4
- Z₄ is distinct from Klein-4: in Z₄, not every element is its own inverse (1+1≠0, 3+3≠0 mod 4)
- Transposition by major third (4 half-steps) generates Z₃ (three applications return to origin)
- Combining inversion + M4 transposition generates dihedral group D₃ (order 6, smallest non-commutative group); isomorphic to symmetries of equilateral triangle
- Bach Canon 3: inversion demonstrated (upside-down clef notation)
- Bach Canon 1: retrograde demonstrated (backward clef at end)
- Bach Canon 14: four-voice augmentation/diminution canon decoded; bottom voice = Goldberg theme × 8 (8× augmented, inverted, transposed)
- Table canon: retrograde inversion realized on Möbius strip of paper

**Logical Method:** Establish group axioms → demonstrate multiple representations (geometric, functional, numerical, musical) → show isomorphism → demonstrate in Bach.

**Logical Gaps:**

- The claim that Bach’s canons are “structurally identical to group theory” is an analogy, not identity. Bach was constructing musical puzzles without a formal algebraic framework. Kung acknowledges this (”group theory hadn’t been discovered”), but the repeated use of group-theoretic language risks implying that Bach was doing mathematics he wasn’t explicitly doing.
- The Möbius strip paper demonstration for the table canon is elegant but conflates the geometric object (Möbius strip) with the musical structure (retrograde inversion). The isomorphism is suggestive rather than exact: a Möbius strip has a continuous surface; the canon is discrete. The demonstration works pedagogically but is metaphorical.
- The dihedral group D₃ isomorphism is stated but not fully derived. Kung claims M4 (transposition by 4 half-steps) plays the same role as 120° rotation because “both cube to identity.” This is correct but the full group table comparison is not shown, requiring the audience to accept the isomorphism on faith.

**Methodological Soundness:** The group theory presentation is accurate and the examples well-chosen. The Bach analysis is illuminating but is analysis-by-analogy, not proof.

---

### LECTURE 9: Self-Reference from Bach to Gödel

**Core Claim:** Self-reference creates beauty and paradox in both mathematics and music, at three levels of complexity: basic (Beethoven’s quotation), intermediate (Bach’s BACH motif; recursive sequences), and advanced (crab canons; Gödel’s incompleteness theorem).

**Supporting Evidence:**

- Beethoven’s 9th last movement: quotes first, second, third movements before Ode to Joy—transcripts shown
- Bach’s BACH motif (B♭-A-C-B in German notation): appears in Art of Fugue Contrapunctus 14 (C.P.E. Bach inscription: “author died here”) and Brandenburg Concerto No. 2 bass line
- Differential equations as self-reference: y’ = ½y means the function appears on both sides
- Golden ratio as continued fraction of all 1s; proven equal to (1+√5)/2 via quadratic x = 1 + 1/x → x² - x - 1 = 0
- Liar’s paradox (”this sentence is false”) → Gödel statement G (”this statement is not provable”) → First Incompleteness Theorem: any consistent system strong enough for arithmetic contains true but unprovable statements
- Crab canon (Musical Offering): second voice = retrograde of first; demonstrated as Möbius strip

**Logical Method:** Conceptual hierarchy (basic → intermediate → advanced) → parallel musical and mathematical examples at each level.

**Logical Gaps:**

- The Gödel section is necessarily compressed. Kung correctly states the theorem but the proof sketch—”coding statements about mathematics with numbers, key is unique prime factorization”—is too brief to constitute understanding. The audience is told that this is the mathematical pinnacle of self-reference without being given enough to evaluate the claim.
- C.P.E. Bach’s inscription (”author died here”) is flagged as possibly fabricated by C.P.E. later—a significant admission that undermines the narrative weight assigned to it.
- The “three levels of self-reference” taxonomy is Kung’s own organization, not a standard mathematical or musicological classification. It is a useful pedagogical scaffold but presented as if it has objective status.

**Methodological Soundness:** The golden ratio continued-fraction proof is complete and rigorous. The Gödel treatment is accurate in what it claims but limited in depth. Musical examples are well-selected.

---

### LECTURE 10: Composing with Math — Classical to Avant-Garde

**Core Claim:** Composers have explicitly used mathematics in composition from Mozart’s algorithmic dice waltz (1787) through Schoenberg’s 12-tone serialism (1920s) to John Cage’s chance music (1950s) and Dmitri Tymoczko’s geometric analysis (2000s).

**Supporting Evidence:**

- Mozart Musikalisches Würfelspiel: 759 trillion possible waltzes calculated as 2 × 11^14 (correcting for two fixed measures); multiplication principle demonstrated; not all equally likely (seven is most probable dice roll)
- Schoenberg 12-tone: tone row of 12 pitch classes → 48 derived rows (original, inversion, retrograde, retrograde inversion, × 12 transpositions); each ensures all 12 notes used once—atonality by construction
- Melody search (Peachnote.com, Vladimir Viro): encodes melody as sequence of half-step intervals (same system as Schoenberg); finds melody by interval sequence regardless of key; demonstrated on Tchaikovsky 5th Symphony
- Cage’s 4’33”: analogy to zero as mathematical concept; first to recognize absence as music
- Ligeti/Messiaen competing patterns: Messiaen uses 17-beat and 29-beat competing cycles; LCM(17,29) = 493 notes before repetition—”until end of time”
- Tymoczko’s 2-note chord geometry: 12×12 grid → torus (by wrapping both axes) → Möbius strip (after halving the space to eliminate double-counting, followed by topological surgery)

**Logical Method:** Historical chronology → increasing mathematical sophistication of compositional methods → geometric analysis as synthesis.

**Logical Gaps:**

- The 759 trillion calculation is correct: 2 × 11^14 ≈ 4.5 × 10^14. However, Kung’s explanation of why two measures are fixed (every roll gives the same measure for bar 8, only two options for bar 16) is stated without showing the table. The audience cannot verify this.
- Schoenberg’s tone row system is described accurately, but the claim that “atonality is achieved by construction” requires a stronger argument. Using all 12 notes once in each row guarantees equal distribution across rows but not equal salience in the listener’s perception—harmonic patterns can still emerge. This is a known criticism of 12-tone theory.
- Cage’s 4’33” is framed as analogous to zero. This is a resonant analogy but Kung does not defend why the absence of composed notes (rather than silence in performance) is the relevant parallel to zero. Silence ≠ absence of number.
- The Möbius strip derivation for 2-note chords is the most sophisticated mathematics in the course, but the “topological surgery” (cutting along the diagonal, flipping triangle, reassembling) is described verbally without showing the result rigorously. Whether this constitutes a proof that the space is a Möbius strip is left implicit.

**Methodological Soundness:** The Mozart calculation is solid. The geometric music theory section is the most original content in the course but is too compressed for verification. The historical narrative is well-supported.

---

### LECTURE 11: The Digital Delivery of Music

**Core Claim:** Digital music delivery requires three layers of mathematics: auto-tune (pitch detection via Fourier analysis, pitch correction via multiplicative frequency scaling), audio compression (Nyquist theorem at 44,100 Hz sampling, perceptual masking via psychoacoustics), and error correction (Hamming codes, Reed-Solomon, cross-interleaving).

**Supporting Evidence:**

- Auto-tune pitch correction: correcting from 430 Hz to 440 Hz requires multiplying spectrum by 44/43, not adding 10 Hz—because overtone series is multiplicative
- Nyquist theorem (1928): sampling at frequency f preserves all information below f/2; hearing limit ~20 kHz → sample at ≥40 kHz; CD uses 44,100 Hz (with margin)
- Perceptual masking: loud sound at 300 Hz masks nearby soft sounds at 320 Hz—demonstrated aurally; far-apart frequencies do not mask—also demonstrated
- CD check digits: Luhn algorithm (double alternating digits, sum, check mod 10) catches all single-digit errors and ~80% of transpositions
- Hamming (7,4) code: 4 data bits + 3 check bits in three overlapping circles; can detect and correct any single-bit error; distance between valid codewords ≥ 3
- Cross-interleaved Reed-Solomon: 16-digit example with ~20% error rate (including burst errors) decoded perfectly; interleaving spreads burst errors so each row/column has at most one error
- CD performance: 50,000 manufacturing errors correctable; burst errors up to 2.4 mm (3,500 bits) correctable

**Logical Method:** Each section follows the pattern: problem (pitch errors, file size, disk errors) → mathematical tool → quantitative result → empirical demonstration.

**Logical Gaps:**

- The auto-tune description is pedagogically clear but technically simplified. The claim that you can correct pitch by “stretching the spectrum by 44/43” assumes the voice is a single sustained tone with stable overtones. Real vocal performance has continuous pitch variation, vibrato, formant transitions, and consonants—none of which are addressed. The actual Time-Domain Pitch Correction (TDPSOLA) algorithm Kung mentions in passing is fundamentally different from frequency-domain stretching.
- Nyquist theorem is stated as “sampling at f preserves all frequencies below f/2” without stating the critical assumption: the signal must be bandlimited. A signal with energy above f/2 will alias. This condition is satisfied by lowpass filtering before sampling (anti-aliasing filter), which is not mentioned.
- The Hamming code demonstration with the circular Venn diagram is pedagogically excellent and mathematically correct. However, the claim that “you now know everything you need to know to tune a piano” at the end of Lecture 6 has an analogue here: “you know everything to understand CD encoding.” Both overclaim; the Reed-Solomon code operates over GF(256) (Galois field), which requires abstract algebra not introduced in the course.

**Methodological Soundness:** The Hamming code proof-of-concept is the clearest worked example in the course. The perceptual masking demonstrations are empirically sound. The auto-tune and Nyquist sections are simplified without being wrong.

---

### LECTURE 12: Math, Music, and the Mind

**Core Claim:** The connections between mathematics and music are not merely structural but neurological—infant brains come pre-wired for both; prodigies cluster in math, music, and chess (all pattern-dominated); creativity, practice, and abstractness are shared traits; music and math are both accessible to the mind independent of physical reference.

**Supporting Evidence:**

- Infant subitizing at 3-4 days (2 vs. 3 dots via habituation/fixation paradigm)
- Karen Wynn (Yale): 5-month-olds distinguish 1+1=2 from 1+1=1 by gaze duration; generalized across object types
- Lamont (UK): conditioned head-turning experiment; 1-year-olds prefer upbeat/familiar music; prenatal music memory persists 1 year
- Prodigies appear in math, music, chess—not biochemistry, psychology, engineering; proposed common trait: pattern recognition
- David Cope melody predictor: fed 5 notes + rhythm, achieves 64-71% accuracy predicting Mozart’s subsequent notes
- Deliberate practice (Ericsson): 10,000 hours in any field; applies equally to musicians (scales, etudes) and mathematicians (problem pondering)
- Mozart at age 5 composed complete stylistically coherent minuet
- Abstractness: mathematics and music are the most abstract of sciences and arts respectively; both can be expressed without reference to physical world

**Logical Method:** Empirical developmental psychology → pattern recognition as common cognitive substrate → creativity and practice as parallel structures → abstractness as philosophical commonality.

**Logical Gaps:**

- The infant subitizing and arithmetic research (Wynn) is legitimate developmental psychology. However, the claim that infants “doing” arithmetic implies a neurological connection between mathematical cognition and musical cognition is not demonstrated—it shows mathematical competence, not a shared substrate with music.
- The prodigy argument (”prodigies appear in math, music, chess—not biochemistry”) is empirically plausible but not tested. Prodigies in art (e.g., painting) exist but are not mentioned. The claim that the common denominator is “patterns” is a post-hoc label that could be applied to many cognitive domains.
- Cope’s 64-71% melody prediction rate is presented as evidence that music is mathematical. But a random model for melody within a diatonic key would achieve above-chance performance simply by staying on scale tones. The relevant baseline is not provided.
- The closing philosophical claim—that mathematics and music are both “abstract” in a Platonic sense—is presented as a finding when it is actually a philosophical position (Platonism about mathematical objects). Kung does not note that mathematical nominalists would dispute this.
- The Brahms quote about the Chaconne is used as an emotional capstone. Inspiring; not evidence.

**Methodological Soundness:** The developmental psychology citations are real. The prodigy clustering claim is empirically defensible but not rigorously tested here. The philosophical claims about abstractness are interesting but unproven.

---

## BRIDGE: Synthesizing the Logical Architecture

**The course’s central claim** is stated in Lecture 1: “How can mathematics help us understand the musical experience?” Kung constructs his answer in three layers:

**Layer 1 (Lectures 1-3): The physics of sound.** The overtone series is derived mathematically and confirmed empirically. This layer is most rigorous; the differential equation framework makes falsifiable predictions that are tested against observation.

**Layer 2 (Lectures 4-6): The mathematics of pitch organization.** The additive/multiplicative incompatibility is the intellectual core of the course. It explains why perfect tuning is impossible, why 12 is the right number of notes, and why Western music evolved toward equal temperament. This argument is tight, original-feeling, and the most transferable mathematical insight in the course.

**Layer 3 (Lectures 7-12): Patterns, structure, and mind.** The mathematical richness decreases and the claims become progressively broader and less provable. Rhythm and LCMs are solid. Group theory analogies are illuminating but explicitly analogical. Self-reference is evocative. The closing claims about mind and cognition are speculative.

**Three recurring tensions:**

*Tension 1: Proof vs. demonstration.* Kung is excellent at demonstrating mathematical structures in music but frequently stops short of proving them. The Möbius strip topology of 2-note chords, the Gödel section, and the infant cognition claims all benefit from the demonstration but would require substantially more work to qualify as proofs.

*Tension 2: The causation problem.* Throughout, Kung implies causal connections where only correlation is shown. Tunings “caused” compositional changes; mathematical structure “causes” perceptual beauty; pattern-matching ability “explains” why prodigies cluster in math and music. Each of these is plausible; none is proven.

*Tension 3: The universality claim.* Kung repeatedly implies that the mathematical principles discussed are universal (e.g., “nearly every musical tradition contains the fifth and octave”). The gamelan example is introduced precisely to complicate this, but the exception is quickly contained rather than used to test the universality claim rigorously.

**Most proven claims:**

- Overtone series is arithmetic; predicted by PDE solution; empirically confirmed
- Additive/multiplicative incompatibility makes perfect tuning impossible (proven mathematically)
- 12 is the smallest n for which equal-spaced notes approximate major third, fourth, and fifth simultaneously (demonstrated by enumeration)
- Beat frequency = |f₁ - f₂| (proven from beat equation via trigonometric identity)
- Hamming (7,4) code corrects all single-bit errors (proven by construction)
- Fibonacci numbers count short/long syllable arrangements (provable by induction)

**Most significant unproven claims:**

- Tuning systems co-evolved causally with compositional styles
- Musical beauty and mathematical beauty share a common cognitive substrate
- Prodigy clustering in math/music/chess demonstrates a shared neural pattern-recognition mechanism
- The human cochlea performs a “Fourier transform” in any mathematically precise sense

**Most honest acknowledgments of limits:**

- Kung repeatedly notes when he is simplifying or when the full mathematics is beyond scope
- The piano tuning lecture explicitly acknowledges that piano tuners don’t compute beat rates analytically
- The auto-tune section correctly identifies the real algorithm (TDPSOLA) differs from the simplified version presented

---

## PART 2: LITERARY REVIEW ESSAY

---

# The Comma No One Can Close

Mathematics and music have been declared siblings so many times that the comparison has acquired the status of received wisdom—invoked at faculty cocktail parties, cited in grant applications, used to justify music programs to school boards that care about STEM. David Kung’s 12-lecture course, *How Music and Mathematics Relate*, takes this relationship seriously enough to build it from axioms. The result is something rarer than a celebration: a rigorous account of exactly where the connection holds, how far it extends, and where it quietly dissolves into analogy.

The course’s intellectual core arrives early, in Lectures 4 and 5, and it is genuinely surprising. The argument begins with a simple observation: the overtone series produced by a vibrating string is an arithmetic sequence—100, 200, 300, 400, 500 Hz, each term formed by adding the fundamental frequency. But musical intervals—octaves, fifths, the distances between notes that define scales—are multiplicative. An octave means doubling frequency. A fifth means multiplying by 3/2. To go up a fifth twice is not to add 3/2 twice but to multiply by (3/2)². These two structures—additive overtones and multiplicative intervals—are mathematically incompatible. They cannot be reconciled. And from this single observation, Kung derives an astonishing consequence: no instrument can ever be perfectly in tune.

The proof is elegant in its inevitability. Stack 12 perfect fifths—each multiplying by 3/2—and you should, after traveling through all 12 pitch classes, arrive exactly seven octaves higher. But (3/2)^12 = 129.74, and 2^7 = 128. These are not the same number. They cannot be made the same number. The discrepancy—23 cents, roughly a quarter of a half-step—is called the Pythagorean comma, and its existence is not a failure of instrument makers or tuners. It is a mathematical theorem. The incompatibility is built into the relationship between arithmetic and geometric sequences.

This is Kung at his best: precise, surprising, and following the logic where it leads. The derivation of equal temperament as the unique solution that distributes the comma evenly across all 12 fifths—with each half-step therefore tuned to the irrational number 2^(1/12)—is clean and complete. The continued-fraction argument explaining why 12 is the right number of notes for a Western scale has the quality of a good proof: it makes the result feel inevitable in retrospect while remaining genuinely unexpected in advance.

---

The course’s most significant single demonstration comes in Lecture 6: the beat equation. When two frequencies close to each other are played simultaneously, the result is not two tones but a single tone that throbs—whose amplitude waxes and wanes at a rate equal to the difference of the two frequencies. This follows directly from the trigonometric identity sin A + sin B = 2·sin((A+B)/2)·cos((A-B)/2). Kung proves this identity in full using elementary geometry—a Euclidean construction involving a right triangle and three angles at a point—and the proof is the most rigorous piece of mathematical work in the course. It is not a metaphor. It is not an analogy. The mathematics directly predicts the physical phenomenon, which is then demonstrated in real time on a piano being tuned.

This demonstration is where the course achieves its clearest statement of what it means for mathematics to “explain” a musical phenomenon. The beat equation does not merely describe the phenomenon; it predicts it quantitatively before the demonstration occurs. The equal-tempered D should beat against the A at approximately 1 cycle per second. Kung tunes the piano. The beats are heard. That is explanation in the strict scientific sense.

I want to use this lecture as a benchmark, because the rest of the course is measurably less rigorous—not wrong, but operating in a different register. When Kung argues in Lectures 7 and 8 that rhythmic polyrhythms create “tension” resolved at their LCM, or that Bach’s canons exhibit “group-theoretic structure,” he is making claims of a different logical type. The LCM calculation is correct. The group table for the Klein-4 group is correct. What is not proven—what may not be provable—is that listeners perceive Chopins’s 3-against-4 polyrhythm as tense because of the LCM, or that Bach composed his retrograde inversions because he was implicitly reasoning about group theory. Kung is careful to note that Bach predated formal group theory by a century. But the word “implicit” is doing considerable work, and a skeptical listener might note that one can find group structure in almost anything once one knows what to look for.

---

The course’s most consequential unproven claim is also its most resonant one. In the final lecture, Kung proposes that mathematics and music share cognitive roots—that infant brains come pre-wired for both, that prodigies cluster in math, music, and chess because all three are pattern-dominated, and that the shared property of abstractness links the two subjects at a philosophical level. The developmental psychology evidence (Karen Wynn’s 1992 experiments showing 5-month-olds’ arithmetic expectations; Lamont’s conditioned head-turning experiments) is real and replicable. What it does not prove is the cognitive connection. Demonstrating that infants perform rudimentary arithmetic before language does not establish that this capacity shares neural infrastructure with musical processing. The claim requires a neuroscience argument that the lecture does not provide.

The prodigy argument is similarly intriguing but underspecified. Prodigies appear in music, mathematics, and chess—and also in art, athletics, and language acquisition. If the common factor is “pattern recognition,” that label applies broadly enough to cover most of human cognition. The more precise claim—that the specific kind of pattern recognition involved in mathematics is the same kind involved in musical listening—would require experimental dissociation studies showing that these capacities co-vary, or lesion studies showing they share neural substrates. Neither is cited.

I do not raise these objections to dismiss the claim. The connection between musical and mathematical thinking may be real and deep. The infant subitizing research, the prodigy clustering, David Cope’s melody prediction accuracy—these form a suggestive constellation. But there is a difference between a suggestive constellation and a proof, and a course that opens with the rigor of differential equations and closes with cognitive speculation should flag that transition more clearly than it does.

---

What the course demonstrates—and this is no small achievement—is that specific, verifiable mathematical structures underlie specific, verifiable musical phenomena. Overtone series: proven. Beat frequencies: proven. The impossibility of perfect tuning: proven. The approximation of just intervals by 12-tone equal temperament: proven. Fibonacci numbers in Sanskrit poetry: provable. The Hamming code on a CD: demonstrated and correct.

What it proposes, but does not prove, is that the *experience* of music—beauty, tension, resolution, the sense that a melody “wants” to go somewhere—is mathematical in the same sense. This is the most interesting question the course raises and the one it is least equipped to answer. Kung ends with the Bach Chaconne, quoting Brahms: “the excess of excitement and earth-shattering experience would have driven me out of my mind.” Brahms, presumably, was not driven out of his mind by the partial differential equation governing the vibrating strings that produced the sound.

There is a comma between the physics and the phenomenology that no tuning system can close. Kung’s course, at its best, makes the measurement of that comma precise. That is enough. The comma is real and irreducible. Mathematics can tell you exactly how large it is—23 cents, give or take—but it cannot play the Chaconne.

---

**Tags:** music mathematics pedagogy, overtone series physics, equal temperament Pythagorean comma, Fourier analysis timbre, group theory Bach canons
