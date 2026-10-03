# AI-1 Video Ideas

## Candidate 01 — Why Seeing Finished Prose Makes You Stop Thinking
- Source: `ai-1/chapters/01-what-ai-plus-one-is.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: A student reads AI output, decides it looks right, and submits it — the error was never visible from the outside.
- Key case: A course designer receives a three-paragraph learning-objectives block from Claude. Each paragraph is grammatically clean, logically structured, and confidently worded. The designer approves all three. Two contain objectives that cannot be assessed. The flaw was invisible because the prose itself triggered a sense of completeness.
- The Question: Fluent prose should signal a complete thought. Here is the case where it signaled an empty one. Why?
- Core idea: Two components lock together — statistical coherence (the model produces output with the shape of correct prose) and processing fluency reward (the human brain reads smoothly flowing text as credible) — and together they close the critical loop before judgment can run.
- Visual object: A two-part lock mechanism: one gear labeled COHERENCE, one labeled FLUENCY REWARD, clicking shut around an empty vault labeled JUDGMENT BYPASSED
- Manim move: accumulate
- Example seed: A freelance instructional designer uses Claude to draft five learning objectives for a compliance module. She reads them, nods — they sound like objectives she'd write. She submits. On QA, two objectives describe activities ("students will explore…") with no measurable outcome. The AI's prose was indistinguishable from her own; her fluency-reward loop never signaled to look harder.
- Length band: 3–5 min
- Still lanes: geo (lock mechanism plate), geo (two-bar input → output flow)
- Prerequisites: what a language model is (roughly)
- Exclusions: no Stochastic Parrots paper history, no full Alter-Oppenheimer study exposition, no discussion of what constitutes a good learning objective, no model architecture explanation
- Score: 9/10

## Candidate 02 — Why Leaving Things Out Is Harder Than Putting Them In (The Figure Problem)
- Source: `ai-1/chapters/11-creating-figures.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: Every element you add to a figure competes with every other element for four slots.
- Key case: An instructional designer shows CAJAL a figure with 14 labeled components and asks for feedback. CAJAL returns a list of suggested additions. The figure now has 17 components. A student looking at it sees a diagram, not an explanation.
- The Question: Adding more information to a figure should make it more informative. Here is the case where it made it less learnable. Why?
- Core idea: Cowan's ceiling — working memory holds roughly 4 chunks, not Miller's 7 — means a figure with more than 6–8 labeled components asks the reader to process a system they cannot hold; the Exclusions field of a figure spec carries more weight than the inclusions.
- Visual object: Two figures side by side — one with 14 labeled nodes (reader bouncing between them), one with 4 nodes (reader traces the path); the 4-node version teaches in one pass
- Manim move: collapse
- Example seed: A learning designer building a figure of the peer-review pipeline starts with 12 labeled boxes. She runs the SCOPE frame, writes the E (Exclusions) section first — cuts editorial board routing, copy-editing, indexing, production — and ends with 5 boxes. Student comprehension on a posttest question doubles.
- Length band: 3–5 min
- Still lanes: geo (side-by-side overloaded vs. stripped figure plates), geo (working memory slot diagram)
- Prerequisites: what a figure is supposed to do (basic); no prior chapters required
- Exclusions: no Miller's law history, no cognitive load theory formalism (CLT), no discussion of specific chart types, no color-theory exposition, no detailed SCOPE walkthrough beyond naming the five parts
- Score: 9/10

