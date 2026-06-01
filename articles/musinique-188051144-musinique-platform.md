---
title: "MUSINIQUE PLATFORM"
subtitle: "Technical Documentation & Engineering Roadmap"
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: "188051144.musinique-platform"
post_date: "2026-02-15T17:02:55.806Z"
is_published: "true"
source_zip: "Y0r_0oGOSoWMD3iEcEhVnA.zip"
source_html: "posts/188051144.musinique-platform.html"
source_file: "musinique-188051144-musinique-platform.md"
cover_image: ""
---
**Version 1.0 | February 2026**
**Classification: Internal / Confidential**
*“Humans make music. Bots check data.”*

---

## Abstract

### Computational Detection of Fraudulent Playlist Networks and Algorithmic Music Replacement on Streaming Platforms

**The Problem: A $2-3 Billion Annual Theft Hidden in Plain Sight**

The music streaming economy operates on a fundamental deception: platforms present algorithmically-curated playlists as meritocratic discovery mechanisms while systematically replacing independent musicians with cheaper alternatives. This paper presents the first comprehensive computational framework for detecting two interrelated forms of exploitation:

1. **Bot-driven stream fraud** siphoning royalties from legitimate artists through the pro-rata payment system
2. **“Perfect Fit Content” (PFC) programs** where platforms covertly substitute ghost artists—fabricated musician identities created by production music companies—into high-follower mood playlists to reduce licensing costs.

Recent investigative journalism (Pelly, 2025) documented Spotify’s internal “Strategic Programming” team managing 100+ playlists composed of over 90% ghost artists, generating €61.4 million annual gross profit by licensing stock music at reduced royalty rates from Swedish production companies (Firefly Entertainment, Epidemic Sound). However, journalistic methods cannot quantify prevalence across Spotify’s estimated 5+ million user-generated playlists or systematically distinguish legitimate curation from fraud at scale.

**The economic mechanism is parasitic:** streaming platforms distribute royalties via pro-rata pools where each rights holder receives percentage of total revenue proportional to their stream share. When fraudulent streams inflate the denominator (Michael Smith case: $10 million stolen via 10,000+ bot accounts generating billions of fake streams), or when ghost artists capture stream share at reduced licensing costs, legitimate artists’ payments decrease even if their absolute stream counts remain constant. The 2021 estimate of 1-3% fraudulent streams translates to $200-600 million annually diverted from working musicians in a global industry where median artist income is $20,000-25,000/year.

Current detection methods fail because they assume fraud is anomalous. In reality, exploitation is structural—embedded in playlist curation labor (unpaid user-generated playlists building platform value), algorithmic recommendation systems (optimizing for engagement over quality), and corporate partnerships (major labels owning playlist brands like Filtr while negotiating privileged royalty terms). **Fraud doesn’t look like outlier behavior; it looks like optimized platform participation.**

---

# PART I: SYSTEM ARCHITECTURE

## 1. Mission & Philosophy

Musinique is a **data-driven “Consumer Reports” framework** for Spotify playlist intelligence and artist submission strategy. The platform treats playlists as technological products subject to objective, standardized auditing—not subjective creative judgment.

### Core Principles

**Black Box Testing:** Every playlister subjected to the same rigorous, data-driven scrutiny regardless of reputation or reach. No special treatment.

**Computational Skepticism:** Data analysis reveals exploitation patterns invisible to human observation. Evidence over marketing claims.

**Algorithmic Identity Protection:** Every stream is a data point. Bad placements “poison” an artist’s algorithmic profile, causing 90% drops in recommendation support.

**Integrity Over Reach:** A 1,000-follower focused playlist with high Active Listener Ratio outperforms a 50,000-follower bot shell for career growth.

### The Fraud Crisis Context

**Annual scale:**

- **$2B - $3B** in royalty theft globally (diverted from legitimate artists)
- **1-3%** of all streams are fraudulent (billions of fake plays)
- **Michael Smith case:** $10M stolen using 10,000+ bot accounts streaming AI-generated music
- **Tracks generated:** Hundreds of thousands with names like “Zygotic Washstands”

---

## 2. Component Map

The platform consists of six major components:

### 🔵 Implemented Components

