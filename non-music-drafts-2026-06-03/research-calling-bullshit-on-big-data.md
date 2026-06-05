### CHAPTER 8: Calling Bullshit on Big Data
**Core Claim:** Machine learning systems are not magical—they are only as good as their training data. Most celebrated AI failures and false promises trace not to algorithmic errors but to garbage-in-garbage-out data problems that non-specialists can identify without opening the technical black box.

**Supporting Evidence:**
- Google Flu Trends: accurate for 2 years, then missed by 2x due to Google Suggest feature changing search behavior; overfitting to a 2003–2008 window
- USPS handwriting recognition: 98% accuracy—appropriate training data, bounded problem, genuine success
- Gaydar algorithm (Wang & Kuzinsky): claimed to detect sexual orientation from facial photos; trained on self-selected dating site photos vs. official ID photos; most likely detecting grooming/self-presentation, not facial structure; claimed prenatal hormone theory support not established
- Criminal face recognition (Wu & Zhang, returned): smile detector, not criminality detector
- Facebook chatbot "inventing its own language": media panic; researchers unconcerned; chatbots had developed repetitive nonsense, not a novel language
- AlphaGo: genuinely impressive, but opacity of decision-making is a feature and a problem
- Husky/wolf classifier: learning snow backgrounds, not animal morphology
- Amazon hiring algorithm: discriminated against women because trained on male-dominated hire history
- COMPAS recidivism algorithm: misclassifies Black defendants as future criminals at nearly 2x the rate of white defendants
- Curse of dimensionality: adding variables requires exponentially more training data

**Logical Method:** The chapter's core analytical move is consistent: identify the training data, identify the labels, identify systematic bias in either, declare the output claims suspect—without examining the algorithm itself.

**Logical Gaps:**
- The Google Flu Trends case is described as a failure of overfitting, but the authors do not clearly distinguish between (a) the algorithm overfitting to 2003–2008 search patterns and (b) the environmental change caused by Google Suggest. These are different failure modes with different prescriptions.
- The Gaydar paper critique is methodologically sound (training data confound, unfair human comparison), but the authors' conclusion that "we suspect the most likely explanation involves grooming and self-presentation" is inferred, not proven. They should flag this more explicitly.
- The chapter argues that "good data" is more important than algorithm sophistication, but the USPS success story involves both good data AND a well-defined problem. The authors underweight problem structure as an independent factor.

**Methodological Soundness:** The "garbage in, garbage out" framework is the chapter's primary analytical contribution and is well-applied. The call for algorithmic transparency and accountability is appropriate but underdeveloped relative to the technical analysis.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-calling-bullshit-on-big-data.md`

Key additions: GIGO starts with a data audit: source, sampling, labels, target, confounds, deployment shift, and error harms. Google Flu Trends combines overfitting and platform-induced distribution shift; USPS success depended on good data and a bounded problem.

Settled: machine-learning systems inherit data and label biases, and distribution shift breaks models. Contested: which fairness metric should govern high-stakes systems when metrics conflict.

Teaching move: before inspecting the model, force a training-data and label audit.