## Candidate 03 — Why Asking Three AIs the Same Question Gets You One Answer
- Source: `ai-1/chapters/03-domain-research.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: One model gives you a confident answer; three models give you a map of what is actually known.
- Key case: A researcher asks Claude what the evidence says about spaced repetition in professional certification prep. Claude returns a clean, confident paragraph with three examples. She asks GPT-4 the same question. It returns different examples — also confident. She asks Gemini. It qualifies two of Claude's three examples as contested. The confident paragraph was a snapshot from one model's training distribution, not a map of the evidence.
- The Question: Using a more capable AI model should produce a more reliable answer. Here is the case where a more capable model produced a more confidently wrong one. Why?
- Core idea: Each model has a characteristic signature — Claude flags uncertainty, GPT enumerates confidently, Gemini grounds in retrieval — so comparing the three reveals where they converge (settled), diverge (contested), and where only one speaks (missing). The gap between them is the actual research question.
- Visual object: Three overlapping circles (one per model) with a synthesis node at the center labeled ALL THREE AGREE; outer regions labeled TWO AGREE, DIVERGENT, ONE ONLY
- Manim move: accumulate
- Example seed: A textbook author asks all three models about the evidence base for retrieval practice outperforming re-reading. Claude: "robust, 200+ studies." GPT: "strong, meta-analyses support." Gemini: "strong for recall tasks; mixed for transfer." Author writes: "retrieval practice robustly outperforms re-reading for recall; transfer evidence is mixed." That last clause came from the gap.
- Length band: 3–5 min
- Still lanes: geo (three-circle Venn plate with synthesis node), geo (signature comparison table)
- Prerequisites: what a language model is (roughly); that models can give different answers
- Exclusions: no model architecture explanation, no prompt-engineering tutorial, no discussion of RAG or grounding techniques, no citation of the Stochastic Parrots paper, no full four-synthesis-marker taxonomy walkthrough
- Score: 8/10

## Candidate 04 — Why Studying Harder With AI Gets You a Lower Grade Without It
- Source: `ai-1/chapters/97-fundamental-themes.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: Students who used AI during practice outperformed their peers by nearly half a standard deviation — then scored worse on the exam.
- Key case: In Bastani's study, students assigned AI tutoring during math practice scored 48% higher during the practice phase. On the unassisted exam, they scored 17 percentage points lower than the control group.
- The Question: AI-assisted practice should transfer to unassisted performance — that is what practice is for. Here is the case where it did the opposite. Why?
- Core idea: When AI scaffolds every problem step, the encoding events that build durable retrieval pathways never fire. Students learn to navigate the AI, not the concept — so when the AI is removed, the retrieval pathway is absent.
- Visual object: Two bars rising side by side (PRACTICE SCORE: AI group towering), then a second pair (EXAM SCORE: AI group lower) — the bars reverse
- Manim move: compare
- Example seed: A professional certification program adds an AI study assistant to its prep course. Learners finish practice modules 40% faster. Pass rates on the proctored exam fall 12 points in the first cohort. The program director assumes the exam got harder. The next cohort is randomized: half with AI assist, half without. Same result. The AI was doing the retrieval for them.
- Length band: 3–5 min
- Still lanes: geo (two-bar reversal plate), geo (encoding pathway diagram)
- Prerequisites: basic idea of retrieval practice; what an exam is
- Exclusions: no SM-2 algorithm exposition, no Ebbinghaus forgetting curve formalism, no discussion of the Kosmyna EEG finding (save for a separate card), no full tier-taxonomy walkthrough, no Bloom's taxonomy
- Score: 8/10