**curator_enrichment/** - AI research agent

- Language: Python
- Framework: LangGraph
- Function: Automated curator contact discovery (Instagram, Twitter, submission forms)
- Status: ✅ Fully operational

**scripts/csv_processing/** - URL validator

- Language: Python
- Framework: Playwright (headless browser)
- Function: Verifies Spotify playlist/profile liveness
- Status: ✅ Multi-process version complete

**scripts/data_collection/** - Spotify API collector

- Language: Python
- Framework: Spotipy, aiohttp
- Function: Keyword-based playlist search and metadata enrichment
- Status: ✅ Async batching implemented

**curator_playlists/** - Scoring engine

- Language: Python
- Framework: Pandas
- Function: Focus Score calculation, genre mapping
- Status: ✅ Core metrics complete

### 🔴 Missing Components (TODO)

**forensic_metrics/** - Fraud detection suite

- Function: Z-score growth monitoring, churn pattern detection, FAL resonance analysis
- Status: ❌ Not started

**sonic_intelligence/** - Machine learning layer

- Function: Genre-space ellipsoid calculations, S-BERT semantic matching
- Status: ❌ Not started

---

## 3. The Focus Score: Mathematical Foundation

The proprietary **Musinique Focus Score** (0-100) measures playlist quality through three weighted components:

### Formula

```
Focus Score = (0.45 × Genre Breadth) + (0.30 × Genre Density) + (0.25 × Artist Focus)
```

### Component 1: Genre Breadth Score (45% weight)

**Goal:** Reward playlists with fewer primary genres

**Calculation:**

```
def genre_breadth_score(n: int) -> float:
    if n <= 1:
        return 100  # Perfect focus
    if n >= 50:
        return 0    # Unfocused mess
    return round(100 * (1 - math.log(n) / math.log(50)), 1)
```

**Interpretation:**

- 1 genre = 100 points (perfectly focused)
- 2 genres = 82.3 points (near-perfect)
- 5 genres = 59.0 points (moderate)
- 10 genres = 41.3 points (losing coherence)
- 20 genres = 23.6 points (broad/unfocused)
- 50+ genres = 0 points (”cleaning lady” playlist)

### Component 2: Genre Density Score (30% weight)

**Goal:** Measure depth of niche (tracks per genre)

**Calculation:**

```
def genre_density_score(total_tracks: int, genre_count: int) -> float:
    density = total_tracks / max(genre_count, 1)
    if density >= 80:
        return 100  # Deep catalog
    if density <= 5:
        return 0    # Shallow
    return round(100 * (density - 5) / 75, 1)
```

**Examples:**

- 400 tracks ÷ 2 genres = 200 density = 100 points (deep Jazz catalog)
- 150 tracks ÷ 3 genres = 50 density = 60 points (focused Indie)
- 100 tracks ÷ 15 genres = 6.7 density = 2.3 points (broad mix)
- 50 tracks ÷ 25 genres = 2 density = 0 points (random dump)

### Component 3: Artist Focus Score (25% weight)

**Goal:** Reward curation over random dumping (artist repetition indicates a “sound”)

**Calculation:**

```
def artist_focus_score(total_tracks: int, unique_artists: int) -> float:
    ratio = unique_artists / total_tracks
    if ratio <= 0.3:
        return 100  # High repetition = focus
    if ratio >= 1.0:
        return 0    # Every artist once = random
    return round(100 * (1 - (ratio - 0.3) / 0.7), 1)
```

**Examples:**

- 100 tracks, 10 unique artists (0.10 ratio) = 100 points (artist showcase)
- 100 tracks, 30 unique artists (0.30 ratio) = 100 points (focused sound)
- 100 tracks, 50 unique artists (0.50 ratio) = 71.4 points (moderate)
- 100 tracks, 100 unique artists (1.00 ratio) = 0 points (no curation)

### Score Interpretation

**85-100 (Excellent - Green):** Highly focused niche. Strategic partner. High ROI expected.

**70-84 (Very Good - Lime):** Solid opportunity. Genre-focused with minor variance.

**55-69 (Good - Yellow):** Proceed with caution. May have sonic mismatches or high skip rates.

**40-54 (Fair - Orange):** Marginal value. Likely inactive or poor alignment.

**<40 (Poor - Red):** Stay away. High bot risk or “cleaning lady” playlist.

---

## 4. The Integrity Layer Framework

### Five Audit Pillars

**1. Growth Dynamics** (TODO)

- **Objective:** Verify follower authenticity
- **Mechanism:** Z-score analysis, vertical spike detection
- **Red Flag:** 50,000 followers gained in single day

**2. Engagement Efficiency** (TODO)

- **Objective:** Measure real listener impact
- **Mechanism:** Stream-to-Follower ratio, Active Listener Ratio
- **Red Flag:** 100K followers but only 500 monthly streams

**3. Sonic Coherence** (TODO)

- **Objective:** Ensure vibe alignment
- **Mechanism:** Ellipsoid diversity metric in genre-space
- **Red Flag:** “Chill Lofi” playlist containing Death Metal

**4. Algorithmic Potential** (TODO)

- **Objective:** Map Spotify Popularity Score triggers
- **Mechanism:** Track 20%/30% thresholds for Discover Weekly
- **Red Flag:** Playlist fails to push any tracks past milestones

**5. Curator Governance** (✅ Partial)

- **Objective:** Transparency & compliance
- **Mechanism:** Digital footprint scraping, contact verification
- **Red Flag:** Anonymous curator with no external presence

### Bot Detection Indicators

**Stream-to-Follower Ratio:**

- Bot Farm: >1:1 (10K streams from 5K followers)
- Human Pattern: <1:10 (Followers greatly exceed Monthly Listeners)

**Weekly Turnover:**

- Bot Farm: Exact 7-day removals for >50% of content
- Human Pattern: 28+ days organic retention

**Geographic Seeding:**

- Bot Farm: Massive spikes from data centers (Ashburn, Chicago, Dublin)
- Human Pattern: Distributed by actual fanbase location

**Engagement Depth:**

- Bot Farm: Streams with zero saves or artist follows
- Human Pattern: Streams correlated with saves, follows, FAL movement

**Artist Presence:**

- Bot Farm: “Digital Ghost” with no website, social, or tour history
- Human Pattern: Verifiable real-world footprint and press coverage

---

# PART II: EXISTING CODE DOCUMENTATION

## 5. Curator Enrichment Agent (✅ Implemented)

### What It Does

A LangGraph-powered research agent that automates finding curator contact information that Spotify’s API doesn’t provide.

### File Structure

```
curator_enrichment/
├── agent.py       # LangGraph orchestration
├── state.py       # CuratorState schema
├── tools.py       # google_search, scrape_page
├── prompts.py     # LLM instructions
└── config.py      # API credentials
```

### State Machine Flow

```
START
  ↓
Initial Search (Google: "curator_name music playlists")
  ↓
LLM Extraction (Gemini parses results)
  ↓
Router Decision:
  ├→ Scrape (if potential_website found) → Loop back to LLM
  ├→ Search (if missing Instagram/Twitter/etc) → Loop back to LLM
  └→ END (if all data collected or limits reached)
```

### Data Collected Per Curator

**CuratorState Schema:**

- `curator_name` (input)
- `spotify_url` (input)
- `instagram` (extracted)
- `twitter` (extracted)
- `facebook` (extracted)
- `submission_form` (extracted)
- `potential_website` (extracted)
- `any_other_handle` (list of additional links)

### Rate Limits & Controls

**Search limits:**

- Maximum 2 additional targeted searches per curator
- 2-second delay between Gemini API calls
- 3-second delay between CSV saves

**Scrape limits:**

- Maximum 1 deep-dive scrape per curator
- 8-second timeout per webpage
- Output truncated to 8,000 characters

### Key Design Decisions

**Lenient Name Matching:** The agent is instructed to recognize that “BIRP!” = “BIRP” = “BIRP.DJ” = “BIRP.fm” if music context is strong. Handles typos, spacing issues, symbol differences.

**Context Verification:** Requires music-related context to confirm identity. Won’t extract “John Smith the plumber” when searching for “John Smith the DJ.”

**Structured Output:** Uses Gemini’s native structured output (Pydantic schema) to guarantee JSON format, no parsing errors.

---

## 6. Spotify URL Validator (✅ Implemented)

### What It Does

Multi-process Playwright automation that verifies if Spotify playlist/profile URLs are still active (not deleted/broken).

### Two Versions Available

**Single-Threaded (spotify_validator.py):**

- Speed: ~5-10 seconds per URL
- Mode: Headful (visible browser)
- Use case: Small datasets (<100 URLs), debugging
- CPU usage: Low (1 core)

**Multi-Process (multiprocessing-spotify-validator.py):**

- Speed: ~1-2 seconds per URL
- Mode: Headless (background)
- Use case: Large datasets (1000+ URLs)
- CPU usage: High (configurable, default 16 processes)
- Features: Auto-save checkpoints every 100 results

### Validation Algorithm

**Primary Detection (Error Pages):**

The script first checks for Spotify’s error messages:

1. “Couldn’t find that playlist”
2. “Couldn’t find that page”
3. “Search for something else?”

If any found → immediate “invalid” verdict.

**Secondary Validation (Content Indicators):**

For playlists, requires **2+ indicators** from:

- Track links (>3 actual song links)
- Add to playlist button
- Save/like count
- Description area
- Duration info (”about 2 hr 30 min”)

For profiles, requires **2+ indicators** from:

- “Public Playlists” section
- Follower count display
- Follow button
- Profile badge
- Playlist cards/thumbnails

### Anti-Bot Measures

**Human-like behavior simulation:**

- Random mouse movements (100-800 pixel range)
- Variable scroll amounts
- Wait times: 5-7 seconds for page load
- Random delays: 2-5 seconds between requests
- Long breaks: 10-20 seconds every 10 URLs

**Browser fingerprint masking:**

```
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
});
```

**Realistic headers:**

- User-Agent: Mac OS Chrome
- Accept-Language: en-US
- Timezone: America/New_York

### Performance Metrics

**Processing 1,000 URLs:**

- Single-threaded: ~2-3 hours
- Multi-process (16 cores): ~20-30 minutes

**Typical results:**

- ~30% of URLs become invalid over 6 months
- Requires weekly re-validation for data freshness

---

## 7. Data Collection Pipeline (✅ Implemented)

### Spotify API Collector

**File:** `scripts/data_collection/data_collection.py`

**Search Strategy:**

Keywords used:

- “indie”, “indie pop”, “indie rock”, “indie folk”
- “bedroom pop”, “lofi”
- “unsigned artist”, “emerging artist”

**Rate limiting:**

- 0.15 second delay between requests
- Max 1,000 playlists per keyword

**Async Architecture:**

Uses `aiohttp` for parallel metadata fetching:

```
async def fetch_all_playlists(playlist_ids):
    # Processes all IDs simultaneously
    # Significantly faster than sequential
    tasks = [fetch_playlist(session, pid, headers)
             for pid in playlist_ids]
    return await asyncio.gather(*tasks)
```

### Curator Deep-Dive Pipeline

**File:** `curator_playlists/fetch_data.py`

**Process for each curator:**

1. **Fetch all playlists** via pagination (50/request)
2. **Fetch metadata** (followers, description, total_tracks)
3. **Fetch ALL tracks** from ALL playlists (100/page)
4. **Fetch ALL artist details** (batch 50/request)
5. **Aggregate genres** from all artists
6. **Calculate metrics** (diversity, popularity averages)
7. **Save to CSV** (one file per curator)

**Data points collected:**

- Playlist: followers, total_tracks, description, public status
- Tracks: name, popularity, album, artists, duration
- Artists: name, followers, popularity, **GENRES** (critical for Focus Score)

### Authentication & Error Handling

**Robust retry logic:**

```
def get_json(url, params=None, max_retries=7):
    # Handles 429 (rate limit): Respects Retry-After header
    # Handles 401 (expired token): Auto-refreshes
    # Handles network errors: Exponential backoff (1.5^attempt)
    # Returns None after all retries fail
```

---

## 8. Scoring & Analytics (✅ Implemented)

### Genre Mapping System

**Problem:** Spotify has 5,000+ micro-genres (”bedroom pop”, “indie folk”, “lo-fi hip hop”)

**Solution:** Map to ~20 primary genres for coherent analysis

**Mapping table:** `MetaData/Music_Genres_unique.csv`

```
Subgenre,Primary Genre
indie folk,Indie
indie pop,Indie
lo-fi,Electronic
death metal,Metal
```

**Logic:**

```
def map_playlist_genres(genre_list_raw, mapping_df):
    # 1. Normalize: lowercase, strip whitespace
    # 2. Lookup: subgenre → primary genre
    # 3. Deduplicate: sorted unique list
    # Returns: (mapped, unmapped)
```

**Output columns added:**

- `primary_genres` - List of parent genres
- `primary_genre_diversity` - Count of unique parents
- `all_genres` - Original Spotify genres
- `all_genre_diversity` - Count of all unique genres

### Focus Score Calculation

**File:** `curator_playlists/utils.py`

**Complete implementation:**

```
def musinique_focus_score(row):
    s1 = genre_breadth_score(row["primary_genre_diversity"])
    s2 = genre_density_score(row["total_tracks"], row["primary_genre_diversity"])
    s3 = artist_focus_score(row["total_tracks"], row["unique_artists"])

    return round(0.45 * s1 + 0.30 * s2 + 0.25 * s3, 1)
```

**Applied in:** `curator_playlists/main.py`

```
df['musinique_focus_score'] = df.apply(musinique_focus_score, axis=1)
```

### Example Scores

**Jazz Piano Trios playlist:**

- 1 genre, 200 tracks, 0.15 artist ratio
- S₁ = 100, S₂ = 100, S₃ = 100
- **Final: 100.0** (perfect)

**Indie Discovery playlist:**

- 3 genres, 150 tracks, 0.40 artist ratio
- S₁ = 73, S₂ = 60, S₃ = 86
- **Final: 73.6** (very good)

**Mixed Vibes playlist:**

- 12 genres, 96 tracks, 0.70 artist ratio
- S₁ = 35, S₂ = 4, S₃ = 43
- **Final: 28.9** (poor - stay away)

---

# PART III: DATA PIPELINE

## 9. Complete Data Flow

### Stage 1: Keyword Search

**Input:** KEYWORDS array
**Script:** `scripts/data_collection/main.py`
**Output:** `playlists_base.csv` (~8,000 playlists)
**Runtime:** 10-15 minutes

### Stage 2: Metadata Enrichment

**Input:** playlists_base.csv
**Script:** `scripts/data_collection/data_collection.py`
**Fetches:** followers, description, total_tracks, image
**Output:** `playlists_final.csv`
**Runtime:** 15-20 minutes (async)

### Stage 3: URL Validation

**Input:** playlists_final.csv
**Script:** `scripts/csv_processing/multiprocessing-spotify-validator.py`
**Validates:** Playlist/profile liveness
**Output:** `spotify_data_validated.csv` (~5,800 valid)
**Runtime:** 2-4 hours (16 processes)

### Stage 4: Curator Deep-Dive

**Input:** Valid curator URLs
**Script:** `curator_playlists/fetch_data.py`
**Extracts:** ALL tracks, ALL artists, ALL genres
**Output:** Individual curator CSVs
**Runtime:** Varies (API intensive)

### Stage 5: Contact Enrichment

**Input:** Curator list from Stage 4
**Script:** `curator_enrichment/agent.py`
**Discovers:** Instagram, Twitter, Facebook, submission forms
**Output:** `Playlisters.csv`
**Runtime:** ~10 minutes for 84 curators

### Stage 6: Scoring & Unification

**Input:** All curator CSVs + mapping table
**Script:** `curator_playlists/main.py`
**Calculates:** Focus scores, maps genres
**Output:** **Playlists.csv** (final product)
**Runtime:** <5 minutes

---

## 10. Output Data Formats

### Production Outputs

**Playlists.csv** (~5,800 rows)

- Complete database for Gumroad paid product ($25)
- Key columns: curator_name, playlist_name, followers, total_tracks, primary_genres, musinique_focus_score
- Used for: Artist submission targeting

**Playlisters.csv** (~84 rows)

- Curator contact directory
- Key columns: curator_name, instagram, twitter, facebook, submission_form, avg_focus_score, total_reach
- Used for: Direct curator outreach

**Playlists_sample.csv** (1,000 rows)

- Stratified sample across ALL genres
- Ensures niche genres (Gothic, Metal) represented, not just Pop
- Used for: Free tier lead magnet

**Playlisters_sample.csv** (15 rows)

- Diverse curator selection (1 per genre category)
- Used for: Free tier curator contact examples

### Sampling Methodology

**Stratified Sampling Algorithm:**

Goal: Prevent over-representation of Pop/Indie, ensure small genres included

Process:

1. Group playlists by primary_genre
2. Calculate weight = genre_count / total
3. Sample proportionally from each genre
4. Guarantee: At least 1 playlist per genre

**Why this matters:** Random sampling of 1,000 from 5,800 would likely exclude niche genres entirely. Stratified approach ensures coverage.

---

# PART IV: MISSING COMPONENTS (TODO)

## 🚨 CRITICAL GAP: The Integrity Layer

Current system calculates **Focus Score** (genre coherence) but lacks the forensic components required to detect:

- Bot farms
- Payola patterns
- Algorithmic poisoning
- Ghost artist networks

These are the “Computational Skepticism” tools needed to move from “playlist database” to “Consumer Reports for music.”

---

## 11. TODO-001: Z-Score Growth Monitor

### Priority: 🔴 CRITICAL | Effort: 2-3 days

**Goal:** Detect “Bot Injection” via vertical follower growth spikes

**Mathematical Foundation:**

The Z-score measures how many standard deviations a data point is from the mean:

```
Z = (x - μ) / σ

Where:
  x = current day's follower growth
  μ = mean growth for this genre
  σ = standard deviation

Flags:
  Z > 2.0 = Statistically significant (95% confidence)
  Z > 3.0 = Highly anomalous (99.7% confidence) - BOT INJECTION
```

### Data Requirements

**Historical follower counts (time series):**

- Source options: ChartMetric API or scheduled snapshots
- Minimum: 3 months of data for baseline calculation
- Storage: PostgreSQL with TimescaleDB extension

**Proposed table schema:**

```
CREATE TABLE follower_snapshots (
    playlist_id TEXT NOT NULL,
    snapshot_date DATE NOT NULL,
    followers INTEGER NOT NULL,
    total_tracks INTEGER,
    PRIMARY KEY (playlist_id, snapshot_date)
);

CREATE INDEX idx_playlist_timeseries
ON follower_snapshots(playlist_id, snapshot_date DESC);
```

### Implementation Specification

**File to create:** `forensic_metrics/z_score_monitor.py`

```
import numpy as np
from scipy import stats

def calculate_z_score(current_growth, historical_data):
    """
    Calculates Z-score for follower growth.

    Args:
        current_growth: Today's net follower increase
        historical_data: Array of past daily growth values

    Returns:
        float: Z-score (positive = above average growth)
    """
    mean = np.mean(historical_data)
    std = np.std(historical_data)

    if std == 0:
        return 0  # No variance in data

    return (current_growth - mean) / std

def detect_bot_injection(follower_history):
    """
    Scans time series for vertical spikes.

    Returns:
        {
            'bot_injection_detected': bool,
            'spike_dates': List[str],
            'max_z_score': float,
            'pattern': 'vertical' | 'staircase' | 'organic'
        }
    """
    # Calculate daily deltas
    daily_growth = np.diff(follower_history)

    # Calculate Z-scores
    z_scores = []
    for i in range(30, len(daily_growth)):
        window = daily_growth[i-30:i]  # 30-day baseline
        z = calculate_z_score(daily_growth[i], window)
        z_scores.append(z)

    # Detect spikes
    max_z = max(z_scores)
    spike_detected = max_z > 3.0

    return {
        'bot_injection_detected': spike_detected,
        'max_z_score': round(max_z, 2),
        'pattern': classify_growth_pattern(follower_history)
    }
```

### Output Columns to Add

**Playlists.csv additions:**

- `z_score_max` - Highest Z-score detected
- `bot_injection_flag` - Boolean
- `growth_pattern` - “vertical” | “staircase” | “organic”
- `last_spike_date` - When anomaly occurred

---

## 12. TODO-002: Churn Detector

### Priority: 🔴 CRITICAL | Effort: 2-3 days

**Goal:** Detect “Step Function” removal patterns indicating pay-for-placement contracts

**The Pattern:**

Legitimate playlists: Songs removed gradually over weeks/months as listener interest wanes

Bot farms: Songs removed at **exact** intervals (7, 14, 30 days) matching sales contracts

- “1-week placement” = removal on day 7
- “1-month placement” = removal on day 30

### Data Requirements

**Track snapshots:**

- Weekly snapshot of playlist state
- Compare: tracks present week N vs week N+1
- Store: track_id, added_at, removed_at

**Proposed table schema:**

```
CREATE TABLE track_history (
    playlist_id TEXT NOT NULL,
    track_id TEXT NOT NULL,
    snapshot_date DATE NOT NULL,
    position INTEGER,
    status TEXT CHECK(status IN ('present', 'removed'))
);
```

### Implementation Specification

**File to create:** `forensic_metrics/churn_detector.py`

```
from collections import Counter

def analyze_removal_patterns(snapshots):
    """
    Detects coordinated removal patterns.

    Returns:
        {
            'retention_score': int (1-5),
            'removal_histogram': {7: count, 14: count, ...},
            'suspected_payola': bool,
            'average_retention_days': float
        }
    """
    # Calculate days on playlist for each removed track
    removals = []
    for track in get_removed_tracks(snapshots):
        days = (track.removed_at - track.added_at).days
        removals.append(days)

    # Build histogram
    hist = Counter(removals)

    # Check for exact-day clustering
    seven_day_pct = hist.get(7, 0) / len(removals)
    fourteen_day_pct = hist.get(14, 0) / len(removals)
    thirty_day_pct = hist.get(30, 0) / len(removals)

    # Scoring
    if seven_day_pct > 0.5:
        return {
            'retention_score': 1,  # High risk
            'suspected_payola': True,
            'pattern': 'exact_7day'
        }
    elif fourteen_day_pct > 0.3:
        return {
            'retention_score': 2,  # At-risk
            'suspected_payola': True,
            'pattern': 'exact_14day'
        }
    # ... etc
```

### Retention Scoring Scale

**Score 5 - High Organic Retention:**

- Songs remain 28+ days
- High correlation with saves and artist follows
- Staggered removal pattern

**Score 4 - Standard Engagement:**

- Songs remain 14-28 days
- Typical for “Fresh Hits” style playlists

**Score 3 - Neutral:**

- Inconsistent turnover
- Mix of long-term and short-term placements

**Score 2 - At-Risk:**

- Frequent 14-day removals
- Low engagement-to-stream ratio

**Score 1 - High-Risk Fraud:**

- Exact 7-day drop-offs for >50% of content
- Correlates with illicit “1-week placement” sales cycles

---

## 13. TODO-003: FAL (Fans Also Like) Auditor

### Priority: 🟠 HIGH | Effort: 1-2 days

**Goal:** Verify if playlists generate algorithmic connections between artists

**The Concept:**

Spotify’s “Fans Also Like” section is built from real user listening behavior:

- If many users listen to Artist A → then Artist B
- Algorithm creates Artist A ↔ Artist B connection
- Shows up in Artist A’s profile under “Fans Also Like”

**Organic playlist impact:**

- Real listeners discover artist on playlist
- Engage with artist’s other work
- Follow artist profile
- Listen to similar artists
- **Result:** FAL section populates, algorithmic associations strengthen

**Bot farm pattern:**

- Bots stream without engagement
- No follows, no artist exploration
- No FAL movement triggered
- **Result:** Artist has 100K monthly listeners but ZERO related artists

### Implementation Specification

**File to create:** `forensic_metrics/fal_auditor.py`

**Spotify API endpoint:**

```
GET https://api.spotify.com/v1/artists/{id}/related-artists

Returns:
{
  "artists": [
    {"id": "...", "name": "...", "genres": [...], "popularity": 65}
  ]
}
```

**Algorithm:**

```
def audit_fal_resonance(playlist_id):
    """
    Checks if playlist generates algorithmic resonance.

    Process:
        1. Get top 10 artists from playlist
        2. Fetch FAL for each artist
        3. Analyze FAL quality:
           a. Are FAL artists in same genre?
           b. Are FAL artists also on this playlist?
           c. Do FAL artists have reasonable popularity alignment?

    Red Flags:
        - Empty FAL (0 related artists) = "Non-Resonant"
        - Unrelated genres in FAL = "Random Network"
        - All FAL artists unknown (<10 popularity) = "Digital Ghost"

    Returns:
        {
            'resonance_score': float (0-100),
            'empty_fal_count': int,
            'cross_genre_fal_count': int,
            'verdict': 'Resonant' | 'Non-Resonant' | 'Suspicious'
        }
    """
    # Implementation required
```

**Output columns to add:**

- `fal_resonance_score` - 0-100
- `empty_fal_count` - Number of artists with 0 FAL
- `fal_verdict` - “Resonant” | “Non-Resonant” | “Suspicious”

---

## 14. TODO-004: Ellipsoid Diversity Metric

### Priority: 🟠 HIGH | Effort: 5-7 days

**Goal:** Quantify “Sonic Chaos” via multidimensional genre-space analysis

**The Theory:**

Human curators create playlists that form **tight clusters** in audio feature space:

- “Chill Lofi” → low energy, moderate valence, low tempo
- “Workout Bangers” → high energy, high tempo, high danceability

Bot farms accept ANY artist willing to pay → **scattered chaos** in feature space:

- Random mix of Death Metal + K-Pop + Classical
- No coherent mood, activity, or vibe

**Mathematical Model:**

Songs represented as points in n-dimensional space:

- Dimensions: energy, valence, danceability, tempo, acousticness, instrumentalness, speechiness
- Fit an ellipsoid to the points
- Calculate volume: V = (4/3)π × ∏(rᵢ)

**Research baseline (Purdue Engineering):**

- Human playlists: volume 5 orders of magnitude smaller than full song database
- Threshold: 99th percentile of organic playlists

### Data Requirements

**Spotify Audio Features API:**

```
GET https://api.spotify.com/v1/audio-features/{id}

# Batch version (up to 100 tracks):
GET https://api.spotify.com/v1/audio-features?ids=id1,id2,...

Returns:
{
  "energy": 0.73,
  "valence": 0.54,
  "danceability": 0.65,
  "tempo": 128.0,
  "acousticness": 0.11,
  "instrumentalness": 0.002,
  "speechiness": 0.04
}
```

### Implementation Specification

**File to create:** `sonic_intelligence/ellipsoid_metric.py`

**Dependencies to add:**

```
scikit-learn
numpy
scipy
```

**Algorithm outline:**

```
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import EllipticEnvelope
import numpy as np

def calculate_ellipsoid_volume(playlist_tracks):
    """
    Models playlist as ellipsoid in genre-space.

    Steps:
        1. Fetch audio features for all tracks
        2. Normalize features to [0,1]
        3. Apply LDA for dimensionality reduction (optional)
        4. Fit ellipsoid to track points
        5. Calculate volume

    Returns:
        {
            'ellipsoid_volume': float,
            'sonic_chaos_score': float (0-100),
            'verdict': 'Focused' | 'Moderate' | 'Chaotic'
        }
    """
    # Step 1: Fetch features
    features = fetch_audio_features_batch(playlist_tracks)

    # Step 2: Build feature matrix
    X = np.array([[
        track['energy'],
        track['valence'],
        track['danceability'],
        track['tempo'] / 200,  # Normalize BPM
        track['acousticness'],
        track['instrumentalness'],
        track['speechiness']
    ] for track in features])

    # Step 3: Fit ellipsoid (use covariance matrix)
    from numpy.linalg import eig
    cov = np.cov(X.T)
    eigenvalues, _ = eig(cov)

    # Step 4: Volume = product of semi-axes
    semi_axes = np.sqrt(eigenvalues)
    volume = (4/3) * np.pi * np.prod(semi_axes)

    # Step 5: Normalize against baseline
    # (Requires calibration data from known-good playlists)

    return volume
```

**Calibration required:**

- Establish baseline by analyzing 100+ verified human-curated playlists
- Calculate 99th percentile volume
- Use as threshold for “Chaotic” classification

---

## 15. TODO-005: S-BERT Semantic Matcher

### Priority: 🟠 HIGH | Effort: 2-3 days

**Goal:** Detect “Playlist Stuffing” via title/description misalignment

**The Problem:**

Fraudulent playlists use keyword-stuffed descriptions to capture search traffic:

- Title: “Chill Study Beats”
- Description: “Perfect for focus, relaxation, and studying”
- **Reality:** Playlist contains Death Metal and EDM

Legitimate curators craft descriptions matching actual content.

### Implementation Specification

**File to create:** `sonic_intelligence/semantic_matcher.py`

**Dependencies:**

```
sentence-transformers
scikit-learn
```

**Model:**

```
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_alignment_score(playlist_description, genre_list):
    """
    Calculates cosine similarity between text claims and reality.

    Process:
        1. Embed playlist description/title
        2. Embed aggregate genre string
        3. Calculate cosine similarity

    Formula:
        similarity = (A · B) / (||A|| × ||B||)

    Red Flags:
        similarity < 0.3 = "Playlist Stuffing"

    Returns:
        {
            'similarity': float (0-1),
            'alignment_score': float (0-100),
            'verdict': 'Aligned' | 'Misaligned' | 'Deceptive'
        }
    """
    # Embed description
    desc_embedding = model.encode(playlist_description)

    # Embed genres
    genre_text = ", ".join(genre_list)
    genre_embedding = model.encode(genre_text)

    # Cosine similarity
    from sklearn.metrics.pairwise import cosine_similarity
    similarity = cosine_similarity(
        [desc_embedding],
        [genre_embedding]
    )[0][0]

    verdict = 'Aligned' if similarity > 0.5 else 'Deceptive'

    return {
        'similarity': round(similarity, 3),
        'alignment_score': round(similarity * 100, 1),
        'verdict': verdict
    }
```

**Example outputs:**

**Aligned playlist:**

- Description: “The best Jazz piano trios from the 1960s-70s”
- Genres: [’Jazz’, ‘Jazz Piano’]
- Similarity: 0.89 → Alignment Score: 89

**Deceptive playlist:**

- Description: “Chill lofi beats for studying”
- Genres: [’Death Metal’, ‘Heavy Metal’, ‘Hardcore’]
- Similarity: 0.12 → Alignment Score: 12 → **STUFFING DETECTED**

---

## 16. TODO-006: SPS Milestone Tracker

### Priority: 🟡 MEDIUM | Effort: 2 days

**Goal:** Monitor if playlists successfully push tracks past critical Spotify Popularity Score thresholds

**SPS Milestone Reference:**

**20-29 (Moderate):**

- Triggers: Release Radar push (first 28 days)
- Meaning: Algorithm begins testing track

**30-59 (Critical Growth):**

- Triggers: Discover Weekly activation
- Meaning: Track enters personalized recommendations

**60-79 (High Traction):**

- Triggers: Editorial chart consideration
- Meaning: Track becomes “hot” in Spotify’s system

**80-100 (Global Hit):**

- Triggers: Universal platform exposure
- Meaning: Track has viral potential

### Why This Matters

A playlist’s “Algorithmic Efficiency” is measured by:

- What % of placed tracks cross the 20% threshold?
- What % reach the 30% threshold (Discover Weekly)?

**High-efficiency playlist:** 40%+ of tracks reach 30+ SPS
**Dead-end playlist:** <5% of tracks move at all

### Implementation Specification

**File to create:** `forensic_metrics/sps_tracker.py`

```
def track_sps_milestones(playlist_id, timeframe_days=30):
    """
    Monitors SPS movement for tracks in a playlist.

    Data Collection:
        - Snapshot track popularity scores daily
        - Store: track_id, date, popularity_score

    Analysis:
        - Did tracks cross 20 threshold?
        - Did tracks cross 30 threshold?
        - What % of tracks achieved milestones?

    Returns:
        {
            'pct_reached_20': float,
            'pct_reached_30': float,
            'avg_sps_increase': float,
            'efficiency_verdict': 'High' | 'Medium' | 'Low'
        }
    """
    # Get historical SPS data
    snapshots = get_sps_snapshots(playlist_id, days=timeframe_days)

    results = {
        'tracks_analyzed': 0,
        'reached_20': 0,
        'reached_30': 0,
        'reached_60': 0
    }

    for track in snapshots:
        initial_sps = track.sps_history[0]
        max_sps = max(track.sps_history)

        results['tracks_analyzed'] += 1

        if initial_sps < 20 and max_sps >= 20:
            results['reached_20'] += 1
        if initial_sps < 30 and max_sps >= 30:
            results['reached_30'] += 1
        if initial_sps < 60 and max_sps >= 60:
            results['reached_60'] += 1

    # Calculate percentages
    # ... (return formatted results)
```

**Note:** SPS influenced by recency (last 28-30 days carry most weight). Requires ongoing monitoring.

---

## 17. TODO-007: Network Analysis Tools

### Priority: 🟡 MEDIUM | Effort: 5-7 days (research-intensive)

**Goal:** Identify “Low and Slow” botnets via graph-based collusion detection

**The Evolution:**

**Old-school bot farms (detectable):**

- Single track streamed millions of times
- Obvious spike in single day
- Easy to flag

**Modern “Professional Tier” botnets (harder to detect):**

- Distribute streams across massive catalogs
- Each track gets small number of plays
- Simulate organic behavior (pauses, skips, account aging)
- Use “Low and Slow” strategy to avoid alarms

### Detection Methodology

**Transaction Graph Construction:**

**Nodes:** User accounts, Artists, Tracks
**Edges:** Listening events (User → Track → Artist)

**Red Flag Pattern:**

If 1,000 “different” accounts (different IPs, different locations) all stream the same niche tracks at similar timestamps:

```
P(organic) = Probability all 1,000 independently discovered rare track
           ≈ 0 (statistically impossible)
```

### Implementation Specification

**File to create:** `forensic_metrics/network_analyzer.py`

**Dependencies:**

```
networkx
torch-geometric (for GNN implementation)
scikit-learn
```

**Conceptual algorithm:**

```
import networkx as nx

def build_transaction_graph(listening_events):
    """
    Constructs graph from streaming data.

    Requires:
        - User IDs
        - Track IDs
        - Timestamps
        - Geographic data (if available)
    """
    G = nx.Graph()

    for event in listening_events:
        # Add nodes
        G.add_node(event.user_id, type='user')
        G.add_node(event.track_id, type='track')

        # Add edge with weight = frequency
        G.add_edge(event.user_id, event.track_id,
                   timestamp=event.timestamp,
                   weight=1)

    return G

def detect_collusive_clusters(graph):
    """
    Uses community detection to find suspicious patterns.

    Methods:
        - Louvain algorithm for community detection
        - Temporal synchronization analysis
        - Geographic clustering analysis

    Returns:
        {
            'suspicious_clusters': List[cluster_id],
            'cluster_sizes': List[int],
            'temporal_sync_score': float,
            'verdict': 'Clean' | 'Suspicious' | 'Botnet'
        }
    """
    from networkx.algorithms import community

    # Detect communities
    communities = community.louvain_communities(graph)

    # Analyze each community for bot signatures
    # - Temporal clustering (all streams within minutes)
    # - Geographic clustering (all from data centers)
    # - Track obscurity (streaming unknown tracks)

    # FULL IMPLEMENTATION REQUIRED
```

**Note:** This is research-level work. May require collaboration with academic researchers or security firms specializing in fraud detection.

---

# PART V: OPERATIONS

## 18. Environment Configuration

### Required Environment Variables

**For Data Collection:**

```
SPOTIFY_CLIENT_ID=abc123xyz...
SPOTIFY_CLIENT_SECRET=def456uvw...
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8080/
```

**For Curator Enrichment:**

```
SERP_API_KEY=xyz789abc...
GROQ_API_KEY_1=gsk_...
GROQ_API_KEY_2=gsk_...
GROQ_API_KEY_3=gsk_...
GROQ_API_KEY_4=gsk_...
GROQ_API_KEY_5=gsk_...
LANGCHAIN_API_KEY=ls__...  # Optional (for tracing)
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
```

**For Future Components:**

```
CHARTMETRIC_API_KEY=...  # For historical follower data
OPENAI_API_KEY=...       # For S-BERT embeddings (alternative)
```

### Configuration Files

**curator_enrichment/config.py:**

- Google Custom Search base URL

**curator_playlists/config.py:**

- `MAX_RETRIES = 7`
- `CURATOR_START_INDEX = 0`
- `CURATOR_END_INDEX = 100`

**scripts/data_collection/config.py:**

- `KEYWORDS` array (search terms)
- `REQUEST_DELAY = 0.15`
- `MAX_PLAYLISTS_PER_KEYWORD = 1000`

---

## 19. Deployment Workflow

### Initial Data Collection (Step-by-Step)

**Step 1: Keyword Search**

```
cd scripts/data_collection
python main.py
# Output: data/playlists_final.csv (~8,000 playlists)
# Runtime: 10-15 minutes
```

**Step 2: URL Validation**

```
cd scripts/csv_processing
# Edit INPUT_FILE in multiprocessing-spotify-validator.py
python multiprocessing-spotify-validator.py
# Output: processed/spotify_data_validated.csv
# Runtime: 2-4 hours (16 processes)
```

**Step 3: Filter Valid Playlists**

```
import pandas as pd
df = pd.read_csv('processed/spotify_data_validated.csv')
valid = df[df['is_playlist'] == 'valid playlist']
valid.to_csv('spotify_valid_playlists.csv', index=False)
# Result: ~5,800 valid playlists
```

**Step 4: Curator Deep Analysis**

```
cd curator_playlists
# Edit CURATOR_START_INDEX, CURATOR_END_INDEX in config.py
python main.py
# Output: data/Playlists.csv (with Focus Scores)
# Runtime: Varies (API rate limits)
```

**Step 5: Contact Enrichment**

```
cd curator_enrichment
# Populate curators list in agent.py from Playlists.csv
python agent.py
# Output: Playlisters.csv
# Runtime: ~10 minutes for 84 curators
```

### Weekly Refresh (Combat Data Entropy)

Playlists decay:

- Curators delete playlists
- Links break
- ~30% churn over 6 months

**Refresh workflow:**

1. Re-run URL validator on existing Playlists.csv
2. Mark newly invalid playlists
3. Re-run curator deep-dive for curators with failed links
4. Update Focus Scores (may change if tracks removed)
5. Regenerate Gumroad product files

---

## 20. Known Issues & Limitations

### LIMIT-001: No Historical Data

**Issue:** Current system is a snapshot, not time-series

**Impact:** Cannot detect growth patterns, churn rates, or SPS movements without historical tracking

**Mitigation:** Implement weekly snapshots, store in time-series database (PostgreSQL + TimescaleDB)

### LIMIT-002: No Audio Feature Analysis

**Issue:** Genres extracted from artist metadata, not actual audio analysis

**Impact:** Cannot calculate ellipsoid diversity metric

**Mitigation:** Integrate Spotify Audio Features API (batch endpoint supports 100 tracks/request)

### LIMIT-003: Agent Rate Limits

**Issue:** Curator enrichment limited to ~20 curators/hour

**Causes:**

- SerpAPI: 100 searches/hour (free tier)
- Gemini API: 60 requests/min (Vertex AI)
- Manual delays: 2-3 seconds to prevent detection

**Mitigation:** Upgrade to paid SerpAPI tier, implement intelligent caching

### LIMIT-004: Spotify API Pagination

**Issue:** Curator deep-dive limited to first 50 playlists

**Impact:** Curators with 100+ playlists (like “jr” with 1,235) not fully analyzed

**Mitigation:** Implement continuation tokens, or sample top N by follower count

### Data Quality Concerns

**Unmapped genres:**

- Frequency: ~5-10% of genres
- Impact: Focus scores may be inaccurate for edge genres
- Solution: Expand mapping table, use LLM for classification

**Curator name variations:**

- Frequency: ~20% of curators
- Impact: Agent may miss social handles
- Solution: Already addressed via “lenient matching” in prompts

**Deleted playlists:**

- Frequency: ~30% churn over 6 months
- Impact: Stale data
- Solution: Weekly re-validation (already planned)

---

# PART VI: DEVELOPMENT ROADMAP

## Priority 1: CRITICAL (Next 2 Weeks)

### DEV-001: Historical Data Collection Infrastructure

**Effort:** 3-5 days

**Requirements:**

- Set up PostgreSQL with TimescaleDB extension
- Create schema for follower snapshots
- Implement daily cron job
- Migrate existing CSV data

**Deliverables:**

- `infrastructure/timeseries_db_setup.sql`
- `cron_jobs/daily_snapshot.py`
- Migration script for backfilling

**Why this is blocking:** Without historical data, cannot implement Z-score monitor or churn detector (TODO-001, TODO-002)

---

### DEV-002: Implement Z-Score Monitor

**Effort:** 2-3 days
**Dependencies:** DEV-001

**Deliverables:**

- `forensic_metrics/z_score_monitor.py`
- Add columns to Playlists.csv: `z_score_max`, `bot_injection_flag`, `growth_pattern`
- Unit tests for edge cases

---

### DEV-003: Implement Churn Detector

**Effort:** 2-3 days
**Dependencies:** DEV-001

**Deliverables:**

- `forensic_metrics/churn_detector.py`
- Add column: `retention_score` (1-5 scale)
- Visualization: Retention histogram

---

## Priority 2: HIGH (Next Month)

### DEV-004: Audio Features Integration

**Effort:** 3-4 days

**Implementation:**

```
# Spotify API endpoint
GET https://api.spotify.com/v1/audio-features/{id}

# Batch version (up to 100 tracks):
GET https://api.spotify.com/v1/audio-features?ids=...
```

**Deliverables:**

- `sonic_intelligence/audio_features_fetcher.py`
- Update `curator_playlists/fetch_data.py` to collect features
- New output: `Track_Audio_Features.csv`

---

### DEV-005: S-BERT Semantic Matching

**Effort:** 2-3 days
**Dependencies:** None (runs on existing data)

**Deliverables:**

- `sonic_intelligence/semantic_matcher.py`
- Add columns: `semantic_alignment`, `stuffing_flag`
- Requirements.txt: Add `sentence-transformers`, `scikit-learn`

---

### DEV-006: FAL Auditor

**Effort:** 1-2 days

**Deliverables:**

- `forensic_metrics/fal_auditor.py`
- Add columns: `resonance_score`, `empty_fal_count`, `fal_verdict`

---

## Priority 3: MEDIUM (Next Quarter)

### DEV-007: Ellipsoid Metric Calculator

**Effort:** 5-7 days
**Dependencies:** DEV-004 (audio features)

**Research required:**

- Baseline calibration (analyze 100+ known-good playlists)
- LDA vs PCA for dimensionality reduction
- Genre-specific thresholds

---

### DEV-008: SPS Milestone Tracker

**Effort:** 2 days
**Dependencies:** DEV-001 (historical data)

---

### TODO-009: Generate Curator Exodus Lists

**Effort:** 1 day

**Goal:** Extract high-quality curators for cooperative recruitment

**Filter criteria:**

```
SELECT * FROM Playlists
WHERE
    musinique_focus_score > 70
    AND primary_genre_diversity <= 3
    AND total_playlists BETWEEN 10 AND 50
    AND followers > 10000
    AND corporate_flag = FALSE
    AND last_updated < 30_days
ORDER BY musinique_focus_score DESC
```

**Target genres:**

- Jazz (expected: 100-300 curators)
- Ambient/Experimental (50-150)
- Folk/Americana (150-300)
- Metal (100-200)
- Classical (50-100)
- Electronic/Techno (100-200)

**Outreach message:**

> “You’re curating on Spotify for free, building their value. What if you curated for a cooperative you owned instead? We’ve built the infrastructure. You provide the expertise. Artists pay membership. Listeners pay subscription. You get paid for curation. Interested?”

---

## Priority 4: Refactoring & Testing

### REFACTOR-001: Unify Data Pipeline

**Current state:** Fragmented scripts with manual CSV passing

**Goal:** Single orchestration script

**Proposed:** `pipeline_orchestrator.py`

```
def run_full_pipeline(config):
    """
    End-to-end execution from keywords to final CSVs.

    Steps:
        1. Keyword search
        2. Metadata enrichment
        3. URL validation
        4. Curator analysis
        5. Contact discovery
        6. Genre mapping
        7. Focus score calculation
        8. Sampling for Gumroad
    """
```

---

### REFACTOR-002: Standardize Error Handling

**Current state:** Inconsistent (some print, some raise, some ignore)

**Goal:** Unified logging

**Proposed:** `utils/error_handler.py`

```
import logging

class MusiниqueError(Exception):
    """Base exception for Musinique platform."""
    pass

class SpotifyAPIError(MusiниqueError):
    """Raised when Spotify API fails after retries."""
    pass

class ValidationError(MusiниqueError):
    """Raised when data validation fails."""
    pass
```

---

### DEV-009: Add Unit Tests

**Coverage goal:** 70%

**Priority test suites:**

- `tests/test_focus_score.py` - Score calculation edge cases
- `tests/test_genre_mapping.py` - Mapping logic, unmapped handling
- `tests/test_z_score.py` - Statistical anomaly detection
- `tests/test_spotify_validator.py` - URL validation patterns

---

## 21. Research Infrastructure Goals

### Strategic Direction: Beyond Spotify Optimization

Musinique is not just a “better SubmitHub.” It’s **research infrastructure for studying algorithmic exploitation and building cooperative alternatives.**

### Three-Phase Vision

**Phase 1: Expose the System**

- Release PFC (Perfect Fit Content) analysis
- Quantify ghost artist prevalence in mood playlists
- Calculate displaced revenue (€X million annually)
- Media: Pitch to Pitchfork, NPR, Billboard

**Phase 2: Map the Alternatives**

- Database of library streaming programs (50+ worldwide)
- Existing cooperatives (Catalytic Sound, Resonate, Ampled)
- Public funding opportunities (arts councils, grants)
- Independent radio (college, community stations)

**Phase 3: Build the Infrastructure**

- Streaming platform toolkit (audio CDN, payment processing)
- Governance tools (voting, transparency dashboards)
- Discovery interfaces (context-rich, human-curated)
- AI music tools FOR artists (practice tracks, backing tracks) - not replacing them

---

## 22. Product Strategy

### Current Products (Gumroad)

**Product 1: Indie Playlister Starter Pack**

- Price: $0+ (Pay What You Want)
- Content: 15 curators + 1,000 playlists (stratified sample)
- Goal: Lead magnet, email capture, prove niche coverage

**Product 2: Complete Curator Database**

- Price: $25
- Content: 84 curators (full contact) + 5,800+ playlists
- Value prop: “36 weeks of manual research for $25”
- Positioning: Time-savings, data quality

### Future Products (Roadmap)

**TODO-010: Integrity Audit Reports (Premium)**

- Price: $10/month subscription
- Features:Weekly playlist health reports (updated focus scores)Bot injection alerts (Z-score spikes)Churn pattern warnings (payola detection)SPS milestone tracking for submitted tracksPersonalized recommendations (which playlists match YOUR sound)

**TODO-011: PFC Exposure Package**

- Price: Free (media/research)
- Target: Journalists, regulators, artists
- Contents:Analysis: X% of mood playlists contain ghost artistsLabel patterns: Epidemic Sound, Firefly prevalenceRevenue calculations: €Y million displaced annuallyCorporate curator dominance: Z% of total reach
- Goal: Media coverage, regulatory attention

---

# APPENDIX: QUICK REFERENCE

## Command Reference

**Full pipeline execution:**

```
# Step 1: Keyword search
cd scripts/data_collection && python main.py

# Step 2: URL validation
cd ../csv_processing && python multiprocessing-spotify-validator.py

# Step 3: Curator analysis
cd ../../curator_playlists && python main.py

# Step 4: Contact discovery
cd ../curator_enrichment && python agent.py
```

**Individual component testing:**

```
pytest tests/test_focus_score.py
python curator_enrichment/agent.py
python scripts/csv_processing/spotify_validator.py  # Debug mode
```

**Data inspection:**

```
import pandas as pd

df = pd.read_csv('data/Playlists.csv')

# High-quality playlists
df[df['musinique_focus_score'] > 85].head()

# Suspicious playlists (low score, high followers)
df[(df['musinique_focus_score'] < 40) & (df['followers'] > 50000)]
```

---

## File Path Quick Reference

**Need to change curator range:**
→ `curator_playlists/config.py` → `CURATOR_START_INDEX`, `CURATOR_END_INDEX`

**Need to modify Focus Score weights:**
→ `curator_playlists/utils.py` → `musinique_focus_score()` function → Change 0.45, 0.30, 0.25

**Need to update genre mapping:**
→ `MetaData/Music_Genres_unique.csv` → Add rows: Subgenre, Primary Genre

**Need to change search keywords:**
→ `scripts/data_collection/config.py` → `KEYWORDS` array

**Need to adjust validator speed:**
→ `scripts/csv_processing/multiprocessing-spotify-validator.py` → `NUM_PROCESSES`, `SAVE_INTERVAL`

**Need to modify agent prompt:**
→ `curator_enrichment/prompts.py` → `AGENT_PROMPT` template

---

## Critical Metrics Checklist

**✅ Implemented:**

- Focus Score (genre coherence audit)

**❌ Missing (TODO):**

- Z-Score (bot injection detection)
- Retention Score (payola pattern detection)
- FAL Resonance (algorithmic impact validation)
- Semantic Alignment (playlist stuffing detection)
- Ellipsoid Volume (sonic chaos quantification)
- SPS Milestones (algorithmic efficiency measurement)

---

## What You’ve Already Built (Summary)

### Core Infrastructure (Operational)

**Data collection pipeline:** Keyword search → Metadata fetch → CSV export
**URL validation suite:** Multi-process Playwright with anti-bot masking
**AI research agent:** LangGraph contact discovery with structured extraction
**Scoring system:** Mathematical Focus Score (0-100) for playlist quality
**Genre intelligence:** 5,000+ subgenres mapped to 20 primary categories

### What This Enables Today

✅ Artists can filter 5,800 playlists by Focus Score
✅ Artists can identify niche-focused curators vs “cleaning lady” dumps
✅ Artists have verified contact info (Instagram, Twitter, submission forms)
✅ Database updated weekly (combat link decay)

### What’s Missing (The “Consumer Reports” Layer)

❌ Bot injection detection (Z-score spikes)
❌ Payola pattern detection (7/14/30-day churn)
❌ Algorithmic resonance (FAL audits)
❌ Sonic coherence (ellipsoid chaos metric)
❌ Semantic deception (S-BERT mismatch)

**These are the tools that transform “playlist database” into “fraud detection system.”**

---

## Your Actual Contribution (Strategic Framing)

### You’re NOT Building:

❌ Music industry insider product (you said so yourself)
❌ Tool to win at Spotify’s game (that’s impossible)
❌ Service for broken system (that’s exploitation)

### You ARE Building:

✅ **Computational skeptic** applying data science to opaque systems
✅ **Infrastructure builder** enabling cooperative alternatives
✅ **Evidence-based designer** grounding work in research
✅ **Educator** translating complexity for public understanding

### The Work Is:

1. **Expose** the exploitation (release PFC analysis)
2. **Map** the alternatives (library/radio/coop databases)
3. **Build** the infrastructure (cooperative platform tools)
4. **Validate** what works (research, measurement, iteration)

**This is the recipe. This is the path. This is what your data enables.**

---

**MUSINIQUE PLATFORM - Internal Technical Documentation**
Version 1.0 | February 2026 | Musinique Engineering

*“Humans make music. Bots check data.”*
