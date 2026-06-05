# BOOKMAP: Automate This: How Algorithms Came to Rule Our World
**Christopher Steiner | Gildan Media | 2012**

---

## PART 1: SECTION-BY-SECTION LOGICAL MAPPING

---

### Introduction

**Core Claim:** Algorithms, once confined to academic and financial backrooms, have become the invisible architecture of contemporary life. The Flash Crash of May 6, 2010 and the Amazon pricing spiral of April 2011 are not outliers but harbingers: systems built to optimize narrowly defined objectives will, absent human oversight, produce outcomes ranging from absurd to catastrophic.

**Supporting Evidence:**
- The Amazon book-pricing incident: two seller algorithms entered a positive feedback loop, escalating the price of *The Making of a Fly* from $35 to $23.7 million before human intervention.
- The 2010 Flash Crash: the Dow fell 998.5 points in under five minutes, erasing nearly $1 trillion in market capitalization, then partially recovered—driven entirely by algorithmic trading with no human in the loop.

**Logical Method:** Two concrete case studies of algorithmic failure establish urgency. Steiner then defines algorithm broadly (a list of instructions producing an output from inputs), positions the book as a survey of algorithmic invasion across sectors, and introduces "bot" for linked multi-algorithm systems.

**Logical Gaps:**
- The introduction conflates two distinct failure modes. The Amazon case is a design flaw—no price ceiling, no termination condition. The Flash Crash remains causally contested. Treating both as equivalent examples of "unsupervised algorithms" elides meaningful structural differences.
- "Algorithms can and will do strange things when left unsupervised" is presented as axiomatic rather than derived.

**Methodological Soundness:** The introduction functions as advocacy framing. Both cases are real and documented. The causal claim that algorithms *caused* the Flash Crash remains disputed as of publication. Steiner appropriately notes the absence of causal consensus.

---

### Chapter 1: Wall Street—The First Domino

**Core Claim:** Thomas Peterffy's invention of fully automated algorithmic trading (late 1970s–1980s) constitutes the founding disruption: a programmer with no trading background demonstrated that an algorithm replicating expert judgment could systematically outperform human market participants.

**Supporting Evidence:**
- Peterffy hacked the NASDAQ terminal to create a fully automated trading system by 1987. After regulatory pressure, he engineered a camera-plus-mechanical-typing-arm workaround in six days—obeying the letter of the law while violating its spirit.
- Made $25M in 1987, $50M in 1988.
- Operated coast-to-coast via the "Correlator" master algorithm by the early 1990s.
- Interactive Brokers IPO'd in 2007 at a $12B valuation.
- 60% of all U.S. stock market trades are now executed by computers with minimal human oversight.

**Logical Method:** Biography traces the three phases of algorithmic takeover: Phase 1 (algorithms issue orders to humans), Phase 2 (algorithms issue orders executed by machines), Phase 3 (algorithms modify themselves independently). Peterffy's career is the through-line.

**Logical Gaps:**
- Attributing the revolution primarily to Peterffy involves selection bias. O'Connor and Associates, Joe Richie, and Blair Hull were developing parallel approaches with similar logic and timing. "Sparked the revolution" is assertion, not derivation.
- The chapter conflates two distinct achievements: automated *execution* and algorithmic *strategy generation*. These are different problems with different intellectual genealogies.

**Methodological Soundness:** The Peterffy narrative is journalistically sourced and internally consistent. The 60% trading figure is supported by multiple industry sources, but no methodology or date for that estimate is specified.

---

### Chapter 2: A Brief History of Man and His Algorithms

**Core Claim:** The mathematical foundations enabling modern algorithmic systems—binary logic (Leibniz), graph theory (Euler), probability (Pascal/Bernoulli), regression and normal distributions (Gauss), Boolean algebra (Boole/Shannon)—were developed over 300 years, and the algorithmic revolution is their inevitable computational instantiation.

**Supporting Evidence:** Documented intellectual lineage: al-Khwarizmi (9th century), Fibonacci (1202), Leibniz (binary system, 1703), Gauss (least squares, normal distribution, early 19th century), Euler (graph theory, 1735), Boole (Boolean algebra, 1854), Shannon (synthesis of binary system with Boolean logic into electronic circuits, late 1930s).

