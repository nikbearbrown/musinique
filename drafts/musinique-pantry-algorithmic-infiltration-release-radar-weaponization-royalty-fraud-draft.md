---
title: "Algorithmic Infiltration: Release Radar Weaponization & Royalty Fraud"
subtitle: "A forensic economic analysis of how bad actors exploit Spotify's Release Radar notification system and distributor metadata vulnerabilities to hijack artist profiles and capture royalty payments. Documents the 2025–2026 wave of attribution fraud targeting jazz and legacy artists."
publication: "musinique"
book: "Musinique"
draft_status: "rewrite"
rewrite_voice: "Baldwin/Subby Substack essay"
source_article: "musinique-pantry-algorithmic-infiltration-release-radar-weaponization-royalty-fraud.md"
source_file: "musinique-pantry-algorithmic-infiltration-release-radar-weaponization-royalty-fraud.md"
post_id: ""
post_date: ""
cover_image: ""
excerpt: "══════════════════════════════════════════════ HEADER Forensic Report · Streaming Fraud · bearbrown.co Algorithmic Infiltration: The Systematic Weaponization of Release Radar A Forensic Economic Model of Royalty Fraud via Attribution Hijacking in the Spotify Distribution Pipeline, 2025–2026 Reporting Date: March 14, 2026 Coverage: 2024 – Q1 2026 Focus:..."
---
# Algorithmic Infiltration: Release Radar Weaponization & Royalty Fraud

_Draft rewrite for Musinique Substack._

══════════════════════════════════════════════ HEADER

Forensic Report

· Streaming Fraud · bearbrown.co

# Algorithmic Infiltration: The Systematic Weaponization of Release Radar

A Forensic Economic Model of Royalty Fraud via Attribution Hijacking in the Spotify Distribution Pipeline, 2025–2026

Reporting Date:

March 14, 2026

Coverage:

2024 – Q1 2026

Focus:

Distribution Pipeline · Artist URI Fraud

TABLE OF CONTENTS

Contents

