# Musinique — the skills breakdown

*Planning document, 2026-09-22. Read before scaffolding anything in this folder.*

## Executive summary

Musinique is a free-by-default toolkit for independent musicians, built the way brutalist.art is built (one launcher, one `SKILL.md` per skill, tiers, phase gates, never publishes) and governed the way the reallocation engine and Madison are governed (verified data, provenance, gates that veto rather than vote, a run log). It does three jobs an indie artist actually has: **draft and prepare songs** (the machine offers lyric possibilities, drafts and suggestions; the artist sings, hears and refines them into the final lyric), **release them cleanly**, and **decide where promotion money should and should not go**. Branding and copy are delegated to Madison; video is delegated to brutalist.art. Musinique never re-implements either.

The nine prompt specs Bear pasted (Lyrical Literacy ×2, Aditi Banksy ×2, Forensic Playlist Audit, Unreal Reels, BRANDY, Nina, Hymn, Ogilvy, RESPell) collapse into **14 skills in four tiers**, plus a data layer the skills read from. The single most important design move: the ghost-artist constellation stops living as prose inside prompts and becomes **verified data** (`artists/<slug>/`), which every skill's artist modifier reads. The second: the playlist audit is the reallocation engine's exact analog and becomes the showcase recipe. The engine's value is in the applications it talks you out of; Musinique's value is in the promo dollars it talks you out of.

What this document decided: the skill list, the tiering, the folder layout, the two integration contracts (Madison, brutalist.art), what to carry from the pasted specs and what to fix, and a six-step build order. Bear has confirmed the launcher name, `./muse`. What is left to Bear: whether `spend-gate` stays a standalone skill. This empty `musinique/` folder is the toolkit root; the book stays in `musinique-bak/`.

---

## 1. What the three parents each contribute

| Parent | What Musinique inherits | What it must not do |
|---|---|---|
| **brutalist.art** (dot) | `./art`-style launcher · `skills/make/<skill>/SKILL.md` as doctrine · `TIERS.md` with a five-builder cap on the hand-out tier · `--silent` mode · free by default, paid steps ask per step · never publishes | Render video. Musinique writes briefs and prompts, then calls `$BRUTALIST_ART/art musinique-bookend` and `lyric-overlay`, which already exist. |
| **the reallocation engine** (Snickerdoodle) | `recipes/` = intent, `scripts/` = execution, `logs/RUN_LOG.md` = truth · `data/raw/` → `data/verified/` · gates are hard stops cleared by a named human · P9 executive summary on every human document · recipe lifecycle DRAFT → VERIFIED with cards · fixtures + a gate harness that proves gates veto | Invent a count, rate, or confidence. Every stream ratio, follower delta, or city flag traces to an SFA or DistroKid export in `data/`. |
| **Madison** | The Nina, Ogilvy, BRANDY and madison-pitch prompt suites already live in `madison/prompts/` · `brand/brand.yml` shape · the two-layer data architecture is already real there | Copy those suites. Musinique ships thin wrappers that add music-specific intake and touchpoint rows, then invoke Madison's prompts. |

Musinique becomes the **third Snickerdoodle domain** (after the reallocation engine and Madison). It copies `SNICKERDOODLE.md` verbatim and writes its own `DOMAIN.md` and `DATA_CONTRACT.md`.

---

## 2. The skills, in tiers

### ARTIST TIER — free, safe, hand out (five builders, deliberately)

