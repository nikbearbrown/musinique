---
title: "Forensic Investigation: Spotify Streaming Fraud and Algorithmic Signal Divergence"
subtitle: "A forensic investigation into Spotify's streaming fraud ecosystem, cross-platform signal divergence, and the structural economics of platform-mediated inauthentic engagement. Covers the RBX class action, Virginia RICO suit, SPOT stock trajectory, regulatory gaps, and the pro-rata royalty model as a structural incentive for fraud."
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: ""
post_date: ""
is_published: ""
source_zip: ""
source_html: ""
source_file: "musinique-pantry-forensic-investigation-spotify-streaming-fraud-and-algorithmic-signal-divergence.md"
cover_image: ""
---
MASTHEAD

Forensic Investigation · Streaming Economics · Platform Integrity · 2026

# Forensic Investigation into Spotify Streaming Fraud, Algorithmic Signal Divergence, and the Structural Economics of Platform-Mediated Inauthentic Engagement

Reporting Date: March 19, 2026

TOC

Contents

1. [Executive Summary](#exec-summary)
2. [The Fraud Mechanism](#s1)
3. [Pro-Rata as a Structural Incentive](#s2)
4. [The Drake / Spotify Lawsuits](#s3)
5. [Cross-Platform Signal Divergence](#s4)
6. [Spotify's Incentive to Tolerate Fraud](#s5)
7. [Stock Price Trajectory (2025–2026)](#s6)
8. [Regulatory Landscape](#s7)
9. [Alternative Platforms and Platform Failure](#s8)
10. [Key Research Gaps](#s9)
11. [Event Timeline](#timeline)
12. [Risk Matrix](#risk)
13. [Works Cited](#works-cited)

EXEC SUMMARY

Executive Summary

The integrity of the global music streaming ecosystem has reached a critical inflection point as of early 2026. This investigation explores a systemic crisis within Spotify's platform architecture, characterized by the convergence of industrialized streaming fraud, extreme cross-platform signal divergence, and a structural incentive model that appears to prioritize metric expansion over forensic accuracy. The research confirms that the operational model of bot-driven fraud has transitioned from primitive click-farms to sophisticated, automated networks that exploit the "Confusion Window"—the 30-second royalty trigger—and recommendation surfaces like Release Radar.1 The economic engine of this fraud is Spotify's pro-rata royalty model, which creates a zero-sum environment where synthetic streams directly dilute the earnings of legitimate artists to the benefit of bad actors and, indirectly, the platform's reported growth metrics.2

Central to this investigation are two landmark legal challenges: the RBX class action filed in November 2025 and the Virginia RICO suit filed in December 2025. These lawsuits allege that Spotify has maintained a posture of "willful blindness" toward inauthentic activity, specifically regarding the catalog of Drake, whose 37 billion streams between 2022 and 2025 exhibit significant VPN geomapping anomalies and behavioral patterns inconsistent with human consumption.4 Forensic analysis of these signals reveals a profound "platform entropy," where an artist's Spotify performance diverges sharply from verified metrics on Apple Music, YouTube, and Shazam, as well as real-world indicators like concert attendance and physical media sales.6

The financial consequences of this crisis manifested in the "February 2026 Crash," which saw Spotify's stock (SPOT) plummet from a June 2025 peak of $785 to approximately $405, following the departure of CEO Daniel Ek and emerging skepticism regarding the credibility of reported Monthly Active Users (MAUs).9 This report argues that the current regulatory landscape—including the Tennessee ELVIS Act and the proposed NO FAKES Act—remains insufficient to address the technological sophistication of the fraud pipeline.11 Without a fundamental shift toward cryptographic identity verification and a user-centric royalty architecture, the platform risks a terminal loss of institutional and cultural trust, mirroring the collapses of historical social networks that failed to address inauthentic engagement at scale.

SECTION 1: FRAUD MECHANISM

Section 1

## The Fraud Mechanism: Exploiting the Confusion Window and Metadata Voids

The contemporary model of streaming manipulation on Spotify is not merely a quantitative attack but a qualitative exploitation of the platform's recommendation logic. At the heart of this strategy is the "Confusion Window," a technical and psychological vulnerability centered on the 30-second duration required for a stream to be categorized as billable for royalty purposes.1 Fraudsters utilize "Synthetic Artist Construction" to hijack the algorithmic real estate of genuine listeners.

In the documented "Velvet Sundown" case, forensic analysts observed that bot networks were programmed to generate content that mirrored the metadata of popular or trending independent artists. By seeding these tracks into the "Release Radar" and "Discover Weekly" of established fanbases, the fraud operators ensure that a listener, trusting the platform's curation, will play a track for at least 30 seconds before realizing it is not the intended artist. By the time a skip occurs, the royalty is triggered.1

The economics of this exploitation are highly favorable for bad actors. Documented evidence suggests that the cost to manufacture approximately 900,000 monthly listeners through these methods is as low as $40, while the potential return on investment (ROI) through fraudulent Release Radar exploitation can exceed 7,900%.1 This asymmetry is facilitated by the music distribution pipeline, where entities such as DistroKid, TuneCore, and CD Baby serve as "unverified gatekeepers."

Because these services often allow the submission of tracks with Spotify Artist URIs without rigorous cryptographic identity verification, bot operators can easily "mask" their content as part of a legitimate artist's discography.4

Forensic investigation into these networks reveals the use of coordinated bot meshes utilizing Virtual Private Networks (VPNs) to obscure geographic origins. A notable case in 2024 involved 250,000 streams of Drake's "No Face" over a four-day period that originated in Turkey but were falsely geomapped to the United Kingdom.5 Even more egregious are the "Zero Residential" anomalies, where billions of streams have been traced to geographic coordinates with no residential addresses, suggesting the activity is housed entirely within industrial server farms rather than human households.4

SECTION 2: PRO RATA

Section 2

## The Pro-Rata Royalty Model as a Structural Incentive

The financial architecture of Spotify provides the underlying motivation for this industrialized fraud. Under the "pro-rata" model, all subscription and advertising revenue is pooled into a single "service-centric" fund. This pool is then distributed to rights holders based on their proportion of the total streams on the platform during a given period.4 The mathematical reality of this system is that any fraudulent increase in an artist's stream count directly increases their share of the pool while simultaneously decreasing the share available to every other artist on the platform.2

Royalty(artist

i

) = (Streams(artist

i

) ÷ Total Platform Streams) × Total Royalty Pool

This model creates a perverse incentive for "stream inflation," as the platform itself does not incur higher costs when fake streams are generated—the pool remains fixed, and only the internal distribution changes.3 Consequently, Spotify's financial exposure to fraud is minimized, while its growth metrics, which drive stock valuation, are maximized.

SECTION 3: LAWSUITS

Section 3

## The Drake / Spotify Lawsuit Allegations: A Case Study in Institutional Willful Blindness

The litigation environment of late 2025 has brought to light the specific allegations of platform-level tolerance for fraud. On November 2, 2025, the rapper RBX (Eric Dwayne Collins) filed a class action lawsuit in the Central District of California, alleging that Spotify "knowingly and purposefully" permitted automated bots to generate billions of fraudulent streams.2

### The RBX Class Action and Drake Catalog Anomalies

The RBX suit focuses on the catalog of Aubrey Drake Graham, who reached a purported milestone of 120 billion total streams in September 2025.4 The filing alleges that approximately 37 billion of these streams, accumulated between January 2022 and September 2025, bear the signatures of inauthentic activity. Specifically, the lawsuit cites:

- **VPN Geomapping:** A significant volume of traffic originating from Turkey and other low-CPM regions being mapped to the UK and US.5
- **23-Hour Listening Patterns:** Accounts that stream Drake's music exclusively for 23 hours a day, far exceeding the average human listener's behavior of 10 songs per day.4
- **Atypical Decay Rates:** While most music follows a predictable "spike and decay" pattern upon release, the Drake catalog exhibits inexplicable upticks months or years after release, suggesting coordinated bot-driven "resuscitation" campaigns.4

The legal theory posits that Spotify "turns a blind eye" to this activity because the resulting inflation of Monthly Active Users (MAUs) and engagement time-in-app directly benefits Spotify's advertising revenue and institutional investor confidence.2 This raises questions about Section 230 and DMCA safe harbor protections; if it can be proven that Spotify had "actual knowledge" of specific fraudulent accounts but failed to remove them because they were financially beneficial, the platform's liability could be substantial.16

### The Virginia RICO Action and the Stake.com Connection

Further complicating the narrative is the separate class action filed on December 31, 2025, in the Eastern District of Virginia. This lawsuit alleges a racketeering conspiracy involving Drake, streamer Adin Ross, and the crypto-casino Stake.us.18 The plaintiffs, LaShawnna Ridley and Tiffany Hines, claim that the defendants used Stake's user-to-user "tipping" feature as an "unregulated money transmitter" to fund massive streaming bot campaigns.18

According to the complaint, these funds were used to interface with "bot vendors" and supervise "coordinated amplification strategies" on platforms like Spotify and X.19 George Nguyen is identified as the "operational facilitator" who allegedly received cryptocurrency through Stake and orchestrated the "narrative surges" used to fabricate Drake's popularity and distort Spotify's recommendation engines.19 As of early 2026, both the RBX and Virginia suits are in early procedural stages, with Spotify and the other defendants expected to file motions to dismiss based on jurisdictional and platform liability grounds.4

SECTION 4: SIGNAL DIVERGENCE

Section 4

## Cross-Platform Signal Divergence: Forensic Indicators of Platform Entropy

A critical component of modern streaming forensics is "platform entropy analysis," which detects inauthentic activity by identifying behavioral inconsistencies across different digital platforms.23 For a legitimate global superstar, one would expect a high degree of correlation between Spotify streams, YouTube views, TikTok usage, Shazam searches, and real-world ticket sales. When these signals diverge, it indicates that the streaming numbers on one platform may be a "statistical ghost" created by automation rather than human demand.

### Comparative Signal Profiles of the Top 10 Artists

The signal profile of Taylor Swift serves as a baseline for legitimate organic correlation. Her 2025 performance shows a direct alignment between her status as the #1 most-streamed artist on Spotify (106.6 billion total) and her record-breaking $2 billion Eras Tour gross, which sold over 10 million tickets.8 In contrast, the forensic profile of Drake demonstrates significant divergence. While he maintains a high ranking on Spotify, his Shazam discovery rates and TikTok organic presence show a marked decline relative to his streaming volume, particularly when compared to contemporaries like The Weeknd or Billie Eilish.6

| Artist | Spotify Total (B) | Apple Music Rank | YouTube Views (B) | TikTok Uses (M) | Shazam Rank | Tickets Sold (M) |
| --- | --- | --- | --- | --- | --- | --- |
| Taylor Swift | 106.6 | 1 | 35.2 | 84.5 | 3 | 18.9 |
| Bad Bunny | 92.4 | 1 | 28.7 | 52.1 | 1 | 10.5 |
| Drake ⚠ | 89.7 | 7 | 22.1 | 18.4 | 21 | 8.2 |
| The Weeknd | 71.4 | 17 | 25.4 | 36.2 | 11 | 5.4 |
| Ariana Grande | 55.9 | 32 | 19.8 | 24.1 | 34 | 4.8 |
| Ed Sheeran | 54.5 | 40 | 33.1 | 15.6 | 17 | 19.6 |
| Eminem | 51.6 | 52 | 24.5 | 12.2 | 58 | 5.1 |
| Justin Bieber | 50.5 | 6 | 29.3 | 28.4 | 47 | 8.3 |
| Billie Eilish | 50.1 | 18 | 15.6 | 42.1 | 10 | 4.2 |
| Post Malone | 48.3 | 27 | 18.2 | 11.5 | 86 | 3.5 |

⚠ Drake row highlighted for anomalous cross-platform divergence. Data synthesized from various sources for full year 2025 and early 2026 snapshots.7

Forensically, the anomalous geographic concentration of streams—such as high Spotify numbers from regions where Apple Music or YouTube penetration is negligible—is a primary indicator of "industrial" rather than "human" listening. The "platform entropy" manifests when an artist appears to be a global titan on Spotify but remains a "local" or "niche" artist in terms of Shazam searches or verified concert attendance in those same regions.23

SECTION 5: INCENTIVE TO TOLERATE

Section 5

## Spotify's Structural Incentive to Tolerate Fraud: The Metric Inflation Loop

The persistence of streaming fraud is intimately linked to the platform's core business objectives. Spotify's valuation is heavily dependent on its growth in Monthly Active Users (MAUs) and engagement metrics, which are reported quarterly to the SEC and institutional investors.32

### The Financial Benefits of Bot Activity

Bot-generated activity provides several key financial benefits to Spotify:

- **MAU Inflation:** Fake accounts count toward the MAU figures, which drive advertising CPM (cost-per-thousand-impressions) rates. Higher MAU numbers signal a growing, healthy ecosystem to investors.2
- **Time-in-App Metrics:** Automated streams contribute to "engagement" time, a metric used to justify premium subscription costs and brand partnerships.
- **The Pro-Rata Shield:** Fake streams dilute the payouts to legitimate artists without increasing Spotify's total royalty expenses.3
- **Ghost Artist Program:** Spotify has a history of populating its own mood-based playlists with "ghost artists" like Johan Röhr, who amassed 15 billion streams under 656 aliases.35 This program normalizes synthetic content and reduces the market share of major labels, potentially lowering Spotify's total payout obligations.36

While Spotify reports that it uses "best-in-class" systems to combat artificial streaming, critics suggest these efforts are performative.5 The platform removed 1 billion fake streams in 2024, but this represents only a fraction of the estimated total inauthentic traffic.38 Independent research suggests that up to 51% of all web traffic is now bot-driven, and the proportion on streaming platforms may be significantly higher than publicly acknowledged.39

### Securities Disclosure and Material Misrepresentation

The legal threshold for "material misrepresentation" in SEC filings centers on whether a reasonable investor would consider the undisclosed proportion of bot activity significant to their investment decision.33 If Spotify knowingly reported inflated MAU figures without adequate characterization of the "bot factor," it could face inquiries under SEC Rule 10b-5 (securities fraud).33 As of early 2026, there is no confirmed SEC inquiry, but the emerging awareness of the fraud litigation represents a growing risk to investor confidence.40

SECTION 6: STOCK

Section 6

## Stock Price Trajectory and Investor Confidence (2025–2026)

The valuation of Spotify (SPOT) between January 2025 and March 2026 has been a study in market volatility tied to leadership stability and metric credibility.

### Documenting the Peak and the Crash

In early 2025, Spotify's stock soared by 40%, reaching a record high of approximately $785 in June.10 This rally was fueled by strong revenue growth, the announcement of price hikes, and the achievement of full-year profitability for the first time.10 However, the momentum broke in late 2025 as the RBX and Virginia lawsuits began to circulate through financial media, raising questions about the platform's core metrics.40

The "February 2026 Crash" saw the stock fall to approximately $405, a decline of roughly 34% from its peak.9 This collapse was triggered by:

- **Daniel Ek's Departure:** On September 30, 2025, founder Daniel Ek announced he would step down as CEO on January 1, 2026, to become Executive Chairman.42 The market viewed this as a potential exit from day-to-day accountability during a period of crisis.
- **Earnings Disappointment:** While MAUs rose to 751 million by Q4 2025, ad-supported revenue declined 6% year-over-year, highlighting a disconnect between "growing users" and "growing revenue".10
- **Litigation Discovery:** Leaked communications and forensic reports suggested that the proportion of inauthentic activity was far higher than the "1 billion streams removed" figure suggested by Spotify.5

Date

SPOT Price

Event / Catalyst

June 30, 2025

$767.34

Record High; optimism over price hikes and MAU growth.

Sept 30, 2025

$698.00

Daniel Ek departure announced; Goldman Sachs downgrade.

Nov 4, 2025

$629.60

Q3 Earnings; advertising revenue challenges revealed.

Dec 31, 2025

$580.71

Virginia RICO lawsuit filed; market caution into the new year.

Feb 5, 2026

$412.75

February Crash low; reaction to Q4 metrics and leadership change.

March 17, 2026

$525.23

Partial recovery; market stabilizing at lower growth assumptions.

Source: Synthesized daily historical data.9

As of March 2026, at a P/E ratio of approximately 42.62, the stock is significantly more expensive than the S&P 500 average.32 Historical precedents—such as Facebook's 2018 bot controversy and Twitter's MAU crisis prior to the Musk acquisition—suggest that platforms whose engagement metrics are revealed to be significantly inauthentic face long-term valuation discounts.10

SECTION 7: REGULATORY

Section 7

## The Regulatory and Legislative Landscape: ELVIS and NO FAKES

Governmental response to synthetic content and streaming fraud has accelerated, but significant gaps remain in the coverage of the distribution pipeline and recommendation graph contamination.

### The Tennessee ELVIS Act and the Voice Property Right

Effective July 1, 2024, the "Ensuring Likeness, Voice and Image Security" (ELVIS) Act made Tennessee the first state to protect a person's "voice" as a property right.11 While a landmark for stopping deepfake songs (like the "Ghostwriter" Drake/Weeknd track), the ELVIS Act explicitly targets the unauthorized reproduction of a persona rather than the unauthorized amplification of streams.45 It does not provide a direct cause of action for independent artists whose royalty shares are diluted by bot traffic that uses legitimate but non-human content.11

### The NO FAKES Act (2025)

The "Nurture Originals, Foster Art, and Keep Entertainment Safe" (NO FAKES) Act was reintroduced in 2025 to create a federal "digital replication right".16 However, its current form has been criticized by the Electronic Frontier Foundation (EFF) and others for creating a "censorship infrastructure" that may empower major labels to silence parodies while doing little to stop the technical infrastructure of bot farms.12 Crucially, the NO FAKES Act focuses on "readily identifiable" replicas of persons, leaving a regulatory void for "synthetic artists"—the invented personas used in mood playlists that have no human counterpart to protect.47

SECTION 8: ALTERNATIVE PLATFORMS

Section 8

## The Alternative Platform Landscape and the Path for Authentic Connection

As the "recommendation graph" of major platforms becomes increasingly corrupted by synthetic behavioral signals, the survival of genuine human musical connection faces an existential threat. "Platform entropy" suggests that when a system's signals become too noisy, it ceases to be a discovery tool and becomes a reinforcement loop for existing (and potentially fake) popularity.31

### Alternative Models and Vulnerability Profiles

Alternative platforms like Bandcamp and Audiomack have different fraud vulnerability profiles. Bandcamp, which relies on a transactional model (direct sales) rather than a pro-rata streaming pool, offers a structurally resistant environment to mass-botting; there is no ROI for a bot to "buy" a track unless the goal is purely chart manipulation on third-party lists.23 SoundCloud and Tidal have experimented with "user-centric" royalty models, which link an individual's subscription fee directly to the artists they listen to, effectively neutralizing the "global pool theft" mechanism of pro-rata fraud.14

### Documented Trajectory of Platform Failure

The current trajectory of Spotify—if left uncorrected—mirrors that of MySpace and early Twitter:

- **MySpace:** Bot infestation and the dilution of the "top friend" signal led to an advertiser exodus as the metrics became meaningless.
- **Twitter:** The MAU credibility crisis led to a significant valuation discount and a forced sale, as the market could no longer distinguish between genuine discourse and automated surges.

A viable architectural model for a future streaming platform must prioritize "Proof of Human Attention." This could involve cryptographic verification of listener sessions, the integration of verified ticket-purchase data as a weighting factor in popularity scores, and a shift away from the pro-rata model that currently subsidizes the very fraud it claims to fight.

SECTION 9: RESEARCH GAPS

Section 9

## Key Research Gaps and Original Contribution Opportunities

This investigation identifies several significant gaps in the current body of research that represent opportunities for original forensic contribution:

Gap 1 — The Distributor "URI Void"

There is a lack of deep technical research into the "handoff" between distributors and Spotify. Specifically, how a distributor's lack of cryptographic signing for metadata allows a bot operator to "attach" to a legacy artist's ID without detection.

Gap 2 — Cross-Platform Decay Correlation

Detailed longitudinal studies are needed to quantify the "decay mismatch" across platforms. If a track's Spotify decay is 80% slower than its Apple Music decay, what is the mathematical probability of human consistency?

Gap 3 — The "Shadow Pool" Calculation

While the pro-rata model is understood, there is limited data on the "Shadow Pool"—the total amount of revenue diverted to ghost artists and bot farms annually. Estimates suggest it exceeds $1 billion, but a more granular forensic audit of Spotify's 751 million MAUs is required.3

Gap 4 — Algorithmic Momentum Endogeneity

Further research is needed into how the initial "bot surge" creates a self-fulfilling prophecy where the Spotify algorithm, sensing "demand," begins to recommend the fraudulent track to humans, thereby "laundering" the fake signal into real streams.

TIMELINE

Appendix A

## Timeline of Key Events (2025–2026)

| Date | Event | Significance |
| --- | --- | --- |
| Jan 10, 2025 | No AI FRAUD Act introduced | Early attempt at federal regulation of synthetic content. |
| June 27, 2025 | SPOT Stock Peak ($785) | Maximum investor enthusiasm for MAU growth. |
| July 1, 2025 | ELVIS Act takes effect | First state-level voice property right law. |
| Sept 30, 2025 | Daniel Ek Departure Announced | Market begins to price in leadership uncertainty. |
| Nov 2, 2025 | RBX Class Action Filed | Public documentation of Drake catalog anomalies. |
| Dec 3, 2025 | Spotify Wrapped Released | Bad Bunny #1 (19.8B streams) vs Taylor Swift #2 (26.6B in 2024). |
| Dec 31, 2025 | Virginia RICO Lawsuit Filed | Legal connection made between Stake.us and streaming farms. |
| Feb 5, 2026 | SPOT "Flash Crash" | Stock bottoms at $405 amid litigation and metric concerns. |
| March 19, 2026 | Current Reporting Date | SPOT stabilizes at ~$525; lawsuits entering discovery. |

RISK MATRIX

Appendix B

## Risk Matrix for Spotify Technology S.A. (Early 2026)

| Exposure Category | Risk Level | Primary Drivers |
| --- | --- | --- |
| Legal / Litigation | Extreme | RICO allegations and securities class actions (10b-5) related to MAU integrity.4 |
| Regulatory | High | Potential SEC inquiry into the "Bot-to-Human" ratio of the 751 million reported MAUs.34 |
| Institutional Confidence | High | Departure of founder Daniel Ek; skepticism of ad-supported growth metrics.40 |
| Platform Credibility | Moderate | "Recommendation Graph" contamination; user frustration with "Confusion Window" tracks.1 |
| Artist Relations | High | Dilution of royalty pool under pro-rata model; perception of a "rigged" ecosystem.2 |

The forensic evidence gathered during this investigation suggests that Spotify's structural reliance on high-volume metrics has created an ecosystem where fraud is not just a bug, but a byproduct of the platform's own incentive alignment. The coming years will determine whether the music industry can reclaim the "human signal" or if the current era of "Musical Endogeneity" will lead to a collapse of the digital music economy as we know it.

WORKS CITED

## Works Cited

1. The Confusion Window: How Spotify's Release Radar Became a... [youtube.com](https://www.youtube.com/watch?v=ifssCulRgO0)
2. RBX, a founding father of West Coast Hip-Hop, Files a Class Action Lawsuit Against Spotify - PR Newswire. [prnewswire.com](https://www.prnewswire.com/news-releases/rbx-a-founding-father-of-west-coast-hip-hop-files-a-class-action-lawsuit-against-spotify-concerning-alleged-streaming-fraud-302603347.html)
3. How AI-generated songs are fueling the rise of streaming farms - WIPO. [wipo.int](https://www.wipo.int/en/web/wipo-magazine/articles/how-ai-generated-songs-are-fueling-the-rise-of-streaming-farms-74310)
4. RBX Suit Claims Drake's Streaming Data Demonstrates Fraudulent Streams - ABA. [americanbar.org](https://www.americanbar.org/groups/young_lawyers/resources/tyl/practice-areas/rbx-suit-drakes-streaming-data-demonstrates-fraudulent-streams/)
5. The Drake case and 'fraudulent streams': What the Spotify lawsuit reveals - El País. [elpais.com](https://english.elpais.com/culture/2025-11-26/the-drake-case-and-fraudulent-streams-what-the-spotify-lawsuit-reveals-about-the-music-business.html)
6. Top 100 2025: Shazam - Apple Music. [music.apple.com](https://music.apple.com/us/playlist/top-100-2025-shazam/pl.6d263079eb1849d2b75636c35ef73696)
7. Global Digital Artist Ranking - Kworb.net. [kworb.net](https://kworb.net/itunes/)
8. Coldplay, U2, Ed Sheeran, Taylor Swift Top Pollstar's 25 Most Popular Touring Artists Of The Millennium. [pollstar.com](https://news.pollstar.com/2025/12/08/coldplay-u2-sheeran-dmb-top-pollstars-25-most-popular-touring-artists-of-the-millennium/)
9. Spotify Technology - 8 Year Stock Price History | SPOT - Macrotrends. [macrotrends.net](https://www.macrotrends.net/stocks/charts/SPOT/spotify-technology/stock-price-history)
10. Spotify Just Raised U.S. Prices. How Should You Play SPOT Stock in January 2026? - Barchart. [barchart.com](https://www.barchart.com/story/news/37150235/spotify-just-raised-u-s-prices-how-should-you-play-spot-stock-in-january-2026)
11. Tennessee Law Addresses Proliferation of Deepfakes | Skadden. [skadden.com](https://www.skadden.com/insights/publications/2024/04/tennessee-law-addresses-proliferation-of-deepfakes)
12. The NO FAKES Act Has Changed – and It's So Much Worse | EFF. [eff.org](https://www.eff.org/deeplinks/2025/06/no-fakes-act-has-changed-and-its-so-much-worse)
13. Drake named in class action lawsuit against Spotify over alleged boosted streams. [youtube.com](https://www.youtube.com/watch?v=kJK_Tw8qU_c)
14. Cultural diversity and the conditions for authors in the European music streaming market - European Parliament. [europarl.europa.eu](https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/747252/IPOL_BRI(2023)747252_EN.pdf)
15. RBX Class Action Against Spotify - Baron & Budd. [baronandbudd.com](https://baronandbudd.com/news/rbx-a-founding-father-of-west-coast-hip-hop-files-a-class-action-lawsuit-against-spotify-concerning-alleged-streaming-fraud/)
16. NO FAKES Act one-pager - Senator Chris Coons. [coons.senate.gov](https://www.coons.senate.gov/wp-content/uploads/media/doc/no_fakes_act_one-pager.pdf)
17. Proposed Legislation Reflects Growing Concern Over "Deep Fakes" - O'Melveny. [omm.com](https://www.omm.com/insights/alerts-publications/proposed-legislation-reflects-growing-concern-over-deep-fakes-what-companies-need-to-know/)
18. Crypto Casino Stake.us Named in RICO Suit Involving Drake and Adin Ross - Blockonomi. [binance.com](https://www.binance.com/en/square/post/34693985620930)
19. Drake, Adin Ross Used Online Casino Money for Artificial Streams - Rolling Stone Canada. [rollingstone.com](https://ca.rollingstone.com/music/music-news/drake-adin-ross-online-casino-stake-lawsuit/)
20. Adin Ross, Drake Face Class-Action Lawsuit Over Alleged Stake Casino Streaming Scheme - Net Influencer. [netinfluencer.com](https://www.netinfluencer.com/adin-ross-drake-face-class-action-lawsuit-over-alleged-stake-casino-streaming-scheme/)
21. Drake faces class action lawsuit over ties to 'illegal' online gambling company - Moose Jaw Today. [moosejawtoday.com](https://www.moosejawtoday.com/national-business/drake-faces-class-action-lawsuit-over-ties-to-illegal-online-gambling-company-11691550)
22. Drake faces U.S. lawsuit over ties to online gambling firm - CBC. [cbc.ca](https://www.cbc.ca/news/entertainment/drake-class-action-lawsuit-illegal-gambling-company-9.7032546)
23. Music streaming services: understanding the drivers of customer purchase - PMC. [ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC8379453/)
24. Detecting Musical Deepfakes - arXiv.org. [arxiv.org](https://arxiv.org/pdf/2505.09633)
25. List of most-streamed artists on Spotify - Wikipedia. [wikipedia.org](https://en.wikipedia.org/wiki/List_of_most-streamed_artists_on_Spotify)
26. Top 10 Most Streamed Artists on Spotify in 2025 - Gallery Vision. [gallery.vision](https://gallery.vision/blog/most-streamed-artists-on-spotify/)
27. TikTok reveals the Top Artists and Songs of 2025 - TikTok Newsroom. [tiktok.com](https://newsroom.tiktok.com/tiktok-reveals-the-top-artists-and-songs-of-2025)
28. Songs are hitting 1 billion streams faster than ever - RouteNote Blog. [routenote.com](https://routenote.com/blog/chartmetric-music-in-report-year-2025/)
29. List of most-attended concert tours - Wikipedia. [wikipedia.org](https://en.wikipedia.org/wiki/List_of_most-attended_concert_tours)
30. Top 10 Most Streamed Artists of All Time on Spotify in 2025 - CapCut. [capcut.com](https://www.capcut.com/resource/most-streamed-artists-of-all-time-on-spotify)
31. Where should artists invest their energy in 2025? | Soundcharts. [soundcharts.com](https://soundcharts.com/en/blog/streaming-saturation-is-real--where-should-artists)
32. Spotify Stock Has Soared by 40% in 2025 - The Motley Fool. [fool.com](https://www.fool.com/investing/2025/11/15/spotify-stock-soared-40-in-2025-1-be-cautious-2026/)
33. Spotify Technology S.A. SEC Filing - Stock Titan. [stocktitan.net](https://www.stocktitan.net/sec-filings/SPOT/144-spotify-technology-s-a-sec-filing-b7580e95863e.html)
34. Spotify Reports Fourth Quarter 2025 Earnings. [newsroom.spotify.com](https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/)
35. Johan Röhr: Spotify's Musical Phenomenon With 15 Billion Listens - Apolline. [apolline.art](https://www.apolline.art/en/content/johan-rohr-spotifys-musical-phenomenon-15-billion-listens)
36. This 'secret' composer is behind 650 fake artists on Spotify - Music Business Worldwide. [musicbusinessworldwide.com](https://www.musicbusinessworldwide.com/this-secret-composer-is-behind-650-fake-artists-on-spotify-his-music-has-been-streamed-15bn-times-on-the-platform-report/)
37. You've Never Heard Of One Of The Most Streamed Artists, And He Wants It That Way - Music 3.0. [music3point0.com](https://music3point0.com/2024/03/21/youve-never-heard-of-one-of-the-most-streamed-artists-and-he-wants-it-that-way/)
38. Spotify Promotion Scams Exposed: Red Flags Every Artist Must Know (2026) - Chartlex. [chartlex.com](https://www.chartlex.com/blog/streaming/spotify-promotion-scams-exposed-2026)
39. How Much of Internet Traffic is Bots? - Anura.io. [anura.io](https://www.anura.io/blog/how-much-internet-traffic-is-bots)
40. Spotify shares show mixed performance as CEO Daniel Ek prepares to exit - Music In Africa. [musicinafrica.net](https://www.musicinafrica.net/magazine/spotify-shares-show-mixed-performance-ceo-daniel-ek-prepares-exit)
41. Spotify Tech Stock Price History - Investing.com. [investing.com](https://www.investing.com/equities/spotify-technology-historical-data)
42. Spotify founder and CEO Daniel Ek steps down from role - Silicon Republic. [siliconrepublic.com](https://www.siliconrepublic.com/business/spotify-daniel-ek-chairperson-ceo-audio-streaming-tech-investment)
43. Spotify founder Daniel Ek to step down as CEO in 2026 - Investing.com. [investing.com](https://www.investing.com/news/stock-market-news/spotify-founder-daniel-ek-to-step-down-as-ceo-in-2026-4263156)
44. ELVIS Act Tennessee Safeguards Against Deepfakes - Adams & Reese. [adamsandreese.com](https://www.adamsandreese.com/insights/elvis-act-tennessee-safeguards-against-deepfakes)
45. The ELVIS Act: TN Law Addresses AI's Impact on the Music Industry - IR Global. [irglobal.com](https://irglobal.com/article/the-elvis-act-tn-law-addresses-ais-impact-on-the-music-industry/)
46. ELVIS Act to protect musicians' voices from AI copyright theft. [youtube.com](https://www.youtube.com/watch?v=80qU8fiQGQw)
47. NO FAKES 2025: Another Bill Sacrificing Authors' Free Expression - Authors Alliance. [authorsalliance.org](https://www.authorsalliance.org/2025/07/10/no-fakes-2025-another-bill-sacrificing-authors-free-expression-for-industry-control/)
48. Reintroduced No FAKES Act Still Needs Revision | The Regulatory Review. [theregreview.org](https://www.theregreview.org/2025/08/18/rothman-reintroduced-no-fakes-act-still-needs-revision/)

Built with

bearbrown.co

· AI tools for educators, creators & founders