**Logical Method:** Historical lineage argument: each breakthrough is a necessary precondition for the next, culminating in Shannon's synthesis. The Gaussian copula misapplication in 2008 is a cautionary case of a mathematically valid tool misapplied outside its assumptions.

**Logical Gaps:**
- The narrative of inevitable progression understates contingency. Shannon's 1937 MIT thesis is presented as the "birth" of computer circuitry, but concurrent developments by Zuse, Turing, and Atanasoff-Berry are omitted, creating a false impression of linear descent.
- The Gaussian copula discussion accurately identifies misuse but attributes too much causal weight to the formula, when the greater failure was institutional—credit rating agencies applying it without understanding its assumptions.

**Methodological Soundness:** Historical claims are accurate and well-sourced. The interpretive framework—that mathematical theory precedes and enables technological application—is sound but overstated as determinism.

---

### Chapter 3: The Bot Top 40—Music

**Core Claim:** Algorithmic analysis of music's underlying mathematical structure can predict commercial success and eventually generate original compositions indistinguishable from human masters—challenging the assumption that creativity is a uniquely human domain.

**Supporting Evidence:**
- Polyphonic HMI's algorithm scored Ben Novak's "Turn Your Car Around" at 7.57 (above the 7.0 hit threshold); it reached number one in the UK.
- The algorithm identified Norah Jones's *Come Away With Me* as containing 9 likely hits before release; it sold 20 million copies and won 8 Grammys. Also identified Maroon 5 before debut.
- David Cope's Emmy algorithm generated 5,000 Bach chorales in one session. At the University of Oregon, audience members identified Emmy's piece as genuine Bach and Steve Larson's human composition as the computer's work.

**Logical Method:** Two complementary demonstrations: predictive algorithms (pattern recognition) and generative algorithms (rule-learning plus controlled rule-breaking). Cope's analogy argument: if Bach built on prior patterns, and Emmy builds on prior patterns, the distinction is one of degree, not kind.

**Logical Gaps:**
- Survivorship bias in the predictive algorithm section: Polyphonic's hits are documented, its misses are not systematically reported. The 20% industry hit rate is mentioned as a baseline, but Polyphonic's overall accuracy rate is never established.
- "Indistinguishable from Bach in a controlled listening experiment" ≠ "equivalent to Bach as a composer." These measure different things. The Oregon experiment was a single event with a small audience; it is not a validated study.

**Methodological Soundness:** Polyphonic case studies are adequately documented as reported claims. The Emmy experiment is real but methodologically limited. The broader claim—that algorithms can "create"—rests on definitional work about creativity that Steiner does not perform rigorously.

---

### Chapter 4: The Secret Highways of Bots—Infrastructure

**Core Claim:** Speed is the decisive competitive variable in algorithmic trading, and the arms race to eliminate latency has produced infrastructure—like Spread Networks' 825-mile dark fiber line—that materially reshapes the physical economy.

**Supporting Evidence:**
- Spread Networks completed a straight-line dark fiber route from Chicago to New York, reducing round-trip latency from ~17ms to 13ms—a 4ms improvement. Construction cost: minimum $200M.
- Lease rates: $3M/year per client vs. $300K for standard dark fiber.
- Built in total secrecy over 18 months with 125 simultaneous construction crews.

**Logical Method:** Economic logic of winner-take-all speed advantage: in arbitrage strategies, being 1ms faster captures all available profit; being 1ms slower captures none. This creates near-infinite willingness to pay for marginal speed improvements.

**Logical Gaps:**
- The chapter does not address whether a 4ms advantage translates into proportional profit advantage. The relationship between latency reduction and trading revenue is asserted, not quantified.
- By publication, microwave networks were already threatening to render dark fiber obsolete (Ciello Networks is mentioned but underweighted as a competitive threat).
- The argument that Wall Street hardware investment democratizes technology through spillover conflates private profit-seeking with social benefit.

**Methodological Soundness:** The Spread Networks account is well-reported and internally consistent. Latency figures are accurate and verifiable. The democratization argument is asserted rather than demonstrated.

---

### Chapter 5: Gaming the System—Poker, Sports, and Game Theory

