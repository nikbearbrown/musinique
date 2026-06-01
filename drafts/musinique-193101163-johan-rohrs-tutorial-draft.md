---
title: "Johan Rohrs Tutorial"
subtitle: ""
publication: "musinique"
book: "Musinique"
draft_status: "rewrite"
rewrite_voice: "Baldwin/Subby Substack essay"
source_article: "musinique-193101163-johan-rohrs-tutorial.md"
source_file: "musinique-193101163-johan-rohrs-tutorial.md"
post_id: "193101163.johan-rohrs-tutorial"
post_date: ""
cover_image: ""
excerpt: "There is a Swedish composer named Johan Röhr whom you have almost certainly never heard of and have almost certainly heard. By 2022, he had generated fifteen billion streams on Spotify under 656 different aliases, composing music under names like Erik Lidbom and Johan Segeholm, earning an estimated six million dollars from a platform that claims, in its..."
---
# Johan Rohrs Tutorial

_Draft rewrite for Musinique Substack._

There is a Swedish composer named Johan Röhr whom you have almost certainly never heard of and have almost certainly heard. By 2022, he had generated fifteen billion streams on Spotify under 656 different aliases, composing music under names like Erik Lidbom and Johan Segeholm, earning an estimated six million dollars from a platform that claims, in its promotional materials and its congressional testimony and its quarterly earnings calls, to exist in order to help artists earn a living from their music.

Röhr’s achievement was not musical. He was competent — the tracks are inoffensive, instrumental, and interchangeable, the sonic equivalent of a waiting room. His achievement was architectural. He identified something the platform had built, understood it more precisely than the people who built it, and used it exactly as designed.

Spotify did not charge him with fraud. They had funded the program through which he operated.

This is the essay that begins there, at that fact, and refuses to leave it until we understand what it means.

## The Perfect Fit Content Initiative

In the years before Röhr became a story, Spotify had been constructing a system called Perfect Fit Content — PFC, in the company’s internal shorthand. The premise was elegant: high-traffic ambient and instrumental playlists (Deep Focus, Sleep, Lo-Fi Beats) needed consistent content, and the market for that content was thin. Professional music was too expensive to license at the volume the playlists required. So Spotify created a program to source music at scale, contracting directly with composers and production companies to supply tracks that would fill the playlists.

The rates were dramatically lower than standard licensing. The composers were credited pseudonymously or not at all. The music was engineered not for ears but for algorithmic metrics — specifically, skip rate and session continuation, the two signals that determine whether a track stays in rotation.

Röhr didn’t break into this system. He applied. He optimized it. He created 2,700 songs across 656 aliases because the platform’s logic rewarded volume and penalized concentration — a composer with one name and 2,700 tracks is traceable, visible, potentially auditable. A composer with 656 names and four tracks apiece is a supply chain.

The Guardian ran the story in March 2024. Spotify, confronted with the numbers, described the program as discontinued. They did not describe it as wrong.

Here is what they did not say: what Röhr demonstrated was not that the system could be abused. What he demonstrated was that the system was the abuse. The ghost artist model — the invented name, the functional music, the suppressed authorship — was not a corruption of Spotify’s playlist ecosystem. It was the playlist ecosystem, rationalized and made explicit.

Röhr handed the proof of concept to anyone willing to read a newspaper.

## What a Platform Owes

To understand why Spotify expressed concern about streaming fraud after the Röhr story and took no structural action to prevent it, you have to understand what Spotify is, as a financial instrument, before you understand what it is as a music service.

Spotify operates under the pro-rata royalty model. The total payout pool is a fixed percentage of revenue. That pool is then divided by total streams, producing a per-stream rate that currently averages between $0.003 and $0.005. The critical detail — the one that explains every subsequent failure of platform policy — is that fraudulent streams do not increase the pool. They dilute it.

When Röhr’s aliases accumulated fifteen billion streams, he was not extracting money that Spotify had set aside for legitimate artists. He was extracting a portion of the same fixed pool that Ed Sheeran and a bebop pianist in New Orleans and a twenty-three-year-old folk singer in Nashville were drawing from. Every stream the aliases captured was a fraction of a cent removed from the royalty that would otherwise have flowed to someone who had made something a human being chose to listen to.

This is the mechanism that Spotify has never been made to explain clearly in public: the platform’s financial obligation to rights holders is fixed at the top. The fraud does not cost Spotify money. The fraud costs other artists money.

Which means, if we follow the logic honestly, that Spotify has no direct financial incentive to stop it.

What the platform does have a financial incentive to maximize is engagement — the total number of minutes users spend inside the application, which drives subscription renewals and advertising revenue. A user who opens Spotify to listen to Deep Focus and spends forty minutes doing so has generated exactly the same engagement value whether the tracks they heard were composed by Aphex Twin or generated by an algorithm in 2017 and attributed to a Swedish alias.

The platform’s interest is captured attention. It is indifferent to whose music captures it.

This is not a conspiracy. It is an incentive structure, and incentive structures, if you follow them far enough, always tell the truth about who a system is actually built for.

## The Upgrade

Someone read the Röhr story and understood it as a tutorial with one design flaw.

The flaw: Röhr had to build an audience. Under the PFC model, the playlist was the distribution mechanism — tracks got exposure because they were placed in editorial playlists with existing listener bases. But PFC was discontinued, which meant the ghost artist playbook now required a ghost artist to accumulate real followers before the economics worked. That was slow. It was expensive. It was the one friction in an otherwise frictionless system.