1. [01Overview & Framing](#overview)
2. [02Metadata Ingestion Vulnerabilities](#metadata)
3. [03The Release Radar Trigger Mechanism](#trigger)
4. [04The Confusion Window](#confusion)
5. [05The 1,000-Stream Arbitrage](#threshold)
6. [06Per-Stream ROI Math](#math)
7. [07Takedown Asymmetry](#takedown)
8. [08Case Documentation 2025–2026](#cases)
9. [09Distributor Accountability](#distributors)
10. [10Regulatory Outlook](#regulatory)
11. [11Platform Incentive Misalignment](#incentive)
12. [12Conclusions & Recommendations](#conclusions)
13. [13Works Cited](#references)

══════════════════════════════════════════════ BODY

── 01 OVERVIEW ──

01 · Overview & Framing

The digital music ecosystem in 2025 and 2026 has been defined by the emergence of a highly specific, technologically enabled form of intellectual property exploitation: **Release Radar weaponization.** This mechanism represents a fundamental shift from primitive streaming fraud—which historically relied on low-quality "click farms"—toward a sophisticated model of attribution hijacking.

By exploiting the technical architecture of the Spotify Artist URI mapping system and the automated notification logic of the Release Radar algorithm, bad actors have successfully bypassed traditional security gates to capture organic listener traffic. This report provides an exhaustive forensic analysis of the technical triggers, behavioral economics, and financial structures that allow this fraud to persist, documenting the systemic failure of verification in the global distribution pipeline.

Fraud Cycle Visual

The Release Radar Fraud Cycle — Six Stages

01

URI Claim

Scammer submits track claiming target artist's Spotify URI via distributor with no identity verification.

02

Profile Injection

Spotify ingests distributor delivery and populates track into the legitimate artist's discography.

03

Radar Trigger

Algorithm identifies a new release and automatically pushes notifications to all followers.

04

Confusion Window

Fans trust the brand, delay skipping, and cross the 30-second royalty trigger threshold.

05

Payout Accrual

Streams accumulate; track crosses 1,000-stream threshold; royalties enter the processing queue.

06

Collection & Exit

Payout cycles before removal. Track taken down 3–8 weeks later. Scammer repeats with a new profile.

── 02 METADATA ──

## 02 · The Technical Genesis of Profile Hijacking: Metadata Ingestion Vulnerabilities

The foundational vulnerability facilitating Release Radar weaponization lies not within Spotify's internal systems but at the point of ingestion — the "handshake" between third-party distributors and the platform's metadata database. Platforms like DistroKid and TuneCore operate as high-volume, self-service portals that prioritize *"frictionless"* uploads.

The critical security gap is the absence of a robust identity verification layer for URI mapping. Scammers do not need to "hack" an artist's Spotify account; they simply need to claim that their new track is a release by an established artist using that artist's publicly available URI. For many distributors, the verification for this claim is limited to a simple **Terms of Service checkbox.**

Once the distributor delivers the track with the targeted artist's metadata, Spotify's ingestion engine treats the distributor as a "preferred partner" and automatically populates the track into the discography of the verified artist profile. The 2026 rebrand of the "Verified Artist" blue checkmark to a "Registered Artist" label has not addressed the underlying vulnerability.

Distributor Verification Matrix — 2025–2026

| Distributor | URI Verification Method | Instant S4A Access | Identity Proofing | Fraud Risk |
| --- | --- | --- | --- | --- |
| DistroKid | ToS Agreement Checkbox | Yes (Special Access menu) | None | High |
| TuneCore | Metadata Match / Artist ID Field | Yes (Dashboard Link) | None (Rising Artist) | Moderate–High |
| CD Baby | Manual Review (Select Tiers) | No (Request-based) | None (Standard) | Moderate |
| Amuse | Automated Metadata Scan | Yes (Professional Tier) | None | Moderate–High |
| Too Lost | ToS Agreement | Yes (Label/Artist Portal) | None | High |

By placing a track on a profile with a high follower count, the scammer effectively **"inherits" the organic reach** of that artist without having to build an audience. This "Profile Injection" is the prerequisite for the entire fraud cycle.

── 03 TRIGGER ──

## 03 · The Trigger Mechanism: Release Radar and Notification Architecture

Once a track is successfully injected into an artist's profile, the Spotify algorithm identifies it as a new release. This status automatically triggers the **Release Radar notification system** — a personalized, algorithmically generated playlist delivered every Friday to every user who follows the targeted artist. Unlike editorial playlists (e.g., New Music Friday), which require human curation, Release Radar is fueled entirely by metadata and the follower relationship.

### The Technical Trigger Hierarchy

1. **Follower Relationship:** If a user follows Artist A, any new release with Artist A as a "Main Artist" or "Featured Artist" is eligible for that user's Release Radar.
2. **Pitching Status:** If the uploader pitches the track via Spotify for Artists at least 7 days before release, they can select a specific song for guaranteed inclusion.
3. **Metadata Finalization:** Once the distributor's ingestion is confirmed, the track is locked into the Release Radar cycle for the following Friday.

Scale of Delivery

For a mid-tier legacy artist with 15,000 to 30,000 followers, a single fraudulent upload generates **thousands of push notifications and email alerts** — all carrying the trust signal of an artist the recipient already follows.

Notification Type Comparison — Engagement & Fraud Utility (2025–2026)

| Notification Type | Estimated Open Rate | User Perception | Royalty Trigger Rate |
| --- | --- | --- | --- |
| Release Radar Push | High | High Trust (Existing Follow) | High |
| Release Radar Email | High | High Trust (Newsletter-style) | Moderate |
| Discover Weekly | Moderate | Exploration (Low Trust) | Low |
| Daily Mix / Radio | Low | Background (Passive) | Low |

This high engagement is the *"Passive Listener Capture"* phase of the fraud model. Listeners are served the track not because they searched for it, but because the platform's internal notification architecture actively pushes it to them as a trusted update from an artist they already enjoy.

── 04 CONFUSION WINDOW ──

## 04 · Listener Behavioral Economics: The "Confusion Window" and Skip Suppression

The financial viability of Release Radar weaponization depends entirely on the first 30 seconds of the listening experience. Spotify's royalty model dictates that a stream is only counted as payable once the listener crosses the **30-second threshold.** In standard fraudulent scenarios involving unknown artists, skip rates are extremely high because listeners quickly identify the content as irrelevant.

However, when the content is attributed to a known, respected artist, the **"Confusion Window"** takes effect — a documented psychological delay where a listener, encountering a stylistically anomalous track (e.g., an AI-generated country song on a bebop pianist's profile), does not immediately skip.

### Why Listeners Wait

Because of brand trust, listeners assume the artist is:

- Experimenting with a new genre or "artistic direction."
- Collaborating with a different type of musician.
- Releasing an archival "lost" recording with different production values.
- Updating their sound for a modern audience.

The Critical Bridge

Data suggests that for followed artists, listeners will often wait **35 to 45 seconds** before deciding they do not like the direction — comfortably past the 30-second royalty trigger. Familiarity suppresses the skip reflex precisely long enough to generate revenue.

The Confusion Window is not a design flaw. It is a consequence of the platform successfully building trust — and that trust is the attack surface.

── 05 THRESHOLD ──

## 05 · The 1,000-Stream Arbitrage: Royalty Thresholds as a Fraud Roadmap

In April 2024, Spotify implemented a minimum royalty threshold requiring each track to achieve at least **1,000 streams within a 12-month period** to be eligible for payments. While the stated rationale was to remove "non-music noise" and low-volume spam, the policy shift has inadvertently created a roadmap for sophisticated scammers.

By targeting established artist profiles with 10,000+ followers, bad actors can ensure that a single Release Radar push will carry a track over the 1,000-stream threshold in the first 24 to 48 hours of release. The royalty is paid per-stream for all streams once the threshold is crossed, meaning the 1,001st stream effectively "unlocks" the value of the previous 1,000.

Follower Tier vs. Fraud Efficiency

| Artist Follower Tier | Expected Radar Reach (Wk 1) | Probability of Crossing 1,000 | Estimated ROI Per Track |
| --- | --- | --- | --- |
| Micro (<5,000) | <500 streams | Low | Negative |
| Mid-Tier (5,000–20,000) | 1,000–5,000 streams | Moderate | Low–Moderate |
| Established (>20,000) | 5,000–30,000 streams | High | High |

The 1,000-stream rule has not eliminated fraud. It has merely shifted the strategy from low-volume "noise" tracks to high-volume "attribution" hijacking. Targeting a mid-tier jazz artist like Benny Green or Nat Adderley is infinitely more efficient than creating original content, as the pre-installed audience acts as a guaranteed monetization engine.

── 06 MATH ──

## 06 · The Math of Per-Stream Payouts and ROI

To calculate the economic return of a single fraudulent release, the following model applies. Let *R* be the total royalty, *S* be the number of streams, *p* be the average payout per stream, and *C* be the all-in cost of the release.

Royalty Capture Formula

R = S × p − C

C = (DistroKid annual fee) + (AI generation cost) + (time cost of URI research)

Where p ≈ $0.003 to $0.005 per stream (2025–2026 average).

DistroKid annual fee ≈ $22.99 (unlimited uploads).

AI generation cost ≈ $0 to $10 per track (Suno / Udio).

Time cost of URI research ≈ negligible (public data).

Single Hijacking — Example Calculation

For a single successful hijacking generating **10,000 streams** at an average of $0.004/stream:

      R = 10,000 × $0.004 − $33 ≈ **$7 net** per track, per operation. Across hundreds of simultaneously hijacked profiles — and with the $33 fixed cost shared across unlimited uploads — **monthly royalty capture can reach tens of thousands of dollars** before detection and removal.

The cost structure approaches near-zero marginal cost at industrial scale. Because DistroKid's "unlimited" plan charges a flat annual fee regardless of upload volume, each additional hijacked profile adds no incremental cost beyond the 10–15 minutes required to identify a target URI and submit a track.

── 07 TAKEDOWN ──

## 07 · The Takedown Asymmetry: Time-to-Removal vs. Payout Cycles

The *"Collection Window Exploitation"* relies on the delay between the reporting of fraudulent content and its actual removal. Documented cases from 2025 and 2026 reveal a significant "Takedown Gap." While automated spam filters can catch identical audio files, they frequently fail to identify stylistic mismatches or attribution fraud where the audio is unique (AI-generated) but the artist is fake.

The Temporal Alignment of Fraud and Payout

| Stage | Typical Timeline | Notes |
| --- | --- | --- |
| Track Upload & Release Radar Push | Day 0–7 | Immediate follower notification upon ingestion confirmation |
| Fan / Artist Discovery of Fraud | Day 7–21 | Fans usually discover via their own Release Radar or artist notifications |
| Reporting via S4A Support Portal | Day 14–28 | Artists must use the S4A portal; fans have no direct "report for fraud" button |
| Average Track Removal | Week 3–8 | Automated filters miss stylistic mismatches; attribution fraud requires manual review |
| Royalty Payout Processing | ~8-week delay | Spotify pays royalties on a two-month cycle — aligned with the removal window |

Perfect Temporal Alignment

By the time the track is removed (Week 8), the first wave of royalties from the first month of streams is already processing for payout. Scammers often time re-uploads to coincide with the beginning of a new month, maximizing their window before the next reporting cycle.

── 08 CASES ──

## 08 · Case Documentation: The 2025–2026 Wave

The following cases illustrate the systematic nature of this fraud. Targets are disproportionately drawn from jazz and legacy folk artists with high-authority brands but limited capacity for real-time digital estate monitoring.

Documented Incidents — 2025–2026

| Artist | Release / Incident | Discovery Date | Removal Delay | Est. Streams | Status |
| --- | --- | --- | --- | --- | --- |
| Emily Portman | Album: *Orca* (AI-generated) | July 2025 | 8 weeks | 10k–20k | Removed after 8-week appeal |
| Benny Green | Fake EP with Freddy Cole | Feb 2026 | 3 weeks | 5k–8k | Removed after fan outcry |
| Nat Adderley | Track: "Hippodelphia" | March 2026 | 4 weeks | 3k–5k | Metadata mismatch identified |
| Abbey Lincoln | March 2026 Wave | March 2026 | 2–4 weeks | 5k+ | Documented by Ted Gioia |
| Sophie | Suspect posthumous albums | Late 2025 | Ongoing | Unknown | Multiple flagged by Paul Bender |
| Johan Röhr | 2,700 songs / 656 aliases | Identified 2024 | N/A (internal) | 15 Billion | "Ghost artist" model via PFC initiative |

The Röhr Proof of Concept

The Johan Röhr case — technically "legal" within Spotify's Perfect Fit Content (PFC) initiative — served as the proof-of-concept for the fraud. Röhr generated significant revenue in 2022 by saturating instrumental playlists with alias-based content. Scammers simply upgraded this model by using the names of famous artists instead of invented ones, knowing that Release Radar would provide a more powerful distribution engine than any static playlist.

── 09 DISTRIBUTORS ──

## 09 · Distributor Accountability and Conflict of Interest

A critical component of the Release Radar weaponization loop is the distributor's role as a gatekeeper. The lack of verification for claiming a legacy Spotify Artist URI is exacerbated by the financial relationship between distributors and the platform.

Distributors benefit from high volume. While they may not take a commission on major DSP royalties, they charge annual subscription fees for "unlimited" uploads. In some cases, such as TuneCore's Social Platforms revenue, the distributor takes a commission on TikTok and YouTube Content ID revenue. This creates a nuanced conflict of interest: **distributors have a financial incentive to allow as much content as possible into the system,** as every new uploader is a paying customer.

### Risk Assessment by Platform

- High

DistroKid
The "Special Access" menu allows users to claim a Spotify for Artists profile nearly instantly once a track is in the system. The "unlimited" model makes it the preferred tool for industrial-scale scammers — zero marginal cost per fraudulent upload beyond the flat annual fee.
- Mod–Hi

TuneCore
Requires a Spotify Artist ID, but offers no secondary identity proofing for "Rising Artist" subscribers. The commission on social revenue creates a vested interest in volume regardless of content legitimacy.
- Moderate

CD Baby
More "legacy" in approach, often involving slower ingestion times which may allow for metadata mismatch detection. Still lacks a formal ID-at-upload requirement for URI mapping on standard tiers.

── 10 REGULATORY ──

## 10 · Legislative and Regulatory Outlook: ELVIS and NO FAKES

The rise of this fraud has prompted a pivot in the legal landscape toward **"Personality Rights"** rather than simple copyright enforcement. Traditional copyright protects the recording; the Release Radar scam exploits the identity of the artist.

### The ELVIS Act (Tennessee, 2024)

Effective July 1, 2024, Tennessee's Ensuring Likeness, Voice, and Image Security (ELVIS) Act was the first law to explicitly prohibit AI voice cloning and unauthorized digital replicas. It provides artists and their estates with a civil right of action against anyone who uses their voice to "mimic an artist's songs without authorization." This law is particularly relevant for the estates of jazz legends like Nat Adderley or Abbey Lincoln, who are disproportionately targeted by this fraud.

### The NO FAKES Act (Federal, 2025)

Reintroduced in April 2025, the NO FAKES Act aims to create a federal right to control one's voice and likeness. The 2025 version includes a **"notice-and-takedown" mechanism** that would require platforms like Spotify to remove unauthorized deepfakes and fraudulent attributions within **48 hours** of a valid report — a significant compression of the current 3–8 week removal window.

It also proposes strict liability for platforms "designed or promoted" to facilitate these replicas, which could eventually be used to force distributors to implement **KYC (Know Your Customer) protocols** for artist profile mapping.

Legislative Gap

Neither act directly mandates cryptographic signing of metadata at the distributor level — the precise point where the fraud originates. Legislative progress on voice rights does not close the Accountability Gap in the distribution pipeline.

── 11 INCENTIVE ──

## 11 · Platform Incentive Misalignment: The Pro-Rata Problem

A fundamental question in the 2026 fraud investigation is whether Spotify has a direct financial incentive to allow fraudulent streams to persist. Under the pro-rata model, the total royalty pool is a fixed percentage of total revenue. Fraudulent streams do not necessarily increase the total amount Spotify pays out; instead, they change *who* gets paid, diluting the per-stream value for legitimate artists.

However, there is a secondary incentive: **total platform engagement.** If a user receives a Release Radar notification for a "new" Benny Green track, they are more likely to open the app and listen to 30 seconds of music. Even if the track is fake, the 30 seconds of attention are "captured" by Spotify, contributing to churn reduction and active user metrics.

The Filter Limitation

While Spotify has committed to a "music spam filter" to detect mass uploads, these filters are currently more effective at catching botnets than at catching the "Confusion Window" behavior of real human followers — who listen voluntarily, making their engagement indistinguishable from legitimate streams.

── 12 CONCLUSIONS ──

## 12 · Conclusions and Systemic Recommendations

The weaponization of Release Radar is a byproduct of the music industry's rush to automate distribution at the expense of verification. The core of the issue is an **"Accountability Gap"** in the metadata pipeline. Until distributors are required to provide cryptographic proof of identity or estate authorization before mapping a track to a verified URI, the Release Radar system will continue to function as a delivery mechanism for fraud.

The 2025–2026 data indicates that scammers have moved past the "AI-generated spam" phase and into a **"Brand-Attribution Hijacking" phase.** This new phase is more damaging because it consumes the organic trust between artists and fans, turning a discovery tool into a vehicle for deception.

The economic model — built on near-zero marginal cost and 8-week takedown windows — is too lucrative to be stopped by simple ToS updates. It requires a fundamental re-engineering of the platform–distributor relationship.

### Required Systemic Changes

- 01

Mandatory 2FA for All URI Mappings
Any track claiming to belong to an existing Spotify Artist URI must be confirmed by the verified account holder via two-factor authentication before the distributor delivers the content to Spotify's ingestion pipeline.
- 02

Fingerprint-to-Artist Verification
Use AI tools not to create music, but to verify that a new upload stylistically matches the profile it is being mapped to before Release Radar notifications are sent. Flag high-divergence submissions for human review before publication.
- 03

Real-Time Estate Reporting
Provide authorized estates of deceased artists with immediate "Approval/Denial" rights for any track delivered to that artist's profile via a third-party distributor. Posthumous profiles are disproportionately targeted and have no living advocate to monitor them in real time.
- 04

Delay Release Radar Until Review Window
For tracks on profiles flagged as high-risk (legacy artists, deceased artists, artists with recent fraud reports), introduce a mandatory 48-hour review hold before Release Radar notifications are dispatched. This decouples the notification from the fraud cycle.

Without systemic change, the Confusion Window will continue to be a profitable collection window for bad actors, and the Release Radar algorithm will remain one of the most efficient — if inadvertent — fraud engines in the digital economy.

── 13 REFERENCES ──

## 13 · Works Cited

1. 1Doc Searls Weblog: This Tuesday [doc.searls.com](https://doc.searls.com/2026/03/10/this-tuesday/)
2. 2APAC Labels Assess Brand Risk as AI Music Clones Spread — Mission Media Asia [missionmedia.asia](https://missionmedia.asia/ai-music-fraud-apac-brand-risk-streaming-platforms/)
3. 3Mastering Spotify Release Radar 2026: Algorithm Hacks for Playlists — ArtisTrack [artistrack.com](https://artistrack.com/spotify-release-radar-2026-strategy/)
4. 4Everything Spotify — DistroKid Help Center [support.distrokid.com](https://support.distrokid.com/hc/en-us/sections/1500000533001-Everything-Spotify)
5. 5Optimizing Your Spotify Footprint: Claiming Your Artist Page — SubmitLink [submitlink.io](https://www.submitlink.io/post/optimizing-your-spotify-footprint-a-guide-to-claiming-your-artist-page)
6. 6Collaborations don't work: Rant + Question — Reddit / DistroKidHelpDesk [reddit.com](https://www.reddit.com/r/DistroKidHelpDesk/comments/1cmbhb3/collaborations_dont_work_rant_question/)
7. 7Instant Spotify for Artists registration — DistroKid [distrokid.com](https://distrokid.com/spotify/)
8. 8Getting music on Release Radar — Spotify Support [support.spotify.com](https://support.spotify.com/us/artists/article/getting-music-on-release-radar/)
9. 9AI fakes flooding playlists — The Star (Malaysia) [thestar.com.my](https://www.thestar.com.my/news/focus/2025/12/25/ai-fakes-flooding-playlists)
10. 10"Is Spotify Enabling Massive Impersonation of Famous Jazz Artists?" — Reddit / r/Jazz [reddit.com/r/Jazz](https://www.reddit.com/r/Jazz/comments/1rpbpf9/is_spotify_enabling_massive_impersonation_of/)
11. 11Track monetization eligibility — Spotify Support [support.spotify.com](https://support.spotify.com/us/artists/article/track-monetization-eligibility/)
12. 12Spotify's 1000-Stream Rule Explained — CyberPR Music [cyberprmusic.com](https://cyberprmusic.com/spotify-royalty/)
13. 13How the Music Industry is Fighting the $2B Streaming Fraud Issue — Trolley [trolley.com](https://trolley.com/learning-center/music-streaming-fraud-challenges-solutions-industry-insights/)
14. 14Spotify Royalty Calculator — Unchained Music [unchainedmusic.io](https://www.unchainedmusic.io/blog-posts/spotify-royalty-calculator)
15. 15Top 7 DistroKid Alternatives for Independent Musicians in 2025 — Loop Fans [music.loop.fans](https://music.loop.fans/blog/sites-like-distrokid)
16. 16Royalty Source of the Week: Too Lost — Infinite Catalog [infinitecatalog.com](https://www.infinitecatalog.com/blog/royalty-source-of-the-week-too-lost)
17. 17Swedish composer becomes Spotify's most-famous musician you've never heard of — The Guardian [theguardian.com](https://www.theguardian.com/uk-news/2024/mar/19/swedish-composer-johan-rohr-becomes-spotifys-most-famous-musician-youve-never-heard-of)
18. 18Composer Behind 650 Spotify Fake Artists Revealed — iMusician [imusician.pro](https://imusician.pro/en/resources/blog/spotify-fake-artist-revealed)
19. 19Controversy over fake artists on Spotify — Wikipedia [wikipedia.org](https://en.wikipedia.org/wiki/Controversy_over_fake_artists_on_Spotify)
20. 20Why Tennessee's ELVIS Act Is the King of AI Protections — Vanderbilt University / JETLAW [vanderbilt.edu](https://www.vanderbilt.edu/jetlaw/wp-content/uploads/sites/356/2025/03/Fowler_FINAL.pdf)
21. 21Transcript: Senate Holds Hearing on AI Deepfakes and the NO FAKES Act — Tech Policy Press [techpolicy.press](https://www.techpolicy.press/transcript-senate-holds-hearing-on-ai-deepfakes-and-the-no-fakes-act/)
22. 22Innovation Law Insights 23 April 2025 — DLA Piper [dlapiper.com](https://www.dlapiper.com/en-qa/insights/publications/innovation-law-insights/2025/innovation-law-insights-23-aprile-2025)
23. 23Spotify Track Monetization FAQ — UnitedMasters [support.unitedmasters.com](https://support.unitedmasters.com/hc/en-us/articles/30011900581267-Spotify-Track-Monetization-FAQ)

══════════════════════════════════════════════ FOOTER

Built with

bearbrown.co

· AI tools for educators, creators & founders

---

## Research Addendum (2026-06-03)

**Research date:** 2026-06-03

**Topic tags:** spotify, industry

**Research notes:**
- Spotify-related claims should distinguish editorial pitching, algorithmic recommendation, playlist exposure, and paid/opt-in tools such as Discovery Mode. Treating them as one black box weakens the argument.
- Spotify defines artificial streaming around listening intent and manipulation, including bots/scripts and paid services that guarantee streams. For playlist-vetting pieces, the central test is whether listener behavior remains durable after exposure ends.
- Discovery Mode terms are useful because Spotify explicitly says the program does not guarantee placement, streams, new listeners, or followers. That caveat supports a careful distinction between influence, exposure, and outcome.
- Use current industry economics carefully: IFPI reports global recorded-music revenue growth and continued paid-streaming importance, while RIAA separates wholesale revenue, retail revenue, paid subscriptions, ad-supported streams, physical, sync, and downloads.
- Royalty arguments should separate sound recording royalties, composition/publishing royalties, performance royalties, distributor fees, label deals, and non-interactive digital performance royalties collected through SoundExchange in the United States.
- For pro-rata versus user-centric royalty discussions, name the allocation mechanism before judging fairness: the dispute is not only payout size, but whether attention from one listener subsidizes music that listener never heard.

**Sources to verify/use:**
- [Spotify for Artists: Artificial Streaming](https://artists.spotify.com/en/artificial-streaming)
- [Spotify support: third-party services that guarantee streams](https://support.spotify.com/is-en/artists/article/third-party-services-that-guarantee-streams/)
- [Spotify support: pitching music to playlist editors](https://support.spotify.com/to/artists/article/pitching-music-to-playlist-editors/)
- [Spotify for Artists: Discovery Mode support](https://support.spotify.com/na-en/artists/article/using-discovery-mode-in-spotify-for-artists/)
- [Spotify legal: Discovery Mode self-serve terms](https://www.spotify.com/us/legal/discovery-mode-selfserve/)
- [IFPI Global Music Report 2026 announcement](https://www.ifpi.org/global-music-report-2026-global-recorded-music-revenues-grow-6-4-as-record-companies-drive-innovation/)
- [RIAA 2025 Year-End Recorded Music Revenue Report](https://www.riaa.com/riaa-reports-us-recorded-music-annual-revenue-achieves-new-high-of-11-5-billion-in-2025/)
- [SoundExchange FAQ](https://www.soundexchange.com/frequently-asked-questions/)