| Skill | Use this when | Source spec | Kind |
|---|---|---|---|
| `song` | You want lyric drafts, options and suggestions to work from — never a finished lyric: a random song, poem, duet, bilingual song, folk adaptation, kids concept song, or a neuro-acoustic song (sleep · lullaby · birthday · grief · heritage · focus · protest) — any of them in a named artist's voice | Lyrical Literacy (the newer version, with `kids`) | prompt + rule files |
| `hymn` | You want the history, full text (extended to 5–7 stanzas), and respelling of any public-domain work | Hymn | prompt + one script (PD-year check) |
| `release` | You have a mastered track and need the whole DistroKid / Spotify / Apple / YouTube envelope: clean title, formatted lyrics, credits, artist link block, YouTube description | Lyrical Literacy `format` + title-cleaning rules + the existing `musinique-bak/distrokid/<slug>/` folders | recipe + script, GATE R |
| `playlist-audit` | A scanner says a playlist is clean and you want to know whether to submit, watch, or skip before spending | Forensic Playlist Audit | recipe + scripts + fixtures, gates |
| `copy` | You need a YouTube description, Reel caption, Substack teaser, artist bio, tagline, or web blurb in the artist's brand voice | Ogilvy (wrapper over `madison/prompts/ogilvy`) | thin wrapper |
| `artist` *(reference, not a builder)* | You want to see, add, or edit an artist profile; every other skill's artist modifier reads from here | Aditi Banksy profile + `riffs/` + `DistroKid.md` links | data + prompt |

### ADVANCED — Bear only

| Skill | Notes | Source spec |
|---|---|---|
| `artist-brand` | Music-specific intake → Nina `/n1`…`/n12` (archetype, personas, brief, voice, palette, logo prompts). Emits `artists/<slug>/brand.yml` in Madison's `brand.yml` shape. | Nina (wrapper over `madison/prompts/nina`) |
| `brandy` | Brand communications audit of an artist, the label, or a competitor. Adds the music touchpoint rows Madison's matrix lacks: Spotify for Artists profile, Apple Music, Bandcamp, SoundCloud, YouTube Music, HyperFollow, Genius, Songkick, Discord. `data` / `xls` / `memo` / `onepage` pass through. | BRANDY (wrapper over `madison/prompts/brandy`) |
| `unreal-reels` | Song or story → sequence-ID'd phone-footage prompts (`song`, `story`, `unreal`, `colorful`, `tiffany`, `tiktok`, `xmas`). Prompt generator only; every mode is a rule file. | Unreal Reels |
| `music-video` | The chain: `release` folder → `unreal-reels` prompts → optional AI video (per-beat approval, Higgsfield three-way contract inherited from brutalist.art) → `art musinique-bookend` → `art lyric-overlay`. Musinique owns the brief; brutalist.art owns every render. | new; composes existing skills |
| `spend-gate` | Before any paid promotion (SubmitHub, playlist pitching, ads, PR): a recipe whose only output is a logged go / no-go by a named human, with the `playlist-audit` verdict and the budget as inputs. The reallocation principle applied to money. | new |

### UTILITIES — invoked by other skills, rarely run directly

| Skill | Notes | Source spec |
|---|---|---|
| `format` | Raw lyrics → Spotify/Apple standard (sentence case, no labels, repeats written out, `!`/`?` only). Deterministic Python, with fixtures. | Lyrical Literacy `format` |
| `title` | Track-title cleaning to DistroKid rules. Returns only the title. Deterministic, with fixtures. | Track Title Cleaning Rules |
| `respell` | Anglicized phonetic respelling, 100% or `respell X` percent, stressed syllable in caps. Rule files + `respell.py`. `hymn` and `song` call it. | RESPell + the `respell` command in Lyrical Literacy |
| `meta` | Enrich lyrics with performance-focused Suno meta tags (never bare `[Verse]`). | Lyrical Literacy `meta` |
| `session` | Session Notes (key, tempo, form map, instrument lanes) + `style`, `remix`, `new song`, `status`. | Lyrical Literacy `session` |
| `visual` | `look` (Look.md → text-to-image styles), `style` (Style.md → full Midjourney prompt with parameters), `describe` (images → image-to-video prompts). | Lyrical Literacy `look` / `style` / `describe` |

### PAID — requires explicit spend approval, never a default

| Step | Where it appears | Note |
|---|---|---|
| AI music generation (Suno / Udio / Artlist `generate_music`) | after `song` + `session` | Ask, then spend. The lyric drafts and session notes are the free deliverable; the audio is the paid one. |
| AI video beats (Higgsfield) | inside `music-video` | Inherit brutalist.art's contract: CLI present + approved → clip; otherwise free path silently. |
| Midjourney stills | `visual`, `unreal-reels` | Prompts are free; generation is the artist's own account. |

