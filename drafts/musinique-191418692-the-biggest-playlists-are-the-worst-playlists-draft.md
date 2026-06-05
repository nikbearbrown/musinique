---
title: "The Biggest Playlists Are the Worst Playlists"
subtitle: ""
publication: "musinique"
book: "Musinique"
draft_status: "rewrite"
rewrite_voice: "Baldwin/Subby Substack essay"
source_article: "musinique-191418692-the-biggest-playlists-are-the-worst-playlists.md"
source_file: "musinique-191418692-the-biggest-playlists-are-the-worst-playlists.md"
post_id: "191418692.the-biggest-playlists-are-the-worst"
post_date: "2026-03-19T04:36:15.451Z"
cover_image: "https://substack-post-media.s3.amazonaws.com/public/images/5e6b936d-f200-48e5-b2e0-1a92e8b748c3_1456x816.png"
excerpt: "Lance Allen is an instrumental guitarist from Tennessee who built a streaming career that paid his mortgage. He did it by doing something that sounds simple and turns out to be almost impossible: he pitched only to playlists whose audiences had specifically chosen to hear acoustic guitar. Not “chill music.” Not “relaxing vibes.” Not playlists with 100,000..."
---
# The Biggest Playlists Are the Worst Playlists

_Draft rewrite for Musinique Substack._

