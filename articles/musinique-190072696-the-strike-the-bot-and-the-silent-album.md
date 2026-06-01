---
title: "The Strike, the Bot, and the Silent Album"
subtitle: "Automated enforcement was designed to protect artists. It has become one of the primary mechanisms for taking their money."
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: "190072696.the-strike-the-bot-and-the-silent"
post_date: "2026-03-06T04:59:21.916Z"
is_published: "true"
source_zip: "Y0r_0oGOSoWMD3iEcEhVnA.zip"
source_html: "posts/190072696.the-strike-the-bot-and-the-silent.html"
source_file: "musinique-190072696-the-strike-the-bot-and-the-silent-album.md"
cover_image: "https://substack-post-media.s3.amazonaws.com/public/images/791e5610-5562-44b0-9774-0e262044e0af_1456x816.png"
---
![](https://substack-post-media.s3.amazonaws.com/public/images/791e5610-5562-44b0-9774-0e262044e0af_1456x816.png)

*This is the seventh installment of The Pre-Floor Period, a series on digital infrastructure and independent creators. Previous pieces: [The Score You Cannot See](https://open.substack.com/pub/nikbearbrown/p/the-score-you-cannot-see) · [The New Music Gatekeepers](https://open.substack.com/pub/musinique/p/the-new-music-gatekeepers) · [The Six-Second Audition](https://open.substack.com/pub/musinique/p/the-six-second-audition) · [The Total Artist Platform](https://open.substack.com/pub/musinique/p/the-total-artist-platform-spotify) · [The Invisible Contract](https://open.substack.com/pub/musinique/p/the-invisible-contract) · [SoundCloud for Artists](https://open.substack.com/pub/musinique/p/soundcloud-for-artists-the-architecture)*

---

In 2014, a Los Angeles funk band called Vulfpeck released an album called *Sleepify* on Spotify. It contained ten tracks of complete silence, each approximately thirty seconds long — just long enough to register as a stream. The band asked its fans to play the album on repeat while they slept. Within a month, *Sleepify* had generated approximately $20,000 in royalties, which Vulfpeck announced it would use to fund a free concert tour.

Spotify removed *Sleepify* after about a month.

The band kept the money.

The stunt was funny. What it revealed was not. The pro-rata royalty system — in which total platform revenue is divided proportionally by stream count — can be gamed by anyone who understands its logic. Vulfpeck demonstrated this as performance art. Michael Smith demonstrated it as federal fraud: in 2024 he was indicted for using AI to generate hundreds of thousands of tracks and 10,000 bot accounts to stream them billions of times, stealing over $10 million in royalties from the pool before federal investigators caught up with him.

Between the sleeping fans and the bot farms, legitimate independent artists are losing money they are owed — not to the fraudsters directly, but to the automated enforcement systems that cannot distinguish between a bot and a loyal listener, and that have been designed to protect institutional interests rather than artist equity.

## The Strike That Freezes the Money

SoundCloud’s two-strike copyright policy is a legal compliance requirement — the DMCA mandates that platforms have a repeat infringer policy, and two unresolved strikes triggering termination is a defensible implementation. The problem is what happens to accrued earnings when termination occurs.

When SoundCloud terminates an account for copyright infringement, it freezes the artist’s royalties — not temporarily, pending resolution, but indefinitely. Artists have documented thousands of dollars in legitimate earnings held based on invalid claims already dismissed by Spotify, Apple Music, and Amazon, while SoundCloud treats the frozen funds as a compliance matter it faces no financial consequence for leaving unresolved.

> This is not a bug. It is an incentive structure.

The platform holds the money. The artist needs the money. The platform bears no cost for delay. The artist bears the entire cost of waiting. The enforcement system has been designed, whether intentionally or by default, to produce exactly this outcome.

## The Bot That Set Up the Content ID

The fraud detection problem runs in the opposite direction with equal damage — and connects directly to the system’s most serious design flaw.

Spotify’s 2024 policy fining distributors $10 for every track with detected artificial streaming was designed to combat operations like Smith’s. The incentive it created in practice: distributors that preemptively remove music at the first anomaly, because the cost of a false negative (a Spotify fine) exceeds the cost of a false positive (a legitimate artist’s catalog wrongfully removed). Scammers add legitimate tracks to bot-heavy playlists to obscure the fraud pattern. When the algorithm detects the bot activity, the legitimate artist takes the penalty alongside the fraudster — permanent ban, royalties forfeited, no appeal mechanism operating at the speed the damage requires.

The bot penalty and the Content ID weaponization documented below are two versions of the same enforcement design failure: systems built to detect fraud that have no reliable mechanism for protecting the innocent artists caught in detection’s path.

## The Content ID System That Can Be Weaponized Against You

MediaMuv, a company that obtained access to YouTube’s Content Management System through AdRev, used that access to file copyright claims on music it did not own. This was not a technical error. It was a deliberate scheme: claim rights to someone else’s content, collect the monetization revenue their legitimate streams generate, and continue until an IRS investigation catches you. Before that investigation concluded, MediaMuv had stolen millions in royalties from artists whose music it had never had any rights to.

What the MediaMuv case demonstrates is that the automated identification systems distributors promote as protection mechanisms are accessible to any entity that can obtain the technical credentials to file a claim — and that detecting systematic fraud of this type requires an IRS investigation, not a platform review. The detection systems are not audited at the speed at which the fraud operates.

The conflict of interest in who owns these systems is structural. AdRev — the Content ID infrastructure through which independent artists’ YouTube monetization flows — is now owned by Universal Music Group, following the $775 million Downtown Music Holdings acquisition [documented in installment five](https://open.substack.com/pub/musinique/p/the-invisible-contract). A major label owns the infrastructure through which independent artists contest copyright claims and receive YouTube revenue. Whether that ownership has been exercised against independent artists is a question the platforms are not obligated to answer publicly. The structure of the conflict exists regardless of whether it has been exploited.

The series has documented a consistent pattern: the institutions that own the enforcement infrastructure have interests that diverge from the independent artists subject to that enforcement. MediaMuv is the case where that divergence became criminal. The structural condition that made it possible — access to enforcement infrastructure governed by the entities with the most to gain from its misuse — remains in place.

## The Union That Was Fired and Replaced With a Chatbot

Artists and industry observers have documented a significant reduction in DistroKid’s human support capacity following a reported unionization drive — a reduction the platform replaced with AI-driven systems. DistroKid has not publicly addressed the connection between the two events. What is documented is the outcome: artists who previously could reach a person to resolve release errors, metadata disputes, or distribution problems now consistently report interactions with automated systems that cannot exercise judgment, escalate edge cases, or take responsibility for outcomes.

The contrast with Symphonic, a mid-tier distributor that maintains human account management, is direct and frequently cited. The difference between a metadata error that gets resolved before a release window closes and one that derails a campaign is, in most cases, the difference between a human who can make a decision and an automated system that routes the problem through a queue until the window passes.

DistroKid’s choice is financially rational. Human support is expensive. AI support scales without proportional cost increase. An individual artist’s dispute is not a revenue driver — it is a cost center. Replacing it with automation that handles routine cases while leaving edge cases unresolved is, from the platform’s accounting perspective, a cost reduction.

From the artist’s perspective, the edge case is not an edge case. It is their release. The asymmetry between how the platform categorizes the problem and how the artist experiences it is the series’ central dynamic, made visible in miniature: a board-level decision to reduce support costs becomes a missed release window for an artist who has no other recourse.

## These Are Not Independent Red Flags. They Are a System.

Industry advocacy organization SoundGirls has documented a taxonomy of warning signs for predatory distribution and production agreements. Read individually, they describe bad actors. Read together, they describe a playbook.

The refusal to use written contracts eliminates the legal record that would allow an artist to challenge wrongful termination, royalty withholding, or content removal after the fact. The absence of documentation is not an oversight. It is structural protection for the platform.

The bait-and-switch — verbal promises that differ from the written Terms of Service — is the mechanism through which AI training clauses, geographic fee disparities, and subscription hostage dynamics become effective without the artist understanding what they agreed to. The verbal promise is the sale. The written ToS is the actual agreement.

The rushed signing produces the same result: an artist bound by terms they didn’t review, who discovers what they agreed to only after the cost of leaving exceeds the cost of staying. The product hostage — refusing to process a takedown request unless the artist agrees to new, unilateral terms — is the subscription model made explicit. Ditto Music’s reported ten-day downtime requirement before a distributor transfer can process is a variation on the same logic.

Each element reinforces the others. The absent contract removes the legal foundation for challenging any of them. The bait-and-switch establishes the terms the rushed signing prevents the artist from reviewing. The product hostage ensures that by the time the artist understands what they agreed to, exit is more expensive than staying.

This is not a collection of bad actors using a collection of bad tactics. It is a coordinated architecture of dependency, operating at scale, in the pre-floor period before the regulatory frameworks that might govern it have arrived.

## What Has Arrived Across Seven Installments

Across seven pieces, this series has documented algorithmic hiring scores that workers cannot see or contest, subscription architectures that hold catalogs hostage to monthly rent, AI training clauses embedded in ToS that most artists have already passively agreed to, royalty redistribution mechanisms that systematically transfer independent artist earnings to major labels, fraud detection systems that punish innocent artists for proximity to fraud, and support infrastructure deliberately reduced below the threshold required to resolve the disputes it generates.

The regulatory responses are real but inadequate. The FCRA litigation against Eightfold AI, New York City’s Local Law 144 for algorithmic hiring tools, the MLC’s lawsuit against Spotify’s royalty reclassification — dismissed. The FTC has the precedent and authority to examine the consolidation of independent distribution infrastructure under major label control. It has not done so.

Understanding the pattern does not change it. It is the precondition for not being surprised by it — which is the minimum protection available while waiting for the law to catch up.

What has arrived, across every platform this series has documented, is a consistent pattern of institutions discovering that independent artists have no structural recourse against a specific harm, and then systematically imposing it.

If you’ve had a copyright strike freeze your royalties, been hit by a bot detection penalty for activity you didn’t generate, or had a distributor hold your catalog during a transfer, I’d like to hear what happened. The comments are open.

---

**Tags:** music streaming enforcement, SoundCloud copyright strikes, music fraud detection, Content ID YouTube royalties, DistroKid support
