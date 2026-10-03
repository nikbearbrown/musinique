# AI+1 — CLI Video Ideas ("X with Claude")

## Candidate 01 — "Run Three LLMs on the Same Prompt with Claude, Compare the Signatures"
- Source: ai-1/chapters/03-domain-research.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: One LLM gives you an answer. Three give you a map of what is settled, contested, and missed — but only if you can spot the four signature types in the raw output.
- The artifact: A side-by-side comparison table (ALL THREE AGREE / TWO AGREE / DIVERGENT / ONE ONLY) rendered as an animated D3 HTML file, with claim-count bars growing in per-category order.
- Prompt seed: `claude "I am a [profession] researching how AI affects my field. Produce an 8-section structured report: AI tool adoption, failure modes, copyright landscape, fluency trap patterns, labor-market data, irreducibly human taxonomy, existing training, solo-practitioner risk. For each section: cite sources, mark contested claims, distinguish current-state from settled territory. Length 1500-2500 words." > claude-output.md` then repeat for GPT and Gemini, then `claude "Read these three research outputs and classify every claim as ALL-THREE-AGREE, TWO-AGREE, DIVERGENT, or ONE-ONLY. Output as a CSV: claim, category, source_llm."`
- Read / check: Verify that the ONE-ONLY claims from Gemini are traceable; that DIVERGENT rows state all positions without premature synthesis; that the animated bars reflect actual claim counts, not invented ones.
- Human supplies: Run on three real frontier models (Claude, GPT-4o, Gemini) with web search enabled — cannot be faked synthetically. A real profession substituted for [profession] is mandatory; a generic placeholder produces generic output. Synthetic stand-in is NOT acceptable; the divergence pattern only appears in real model outputs.
- Output medium: d3 (animated) — bars growing left-to-right per category, with a sweep line across claim rows.
- The change: Strip the ONE-ONLY claims and re-run the synthesis; show how the brief degrades when the "gap-finding" model is removed from the rotation.
- Teardown angle: The triangulation is not averaging — it is reading three biased reports with professional judgment and marking confidence. The skill is triage, not consensus.
- Exclusions: Model internals, Constitutional AI theory, detailed prompt engineering for any one model, the full 9000-word source brief.
- Score: 9/10

## Candidate 02 — "Build a TIKTOC.md with Claude: Phase-Gate a Textbook Spec in 2 Hours"
- Source: ai-1/chapters/02-what-tic-toc-does.md + 04-generating-your-tiktoc.md (LLM Exercises)
- Lane: BUILD (Claude Code)
- Hook: An author's outline tells the writer what to cover. A TIKTOC.md spec tells the AI what the reader must be able to do — and those are not the same thing. The difference becomes visible the first time you try to write a demonstrable capability verb.
- The artifact: A completed TIKTOC.md file with: capability statements using Bloom's verbs, a Bloom's ceiling table per chapter, and bridge questions linking every chapter — rendered in the terminal and validated against a simple Python gate that checks for prohibited verbs (understand, appreciate, be aware of).
- Prompt seed: `claude "I am building a specification for a practitioner textbook. Run the Tic TOC intake session starting at /i1. My book concept: [user supplies]. Push back if my capability statements use vague verbs (understand, appreciate). Require demonstrable outcomes. Run through /i4, /l1-l4, /c1-c4, /g1, /g2."` then `python3 -c "import re, sys; text=open('TIKTOC.md').read(); bad=['understand','appreciate','be aware','be familiar']; [print(f'FAIL: {b}') for b in bad if b in text.lower()] or print('PASS')"`
- Read / check: Confirm the gate rejects vague verbs in capability statements; confirm the Bloom's ceiling column covers all chapters; confirm bridge questions are stated as questions not topic labels.
- Human supplies: A real book concept to run the session on — substituting a placeholder produces a generic TIKTOC.md. The two-hour session itself requires a human domain expert to answer Tic TOC's pushbacks. Synthetic stand-in is NOT acceptable for the pushback transcript; the friction is the lesson.
- Output medium: screen-recording mp4 — terminal session showing the Tic TOC exchange and the Python gate pass/fail sweep.
- The change: Revise one chapter's capability statement from "understand X" to "defend X in a client review" and re-run the gate to show it now passes.
- Teardown angle: The gate is not the point — the gate is just a proxy for the two-hour cognitive work. Catching vague verbs before 50k words of drafting is the arithmetic.
- Exclusions: Full Tic TOC transcript, the publishing-industry acquisitions framework, detailed Backward Design theory.
- Score: 9/10

