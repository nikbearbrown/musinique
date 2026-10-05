# Film 09 "Your AI Manager" — slate-cut QC spot check

**Date:** 2026-10-05 ~00:10 EDT
**File:** `film-09-ai-manager--slate-cut.mp4`
**Result:** PASS (spot check, 7 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 291.59s (~4m52s), matches beat-sheet audio sum 291.47s (mux rounding)
- Video: h264 1920×1080 — Audio: AAC, no drift
- Size: 6,426,844 bytes (6.4 MB)

## Audio

- Real speech verified: beat-BIDEA peaks −1.0 dB, RMS −19.9 dB (healthy
  narration level)
- 16 beats, all Kokoro `am_puck`; numbers written as words per the Film 08
  nit (no raw digits in narration text)

## Frame inspection

Sampled at t=3, 40, 90, 150, 210, 270, 288s; visually inspected
t=3 (BIDEA), t=150 (B07), t=288 (BOUT):

- No edge-bleed: all text well inside frame edges (Film 08 title-safe
  margins replicated; test-reel QC blockers do not recur)
- Consistent branding: rust top bar, "@Musinique — Your AI Manager" footer,
  beat label top-left
- Headlines and deks legible, good title-safe margins

## Open items

- Drive upload + GitHub commit handled by the main agent (pre-authorized
  per standing rule; system approval card tap needed for Drive).
