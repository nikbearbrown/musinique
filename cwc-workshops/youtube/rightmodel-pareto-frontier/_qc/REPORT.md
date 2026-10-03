# _qc/REPORT.md — rightmodel-pareto-frontier

**Date:** 2026-08-26  
**Cut:** rightmodel-pareto-frontier-slate.mp4  
**Duration:** 306.8s (5:06)  
**Audio:** AAC, mean_volume -24.3 dB ✓

---

## Frame sampling

- 2fps grid: 614 frames extracted to `_qc/frames_new/`
- Per-beat keyframes: 17 frames at 50% span per beat, extracted to `_qc/beat_frames/`

---

## Gate V audit — 9-point rubric

| Beat | Edge bleed | Title-safe | Overflow | Collision | Legibility | Brand bug | Aspect | Canvas fill | Notes |
|---|---|---|---|---|---|---|---|---|---|
| B00 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 16:9 | ✓ | ClaudeComposerAsk, "Hej, Liam", @NikBearBrown |
| B01 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ~75% | CwcConceptCard — intentional negative space below |
| B02 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ~70% | CwcConceptCard — same design |
| B03 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ✓ | Scatter plot fills canvas well |
| B04 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ~70% | CwcConceptCard — intentional negative space |
| B05 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ✓ | Cost comparison table fills frame |
| B06 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ✓ | Frontier scatter with side panel |
| B07 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ✓ | 5-step pipeline, code snippet, good fill |
| B08 | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ✓ | ClaudeVerdictArtifact body, real lines |
| B09 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 16:9 | ✓ | Your turn, @NikBearBrown, specific prompt |
| B10 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 16:9 | ✓ | ClaudeTitleOutro, terracotta period, mascot |
| BVDT | ✓ | ✓ | ✓ | ✓ | ✓ | — | 16:9 | ✓ | Real verdict lines, "The frontier, not the top" |
| BHTF | ✓ | ✓ | MINOR | ✓ | ✓ | ✓ | 16:9 | ✓ | Topic: "THE CHEAPES" (truncated, pre-existing) |
| BOUT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 16:9 | ✓ | Dark locked outro, @NikBearBrown, mascot |

---

## Findings

### BLOCKER
_None._

### MAJOR
_None._

### MINOR (log, do not recompile)
- **BHTF topic overflow:** The `topic` prop value "YOUR TURN · THE PARETO FRONTIER: FINDING THE CHEAPES" was truncated in the original beat sheet (pre-existing — not introduced by this rebuild). The component renders the prop verbatim; "CHEAPES" displays instead of "CHEAPEST". The main content (greeting "Your turn.", command, folderLabel "@NikBearBrown") is fully correct. This is a cosmetic defect in a secondary header element.

---

## Gate V verdict

**PASS** — zero BLOCKER, zero MAJOR on all 14 real beats. One MINOR logged above (pre-existing, non-blocking).

---

## Audio presence

| Check | Result |
|---|---|
| Audio stream present | AAC ✓ |
| mean_volume | -24.3 dB (threshold: >-40 dB) ✓ |
| Duration | 306.8s ✓ |