**Core Claim:** Game theory algorithms navigating incomplete information (unknown opponent strategies, hidden variables) are the frontier of algorithmic capability—with applications from poker to airport security to geopolitical prediction with documented accuracy superior to human experts.

**Supporting Evidence:**
- Sandholm's poker bot defeated all humans in head-to-head *limit* poker by 2012.
- Bueno de Mesquita's game theory algorithms predicted the Soviet collapse and the Arab Spring. In a CIA study spanning ~20 years, his algorithms were right twice as often as CIA analysts.
- LAX deployed Sandholm-inspired security patrol algorithms in 2007; TSA adopted similar tools nationally.
- Philip Tetlock's survey of 2,000 political experts found their predictions were no better than randomly assigned probabilities.

**Logical Method:** Demonstrated superiority over human experts in controlled conditions. The Tetlock finding establishes the baseline: human expert political prediction is at chance level. Sandholm's poker results provide the cleanest experimental evidence since poker has defined rules and measurable outcomes.

**Logical Gaps:**
- The CIA superiority claim (right twice as often) is presented without the study's methodology, sample size, or evaluation criteria. What counts as a "correct" geopolitical prediction is a significant operationalization problem Steiner does not address.
- The Iran nuclear prediction—that Iran would develop weapons-grade uranium but not build a bomb—is presented as a confirmed success, but proof of the negative (did not build a bomb) is unfalsifiable at time of writing.
- Sandholm's bot "slightly lags" humans in no-limit and multi-player games. This limitation is acknowledged but underweighted, given that no-limit is the prestige format.

**Methodological Soundness:** Poker results are the most methodologically clean evidence in this chapter. The CIA claim is the weakest, presented with insufficient transparency. The Tetlock expert-forecasting research is legitimately cited and well-established.

---

### Chapter 6: Paging Dr. Bot—Medicine

**Core Claim:** Algorithms will displace human judgment across routine medicine—diagnosis, pharmacology, test analysis—and produce better outcomes at lower cost, with the residual human role being the unusual and contextually complex case.

**Supporting Evidence:**
- UCSF's robotic pharmacy filled 2 million prescriptions without error; human pharmacist error rate estimated at 1–1.7% (37–63M errors annually across 3.7B U.S. prescriptions).
- BD's algorithm combined with cytotechnologist detected 86% of cancer instances vs. 76% without it (Pap tests).
- Algorithms improved radiologist nodule detection by 16% on MD CT scans.
- Intermountain Medical Center: coronary bypass mortality 1.5% vs. 3% nationally; pneumonia death rates 40% below national average.
- IBM Watson correctly diagnosed atypical vitamin-D-resistant rickets in seconds; human physicians had missed it for 15 years.

**Logical Method:** Comparative effectiveness studies plus Watson's singular diagnosis demonstration. The pharmacy error rate comparison is particularly strong because the baseline is documented, not constructed.

**Logical Gaps:**
- Intermountain's results conflate algorithmic decision-making with Dr. Brent James's broader data-driven culture change. The two are not separated.
- The 86% vs. 76% detection improvement was conducted by BD, a company selling the algorithm—a conflict of interest not acknowledged.
- The Watson case study is a single anecdote, not a clinical trial.
- Khosla's claim that algorithms will replace 90–99% of physician need is cited without challenge.

**Methodological Soundness:** Pharmacy robot and Pap test figures are the most credible. The broader displacement claim is advocacy-inflected. Jerome Groopman's counterargument—that algorithmic medicine makes doctors worse at atypical cases—is presented fairly.

---

### Chapter 7: Categorizing Humankind—Personality Algorithms

