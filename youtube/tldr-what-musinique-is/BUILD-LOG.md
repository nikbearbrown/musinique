# BUILD-LOG — tldr-what-musinique-is

## Executive summary

*What Musinique Is* is a `tldr` film giving an overview of Musinique, built on 2026-09-23 at Bear's request: "a TLDR in colors and default voice giving an overview of what Musinique is". It uses the Claude colors (cream, warm ink, one terracotta accent), and Liam narrates, in for Bear, on Kokoro `am_onyx`. One indie artist's week after a finished song is the running case. The machine takes the chores and offers lyric drafts, which the artist sings, hears and refines into the final lyric. A playlist offer that a scanner calls clean is vetoed by a gate on the artist's own data, and the budget survives. The rule arrives last: the machine suggests, you decide, on your own data. Brand and copy go to Madison, video to brutalist.art.

**Every gate passes:** Gate F/L/A/W, Gate B, Gate V 0 defects, GATE T PASS, GATE BOOKEND PASS. **The master is cut. It has not been staged or published.**

**MASTER:** `exports/landscape/tldr-what-musinique-is.mp4`, 3840×2160, 24 fps, about 262 s (4:22). **Captions:** `tldr-what-musinique-is.srt`, full narration of full narration.

## Decisions

- **Honesty:** the toolkit is a plan (`musinique/SKILLS-BREAKDOWN.md`), so the film says "being built" and, in B18, "a plan today". The playlist numbers are the audit spec's worked example, captioned "example numbers".
- **Bear's rules:** no voice vendor is named anywhere; `make_sheet.py` asserts this over narration, card props and metadata. Every narration line and on-screen string is spell-checked against the system dictionary plus a names allow-list.
- **Greeting:** Namaste. Kokoro drops the final vowel of "Namaste", so the narration spells it "Namasté"; the card and captions spell it "Namaste".
- **Timing:** reveals are keyed to spoken phrases via `words.py` (faster-whisper) and `cues.py`, so a re-narration only needs `words.py` again.
- **GATE S:** section S1 of `../tldr-sections-skills-breakdown.md`, picked by Bear's request. S2 (the playlist audit) and S3 (artists as data) wait for a pick.

## Revision 2 (Bear, 2026-09-23)

Bear: "the machine should not write the lyrics... rather give possibilities and drafts and suggestions." Nine beats were re-narrated (B00, B02, B10, B11, B13, B14, B17, B18, BVDT). The lyrics job is now "Finish the lyrics", tagged "you finish". B11 ends on a draft → hear → refine loop. In B14 the lyrics sit on the decision side ("decision: your ear") beside the playlist ("decision: your data"), and the old single divider is retired. The B17 rule now reads "the machine suggests · you decide". All gates passed again on the re-cut.

## Gate history

- B02 audio was 8.0 s, under the hesitant writer's 9 s floor: one clause added, now 9.6 s.
- B14 narration said "two columns" while the picture sorts two groups: re-narrated as "two kinds".
- GATE F: the paperwork set (SHOTLIST, PROMPTS, README) was missing; added.
- Gate A: the title underline read `head.width`, which the stub geometry inflates; replaced with a measured constant. Gate A copies `scenes.py` alone into a temp dir, so the cue import now falls back to zero timings there.
- Gate V: B11 low contrast twice. First the faded job rows (removed), then the large ghost-filled profile card pulled the frame's ink average toward the page. The card is now an ink pull-quote rule.
- Contact sheet: "the machine" tags collided with the right-panel evidence, so the tag became "machine". The B17 rule collided with the budget label, so it moved down a line.
- Frames looked at: B00 late (all three lines), B02 late (correction on screen), B16 end (gate, skip, X), and the contact sheet.

## Open

- Bear's verdict on the cut, and human sign-off on FACTCHECK.md.
- GATE T advisory (does not block): B00 and B01 narration recite their cards.
- Staging only on Bear's word: `stage_publish.py` → `build_srt.py` → `art post`.
