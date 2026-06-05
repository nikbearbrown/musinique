### LECTURE 6: Dissonance and Piano Tuning

**Core Claim:** Dissonance arises from beats—rapid amplitude oscillations produced when two frequencies are close but not equal. The beat equation (sin A + sin B = 2 sin((A+B)/2) cos((A-B)/2)) predicts beat frequency as |A - B| Hz. This phenomenon is exploited for piano tuning: equal-tempered intervals produce predictable beat rates that tuners use as calibration targets.

**Supporting Evidence:**
- Beat equation derived from trigonometric identity: sin(5t) + sin(3t) = 2sin(4t)cos(t)—the cosine envelope term produces the beating
- Graphical and aural demonstration: 440 Hz + 450 Hz produces 10 beats/second; 440 Hz + 444 Hz produces 4 beats/second—confirming beat frequency = |f₁ - f₂|
- The factor-of-2 reconciliation: cosine of frequency (A-B)/2 produces 2 beats per cycle (one when cosine is positive, one when negative), so beats/second = 2 × (A-B)/2 = A-B
- When A = B: cos(0) = 1, so the formula yields 2sin(ft)—simply double amplitude, no beating. Verified.
- Octave beating: playing A4 (440 Hz) and A3 (220 Hz); overtone at 880 Hz (2nd harmonic of A3 if A3 were perfectly at 220) interacts with 440 Hz; if A3 is at 222 Hz, its 2nd harmonic is 444 Hz, producing 4 beats/second with the 440 Hz fundamental—octave tuning uses overtone beating, not fundamental beating
- Equal-tempered D below A440: Z such that Z × 2^(7/12) = 440, giving Z ≈ 293.66 Hz; third harmonic of D = 3 × 293.66 ≈ 880.99 Hz; beats with A's second harmonic at 880 Hz = ~1 beat/second; piano tuners target exactly this
- Piano string inharmonicity: coiled strings produce slightly sharp overtones (not at exact integer multiples), requiring "stretch tuning"—treble strings tuned slightly sharp, bass strings slightly flat relative to theoretical equal temperament
- Aaron Copland's Fanfare for the Common Man (1942): built on "open" perfect intervals (octaves, fifths, fourths) that require precision tuning—dissonance if even slightly off

**Proof of Beat Equation:**
The lecture includes a full geometric proof of sin(u+v) = sin(u)cos(v) + cos(u)sin(v) from first principles using a unit circle and similar triangles, which is then used to prove the beat equation. This is the most rigorous mathematical derivation in the course.

**Logical Gaps:**
- The cultural component of dissonance is acknowledged ("what Bach considered beautiful, medieval composers might have called dissonant") but not integrated into the mathematical framework. The course treats dissonance as a psychophysical phenomenon (beats) but dissonance judgments are also learned, cultural, and context-dependent. The beat theory explains a physical correlate, not the full perceptual experience.
- "Musicians must be more careful with some intervals than others, like octaves, fourths, fifths." This is derived from the observation that these intervals have overtones that coincide and therefore produce audible beats when slightly mistuned. But the claim is presented as if precision matters only for these "perfect" intervals. In practice, major thirds in common-practice harmony also require close attention to tuning, particularly in string quartet playing.
- Piano tuning as presented (calculate target beat rate, tune to that) is acknowledged as a simplified model. The actual complication of inharmonicity (stretch tuning) is noted but not quantified.

**Methodological Soundness:** The mathematical content is the most rigorous in the course—the full proof of the beat equation is given. The piano tuning application is a genuine use of the mathematics, though simplified from professional practice.

---