![](https://substack-post-media.s3.amazonaws.com/public/images/5e6b936d-f200-48e5-b2e0-1a92e8b748c3_1456x816.png)

Lance Allen is an instrumental guitarist from Tennessee who built a streaming career that paid his mortgage. He did it by doing something that sounds simple and turns out to be almost impossible: he pitched only to playlists whose audiences had specifically chosen to hear acoustic guitar.

Not “chill music.” Not “relaxing vibes.” Not playlists with 100,000 followers and titles that gestured vaguely at a mood. He found the playlists where every track was acoustic guitar, where every listener had self-selected for that sound, and he pitched there. His placement on Spotify’s editorial playlist “Acoustic Concentration” in 2016 started a chain of algorithmic momentum that compounded for years. As he told American Songwriter, it eventually made him possibly the world’s most-streamed acoustic guitarist, with over 100 million streams. The algorithm learned who his music was for because the listeners generating the data were the right listeners. Every save confirmed the signal. Every Discover Weekly cycle found more people like the ones who had already saved. The momentum built from coherence.

Thanks for reading Musinique! Subscribe for free to receive new posts and support my work.

I have been thinking about Lance Allen since the day the Musinique database returned a number that made me recheck the query.

We scored 5,859 playlists across 84 curators for genre coherence, using the Musinique Focus Score. I expected the usual distribution. What I found instead was a structural inversion that explains why Lance Allen’s discipline was not just good strategy but the only strategy that could have worked, and why almost every other independent artist is being guided toward the opposite.

42.7 percent of all listener reach in our database sits behind playlists that would damage an artist’s algorithmic profile. 10.8 percent sits behind playlists that would help. The ratio is nearly 4 to 1. The playlists most visible to artists, the ones with the highest follower counts, are on average the playlists most likely to teach Spotify’s recommendation engine the wrong things about who the music is for.

Lance Allen avoided those playlists by instinct and discipline. The data now shows what he was avoiding, and how much of the ecosystem it covers.

---

## A Playlist Called “Indie Folk Instrumental” That Contains Drone Metal

There is a playlist on Spotify called “Woodland | Indie Folk Instrumental.” It has 34,205 followers and a Focus Score of 23 out of 100. An acoustic guitarist looking for playlists to pitch to would see that title and recognize it as an exact description of their music. They would see the follower count and conclude the playlist is worth a Submithub credit.

Here is what their song would sit next to: acoustic pop, alt country, ambient, bluegrass, celtic, chamber music, classical, contemporary classical, dream pop, drone metal, free jazz, jazz fusion, lo-fi hip hop, musique concrete, neoclassical, post-rock, shoegaze, slowcore. Thirty-one subgenres in total.

Drone metal is on a playlist called “Indie Folk Instrumental.” Free jazz is on it. Musique concrete, the mid-twentieth-century French practice of composing with recorded environmental sound, is on it. A listener who followed for drone metal hears the folk song and skips. A listener who followed for free jazz hears the voice and moves on. Each skip enters the collaborative filtering model that Spotify uses to decide who else should hear this artist’s music. The model does not know the playlist was incoherent. It knows a listener rejected the track. It adjusts.

Lance Allen would not have pitched to “Woodland.” He would have looked past the title and the follower count and found the playlist where the audience matched the music. But Lance Allen had years of experience and an unusual willingness to turn down reach in favor of fit. Most independent artists do not have that experience. They have a title, a follower count, and the advice of every promotion guide they have ever read: pitch to the biggest playlists you can find.

Four months of writing. A Submithub credit. Thirty-one betrayals of a two-word promise.

---

## How the Score Works

We have not published the internal methodology of the Focus Score before. Here is the logic.

The score has three components, each normalized to a 0-to-100 scale and combined as a weighted sum. Genre Breadth carries the heaviest weight. Genre Density is second. Artist Focus is third. The exact weights and the full mathematical specification will be published in a forthcoming academic paper. What follows is how each component thinks.

**Genre Breadth** counts the number of distinct primary genres on a playlist and applies a logarithmic decay function. Not linear. Logarithmic. This is the design decision that matters most, and it reflects the mechanism it measures.

A playlist with one genre scores the maximum. A playlist with two genres has already lost significant ground. A playlist with five genres has lost more than half. A playlist with fifty or more genres scores zero. The curve is steep at the top and shallow at the bottom, because the first dilution is the most damaging. Going from one genre to two means a second listener community has been introduced. Going from 30 genres to 31 has not meaningfully changed the audience composition. The penalty is front-loaded because the damage is front-loaded. A playlist that was pure and adds one wrong genre has broken something. A playlist that was already chaotic and adds one more genre has changed nothing.

**Genre Density** divides total tracks by number of primary genres. A playlist with 100 tracks and one genre goes deep. A playlist with 100 tracks and 20 genres is sampling. The component rewards depth over breadth, on the premise that a playlist which commits to a sound, stacking track after track in the same genre, has built an audience that selected for that sound specifically. A playlist that samples many genres at shallow depth has built an audience that selected for variety, which means the audience is, by definition, genre-diverse, which means their behavioral responses to any given track are unpredictable.

**Artist Focus** measures the ratio of unique artists to total tracks. A playlist where the same artists appear repeatedly scores high. A playlist where every track is by a different artist scores low. This component captures whether a curator builds around a consistent artist community or aggregates content from everywhere. Repetition signals a curatorial identity. Maximum diversity signals a submission inbox left open.

For Woodland, eleven primary genres drives Genre Breadth well below the midpoint. Ninety-nine tracks across those eleven genres produces a Genre Density score near the floor. Eighty-eight unique artists out of 99 tracks, meaning almost no repetition, drives Artist Focus into the lowest range. The composite: 23.

For Root Note Records’ “Cozy Acoustic Instrumentals,” one primary genre drives Genre Breadth to the maximum. Enough tracks in that single genre to exceed the density threshold drives Genre Density to the maximum. Enough artist repetition to signal a committed curatorial identity drives Artist Focus to the maximum. The composite: 100.

The difference between 23 and 100 is not aesthetic. It is predictive. It predicts the behavioral data those audiences will produce before the artist spends a credit to find out. One number says: the listeners on this playlist arrived for the same reason your music is there. The other says: they arrived for eleven different reasons, and yours is one of them.

Lance Allen’s playlists would have scored near the top. The playlists that most artists find first score near the bottom. The Focus Score makes that difference visible. Until it existed, the information lived nowhere the artist could access it.

---

## The Growth Loop That Builds the Trap

A playlist that accepts Hip Hop and Folk and Electronic and Pop and Metal casts a wider net than a playlist that accepts only acoustic guitar instrumentals. The wider net catches more followers. More followers make the playlist more visible. More visibility attracts more submissions. More accepted submissions from more genres widen the net further. At each turn, two things happen at the same time: the follower count rises and the genre coherence degrades.

The growth is the degradation. They are not separate processes. They are the same process, and the artist can see only one side of it.

This is why 42.7 percent of all reach in our database sits behind playlists with Focus Scores below 30. The playlists that grew fastest are the playlists that accepted most broadly, which means they are the playlists with the most followers, which means they are the playlists an artist finds first, which means they are the playlists an artist submits to, which means they are the playlists that will introduce the artist’s music to an audience assembled from six or eight or twelve genre communities, none of whom arrived for the artist’s genre.

The top 1 percent of playlists by follower count, 58 playlists, control 64.8 percent of all reach in the database. Their average Focus Score is 38.7. The system was not designed to produce this outcome. It was designed in a way that makes this outcome inevitable. For the artist absorbing the cost, the distinction is academic.

---

## How It Happens to You

Every step here is rational. Every step is standard industry advice. I have watched the pattern in the data enough times to describe the sequence exactly.

You finish your release. You have two to four weeks before Spotify’s recommendation engine forms a stable model of who your music is for. Everything that happens in this window, every stream, every save, every skip, carries disproportionate weight in every algorithmic decision that follows.

You open Submithub. You sort by follower count, because follower count is the number visible to you. You find playlists whose names match your genre. “Indie Folk.” “Chill Acoustic.” “Singer-Songwriter Vibes.” The names feel right. The numbers feel significant. You submit.

You do not check what is actually on those playlists. You cannot check. No tool available to you measures whether “Indie Folk” by OurVinyl, with 18,593 followers and a Focus Score of 33, mixes Country, Folk, Pop, and Religious music under a two-word genre label. No tool tells you that “sleepy indie songs” with 14,993 followers spans twelve primary genres including Hip Hop, Metal, and Avant-Garde. The information does not exist in any form you can access. You are making the most consequential marketing decision of your release cycle based on a title and a number, and neither one measures the thing that matters.

A curator accepts your track. Streams begin to arrive. You watch the count rise in Spotify for Artists and feel the work paying off.

What you do not watch, because it moves slower, hides deeper in the dashboard, and no one told you to look, is the save rate. The repeat-listen rate. The Discover Weekly placement frequency. Those numbers are telling a different story. The streams are real. The listeners are real. But most of them arrived for a genre that is not yours. They skip, or they listen once and never return, and each of those responses is a signal to the algorithm that says: this track does not belong with this audience.

Two months later, the campaign is over. The stream count was respectable. The Discover Weekly cycle is quieter than it was before the release. The foundation you needed to build in the first weeks was not built. It was contaminated, by streams that looked like the thing you wanted.

You conclude that the algorithm is unfair, or that your music was not strong enough, or that you need to spend more on the next campaign. None of those are what happened. What happened is that the ecosystem’s visibility structure guided you, rationally, toward the playlists that would hurt you most. You followed the path that every tutorial and every promotion service told you to follow. The path led here.

Lance Allen followed a different path. He chose the playlists where the audience already wanted what he made. He turned down reach for fit. The algorithm rewarded him for it, because coherent audiences produce the behavioral data that the algorithm needs to compound. The standard advice points artists away from Lance Allen’s path. The data shows that his path was the only one that leads where artists want to go.

---

## 137,876 Followers and a Perfect Score

Root Note Records is an instrumental folk and acoustic label that runs 56 playlists on Spotify. One of them is called “Non-AI Instrumental Music,” a name that carries more information about the curator’s intent than a million followers could. This is a person who thought carefully enough about what belongs on a playlist to define it not just by genre but by provenance. Acoustic instrumentals made by humans.

“Cozy Acoustic Instrumentals” has 35,466 followers and a Focus Score of 100. Every artist in the same sonic world. Every listener there for the same reason. “Cozy Fall Instrumentals”: 19,014 followers, perfect score. “Calming Guitar Instrumentals”: 2,874 followers, perfect score. Seven of their 56 playlists score a perfect 100. Median across the catalog: 85.8. Total reach across all 56 playlists: 137,876.

Filtr US, Sony Music Entertainment’s playlist operation, runs 96 playlists with a combined reach of 9.19 million and a median Focus Score of 33. Three of their playlists score above 55. Those three hold 3.7 percent of their total reach. Fifty-eight playlists score below 35. Those hold 64 percent.

The ratio of Filtr US’s reach to Root Note Records’ reach is 67 to 1. An acoustic guitarist searching for playlists to pitch to will find Filtr US on the first page and Root Note Records possibly never. The 35,466 listeners on “Cozy Acoustic Instrumentals” would hear that guitarist’s track and respond as people who chose acoustic instrumentals. The hundreds of thousands on Filtr US’s “Feel Good Happy Hits,” Focus Score 21.3, would hear it as an interruption in a stream they chose for a different reason.

Root Note Records is the kind of curator Lance Allen would have found. Filtr US is the kind of curator the standard advice would have sent him to. The 67-to-1 reach ratio is the reason most artists never make the choice he made. The Focus Score data is the reason they should.

---

## “Pure Country” Is Not Pure Country

A curator called “Pure Country” operates 218 playlists with a combined reach of 1.6 million. The name is a genre declaration. Ninety-nine percent of their playlists contain Country somewhere in the genre profile.

Their second-largest playlist, “Beach Playlist 2025,” has 106,223 followers and a Focus Score of 21.7. Its genres include Country, Easy Listening, Electronic, Folk, and Hip Hop. Their third-largest, “Pop Rock Workout 2025,” has 86,436 followers and a Focus Score of 22.4: Country, Electronic, Folk, Hip Hop, Metal, Pop, Rock. A country songwriter who sees “Pure Country” and 1.6 million reach and pitches to the highest-follower lists has sorted for the worst outcomes. The same sorting mechanism. The same trap.

Some of their playlists deliver on the name. “Best Country Love Songs 2025” scores 69.8. “2000 Country Music” scores 71.3. But those are not the playlists with the big numbers. The big numbers belong to the playlists that grew by accepting everything.

---

## Twenty-Nine Percent of Playlists Have Not Been Updated in Two Years

The reach-quality trap is compounded by abandonment at a scale I did not expect to find.

Not a single playlist in the database was updated in the 30 days prior to our analysis window. Six percent were updated in the prior 30 to 90 days. Twenty-nine percent have not been updated in over two years. Active playlists average a Focus Score of 53.2. Abandoned playlists average 39.7, because maintaining coherence requires ongoing curatorial judgment, and when the judgment stops, the coherence decays while the follower count stays.

Two hundred and forty playlists are both abandoned and visible: not updated in a year or more, 1,000 or more followers. Combined reach: 4.46 million. Rockstar Games’ “Non-Stop-Pop FM (GTAV)” has 346,176 followers, a Focus Score of 21.1, and has not been updated in over eight years. A museum exhibit that Spotify indexes as a living playlist. An artist who submits to it is spending a credit to pitch into eight years of silence. The follower count did not mention that.

---

## The Volume Objection

You need volume. You need the numbers in the first two weeks. Focused mid-tier playlists cannot generate enough momentum to trigger editorial consideration.

This is partially true. Volume matters. But engagement quality determines whether volume builds or dissipates. Five thousand streams with a 20 percent save rate is 1,000 listeners who decided the track was worth keeping. Fifty thousand streams with a 1 percent save rate is 49,500 listeners who decided it was not. The editorial team can see both numbers. The algorithm can see both numbers. The campaign that chases volume from incoherent playlists is building a documented record of low engagement, visible to every system that determines what happens next. The stream count looks like progress. The save rate is the truth.

---

## What Is Actually Being Lost

Every article in this series has asked some version of the same question. The Confusion Window asked what is lost when Release Radar’s trust architecture is exploited for fraudulent royalties. The answer was the listener’s trust, liquidated at $0.004 per stream. “The Ghost That Followed Back” asked what is lost when engagement metrics reward constructed personas indistinguishable from real people. The answer was the distinction between connection and capture.

The reach-quality inversion asks: what is lost when the ecosystem’s visibility structure systematically directs artists toward the playlists most likely to damage them?

The answer is the career that was supposed to compound.

Not the streams. The streams happened. Not the campaign budget. That was spent. What is lost is the two-to-four-week window after a release when the algorithm is listening most carefully to who the music is for, spent generating data from the wrong audience, building a collaborative filtering profile that points nowhere specific, teaching Spotify to send the track to people who will confirm by their skipping that the track does not belong where the algorithm put it. That window does not come back. The artist who spent it on the wrong playlists does not get a second first impression with the recommendation engine.

The particular cruelty is that it does not look like failure while it is happening. It looks like progress. The stream count rises. The save rate stays flat. Discover Weekly gets quieter. Release Radar reaches fewer people. And the artist, reading the stream count as evidence that the system is working, does not know that the system is learning the wrong lesson about their music. And that the lesson, once learned, is difficult to unlearn.

Only 14 of the 84 curators in our database maintain an average Focus Score above 50. Fourteen out of eighty-four. That is the fraction of the ecosystem where the curator’s growth practice and the artist’s algorithmic interest point in the same direction.

Root Note Records is one of those fourteen. They are invisible in the follower-count framework. In the Focus Score framework, they are among the most valuable curators in the database. That gap, between what is visible to the artist and what is real for the artist, is where careers quietly come apart.

Lance Allen found his way to the right side of that gap through years of discipline and a willingness to say no to playlists that looked like opportunities and were not. His career compounded because his data compounded. The playlists that would help him held 10.8 percent of the reach. The playlists that would hurt him held 42.7 percent. He navigated a 4-to-1 trap without a map.

The playlists that look the best are, on average, the worst. The playlists that look unremarkable are, on average, the best. The artist who follows the standard advice follows it toward the quiet erosion of the thing they were trying to build. And the information that would let them choose differently, the genre composition of the playlist, the coherence of its audience, whether the people listening arrived for the same reason the music is there, has not been available to them in any form.

It is now.

---

*The Musinique Focus Score is calculated from three components: Genre Breadth (logarithmic decay), Genre Density, and Artist Focus. The composite ranges from 0 to 100. The exact weights and full mathematical specification will be published in a forthcoming academic paper. All statistics are derived from the Musinique database (5,859 playlists, 84 curators, 36,000+ unique tracks) as of March 2026. The database covers a meaningful but not comprehensive sample of the independent playlist ecosystem. The findings describe a structural pattern that is clear in the data. We will continue to expand the dataset and refine the methodology, and we will publish what we find as we find it, including the parts that surprise us.*

Thanks for reading Musinique! Subscribe for free to receive new posts and support my work.

---

## Research Addendum (2026-06-03)

**Research date:** 2026-06-03

**Topic tags:** spotify, theory, cognition

**Research notes:**
- Spotify-related claims should distinguish editorial pitching, algorithmic recommendation, playlist exposure, and paid/opt-in tools such as Discovery Mode. Treating them as one black box weakens the argument.
- Spotify defines artificial streaming around listening intent and manipulation, including bots/scripts and paid services that guarantee streams. For playlist-vetting pieces, the central test is whether listener behavior remains durable after exposure ends.
- Discovery Mode terms are useful because Spotify explicitly says the program does not guarantee placement, streams, new listeners, or followers. That caveat supports a careful distinction between influence, exposure, and outcome.
- Music-theory claims should keep the elements distinct: pitch organizes high/low relations, rhythm organizes duration and pulse, melody orders pitches through time, harmony stacks or relates pitches, and timbre identifies sound color.
- For guitar/theory pieces, translate notation into action. Readers need to know what their fingers, ears, and attention should do differently after the concept is introduced.
- The strongest theory writing alternates between technical naming and audible consequence: what does the concept let the musician hear, predict, vary, or repair?
- Music-cognition pieces should avoid reducing music to brain trivia. The interesting point is how perception, expectation, memory, movement, emotion, and social context make sound meaningful.
- For music-as-medicine or music-and-memory claims, keep the clinical language cautious: distinguish anecdotal therapeutic power from controlled evidence, and name the mechanism being proposed.

**Sources to verify/use:**
- [Spotify for Artists: Artificial Streaming](https://artists.spotify.com/en/artificial-streaming)
- [Spotify support: third-party services that guarantee streams](https://support.spotify.com/is-en/artists/article/third-party-services-that-guarantee-streams/)
- [Spotify support: pitching music to playlist editors](https://support.spotify.com/to/artists/article/pitching-music-to-playlist-editors/)
- [Spotify for Artists: Discovery Mode support](https://support.spotify.com/na-en/artists/article/using-discovery-mode-in-spotify-for-artists/)
- [Spotify legal: Discovery Mode self-serve terms](https://www.spotify.com/us/legal/discovery-mode-selfserve/)
- [Britannica: Essential elements of music](https://www.britannica.com/art/Essential-elements-of-music)
- [Britannica: Melody](https://www.britannica.com/art/melody)
- [Britannica: Musical composition](https://www.britannica.com/art/musical-composition)

