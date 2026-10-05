# PROMPTS.md — Film 06: "A Visual Language for Pennies"

## Narration (Kokoro TTS)

- Engine: Kokoro ONNX (`kokoro-v1.0.onnx` + `voices-v1.0.bin`)
- Voice: `am_puck` — the `claude-musinique` channel voice
- Register: Musinique Sardonic — dry, contrarian, plain-spoken; wry but never
  smug. Write for the ear: short sentences, no parentheticals, no markdown in
  the spoken text. Midjourney flag syntax (`--profile`, `/tune`) is spoken as
  words ("profile flag", "tune command") — never read the raw glyphs aloud.
- One MP3 per beat: `mp3/beat-<ID>.mp3`. Measure each file's real duration
  (ffprobe) and write it into `beat_sheet.json` as `actual_duration_s` —
  the assembly conforms to these, not to estimates.

## Title cards (Pillow)

- 1920×1080 PNG per beat. Cream background `#f7f4ed`, rust top bar
  `#c05a32`, ink text `#2b2620`.
- Layout: beat label top-left, headline centered upper-third, dek below it,
  footer `@Musinique — A Visual Language for Pennies` bottom-center.
- **Title-safe margins (learned the hard way):** keep all text at least 120px
  inside every frame edge; body content should fill ≥55% of the safe area.
  The test reel failed visual QC on edge-bleed — do not repeat it.

## Assembly (ffmpeg)

- Per beat: loop the card PNG for `actual_duration_s`, pair with the beat
  MP3 → `clips/<ID>.mp4` (h264 + AAC). Use explicit `-t` from
  `mp3/timings.json` — NOT `-shortest`, which leaves dead air.
- Concat in beat order → `film-06-visual-language--slate-cut.mp4`.
- Verify: ffprobe shows h264 + AAC, playable, total duration ≈ Σ beat
  durations. Sample frames across the runtime for the QC spot check.
