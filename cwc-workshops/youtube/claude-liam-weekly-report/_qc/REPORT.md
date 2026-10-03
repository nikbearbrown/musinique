# QC REPORT — claude-liam-weekly-report
**Date:** 2026-08-26  **Run:** film-factory unattended

---

## Gate V — Frame Inspection

| Beat | Frame | Finding | Severity | Action |
|------|-------|---------|----------|--------|
| B00 | 50% | ClaudeComposerAsk: "Hola, Liam", "Opus 4.7", "@NikBearBrown", send button terracotta. Clean. | PASS | — |
| B01 | 50% | SkillTeardownAnatomy: SKILL.md listed in terracotta, callout box, sparkLine bottom-left. Content within safe area. Generous negative space (minimal skill = 1 file). | PASS | — |
| B02 | 50% | SkillTeardownPipeline: animated flow renders. Plato footerNote visible. Two terracotta elements (accent phase + output box border) — component design. | MAJOR | Component-level; not patchable via props. Log for next component pass. |
| B03 | 50% (post-fix) | SkillTeardownMechanism: body 7 words ✓, trigger phrases in monospace quote block, Popper verdictLabel chip, "The spec bites." sparkLine. One terracotta (spark). | PASS | — |
| BHTF | 50% | ClaudeComposerAsk: "Your turn.", repaired command readable, "Opus 4.7", one terracotta (send button). | PASS | — |
| BOUT | 50% | ClaudeTitleOutro: title restated, "@NikBearBrown", slug-seeded pixel-art mascot, no subline, dark background. Crisp pixel rendering. | PASS | — |

**BLOCKER defects: 0**
**MAJOR defects: 1** (B02 double terracotta — component design, not fixable via props)
**Gate V: PASS** (zero BLOCKER on real beats)

---

## Audio Presence
- Stream: AAC, 1 channel
- GATE AUDIO: PASS (mean_volume −23.8 dB, well above −40 dB floor)

---

## Build Counter
`VIDEO: 6` — 0 slates, 0 punts
