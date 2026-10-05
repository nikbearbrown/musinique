# Film 02 "The Secrets of Songwriting, Accelerated" — slate-cut QC spot check

**Date:** 2026-10-04 ~20:45 EDT
**File:** `film-02-secrets-of-songwriting--slate-cut.mp4`
**Result:** PASS (spot check, 6 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 295.75s (~4m56s); beat-sheet audio sum 295.64s (Δ 0.11s, mux rounding)
- Video: h264 1920x1080 — Audio: aac, no drift
- Size: 6,598,846 bytes (6.6 MB)

## Audio

- `mp3/beat-BIDEA.mp3`: peak −0.07 dB, RMS −20.0 dB — real speech, healthy levels
- 16/16 per-beat MP3s present; `mp3/timings.json` written; `actual_duration_s`
  back-filled into `beat_sheet.json`

## Frame inspection

Sampled at t=5, 60, 120, 180, 240, 290s; visually inspected t=120 (B05),
t=290 (BOUT), plus card PNG for B02 (longest title):

- No edge-bleed: all text well inside frame edges (Film 01's fixed
  title-safe margins replicated; test-reel blockers do not recur)
- Consistent branding: terracotta top bar, `@Musinique — Songwriting,
  Accelerated` footer, beat label top-left
- Headlines/deks legible; longest title fits on one line within safe area

## Build notes

- First assembly used `-shortest` per clip → ~1.4s dead air per beat
  (total 314.7s vs 295.6s audio). Rebuilt with explicit `-t <beat duration>`
  from `timings.json`; final duration matches audio sum.
- TTS via direct kokoro-onnx (`tts_film02.py`), bypassing brutalist
  approval gates per the standing rule; cards via fresh `cards_film02.py`
  (not the test-reel generator).

## Open items

- None technical. Delivery (Drive upload / GitHub commit) is the main
  agent's job — not done by this build.
