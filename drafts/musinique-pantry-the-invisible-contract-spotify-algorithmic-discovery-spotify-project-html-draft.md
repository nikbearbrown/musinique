---
title: "The Invisible Contract — Spotify Algorithmic Discovery"
subtitle: ""
publication: "musinique"
book: "Musinique"
draft_status: "rewrite"
rewrite_voice: "Baldwin/Subby Substack essay"
source_article: "musinique-pantry-the-invisible-contract-spotify-algorithmic-discovery-spotify-project-html.md"
source_file: "musinique-pantry-the-invisible-contract-spotify-algorithmic-discovery-spotify-project-html.md"
post_id: ""
post_date: ""
cover_image: ""
excerpt: "COVER 🎵 INFO 7375 — GENERATIVE AI FINAL PROJECT THE INVISIBLE CONTRACT Genre-Consistent Agentic Recommenders for Independent Musicians on Spotify How a two-week algorithmic window quietly decides whether an independent musician gets discovered — and what a multi-agent AI system can do about it. \"The algorithm wasn't unpredictable. It was doing exactly what..."
---
# The Invisible Contract — Spotify Algorithmic Discovery

_Draft rewrite for Musinique Substack._

COVER

🎵 INFO 7375 — GENERATIVE AI FINAL PROJECT

# THE INVISIBLE CONTRACT

Genre-Consistent Agentic Recommenders for Independent Musicians on Spotify

How a two-week algorithmic window quietly decides whether an independent
    musician gets discovered — and what a multi-agent AI system can do about it.

"The algorithm wasn't unpredictable. It was doing exactly what it was designed to do.
    The problem was the data you fed it."

INFO 7375 | Generative AI Final Project | Spring 2026

Northeastern University — Khoury College / College of Engineering

PIECE I: The Investigative Feature  | 
      PIECE II: The Conversational Explainer

TOC

### 📋 Contents