## Candidate 03 — "Scaffold a Book in 30 Seconds with new_book.py"
- Source: ai-1/chapters/05-book-scaffold.md (Exercise 5.1, 5.2)
- Lane: BUILD (Claude Code)
- Hook: A directory generated from a spec is not a template. It is the spec made legible as a file system — and the first time you see your chapter list as named empty files, the vague parts of your spec become visible.
- The artifact: A complete book directory created from a real TIKTOC.md, with all 17 scaffold files present, color-coded by audience (Cowork-facing / Human-facing / Build-facing) in a terminal tree view, plus metadata.yaml fully populated.
- Prompt seed: `python3 new_book.py --tiktoc TIKTOC.md --slug my-book && tree my-book/ && python3 -c "import yaml; d=yaml.safe_load(open('my-book/metadata.yaml')); [print(f'MISSING: {k}') for k in ['title','author','publisher','rights','language','date','description','identifier'] if not d.get(k) or '<' in str(d.get(k,''))]"`
- Read / check: Confirm the script refuses to overwrite an existing directory; confirm all 17 expected files exist; confirm the TIKTOC.md chapter list maps to files in chapters/; confirm the metadata check gate fires on placeholder values.
- Human supplies: A completed TIKTOC.md from a prior session. The new_book.py script from the AI+1 pipeline (available from the Bear Brown repository). Nothing requiring a screen-recording of actual model output — this is a pure Python build step.
- Output medium: screen-recording mp4 — terminal running the scaffold command, tree output, metadata gate.
- The change: Delete the directory, introduce one vague chapter title into TIKTOC.md (no capability verb), re-run — show that the scaffold still generates but the spec's gap is now a named empty file with no spec.
- Teardown angle: The scaffold is not the output of the script. It is the output of the Tic TOC session, made visible as files. The script is a mirror, not a generator.
- Exclusions: pandoc build pipeline (Chapter 12), full directory audience taxonomy lecture, Python installation walkthrough.
- Score: 8/10