## Candidate 05 — Why Asking AI to Explain Things Stops You From Learning Them
- Source: `ai-1/chapters/15-glimmers.md`, `ai-1/chapters/20-ask-ai-everywhere.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: Every time a student asks AI to explain something, the AI does the cognitive work the student needed to do.
- Key case: Maya is writing a case analysis on a design ethics scenario. She's stuck on why the stakeholder mapping matters. She types the question into Claude. Claude explains in three clear paragraphs. Maya reads them, feels unstuck, and moves on. Three weeks later she cannot reconstruct the reasoning — she never built it.
- The Question: Having an expert explain something clearly should produce understanding. Here is the case where it produced recognition without learning. Why?
- Core idea: Explanation triggers recognition (smooth reading, sense of familiarity) but not the generation events — retrieval, elaboration, self-explanation — that encode durable knowledge. The Glimmer design inverts the loop: AI interrogates the student, forcing the generation the student was about to outsource.
- Visual object: A forked path from a single stuck-student node — left path goes to VENDING MACHINE (student asks, AI explains, recognition fires, nothing encodes); right path goes to INTERROGATING LOOP (AI probes, student generates, encoding fires)
- Manim move: split
- Example seed: A cohort of MBA students uses an AI study partner for a strategy module. Group A uses it in vending-machine mode (ask for explanations). Group B uses Glimmer mode (AI asks escalating probes until the student can explain without help). On a transfer case two weeks later, Group B outperforms by 22% on novel application questions.
- Length band: 3–5 min
- Still lanes: geo (forked-path plate), geo (encoding vs. recognition loop diagram)
- Prerequisites: basic idea that learning requires some effort; what an AI chatbot does
- Exclusions: no full Glimmer four-component walkthrough, no Socratic method history, no desirable difficulty formalism, no Roediger citation parade, no discussion of grading Glimmer outputs
- Score: 8/10

## Candidate 06 — Why "The Reader Learns to Use AI" Is Not a Learning Objective
- Source: `ai-1/chapters/04-generating-your-tiktoc.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: The most common capability statement in AI-literacy courses describes an activity, not a competency.
- Key case: A curriculum designer writes: "The reader learns to use AI in their design practice." The Tic TOC diagnostic /g2 prompt returns a 7-failure-mode grid. Failure mode 1: no domain constraint. Failure mode 3: no ceiling (what decisions stay human). The capability statement is grammatically complete and intellectually empty.
- The Question: A capability statement should specify what the learner can do after the course. Here is the case where it specified what the learner will do during it. Why?
- Core idea: Capability statements collapse when they describe the tool use rather than the domain judgment — "use AI" maps to no Bloom's level, no assessment, no ceiling. The refinement staircase — vague topic → add constraint → add action → confirmed ceiling — produces a statement that is falsifiable and assessable.
- Visual object: A four-rung staircase: rung 1 "use AI in design," rung 2 "use AI in UX audits," rung 3 "use AI to identify accessibility gaps," rung 4 "identify which accessibility decisions must stay human and defend that map to a client" — each rung narrower and taller
- Manim move: transform
- Example seed: An instructional designer is building an AI-literacy module for HR professionals. She starts with "learners will leverage AI tools in hiring workflows." Four refinement moves: domain constraint (bias detection in resume screening), action constraint (flag vs. decide), ceiling (what the human must own), assessment (defend the flag list to a hiring panel). Final statement: "Learners will identify which screening signals require human judgment and articulate why to a panel."
- Length band: 3–5 min
- Still lanes: geo (four-rung staircase plate), geo (Bloom's ceiling distribution bar)
- Prerequisites: basic idea of a learning objective; what a curriculum is
- Exclusions: no Bloom's taxonomy history, no full /g2 seven-failure-mode grid, no discussion of Tic TOC phases beyond capability statement refinement, no competency-based education formalism
- Score: 8/10

## Candidate 07 — Why Rereading Feels Like Learning but Isn't
- Source: `ai-1/chapters/16-spaced-repetition.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: Rereading produces a strong sense of familiarity — which the brain reports as understanding.
- Key case: A graduate student rereads her notes the night before a qualifying exam. The material feels completely familiar by the end of the session. She fails two retrieval questions the next morning on concepts she'd reread three times.
- The Question: Reading material until it feels completely familiar should produce durable recall — that is what "knowing it" feels like. Here is the case where familiarity produced zero retrieval. Why?
- Core idea: Recognition and retrieval are separate encoding events. Rereading strengthens the recognition pathway (smooth, familiar feeling) but does not fire the retrieval pathway — the retrieval event only fires when the memory is pulled from scratch with nothing on the page. Spacing adds a second mechanism: retrieval after a delay requires the memory to be reconstructed, deepening encoding each time.
- Visual object: A forgetting curve that drops steeply, then three spaced-retrieval spikes that each reset the curve at a higher floor — versus a flat "rereading" line that never dips but also never consolidates
- Manim move: decay / trace
- Example seed: A professional takes an online compliance module and rerereads the case studies twice before the quiz. She scores 90%. Three weeks later the organization runs a surprise scenario audit. She recalls 40% of the procedural steps. A colleague who used the module's built-in spaced quiz feature at days 1, 3, and 7 recalls 78%.
- Length band: 3–5 min
- Still lanes: geo (forgetting curve with spaced spikes plate), geo (recognition vs. retrieval pathway split)
- Prerequisites: basic idea that memory can fail; no technical prior chapters required
- Exclusions: no SM-2 algorithm formula or numerical exposition, no Ebbinghaus historical biography, no discussion of Anki or .apkg format, no desirable difficulty formalism citation
- Score: 8/10

## Candidate 08 — Why the Research Note That Looks Like a Citation Isn't One
- Source: `ai-1/chapters/06-research-pass.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: A sentence with a number, a percentage, and a hedged claim looks exactly like a sentence with a source — but only one of them had a retrieval event.
- Key case: A textbook author reads a Cowork draft that contains the line: "Studies show that 78% of design firms now require AI fluency in senior hires." The sentence has a precise number, is hedged with "studies show," and is placed correctly in the argument. The author marks it [verify]. The number is unfindable. It was generated with the shape of a citation but no citation exists.
- The Question: A sentence with a percentage and a hedge should flag its source clearly. Here is the case where it had the shape of a citation and no source at all. Why?
- Core idea: Language models are trained on text that includes citations, so they produce citation-shaped sentences. The pantry system requires a retrieval event for every factual claim — the note must name the source before the sentence can appear in the chapter, making AI-laundered statistics structurally impossible if the gate holds.
- Visual object: Three stacked layers — SOURCE (article, study), NOTE (pantry annotation with retrieval marker), CHAPTER (sentence) — with an illegal shortcut arrow bypassing the note layer, blocked by a gate
- Manim move: split
- Example seed: An author drafts a chapter section on remote work productivity. Cowork produces: "Research consistently shows a 23% productivity gain for knowledge workers in hybrid arrangements." The author searches for 30 minutes. Finds a McKinsey report with no percentage, a Stanford study with a different measure, and no 23% figure anywhere. The [verify] flag held. She cuts the number and writes: "Research on hybrid productivity is mixed; the largest gains appear in roles with high autonomy."
- Length band: 2–3 min
- Still lanes: geo (three-layer stack with blocked shortcut plate), geo (citation-shaped text vs. cited text comparison)
- Prerequisites: basic idea of a citation; what a textbook draft is
- Exclusions: no Zettelkasten history or formalism, no full pantry nine-section anatomy, no discussion of the four evaluation questions in detail, no citation management software comparison
- Score: 7/10

## Candidate 09 — Why the Author's Voice Disappears by Paragraph Three
- Source: `ai-1/chapters/08-the-human-rewrite.md`
- Topic: AI-ASSISTED AUTHORSHIP
- Hook: A Cowork draft and an authored chapter look nearly identical from the outside — until you read the first three paragraphs of each.
- Key case: Two opening paragraphs, 75 words each, are placed side by side. Version A opens with a scene — a specific designer, a specific decision, a named trade-off. Version B opens with a thesis statement, three supporting points, and a transition sentence. A reader identifies which is Cowork by the second sentence. The difference is not grammar. It is what is present and who put it there.
- The Question: Trained on millions of published texts, a language model should produce prose that sounds like the author it is working with. Here is the case where it produced prose that sounded like every author at once. Why?
- Core idea: Cowork drafts toward the center of its training distribution — the most statistically average "correct chapter opening." Author voice is built from deviation: the specific scene chosen, the trade-off named, the aside risked. The human rewrite is not editing — it is the act of reinserting deviation that the model statistically suppressed.
- Visual object: Two text panels side by side — one with "voice fingerprint" nodes highlighting specificity markers (scene, trade-off, aside, named person), one flat and unmarked — the marked one is the author's
- Manim move: compare
- Example seed: A learning designer finishes a chapter on accessibility audits. Cowork opens with: "Accessibility audits are a critical component of inclusive design practice. This chapter examines the key steps involved and their rationale." The author's rewrite opens: "Marcus spent four hours on a WCAG checklist before realizing the product had no keyboard focus states — the checklist had no row for it." The Cowork opening has no scene, no named person, no trade-off. It is correct and empty.
- Length band: 2–3 min
- Still lanes: geo (side-by-side text comparison plate with specificity markers), c2v (optional writer-at-desk figure for the cold open)
- Prerequisites: basic idea of a textbook chapter; what an AI writing assistant does
- Exclusions: no Sommers 1980 revision study exposition, no Combined Test 14-item walkthrough, no discussion of the 3-pass rewrite sequence, no literary theory, no discussion of other AI writing tools
- Score: 7/10