**Core Claim:** Human personality can be reliably categorized through speech pattern analysis (Taibi Kahler's Process Communication Model), this categorization can be automated, and matching people with compatible personality types in customer service contexts doubles resolution rates while halving call duration.

**Supporting Evidence:**
- NASA adopted Kahler's method after McGuire found it predicted crew conflict with higher accuracy than any other tool; right on 5 of 6 predicted crew conflicts.
- E-Loyalty tested personality-matching on 1,500 Vodafone calls: matched personalities → 5-minute calls, 92% resolution; mismatched → 10-minute calls, 47% resolution.
- Vodafone's personality-targeted sales approach produced an 8,600% increase in sales success.
- E-Loyalty analyzed 750 million conversations; 600 terabytes of customer data by 2011.

**Logical Method:** Controlled comparison (matched vs. mismatched personality pairs) with measurable outcomes. NASA application provides independent validation of Kahler's base methodology in a high-stakes domain.

**Logical Gaps:**
- 1,500 calls across 12 agents is a small sample for the magnitude of the claimed effect.
- The 8,600% sales increase is extraordinary and requires methodological context—baseline conversion rate, observation duration, control conditions—that is absent.
- Whether the personality-matching study has been independently replicated is not established.
- The psychometric reliability and validity of the 6-type classification system is not discussed.

**Methodological Soundness:** NASA adoption provides external credibility for Kahler's framework. The core claim is plausible and consistent with psychological research on rapport. But the reported effect sizes strain credulity without rigorous methodological disclosure.

---

### Chapters 8–10: Wall Street vs. Silicon Valley / The Future

**Core Claim:** The 2008 financial collapse functioned as a talent redistribution event, redirecting quantitative engineering from Wall Street's zero-sum arbitrage games toward Silicon Valley's platform and data businesses, with measurable benefit to the broader economy.

**Supporting Evidence:**
- MIT finance graduates rose 67% from 2000 to 2006, reaching 25% of the class. Post-2008, Goldman and Morgan disappeared from university recruiting events.
- Jeffrey Hammerbacher left Bear Stearns for Facebook and co-founded Cloudera.
- Conway recruited 60 algorithm builders in two years post-2008.
- Kauffman Foundation: 60%+ decline in entrepreneurship rates among experienced engineers since the early 1980s, correlating with Wall Street's talent drain.

**Logical Method:** Structural economic argument: talent follows compensation, 2008 repriced Wall Street compensation and social prestige downward, Silicon Valley remained high, therefore talent reallocated. Supplemented by direct testimony from engineers who switched.

**Logical Gaps:**
- The Kauffman Foundation correlation (financial sector growth → entrepreneurship decline) is correlation, not causation.
- Steiner assumes Wall Street and Silicon Valley compete for identical talent pools—this is partially true but overstated.
- The policy prescription (forgive engineering student debt for non-finance careers) is asserted without analysis of incentive effects or implementation feasibility.
- The closing optimism ("the door is open for anybody") is rhetorical conclusion, not logical inference from the preceding analysis.

**Methodological Soundness:** The post-2008 talent shift is real and documented. The causal chain from financial sector dominance to reduced entrepreneurship is plausible but not proven by available evidence.

---

## BRIDGE: Synthesizing the Logical Architecture

Steiner's book advances one thesis through three nested arguments. The surface thesis is descriptive: algorithms already govern most economically significant decisions in developed economies. The middle thesis is predictive: this governance will expand until algorithms touch every domain of human activity. The deepest thesis is cautionary: this expansion is largely beneficial but carries systemic risks that current oversight mechanisms are inadequate to manage.

**Four structural tensions run through every chapter:**

**Tension 1: Optimization vs. Systemic Fragility.** Every algorithm is optimized for a narrowly defined objective function. The Amazon pricing bots were optimizing price relative to a competitor. The Flash Crash algorithms were optimizing execution speed and position hedging. Both produced catastrophic macro-level outcomes from locally rational micro-level decisions. Steiner establishes this tension in the introduction and never resolves it—he offers no framework for distinguishing safe from dangerous optimization domains.

**Tension 2: Replication vs. Improvement.** The book oscillates between two distinct arguments for why algorithms succeed: (A) they faithfully replicate what skilled humans do, only faster and more consistently, and (B) they outperform the best humans by accessing patterns humans cannot perceive. These require different evidence. Peterffy (replication) and Bueno de Mesquita's CIA algorithms (genuine improvement) are treated as instances of the same phenomenon when they are structurally different.

**Tension 3: Democratization vs. Concentration.** Steiner repeatedly argues that algorithmic technology democratizes access. But the evidence more consistently shows concentration: Spread Networks' $3M/year dark fiber is accessible only to the largest traders; personality-matching algorithms are deployed by corporations against individual consumers; Wall Street's talent absorption depressed broader economic innovation for two decades. The democratization argument requires substantially more evidence than Steiner provides.

**Tension 4: Determinism vs. Contingency.** The historical narrative presents the algorithmic takeover as the inevitable consequence of mathematics developed over three centuries. But the biographical chapters—Peterffy hacking the NASDAQ, Cope stubbing his opera commission, Sandholm hearing a conference talk—are stories of radical contingency. The book does not reconcile these framings.

**Most proven claims:** Algorithms outperform humans in narrowly defined, measurable, data-rich domains (trading spreads, image scanning for cancer, pharmacology cross-checks). The post-2008 talent shift is real and documented.

**Most significant unproven claims:** Algorithms will achieve general equivalence with human creativity; algorithmic expansion will primarily democratize rather than concentrate power; the CIA superiority claim as stated.

---

## PART 2: LITERARY REVIEW ESSAY

# The Optimization Problem We Cannot Escape

Consider the precise mathematical problem that opens Christopher Steiner's *Automate This*: two Amazon seller algorithms, each programmed to set its price slightly higher than its competitor's, entered a price war whose logic ran in the wrong direction. Neither algorithm contained a termination condition. Neither checked whether its output remained within any plausible range of human intent. The price of a 1992 academic book about fly genetics reached $23.7 million. A human stopped it.

This incident—trivial in its consequences, clarifying in its logic—reveals the central problem of algorithmic governance that Steiner's book both explores and, ultimately, cannot solve: every algorithm optimizes for its defined objective function with perfect fidelity, and the objective function is never quite right.

Steiner's argument, assembled from a decade of journalism and structured as a survey of algorithmic invasion across finance, medicine, music, intelligence, and everyday life, is that algorithms have already won. They execute 60% of U.S. stock trades with no meaningful human oversight. They diagnose cancers more accurately than radiologists in controlled conditions. They compose music indistinguishable from Bach. They predict geopolitical events twice as accurately as CIA analysts. The book was published in 2012. By any reasonable measure, these forecasts proved conservative.

What makes the book worth interrogating now is not its predictions—largely vindicated—but its reasoning. Steiner is a journalist rather than a mathematician, and he sometimes treats algorithmic capability claims with less skepticism than the evidence warrants. But he is a more careful observer than his genre typically produces, and in several moments his reporting discovers something his framing does not fully acknowledge: the humans who built these systems were often not sophisticated practitioners implementing proven theory but hackers improvising workarounds, and the systems that succeeded often did so by exploiting institutional vulnerabilities rather than by being genuinely better.

---

Thomas Peterffy's Wall Street conquest is the book's founding case, and it is instructive in ways Steiner does not fully develop. Peterffy did not arrive on Wall Street with a superior theory of markets. He arrived as a programmer who understood that the existing infrastructure of market-making—human traders at NASDAQ terminals, updating prices with finite reaction times—had exploitable latency. His algorithms did not know more than human traders about whether IBM would rise. They knew how to update prices 500 milliseconds faster. The advantage was entirely institutional: the market's rules assumed human actors, and Peterffy had introduced a class of actor that didn't fit the assumptions.

I argue this matters because if the story of algorithmic success on Wall Street is primarily a story of exploiting institutional latency rather than intellectual superiority, then the democratization narrative Steiner builds on top of it is suspect. The 60% of trades executed by algorithms are not producing better price discovery or more efficient capital allocation than human market-makers did. They are, as Peterffy himself concedes in the book's most honest passage, an arms race whose primary social product is volatility risk: his "ultimate fear is that a rogue series of algorithms sparks a string of colossal losses that the owners can't cover." The man who built the revolution regards it as having gone too far. This deserves more analytical weight than Steiner gives it.

---

The book's strongest empirical section is medicine, and it is worth understanding why. The pharmacy robot at UCSF filled 2 million prescriptions without error. Human pharmacists produce errors at roughly 1–1.7%—meaning somewhere between 37 and 63 million prescription errors annually in the United States. Algorithms cross-checking drug interactions against a complete patient medication record do not get tired, do not get distracted, and do not forget what the previous pharmacist already prescribed. This is not a story about algorithmic creativity or insight. It is a story about the fundamental human limitations of attention and memory in high-volume, high-stakes environments—and the fact that a well-structured lookup table outperforms a fatigued human professional in exactly those conditions.

This distinction sets the correct scope for algorithmic advantage. Where the task is: retrieve the correct item from a large database, cross-reference against defined constraints, and flag any violation—algorithms are not merely better than humans, they are categorically better. Human performance on such tasks degrades with volume, fatigue, and time pressure. Algorithmic performance is flat. This is the same logic explaining why algorithms beat radiologists at detecting lung nodules (16% improvement) and why they detect more cancer in Pap smear screening (86% vs. 76%). These are pattern-recognition tasks with defined correct answers and large training datasets. They are not tasks requiring clinical judgment, empathy, or the ability to recognize that a patient's complaint is the wrong complaint.

Jerome Groopman's objection—that algorithmic medicine makes doctors worse at the unusual and atypical case—is given a fair hearing in Steiner's book, and his proposed resolution (give routine cases to algorithms, reserve unusual cases for physicians) is intuitively appealing but underspecified. The clinical problem is that you do not know a case is unusual until you have already processed it through the routine pathway and found it doesn't fit. The algorithm that dismissed Anne Dodge's symptoms as anorexia was not doing anything wrong by its design specifications. It matched her symptoms against prior presentations. The failure was a failure to recognize that the pattern-matching itself was wrong—a recognition that required a human holding contradictory hypotheses simultaneously until one became untenable.

---

The book's most intellectually honest passage arrives in the discussion of personality-matching algorithms derived from NASA's astronaut selection methodology. Kelly Conway's E-Loyalty documented that matching customer service callers with agents of compatible personality types doubled resolution rates (92% vs. 47%) while halving call duration. Steiner reports this but does not follow its implication: if deployed universally, this technology systematically routes like-minded people into contact with each other, reducing the frequency with which people must navigate across personality difference. This is not democratization. It is optimization in the service of corporate cost reduction that incidentally reduces the social friction that produces tolerance, negotiation, and accommodation. Steiner raises this concern in a single paragraph and does not return to it.

The Kopp finding in the AutoTutor literature—that mixing intense dialog with periods of no dialog outperformed exclusively intense dialog—has an analog here. Optimizing for measured outcomes (call resolution rate, call duration) removes exactly the friction that produces adaptability, tolerance, and growth. You can make the metric go up and make the underlying thing go down. Steiner sees this in personality-matching and sets it aside. That is the book's most significant intellectual retreat.

---

What *Automate This* ultimately demonstrates, beneath its survey of algorithmic conquests, is that the humans most threatened by algorithm invasion are those whose professional value was always primarily about processing volume and applying defined rules—radiologists reading routine scans, pharmacists cross-checking drug interactions, junior lawyers reviewing documents, market-makers maintaining bid-ask spreads. These roles were never really about judgment. They were about attention, consistency, and the patience to perform the same cognitive operation ten thousand times. Algorithms are categorically better at those tasks.

The humans least threatened are those whose value exists precisely in the places algorithms fail: recognizing that the defined task is the wrong task; holding multiple contradictory hypotheses in tension until one becomes untenable; noticing the thing that was not in the training data; making a decision whose consequences are moral rather than computational. David Cope's Emmy algorithm composed chorales indistinguishable from Bach in a controlled single-session test. But Emmy could not decide to destroy itself—which Cope did in 2004, out of exhaustion, principle, and something that looks like artistic conscience. That decision was not in the training data.

The question Steiner's book raises and does not answer is the right one: not whether algorithms will take over, but whether the humans who survive that takeover will be the ones who learned to write better algorithms, or the ones who learned to ask better questions. The evidence in *Automate This*, read carefully, suggests the latter—and that is a more hopeful conclusion than the book's closing techno-optimism manages to articulate.

---

**Tags:** algorithmic trading history Thomas Peterffy, high-frequency trading Flash Crash systemic risk, algorithmic displacement professional labor markets, music composition AI creativity Emmy David Cope, geopolitical prediction game theory CIA Bruce Bueno de Mesquita
