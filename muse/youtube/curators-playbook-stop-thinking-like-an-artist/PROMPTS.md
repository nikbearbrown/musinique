# PROMPTS.md — Film 05: "The Curator's Playbook: Stop Thinking Like an Artist"

## Narration (Kokoro TTS)

- Engine: Kokoro ONNX (`kokoro-v1.0.onnx` + `voices-v1.0.bin`)
- Voice: `am_puck` — the `claude-musinique` channel voice
- Register: Musinique Sardonic — dry, contrarian, plain-spoken; wry but never
  smug. Write for the ear: short sentences, no parentheticals, no markdown in
  the spoken text. Numbers are spelled out where they'd be misread
  ("three point eight three", "twenty-five hundred").
- One MP3 per beat: `mp3/beat-<ID>.mp3`. Measure each file's real duration
  (ffprobe) and write it into `beat_sheet.json` as `actual_duration_s` —
  the assembly conforms to these, not to estimates.

## Title cards (Pillow)

- 1920×1080 PNG per beat. Cream background `#f7f4ed`, rust top bar
  `#c05a32`, ink text `#2b2620`.
- Layout: beat label top-left, headline centered upper-third, dek below it,
  footer `@Musinique — The Curator's Playbook` bottom-center.
- **Title-safe margins (learned the hard way):** keep all text at least 120px
  inside every frame edge; body content should fill ≥55% of the safe area.
  The test reel failed visual QC on edge-bleed — do not repeat it.

## Assembly (ffmpeg)

- Per beat: loop the card PNG for `actual_duration_s` (explicit `-t` from
  `mp3/timings.json`), pair with the beat MP3 → `clips/<ID>.mp4`
  (h264 + AAC, yuv420p, 30fps).
- Concat in beat order → `film-05-curators-playbook--slate-cut.mp4`.
- Verify: ffprobe shows h264 + AAC, playable, total duration ≈ Σ beat
  durations. Sample frames across the runtime for the QC spot check; verify
  one beat's audio is real speech (peaks/RMS), not silence.
