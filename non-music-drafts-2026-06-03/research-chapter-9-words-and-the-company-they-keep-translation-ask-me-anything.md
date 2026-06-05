### CHAPTER 9 (Chapters 11–13 in audio): Words and the Company They Keep / Translation / Ask Me Anything

**Core Claim:** Natural language processing has achieved remarkable surface performance in speech recognition, machine translation, sentiment analysis, and question answering—but none of these systems understand the language they process. Understanding requires common sense knowledge, and common sense knowledge is what all current systems lack.

**Supporting Evidence:**
- The restaurant story: did the man eat the hamburger? Answering confidently requires inference chains about restaurant norms, sarcasm recognition, action sequencing, and social expectations that no current system can perform
- Deep learning for speech recognition: error rates dropped dramatically post-2012; Google's Android speech recognition correctly transcribed the restaurant story word-for-word but understands nothing about it
- Google Translate's French/Italian/Chinese renderings of the restaurant story: "rare" becomes "infrequent," "bill" becomes "proposed legislation," "bent out of shape" becomes "distorted"—all correct word substitutions, all semantically wrong in context
- Watson on Jeopardy: won but made non-human-like errors (classified "Toronto" as a U.S. city) and was trained on 100,000 Jeopardy clues with single correct answers—a very specific format
- The SQuAD dataset: Alibaba and Microsoft systems exceeded measured human accuracy (87%) on answer extraction from Wikipedia paragraphs, but this is not reading comprehension—the answer is guaranteed to appear in the text
- Winograd schemas: "The city council refused the demonstrators a permit because they feared violence" (who feared violence?). Best AI performance ~61% on ~250 schemas; random guessing is 50%
- Word2Vec: learns that "man is to woman as king is to queen" from statistical co-occurrence, but also that "man is to woman as computer programmer is to homemaker"

**Logical Method:** Systematic breakdown of each NLP subtask → demonstration of what the system actually learned vs. what it is claimed to have learned.

**Logical Gaps:**
- The chapter does not address why the "last 10%" is the hardest in speech recognition with the same analytical rigor applied to vision. Mitchell asserts that understanding may be required for the last 10% without testing whether there is a performance plateau.
- IBM Watson receives extended critical treatment, but Mitchell acknowledges she cannot fully trace what happened between the Jeopardy system and the commercial Watson products. This honest uncertainty is noted but limits the analysis.
- Word2Vec's gender biases are mentioned without fully developing the mechanism: the bias is structural, not incidental. Any system trained on human-generated language will encode the biases of the language-producing culture.

**Methodological Soundness:** The back-translation test (restaurant story through Google Translate and back) is a brilliant empirical demonstration rather than a theoretical claim.

---

## Extended Research Notes

**Pantry note:** `pantry/notes-chapter-9-words-and-the-company-they-keep-translation-ask-me-anything.md`

Key additions: NLP subtask success should be separated into speech recognition, translation, answer extraction, and distributional semantics. Fluent or correct output is not proof of common-sense understanding, especially when the benchmark guarantees the answer's location.

Settled: language models encode statistical and cultural patterns and can perform many NLP tasks. Contested: whether large multimodal/tool-using models possess genuine understanding or robust simulation of it.

Teaching move: compare one question whose answer is extractable with one requiring unstated background knowledge.
