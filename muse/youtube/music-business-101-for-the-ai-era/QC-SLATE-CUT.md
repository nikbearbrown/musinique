# Film 08 "Music Business 101 for the AI Era" — slate-cut QC spot check

**Date:** 2026-10-04 ~23:00 EDT
**File:** `film-08-music-business-101--slate-cut.mp4`
**Result:** PASS (spot check, 7 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 431.38s (~7m11s), matches beat-sheet audio sum 431.26s (mux rounding)
- Video: h264 1920×1080 — Audio: AAC, no drift
- Size: 9,698,093 bytes (9.7 MB)

## Audio

- Real speech verified: beat-BIDEA peaks −1.85 dB, RMS −20.3 dB (healthy
  narration level)
- 16 beats, all Kokoro `am_puck`

## Frame inspection

Sampled at t=5, 60, 120, 200, 300, 400, 425s; visually inspected
t=5 (BIDEA), t=200 (B06), t=400 (B13), t=425 (BOUT):

- No edge-bleed: all text well inside frame edges (test-reel QC blockers do
  not recur; Film 07 title-safe margins replicated)
- Consistent branding: rust top bar, "@Musinique — Music Business 101 for
  the AI Era" footer, beat label top-left
- Headlines and deks legible, good title-safe margins

## Open items

- Drive upload handled by the main agent (pre-authorized per standing rule;
  system approval card tap needed).
