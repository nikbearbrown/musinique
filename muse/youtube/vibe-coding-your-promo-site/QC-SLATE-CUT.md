# Film 11 "Vibe-Coding Your Promo Site" — slate-cut QC spot check

**Date:** 2026-10-05 ~00:00 EDT
**File:** `film-11-vibe-coding--slate-cut.mp4`
**Result:** PASS (spot check, 6 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 245.21s (~4m05s), matches beat-sheet audio sum 245.10s (mux rounding)
- Video: h264 1920×1080 — Audio: AAC, no drift
- Size: 5,473,982 bytes (5.5 MB)

## Audio

- Real speech verified: beat-BIDEA peaks −0.4 dB, RMS −19.8 dB; beat-B09
  peaks −1.5 dB, RMS −20.2 dB; beat-BOUT peaks −0.6 dB, RMS −20.0 dB
  (healthy narration levels, not silence)
- 16 beats, all Kokoro `am_puck` at speed 1.2
- Numbers written as words per the Kokoro nit (no raw digits in narration
  text — verified by script before TTS)

## Frame inspection

Sampled at t=3, 40, 90, 140, 190, 240s; visually inspected
t=3 (BIDEA), t=90 (B04), t=140 (B07), t=240 (BOUT):

- No edge-bleed: all text well inside frame edges (Film 10 title-safe
  margins replicated; test-reel QC blockers do not recur)
- Consistent branding: rust top bar, "@Musinique — Vibe-Coding Your Promo
  Site" footer, beat label top-left
- Headlines and deks legible, good title-safe margins

## Open items

- Drive upload + GitHub commit handled by the main agent (pre-authorized
  per standing rule; system approval card tap needed for Drive).
