# CLAUDE-CODE-RENDER.md — Film 01: "AI as Punk Rock: Your Taste Is the Instrument"

**Status:** SLATE CUT RENDERED 2026-10-04. This prompt reproduces the build.
**Source article:** `articles/musinique-187481091-ai-as-the-punk-rock-of-music-software.md`
**Slate:** `muse/README.md` film #1

## Film facts (do not invent more)

- 16 beats: BIDEA, BDEFS, B01–B13, BOUT. Total narration ~279s (~4m39s).
- Channel `@Musinique` · Persona `claude-musinique` ("Musinique," Sardonic register)
- Voice: Kokoro `am_puck` · Audience: indie musicians
- Narration text per beat: `beat_sheet.json`
- Every factual claim verified in `FACTCHECK.md`. If a visual fix tempts you
  to add a new claim, don't — fix the visual, not the script.

## Reproduce the slate cut

On a machine with the brutalist.art toolkit and Kokoro models:

1. Sanity check: `beat_sheet.json` parses, 16 beats, every beat has
   `narration_text`, `shot`, and `audio_file`.
2. Narration: Kokoro TTS voice `am_puck`, one MP3 per beat →
   `mp3/beat-<ID>.mp3` (git-ignored; renders never committed).
3. Cards: one 1920×1080 PNG per beat in `media/` — cream/terracotta/ink
   palette, `@Musinique` footer, beat label top-left. **Generous title-safe
   margins** (the test reel failed QC on edge-bleed; keep all text well
   inside the frame, content filling ≥55% of the safe area).
4. Per-beat clips: still card held for the beat's measured audio duration,
   then concatenated in beat order (audio-first conform — the audio track is
   the master clock).
5. Output: `film-01-ai-as-punk-rock--slate-cut.mp4` (h264 + AAC).
   Verify with ffprobe: playable, duration ≈ sum of beat audio durations.
6. Write `QC-SLATE-CUT.md` with the spot-check results.

**Never publish, upload, or stage anything.** MP3/MP4 stay local and go to
Bear's shared Drive folder only. Git holds source, beat sheets, prompts, and
QC paperwork — never renders.

## Standing rule (Bear, 2026-10-04)

Take every film all the way to a watchable slate cut without asking for
approvals. Brutalist's approval gates are for Brutalist's own runs. Bear
reviews the slate cut; that review IS the approval gate.
