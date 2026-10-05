# Film 03 "What AI Should Be Allowed to Touch" — PROMPTS

Build prompts used for this slate cut (deterministic, local, $0).

## Narration (Kokoro TTS)

- Script: `tts_film03.py` — direct `kokoro-onnx` synthesis, bypassing
  brutalist's `generate_audio_kokoro.py` approval gates per Bear's 2026-10-04
  standing rule (gates are for Brutalist's own runs).
- Model: `~/workspace/brutalist.art/runtime/models/kokoro/kokoro-v1.0.onnx`
  + `voices-v1.0.bin`; venv `~/workspace/film-venv` (kokoro-onnx).
- Voice: `am_puck`, lang `en-us`, speed 1.0. WAV → 128k MP3 via ffmpeg.
- Output: `mp3/beat-<ID>.mp3`, `mp3/timings.json`; `actual_duration_s`
  written back into `beat_sheet.json` (ground truth for assembly).

## Cards

- Script: `cards_film03.py` (fresh for Film 03; does not reuse the test-reel
  card generator). Replicates Films 01–02 fixed layout: 1920x1080, cream
  background, terracotta top bar, beat label, DejaVu Serif Bold headline
  auto-fit to 3 lines within x 120–1800, dek, muted footer
  `@Musinique — The Human Line`. Title-safe margins generous
  (test-reel edge-bleed blockers do not recur).

## Assembly

- Per-beat clip: `ffmpeg -loop 1 -framerate 30 -i media/<ID>.png
  -i mp3/beat-<ID>.mp3 -t <duration from timings.json>
  -c:v libx264 -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k clips/<ID>.mp4`
  (explicit `-t`, NOT `-shortest` — that leaves dead air)
- Concat: demuxer file list → `-c copy` into
  `film-03-what-ai-should-be-allowed-to-touch--slate-cut.mp4`.
- Verify: `ffprobe` streams (h264 + aac), duration ≈ sum of
  `actual_duration_s`; spot-check frames for edge-bleed/margins.

## Narration script provenance

- 16-beat script drafted from the musinique article
  (`musinique-188009916-when-the-spiritual-gets-stripped-...-what-ai-should-be-allowed-to-touch.md`),
  Musinique sardonic register, ~4–5 min target. The essay's first-person
  voice is translated to third-person narration; factual claims stay the
  article's. See FACTCHECK.md for claim grounding.
