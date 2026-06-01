---
title: "Spotify Engagement Integrity: MAU Methodology, Bot Classification & SEC Disclosure"
subtitle: "An investigative analysis of Spotify's 751M MAU methodology, automated traffic risks, and SEC disclosure sufficiency compared to Meta, Twitter, and YouTube. Examines the RBX v. Spotify class-action lawsuit, royalty accounting implications, and advertiser fraud exposure."
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: ""
post_date: ""
is_published: ""
source_zip: ""
source_html: ""
source_file: "musinique-pantry-spotify-engagement-integrity-mau-methodology-bot-classification-sec-disclosure.md"
cover_image: ""
---
MASTHEAD

Investigative Analysis · Streaming Economics · Securities Law

# Spotify Engagement Integrity: An Analysis of MAU Methodology, Bot Classification, and SEC Disclosure Sufficiency

As of fiscal year 2025 · bearbrown.co research notes

TOC

Contents

1. [Executive Summary](#exec-summary)
2. [Technical Definition and Internal Counting Criteria](#s1)
3. [The Good Bot Problem and Audio-Specific Anomalies](#s2)
4. [Systematic Review of SEC Filings (2020–2025)](#s3)
5. [The Advertiser Angle and Invalid Traffic Standards](#s4)
6. [The MAU Inflation Incentive Structure](#s5)
7. [Comparative Platform Methodology and Discovery Findings](#s6)
8. [Legal Exposure and Securities Fraud Analysis](#s7)
9. [The Royalty Accounting Dimension](#s8)
10. [Nuanced Conclusions and Investigative Outlook](#conclusions)
11. [Top 5 Unanswered Questions for Regulatory Subpoena](#questions)
12. [Works Cited](#works-cited)

EXECUTIVE SUMMARY

Executive Summary

As of the conclusion of the 2025 fiscal year, Spotify Technology S.A. reported a record 751 million Monthly Active Users (MAUs), marking a pivotal moment in the platform's history as it surpassed three-quarters of a billion global participants.1 This metric serves as the foundational pillar for the company's market capitalization, which has fluctuated significantly as investors weigh the platform's ubiquity against its long-term profitability goals.3 However, the methodological soundness of this 751 million figure is increasingly subject to scrutiny due to a systemic shift in the nature of global internet traffic. Cybersecurity analysis provided by the 2025 Imperva Bad Bot Report establishes that for the first time in a decade, automated traffic has surpassed human activity, now accounting for 51% of all web traffic—composed of 37% "bad bots" and 14% "good bots".5

The central challenge for Spotify lies in the functional reality of audio streaming: unlike search indexing or performance monitoring, there is no legitimate technical rationale for a non-human agent to initiate and maintain an audio stream for the 30-second duration required to trigger royalty and engagement thresholds.6 Consequently, any automated activity that registers as a stream within Spotify's reported engagement figures is definitionally either a miscount or a malicious intervention. This research investigates whether Spotify's counting methodology, as disclosed in its 20-F and 6-K filings, sufficiently accounts for this distinction and whether the platform's historical disclosure practices align with the transparency standards set by peers such as Meta, Alphabet, and the pre-acquisition Twitter.9

The investigation identifies a significant divergence between Spotify's high-level growth narrative and the rising legal risks associated with metric inflation. The late 2025 filing of the RBX v. Spotify class-action lawsuit highlights specific allegations that the platform has "deliberately turned a blind eye" to billions of fraudulent streams, particularly those originating from virtual private networks (VPNs) and non-populated geographic areas.8 Under SEC Regulation S-K Item 303, the company is obligated to disclose known uncertainties that could materially impact operations; yet, Spotify continues to rely on qualitative assurances regarding its "best-in-class" systems without providing the quantitative bot-load estimates that have become standard in the ad-supported platform sector.12 As the platform transitions toward a more aggressive monetization of its 476 million ad-supported users, the risk of securities fraud and advertiser disputes remains high, potentially compromising the integrity of the $11 billion in annual royalties paid to the global music industry.1

SECTION 1

Section 1

## Technical Definition and Internal Counting Criteria

The Monthly Active User (MAU) metric is the primary Key Performance Indicator (KPI) through which Spotify communicates its market penetration and the vitality of its ecosystem. In its official communications to the Securities and Exchange Commission (SEC), Spotify defines an MAU as an individual account that has interacted with the platform within a rolling 30-day window.16 While seemingly straightforward, the technical nuances of what constitutes "activity" and how that activity is validated are critical for assessing the platform's vulnerability to automated inflation.

### Technical Parameters of the MAU Count

In contrast to some social media platforms that require an "authenticated" visit or a specific login event, Spotify's high-level definitions often encompass any account that registers a session on its infrastructure.18 The platform distinguishes between its two primary tiers—Premium Subscribers and Ad-Supported MAUs—but aggregates these into a single top-line figure for quarterly growth assessments.19

| Metric Category | Q4 2024 Actual | Q4 2025 Actual | YoY Growth |
| --- | --- | --- | --- |
| Total MAUs | 675 Million | 751 Million | 11% |
| Premium Subscribers | 263 Million | 290 Million | 10% |
| Ad-Supported MAUs | 425 Million | 476 Million | 12% |

Data derived from.1

The 12% year-over-year growth in the Ad-Supported tier is particularly relevant to the bot-exclusion discussion. Ad-supported accounts are free to create and do not require the verification of a credit card or a verified payment method, which is the primary friction point preventing large-scale bot-farming in the Premium segment.15

The fact that the free tier is growing at a faster rate than the verified subscriber base suggests that the platform's overall growth narrative is increasingly reliant on its most vulnerable demographic.1

### Qualifying Actions and Session Initialization

A "qualifying action" for MAU purposes generally includes opening the application or visiting the website while logged in. However, Spotify's technical ecosystem is complex, involving integrations with smart speakers, wearables, automotive interfaces, and third-party APIs.23 In October 2025, the company launched an integration with ChatGPT, allowing the AI to initiate platform interactions.25 This raises the question of whether an AI-initiated query or a background "ping" from an integrated device registers as an MAU event. If background updates or non-human API requests are captured in the count, the 751 million figure may reflect system-level interactions rather than human intent.

### Technical Validation Systems

Spotify acknowledges in its risk factors that its internal company tools are used to track these metrics and are not independently verified.11 While the company claims to invest in "always-improving, best-in-class systems" to combat artificial engagement, it does not disclose the technical specifics of its human-verification layers.15 Peers like Google and TikTok utilize more visible validation steps, such as freezing counts for manual review or requiring minimum watch times (5 to 30 seconds) to qualify an interaction as engagement.28 Spotify's methodology remains focused on the binary presence of activity within the 30-day window, a standard that is increasingly easy for modern, AI-enhanced bots to satisfy by mimicking legitimate session patterns.6

### Consistency and Material Changes (2020–2026)

From 2020 through early 2026, Spotify's MAU definition has remained largely static in its public filings, despite massive changes in the platform's content mix.1 The expansion into podcasts and audiobooks has provided new ways for accounts to be "active" without ever listening to music.1 This diversification is intended to increase "ubiquity," but it also complicates the validation of human users, as different content types attract different bot behaviors (e.g., podcast indexing bots vs. music metadata scrapers).25

SECTION 2

Section 2

## The Good Bot Problem and Audio-Specific Anomalies

The global internet infrastructure depends on "good bots" for basic functionality. These include search engine crawlers like Googlebot and Bingbot, API monitors for service uptime, and metadata aggregators that fuel the music discovery ecosystem.35 However, the presence of these agents on an audio streaming platform presents a unique methodological problem: unlike text-based websites, where a crawl is a legitimate interaction, a bot "listening" to music is an anomaly.

### Categories of Automated Platform Interaction

Multiple categories of legitimate bots interact with Spotify daily:

- **Search Indexing:** Crawlers index artist and track pages to ensure Spotify links appear in search results.37
- **API Monitoring:** Third-party services monitor API responsiveness and availability.6
- **Podcast Indexing:** Bots crawl RSS feeds and episode descriptions for searchability.34
- **Analytics Scrapers:** Services scrape public chart data to provide industry reports.40

The foundational logical premise is that these bots have no reason to initiate an audio stream for the 30+ second duration that triggers royalty recognition and engagement tracking.6 If a bot crawling an artist page incidentally triggers a preview play or an embedded stream, and that interaction is recorded as an "active" event, it creates an inorganic inflation of the MAU count.

### Academic and Technical Literature on Bot Intent

Cybersecurity literature, including the 2025 Imperva report, notes that bots are increasingly using "headless browsers"—software that executes JavaScript and renders web pages like a human user but without a visual interface.6 This allows bots to bypass simple detection and potentially interact with play buttons or media elements.42 While search crawlers traditionally ignore overlays and "interstitials," new multimodal Large Language Model (LLM) agents are capable of "audio private attribute profiling," where they ingest audio data to infer sensitive attributes.43 This suggests that "good bots" (like LLM training scrapers) may now have a functional reason to play audio, which directly conflicts with Spotify's human-centric engagement narrative.

### Miscounting Cases on Audio Platforms

Documented cases of legitimate bot activity being miscounted as human engagement are rare in public disclosures but prevalent in industry discussions. The RBX v. Spotify lawsuit alleges that billion-stream artists like Drake show "staggering and irregular" streaming patterns that deviate from typical human decay curves.8 Specifically, accounts were found listening exclusively to one artist's catalog for 23 hours a day—a pattern that is physically impossible for a single human user but standard for an automated script.8 If Spotify's systems are not rigorously filtering these impossible patterns from the MAU count, the "active user" figure becomes a measure of total platform usage rather than unique human participants.

### Video Benchmarking (YouTube vs. Spotify)

YouTube provides the industry benchmark for bot traffic mitigation. Its methodology publicly documents the distinction between "views" and "unique viewers" and includes a validation phase for counts that exceed certain thresholds.28 YouTube's 30-second requirement is designed specifically to filter out accidental clicks and automated pings.29 Spotify's MAU metric lacks this level of granular, publicly documented validation. While YouTube Music is technically larger by users (2.7 billion MAU), its reliance on Google's more mature bot-filtering infrastructure provides a level of metric integrity that Spotify's "internal company tools" struggle to match.44

SECTION 3

Section 3

## Systematic Review of SEC Filings (2020–2025)

Spotify's regulatory disclosures between 2020 and 2025 reveal a consistent pattern of reporting aggregate user growth while hedging the reliability of those metrics through standardized risk language.14

### Defining MAU in Risk Factors

In its 20-F filings, Spotify includes a dedicated section on "Industry Data and User Metrics".11 The company states that its MAUs and average revenue per user (ARPU) are calculated using internal company data that hasn't been independently verified.26 The risk factors disclose that:

- Real or perceived inaccuracies in these metrics could harm reputation and business results.11
- The metrics are affected by applications on certain mobile devices that "automatically contact our servers for regular updates with no user action involved".11
- This activity can cause the system to count the associated device as an active user for that period.26

### The Quantitative Disclosure Gap

The most striking finding of the systematic review is the lack of a quantified bot estimate. Since its 2011 IPO filings, Meta (formerly Facebook) has disclosed that "false or duplicate accounts" represented approximately 5–6% of its MAU.11 By 2019, Meta narrowed this to an estimate of ~5% fake accounts, noting that they proactively detect 99% of them.50 Similarly, Twitter's pre-acquisition filings claimed that "fewer than 5%" of its monetizable daily active users (mDAU) were false or spam accounts.10

In contrast, Spotify's filings from 2020 through 2025 contain no such quantified estimate.14 The platform acknowledges the existence of automated traffic but fails to provide investors with a percentage-based margin of error. This omission is particularly significant given the 2025 Imperva data showing that bot traffic is at an all-time high.5

### SEC Disclosure Rules and MD&A Obligations

Regulation S-K Item 303 (Management's Discussion and Analysis) requires companies to focus on material events and uncertainties known to management.12 The SEC's 2020 update emphasized that MD&A should include any known trends "reasonably likely to cause a material change" in the relationship between costs and revenues.52 If Spotify management is aware of a high-volume bot presence that is inflating the MAU count—and thereby affecting CPM rates and labels' perceptions of market share—Item 303 mandates its disclosure.12 Failure to quantify this risk, especially when peers have established a precedent for doing so, creates a material vulnerability under Rule 10b-5.48

SECTION 4

Section 4

## The Advertiser Angle and Invalid Traffic Standards

Spotify's revenue model is bifurcated, with its 476 million ad-supported users generating revenue through Cost Per Thousand (CPM) impression rates.1 For advertisers, the integrity of these engagement figures is not just a matter of platform health but of contractual performance.

### Advertising Contracts and Real Person Representations

The fundamental value proposition Spotify makes to brands is access to a massive, engaged human audience.57 Advertisers typically assume that the impressions they purchase are seen or heard by "real people".58 If a material portion of the MAU base is automated, the impressions served to those accounts are "invalid".61

### The Role of the Media Rating Council (MRC)

The Media Rating Council (MRC) and the Interactive Advertising Bureau (IAB) have established rigorous standards for Invalid Traffic (IVT) detection.64 These guidelines divide traffic into:

- **General Invalid Traffic (GIVT):** Simple bots, crawlers, and data-center traffic identifiable through routine filtration.61
- **Sophisticated Invalid Traffic (SIVT):** More difficult cases requiring advanced analytics, such as bots masquerading as humans, hijacked devices, and falsified location data.61

Measurement organizations must be audited by independent CPA firms to claim MRC accreditation.65 While Spotify has integrated third-party verification tools like DoubleVerify (DV) for its video ads to measure fraud and viewability, the platform itself is not currently listed as fully MRC-accredited for its total MAU or audio engagement metrics.58

### The Scale of the Ad Fraud Problem

Industry reports from 2025 indicate that $63 billion was lost to invalid traffic across digital advertising.70 Programs like TikTok show IVT rates as high as 24.2%, while programmatic auction baselines for unfiltered fraud hover around 10.36%.6 Spotify's reliance on automated sales channels—which are the primary contributors to its ad growth—creates an analogous exposure to these high IVT rates.1

| Platform | Average IVT Rate (2025 Est.) | Disclosure Rigor |
| --- | --- | --- |
| TikTok | 24.2% | High (Purge transparency) |
| LinkedIn | 19.88% | Medium (Third-party integration) |
| X (Twitter) | 12.79% | Medium (Musk-led transparency) |
| Meta | 8.2% | High (Quarterly false account est.) |
| **Spotify** | Not Disclosed | Low (Boilerplate risks only) |

Data based on.14

The lack of quantified IVT or bot-presence disclosure makes it impossible for advertisers to determine if they are receiving the "human" reach they are paying for. If Spotify serves advertisements to sessions that are bot-generated, this could be construed as advertiser fraud under state and federal consumer protection frameworks.15

SECTION 5

Section 5

## The MAU Inflation Incentive Structure

Spotify's valuation as a high-growth technology company is contingent on its ability to sustain double-digit MAU increases.3 This creates a powerful structural incentive to avoid the implementation of rigorous bot exclusion that would result in a net user count decrease.

### Stock Market Capitalization and Investor Sentiment

In 2025, Spotify's market valuation reached approximately $100 billion, fueled by record net MAU additions in Q4.1 However, the stock remains sensitive to even minor misses in guidance.4 Analysts from firms like Bernstein and Wolfe Research have highlighted "longer-dated risks" related to valuation, suggesting that any disruption to the growth narrative would lead to significant price target reductions.4

### Leveraging Dominance against Rights Holders

Spotify's size (751 million MAU) is its primary leverage in negotiations with the Big Three labels (Universal, Sony, Warner).22 By reporting a user base that is "more than double its nearest competitor," Spotify can demand more favorable licensing terms and lower effective royalty rates.22 If a rigorous bot audit revealed that the platform's "human" base was actually 10–15% smaller than reported, its competitive standing would be significantly diminished.

### The Financial Cost of Admitting Inflation

If bot activity inflates the MAU count by even 5–10%, the financial implications are massive:

- **Ad Revenue:** A 10% reduction in "valid" users would theoretically lead to a 10% reduction in the total available ad impressions, directly impacting the €518 million quarterly ad-supported revenue.1
- **Royalty Payouts:** Under the "streamshare" model, bot-generated streams increase the size of the "total streams" denominator, effectively siphoning royalties away from legitimate artists and toward the bot operators.8

### Evidence of Systemic Blindness

The RBX v. Spotify lawsuit specifically alleges that the platform's anti-fraud systems are "nothing more than window dressing".15 The complaint asserts that Spotify benefits from the "increased number of overall music streams generated by bot accounts" because it allows them to report higher engagement to shareholders.77 This theory suggests that Spotify has a vested interest in maintaining the status quo as long as the true origin of the streams remains hidden.

SECTION 6

Section 6

## Comparative Platform Methodology and Discovery Findings

A deep dive into the methodology of Spotify's peers reveals a much more aggressive approach to bot exclusion and transparency.

### YouTube's Validation and View-Freeze

YouTube documents its view count validation methodology publicly, explaining that it removes non-human traffic and validates "real" views through behavioral analysis.28 This rigorous approach is a response to the "viewbotting" industry, which artificially boosts counts to simulate popularity.30 YouTube Music benefits from this established infrastructure, whereas Spotify relies on internal tools developed for audio that may not have the same cross-platform verification capabilities.26

### Meta's False Account Estimates

Meta's quarterly evaluation of "duplicate" and "false" accounts is the gold standard for platform transparency. By dividing false accounts into "user-misclassified" and "violating" (spam/bots), Meta provides a clear quantitative framework for investors to assess metric reliability.9 Spotify's refusal to provide an analogous percentage—despite having a similarly large ad-supported base—is a notable outlier in the sector.14

### Twitter/X Discovery and the Zatko Complaint

The legal battle over the Twitter acquisition revealed the immense difficulty of counting bots. Discovery showed that Twitter utilized a subjective, human-led process for auditing 100 mDAU per day (approximately 9,000 per quarter) to verify the automated screening's effectiveness.10 The Zatko (Peiter "Mudge" Zatko) whistleblower complaint alleged that Twitter was violating FTC consent decrees regarding data security and user engagement integrity, claiming the platform was vulnerable to widespread bot manipulation that management knew about but did not adequately disclose.10

### TikTok's High-Friction Validation

TikTok's model is inherently "generous" in counting plays, but its "qualified view" system for payouts requires the For You Page (FYP) as the source, excluding views from direct links or sharing to prevent gaming.28 TikTok also purges millions of fake accounts quarterly, providing a level of "hygiene" transparency that Spotify lacks in its Ad-Supported MAU reporting.29

SECTION 7

Section 7

## Legal Exposure and Securities Fraud Analysis

The convergence of high bot traffic, unquantified disclosures, and allegations of "willful blindness" creates a substantial legal risk profile for Spotify Technology S.A.

### Securities Fraud (Rule 10b-5) Elements

To prevail in a Rule 10b-5 securities fraud claim, a plaintiff must establish:

- **Materiality:** Would a reasonable investor find the inclusion of bots in the 751 million MAU figure important? Given the platform's growth-dependent valuation, the answer is likely yes.4
- **Scienter:** Did Spotify know or recklessly disregard that its MAUs were inflated? The RBX lawsuit's specific data points—such as 250,000 suspect streams of a single song in a four-day period from Turkey falsely geomapped as U.K. traffic—provide a strong basis for alleging scienter.27
- **Loss Causation:** Investors would need to show that their financial losses were directly related to the revelation of inflated metrics.4

### Advertiser Fraud and FTC Regulation

Selling ad inventory based on metrics that management knows include automated traffic is a potential violation of Section 5 of the FTC Act, which prohibits "unfair or deceptive acts or practices".15 The RBX complaint specifically alleges that Spotify uses "insufficient measures to address fraudulent streaming," which by extension means it is selling ad impressions based on a "purported system" that is inadequate.78

### Class Action Exposure Matrix

| Risk Factor | Rating | Supporting Rationale |
| --- | --- | --- |
| Securities Fraud | High | Absence of quantified bot disclosure compared to Meta/Twitter; MAU-dependent valuation.4 |
| Advertiser Fraud | Medium | Partial mitigation via DV/IAS, but total MAU narrative remains unverified.58 |
| Class Action Risk | High | The RBX v. Spotify lawsuit creates a blueprint for over 100,000 U.S. rights holders.72 |
| Regulatory Inquiry | High | Imperva 2025 data + lawsuit allegations may trigger SEC spot checks of Item 303 compliance.6 |

### Legally Vulnerable Language in the 2025 20-F

The most legally vulnerable statement in Spotify's 2025 Form 20-F is: "We regularly review our processes to assess potential improvements to their accuracy… From time to time, we may discover inaccuracies in our metrics or make adjustments to improve their accuracy".26 This "safe harbor" language may be insufficient if discovery reveals that management was presented with specific, large-scale bot-load data and chose not to make a public adjustment or restatement.

SECTION 8

Section 8

## The Royalty Accounting Dimension

Spotify's $11 billion annual payout to the music industry is governed by the "streamshare" model.2 This pro-rata system makes the accuracy of every single stream count—and every unique user—a matter of financial life or death for independent artists.

### The "Denominator Problem" in Streamshare

Royalties are calculated as:

Artist Royalty = (Artist's Streams ÷ Total Platform Streams) × Total Royalty Pool

If bots generate billions of "Total Platform Streams," the denominator increases while the fixed "Total Royalty Pool" remains the same. This dilutes the value of every legitimate human stream.8 The RBX suit asserts that this causes "massive financial harm to legitimate artists… whose proportional share is decreased as a result of fraudulent stream inflation".8

### Accounting Standards (GAAP/IFRS) and Royalty Recognition

Spotify utilizes International Financial Reporting Standards (IFRS) for its consolidated statements.14 Under IFRS 15 (Revenue from Contracts with Customers), performance obligations must be measurable with precision.84 If the data underlying the royalty obligation (the stream count) is corrupted by a material percentage of fraudulent activity, the platform's liability disclosures could be fundamentally inaccurate.

### Audit Rights and the Power Imbalance

Major labels have the contractual right to audit Spotify's books, but these audits are often restricted by NDAs and focus on the total pool size rather than the integrity of the stream count.86 Independent artists often have no such rights and must rely on Spotify's internal data, which they allege is "negligently" or "willfully" unmonitored.72 The "Musical Endogeneity" trilogy suggests that this power imbalance allows the platform to maintain high-level engagement narratives that structurally disadvantage the "backbone" of the music business: the independent creator.15

CONCLUSIONS

Conclusions

## Nuanced Conclusions and Investigative Outlook

The cumulative evidence demonstrates that Spotify Technology S.A. operates with a methodological "black box" regarding its primary engagement metric. While the platform reports 751 million MAUs, the failure to quantify the automated traffic within that figure—in an era where 51% of web traffic is non-human—presents a severe credibility gap.1 The platform's methodology focuses on broad activity windows that modern bots easily exploit, and its SEC disclosures lack the quantitative rigor found in peer filings.9

The resolution of this paradox will likely come from the legal discovery process in the RBX v. Spotify lawsuit, which has the potential to force the disclosure of internal bot-exclusion rates for the first time.15 If the alternative hypothesis is proven—that Spotify has willfully ignored metric inflation—the platform faces significant financial and reputational damages from both the investment and creator communities.

QUESTIONS

Regulatory Outlook

## Top 5 Unanswered Questions for Regulatory Subpoena

1. **Technical Log Discrepancy**
What is the quantified delta between "reported Ad-Supported MAUs" and "human-verified ad impressions" as recorded by third-party SIVT monitors like DoubleVerify across the entire platform?
2. **API Playback Breakdown**
What percentage of play requests originating from the ChatGPT and AI-integrated endpoints involve a verified human interaction versus an automated background agent?
3. **VPN Filtering Failure**
Why does Spotify's infrastructure allow millions of streams to be geomapped to residential regions with zero population, as alleged in the RBX complaint, and was this data ever presented to the Audit Committee?
4. **Incentive Alignment**
Is there any internal Spotify documentation discussing the negative impact that aggressive bot removal would have on the platform's P/E ratio and stock valuation?
5. **Royalty Recapture**
When Spotify removes "tens of thousands of songs" due to bot activity (as with the Boomy incident), where are the recaptured royalties re-allocated, and why is this process not disclosed to rights holders in the monthly statements?79

WORKS CITED

## Works Cited

1. Spotify Technology S.A. - Cloudfront.net, accessed March 19, 2026. [cloudfront.net](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001639920/55ed6eb9-217c-44f2-bac5-1d58f79782e1.pdf)
2. Spotify Reports Fourth Quarter 2025 Earnings, accessed March 19, 2026. [newsroom.spotify.com](https://newsroom.spotify.com/2026-02-10/spotify-q4-2025-earnings/)
3. Spotify goes public – an economic background analysis - Music Business Research, accessed March 19, 2026. [musicbusinessresearch.wordpress.com](https://musicbusinessresearch.wordpress.com/2018/04/03/spotify-goes-public-an-economic-background-analysis/)
4. Spotify Technology (SPOT) - Trefis, accessed March 19, 2026. [trefis.com](https://www.trefis.com/data/companies/SPOT)
5. 2025 Imperva Bad Bots Report, accessed March 19, 2026. [exclusive-networks.com](https://pages.insights.exclusive-networks.com/2025-imperva-bad-bots-report?hsLang=en)
6. 2025-Bad-Bot-Report.pdf - Thales CPL, accessed March 19, 2026. [thalesgroup.com](https://cpl.thalesgroup.com/sites/default/files/content/campaigns/badbot/2025-Bad-Bot-Report.pdf)
7. Understand your analytics - Apple Music for Artists, accessed March 19, 2026. [artists.apple.com](https://artists.apple.com/support/1105-understand-your-analytics)
8. RBX Suit Claims Drake's Streaming Data Demonstrates Fraudulent Streams, accessed March 19, 2026. [americanbar.org](https://www.americanbar.org/groups/young_lawyers/resources/tyl/practice-areas/rbx-suit-drakes-streaming-data-demonstrates-fraudulent-streams/)
9. meta-20231231 - SEC.gov, accessed March 19, 2026. [sec.gov](https://www.sec.gov/Archives/edgar/data/1326801/000132680124000012/meta-20231231.htm)
10. Twitter Update - Bireme Capital, accessed March 19, 2026. [biremecapital.com](https://www.biremecapital.com/blog/twitter-update)
11. Filed pursuant to Rule 424(b)(4) - SEC.gov, accessed March 19, 2026. [sec.gov](https://www.sec.gov/Archives/edgar/data/1326801/000119312512240111/d287954d424b4.htm)
12. 3.1 Management's Discussion and Analysis | DART – Deloitte, accessed March 19, 2026. [dart.deloitte.com](https://dart.deloitte.com/USDART/home/publications/deloitte/additional-deloitte-guidance/roadmap-sec-comment-letter-considerations/chapter-3-sec-disclosure-topics/3-1-management-s-discussion-analysis)
13. Recent SEC Emphasis on KPIs and Other Metrics - FinancialReportingHub, accessed March 19, 2026. [financialreportinghub.org](https://www.financialreportinghub.org/article/recent-sec-emphasis-on-kpis-and-other-metrics)
14. Spotify-20-F-Filing.pdf, accessed March 19, 2026. [q4cdn.com](https://s29.q4cdn.com/175625835/files/doc_financials/2025/q4/Spotify-20-F-Filing.pdf)
15. The Legal Beat: RAPPER RBX'S CLASS ACTION AGAINST SPOTIFY, accessed March 19, 2026. [musicconnection.com](https://www.musicconnection.com/the-legal-beat-rapper-rbxs-class-action-against-spotify/)
16. FOI 3490 - Digital Platform Services Inquiry 2020–2025 - The Treasury, accessed March 19, 2026. [treasury.gov.au](https://treasury.gov.au/sites/default/files/2023-12/foi-3490.pdf)
17. Q4 2024 Update, accessed March 19, 2026. [q4cdn.com](https://s29.q4cdn.com/175625835/files/doc_financials/2024/q4/Q4-2024-Shareholder-Deck-FINAL.pdf)
18. Q4 2025 Update, accessed March 19, 2026. [q4cdn.com](https://s29.q4cdn.com/175625835/files/doc_financials/2025/q4/Q4-2025-Shareholder-Deck-FINAL.pdf)
19. Spotify Q4 2025 users, profits and cash surge | SPOT SEC Filing - Stock Titan, accessed March 19, 2026. [stocktitan.net](https://www.stocktitan.net/sec-filings/SPOT/6-k-spotify-technology-s-a-current-report-foreign-issuer-6db479a7ff07.html)
20. Managing the personalization paradox: Lessons from Spotify's AI DJ - SMU, accessed March 19, 2026. [smu.edu.sg](https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=8800&context=lkcsb_research)
21. Spotify Statistics 2026 - SoundCampaign, accessed March 19, 2026. [soundcamps.com](https://soundcamps.com/blog/spotify-statistics/)
22. SEC.gov 99.1 filing, accessed March 19, 2026. [sec.gov](https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm)
23. Qualified Views Vs Total Views On Tiktok (2025), accessed March 19, 2026. [shortimize.com](https://www.shortimize.com/blog/qualified-views-vs-total-views)
24. How Does TikTok Count Views? | AdManage.ai Blog, accessed March 19, 2026. [admanage.ai](https://admanage.ai/blog/how-does-tiktok-count-views)
25. Critics, Media Ratings Council at odds over solution to invalid ad traffic | Marketing Dive, accessed March 19, 2026. [marketingdive.com](https://www.marketingdive.com/news/critics-media-ratings-council-at-odds-over-solution-to-invalid-ad-traffic/412185/)
26. FORM 20-F (2023), accessed March 19, 2026. [q4cdn.com](https://s29.q4cdn.com/175625835/files/doc_financials/2023/ar/26aaaf29-7cd9-4a5d-ab1f-b06277f5f2a5.pdf)
27. Limitations of Nonfinancial Metrics Reported by Social Media Companies - CSUSB, accessed March 19, 2026. [csusb.edu](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1074&context=jitim)
28. Facebook Provides New Detail on Fake Accounts - Social Media Today, accessed March 19, 2026. [socialmediatoday.com](https://www.socialmediatoday.com/news/facebook-provides-new-detail-on-the-prevalence-of-fake-accounts-on-its-plat/555480/)
29. Twitter v. Musk: Explaining the Case that Broke the Internet - Equal Justice Project, accessed March 19, 2026. [equaljusticeproject.co.nz](https://www.equaljusticeproject.co.nz/articles/twitter-v-musk-explaining-the-case-that-broke-the-internet2022)
30. 17 CFR § 229.303 - Item 303 - Law.Cornell.Edu, accessed March 19, 2026. [law.cornell.edu](https://www.law.cornell.edu/cfr/text/17/229.303)
31. SEC Issues New Guidance on KPIs and Metrics in MD&A | Wilson Sonsini, accessed March 19, 2026. [wsgr.com](https://www.wsgr.com/en/insights/sec-issues-new-guidance-on-the-use-of-kpis-and-metrics-in-mdanda-and-proposes-amendments-to-financial-disclosures.html)
32. Twitter v. Musk: The "Trial of the Century" That Wasn't - Columbia Law, accessed March 19, 2026. [columbia.edu](https://scholarship.law.columbia.edu/cgi/viewcontent.cgi?article=4923&context=faculty_scholarship)
33. DoubleVerify Expands Invalid Traffic and Viewability Measurement to Spotify Video Ads, accessed March 19, 2026. [doubleverify.com](https://doubleverify.com/company/newsroom/doubleverify-expands-invalid-traffic-and-viewability-measurement-to-spotify-video-ads-continuing-to-lead-industry-in-independent-platform-measurement)
34. A Complete Guide to Invalid Traffic – Spider Ad Fraud, accessed March 19, 2026. [spideraf.com](https://spideraf.com/articles/types-of-invalid-traffic-and-prevention)
35. Minimum Standards for Media Rating Research | MRC, accessed March 19, 2026. [mediaratingcouncil.org](https://www.mediaratingcouncil.org/standards-and-guidelines)
36. MRC IVT 2.0 Status Report - Media Rating Council, accessed March 19, 2026. [mediaratingcouncil.org](https://mediaratingcouncil.org/sites/default/files/News/Accreditation-Matters/MRC%20IVT%202.0%20Status%20Report%20on%20Accredited%20Vendors.pdf)
37. Report: $63bn lost to IVT across digital advertising in 2025 | Advanced Television, accessed March 19, 2026. [advanced-television.com](https://www.advanced-television.com/2026/01/21/report-63bn-lost-to-ivt-across-digital-advertising-in-2025/)
38. Spotify Faces Class Action Over Alleged Fake Streams - LawCommentary, accessed March 19, 2026. [lawcommentary.com](https://www.lawcommentary.com/articles/spotify-faces-class-action-over-alleged-fake-streams-that-deprived-artists-of-royalties)
39. The Drake case and 'fraudulent streams' - El País, accessed March 19, 2026. [elpais.com](https://english.elpais.com/culture/2025-11-26/the-drake-case-and-fraudulent-streams-what-the-spotify-lawsuit-reveals-about-the-music-business.html)
40. Earnings call: Spotify beats subscriber forecasts, misses on MAU growth - Investing.com, accessed March 19, 2026. [investing.com](https://uk.investing.com/news/stock-market-news/earnings-call-spotify-beats-subscriber-forecasts-misses-on-mau-growth-93CH-3607601)
41. RBX, a founding father of West Coast Hip-Hop, Files a Class Action Lawsuit Against Spotify - Baron & Budd, accessed March 19, 2026. [baronandbudd.com](https://baronandbudd.com/news/rbx-a-founding-father-of-west-coast-hip-hop-files-a-class-action-lawsuit-against-spotify-concerning-alleged-streaming-fraud/)
42. Spotify's streaming fraud initiatives are "nothing more than window dressing" says rapper RBX - CMU, accessed March 19, 2026. [completemusicupdate.com](https://completemusicupdate.com/spotifys-streaming-fraud-initiatives-are-nothing-more-than-window-dressing-says-rapper-rbx-as-he-files-class-action-lawsuit/)
43. Collins v. Spotify USA Inc. et al - ClassAction.org, accessed March 19, 2026. [classaction.org](https://www.classaction.org/media/collins-v-spotify-usa-inc-et-al-complaint.pdf)
44. YouTube — Statistics & Facts 2026 - Business Stats, accessed March 19, 2026. [businesstats.com](https://businesstats.com/youtube-statistics/)
45. APIs Become Primary Target for Cybercriminals - Imperva, accessed March 19, 2026. [imperva.com](https://www.imperva.com/company/press_releases/apis-become-primary-target-for-cybercriminals-over-40000-api-incidents-in-first-half-of-2025/)
46. WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents - ResearchGate, accessed March 19, 2026. [researchgate.net](https://www.researchgate.net/publication/396418425_WebCloak_Characterizing_and_Mitigating_Threats_from_LLM-Driven_Web_Agents_as_Intelligent_Scrapers)
47. What is royalty revenue recognition? - Stripe, accessed March 19, 2026. [stripe.com](https://stripe.com/gb/resources/more/what-is-royalty-revenue-recognition-a-guide-to-royalty-revenue-counting)
48. Before the UNITED STATES COPYRIGHT ROYALTY JUDGES - CRB.gov, accessed March 19, 2026. [crb.gov](https://www.crb.gov/rate/16-CRB-0003-PR/rebuttals/spotify-tab-02-proposed-rates-and-terms.pdf)
49. How Fake Viewers Undermine Marketing on Streaming Platforms - Streams Charts, accessed March 19, 2026. [escharts.com](https://cdn.escharts.com/media/whitepaper/Streams-Charts_Audiencly_The-Hidden-Cost-of-Viewbotting_WP.pdf)
50. fb-20201231 - SEC.gov, accessed March 19, 2026. [sec.gov](https://www.sec.gov/Archives/edgar/data/1326801/000132680121000014/fb-20201231.htm)
51. Twitter v. Musk: Plaintiff's Response to Defendant's Counterclaim - Harvard Law, accessed March 19, 2026. [harvard.edu](https://corpgov.law.harvard.edu/2022/08/10/twitter-v-musk-plaintiffs-response-to-defendants-counterclaim/)
52. Spotify Sued Over "Billions" of Fraudulent Drake Streams - Consequence, accessed March 19, 2026. [consequence.net](https://consequence.net/2025/11/spotify-lawsuit-drake-streams/)

Built with

bearbrown.co

· AI tools for educators, creators & founders
