---
title: "The Absence Of Measurement Is The"
subtitle: ""
publication: "musinique"
book: "Musinique"
draft_status: "rewrite"
rewrite_voice: "Baldwin/Subby Substack essay"
source_article: "musinique-193125367-the-absence-of-measurement-is-the.md"
source_file: "musinique-193125367-the-absence-of-measurement-is-the.md"
post_id: "193125367.the-absence-of-measurement-is-the"
post_date: ""
cover_image: ""
excerpt: "There is a researcher — working outside Spotify, with no access to server logs, no account-level data, no payment records, no internal documentation of any kind — who built a fraud detection model using seven public signals and achieved an AUC of 0.97. For readers outside machine learning: 1.0 is perfect classification. Random guessing produces 0.5. The..."
---
# The Absence Of Measurement Is The

_Draft rewrite for Musinique Substack._

There is a researcher — working outside Spotify, with no access to server logs, no account-level data, no payment records, no internal documentation of any kind — who built a fraud detection model using seven public signals and achieved an AUC of 0.97.

For readers outside machine learning: 1.0 is perfect classification. Random guessing produces 0.5. The researcher’s model, built from what anyone with an API key and patience can observe, correctly identified fraudulent streaming activity 97 percent of the time.

Spotify’s internal team has access to everything. Every account. Every listening session. Every payment flow. Every geographic routing pattern. Every follower acquisition event. Every playlist placement and the timing of what follows it. They have the server logs that show whether a stream came from a device that had been stationary for six hours. They have the payment records that reveal whether the royalty recipient is a legal entity with a verifiable address or a shell structure routing money through a jurisdiction with minimal financial disclosure requirements. They have the anomaly that the RBX class-action lawsuit documented in public filings: accounts listening to a single artist for 23 hours a day, streams geomapped to postal codes with zero residential addresses, 250,000 plays of one song routed through Turkey in four days and recorded as UK traffic to capture higher royalty rates.

These anomalies are not subtle. A human analyst looking at them for the first time would recognize them immediately. A machine learning engineer with access to the full data corpus would build a model orders of magnitude more powerful than what an outside researcher achieved with seven public signals.

Spotify has produced no formal finding.

This essay is about what that silence means — not as evidence of corruption, which is the easier accusation and the less precise one, but as evidence of something more durable and more important to understand: rational institutional behavior in the presence of inconvenient truth.

## The Shape of the Silence

Before naming what the silence means, it is worth being precise about what it is.

Spotify’s public disclosures on streaming fraud consist of what the financial and legal literature calls boilerplate risk language: acknowledgments, in the standard format required by securities regulations, that fraud exists as a category of risk, that it may affect the company’s metrics, and that the company takes steps to address it. The steps are described in general terms. The methodology is not published. The findings are not disclosed. The percentage of monthly active users that represents genuine human engagement, as distinct from automated simulation of genuine human engagement, has never appeared in a Spotify earnings report or investor presentation.

Meta, at approximately the same market capitalization — $100 billion — as Spotify holds today, began disclosing false account estimates in 2012, the year of its IPO. The disclosure was not voluntary in the sense of being generous; it was the product of SEC pressure and institutional investor demands for accountability. But it happened. Every quarter since, Meta has published an estimate: approximately 5 percent of monthly active users are false or duplicate accounts. The methodology for producing that estimate is described. The number is auditable. It exists.

Twitter, in its pre-acquisition public filings, disclosed that fewer than 5 percent of monetizable daily active users were false or spam accounts. Google publishes view validation methodology for YouTube. These are not complete or necessarily accurate disclosures — the incentive to underestimate is obvious, and the methodology choices that produce the estimate are consequential. But the disclosures exist. They represent an acknowledgment that the question has been asked and an answer, however imperfect, produced.

Spotify’s equivalent: nothing.

The absence is precise. It is not the absence of capability — the researcher outside the platform, working from public signals, demonstrated that the measurement is tractable. It is not the absence of resources — $5 to $10 million annually would staff a fraud research operation at the scale the problem requires, against $17 billion in annual revenue. It is not the absence of evidence — the anomalies visible from outside, with seven public signals, are the fraction of the iceberg above the waterline. The internal team is looking at the whole iceberg.

The absence is a choice. At $100 billion, it is an informed one.

## What the ML Engineer Knows

I want to be careful here, because the argument I am making is not about individual people and their individual choices. It is about the conditions under which individuals make choices that are, in aggregate, institutional.

A Spotify machine learning engineer working on recommendation systems knows several things that are directly relevant to this question. They know that the behavioral signals feeding collaborative filtering show anomalies inconsistent with human listening patterns — that the ratios of replays to unique listeners, the timing of saves, the geographic distribution of streams for certain categories of content do not match what human behavior produces. They know that the follower conversion rates for content on official editorial playlists vary by orders of magnitude across ostensibly similar artists — that some tracks produce the fan deepening behavior that genuine discovery generates, and others produce a statistical profile that has no plausible human explanation. They know that the popularity score trajectories for certain content are suspiciously smooth during the critical early windows when organic discovery would produce irregularity.

They know these things because they work with the data daily. The signals are not hidden. They are visible to anyone looking at the system from the inside with competence and attention.

