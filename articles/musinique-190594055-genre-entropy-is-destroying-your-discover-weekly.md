---
title: "Genre Entropy Is Destroying Your Discover Weekly."
subtitle: ""
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: "190594055.genre-entropy-is-destroying-your"
post_date: "2026-03-11T12:31:25.359Z"
is_published: "true"
source_zip: "Y0r_0oGOSoWMD3iEcEhVnA.zip"
source_html: "posts/190594055.genre-entropy-is-destroying-your.html"
source_file: "musinique-190594055-genre-entropy-is-destroying-your-discover-weekly.md"
cover_image: "https://substack-post-media.s3.amazonaws.com/public/images/47881cd9-1e32-49b0-bb92-a06fb08dec5b_1024x1024.png"
---
![](https://substack-post-media.s3.amazonaws.com/public/images/47881cd9-1e32-49b0-bb92-a06fb08dec5b_1024x1024.png)

Lance Allen is an instrumental guitarist from Tennessee. He built a career on Spotify by doing one thing with unusual discipline: he pitched exclusively to playlists that were specifically for acoustic guitar. Not “chill music.” Not “relaxing vibes.” Playlists where every track was acoustic guitar, whose listeners were there specifically for that sound. His placement on Spotify’s editorial playlist “Acoustic Concentration” in 2016 started a chain of algorithmic momentum that eventually paid his mortgage, his bills, and, as he told American Songwriter, made him possibly the world’s most-streamed acoustic guitarist with over 100 million streams.

Allen understood something about Spotify’s algorithm that most independent artists learn only after the damage is done. When the right listener hears your track, saves it, adds it to their personal playlist, and comes back to it, Spotify’s recommendation engine learns who your music is for. That learning compounds. Discover Weekly begins introducing your track to more people who resemble your existing listeners. Each new listener who fits the profile saves more often, skips less, confirms the pattern. The momentum builds not from volume but from coherence.

Thanks for reading Musinique! Subscribe for free to receive new posts and support my work.

When the wrong listener hears your track, the opposite happens. The algorithm learns the wrong thing about your music and begins sending it to the wrong people. Those people skip. The algorithm takes the skips as confirmation and recommends the track to fewer people. The profile contamination compounds in exactly the same way the profile coherence does, just in the other direction.

By December 2023, as documented in reporting on Spotify’s ghost artist program, Allen’s playlist placements had been systematically replaced by tracks from Epidemic Sound and Firefly Entertainment, production music companies that license stock music to Spotify at reduced rates. His genre-coherent algorithmic profile, built over years of disciplined pitching, had been undermined not by bad data from his own campaigns but by the platform redirecting streams from the focused acoustic playlists that had made his career. His Discover Weekly presence went quiet. The lesson of his rise and what followed it is the same: genre coherence is the mechanism by which Spotify learns to find your audience. Disrupt that coherence, whether by pitching to the wrong playlists yourself or by having the platform do it to you, and the algorithm learns to send your music somewhere it does not belong.

I was running data on the Musinique database when the other side of this pattern became clearly visible. A cluster of artists with stream counts going up and Discover Weekly placement going quiet. The playlists they had landed on had high follower counts and Focus Scores in the bottom quartile of our database. Metal next to bedroom pop next to ambient next to afrobeats, all under the same “Indie” or “Chill” label. The streams were real. The algorithmic damage was also real. And the connection between the two is how Spotify’s collaborative filtering actually works.

## How Spotify Builds Its Picture of Your Music

Spotify’s recommendation engine uses collaborative filtering as one of its core mechanisms. The system builds and continuously updates clusters of listeners who share taste profiles, then matches tracks to those clusters. Every stream a track generates is a data point attaching it to a listener profile.

If the listeners who stream a track predominantly belong to the same genre ecosystem, the track gets recommended to more listeners in that ecosystem. The collaborative filtering data is coherent. The algorithm knows where the music belongs and sends it there. Each recommendation that lands well confirms the placement. The algorithm increases the track’s weight in that ecosystem. More listeners. More saves. More confirmation.

If the listeners who stream a track are a genre-incoherent mix, assembled by a playlist that aggregates rather than curates, the collaborative filtering data becomes noise. The algorithm has seen the track streamed by a heavy metal fan, an ambient fan, a K-pop fan, and a bedroom pop fan, all on the same playlist in the same week. It cannot confidently place the track in a single listener cluster. It does not know who the music is for. Its recommendations become imprecise. The listeners it sends the track to are less likely to fit. They skip at higher rates. Each skip pulls the recommendation weight down further.

Music Tomorrow, which analyzes streaming algorithm behavior for labels and independent artists, has documented this outcome directly. A metal band released an acoustic ballad that landed on a large editorial playlist and generated genuine saves and listenership. By every visible metric it was a success. Then Spotify updated its model of who the band was for. The algorithm had learned the band’s music resonated with ballad listeners. When the rest of the catalog, primarily metal, began reaching those listeners through Discover Weekly, they encountered something that did not match what they had saved. They skipped. Algorithmic streams for the band decreased across their catalog. The success of one genre-mismatched placement had contaminated the profile the band had spent years building.

The visibility of the damage was delayed, which is part of what makes genre entropy so dangerous. Stream counts looked fine while the collaborative filtering profile degraded underneath. By the time the drop in algorithmic placement was apparent, the contamination had already propagated across the recommendation engine.

## What the Focus Score Measures

The Musinique Focus Score measures genre coherence using three components: genre breadth, which penalizes playlists with many primary genres; genre density, which measures how many tracks exist per genre, rewarding playlists that go deep into a sound rather than sampling many; and artist focus, which rewards playlists where artists appear repeatedly, indicating a curator building a consistent identity rather than aggregating content.

A playlist with a high Focus Score is a genre-coherent environment. Its listeners chose it for a specific sound. When a new track appears, they evaluate it in context. They are predisposed to stay if it belongs. They are predisposed to skip if it does not. The signal generated by that audience is clean because the audience itself is self-selected for the genre.

A playlist with a low Focus Score is genre-entropic. It has accumulated diverse content without a consistent organizing principle. Its listeners arrived from multiple genre directions. Some came for rock, some for hip-hop, some for ambient. When any given track appears, their response depends entirely on which direction they came from, not on whether the track is good. The data generated by that audience is incoherent because the audience is incoherent.

When a track lands on an entropic playlist, the collaborative filtering data generated by those streams pulls the track in multiple taste directions simultaneously. The algorithm attempts to find the cluster the track belongs to. The data points to several clusters at once. The resulting recommendation weight is diffuse. Discover Weekly does not know where to send the track. The introductions it makes are imprecise. The listeners it reaches are more likely to skip, which confirms to the algorithm that the track should be recommended to fewer people, which means fewer chances to accumulate the coherent signal that would reverse the trend.

## The Contamination Timeline

The damage accumulates over time, and it accumulates fastest in the weeks immediately following a release, which are the most algorithmically sensitive.

Early streams from the wrong listener profile set an anchor for who the track is for. Spotify’s recommendation engine is continuously updating its models, but early data carries weight because it is the first signal the algorithm has about a new release. If that signal is contaminated by genre-incoherent playlist placement, subsequent algorithmic recommendations are built on a compromised foundation. Every Discover Weekly inclusion, every Radio play, every recommendation carries the contaminated profile forward.

An artist who runs a promotion campaign in the first two weeks after a release and lands on several low-focus playlists has potentially set a contaminated anchor for the lifetime of that release. The stream count looks positive. The algorithmic health is degrading. The divergence is not visible in the stream data. It is visible only in the save rate, the repeat listen rate, and eventually in the collapse of Discover Weekly and Release Radar placement.

Reversing contamination requires an equivalent volume of genre-coherent streams from the right listeners to outweigh the bad data. For an independent artist without label promotional infrastructure, generating that volume on demand after the damage has been done is difficult. The window to establish the right anchor, the first two to four weeks after release, is gone.

## What the Musinique Database Shows

When I look at the bottom quartile of the Musinique database by Focus Score, these are playlists spanning rock, hip-hop, electronic, and folk simultaneously, all labeled “good vibes” or “the mix.” Their follower counts are often high. They have been around long enough to accumulate followers from multiple genre communities. They accept pitches broadly. They grow. Every artist who lands on them contributes to their own genre contamination.

The high-focus playlists in our database are the inverse. Playlists where a curator has maintained a consistent genre identity over time, where artist repetition is high, where track count per genre is dense. Fewer followers on average. Fewer absolute streams. But every stream comes from a listener who chose the playlist for that specific genre. Save rates are higher. Skip rates are lower. The collaborative filtering contribution is clean.

In our database, Filtr US, the Sony-owned operator with 9.19 million combined followers and an average Focus Score of 33.8, sits at the top of the high-reach, low-focus end. A Filtr placement reaches millions of listeners who have no consistent genre relationship with each other. For an artist whose sound is genre-specific, those streams contaminate before they compound. The indie-accessible range in our database, between 1,000 and 50,000 followers, accounts for 30 percent of total reach and shows significantly higher average Focus Scores. Smaller audience. Right audience.

Lance Allen built his career in exactly that range. He pitched to curators who ran acoustic guitar playlists with audiences specifically there for acoustic guitar. The algorithm learned from those streams precisely who his music was for and began sending it to more of the same people. The momentum compounded because the foundation was coherent. He did not try to reach the biggest playlists. He tried to reach the right playlists. For years, that strategy worked exactly as the mechanism predicts it should.

## The Counterargument About Reach

The standard response to this analysis is that smaller, high-focus playlists do not generate enough initial momentum to attract algorithmic attention, and that raw stream volume in the first weeks after release is the primary driver of editorial consideration. This is worth addressing directly because it is partially true.

Spotify’s editorial team does consider performance metrics when selecting tracks for larger playlists. A track that has generated no initial traction is less likely to receive editorial placement. Stream volume matters.

But the engagement metrics that accompany that stream volume matter more. A track with 5,000 streams and a 20 percent save rate demonstrates to Spotify that listeners who heard the track found it worth keeping. A track with 50,000 streams and a 1 percent save rate demonstrates that 49,500 of the listeners who encountered it did not. The first track is a stronger editorial candidate than the second, because it shows genuine resonance rather than passive exposure.

The campaign that chases volume from genre-incoherent playlists is not building toward editorial placement. It is building a documented record of low engagement that is visible to both the algorithm and the editorial team simultaneously. The Focus Score identifies which playlists generate the engagement quality that editorial consideration actually requires.

Genre entropy does not just fail to help a track find its listeners. It actively teaches Spotify to send it to the wrong ones, and it does so during the period when the algorithm is most attentive and most influential. The Focus Score is the measurement that tells you, before you pitch, whether a playlist will build the right foundation or contaminate it.

Pitch where the audience matches. The algorithm does the rest.

Thanks for reading Musinique! Subscribe for free to receive new posts and support my work.