## Candidate 04 — "Audit a Pantry File with Claude: Catch the 'Studies Show' Pattern"
- Source: ai-1/chapters/06-research-pass.md (LLM Exercises)
- Lane: BUILD (Claude Code)
- Hook: A pantry file that says "studies show 78% of design firms are integrating AI" looks like research. It is the grammatical form of research with the substance removed — and Claude will draft an authoritative-sounding chapter from it unless you run the audit first.
- The artifact: A Python script that reads pantry/*.md files and flags: (a) unsourced percentage claims, (b) "studies show" / "research indicates" without named study, (c) examples from off-domain fields. The output is a JSON audit report with flagged lines, rendered as a color-coded terminal table.
- Prompt seed: `claude "Read this pantry file and audit it against these three criteria: (1) every numeric claim must name a source with enough metadata to find it; (2) 'studies show' without a named study is a flag; (3) every example must belong to the book's primary domain [domain]. Output as JSON: {flagged: [{line, reason, severity}], passed: count}." < pantry/ch-03.md`
- Read / check: Verify that the flagged items are genuinely unsourced (not just paraphrased with citation later); verify that the domain-example check correctly identifies off-domain examples; verify the JSON parses cleanly.
- Human supplies: A real pantry file from the AI+1 pipeline, or a synthetically constructed one containing the failure patterns. A synthetic file with planted failures is acceptable for the video — the audit patterns are illustrative, not dependent on real research content.
- Output medium: screen-recording mp4 — terminal showing the audit run, color-coded flag output, then the corrected pantry file side-by-side.
- The change: Correct the top three flagged items (add a real source, drop the off-domain example, replace "studies show") and re-run the audit to show the flag count drop.
- Teardown angle: The pantry audit is the fluency trap check run on your own research before it poisons the draft. The habit starts at the research layer, not the chapter layer.
- Exclusions: Full nine-section pantry structure lecture, Chapter Research Gatherer prompt internals, the three-LLM domain research method.
- Score: 8/10

## Candidate 05 — "Detect the Five Chapter-Draft Failure Modes with Claude"
- Source: ai-1/chapters/07-chapter-writing.md (LLM Exercises)
- Lane: BUILD (Claude Code)
- Hook: A log.csv of 14 green rows looks like a finished book. The first paragraph of any chapter tells the truth — "in today's rapidly evolving design landscape" is the sound of the fluency trap running at chapter scale.
- The artifact: A Claude-powered chapter auditor that reads a Cowork draft and classifies each paragraph against five failure modes: generic-field language, unsourced "studies show" claims, off-domain examples, vague bridge questions, and capability statements with no demonstrable verb. Output: an annotated markdown file with failure-mode callouts.
- Prompt seed: `claude "Read this chapter draft and classify every paragraph against these five failure modes: (1) generic-field language that would work in any profession, (2) percentage claims without named sources, (3) examples from outside the book's domain, (4) bridge questions that are topic labels not questions, (5) capability verbs that are 'understand'/'appreciate' rather than demonstrable. Output as annotated markdown with [FAILURE-MODE-N] tags." < chapters/01-draft.md`
- Read / check: Verify that the "in today's rapidly evolving X landscape" pattern is caught as failure mode 1; verify the annotation tags are parseable; verify the tool does not false-flag domain-specific prose as generic.
- Human supplies: A real Cowork chapter draft, or a synthetic one containing the planted failure patterns. A synthetic draft is acceptable for the video — the five failure modes are illustrative, not dependent on real chapter content.
- Output medium: screen-recording mp4 — terminal running the auditor, annotated output scrolling, then the human rewrite of one flagged paragraph.
- The change: Run the auditor on the human-rewritten version of the same chapter and show the failure count drop from five to zero.
- Teardown angle: The auditor is not a replacement for the human rewrite. It is the difference between reading your own draft with fresh eyes and reading it as the AI's version of you.
- Exclusions: Full Chapter Writer Cowork architecture, TIKTOC.md spec internals, pandoc build pipeline.
- Score: 8/10

## Candidate 06 — "Build a CAJAL Figure Spec and Pass the 6-Component Gate"
- Source: ai-1/chapters/11-creating-figures.md (LLM Exercises)
- Lane: BUILD (Claude Code)
- Hook: The image model wants to give you 14 labeled nodes, 3 legends, and a pair of decorative gears. The SCOPE exclusion list is the only thing standing between you and a figure that looks polished and teaches nothing.
- The artifact: A CAJAL SCOPE specification for one figure, plus a Python gate that checks: component count ≤ 8, an exclusion list is present, no decorative elements named, no "and" conjunctions in the figure description (which signal two figures in disguise). Gate output: PASS/FAIL with line-level callouts.
- Prompt seed: `claude "I need a figure showing [concept]. Build a CAJAL SCOPE specification: S=canvas specs, C=exactly which concepts and relationships, O=spatial layout logic, P=presentation constraints (flat vector, colorblind-safe, no gradients), E=exclusion list of what must NOT appear. Apply the 6-to-8 component ceiling. Name a specific thing this figure will NOT show even though it is adjacent to the concept."` then `python3 cajal_gate.py scope.md`
- Read / check: Verify the component count in C is ≤ 8; verify E names at least two specific exclusions; verify the Python gate correctly flags a spec with "and" conjunctions as a split candidate.
- Human supplies: A concept from a real chapter to spec the figure for. The gate script (approximately 20 lines of Python — writable within the video). Nothing requiring external assets — fully synthetic.
- Output medium: screen-recording mp4 — terminal running the SCOPE prompt, gate script, PASS output, then a deliberate overcount failure and gate FAIL.
- The change: Introduce a ninth component into the spec; re-run the gate to show the FAIL, then split into two specs and show both passing.
- Teardown angle: The exclusion list is more important than the inclusion list. Anyone can say what a figure is about. The figure that fails is the one where no one wrote down what it is NOT about.
- Exclusions: SVG-to-PNG build pipeline, CAJAL command set internals, working-memory theory lecture.
- Score: 9/10

## Candidate 07 — "Stress-Test a Bloom's Ceiling Distribution with Claude"
- Source: ai-1/chapters/02-what-tic-toc-does.md (LLM Exercise 3)
- Lane: BUILD (Claude Code)
- Hook: A Bloom's ceiling table with Apply, Evaluate, Evaluate, Apply, Create, Evaluate, Create looks like a real cognitive arc. But two Create chapters at the end, with no Apply prerequisites for the second, is a prerequisite gap that ships into 50,000 words of drafting.
- The artifact: A Python script that reads a TIKTOC.md Bloom's ceiling table and checks: (a) no Create-level chapter lacks a prerequisite Apply/Analyze chapter in the chapters before it, (b) no more than two Create chapters appear in the final three chapters, (c) the arc rises from left to right with no unexplained reversals. Output: a Manim animation of the Bloom's arc as a step chart, with flagged violations marked in red.
- Prompt seed: `claude "Here is a Bloom's ceiling distribution for a [N]-chapter textbook: [list]. Critique this distribution. Is it well-designed for a practitioner textbook? Identify: (1) prerequisite gaps where a Create chapter lacks a prior Apply chapter, (2) clusters of Evaluate chapters with no Create destination, (3) downward reversals in the arc. Output as JSON: {gaps: [], clusters: [], reversals: []}."` then feed JSON to Manim step-chart renderer.
- Read / check: Verify that the JSON flags a Create chapter at position 5 when position 3 is the only prior Apply chapter; verify the Manim arc renders the Bloom's level names correctly on the y-axis; verify red markers appear on flagged chapters.
- Human supplies: A real or synthetic TIKTOC.md Bloom's ceiling table. Synthetic is fully acceptable — the distribution pattern is the lesson, not the content. Manim installed (standard vox toolkit dependency).
- Output medium: Manim (animated) — step chart sweeping left to right, red flags dropping onto violation chapters.
- The change: Revise the distribution to fix one prerequisite gap (insert an Apply chapter before the flagged Create) and re-render to show the flag disappear.
- Teardown angle: The Bloom's arc is not aesthetic — it is a prerequisite sequence commitment. A Create chapter without an Apply foundation is a defect that costs 10-100x more to fix in the manuscript than in the spec.
- Exclusions: Full Bloom's taxonomy revision history, Gagné's conditions of learning, the TIKTOC.md /l1-l4 session transcript.
- Score: 8/10

## Candidate 08 — "Run the AI+1 Exercise Audit: Catch the Interchangeable Pattern"
- Source: ai-1/chapters/10-enrichment-for-ai.md (LLM Exercise 2)
- Lane: BUILD (Claude Code)
- Hook: An LLM Exercise that says "ask Claude to explain the eight-section structure of a textbook chapter" is not an exercise — it is Claude documentation dressed as pedagogy. The three-question audit catches it in 30 seconds. The audit that catches it after 60 exercises takes about 5 minutes.
- The artifact: A Claude-powered exercise auditor that takes a set of LLM Exercises and classifies each against three questions: (1) transplant test — does it break if you swap the field name? (2) reader-brings-something test — does the reader supply a real artifact from their domain? (3) deliverable-is-judgment test — is the output a reader-produced verdict, not raw model output? Output: a CSV with PASS/FAIL per question per exercise, plus a summary of the three failure patterns.
- Prompt seed: `claude "Here are [N] LLM Exercises from a textbook on [field]. For each, apply the AI+1 three-question audit: (1) transplant test: would this exercise work unchanged in a textbook on accounting or veterinary medicine? (2) reader-brings test: does it require the reader to supply something only they have — a real brief, client, portfolio, remembered failure? (3) deliverable test: is the output a judgment the reader produces, not just LLM text to read? Output as CSV: exercise_id, q1, q2, q3, overall." < exercises.md`
- Read / check: Verify that a generic "ask Claude to explain X" exercise fails all three; verify that a specific "paste your own client brief and identify three places Claude missed something" exercise passes all three; verify the CSV is clean.
- Human supplies: A set of LLM Exercises from a real or synthetic chapter draft. A synthetic set with planted failures (one generic, one no-deliverable, one interchangeable pair) is fully acceptable.
- Output medium: screen-recording mp4 — terminal running the auditor, CSV output, then the hand-rewrite of one failing exercise.
- The change: Run the stress-test prompt from Exercise 3 on the rewritten exercise to confirm the model agrees it now passes all three.
- Teardown angle: The audit does not improve the exercises — you do. The generator produced the failure once and will produce it again. The rewrite is the irreducibly human layer at the pedagogy scale.
- Exclusions: Freire's Pedagogy of the Oppressed lecture, the Wayback Machine historical figure section, Chapter 00 generation details.
- Score: 8/10

## Candidate 09 — "Fact-Check a Chapter with Claude's Fact-Checking Assistant"
- Source: ai-1/chapters/12-final-check-and-build.md
- Lane: BUILD (Claude Code)
- Hook: The Fact-Checking Assistant scans every assertion in a chapter and classifies it along two dimensions — type (empirical, historical, definitional, contested) and confidence (verified, probably-true, unverified, flagged). The output is not a list of errors. It is a map of where the author needs to be a scholar.
- The artifact: A Claude-powered fact-checker that reads a chapter file and outputs a JSON audit: each assertion classified by type and confidence, with a summary count per category and a list of HIGH-PRIORITY flags (contested claims stated as settled, invented citations, precision illusions).
- Prompt seed: `claude "Read this chapter and classify every assertion. For each: (1) type: empirical/historical/definitional/contested, (2) confidence: verified/probably-true/unverified/flagged, (3) flag if: a percentage claim lacks a named source, a named study cannot be verified in 5 minutes, a contested claim is stated as settled. Output as JSON: {assertions: [{text, type, confidence, flag, reason}], summary: {counts, high_priority}}." < chapters/03-domain-research.md`
- Read / check: Verify that "Studies show 78%" triggers a HIGH flag; verify that a correctly attributed claim (Curtis, Krashen, 1988) passes; verify the JSON parses; verify the summary count matches the flagged-assertions list length.
- Human supplies: A real chapter file with a mix of sourced and unsourced claims. A synthetic chapter with planted citation failures is acceptable — the pattern is illustrative.
- Output medium: screen-recording mp4 — terminal running the fact-checker, JSON output, HIGH flags highlighted.
- The change: Correct one HIGH-flagged claim (remove an invented percentage, replace with "a substantial majority") and re-run to show the flag disappear.
- Teardown angle: The fact-checker does not verify claims — you do. It maps the territory so you know which claims need five minutes of search before you ship 50,000 words.
- Exclusions: EPUB/PDF build pipeline, pandoc metadata YAML, full Appendix citations list.
- Score: 7/10

## Candidate 10 — "Build the Enrichment Generator's Chapter 00 — Domain-Specific Claude Basics"
- Source: ai-1/chapters/10-enrichment-for-ai.md (LLM Exercise 1)
- Lane: BUILD (Claude Code)
- Hook: A Chapter 00 that says "Claude is a large language model that can answer questions and assist with creative tasks" has failed the AI+1 standard before the first chapter begins. A Chapter 00 that says "Claude can read a client brief and tell you what the brief is not saying — but cannot tell you whether this particular client tends to backslide on color choices three weeks into a project" has passed.
- The artifact: A Claude-generated Chapter 00 for a practitioner textbook in a specified field, then a three-question AI+1 audit of the generated chapter: (a) do capabilities name specific workflows not just model abilities? (b) do failure modes name specific tools and workflow moments? (c) is there a worked example with a real artifact (not a hypothetical client)?
- Prompt seed: `claude "Generate Chapter 00 'Claude Basics for [field]' for a practitioner textbook. Four sections: (1) what Claude can and cannot do for [a specific practitioner type] — pair every capability with a workflow moment and every limitation with a domain-specific failure pattern, (2) when to use Claude vs Claude Project vs Claude Code — with estimated distribution by workflow stage, (3) a worked example with an anonymized real artifact, (4) five field-specific failure modes named with tool and workflow context. No generic statements that would work for any profession."` then run AI+1 audit.
- Read / check: Verify that section 1 names at least three specific workflow moments (not just "creative tasks"); verify the worked example is domain-specific (not a hypothetical); verify the audit correctly flags any remaining generic sentences.
- Human supplies: A specific profession for the [field] substitution. The richer the practitioner context, the more specific the output. Synthetic is acceptable if the field is specified precisely.
- Output medium: screen-recording mp4 — terminal running the generator, then the audit prompt, then one targeted rewrite of a flagged generic section.
- The change: Run the audit's transplant test ("could this be retitled 'Claude Basics for Accountants' with search-and-replace?") and show one section failing, then revise to pass.
- Teardown angle: The binding of LLM behavior to domain workflow is the whole distinction between AI+1 and generic. When the binding is tight, the chapter passes. When it is loose, the chapter is documentation.
- Exclusions: Full enrichment generator three-phase pipeline, Dig Deeper vs LLM Exercise distinction lecture, AI Wayback Machine section.
- Score: 7/10