- [PIECE I — The Investigative Feature: *The Window That Closes*](#piece1)
- [The Gemini Test](#p1-gemini)  ·  [The Silent Failure](#p1-silent)  ·  [What the System Does](#p1-system)  ·  [The Ghost in the Machine](#p1-ghost)
- [PIECE II — The Conversational Explainer: *Why Does Spotify Keep Recommending Me to the Wrong People?*](#piece2)
- [The Gemini Test (Conversational)](#p2-gemini)  ·  [Ground Truth](#p2-ground)  ·  [Ethics Beat](#p2-ethics)  ·  [Forward-Looking Close](#p2-forward)

================================================

PIECE I: INVESTIGATIVE FEATURE

================================================

# PIECE I — THE INVESTIGATIVE FEATURE

The Atlantic — Essay / Longform Technology

## The Window That Closes

How a two-week math problem is quietly ending independent music careers — and what one AI system is trying to do about it

---

You released the song on a Friday. A playlist curator with 40,000 followers picked it up that weekend. The streams came in — real ones, visible ones, the kind you screenshot. For ten days you watched the numbers climb. Then they stopped. Discover Weekly never came. Your monthly listener count drifted back to where it started, maybe lower. You told yourself the algorithm was unpredictable. You moved on.

The algorithm was not unpredictable. You fed it the wrong data. And now the window is closed.

That window — the two to four weeks after a release when Spotify's recommendation engine is most actively learning what your music is and who it belongs to — is the most consequential moment in an independent artist's career. Get coherent listening data into that window and the algorithm begins routing your track toward more people who resemble your actual audience. The flywheel turns. Get incoherent data — listeners from four different genres who skip at varying rates — and the machine files your track as belonging nowhere. The routing stops. The damage is invisible in the stream count. It shows up, months later, in your stalled career.

This is not a metaphor. It is the mechanism. And most independent artists never see it coming.

📊 FIGURE 1 — THE CONTAMINATION WINDOW: TWO PATHS FROM THE SAME RELEASE DAY

```
PATH A — Genre-Coherent Placement
────────────────────────────────────────────────────────────────
  Day 1–7   │ Track placed on 5K-follower niche playlist
  Day 2–7   │ Save rate: 18%  ███████████████░░░░░░░░░░░░░░░░░░
  Week 2–3  │ Discover Weekly trial begins
  Week 3–4  │ Algorithmic routing activates → audience compounds
  Month 2   │ Monthly listeners: 8K → 20K (no additional pitches)

PATH B — Genre-Entropic Placement
────────────────────────────────────────────────────────────────
  Day 1–7   │ Track placed on 500K-follower mixed playlist
  Day 2–7   │ Save rate: 1.8%  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  Week 2–3  │ Algorithm registers: no coherent community
  Week 3–4  │ Discover Weekly: silent
  Month 2   │ Monthly listeners: unchanged. Window: closed.
```

A playlist with 5,000 followers and a 15% save rate is not a smaller version of a 500,000-follower playlist with a 2% save rate. It is a categorically different asset. One generates streams and contamination. The other generates streams and algorithmic momentum.

## The Gemini Test

Here is the problem with simply asking an AI tool to fix this. Open ChatGPT, or Gemini, or any general-purpose assistant, and ask it to find you the right playlist curators for your new track. What you get back is a list. Maybe a good one. The AI can read genre labels. It can search the web. It can name playlists that have the word "indie" in the title.

What it cannot do is read the behavioral fingerprint of a curator's audience — the save rates, the skip rates, the follower retention curve that tells you whether this playlist's listeners are a coherent taste community or a fragmented aggregate assembled through years of genre drift. What it cannot do is cross-reference your track's tempo, timbre, and harmonic density against the last fifty tracks a curator accepted, then model whether your placement would generate signal or noise. What it cannot do is protect the contamination window.

GENERIC AI

What you get

A list of playlists with the right genre label. Follower counts. Maybe recent activity.

What's missing:

Save rate history. Audience coherence. Bot detection. Sonic match depth.

THIS SYSTEM

What it adds

Behavioral fingerprint of the curator's audience. Track-level sonic cross-reference. Contamination risk score per curator.

The difference:

Reach vs. the right listeners. Not the same thing.

A general AI tool gives you reach. It cannot give you *the right listeners*. Those are not the same thing, and confusing them is how careers stall.

## The Silent Failure

⚠️ The Scenario That Separates Serious Builders from Optimists

Your agentic recommender identifies a playlist. The match looks clean on every surface metric — genre label, follower count, recent activity. The pitch goes out. The placement happens. Streams begin. The system appeared to work. The output looked professional. The damage was invisible until it was done.

Here is what happened: the curator, three years ago, ran a paid bot campaign to inflate their follower count. The "audience" is a fiction. The listeners who encounter your track arrive from nowhere and return to nowhere. The save rate collapses. The algorithm registers your track as music that no coherent community claims. The contamination window closes on bad data.

This is the silent failure: **high-confidence output, broken result.** Any honest system built in this space has to account for it. The system described here attempts to. Whether it succeeds is the right question to ask.

Silent Failure Rate

Defined as: placements that pass all surface-level match criteria but produce save rates below 5% — indicating audience incoherence that pre-placement analysis did not detect. The system monitors this metric per curator over time and degrades curator trust scores accordingly.

Contamination Cost

A track that fails its initial algorithmic trial due to poor placement fit may see its Discover Weekly potential stalled for the remainder of its release lifecycle. The window is two to four weeks. It does not reopen.

## What the System Actually Does

The project is a multi-agent AI system designed to do one thing precisely: match independent musicians to playlist curators whose audiences will generate coherent algorithmic data during the release window.

| Agent | Function | Key Output |
| --- | --- | --- |
| **Playlist Agent** | Analyzes track audio fingerprint — tempo, spectral texture, harmonic profile, timbral qualities | Sonic match score per curator |
| **Verification Agent** | Vets curator follower base for bot inflation signatures; checks acceptance rate integrity (5–20% = healthy) | Curator trust score + contamination risk flag |
| **Curator Agent** | Cross-references track against curator's last 50 accepted tracks; models placement fit | Ranked shortlist of coherent-audience curators |
| **Social Agent** | Crafts personalized pitch referencing specific similar tracks on the curator's list | Pitch draft with demonstrated genre fit evidence |
| **Monitoring Agent** | Tracks post-placement save rate, skip rate, and Discover Weekly inclusion signals | Silent failure detection; curator trust score update |

The logic is not "find a big playlist." The logic is "find the playlist whose audience will teach Spotify exactly who this music is for." A 5,000-follower playlist with a 15% save rate from a coherent taste community is not a smaller version of a 500,000-follower playlist with a 2% save rate. It is a categorically different asset.

## The Ghost in the Machine

There is a complication worth naming before any honest conclusion.

The platform this system is built to navigate has its own interests — and those interests are not always aligned with the musicians and curators who make the algorithm work. Spotify's ghost artist program fills mood-based editorial playlists with music licensed from production companies at reduced royalty rates. "Peaceful Piano." "Deep Focus." "Ambient Relaxation."

📈 Ghost Artist Scale — By the Numbers

| Metric | Value |
| --- | --- |
| Cumulative streams of a single ghost producer (Johan Röhr) | Over 15 billion |
| Fake artist names used by one composer | At least 656 aliases |
| AI-generated content share on Deezer | ~39% of daily intake (60,000 tracks/day) |
| Drop in algorithmic playlist engagement | 23% between 2023 and 2026 |

These are precisely the playlists where listener intent is most coherent, where algorithmic signals should be most powerful — and they are increasingly populated by fictitious artist profiles with no real-world presence and billions of accumulated streams.

This does not change the mechanism. Genre coherence still generates better outcomes than genre entropy for the artists who can achieve it. But the infrastructure being protected is being quietly harvested by the platform it runs on. The system described here cannot fix that. It can help independent artists navigate it more intelligently.

The algorithm has a question it asks about every track: not "is this good music?" — but "who saved this, and who else do they resemble?"

**The window is real. It opens for two weeks. Then it closes. The question is what kind of data you put inside it.**

✍️ Author's Reflection

The proposal's technical architecture — SAR workflow, BaRT system integration, SUTRA tokenomics — had to be compressed almost entirely into a single table. The AI draft leaned heavily on the SUTRA philosophical framework ("Noble Eightfold Digital Path") in ways that read as grandiose rather than grounded; I replaced that framing with the concrete mechanism of the contamination window, which carries the same stakes without requiring the reader to adopt a new vocabulary. The silent failure scenario the AI generated was plausible but didn't specify

why

the failure was invisible — I added the bot-inflated follower base as the specific mechanism, which is both accurate to the proposal and more alarming to a general reader.

================================================

PIECE II: CONVERSATIONAL EXPLAINER

================================================

# PIECE II — THE CONVERSATIONAL EXPLAINER

Wait But Why — Patient · Technically Honest · Genuinely Fun

## Why Does Spotify Keep Recommending Me to the Wrong People?

A conversation about the invisible math deciding whether independent musicians get discovered — or disappear

---

Wait — isn't Spotify's algorithm just... random? Or at least unpredictable?

No. That's the thing. The algorithm isn't being random. It's doing its job precisely. The problem is that the data it received about your music was incoherent — and it made a very confident, very accurate decision based on that incoherence.

Here's the core question this project raises: *Why do some independent artists go from 8 monthly listeners to 20,000 in thirty days without a label, a viral moment, or a promotional budget — and why do others release a song that gets real streams on a real playlist and then... nothing?*

The answer is not luck. It's data quality. And almost no one is helping independent artists manage it.

## The Gemini Test — Conversational Version

Okay but why can't I just ask ChatGPT or Gemini to find me good playlists?

Great. Open it right now. Ask it: `"Find me genre-coherent playlist curators for my atmospheric indie folk track with a BPM around 78."`

You'll get a list. Probably a fine one. But here's what you *won't* get:

- The save rate those curators have delivered for tracks in your sonic neighborhood over the last six months
- Their follower retention curve — whether their audience is a real, stable taste community or an inflated aggregate
- A flag saying "this curator bought bot followers in 2023 and their audience data is poisoned"
- A comparison of your track's harmonic texture against the last fifty tracks they accepted

💡 That's actually the moment where I go from skeptical to intrigued. So the problem isn't finding playlists — it's finding the

right listeners

?

Exactly. A general AI can read genre labels. It cannot read the behavioral fingerprint of a listener community. And behavioral fingerprint is the only thing Spotify's recommendation engine actually cares about. Reach and the right listeners are not the same thing.

MOMENT OF CONFUSION

Hold on — what does "behavioral fingerprint" actually mean?

Think of it this way. When 10,000 people who save Sufjan Stevens also save a track by some unknown artist, Spotify learns something precise: this unknown artist belongs in the same listening community as Sufjan Stevens. That inference — drawn entirely from *behavior*, not from audio analysis — is worth more to that unknown artist than any playlist pitch or press mention.

The algorithm doesn't hear music the way you do. It hears the pattern of everyone who's ever encountered it. Who saved it. Who skipped it. Who played it again at 2am. That pattern — the behavioral fingerprint — is the instruction it uses when building next Monday's Discover Weekly for 239 million users.

🧠 TL;DR — I'm getting lost. What does this system actually do?

Short version: it's a team of specialized AI agents that answers one question before your release window opens —

which curator's audience will teach Spotify's algorithm exactly who your music is for?

One agent reads your track's sonic fingerprint. One checks whether a curator's followers are a real community. One cross-references your music against what that curator has accepted before. One writes the pitch. They work in sequence. The goal isn't reach. It's signal quality.

## Ground Truth — What Does "Success" Actually Mean?

SKEPTICISM

You're making this up. How would you even know if it worked?

This is the part most AI projects gloss over. Here's the honest answer.

A perfect output from this system is *not* "you got placed on a playlist." That's a surface metric. A perfect output is: your track lands on a playlist whose listeners share enough taste DNA that a meaningful percentage of them save it. That save rate becomes the instruction Spotify uses when it builds next week's Discover Weekly.

| Ground Truth Metric | Target | What It Signals |
| --- | --- | --- |
| Save-to-listener ratio | > 30% | High-intent listeners — the algorithm treats these as "this person chose this track" |
| Skip rate (<30 seconds) | < 30% | Strong negative signal — too many early skips "poisons" the track's data profile |
| Discover Weekly inclusion | Within 3 weeks of release | The flywheel started — algorithm is routing track to non-followers |
| Curator acceptance rate | 5–20% (the picky ones) | Curators who reject most pitches have more coherent — and more valuable — audiences |

If the system places you on a 40,000-follower playlist and your save rate is 2%, it failed. Even if the stream count looked good. The ground truth is behavioral, not volumetric.

## The Ethics Beat

What about the ethics of all this? Aren't you just gaming the algorithm?

Yes and no. The system is designed to generate *honest signal* — real listeners with real taste, making real decisions. That's not gaming the algorithm. That's working with it the way it was designed to work.

### ⚖️ Ethical Infrastructure — What the System Does and Doesn't Do

- **Data sourcing:** Draws on public streaming metrics and SubmitHub analytics, not private platform data. No access to Spotify's internal systems.
- **No fabricated engagement:** The system identifies real, coherent curator audiences. It does not manufacture saves, streams, or follower counts.
- **Curator compensation model:** Inspired by the SUTRA framework — curators are compensated for detailed, honest feedback, not just placement. This keeps the human curation layer from becoming its own version of the ghost-artist problem.
- **The platform problem:** Spotify fills its highest-intent playlists with ghost artist content licensed cheaply, displacing the independent musicians whose work built those taste communities. This system helps artists navigate that landscape. It does not fix it.

💡 So you're honest about what the system can't do. That's actually more convincing than if you'd promised it solves everything.

That's the assignment. A system that names where it fails is more useful than one that pretends it doesn't.

## The Question This Project Opens

So where does this end up? What question does the project open — not close?

Here's the one the project can't answer yet:

As agentic AI handles more of the search-and-pitch workflow for more independent artists simultaneously, does the signal get cleaner — or does the coherence that makes the mechanism work get washed out when everyone is optimizing for it at scale?

If every independent artist is using the same intelligent system to find the same coherent curators, do those curators get overwhelmed? Does the "rejection integrity" that makes their playlists valuable collapse under the volume? Does genre coherence itself become a new form of noise?

The algorithm rewards artists who send it coherent data from real taste communities. But if every artist is using the same system to find the same curators — is coherence still coherence, or is it just the next thing to game?

📊 FIGURE 2 — THE SIGNAL LOOP: TWO PATHS FROM THE SAME STARTING POINT

```
THE FLYWHEEL PATH
───────────────────────────────────────────────────────────────────
Genre-Coherent Track
    ↓
Right Curator (5–20% acceptance rate · stable followers · no bot inflation)
    ↓
Coherent Listener Community Saves Track
    ↓
Algorithmic Anchor Set: "This track belongs to THIS taste community"
    ↓
Discover Weekly Routing → More listeners who resemble the savers
    ↓
Audience Compounds Without Additional Pitches
    ↓
Career momentum ████████████████████████████████████

THE STALL PATH
───────────────────────────────────────────────────────────────────
Genre-Entropic Track (or Coherent Track, Wrong Curator)
    ↓
Wrong Curator (high follower count · mixed audience · bot-inflated)
    ↓
Fragmented Listener Behavior: saves + skips from 4 different taste communities
    ↓
Data Confusion: Algorithm cannot build a coherent "lookalike" profile
    ↓
Discover Weekly: Silent
    ↓
Contamination Window Closes on Bad Data
    ↓
Career stalls ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

Both paths start with a real playlist placement. Both generate real streams. Only one of them starts the flywheel. The difference is not volume — it's the coherence of who was listening.

✍️ Author's Reflection

The hardest concept to translate was "collaborative filtering" — the AI's initial analogy compared it to a Venn diagram of friends' movie preferences, which was technically accurate but lost the

urgency

of the release window entirely. I replaced it with the behavioral fingerprint framing, which makes it feel like something actionable rather than something academic. The "Noble Eightfold Digital Path" analogy from the original proposal didn't survive contact with a general reader — I kept the ethics values it represented but dropped the framework, because in plain conversation it reads as ornamentation rather than explanation.

KEY CONCEPTS REFERENCE

# REFERENCE — KEY CONCEPTS

| Term | Plain-Language Definition | Why It Matters |
| --- | --- | --- |
| **Collaborative Filtering** | Spotify's method of predicting what you'll like based on the behavior of people with similar taste — not based on the music itself | The foundation of all algorithmic recommendation. Every strategic decision flows from this. |
| **Contamination Window** | The 2–4 week post-release period when early listening data disproportionately shapes the algorithm's permanent model of a track | Get the wrong listeners here and the damage may be irreversible within the track's lifecycle. |
| **Save Rate** | The percentage of listeners who save a track to their library after encountering it on a playlist | The primary signal of high-intent listening. >30% triggers Discover Weekly consideration. |
| **Focus Score** | A measure of genre entropy across a playlist's content — how stylistically consistent the tracks are | Distinguishes the coherent tastemaker (high score) from the aggregator and bot farm (low score). |
| **Ghost Artists** | Fictitious artist profiles — often with no real-world presence — used to populate mood-based editorial playlists with cheap-to-license content | Displace independent musicians from the highest-intent playlists; undermine discovery infrastructure. |
| **Silent Failure** | When a system produces output that looks professional and functional but is factually or structurally broken | In this system: a curator that passes all match criteria but has a bot-inflated, incoherent audience. |
| **Rejection Integrity** | The practice of curators accepting only 5–20% of submitted tracks, maintaining audience coherence | Curators with high rejection rates have more algorithmically valuable audiences than open-gate curators. |

**THE INVISIBLE CONTRACT — INFO 7375 FINAL PROJECT**

Generative AI for Business | Spring 2026

Northeastern University — Khoury College / College of Engineering

Submitted via Canvas as .md file or Substack URL per course requirements.

    AI tools used for first draft generation; all technical content verified against proposal and cited sources.

    Human judgment documented in reflections appended to each piece.

---

## Research Addendum (2026-06-03)

**Research date:** 2026-06-03

**Topic tags:** spotify, cognition

**Research notes:**
- Spotify-related claims should distinguish editorial pitching, algorithmic recommendation, playlist exposure, and paid/opt-in tools such as Discovery Mode. Treating them as one black box weakens the argument.
- Spotify defines artificial streaming around listening intent and manipulation, including bots/scripts and paid services that guarantee streams. For playlist-vetting pieces, the central test is whether listener behavior remains durable after exposure ends.
- Discovery Mode terms are useful because Spotify explicitly says the program does not guarantee placement, streams, new listeners, or followers. That caveat supports a careful distinction between influence, exposure, and outcome.
- Music-cognition pieces should avoid reducing music to brain trivia. The interesting point is how perception, expectation, memory, movement, emotion, and social context make sound meaningful.
- For music-as-medicine or music-and-memory claims, keep the clinical language cautious: distinguish anecdotal therapeutic power from controlled evidence, and name the mechanism being proposed.
- The listener is not a passive receiver. Anticipation, repetition, surprise, entrainment, and memory help explain why a simple musical event can feel larger than its acoustic facts.

**Sources to verify/use:**
- [Spotify for Artists: Artificial Streaming](https://artists.spotify.com/en/artificial-streaming)
- [Spotify support: third-party services that guarantee streams](https://support.spotify.com/is-en/artists/article/third-party-services-that-guarantee-streams/)
- [Spotify support: pitching music to playlist editors](https://support.spotify.com/to/artists/article/pitching-music-to-playlist-editors/)
- [Spotify for Artists: Discovery Mode support](https://support.spotify.com/na-en/artists/article/using-discovery-mode-in-spotify-for-artists/)
- [Spotify legal: Discovery Mode self-serve terms](https://www.spotify.com/us/legal/discovery-mode-selfserve/)
- [Oliver Sacks: Musicophilia](https://www.oliversacks.com/books-by-oliver-sacks/musicophilia/)
- [Britannica: Music](https://www.britannica.com/art/music)
- [Britannica: Musical notation](https://www.britannica.com/art/musical-notation)

