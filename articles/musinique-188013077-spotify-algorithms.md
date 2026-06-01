---
title: "Spotify Algorithms"
subtitle: ""
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: "188013077.spotify-algorithms"
post_date: "2026-02-15T05:33:39.966Z"
is_published: "true"
source_zip: "Y0r_0oGOSoWMD3iEcEhVnA.zip"
source_html: "posts/188013077.spotify-algorithms.html"
source_file: "musinique-188013077-spotify-algorithms.md"
cover_image: "https://substack-post-media.s3.amazonaws.com/public/images/47f764dc-832a-42e0-8ca8-47e0198e3741_500x500.jpeg"
---
![](https://substack-post-media.s3.amazonaws.com/public/images/47f764dc-832a-42e0-8ca8-47e0198e3741_500x500.jpeg)

## Part 1: Chapter-by-Chapter Logical Mapping

---

### Chapter 1: Introduction

**Core Claim**: Spotify’s algorithm can be understood and leveraged systematically through data-driven experimentation, not insider knowledge.

**Supporting Evidence**:

- Author’s investment: “tens of thousands of dollars into education, testing marketing services”
- Scale of testing: “well over a million dollars in music marketing budgets” through clients
- Track record: “almost every song I’ve released in the past three years onto Discover Weekly”

**Logical Method**: Empirical induction from repeated experimentation. Southworth positions himself as a practitioner-researcher who derived patterns from testing rather than theory.

**Gaps/Assumptions**:

- No verification of whether his methods work for artists in different genres or at different scales
- Assumes correlation between his promotional tactics and algorithmic placement equals causation
- “Almost every song” implies some failures, but these aren’t examined

**Argumentative Structure**: Establishes ethos through credentials and financial stakes, then promises demystification of a “black box” through practical knowledge.

---

### Chapter 2: The Algorithm (Three-Tier System)

**Core Claim**: Spotify’s algorithm operates through three distinct but interconnected systems: collaborative filtering (primary), web crawling (secondary), and audio analysis (tertiary for new releases).

**Supporting Evidence**:

- Direct observation: “I watched hours of content from Spotify developer conferences”
- Theoretical framework borrowed from information retrieval systems (Google analogy)
- Testing validation: “I tested my own theories... with Facebook ad campaigns and Spotify playlist promotions”

**Logical Method**: Deductive reasoning from known systems (collaborative filtering in recommendation engines, web crawling for search) applied to observed Spotify behavior.

**Collaborative Filtering Evidence Chain**:

1. Premise: If 100 people save Song A, and 10 of those also save Song B
2. Observed pattern: Song B gets recommended to the other 90
3. Inference: Spotify correlates user behavior across the platform
4. Tracks: saves, skips, full listens, playlist additions, artist follows, repeat listens

**Web Crawling Logic**:

- Analogy to Google search indexing
- Mechanism: Spotify crawls internet for artist mentions, blog coverage, associations
- Function: Influences “related artists” and potentially algorithmic playlists
- **Critical limitation**: Southworth labels this “more speculative” - honest acknowledgment of uncertainty

**Audio Analysis**:

- Technical fact: Spotify analyzes waveforms for key, tempo, acousticness, danceability
- Claimed use case: Placing major artist releases before collaborative filtering data accumulates
- **Key assertion without proof**: “This audio analysis does not seem to influence smaller artists”
- Reasoning: Plausible (Spotify needs user engagement data for unknowns), but untested

**Gaps**:

- No direct access to Spotify’s actual code or decision trees
- Web crawling impact is speculative (”a little bit of a black box”)
- Audio analysis claims based on inference from Spotify’s stated purposes, not observed outcomes
- Assumes three-tier model is complete; no consideration of other potential factors (label relationships, genre quotas, temporal trends)

**Strength**: Clear mechanical descriptions that avoid mystification. Each tier has a logical purpose in a recommendation system.

---

### Chapter 3: Algorithmic Playlists

**Core Claim**: Algorithmic playlists (especially Release Radar and Discover Weekly) drive one-third of all Spotify streams and operate on quantifiable thresholds.

**Supporting Evidence**:

- **Release Radar mechanics**: Songs from followed artists appear for 4 weeks; high-performing songs get placed on Release Radar for non-followers
- **Threshold claim**: “Songs tend to get algorithmic release radar pushes when the popularity index of a song is about 20%”
- **Study cited**: “I ran a study with data from 300 songs with a data analyst”Average to hit 20% popularity: 2,503 streams, 993 listeners, 375 saves in weeks 1-3
- **Discover Weekly threshold**: ~30% popularity indexAverage: 9,217 streams, 4,097 listeners, 447 saves

**Logical Chain**:

1. Observation: Songs hitting certain metrics consistently get playlist placement
2. Data collection: 300-song sample with analyst
3. Statistical pattern: Average thresholds emerge
4. Predictive model: Hit these numbers → expect placement

**Critical Gaps**:

- **Sample bias not addressed**: Were these 300 songs all from similar genres? Similar promotional methods? The author’s own clients?
- **Outliers acknowledged but unexplained**: “There were definitely outliers” - no analysis of what differentiates success vs. failure at similar metrics
- **Correlation vs. causation**: Does hitting the threshold *cause* placement, or are both effects of underlying quality signals?
- **Save rate mentioned as additional factor**: “I’ve seen several people hit all of these metrics above, but their save rate... was very low, and they never got on Discover Weekly”This undermines the sufficiency of the numeric thresholdsSuggests additional unmeasured factors

**Discover Weekly specific mechanism**:

- Save button + “don’t show me more music from this artist” button = explicit user voting
- Implication: Spotify uses negative feedback to refine recommendations
- But: No data on how negative votes affect future placement

**Strength**: Quantified targets give artists concrete goals. The 300-song study provides empirical grounding (though methodology isn’t detailed).

**Weakness**: Averages can mislead. If the distribution is bimodal or heavily skewed, the average may not represent typical experience.

---

### Chapter 4: The Most Important Metrics

**Core Claim**: Four metrics determine algorithmic success: save rate (saves/listeners), repeat listen rate (streams/listeners), playlist adds, and follower growth. High performance across these signals quality to Spotify’s algorithm.

**Supporting Evidence**:

- **Direct from Spotify**: List of “critical algorithmic signals” tracking user behavior (album checks, profile views, listen duration, skips, saves, playlist adds, repeat listens, multi-day listening)
- **Author’s hierarchy of importance**:**Save rate**: Target >40% in week 1 for algorithmic leverage; >10% sustainable on playlists**Repeat listen rate**: Target >2, preferably 3-4 (streams per listener)**Playlist adds**: Raw count of user playlists containing the song**Follower growth**: During promotional window

**Logical Foundation**:

- **Quality inference model**: If users save, repeat, and playlist a song, they value it highly
- **Algorithmic mirror**: Spotify’s algorithm should replicate human quality judgments
- **Inverse validation**: Low engagement (one listen, no save, no follow) signals low interest

**The Time Factor**:

- **Critical window**: First few days, especially first week after release
- **Mechanism**: “If you can create a large spike in streams during the first week... much higher than is expected for an artist of your current size... you have a high chance of getting added to a large selection of release radar playlists”
- **Cascade effect**: Release Radar boost → Discover Weekly → months/years of streaming
- **Analogy to artist behavior**: Major artists build TikTok hype pre-release to create “massive splash” on day 1

**Pre-Saves Don’t Exist (Critical Revelation)**:

- **Mechanism exposed**: Pre-save services (Hypedit, Feature FM, etc.) store user credentials and song URI, then use Spotify API on release day to auto-save
- **Key fact**: “Spotify does not see those pre-saves”
- **Exception**: If you tell Spotify directly (online pitching tool or industry meetings)
- **Implication**: Pre-save campaigns create day-1 save spikes (helpful due to time factor) but aren’t seen as “pre-release demand” by algorithm
- **User friction**: Pre-save requires scary-looking permissions, reducing conversion

**Logical Gaps**:

- **Percentages lack context**: Is 40% save rate achievable for all genres? Does ambient music have lower save rates than pop?
- **Self-selection bias**: Artists who hire Southworth may already have higher-quality music or better fanbases
- **Conflation of metrics**: Save rate >40% AND repeat listen rate >2 AND high streams - are all necessary, or can one compensate for another?
- **Pre-save timing advantage**: He claims day-1 spike helps, but earlier said Spotify doesn’t see pre-saves. The mechanism is: spike happens on day 1 (good) but it’s not differentiated from organic saves (unclear if this matters)

**Strength**: Metrics are measurable in Spotify for Artists, giving readers actionable tracking. The pre-save revelation is valuable skepticism of common industry practices.

---

### Chapter 5: Leverage the Metrics (Three Promotion Styles)

**Core Claim**: Playlist promotion is the worst method despite industry hype; organic social media is powerful but slow; Facebook/Instagram ads are optimal for hitting critical metrics.

---

#### Playlist Promotion Analysis

**The Three Methods**:

1. **Get Banned Way**: Pay for placement (against Spotify TOS)
2. **Bad Way**: Hire pitching companies that guarantee follower counts (often botted or pay-to-play networks)
3. **Best Way**: Organic outreach via SubmitHub/Groover, where curators can decline

**Core Indictment**: “By itself playlist promotion is the worst form of promotion out there”

**Evidence for Failure**:

- **Passive listening behavior**: “People often click play in a playlist and go about their day very rarely looking at what song is playing”
- **Metric performance**: “Horrible save rates, horrible repeat listen rates, high skip rates”Save rates typically 5% even on Spotify editorial playlistsPlaylist add rates “just as bad”Follower rates “practically zero”
- **Temporary effect**: “When the sentence [song] kicked off the playlist, your monthly listeners go back down to where you started”
- **Long-term harm**: “Some artists are paying hundreds or thousands of dollars to get onto the playlist that are actively hurting their chances of long term growth”Mechanism: Poor metrics train Spotify’s algorithm incorrectly

**Logical Chain**:

1. Playlists generate passive listeners
2. Passive listeners don’t engage (save, follow, repeat)
3. Poor engagement signals low quality to algorithm
4. Algorithm deprioritizes the song
5. Artist is worse off than before promotion

**Gap in Logic**:

- **Not all playlists are equal**: Curated genre-specific playlists with engaged followers should perform better than generic mood playlists
- **Author acknowledges this**: “Your song will only get added to the playlist if it is genuinely a good fit” (for SubmitHub/Groover method)
- **Contradiction**: If the song is a good fit and listeners chose that playlist genre, why wouldn’t they engage?
- **Possible explanation**: Even genre-matched listeners are passive in playlist context vs. active search
- **Alternative theory not considered**: Maybe playlist promotion works fine, but *paid* playlist promotion attracts low-quality curators

**Best Use Case**: “Playlist promotion is best used as a supplement to other more high quality marketing methods”

---

#### Organic/Social Media Promotion

**Core Mechanism**: High-volume content creation → inbound traffic from interested users → engaged listeners

**Logic**:

- Each piece of content = “hook in the ocean”
- Followers gained through value provision (entertainment, education, connection)
- Followers are pre-qualified: “If someone is following your Instagram account because you made awesome content around your music they probably enjoy your music”
- Result: When you post new song, they save, repeat listen, playlist add, follow profile

**Metric Performance**: Hits all critical metrics because traffic is intentional, not accidental

**Content Strategy**:

- **Reframe as “documenting”**: Record during creation sessions
- **Content reutilization**: One long-form session → 30-80 short-form posts
- **Platform focus**: Dominate 1 platform + 1-2 secondary (don’t spread thin across 15)
- **Commitment**: 6-12 months on chosen platform before evaluating

**Trade-offs**:

- **Cost**: Free (in money) but expensive (in time)
- **Timeline**: “Powerful but it takes a ton of work in a long time”
- **Scalability**: Can’t buy your way to faster results

**Gaps**:

- **No data on conversion rates**: What percentage of social followers actually stream music?
- **Platform decay not addressed**: Algorithm changes can destroy reach overnight
- **Genre bias**: Visual/personality-driven genres (pop, hip-hop) may outperform cerebral genres (ambient, classical)
- **Time horizon undefined**: How long until you see meaningful results?

**Honest acknowledgment**: “Social media platforms are constantly changing so it’s impossible for me to recommend what you should use otherwise it’ll be out of date before I even publish this book”

---

#### Facebook/Instagram Ads (The Crown Jewel)

**Core Claim**: “Facebook and Instagram ads... are the crown jewel of music marketing in my opinion”

**Why Ads Solve the Metric Problem**:

- **Precision targeting**: Show ads to people interested in similar artists, specific age ranges, Spotify users in countries where platform is available
- **Self-selection**: “The person wouldn’t have clicked your ad if they weren’t interested already”
- **Result**: “You’re able to hit every single one of the most important metrics to the Spotify algorithm because you can drive the right person to your song”

**Contrast with Playlists**:

- Playlist = passive, forced exposure
- Ad click = active choice, indicating interest

**Campaign Structure**:

1. **Research Phase**:Identify similar artists (ask friends, check Spotify related artists, test Facebook targeting availability)Map genre, sub-genres, festivals, blogsFind intersection of “sounds like” and “targetable on Facebook”
2. **Conversion Campaign Setup**:Use landing page (Hypedit, Feature FM, Tondon) with Facebook pixelOptimization: Facebook learns who converts, avoids bots/accidental clicksStructure: 3-5 ad sets (different audiences) × 3-5 ads (different creatives) = testing matrix**Campaign Budget Optimization**: Facebook spends most on cheapest-converting combination
3. **Analysis (Critical Window: First 48 Hours)**:**Benchmark ratio**: 100 conversions → 100-150 streams, 50+ listeners, 25+ savesLanding page click-through rate should exceed 50%Don’t touch campaigns during “learning phase” (first 48 hours)After learning: Turn off expensive ad sets, double down on winners

**Cost Structure Not Provided**:

- No specific cost-per-conversion targets
- No budget recommendations for different artist sizes
- Case study later shows $300 budget over 4 weeks, but scaling unclear

**Logical Gaps**:

- **Attribution uncertainty**: How do you know the ad caused the engagement vs. the quality of the song?Counter: A/B testing across campaigns would isolate this, but not discussed
- **Genre ceiling**: Do Facebook ads work equally for all genres, or just EDM/pop (author’s background)?
- **Competition dynamics**: As more artists use this method, does cost-per-conversion rise?
- **Algorithm changes**: Facebook’s ad platform “changing like every month or two” creates instability

**Strength**: Testable, measurable, actionable. The conversion benchmarks give clear success criteria.

---

### Chapter 6: Spotify Profits (ROI Defense)

**Core Claim**: Judging Spotify promotion by immediate streaming revenue alone is “stupid logic” that ignores long-term value creation.

**The Math People Get Wrong**:

- Surface view: $1,000 spent → 29,000 streams → $100 revenue = 90% loss
- **Missing assets created**:7,000 listeners2,500 saves1,200 playlist adds400 Spotify followers400 Instagram followers5,000 YouTube views166 YouTube subscribers

**Long-Term Value Arguments**:

1. **Recurring Passive Income**: “Every month I get 60,000 streams from my saves and playlist ads for free”Mechanism: Saves persist in libraries; playlist adds generate ongoing streamsLifespan: Years potentially
2. **Compounding Reach**: Followers mean future releases start with built-in audience (no cost)
3. **Conversion Funnel**: “Your music is a gateway drug to your brand”Streaming → email list → merch sales → show attendance“For most artists, this is where the real value of streaming comes from”
4. **Algorithmic Momentum**: Strong initial metrics → algorithmic playlists → sustained streaming**Proof point**: Song doubled from 29,000 to 64,000 streams “with no additional promotion” in 2 monthsProjection: “A year from now, this song will have over 100,000 streams”
5. **Customer Acquisition Cost**: “There has never been an easier time in human history to get a stranger to listen to your song”Streaming removes financial barrier for listenerCompare to pre-Spotify: listener had to purchase to hear

**The Business Case**:

- “Why bother investing so much money in the creation of your music if you aren’t going to bother promoting it?”
- “The marketing budget should always be higher than the creation budget unless you’re doing this as a hobby”
- **Harsh reality**: “Most businesses are not immediately profitable and most businesses fail. The music industry is a hostile place... most people that try will fail.”

**Logical Gaps**:

- **Survivorship bias**: Is he showing a successful example while most campaigns fail?He addresses this: “While this campaign profited, most songs will not profit”But then why spend $1,000 if most don’t profit? The long-term value argument must carry weight
- **Uncertain conversion rates**: What percentage of Spotify listeners actually join email lists, buy merch, attend shows?No data provided“These numbers are hard to assign a dollar amount to” - acknowledges valuation difficulty
- **Genre/artist variability**: Does ambient music with 100,000 streams convert to show attendance as well as pop/EDM?
- **Time value of money not considered**: $1,000 now vs. $100/month for years - what’s the breakeven timeline?
- **Opportunity cost**: Could that $1,000 generate more value elsewhere (different marketing, better production, etc.)?

**Strength**: Reframes success metrics beyond immediate ROI. The compounding value of saves/playlist adds is a strong empirical observation.

**Weakness**: No comparative analysis. Is $1,000 on Facebook ads better than $1,000 on touring, PR, sync licensing pursuit, etc.?

---

### Chapter 7: Case Study - “Socialize”

**Release**: May 7, 2020
**Budget**: $300 over first 4 weeks ($20/day initially)
**Current Streams**: 500,000+
**Revenue**: ~$1,100 from Spotify alone

**Week 1 Performance**:

- Save rate: >60%
- Repeat listen rate: 3x
- Result: Release Radar placement (Friday after release)

**Cascade Effect**:

- Release Radar → surge in streams
- Maintained high metrics → Discover Weekly placement (Monday)
- **Visual pattern**: Spikes every Friday (Release Radar) and Monday (Discover Weekly) for months
- Gradual decay but periodic algorithmic boosts throughout year

**Profitability Analysis**:

- $300 spent → $1,100+ earned = 267% ROI (best case)
- Worst case (assuming $2/1000 streams): $1,000 revenue = 233% ROI
- **But**: “This song is still climbing in streams every day”
- Doesn’t include Apple Music, YouTube, or fan conversion value

**Key Causal Chain**:

1. Facebook ads → targeted, interested listeners
2. High save rate (60%) + high repeat rate (3x) in week 1
3. Algorithm recognizes quality signal
4. Release Radar placement
5. Maintains metrics during Release Radar
6. Discover Weekly placement
7. Months of sustained algorithmic activity

**Gaps**:

- **Song quality not mentioned**: Was “Socialize” just a better song than his previous releases?
- **Promotion timing**: Did he also do social media content? Other marketing?
- **Genre advantage**: EDM/electronic may perform better on Spotify algorithms than other genres
- **Network effects**: As an established YouTube creator, did he have built-in audience advantages?
- **Selection bias**: This is a success story. How many campaigns *didn’t* work?He admits: “Most songs will not profit”So why feature this one? Because it’s instructive, or because it’s rare?

**Honest caveats buried**:

- “The point of marketing your music on Spotify shouldn’t be to profit financially, especially not in the short term”
- This contradicts the profitability framing but is more realistic

**What the case study*****doesn’t*****show**:

- Comparative analysis: What would have happened with playlist promotion only? Or no promotion?
- Specific ad creative details: What did the ads look like? What messaging worked?
- Learning curve: How many failed campaigns preceded this success?

**Strength**: Concrete data, clear timeline, documented outcomes. The graph of spikes aligning with playlist update days validates the algorithmic mechanism.

---

### Chapter 8: Learn More (Product Offerings)

Southworth lists his products/services:

1. **Spotify Growth Machine** (course): Facebook conversion campaign setup
2. **Consulting**: 1-hour Zoom calls ($?)
3. **YouTube Growth Machine** (course): Organic + Google ads
4. **Ad Management Services**: Agency model
5. **Music Funnels**: All-in-one website/email platform
6. **Fan Growth Machine** (upcoming course): Website, store, funnels, email list

**Critique from ISE Perspective**:

- This chapter is pure sales funnel, not analysis
- No pricing transparency (intentional to drive traffic to website)
- The book itself is lead generation for higher-ticket offerings
- **Conflict of interest**: Does his consulting bias his advice toward tactics that require ongoing support?

**However**:

- Transparency about motives: “I don’t want this to turn into too much of a sales pitch, but...”
- Acknowledges free community option
- The advice in previous chapters stands on its own merits (testable, data-driven)

---

## Bridge Section: Synthesizing the Logical Architecture

### The Three-Layer Argument Structure

**Foundation (Chapters 2-3)**: Spotify’s algorithm is knowable

- Layer 1: Collaborative filtering (behavioral data)
- Layer 2: Web crawling (external signals)
- Layer 3: Audio analysis (content features)
- Algorithmic playlists operate on quantifiable thresholds

**Mechanism (Chapters 4-5)**: Success requires optimizing specific metrics

- Save rate, repeat listen rate, playlist adds, follower growth
- Time window matters (week 1 is critical)
- Promotional method determines metric performance:Playlists: Passive listeners → poor metrics → algorithmic harmOrganic social: Engaged followers → strong metrics → slow growthFacebook ads: Targeted clicks → strong metrics → scalable growth

**Economics (Chapters 6-7)**: Value creation transcends immediate ROI

- Streaming revenue is lagging indicator
- True value in: algorithmic momentum, audience building, conversion funnel
- Profitability possible but not primary goal
- Most campaigns won’t profit directly

### Logical Consistency Across Chapters

**Coherent through-line**:

1. Algorithm can be reverse-engineered (Ch 2-3)
2. Specific metrics trigger algorithmic rewards (Ch 4)
3. Different promotion methods produce different metric patterns (Ch 5)
4. Method choice determines algorithmic outcome
5. Facebook ads uniquely solve the metric optimization problem (Ch 5)
6. Long-term value justifies short-term investment (Ch 6)
7. Case study validates the model (Ch 7)

**Internal Tensions**:

1. **Correlation vs. Causation**:Southworth claims hitting metric thresholds causes playlist placementBut acknowledges outliers who hit thresholds and failAlternative: Metrics and placement are both effects of underlying song qualityResolution: Partial causation - quality is necessary, but metrics *amplify* algorithmic response
2. **“Most songs will not profit” vs. “This is the best method”**:If most fail to profit, why recommend expensive ad campaigns?Resolution: Goal isn’t profit but audience building (but this contradicts emphasis on profitability in Ch 7)Charitable reading: Southworth redefines success away from immediate ROI, but messaging is inconsistent
3. **Pre-saves “don’t exist” vs. “day-1 spike matters”**:Spotify doesn’t see pre-saves, but day-1 save volume mattersSo pre-save campaigns do work, just differently than advertisedThe mechanism is: artificial day-1 spike (via API automation) mimics organic hypeThis is logically consistent but undermines the “pre-saves don’t exist” framing
4. **Collaborative filtering requires data, but audio analysis doesn’t help small artists**:Spotify can analyze small artist songs but allegedly doesn’t use it for placementWhy not? Resource constraints? Quality filtering?Southworth speculates it’s because they “just won’t put you on a playlist... purely on audio analysis”This is an assertion without proof - audio analysis *could* influence algorithmic radio or related artist placement

### Gaps in the Overall Argument

**What’s Missing**:

1. **Genre Effects**:Southworth’s background is EDM/electronicDo these methods work for folk, classical, jazz, hip-hop?Save rates, repeat rates, and ad costs likely vary by genreNo data on genre-specific performance
2. **Scale Effects**:Does this work for artists with 0 followers? Or only those with existing fanbases?The case study song benefited from his YouTube following (likely)Cold-start problem not addressed
3. **Competitive Dynamics**:If everyone follows this playbook, costs rise and effectiveness fallsNo discussion of market saturationFacebook ad costs have risen dramatically since 2020 (when case study ran)
4. **Platform Risk**:Entire strategy depends on Facebook ads remaining effective and affordableAlgorithm changes (Facebook or Spotify) could invalidate approachNo backup strategy if Facebook bans music ads or costs spike
5. **Quality Floor**:Does this work for objectively bad music?Southworth assumes song quality is sufficient to convert interested listenersWhat if save rates are low because the song isn’t good, not because listeners are passive?No discussion of product-market fit or quality thresholds
6. **Methodology Transparency**:The 300-song study is cited but not detailedWho was the data analyst? What was the methodology?Were there controls? How were genres distributed?Lack of peer review or replication
7. **Counterfactual Thinking**:No A/B tests comparing promotion methods head-to-head“Socialize” case study has no control (what would have happened with no ads?)Playlist promotion critique may be strawman (comparing worst playlists to best ads)

### What Southworth Gets Right

**Empirical Grounding**:

- Uses real data (Spotify for Artists metrics)
- Tests theories with money at stake (skin in the game)
- Acknowledges uncertainty (”more speculative,” “my best guess”)
- Updates beliefs based on evidence (pre-saves revelation)

**Practical Actionability**:

- Metrics are trackable by any artist
- Thresholds give concrete targets
- Ad platform instructions are specific
- Honest about time/money costs

**Systems Thinking**:

- Recognizes interconnected metrics (save rate affects Discover Weekly)
- Understands time dynamics (week 1 matters more)
- Sees second-order effects (saves → ongoing streams)
- Frames promotion as investment, not expense

**Intellectual Honesty**:

- Admits most songs won’t profit
- Acknowledges platform changes constantly
- Disclaims insider knowledge
- Shows failed predictions (thought playlists were key, learned they weren’t)

### What Requires Skepticism

**Causation Claims**:

- Hitting metric thresholds *may* not cause playlist placement
- Both could be effects of underlying quality + luck
- Survivorship bias in case study selection

**Generalizability**:

- Sample of 300 songs (unstated composition)
- Author’s genre/network may not represent average artist
- Time period (2019-2023) may not predict future

**Economic Model**:

- Long-term value arguments rely on assumptions about conversion rates
- No data on email list growth, merch sales, show attendance correlation
- “Hard to assign dollar amounts” undermines ROI defense

**Platform Dependency**:

- Entire strategy hostage to Facebook and Spotify algorithm stability
- No hedge against platform risk
- Timing matters (was this easier in 2020 than 2025?)

---

## Part 2: Full Literary Review Essay

---

The numbers arrive with the force of revelation: 2,503 streams, 993 listeners, 375 saves. Hit these in your first week and Spotify’s algorithm will, with high probability, place your song on Release Radar for thousands of strangers. Miss them and your song vanishes into the platform’s 100-million-track catalog, accumulating streams at a rate measured in single digits per day. Andrew Southworth’s *Spotify Algorithms* makes a specific mathematical claim about how attention is allocated in the streaming economy, and the claim is either verifiable or it isn’t. The stakes are measurable: artists invest thousands of dollars promoting music that earns hundreds in return, justified by the belief that algorithmic placement will compensate over time through compounding passive income. Is this belief rational? Southworth argues yes, but his proof rests on a 300-song study he doesn’t fully detail and a case study that may not generalize. Still, the book succeeds where most music marketing advice fails - it provides testable hypotheses rather than vague platitudes.

Southworth positions himself as practitioner-researcher, not industry insider. He spent “tens of thousands of dollars” testing promotional methods and “well over a million dollars” managing client campaigns, seeking patterns in the black box of Spotify’s recommendation engine. His conclusions emerged from empirical observation: nearly every song he’s released in three years landed on Discover Weekly, a feat most artists never achieve. The methodology is inductive - run hundreds of campaigns, track which metrics precede algorithmic placement, formulate rules. It’s market research disguised as memoir, and the central finding is counterintuitive: playlist promotion, widely considered the holy grail of Spotify growth, actively harms long-term algorithmic performance.

The three-tier algorithm model Southworth proposes - collaborative filtering, web crawling, audio analysis - borrows familiar concepts from information retrieval systems. Collaborative filtering, the dominant mechanism, correlates user behavior: if 100 people save Song A and 10 also save Song B, Spotify recommends B to the other 90. Every action - saves, skips, full listens, playlist additions, repeat streams - feeds the system’s understanding of taste similarity. Web crawling searches for artist mentions across the internet, influencing related artist suggestions and potentially playlist placement, though Southworth admits this is “more speculative.” Audio analysis determines key, tempo, danceability, and other features, allegedly used to place major artist releases before sufficient behavioral data accumulates. For smaller artists, Southworth claims, audio analysis has minimal impact - Spotify won’t place you on algorithmic playlists based purely on sonic characteristics.

This model is mechanically plausible. Recommendation engines like Netflix and YouTube rely heavily on collaborative filtering. Google’s search algorithm crawls web content. Audio fingerprinting technology exists. But Southworth has no direct access to Spotify’s actual code or decision trees. He watched “hours of content from Spotify developer conferences,” read available documentation, and tested theories with ad campaigns. The three-tier framework could be incomplete or oversimplified. Label relationships, genre quotas, editorial override, anti-gaming measures - any of these could influence outcomes without his knowledge. He’s mapping the algorithm from outside, inferring mechanism from observed patterns. This doesn’t make him wrong, but it limits the confidence his quantitative claims can support.

The metric thresholds - 20% popularity index for Release Radar, 30% for Discover Weekly - come from “a study with data from 300 songs with a data analyst.” Who was the analyst? What was the sample composition? Were there genre controls? Southworth provides averages (2,503 streams, 993 listeners, 375 saves for 20% popularity) but not distributions. If the data are bimodal or heavily skewed, averages mislead. He acknowledges “outliers” who hit the numbers and still fail to get playlist placement, suggesting additional factors matter - save rate is mentioned as critical - but doesn’t provide a complete predictive model. The thresholds are useful heuristics, but they’re presented with more certainty than the evidence warrants. A 300-song sample isn’t trivial, but without methodology transparency, it’s hard to assess how much weight the findings can bear.

The book’s strongest section examines promotional methods through the lens of these metrics. Southworth draws a sharp distinction: playlist promotion generates passive listeners who rarely save songs or follow artists, resulting in “horrible save rates, horrible repeat listen rates, high skip rates.” These poor metrics signal low quality to Spotify’s algorithm, undermining future performance. The logic is clear - playlists force exposure on inattentive listeners, while Facebook ads deliver music to self-selected interested parties. Someone who clicks an ad for a song similar to artists they follow is making an active choice, and their subsequent behavior (saving, repeat listening, playlist addition) signals genuine interest. The algorithm rewards this pattern.

Here the argument becomes more than descriptive; it’s a theory of how attention markets function. Southworth claims that paying for playlist placement, even on legitimate playlists, creates a quality signal problem. Artists accumulate streams but not engaged listeners. When the song eventually drops off the playlist, monthly listeners crater back to baseline. Worse, the algorithm has learned the song generates passive, low-engagement streams, making it less likely to be placed on algorithmic playlists where sustained growth happens. By this logic, some promotion is worse than no promotion - it poisons the data Spotify uses to evaluate your music.

This is the book’s most provocative claim, and it requires examination. Southworth contrasts the worst of playlist promotion (botted networks, pay-to-play schemes) with the best of Facebook ads (precision targeting, conversion optimization). The comparison may be unfair. A genuinely curated genre-specific playlist with engaged followers should generate better metrics than a generic mood playlist or botted trash. Southworth acknowledges this when discussing SubmitHub and Groover - platforms where curators can decline songs, ensuring fit - but still concludes “even the best way of promoting your music with playlist still isn’t very good.” Why? Because “most people listening... are listening passively.”

This assertion deserves scrutiny. Are playlist listeners inherently passive, or does it depend on the playlist? A user who subscribes to “Deep Focus Ambient” and puts it on while working will skip rarely and engage little, even if they like what they hear. A user who curates “My Favorite Indie Rock 2025” and actively adds songs is highly engaged. Southworth treats all playlist listening as passive, which oversimplifies. The real issue may be that *paid* playlist promotion attracts low-quality curators with disengaged audiences. Organic playlist placement on well-curated lists could work fine. But Southworth’s experience with “every promotion company I could find” suggests the market for playlist promotion is dominated by scams and mediocrity.

The Facebook ad methodology receives the most detailed explanation. Southworth recommends conversion campaigns using landing pages with Facebook pixels, allowing the platform to optimize for serious interest while filtering bots and accidental clicks. The campaign structure - 3-5 ad sets with different targeting parameters, each containing 3-5 creative variations - lets Facebook’s algorithm identify the cheapest cost per conversion. An artist might target fans of three different EDM artists across three ad sets, then test verse, chorus, and pre-chorus clips as creatives within each set. Facebook allocates budget to the best-performing combinations, ideally discovering that, say, “fans of Seven Lions” + “chorus clip” converts at $0.30 while “fans of Illenium” + “verse clip” costs $0.80. Turn off the expensive combinations, double down on winners.

The logic is sound. Facebook has massive data on user behavior and sophisticated optimization algorithms. If you tell it “I want conversions to Spotify” and provide a testing matrix, it will find the cheapest path. The benchmark ratio Southworth provides - 100 conversions should generate 100-150 streams, 50+ listeners, 25+ saves - gives artists a quality check during the critical first 48 hours. If streams are way below conversions, either the targeting is wrong (people clicking but not interested enough to listen) or the landing page is leaking traffic (click to landing page doesn’t convert to click to Spotify). If saves are below 25%, the music isn’t resonating even with interested listeners, suggesting a quality problem.

This transparency is valuable. Most music marketing advice is vague - “build a fanbase,” “engage on social media,” “find your niche.” Southworth gives specific numbers and explains what they mean. The conversion benchmark is testable. An artist can run a campaign, track metrics, and evaluate whether the method works for them. If they hit 100 conversions, get 30 streams, and 5 saves, they know something is wrong - bad targeting, weak music, or broken funnel. Adjust and test again.

But Southworth doesn’t provide cost benchmarks. What’s a good cost per conversion? He mentions spending $300 over four weeks for “Socialize” (roughly $20/day), but doesn’t say how many conversions that bought or what the per-conversion cost was. Without this, artists can’t budget effectively. If conversions cost $2 each and you need 1,000 to hit Discover Weekly thresholds, that’s $2,000 per song. For many independent artists, that’s prohibitive. The case study shows profitability ($300 spent, $1,100+ earned), but Southworth admits “most songs will not profit.” So is the investment justified? Only if the long-term value arguments hold.

The economic model Southworth defends treats streaming revenue as insufficient justification by itself. He argues that $1,000 spent to generate $100 in streams makes sense when you account for:

1. **Recurring passive income from saves and playlist adds**: “Every month I get 60,000 streams from my saves and playlist ads for free”
2. **Compounding audience growth**: Followers mean future releases start with built-in reach
3. **Conversion funnel to higher-value actions**: Streaming listeners become email subscribers, merch buyers, concertgoers
4. **Algorithmic momentum**: Initial strong metrics trigger sustained algorithmic placement

This reframing is necessary because the direct ROI is usually negative. Spotify pays $2-5 per 1,000 streams. Even at the high end, 29,000 streams = $145. If you spent $1,000 to get them, you’re down $855. The long-term value proposition must carry the argument. Southworth’s “Socialize” case study supports this - the song doubled streams in two months after the campaign ended, validating the algorithmic momentum claim. But he’s showing a success story. How many campaigns generated 29,000 streams that then *didn’t* double? What percentage of artists who hit the 30% popularity threshold actually sustain Discover Weekly placement long enough to recoup costs?

The case study also doesn’t control for song quality. Maybe “Socialize” was just better than his previous releases. Southworth achieved 60% save rate and 3x repeat listen rate in week one - exceptional numbers. Did Facebook ads cause this, or did they simply deliver the song to an audience that would have loved it anyway? The ads provide reach, but conversion quality depends on the music itself. An artist could run a perfect Facebook campaign targeting ideal listeners, and if the song is mediocre, save rates will be low and algorithmic placement won’t happen. Southworth assumes the song crosses a quality threshold sufficient to convert interested listeners, but this assumption is doing significant work.

The book’s major blind spot is genre effects. Southworth’s background is EDM and electronic music, genres that perform well on Spotify’s algorithmic playlists. Do these methods work for folk, classical, jazz, ambient? Save behaviors likely vary by genre - ambient listeners may love a track but not save it because they prefer playlists curated by mood. Repeat listen rates differ - some genres invite repeated listening (pop), others don’t (spoken word, long-form classical). Ad costs vary - targeting fans of Taylor Swift costs more than targeting fans of niche lo-fi producers because the former audience is heavily competed for. None of this is addressed.

Scale effects also matter. Southworth had an existing YouTube audience when he ran the “Socialize” campaign. Did his subscribers provide a base of engaged listeners that primed the algorithm? For a completely unknown artist with zero followers, hitting 375 saves in week one may be much harder, requiring either more ad spend or higher conversion quality. The cold-start problem isn’t discussed.

Platform risk is the elephant in the room. The entire strategy depends on Facebook ads remaining effective and affordable. If Facebook changes its algorithm, bans music ads, or if costs spike due to competition, the method breaks. Southworth acknowledges Facebook’s ad platform “changes like every month or two,” creating instability. Spotify could also change its algorithm to de-emphasize metrics Southworth prioritizes or introduce anti-gaming measures that detect sudden spikes in activity. The book was written around 2023 based on 2019-2022 experience. Algorithmic landscapes shift. What worked in 2020 may not work in 2026.

Still, Southworth’s intellectual honesty elevates the book above typical marketing advice. He admits uncertainty (”more speculative,” “my best guess”), acknowledges failed strategies (he initially focused on playlists before realizing they didn’t work), and provides falsifiable claims. The metric thresholds are testable. The promotional method comparison is empirically grounded. The economic model, while dependent on unverified assumptions about long-term value, at least makes the assumptions explicit. He warns readers that “most people that try will fail” and that music is a “hostile” industry. This isn’t the false hope peddled by most music marketing gurus - it’s a sober assessment that success requires both quality and systematic promotion.

The pre-save revelation exemplifies his commitment to demystification. Most artists believe Spotify sees their pre-save counts and factors them into editorial playlist decisions. Southworth explains the technical reality: pre-save services store credentials and use Spotify’s API on release day to auto-save songs. Spotify doesn’t see the “pre” part - it just sees a spike in saves on day one. This spike helps due to the time factor (week one matters more), but it doesn’t function as “early demand signal” the way artists assume. The only exception is if you pitch directly to Spotify editors via industry connections and tell them your pre-save numbers. For most artists, this never happens. Southworth could have stayed silent on this point, but exposing the mechanism helps artists make informed decisions about whether pre-save campaigns’ high user friction is worth the day-one save bump.

The book’s rhythm occasionally falters. The chapter structure is logical - algorithm explanation, metrics identification, method comparison, economic justification, case study - but transitions are abrupt. The “Learn More” chapter is pure product pitch, which feels transactional after the analytical rigor of previous sections. But this is a self-published work written by a practitioner, not a professional author. The prose is serviceable, the explanations clear, and the data presentation usually effective (though the audiobook format makes charts difficult to convey, as Southworth himself notes).

What matters is whether the central claims withstand scrutiny. Southworth argues:

1. Spotify’s algorithm responds to specific behavioral metrics in predictable ways
2. Different promotional methods generate different metric patterns
3. Facebook ads optimize for the metrics Spotify rewards
4. Long-term value from algorithmic placement justifies upfront investment

Claims 1 and 2 are well-supported by his experience and align with how recommendation systems generally work. Claim 3 is logically sound - self-selected ad clicks should generate higher engagement than passive playlist exposure - though the comparison may be tilted by contrasting best ads to worst playlists. Claim 4 requires faith in assumptions about conversion rates and sustained algorithmic performance that aren’t fully proven.

The 300-song study would benefit from publication with full methodology. The case study would be more convincing with controls and comparison to non-promoted releases. The genre, scale, and platform risk issues need addressing. But the book does what most music marketing advice doesn’t: it provides testable hypotheses, concrete metrics, and honest acknowledgment of uncertainty. An artist can implement these methods, track the numbers Southworth specifies, and evaluate whether the approach works for their music in their genre at their scale. If save rates are below 40% despite targeted ads, they learn their music isn’t resonating with the intended audience. If costs per conversion are prohibitively high, they learn their genre or positioning has challenges. If algorithmic placement doesn’t follow despite hitting thresholds, they learn additional factors are at play.

This empirical feedback loop is valuable even if Southworth’s specific claims turn out to be partially wrong or time-limited. He’s teaching artists to think like scientists - form hypotheses, run experiments, measure outcomes, update beliefs. In an industry often dominated by myth, superstition, and self-serving advice from people selling tools or services, this methodological rigor matters more than whether the 2,503-stream threshold remains accurate in 2026.

The final question is whether this approach is accessible. Facebook ads require learning a complex platform, continuous optimization, and capital to test. Organic social media requires massive time investment and content creation skills. Playlist promotion, for all its flaws, is simple - pay someone, get streams. Southworth’s path is harder, but he claims it’s more effective. Whether artists have the resources, knowledge, and persistence to execute it is another question entirely. The book provides the blueprint. Whether the foundation it’s built on - Spotify’s current algorithmic logic and Facebook’s current ad platform - remains stable enough to justify construction is unknowable until years from now, when the data will tell whether these songs, promoted with precision and metric obsession, actually accumulated the long-term audience value that justified spending more on marketing than the music would ever earn directly from streams.

---

**Tags:** Spotify algorithm mechanics, music marketing strategy, Facebook ads conversion optimization, streaming platform growth tactics, Andrew Southworth
