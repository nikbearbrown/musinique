# PROMPTS.md — Film 11: "Vibe-Coding Your Promo Site"

## Narration (Kokoro TTS)

- Engine: Kokoro ONNX (`kokoro-v1.0.onnx` + `voices-v1.0.bin`)
- Voice: `am_puck` — the `claude-musinique` channel voice, speed 1.2
- Register: Musinique Sardonic — dry, contrarian, plain-spoken; wry but never
  smug. Write for the ear: short sentences, no parentheticals, no markdown in
  the spoken text.
- **Kokoro nit:** numbers as words, never raw glyphs ("two and a half
  billion", "a hundred thousand", "twenty twenty-six"). No digits anywhere
  in narration text — verified by script before TTS.
- One MP3 per beat: `mp3/beat-<ID>.mp3`. Measure each file's real duration
  (ffprobe) and write it into `beat_sheet.json` as `actual_duration_s` —
  the assembly conforms to these, not to estimates. Verify astats show real
  speech (peaks well above silence), not placeholder audio.

## Title cards (Pillow)

- 1920×1080 PNG per beat. Cream background `#f7f4ed`, rust top bar
  `#c05a32`, ink text `#2b2620`.
- Layout: beat label top-left, headline centered upper-third, dek below it,
  footer `@Musinique — Vibe-Coding Your Promo Site` bottom-center.
- **Title-safe margins:** all text ≥120px inside every frame edge
  (safe box x 120..1800, y 150..950); body content ≥55% of the safe area.

## Assembly (ffmpeg)

- Per beat: loop the card PNG for `actual_duration_s` (explicit `-t` from
  `mp3/timings.json`, NOT `-shortest` — that leaves dead air), pair with the
  beat MP3 → `clips/<ID>.mp4` (h264 + AAC, 30fps, yuv420p).
- Concat in beat order → `film-11-vibe-coding--slate-cut.mp4` (stream copy).
- Verify: ffprobe shows h264 + AAC, playable, total duration ≈ Σ beat
  durations. Sample frames across the runtime for the QC spot check.
