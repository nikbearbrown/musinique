# Film 10 "The Wizard Has a Balance Sheet" — slate-cut QC spot check

**Date:** 2026-10-05 ~00:40 EDT
**File:** `film-10-wizard-balance-sheet--slate-cut.mp4`
**Result:** PASS (spot check, 6 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 399.04s (~6m39s), matches beat-sheet audio sum 398.92s (mux rounding)
- Video: h264 1920×1080 — Audio: AAC, no drift
- Size: 9,098,205 bytes (9.1 MB)

## Audio

- Real speech verified: beat-BIDEA peaks −0.8 dB, RMS −20.1 dB (healthy
  narration level)
- 16 beats, all Kokoro `am_puck` at speed 1.2 (first pass at 1.0 ran 446.7s,
  over the ~4–6 min target; re-rendered at 1.2 → 398.9s)
- Numbers written as words per the Kokoro nit (no raw digits in narration text)

## Frame inspection

Sampled at t=3, 60, 150, 250, 330, 392s; visually inspected
t=150 (B05), t=330 (B11):

- No edge-bleed: all text well inside frame edges (Film 09 title-safe
  margins replicated; test-reel QC blockers do not recur)
- Consistent branding: rust top bar, "@Musinique — The Wizard Has a Balance
  Sheet" footer, beat label top-left
- Headlines and deks legible, good title-safe margins

## Open items

- Drive upload + GitHub commit handled by the main agent (pre-authorized
  per standing rule; system approval card tap needed for Drive).
