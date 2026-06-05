### CHAPTER 6 (Chapter 7 in audio): On Trustworthy and Ethical AI

**Core Claim:** AI systems are being deployed in consequential real-world applications before their reliability and biases are adequately understood, and before governance structures exist to regulate them. The value alignment problem—ensuring AI systems' values match human values—cannot be solved until we can define human values consistently.

**Supporting Evidence:**
- Self-driving car accidents (Google bus collision, Tesla autopilot failures in snow) as instances of long-tail failures
- Face recognition: ACLU test found Amazon's Rekognition falsely matched 28/535 members of Congress with criminal databases, with African Americans disproportionately misidentified
- CEO of Kairos (face recognition company) publicly opposing law-enforcement use of his own product's technology
- The trolley problem: 76% of survey participants said AVs should sacrifice one passenger to save ten pedestrians, but the overwhelming majority said they would not personally buy an AV programmed that way—direct measurement of inconsistency in stated moral preferences
- Pew Research: 63% of technology experts predicted AI would leave humans better off by 2030; 37% disagreed

**Logical Method:** The chapter proceeds from specific documented harms → governance gap → the deeper philosophical problem (value alignment requires coherent values).

**Logical Gaps:**
- Asimov's Three Laws of Robotics are used to illustrate the problem of rule-based machine morality (the laws create conflicts and unintended consequences), but Mitchell does not engage with the counterfactual: what would a *non-rule-based* moral architecture look like? She gestures at learning from human behavior but correctly notes this inherits all the biases of the training data.
- The chapter discusses both near-term reliability failures and long-term superintelligence risks without clearly ranking them as threats. Mitchell's personal view (reliability failures are the real problem) is stated but could be argued more forcefully.

**Methodological Soundness:** The trolley problem data is compelling precisely because it shows inconsistency within individuals, not just across groups.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-6-on-trustworthy-and-ethical-ai.md`

Key additions: trustworthiness requires reliability, subgroup evaluation, monitoring, accountability, and governance. Thresholds, false-positive costs, subgroup error rates, and use-case stakes matter more than generic accuracy.

Settled: high-stakes AI needs evaluation, monitoring, accountability, and bias assessment. Contested: which uses should be banned, licensed, audited, or left to market forces.

Teaching move: build a confusion matrix by subgroup, then ask which errors matter most in the specific use case.
