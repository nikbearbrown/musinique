# Film 12 "Muse vs Codex vs Gemini: The Indie Artist's Stack" — slate-cut QC spot check

**Date:** 2026-10-05 ~00:45 EDT
**File:** `film-12-ai-stack--slate-cut.mp4`
**Result:** PASS (spot check, 5 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 255.87s (~4m16s), matches beat-sheet audio sum 255.76s (mux rounding)
- Video: h264 1920×1080 — Audio: AAC, no drift
- Size: 5,662,063 bytes (5.7 MB)

## Audio

- Real speech verified: beat-BIDEA peaks −2.4 dB, RMS −19.6 dB; beat-B07
  peaks +0.0 dB; beat-BOUT peaks +0.0 dB (healthy narration levels, not
  silence)
- 16 beats, all Kokoro `am_puck` at speed 1.0
- Numbers written as words per the Kokoro nit (no raw digits in narration
  text — asserted by script before TTS)
- Build note: first TTS pass at speed 1.2 totaled 226.57s, under the 4–6 min
  target; re-rendered at speed 1.0 for 255.76s.

## Frame inspection

Sampled at t=3, 60, 130, 200, 250s; visually inspected
t=60 (B02), t=200 (B11):

- No edge-bleed: all text well inside frame edges (Film 11 title-safe
  margins replicated; test-reel QC blockers do not recur)
- Consistent branding: rust top bar, "@Musinique — Muse vs Codex vs Gemini"
  footer, beat label top-left
- Headlines and deks legible, good title-safe margins

## Open items

- Drive upload + GitHub commit handled by the main agent (pre-authorized
  per standing rule; system approval card tap needed for Drive).
