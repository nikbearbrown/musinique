# QC REPORT — claude-liam-analyzing-financial-statements

**Run:** 2026-08-25  
**Cut:** claude-liam-analyzing-financial-statements-slate.mp4  
**Duration:** 89.9s  
**Frames sampled:** 21 (at 15/50/85% of each beat's span, 2fps grid)

---

## Gate V — 9-point rubric

| Check | Beat | Result | Notes |
|-------|------|--------|-------|
| Edge bleed / clipping | all | PASS | All text within safe margins |
| Title-safe margins | all | PASS | No elements crossing the 5% safe inset |
| Container overflow | all | PASS | No overflow observed |
| Collision | all | PASS | No text/element overlap |
| Offscreen anchors | all | PASS | No elements cut at edge |
| Legibility | all | PASS | All type reads at review size |
| Brand bug placement | B00, BHTF | PASS | @NikBearBrown in footer on ComposerAsk beats |
| Aspect ratio | all | PASS | 16:9 confirmed |
| Canvas fill | B01, B03 | ADVISORY | SkillTeardownAnatomy and SkillTeardownMechanism templates cluster content in upper 30–40% of frame; large dead space below. Template-level design — not fixable at props level in this pass. Logged for template review. |

**Zero BLOCKERS. Zero MAJORS on real beats. Two ADVISORY items (template canvas fill).**

---

## Beat-by-beat notes

| Beat | Pattern | Visual result |
|------|---------|---------------|
| B00 | ClaudeComposerAsk | "Hola, Liam" greeting, command, output lines rendering. Clean. |
| B01 | SkillTeardownAnatomy | File tree (calculate_ratios.py, interpret_ratios.py, SKILL.md) + callout. Content upper third. |
| B02 | SkillTeardownPipeline | 3-phase pipeline flow: YOUR REQUEST → Read SKILL.md → Execute → Return output → RESULT. Terracotta accent on phase 1. Good. |
| B03 | SkillTeardownMechanism | "The interesting constraint." heading + body text. Content upper quarter. |
| BVDT | ClaudeVerdictArtifact | Paginated artifact card (1/2). All 4 verdict lines visible and complete. No truncation visible. |
| BHTF | ClaudeComposerAsk | "Your turn." greeting. Full coherent prompt typed in. |
| BOUT | ClaudeTitleOutro | Title + terracotta period + @NikBearBrown + pixel-art mascot. No subline. Crisp pixel art. |

---

## Audio

GATE AUDIO: PASS — mean_volume −24.0 dB (threshold: −40 dB)

---

## Verdict

Gate V: **PASS** (no BLOCKER, no MAJOR). Advisory: template canvas fill on B01/B03.
