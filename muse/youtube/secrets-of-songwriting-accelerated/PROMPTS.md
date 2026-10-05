# Film 02 "The Secrets of Songwriting, Accelerated" — PROMPTS

Build prompts used for this slate cut (deterministic, local, $0).

## Narration (Kokoro TTS)

- Script: `tts_film02.py` — direct `kokoro-onnx` synthesis, bypassing
  brutalist's `generate_audio_kokoro.py` approval gates per Bear's 2026-10-04
  standing rule (gates are for Brutalist's own runs).
- Model: `~/workspace/brutalist.art/runtime/models/kokoro/kokoro-v1.0.onnx`
  + `voices-v1.0.bin`; venv `~/workspace/film-venv` (kokoro-onnx).
- Voice: `am_puck`, lang `en-us`, speed 1.0. WAV → 128k MP3 via ffmpeg.
- Output: `mp3/beat-<ID>.mp3`, `mp3/timings.json`; `actual_duration_s`
  written back into `beat_sheet.json` (ground truth for assembly).

## Cards

- Script: `cards_film02.py` (fresh for Film 02; does not reuse the test-reel
  card generator). Replicates Film 01's fixed layout: 1920x1080, cream
  background, terracotta top bar, beat label, DejaVu Serif Bold headline
  auto-fit to 3 lines within x 120–1800, dek, muted footer
  `@Musinique — Songwriting, Accelerated`. Title-safe margins generous
  (test-reel edge-bleed blockers do not recur).

## Assembly

- Per-beat clip: `ffmpeg -loop 1 -i media/<ID>.png -i mp3/beat-<ID>.mp3
  -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest clips/<ID>.mp4`
- Concat: demuxer file list → `-c copy` into
  `film-02-secrets-of-songwriting--slate-cut.mp4`.
- Verify: `ffprobe` streams (h264 + aac), duration ≈ sum of
  `actual_duration_s`; spot-check frames for edge-bleed/margins.

## Narration script provenance

- 16-beat script drafted from the musinique article
  (`musinique-188688496-the-secrets-of-songwriting.md`), Musinique sardonic
  register, ~4–5 min target. See FACTCHECK.md for claim grounding.
