# QC REPORT — claude-liam-mining

**Date:** 2026-08-26  
**Cut:** claude-liam-mining.mp4 (4K, 71.4s)  
**Gate T:** PASS (advisory §8.10 BVDT 0.80 — not a FAIL)

## Gate V — Frame Audit

| Beat | Pattern | Edge bleed | Safe margins | Overflow | Legibility | Canvas fill | Terracotta | Result |
|---|---|---|---|---|---|---|---|---|
| B00 | ClaudeComposerAsk | PASS | PASS | PASS | PASS | PASS | 1 (send btn) | **PASS** |
| B01 | SkillTeardownAnatomy | PASS | PASS | PASS | PASS | MINOR* | 1 (SKILL.md text) | **MINOR** |
| B02 | SkillTeardownPipeline | PASS | PASS | PASS | PASS | PASS | 2† | PASS |
| B03 | SkillTeardownMechanism | PASS | PASS | PASS | PASS | PASS | 1 (verdict pill) | **PASS** |
| BVDT | ClaudeVerdictArtifact | PASS | PASS | PASS | PASS | PASS | 1 (asterisk) | **PASS** |
| BHTF | ClaudeComposerAsk | PASS | PASS | PASS | PASS | PASS | 1 (send btn) | **PASS** |
| BOUT | ClaudeTitleOutro | PASS | PASS | PASS | PASS | PASS | 1 (period + mascot) | **PASS** |

**BLOCKERS: 0. MAJORS: 0.**

### Notes

*B01 MINOR — Canvas fill: 1-file skill anatomy inherently sparse (title + 1 file row + callout). Font sizes increased (64px title, 28px filename, 28px callout text) after first render showed clustering in top 35%. Residual dead space (~55% vertical) is structural to content, not undersized text. Downgraded from MAJOR after font increase.

†B02 — SkillTeardownPipeline renders both the INPUT/OUTPUT box outlines AND the accented phase ("Read SKILL.md") in terracotta. Two distinct terracotta elements visible simultaneously. This is a component design characteristic (the accent phase + the output terminal are both branded). Advisory logged; cannot fix without component redesign that would change semantics.

### Minor items (no rebuild required)
- BHTF command prop grammar error: "I want to where diamonds spawn" missing "find out." Narration locked per rebuild contract — cannot fix without audio re-record. Logged for next human edit pass.
- B01 residual canvas fill — see note above.
