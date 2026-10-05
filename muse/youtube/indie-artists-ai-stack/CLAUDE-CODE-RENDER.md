# CLAUDE-CODE-RENDER.md — Film 12: "Muse vs Codex vs Gemini: The Indie Artist's Stack"

**Status:** SLATE CUT RENDERED 2026-10-05. This prompt reproduces the build.
**Source articles:**
`articles/musinique-194260243-the-same-tools-pointed-differently.md`
("The Same Tools, Pointed Differently," 2026-04-16) and
`articles/musinique-193817272-the-musinique-article-drafting-workflow-from-raw-artist-data-to-published-substack.md`
**Slate:** `muse/README.md` film #12 — the last film of the slate.

## Film facts (do not invent more)

- 16 beats: BIDEA, BDEFS, B01–B13, BOUT. Total narration ~256s (~4m16s).
- Channel `@Musinique` · Persona `claude-musinique` ("Musinique," Sardonic register)
- Voice: Kokoro `am_puck` at speed 1.0 · Audience: indie musicians
- Narration text per beat: `beat_sheet.json`
- Every factual claim verified in `FACTCHECK.md`. No single article compares
  these tools — the comparison frame comes from the mission brief (Muse,
  Codex, Claude Code, Claude Cowork, Gemini) and the article's thesis that
  tools are neutral and intent decides. Tool descriptions are structural
  (talker / coder / fetcher): no pricing, version numbers, or feature-matrix
  claims — they rot within a quarter, and the film says so itself. If a
  visual fix tempts you to add a new claim, don't — fix the visual, not the
  script.

## Reproduce the slate cut

On a machine with the brutalist.art toolkit and Kokoro models:

1. Sanity check: `beat_sheet.json` parses, 16 beats, every beat has
   `narration_text`, `shot`, and `audio_file`.
2. Narration: Kokoro TTS voice `am_puck`, speed 1.0, one MP3 per beat →
   `mp3/beat-<ID>.mp3` (git-ignored; renders never committed). Numbers as
   words, never raw glyphs ("Rule one", "fifty").
3. Cards: one 1920×1080 PNG per beat in `media/` — cream/terracotta/ink
   palette, `@Musinique` footer, beat label top-left. **Generous title-safe
   margins** (keep all text ≥120px inside every frame edge; content ≥55% of
   the safe area).
4. Per-beat clips: still card held for the beat's measured audio duration
   (use explicit `-t` from `timings.json`, NOT `-shortest` — that leaves dead
   air), then concatenated in beat order. Audio is the master clock.
5. Output: `film-12-ai-stack--slate-cut.mp4` (h264 + AAC).
   Verify with ffprobe: playable, duration ≈ sum of beat audio durations;
   verify MP3 astats show real speech, not silence.
6. Write `QC-SLATE-CUT.md` with the spot-check results.

**Never publish, upload, or stage anything.** MP3/MP4 stay local and go to
Bear's shared Drive folder only. Git holds source, beat sheets, prompts, and
QC paperwork — never renders.

## Standing rule (Bear, 2026-10-04)

Take every film all the way to a watchable slate cut without asking for
approvals. Brutalist's approval gates are for Brutalist's own runs. Bear
reviews the slate cut; that review IS the approval gate.