The question is not whether the signals are visible. The question is what happens to a person who looks at them carefully, names what they indicate, and considers publishing the findings internally.

What happens is that they have made a finding that, if accurate and material, requires disclosure. Material findings — findings that would affect a reasonable investor’s decision about the company’s securities — are subject to reporting obligations. A finding that Spotify’s monthly active user count includes a percentage of automated accounts that would require downward revision is material. A finding that the advertising impression inventory is partially composed of bot-generated plays that brands are paying for as if they were human attention is material. A finding that the growth narrative that sustains a $100 billion market capitalization is partly a story about machines listening to machines — that is material.

The researcher who makes that finding and publishes it internally has done their job. They have also, potentially, initiated a process that compresses the market cap by tens of billions of dollars, triggers regulatory scrutiny, and generates internal consequences for the metrics teams whose numbers the finding undermines.

The organizational culture of a company under Wall Street growth pressure does not need to explicitly threaten people who ask inconvenient questions. It needs only to make clear, through the ordinary mechanisms of performance reviews and promotion decisions and project prioritization, which questions produce valued outcomes and which questions produce friction. Engineers and researchers working within that culture make rational choices. They ask the questions that are valued. They leave the others, carefully, unasked.

This is not corruption. It requires no conspiracy. It requires only the normal operation of institutional incentives — the same incentives that produced the Ford Pinto safety analysis, in which engineers calculated the cost of a fuel tank redesign against the projected cost of settling wrongful death litigation and chose the litigation. The same incentives that produced the tobacco industry’s internal research on nicotine addiction, conducted with rigor and precision and filed without publication. The same incentives that produced the banking industry’s risk models before 2008, which told the institutions what was coming with considerable accuracy and were not acted upon because acting on them would have required acknowledging, internally and then externally, that the products being sold were structured to fail.

In each case, the technical capability to measure the problem existed and was not deployed at full capacity. In each case, the findings that the measurement would have produced were economically inconvenient. In each case, the institutional explanation was not “we didn’t know” but “we chose the level of knowing that our incentive structure rewarded.”

Spotify is not Ford. It is not Altria. It is not Lehman Brothers. Those comparisons carry moral weight that the streaming fraud story has not yet earned and may not earn. But the structure is the same structure. The mechanism is the same mechanism. The silence is the same kind of silence.

## The $10 Million Question

The document that frames this argument makes a calculation that deserves to be read slowly.

A fraud research operation adequate to the problem would cost approximately $5 to $10 million annually. It would require 10 to 15 senior machine learning researchers with expertise in anomaly detection and behavioral modeling, a dedicated data infrastructure team for longitudinal signal tracking, independent audit capacity with no reporting line to the metrics teams whose numbers they are auditing, and public disclosure of methodology and results — the same standard Meta has maintained since its IPO.

Against $17 billion in annual revenue and a $100 billion market cap, $10 million is not a budget problem. It is a rounding error in the company’s quarterly earnings.

If the fraud research group found what the external evidence suggests it would find — and the external evidence, remember, produces 0.97 AUC from public signals alone — the findings would potentially require disclosure. The disclosure would require downward revision of MAU counts. The downward revision would compress the growth narrative. The compressed growth narrative would pressure the $100 billion market cap.

The research group would cost $10 million to run. It could cost $20 billion in market capitalization if its findings were material and required disclosure.

This is not a difficult calculation. A company with Spotify’s financial sophistication is not failing to make it. The calculation has been made. The result is the absence of the research group. The absence of the research group is the finding.

## What Measurement Would Cost

The argument I am making is not that Spotify should be prosecuted. It is not that the people running the company are bad people — they are people responding rationally to the incentive structure of a public company under growth pressure, which is the condition that the market creates for every public company under growth pressure.

The argument is that the absence of measurement, at this scale, with these resources, in the presence of this much external evidence, is itself a form of information. It tells us something specific about what the company knows and has chosen not to formalize into a finding that would require action.

And the argument is that the external researcher who achieved 0.97 AUC from seven public signals has done something that the internal team, with access to everything, has not done — not because the internal team lacks the capability, but because the internal team operates inside an institution with a $100 billion reason to leave certain questions carefully unasked.

The contribution of the external measurement is not primarily its findings. It is its demonstration that the measurement is tractable. That the anomalies are not subtle. That no technical limitation prevents a well-resourced internal team from producing, with high confidence, exactly the kind of formal finding that would require disclosure.

The absence of that finding is not a technical limitation. It is a choice.

At $100 billion, it is an informed one.

The last line of the RBX class-action complaint, in its summary of the evidence for systematic enforcement disparity between major-label and independent catalogs, reads: “Spotify knows or should know.” That phrase is doing legal work — it establishes the knowledge standard for liability. But it is also doing something more than legal work. It is describing the precise condition of a company that has access to the information, has the capability to formalize it, and has made a rational institutional choice not to.

Knows or should know.

The silence is not the absence of an answer. It is the answer.

---

**Tags:** Spotify fraud detection AUC methodology institutional incentives, streaming fraud MAU disclosure Wall Street growth pressure, RBX class action Spotify material findings disclosure, Ford Pinto tobacco internal research institutional complicity, $100 billion market cap streaming accountability