The upgrade was elegant in the way that solutions to well-defined problems tend to be elegant: instead of inventing a new audience, inherit an existing one.

Spotify’s platform provides every user who follows an artist with a personalized playlist called Release Radar, delivered every Friday, automatically populated with new releases from followed artists. The mechanism requires no editorial approval, no human review, no curatorial judgment. It requires only that a track be delivered to a distributor with the correct Artist URI in the metadata field.

The Artist URI for Benny Green is public. The Artist URI for Nat Adderley is public. The verification layer for claiming that your new track belongs to Benny Green’s catalog — the thing that stands between a submitted URI and a push notification delivered to tens of thousands of people who have followed Benny Green since 1990 — is a Terms of Service checkbox.

That is the entirety of the gate.

In 2025 and 2026, the research documents it clearly: a fraudulent track injected into an established artist’s profile will reach the Release Radar of every follower within the same Friday delivery cycle. For a mid-tier jazz artist with fifteen thousand followers, this means fifteen thousand push notifications sent under the artist’s name, fifteen thousand listeners who trust that what they’re about to hear is from someone they chose to follow.

The listener waits. This is what the research calls the Confusion Window — the 35 to 45 seconds a follower will hold before skipping a track that sounds wrong, because the trust they have in the artist delays the recognition that something is wrong. That 35 to 45 seconds crosses the 30-second threshold at which Spotify counts a stream as payable.

The confusion is the monetization mechanism.

## What the Platform Calls Surprise

In March 2026, the critic Ted Gioia documented a wave of fraudulent releases attributed to Abbey Lincoln — an artist who died in 2010. In the same period, fans of Emily Portman discovered an AI-generated album called *Orca* attributed to her catalog and delivering to her followers for eight weeks before removal. Benny Green’s profile was injected with a fake EP attributed as a collaboration with the late Freddy Cole.

Spotify, asked about these cases, indicated that it takes streaming fraud seriously and is actively working to improve its detection systems.

This is a sentence that contains almost no information.

The detection system that would prevent Release Radar weaponization is not technically complex. A fingerprint comparison between submitted audio and the catalog of the artist whose URI is being claimed would catch stylistic mismatches. A 48-hour hold on Release Radar distribution pending metadata verification would interrupt the collection window. A mandatory two-factor authentication requirement for URI mapping would eliminate the zero-verification submission pipeline.

None of these changes have been implemented. The removal window for documented fraudulent attributions remains three to eight weeks. The royalty payout cycle runs on a two-month delay. The temporal alignment is precise: by the time the track is removed, the first wave of royalties from the first month of streams is already processing.

The research documents an estimated 200 to 500 percent return on investment per fraudulent track targeting a mid-tier catalog, before detection and removal.

A platform that was surprised by this would have fixed it. A platform that has not fixed it has revealed its priorities through that decision.

## What Röhr Made Possible

I want to be careful here, because accuracy requires it: Johan Röhr did not commit the fraud currently being documented against Abbey Lincoln’s estate and Benny Green’s catalog. He operated within a program his platform created and funded. What he did was demonstrate, at scale and in public, that the platform’s architecture had no meaningful protection against the conversion of audience trust into extracted royalties.

He wrote the proof of concept. Others wrote the application.

This is the distinction the platform would prefer we not make, because the alternative framing — bad actors exploiting an otherwise sound system — allows Spotify to present itself as a victim of fraud rather than the entity whose design decisions made the fraud structurally inevitable.

The distributor side compounds this. DistroKid, TuneCore, and CD Baby function as high-volume, self-service upload portals. Their business model rewards volume: more uploads mean more annual subscribers, and in some cases more commission on social platform revenue. The financial incentive at the distributor level runs in the same direction as the incentive at the platform level. Neither party profits from the friction that verification would introduce. The artist who wakes up to find a fraudulent release in their catalog, delivering to their followers under their name, is the only party in this system who has an interest in the gate being closed.

They are also the only party with no power over whether it is.

## What Changes

The ELVIS Act, passed in Tennessee in 2024, created a civil right of action against AI voice cloning without authorization. The NO FAKES Act, reintroduced federally in April 2025, proposes a 48-hour takedown mechanism and explores strict liability for platforms designed to facilitate unauthorized replicas. These are meaningful moves. They are also downstream of the actual problem.

The actual problem is that verification was never required in the first place — not because no one thought to require it, but because the parties positioned to require it had financial reasons not to.

Mandatory KYC protocols at the distributor level would slow ingestion. Real-time estate authorization rights for deceased artists would introduce human review into an automated pipeline. Fingerprint-to-catalog verification would require computational overhead Spotify has not been required to absorb.

Each of these changes costs something to the platform. None of them cost anything to the artist whose audience is currently being used as an inheritance the artist never consented to give.

The music industry did not fail to notice that Johan Röhr was generating fifteen billion streams under 656 names. It noticed, reported it, and waited. What it was waiting for was a regulatory requirement that would make the cost of inaction higher than the cost of change.

That requirement has not yet arrived. Until it does, the Release Radar algorithm will function as the most efficient fraud delivery system in the digital economy — not because it was designed to, but because it was designed well, and someone paid attention.

Röhr paid attention first. He just wasn’t the last.

---

**Tags:** Johan Röhr Spotify ghost artist fraud, Release Radar weaponization streaming, pro-rata royalty model incentive misalignment, Perfect Fit Content Spotify PFC, attribution hijacking digital music 2026