**Why five builders on the hand-out tier.** Same reason brutalist.art caps it: a new artist's failure mode is not missing capability, it is fourteen commands and no idea which to open. `song`, `hymn`, `release`, `playlist-audit`, `copy` are the five things an indie artist does in a week.

---

## 3. The data layer — where the constellation goes

Today the ghost artists exist as: a table inside the Lyrical Literacy prompt, one long Aditi Banksy profile pasted twice, a links list in `riffs/DistroKid.md`, and per-artist `riffs/<slug>/README.md` stubs that mostly say "no additional notes." That is prose, not data. Every skill's artist modifier should read one place.

```
artists/
  _schema.md                  ← what a profile must contain; the Aditi Banksy profile is the exemplar
  aditi-banksy/
    profile.md                ← origin · vocal style · sound · lyrical themes · influences ·
                                 AI music generation reference prompt · DistroKid bio
    links.yml                 ← spotify, apple, subdomain, youtube, distrokid ids (from DistroKid.md)
    voice.yml                 ← registers, languages, BPM range, style tags, banned tags,
                                 the [Voice Tag] strings the song skill emits
    brand.yml                 ← written by artist-brand (Madison shape); absent until run
    look.md                   ← Midjourney style macros + srefs (optional)
  liam-bear-brown/ …
  mama-sparrow/               ← org: humanitarians-ai (the Lyrical Literacy personas are the
                                 same schema with an org field, not a second table)
  musinique/                  ← the label itself is an artist entry
```

Seed sources, in order: `riffs/*/README.md`, `riffs/DistroKid.md` (links), `musinique-bak/distrokid/DistroKid.md`, the pasted Aditi profile, the two constellation tables. Nothing is deleted; `riffs/` stays as provenance and gets a pointer.

**Unknown artist behavior** stays as specified: *"Artist '[name]' not found. Type `artist list` to see available modifiers."*

---

## 4. Folder layout

```
musinique/
  README.md · AGENTS.md · CLAUDE.md      ← AGENTS/CLAUDE generated from instructions/ (Madison pattern)
  SNICKERDOODLE.md · DOMAIN.md · DATA_CONTRACT.md · PROJECT_RULES.md
  muse                                   ← the launcher (decided)
  setup                                  ← dependency check (python, ffprobe, kokoro optional)
  skills/
    TIERS.md · SILENT-MODE.md
    make/<skill>/SKILL.md                ← the 14 skills above, one folder each
  artists/<slug>/                        ← §3
  rules/                                 ← the .md rule files the GPT specs referenced but never shipped
    style.md · songs.md · look.md · meta-tags.md
    sequence.md · unreal.md · colorful.md · tiffany.md · tiktok.md · xmas.md
    pronunciation.md · syllable-rules.md · custom-map.md
    neuro-acoustic.md                    ← the seven target profiles, one table
    formatting.md · title-cleaning.md
  recipes/                               ← intent (Snickerdoodle frontmatter, DRAFT to start)
    release.md · playlist-audit.md · spend-gate.md · music-video.md · artist-brand.md
    *.card.md                            ← the human cards
  scripts/
    format_lyrics.py · clean_title.py · respell.py
    playlist_ratio.py · geo_flag.py · decay_curve.py · playlist_gate_harness.py
    release_envelope.py · pd_year.py · conformance.mjs · to-markdown.mjs
    fixtures/                            ← every deterministic script has one
  prompts/
    deep-research/playlist-{1..5,synthesis}.md   ← the five Google Deep Research prompts, verbatim
  data/
    raw/                                 ← SFA exports, DistroKid earnings CSV — gitignored, private
    verified/                            ← validated, schema-checked copies
    examples/                            ← public fixtures (a synthetic SFA export, a bot-shaped playlist)
    reference/data-center-cities.yml     ← Ashburn VA, Council Bluffs IA, Dublin, Helsinki, Frankfurt, Singapore, Sydney …
  releases/<slug>/                       ← migrated from musinique-bak/distrokid/<slug>/
  logs/RUN_LOG.md · logs/gate-decisions/
  youtube/                               ← reels built BY brutalist.art land here per its post contract
```

