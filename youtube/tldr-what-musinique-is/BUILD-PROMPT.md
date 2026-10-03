# BUILD-PROMPT — tldr-what-musinique-is

**What this is.** A paste-ready rebuild of *What Musinique Is*, a `tldr` film giving an overview of Musinique: an independent label, and a free toolkit being built for indie musicians. Source: `musinique/SKILLS-BREAKDOWN.md`, section S1 of `../tldr-sections-skills-breakdown.md`.

**Why.** Bear asked on 2026-09-23 for a TL;DR in the Claude colors and the default voice. The lesson: the machine executes the chores, you decide on your own data, and a gate on your own evidence protects the budget from a playlist a scanner called clean.

**Rebuild (from `books/`).**

```bash
R=$PWD/musinique/youtube/tldr-what-musinique-is
python3 $R/make_sheet.py                                          # asserts: no voice vendor named, no misspellings
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam, Kokoro am_onyx
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
(cd $R && python3 words.py && python3 lock_audio.py)              # word timestamps → reveal times; durations; TL;DR cues
for S in B10_TheWeek B11_ArtistAsData B12_CleanTheRelease B13_DoItAllFaster B14_TwoKinds B15_Commit B16_TheGateVetoes B17_TheMiddle B18_SameWeekMoneyKept; do
  python3 brutalist.art/runtime/qc/manim_layout_audit.py $R/scenes.py --class $S --curve-strict; done
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 $R/build_srt.py --check
```

Then LOOK at the frames (`_qc/`, `qc-sheet.png`, B00 and B02 late, B16 end).

**Rules.** Liam in for Bear, Kokoro `am_onyx`; no voice vendor named anywhere. The toolkit is a plan: say "being built". Playlist numbers are captioned examples. OUTRO-LOCK.

**Stop line.** Cut the master and stop. Never stage or publish.
