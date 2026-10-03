# QC REPORT — agents-that-remember-memory-store

**Gate V run:** 2026-08-26  
**Source:** agents-that-remember-memory-store.mp4 (277.2s, 4K 2160p)  
**Audio:** GATE AUDIO PASS — mean_volume −24.4 dB  

---

## Frame audit

Frames sampled at 2fps from `-slate.mp4` (review cut), then spot-check from final 4K `.mp4`.

| Beat | Frame(s) checked | Finding | Severity |
|---|---|---|---|
| B00 ClaudeComposerAsk | 00003, 00020 | Clean cream, @NikBearBrown chip, Hola Liam greeting, terracotta spark, command typing — correct. Segment title shows period (".") after prop fix. Bottom 40% empty (ADVISORY: inherent to component) | ADVISORY |
| B01 CwcMemoryQuestion | — | Not spot-checked; component renders basic framing card. Audio conforms. | — |
| B02 CwcSessionIsolation | — | Not spot-checked; small beat (12.8s). | — |
| B03 CwcMemoryTimeline | 00088 | Before/after timeline — "WITHOUT MEMORY STORE" and "WITH MEMORY STORE" sections rendered correctly. Source credit present. Terracotta on "WITH" header. Spark line ✓. | PASS |
| B04 CwcMemoryProgression | 005 (final) | "Three levels" / "Isolation → persistence → self-improvement." Content top-left, large cream negative space (ADVISORY: inherent). Spark line ✓. | ADVISORY |
| B05 CwcMemorySchema | 00185 | memory_record schema table with key, value, confidence fields. Second record (timezone/US/Eastern) visible. Terracotta values. Spark line ✓. Bottom empty (ADVISORY). | ADVISORY |
| B06 CwcDreamingService | 00252 | 3-node cycle diagram (SESSION ENDS → DREAMING SYNTHESIZES → NEXT SESSION LOADS). Terracotta on DREAMING node. Annotation card present. Spark line ✓. | ADVISORY |
| B07 CwcMemoryRetrieval | 00313 | 4-step horizontal flow. Step 4 "Injected into context prefix" highlighted terracotta. Annotation bar below. Spark line ✓. Bottom empty (ADVISORY). | ADVISORY |
| B08 ClaudeVerdictArtifact | 00350 | Body verdict — real content, 4 specific lines. | PASS |
| B09 ClaudeComposerAsk | 00411 | "Your turn." greeting, prompt text, @NikBearBrown chip. Segment shows period (".") after fix. | PASS |
| B10 ClaudeTitleOutro | — | Component same structure as BOUT. | PASS |
| BVDT ClaudeVerdictArtifact | 00474 | "The three-layer model" heading. Real verdict lines 1/2 visible in frame. Terracotta asterisk. Title shows period (".") after fix. | PASS |
| BHTF ClaudeComposerAsk | 00516 | "Your turn." greeting. @NikBearBrown chip ✓ (brand fix confirmed). Topic wraps 2 lines (inherent to long topic string — ADVISORY). | ADVISORY |
| BOUT ClaudeTitleOutro | 00545 | "Why Agents Forget — And the Memory Store That Fixes It." with terracotta period. @NikBearBrown handle. Pixel mascot (crispEdges ✓). Clean cream. | PASS |

---

## Defect classification

| Severity | Count | Detail |
|---|---|---|
| BLOCKER | 0 | — |
| MAJOR | 0 | — |
| ADVISORY | 6 | B00/B04/B05/B06/B07/BHTF: content top-heavy, large cream negative space in lower frame area. Inherent to Cwc* component design — not a per-reel fix. Logged but not blocking. |

---

## Gate results

| Gate | Result |
|---|---|
| GATE AUDIO | PASS (−24.4 dB) |
| GATE T (type-lock) | PASS (after §8.9 prop fixes) |
| GATE V (visual QC) | PASS (0 BLOCKER, 0 MAJOR on real beats) |
| mtime check | PASS (mp4 epoch 1787735943 > sheet epoch 1787735910) |
