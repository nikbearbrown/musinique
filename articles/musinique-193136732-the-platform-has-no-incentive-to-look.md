---
title: "The Platform Has No Incentive to Look"
subtitle: "A researcher built a fraud detector from public data. It works. Spotify hasn't."
publication: "musinique"
book: "Musinique"
substack_name: "Musinique"
format: "substack article"
post_id: "193136732.the-platform-has-no-incentive-to"
post_date: "2026-04-04T03:58:16.793Z"
is_published: "true"
source_zip: "Y0r_0oGOSoWMD3iEcEhVnA.zip"
source_html: "posts/193136732.the-platform-has-no-incentive-to.html"
source_file: "musinique-193136732-the-platform-has-no-incentive-to-look.md"
cover_image: "https://substack-post-media.s3.amazonaws.com/public/images/67ab3e28-7ecc-4ddc-bfdf-7bec168c08f6_1456x816.png"
---
![](https://substack-post-media.s3.amazonaws.com/public/images/67ab3e28-7ecc-4ddc-bfdf-7bec168c08f6_1456x816.png)

Here is a number that should make you angry if you have ever uploaded a song to Spotify and watched the stream count accumulate while the royalty check didn’t: 0.97.

That is the AUC — the classification accuracy, on a scale where 1.0 is perfect and 0.5 is a coin flip — of a fraud detection model built entirely from Spotify’s public API. No internal data. No server logs. No account-level information. No platform cooperation of any kind. Seven signals that anyone with a developer key and patience can observe, combined into a Bayesian probability score that correctly identifies recommendation graph contamination 97 percent of the time.

The researcher who built it is Nik Bear Brown, an associate teaching professor at Northeastern who has spent the past several months publishing what is effectively an independent audit of Spotify’s recommendation infrastructure — the system that decides which music gets heard and which music gets buried. The methodology is published openly. The labeled corpus is available. The code is not a secret.

Spotify’s internal team, with access to everything — every stream, every account, every payment record, every geographic routing pattern — has produced no equivalent finding. Has disclosed no equivalent number. Has published no audit of its own engagement metrics in any SEC filing or investor communication.

You should sit with that for a moment.

A professor with a public API built a 97 percent accurate fraud detector. The company with the data to build a 99.9 percent accurate fraud detector has chosen not to build it, or has built it and chosen not to tell you.

Those are the only two possibilities. Neither of them is flattering.

## What the Graph Actually Is

Before the anger, the mechanism — because the mechanism is the argument, and the argument is more specific than “Spotify has a fraud problem.”

The fraud is not in the music. The fraud is in the graph.

Earlier generations of streaming manipulation were crude: bot farms playing tracks on repeat, crossing the 30-second threshold that triggers a payable stream, extracting pennies from a royalty pool that your pennies were supposed to come from. That fraud still exists. It is not the interesting fraud.

The interesting fraud operates upstream, in the recommendation system itself. Spotify’s algorithm — the engine behind Discover Weekly, Release Radar, Radio, Autoplay — does not select music based on quality. It selects music based on behavioral signals: saves, completions, non-skips, playlist additions, the ratio of followers to monthly listeners. These signals are supposed to represent human preference. They are supposed to tell the algorithm what real people actually like.

They can be manufactured.

By injecting calibrated save rates and completion rates into a track’s first 28 days — the contamination window, the period when early data disproportionately shapes a track’s long-term algorithmic trajectory — a bad actor can teach Spotify’s recommendation system that a track has already been validated by real human listeners who do not exist. The algorithm then routes the track to real human listeners, who generate real engagement, which makes the manufactured signals self-reinforcing.

You were not competing with that track on a level surface. You were competing with a track that had already paid to appear as though it had won.

## The Ghost Artist Economy

Brown’s research has documented this at industrial scale. Forty confirmed ghost artists — fabricated identities, invented biographies, AI-generated music released under names that sound vaguely like real people — with combined monthly listeners exceeding ten million and combined followers fewer than ten thousand. One artist, Spring Euphemia, produced fifty-one million plays and 529 followers. The follower conversion rate: 0.00215.

For context: the organic baseline — the rate at which real listeners who genuinely enjoy an artist’s music choose to follow them — runs between 5 and 15 percent. Spring Euphemia’s rate is two to three orders of magnitude below that floor. Not a little below. A hundredth of the minimum. The gap between the stream count and the follow count is not a personality quirk. It is the fraud made numerically visible.

Most of these artists trace back to five Swedish production companies. Their catalogs are concentrated in the genres Spotify’s own internal programming has historically targeted for what the platform calls Perfect Fit Content: ambient, sleep, lo-fi, focus, peaceful piano. The genre categories with the lowest mean Human Engagement Probability scores in Brown’s framework are precisely the categories the platform’s own economic model identified as needing cheap, high-volume, royalty-minimizing content.

The platform did not cause this fraud. But the platform created the economic conditions that made this fraud the rational response. And then the platform failed to detect it. Or detected it and said nothing.

## The Seven Things Spotify Could Measure

The Human Engagement Probability framework Brown built works because genuine human engagement with music leaves observable traces — behavioral signatures that automated systems optimizing for royalty extraction cannot efficiently replicate.

A human listener who genuinely loves a track follows the artist. Bots don’t. A track that breaks organically shows up on TikTok and Twitter before it moves on Spotify. A bot-injected track appears in the Spotify data first, with no external signal. A human curator adding a track to a playlist applies taste — the track ends up in a coherent sonic neighborhood. A paid playlist promotion service applies economics — the track ends up next to Japanese acid jazz and sleep meditation and workout electronica simultaneously, because the placement is purchased not curated.

Real playlists are removed from one at a time, by individual humans making individual decisions on no particular schedule. Paid placements are removed simultaneously, across all playlists in the operator network, because the trigger is a single database event — a payment failure, a subscription cancellation, a DELETE statement running on the backend of a playlist promotion service. Seven playlists dropping a track within the same hour, across genres sharing no aesthetic relationship, is not a coincidence. It is an invoice.

These signals are all publicly observable. They are all in the API. They achieve 0.97 AUC together. They require no cooperation from the platform.

If an outside researcher can see this from the public data, the internal team can see it from the full data with a precision that would make the 0.97 look like a rough estimate.

## Why Spotify Hasn’t Looked

Here is the calculation the paper makes, stated plainly.

Spotify’s market capitalization is approximately $100 billion. Its reported Monthly Active Users — 751 million, the number that underpins the advertising revenue and the growth narrative and the stock price — include an unquantified fraction that is not human. Beatdapp, the music industry’s leading independent fraud detection firm, has documented fraud rates between 20 and 74 percent among specific distributor pipelines. Apple Music, which charges $10.99 a month and therefore costs a bot farm $10.99 per account per month, claims under 1 percent manipulation. Spotify’s free tier costs a bot farm $0.

The structural asymmetry is not a coincidence. It is the business model.

A fraud research operation adequate to quantify Spotify’s actual human engagement rate would cost approximately $5 to $10 million annually. Against $17 billion in annual revenue and a $100 billion market cap, that is a rounding error. The reason it doesn’t exist is not that Spotify can’t afford it.

The reason it doesn’t exist is that it might find something. And if it found something material — if the audited human fraction of 751 million MAUs required downward revision, if the advertising impression inventory turned out to include a significant proportion of bot-generated plays that brands were paying for as if they were human attention — that finding would require disclosure. Disclosure would compress the growth narrative. A compressed growth narrative would pressure the market cap.

The research operation would cost $10 million to run. It could cost $20 billion in market capitalization if the findings were material.

Meta, at approximately the same $100 billion market cap Spotify holds today, began disclosing false account estimates quarterly in 2012. The methodology is published. The number is auditable. Spotify’s equivalent: boilerplate risk language in SEC filings. Acknowledgment that fraud exists as a category of risk. No number. No methodology. No finding.

The absence of the finding is the finding.

## What You Can Do With This

Brown’s paper ends the same way both of his previous papers end: the methodology is not a secret. The framework is published. The labeled corpus is available. The code can be run by anyone with a developer key and the inclination.

This matters for indie musicians in a specific and practical way. An independent artist penalized by Spotify’s distribution system for the crime of being added to bot-heavy playlists without their knowledge — a thing that happens, that has happened to documented artists whose tracks were pulled by automated systems that couldn’t distinguish their legitimate organic spike from manipulation — can now generate a timestamped HEP evidence report. Structural anomalies in their playlist neighborhood. Coordinated removal events affecting their track. Overall contamination probability with explicit uncertainty bounds. All from public data. No platform cooperation required.

That evidence exists. It can be generated. It provides a basis for dispute that the current system makes nearly impossible, because the current system asks artists to prove something went wrong in a data environment controlled entirely by the party that may have done it wrong.

The broader implication is simpler and harder at the same time. Spotify will not audit its own engagement metrics as long as the cost of not auditing is lower than the cost of auditing. The research community publishing independent methodology — openly, requiring no cooperation — changes the cost structure. It makes the absence of internal audit indefensible rather than merely convenient.

The ghost is still playing on someone’s sleep playlist tonight. The mechanism is now documented. The 0.97 is public. The question is what the regulator, the journalist, and the independent artist do with it — and whether the platform, having now had the methodology demonstrated to it from outside, decides that looking is finally cheaper than not looking.

It should. But it’s a $100 billion company that has never had to. That combination is not usually resolved by the company choosing to do the right thing.

It is resolved by the cost of not doing the right thing becoming too high.

---

**Tags:** Spotify fraud detection HEP framework indie artist royalties, ghost artist streaming manipulation bot playlist, recommendation graph contamination algorithmic accountability, streaming fraud $100 billion market cap disclosure, independent music platform audit public API methodology