---

## 5. Integration contract A — Madison (branding, marketing, copy)

Madison already holds `prompts/nina`, `prompts/ogilvy`, `prompts/brandy`, `prompts/madison-pitch`, plus `_shared/archetypes.md` and `_shared/readiness-score.md`. Musinique's `artist-brand`, `brandy`, and `copy` are wrappers:

1. **Intake is music-specific.** The wrapper replaces Nina's `/n1` questions and Ogilvy's brand-voice intake with the artist profile: `profile.md` + `voice.yml` answer most of the ten questions already. Nothing is asked twice.
2. **Touchpoints are music-specific.** `brandy` appends the streaming and live rows to Madison's matrix. Everything else (labels, memo, onepage, xls, forbidden phrases) passes through unchanged.
3. **Output lands in both trees.** `artist-brand` writes `artists/<slug>/brand.yml` in Madison's `brand/brand.yml` shape, so Madison recipes (consistency checker, launch handoff, performance reporting) can run on an artist without translation.
4. **The pasted specs are Madison's.** The Nina, Ogilvy and BRANDY text in Bear's paste is newer in places than what a `.build/` listing shows (e.g. Ogilvy's `/urso` already names "the Musinique Substack"; `/medhavy` and `/causal` are new). **Check on build:** diff the paste against `madison/prompts/{nina,ogilvy,brandy}` and land any newer version there, not here.

## 6. Integration contract B — brutalist.art (video)

Musinique never runs Remotion, Manim, or ffmpeg encodes. It produces briefs and calls the toolkit:

| Musinique step | brutalist.art skill it calls | What Musinique hands over |
|---|---|---|
| finished song video needs open/close | `musinique-bookend` | title, artist slug → the outro card's artist name + links come from `artists/<slug>/links.yml` (today they are hand-copied into every `youtube-description.md`) |
| karaoke cut | `lyric-overlay` | the video + `releases/<slug>/lyrics.txt` as the wording reference |
| explainer about a song, an artist, or the label | `ai-explainer` / `deep-explainer` | a beat-sheet brief; the film is built in brutalist.art's tree and posted through its `post` contract |
| commentary on a clip | `riff` | the clip |

The one-line rule for SKILL.md files: **"If it renders, it is brutalist.art's. If it decides what to render, it is Musinique's."**

---

## 7. What to carry from the pasted specs, and what to fix

Carry verbatim into rule files:

- Lyrics formatting rules, style guidelines (3 styles + 2 instruments, warm-up, preferred / alternate / banned), the seven neuro-acoustic profiles, the `kids` rules, the Session Notes template, the meta-tag guidance.
- The five playlist probes and the synthesis prompt, exactly as written, into `prompts/deep-research/`. The thresholds (stream:follower above 5:1 escalates; ±2 followers/day variance for 30 days; data-center city list; 24–48h cliff vs 14–28 day organic decay) go into `rules/` **labeled as heuristics**, since they are not sourced.
- Unreal Reels' sequence-ID scheme (A0…, B0…), the prompt formula, the "no engine language" rule.
- RESPell's session logic (`input:`, `respell X`, `status`, `reset`).
- The BRANDY artifact naming convention (`[command]_[brand]_[month]_[day]_[year]`), applied to every Musinique report.

Fix on the way in:

1. **Hymn's public-domain threshold is stale.** The spec says pre-1928. US public domain moves every January; in 2026 it is works published 1930 or earlier. `pd_year.py` computes it from the current year instead of hard-coding it, and the `history` output states the year it used.
2. **Two Lyrical Literacy versions were pasted.** The one with `kids` is the newer superset. The older "with Image Analysis" GPT adds nothing except a stray closing line; drop it.
3. **Aditi Banksy was pasted twice.** One `profile.md`. The second copy in the paste also ends with a truncated line ("She has not corrected any of them." without the last sentence); the first copy is complete.
4. **"Write to the artifact window" instructions** are GPT-era. In the CLI, output goes to a file in the working folder (a report, a lyrics file, a release envelope), and the launcher prints the path.
5. **"On first load run `list`"** becomes `./muse --list` and `./muse <skill> --help`, matching `./art`.
6. **Unsourced numbers in Ogilvy's `/cta`** (+161%, +202%, +332%) are Madison's problem, but Musinique's `copy` wrapper must not repeat them as facts. P3.
7. **RESPell's "next steps"** (PRONUNCIATION.md, SYLLABLE_RULES.md, CUSTOM_MAP.md, respell.py, side-by-side mode) are exactly the rule files and script in §4. They stop being a wish list.

---

## 8. Decisions made here, and the two left open

Made (revisit if wrong, but the build proceeds on these):

- `musinique/` (this folder) is the toolkit root. The book manuscript stays in `musinique-bak/`, the Suno book in `musinique-suno/`, the courses in `musinque-*-and-claude/` (that spelling is the real on-disk folder name, not a typo). Nothing is renamed or moved; the toolkit gets pointers.
- Third Snickerdoodle domain, generated `AGENTS.md`/`CLAUDE.md` from `instructions/`, conformance hook, no-delete rule. Same as Madison.
- Artist-tier cap is five builders. `artist` is a reference, not a sixth builder.
- All fourteen skills start as DRAFT recipes. Only the deterministic utilities (`format`, `title`, `respell`) and `playlist-audit`'s scripts get fixtures and a harness in the first pass, because those are the ones a machine can verify.
- Narration is Liam, in for Bear, on Kokoro `am_onyx`: free and local, the only voice.

Decided by Bear, 2026-09-23:

- **The machine never writes the final lyric.** `song`, `hymn` extensions and `meta` produce possibilities, drafts and suggestions. A lyric is finished only after a person has sung it, heard it and rewritten it, so every `song` output is labeled a draft, and no skill marks lyrics as final. The film *What Musinique Is* makes this its own beat.

Decided by Bear, 2026-09-22:

- **Launcher name is `./muse`.** Four letters, matches `./art`. Final.

Open for Bear:

1. **Whether `spend-gate` is its own skill or a gate inside `playlist-audit` and `release`.** Drafted as its own recipe so it can also gate ad spend and PR, which no other skill touches.

---

## 9. Build order

Each step is a full session of its own and leaves the tree runnable.

1. **Scaffold.** Launcher, `setup`, `TIERS.md`, `SNICKERDOODLE.md` (copied), `DOMAIN.md`, `DATA_CONTRACT.md`, `instructions/` → generated `AGENTS.md`/`CLAUDE.md`, `logs/RUN_LOG.md`. Migrate the constellation into `artists/` from `riffs/` and `DistroKid.md`. Write `rules/` from the pasted specs (§7).
2. **Deterministic utilities with tests.** `format_lyrics.py`, `clean_title.py`, `respell.py` + fixtures. These are the first VERIFIED recipes because a machine can prove them.
3. **`song` and `hymn`.** Rule-file driven, artist-modifier driven. `hymn` gets `pd_year.py`.
4. **`release`.** `release_envelope.py` builds the folder; migrate `musinique-bak/distrokid/<slug>/` into `releases/`; GATE R (human confirms metadata) logged. Artist link blocks now come from `links.yml`.
5. **`playlist-audit` + `spend-gate`.** Scripts, a synthetic bot-shaped fixture, a gate harness that proves a data-center city or a 24h cliff forces Skip regardless of scanner verdict (the exact shape of the reallocation engine's `gate-behavior` harness). This is the showcase; its card is the first one written.
6. **Bridges.** `copy`, `artist-brand`, `brandy` wrappers over Madison; `music-video` chain over brutalist.art; `unreal-reels` and `visual` rule files. Then an engineloop-style film about the toolkit, built in brutalist.art.

---

## 10. One-line description (for a directory listing)

Musinique is a free command-line toolkit for independent musicians: get lyric drafts and suggestions in a named artist's voice to refine by ear, prepare a release for DistroKid and the streaming platforms, and audit whether a playlist or a promo spend is worth it before paying, with every number traced to your own Spotify for Artists data. Branding and copy run through Madison; videos run through brutalist.art. Built for the Musinique label's ghost-artist constellation and for any indie artist who wants the same discipline.
