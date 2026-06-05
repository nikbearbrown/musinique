### CHAPTER 2: Aligning the Alien

**Core Claim:** The alignment problem—ensuring AI systems pursue human-beneficial goals—operates at multiple levels simultaneously: existential (paperclip maximizer/ASI), practical (bias and fairness), and behavioral (jailbreaking and misuse). Current RLHF-based approaches partially address behavioral alignment while leaving existential alignment unsolved.

**Supporting Evidence:**
- Expert panel estimated 12% probability of AI killing ≥10% of humans by 2100; futurists estimated 2%
- GPT-4 pre-RLHF could: provide kill-as-many-people-as-possible instructions for under $1, write violent threats, recruit for terrorist organizations
- Bloomberg study: Stable Diffusion depicted judges as male 97% of time (vs. 34% actual female judges); fast food workers as darker-skinned 70% of time (vs. 70% actually white)
- GPT-4 gender bias: more likely to correctly identify "the lawyer" when pronoun was male; more likely to misidentify as "the assistant" when pronoun was female
- Napalm jailbreak: theatrical framing bypassed content filters producing detailed synthesis instructions
- RLHF workers: trauma from exposure to graphic content; low pay; described as "testing the ethical boundaries" of their own contract workers
- LLMs show human-equivalent moral judgments 93% of time after RLHF fine-tuning

**Logical Method:** Layered threat analysis from most extreme (ASI extinction) to most immediate (bias, misuse), with RLHF positioned as partial mitigation of behavioral layer.

**Logical Gaps:**
- The 12% extinction probability figure is presented without interrogation of how such a probability is estimated for unprecedented events. Experts assigning probability to non-base-rate events are expressing intuition, not calculating from data.
- The napalm jailbreak example is vivid but the solution it implies—better content filtering—is immediately undermined by acknowledging "it may be impossible to avoid these sorts of deliberate attacks." The chapter raises the problem more clearly than it proposes solutions.
- "AI has made the same moral judgments as humans do in simple scenarios 93% of the time"—this conflates moral judgment in low-stakes test scenarios with moral judgment in high-stakes deployment conditions. The 7% error rate at scale has enormous implications not examined here.
- The RLHF workers section is one of the book's most important and most underexplored: the labor conditions of alignment workers are treated as a paragraph-length ethical concern rather than as a structural argument about whose values are being embedded in AI systems.

**Methodological Soundness:** The alignment framing is accurate and useful. The chapter's most intellectually honest move is acknowledging that AI companies "signed a statement about extinction risk and continued development anyway." This contradiction is named but not resolved.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-aligning-the-alien.md`

Key additions: alignment has layers: existential, misuse, bias/fairness, truthfulness, conversational safety, and labor/governance. RLHF is behavioral alignment, not a full solution. Bias and content-moderation labor are not side issues; they are part of how alignment is built.

Settled: RLHF improves some behaviors but is incomplete; jailbreaks and bias persist. Contested: x-risk probabilities and what alignment should optimize.

Teaching move: classify each AI risk by layer and match it to a mitigation that also names what it does not solve.
