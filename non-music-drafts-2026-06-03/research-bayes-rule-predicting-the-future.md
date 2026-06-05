### CHAPTER 6: Bayes' Rule — Predicting the Future

**Core Claim:** Bayes' rule, particularly Laplace's Law and the Copernican Principle, provides a mathematically grounded framework for making predictions from small data. The appropriate prediction rule—multiplicative (power law), average (normal distribution), or additive (Erlang/memoryless)—depends entirely on the prior distribution of the quantity being predicted. Human intuitions about prediction are surprisingly well-calibrated when the prior is absorbed from real experience, but degrade when the prior is unavailable or distorted by media overrepresentation.

**Supporting Evidence:**
- Laplace's Law: after W wins in N attempts, expected probability = (W+1)/(N+2)—derived from calculus integration over all possible hypotheses with uniform prior
- Copernican Principle (Gott 1969): best prediction for total lifespan = 2 × current age; derived from uninformative prior via Bayes
- Allied tank counting in WWII: Bayesian serial number analysis predicted 246/month; aerial reconnaissance predicted 1,400; actual = 245. Bayesian analysis won.
- Normal distribution → average rule; power law → multiplicative rule; Erlang → additive rule
- Tom Griffiths and Josh Tenenbaum experiment: people's predictions for movie grosses, lifespans, political terms closely tracked Bayesian optimal predictions for each domain
- Movie box office: power law → multiplicative rule (1.4x current gross); human life spans: normal → average rule; congressional terms: Erlang → additive rule ("five more minutes")
- Media distortion: murder rate fell 20% in the 1990s; media coverage of gun violence rose 600%—distorts priors
- Marshmallow test reinterpretation: willingness to wait rationally depends on prior about experimenter reliability (power law vs. normal); Rochester experiment confirmed
- Gould (mesothelioma diagnosis): understood the right-skewed distribution, recognized he might be in the long tail, lived 20 more years

**Logical Method:** Mathematical derivation (Laplace) + behavioral experiment (Griffiths/Tenenbaum) + historical cases (WWII tanks, Gott's Berlin Wall prediction).

**Logical Gaps:**
- Laplace's Law assumes a uniform prior (equal probability of any winning rate). This is mathematically clean but epistemically questionable: we almost never know nothing. The authors present it as a general tool when it is specifically a tool for genuine ignorance.
- The Tenenbaum/Griffiths experiment showing humans are well-calibrated Bayesians is a genuine finding, but the domains tested (movie grosses, lifespans) are ones with abundant everyday experience. For novel domains, human calibration degrades—the pharaoh reign example is mentioned briefly but its implication (Bayesian reasoning depends on good priors, which humans often lack) deserves more weight.
- The media distortion point is well-taken but leads to a prescriptive conclusion ("turn off the news") that is not derived from Bayes' rule—it's a practical heuristic. The book does not discuss how to correct for known media biases in one's priors, which is the actual Bayesian solution.
- The Copernican Principle works when we have no information. The authors apply it to phenomena (Google's expected lifespan, US life expectancy as a nation) where we have substantial relevant information. The principle applies to those examples only in the absence of domain knowledge, and domain knowledge matters enormously for well-known entities.

**Methodological Soundness:** The mathematical derivations are correct. The behavioral experiments are genuine. The case applications require that the uninformative prior assumption holds, which is rarely examined.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-bayes-rule-predicting-the-future.md`

Key additions: Bayes' rule updates prior beliefs with evidence; different priors produce different prediction rules. Laplace's rule of succession and Copernican-style prediction are special ignorance cases, not universal forecasting laws. In familiar domains, prior knowledge can make prediction much better; in distorted media environments, priors can be badly miscalibrated.

Settled: Bayesian updating is the normative formal framework for combining prior probability and evidence. Contested: when human cognition is genuinely Bayesian, approximately Bayesian, or better described by simpler heuristics.

Teaching move: solve the same "how long will this last?" problem under three priors so students see that the prior is not decorative; it changes the answer.
