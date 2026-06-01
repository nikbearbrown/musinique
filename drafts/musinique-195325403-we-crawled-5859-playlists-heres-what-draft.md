---
title: "We Crawled 5859 Playlists Heres What"
subtitle: ""
publication: "musinique"
book: "Musinique"
draft_status: "rewrite"
rewrite_voice: "Baldwin/Subby Substack essay"
source_article: "musinique-195325403-we-crawled-5859-playlists-heres-what.md"
source_file: "musinique-195325403-we-crawled-5859-playlists-heres-what.md"
post_id: "195325403.we-crawled-5859-playlists-heres-what"
post_date: ""
cover_image: ""
excerpt: "Most playlist advice is folklore. Submit to active playlists. Target curators in your genre. Aim for the sweet spot — not too mainstream, not too niche. This advice is not wrong exactly. But it is unexamined. Nobody has shown you the distribution. Nobody has shown you what “active” actually means when you put a number on it, or what “sweet spot” looks like..."
---
# We Crawled 5859 Playlists Heres What

_Draft rewrite for Musinique Substack._

Most playlist advice is folklore.

Submit to active playlists. Target curators in your genre. Aim for the sweet spot — not too mainstream, not too niche. This advice is not wrong exactly. But it is unexamined. Nobody has shown you the distribution. Nobody has shown you what “active” actually means when you put a number on it, or what “sweet spot” looks like when you plot 5,859 playlists and run a kernel density estimate across them.

We did. Here’s what we found.

---

## The Database

Musinique crawled 5,859 Spotify playlists maintained by 83 curators, capturing 16 fields per playlist: curator identity, playlist URL, follower count, track count, last updated date, genre tags, average artist popularity, average artist followers, genre diversity, and our proprietary Musinique Focus Score — a 0–100 measure of how genre-specific and curatorially intentional a playlist is.

Crawl date: December 21, 2025.

Everything that follows is derived from that snapshot. Every number is real. Every threshold has been tested against the data. Nothing here is a heuristic we inherited from someone else’s blog post.

---

## The First Surprise: Half the Corpus Is Dead

The single most powerful filter isn’t genre. It isn’t follower count. It’s time.

When we plotted playlist activity against crawl date, the distribution split cleanly into three populations:

A full 38% of playlists — 2,224 of 5,859 — hadn’t been updated in over a year. Some hadn’t been touched since 2013. These are not dormant playlists. They are dead ones. Pitching to them is not a long shot. It is a message sent to an address that no longer exists.

A further 13% sit in a grey zone — updated in the last year but not in the last six months. Reachable in theory. Worth deprioritizing in practice.

That leaves 48.9% — 2,865 playlists — updated within 180 days of our crawl. This is the active corpus. Everything else in our analysis runs on this subset.

The 180-day threshold isn’t arbitrary. We tested every threshold from 60 days to 365 days. At 60 days, you eliminate two thirds of the corpus and miss curators who update quarterly. At 365 days, you’re pitching to people who may have walked away from curation entirely. The 180-day line sits at a natural inflection point in the update frequency distribution — aggressive enough to cut the stale half, permissive enough to retain the active majority.

---

## The Second Surprise: The “Sweet Spot” Was Wrong

Every guide you’ve read about playlist targeting will tell you some version of the same thing: target playlists where the average artist has a Spotify Popularity Index around 20–60. Low enough that the curator isn’t gatekeeping for major label artists. High enough that the playlist has real listeners.

The logic is sound. The numbers are wrong.

When we ran a kernel density estimate across the 5,854 playlists with artist popularity data, the distribution peaked between 40 and 80. Only 1.6% of playlists had an average artist popularity below 20. The KDE found a single natural valley in the data — at 32.3, not 20. Below that valley is a thin left tail of genuinely obscure playlists. Above it is everything else.

The practical implication: the 20–60 band that’s been floating around as received wisdom has its lower bound 12 points below where the data actually breaks. It’s pulling in the dregs of the corpus and excluding the mainstream-indie window where most of the real placement opportunity lives.

We adjusted the band to 30–65. This is what the data supports.

---

## The Musinique Focus Score and What It Does (and Doesn’t) Predict

The Focus Score measures how consistently genre-specific a playlist is — a playlist that stays tightly within a single genre scores high, a broad mood playlist scores low. We designed it to identify curators who take their genre seriously.

What we did not design it to do — and what the data confirmed it cannot do — is predict whether a playlist falls in the 30–65 popularity window.

When we ran ROC analysis trying to derive a Focus Score cutoff that would predict artist popularity, the AUC came back at 0.405. Worse than random. High Focus Score playlists tend toward deeply niche curators whose artists score below 30 on Spotify’s popularity index. They’re not wrong — they’re just targeting a different artist tier.

This was clarifying rather than discouraging. It told us the Focus Score and the popularity window are measuring different things, which means they should be used as independent filters, not as proxies for each other. A playlist can have a high Focus Score and low artist popularity. A playlist can have a low Focus Score and mid-range artist popularity. What we want is both: genre coherence *and* the right artist tier.

We set the Focus Score floor at 35, tested sensitivity across 25–50 in 5-point increments, and found 35 sits at a natural elbow in the funnel — dropping to 30 adds 34% more playlists for a 5-point relaxation; tightening to 40 loses 26% with meaningful quality gain. The elbow is where you want to be.

---

## The Five Gates

Starting from 5,859 playlists, the full qualification funnel:

**Gate 1 — Activity (≤180 days):** 2,865 playlists survive. 2,994 eliminated. The single biggest cut in the funnel — time kills more pitching opportunities than any other factor.

