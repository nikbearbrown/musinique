# Film 03 "What AI Should Be Allowed to Touch" — slate-cut QC spot check

**Date:** 2026-10-04 ~21:30 EDT
**File:** `film-03-what-ai-should-touch--slate-cut.mp4`
**Result:** PASS (spot check, 5 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 341.13s (~5m41s); beat-sheet audio sum 341.02s (Δ 0.11s, mux rounding)
- Video: h264 1920x1080 — Audio: aac, no drift
- Size: 7,896,284 bytes (7.9 MB)

## Audio

- `mp3/beat-BIDEA.mp3`: peak ≈ −0.7 dB, RMS −20.4 dB — real speech, healthy levels
- 16/16 per-beat MP3s present; `mp3/timings.json` written; `actual_duration_s`
  back-filled into `beat_sheet.json`

## Frame inspection

Sampled at t=10, 100, 200, 300, 335s; visually inspected t=100 (B04),
t=300 (B13), plus card PNG for BOUT (longest title):

- No edge-bleed: all text well inside frame edges (Film 01's fixed
  title-safe margins replicated; test-reel blockers do not recur)
- Consistent branding: terracotta top bar, `@Musinique — The Human Line`
  footer, beat label top-left
- Headlines/deks legible; longest title fits within safe area

## Build notes

- Two agents worked this film concurrently (sibling wrote beat sheet +
  paperwork and ran TTS; this agent ran cards + assembly). Both assembly
  runs appended to the same `concat.txt` → first concat was 662.8s (every
  clip listed twice, order scrambled). Fixed by rewriting `concat.txt`
  with 16 entries in beat order and re-running the concat step only;
  clips were individually correct throughout.
- Assembly used explicit `-t <beat duration>` from `timings.json` from the
  start (the `-shortest` dead-air lesson from Film 02 applied).
- TTS via direct kokoro-onnx (`tts_film03.py`), bypassing brutalist
  approval gates per the standing rule; cards via fresh `cards_film03.py`
  (not the test-reel generator).

## Open items

- None technical. Delivery (Drive upload / GitHub commit) is the main
  agent's job — not done by this build.
