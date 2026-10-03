# FACTCHECK — tldr-what-musinique-is

## Executive summary

This file checks every factual claim in *What Musinique Is* against its source. Every claim holds. Two kinds of claim needed care. First, the Musinique toolkit does not exist yet: it is a plan written on 2026-09-22, so the film says "being built" and "a plan today" and never implies it runs. Second, the playlist numbers are the audit plan's own worked example, not a real playlist, and they are captioned "example numbers" on screen. No voice vendor is named anywhere.

## Claims

| # | Claim (beat) | Verdict | Source or derivation | Fix |
|---|---|---|---|---|
| 1 | Musinique is an independent label (B00, BVDT) | holds | `riffs/musinique/README.md`: "a record label and publishing company"; releases distributed via DistroKid (`musinique-bak/distrokid/`) | — |
| 2 | A free toolkit **being built** for indie musicians (B00, BVDT, B18) | holds as stated | `musinique/SKILLS-BREAKDOWN.md` (plan, 2026-09-22, "nothing scaffolded yet"); free-by-default by design | Worded as a plan, never as a running product |
| 3 | The machine offers lyric drafts and suggestions in an artist's voice; a person sings, hears and rewrites them into the final lyric (B11, B14, B18) | holds as the plan's design, revised per Bear 2026-09-23 | SKILLS-BREAKDOWN §2 `song`, §3 `artists/<slug>/` | — |
| 4 | Aditi Banksy: post-punk spoken word, five languages (B11) | holds | Aditi Banksy profile: Hindi, French, Punjabi, English, Portuguese; post-punk / world spoken word | — |
| 5 | Mama Sparrow: close-miked lullabies, soprano (B11) | holds | Lyrical Literacy persona table: "Lullabies · close-miked soprano" | — |
| 6 | "A Freedom Riders Prayer" is the clean title (B12) | holds; the messy working title is **constructed** | Real Musinique release, `musinique-bak/distrokid/a-freedom-riders-prayer/`; title rules from the Track Title Cleaning spec (remove version IDs, year tags) | Captioned "constructed example" |
| 7 | "Chorus 2x" is written out in full (B12) | holds | Lyrics formatting rules: "write all repeated lines in full" | — |
| 8 | These rules are fixed, so a test can prove them (B12) | holds as the plan's design | SKILLS-BREAKDOWN §2 utilities `format`, `title`: deterministic, with fixtures | — |
| 9 | About a dozen followers, hundreds of streams a day, top city Ashburn (B15) | **example**, not a real playlist | Forensic Playlist Audit spec's worked example (12 followers, 400 streams/day, Ashburn VA) | Captioned "example numbers" |
| 10 | Ashburn is one of the world's biggest data-center hubs (B16) | holds | Loudoun County official site, "Data Centers: The Loudoun Story" (highest concentration of data centers anywhere); datacentermap.com lists 140 Ashburn facilities | — |
| 11 | A dozen followers rarely explain hundreds of plays a day (B16) | model judgment, worded as "rarely" | Audit spec: stream-to-follower above 5:1 warrants escalation (a heuristic, unsourced in the spec) | Hedged; no rate claimed as fact |
| 12 | In the plan, a data-center city is a gate that vetoes (B16) | holds as the plan's design | SKILLS-BREAKDOWN §9 step 5: the harness proves a data-center city forces Skip regardless of scanner verdict | Said "in the plan" |
| 13 | Brand and copy go to Madison; video goes to brutalist.art (B17, BVDT) | holds as the plan's design | SKILLS-BREAKDOWN §5, §6 | — |
| 14 | A distributor like DistroKid delivers songs to streaming platforms (B03) | holds | DistroKid's service | — |
| 15 | Spotify for Artists shows your streams, listeners and their cities (B03) | holds | Spotify for Artists audience tab (top cities) | — |

## Bear's rules

- **No voice-vendor mention:** `make_sheet.py` asserts that no narration, card prop or metadata field names a paid voice vendor. PASS.
- **No misspellings:** every narration line, card prop and on-screen Manim string is checked against `/usr/share/dict/words` plus a names allow-list. PASS. The narration spells the greeting "Namasté" so Kokoro says the final vowel; the card and the captions spell it "Namaste".