**Gate 2 — Reachability:** Every active playlist in our database traces back to one of 83 catalogued curators, all of whom have verified contact methods. Zero eliminated here — but this gate matters architecturally. Contact data lives at the curator level, not the playlist level. The join required matching playlist to curator before any contact routing was possible, and that link was missing from the exported data until we traced it back to the raw crawl files.

**Gate 3 — Focus Score ≥35, Classical excluded:** 1,757 playlists survive. 1,108 eliminated. Classical playlists — 957 of them, 16% of the entire corpus — are set aside here not because they’re unworthy, but because they require a different analysis. More on that below.

**Gate 4 — Artist popularity 30–65:** 931 playlists survive. 826 eliminated. This is the KDE-validated indie-mainstream window: established enough to have a real Spotify presence, not so mainstream that curators are gatekeeping for labels.

**Gate 5 — Followers ≥500:** 202 playlists survive. 729 eliminated. Gate 4 had a median follower count of 3. Half the “viable” playlists had essentially no audience — private lists, test playlists, abandoned experiments. Gate 5 cuts the long tail and leaves a pool where P25 is ~1,000 followers and the median is 2,470.

**Final result: 202 mainstream viable targets across 36 curators.**

---

## The Classical Problem

Classical playlists deserve their own analysis, and they have one now.

The 957 classical playlists in our corpus have a different popularity distribution from the rest. Their KDE natural break sits at 60.1 — the mainstream classical world sits above that line, the niche/discovery classical world below it. Applying the 30–65 mainstream band to classical would simply capture both halves, which is not what we want.

We ran a separate classical funnel with adjusted thresholds — Focus Score ≥30 (relaxed because classical playlists score lower on our metric by structural design), artist popularity 5–40, followers ≥500. The result: 38 viable classical targets across 11 curators.

**Combined master list: 240 playlists, 39 curators.**

---

## Contact Routing: Not All “Reachable” Is Equal

The 83 curators in our database all have contact methods. But contact method is not a single thing. We parsed the enriched curator data into per-channel fields and found the following across the 240 viable targets:

98 playlists (41%) route to a direct submission form — the curator has explicitly built infrastructure to receive pitches. These are warm outreach targets. The friction is low, the intent is stated.

105 playlists (44%) route to YouTube as the best available channel — the curator has an active YouTube presence but no submission form.

16 playlists (7%) route to Instagram. 14 (6%) have no reachable channel beyond Spotify itself and are flagged for manual research before pitching.

A notable finding from the classical segment: 76% of classical viable targets have a submission form, compared to 34% in the mainstream pool. Classical curators are more likely to have built formal submission infrastructure — possibly because they manage higher inbound volume, or because the classical world has stronger norms around formal submissions.

---

## What the Regression Told Us About What We Don’t Control

We ran an OLS regression predicting average artist popularity from Focus Score, genre diversity, track count, days since update, and follower count across the full 5,859-playlist corpus.

R² = 0.096.

All five predictors are statistically significant. None of them matter much. Together they explain less than 10% of the variance in artist popularity across playlists. The rest — more than 90% — is determined by factors we cannot see in the metadata: editorial relationships, algorithmic boosting, the particular tastes of individual curators, the specific moment a playlist got picked up by Spotify’s recommendation engine.

This is not a failure of the model. It is an accurate description of the ecosystem. Playlist targeting is a probabilistic game played inside a system that rewards factors you cannot measure in advance. The qualification framework we’ve built doesn’t claim to predict placement outcomes. It claims to eliminate the targets that are definitely wrong — dead playlists, unreachable curators, genre mismatches, audiences too small to matter — and leave you with a pool where the probability of a meaningful outcome is no longer zero.

That’s a different claim, and it’s the honest one.

---

## The Cluster Structure

We ran k-means clustering on the full 7-feature dataset (Focus Score, artist popularity, followers, track count, days since update, genre diversity, artist followers) to see if the data separated into natural segments.

Silhouette scores across k=2 through k=7 ranged from 0.23 to 0.28. The data doesn’t cluster cleanly — it’s a continuum. This is what you’d expect from a real-world curator corpus without hard categorical boundaries.

What clustering did reveal, even with soft boundaries, was a useful split within the viable target pool:

**Focused/niche** (100 of 240 viable targets): High Focus Score (avg 73.2), higher average followers (15,608), but bimodal — many small playlists with a few very large ones. These are the genre specialists. They’re harder to pitch cold and less likely to have submission forms, but when they place you, the fit is tight and the audience is self-selected.

**Broad aggregators** (146 of 240): Lower Focus Score (avg 41.2), more consistent mid-range follower counts (median 3,619), and 73 of the 98 total Tier 1 submission-form targets. More accessible, more infrastructure, slightly less precise genre fit.

If you’re prioritizing volume and conversion rate, start with broad aggregator Tier 1 — 73 playlists, all with submission forms, median ~3,600 followers. If you’re prioritizing fit and long-term audience building, focused/niche playlists are the play.

---

## What This Is, and What It Isn’t

This is a qualification framework. It tells you which playlists are worth pitching to. It does not tell you whether your music will be placed, how long placement will take, or whether placement will produce meaningful streaming numbers. Those are legitimacy, matching, and ROI questions — separate research problems that require data we don’t yet have.

What we do have is a defensible, empirically grounded method for reducing 5,859 possibilities to 240 high-quality targets, with every elimination decision traceable to a specific, tested threshold.

The 240 are not guaranteed. They are simply not obviously wrong.

In an ecosystem where most pitching advice is speculation dressed up as strategy, that distinction is worth something.
