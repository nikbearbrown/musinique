### CHAPTER 10: Networking — How We Connect

**Core Claim:** The protocols underlying the internet—TCP/IP, packet switching, exponential backoff, AIMD flow control, acknowledgment systems—instantiate solutions to fundamental communication problems that also appear in human interaction. Exponential backoff is an optimal response to collision in any shared medium. Buffer bloat is a systemic pathology affecting both internet infrastructure and human attention. Latency, not bandwidth, is the critical metric for interactive communication.

**Supporting Evidence:**
- Packet switching vs. circuit switching: Kleinrock (ARPANET); robustness scales exponentially with network size under packet switching, exponentially declines under circuit switching
- TCP three-way handshake; acknowledgment numbers and serial number scheme
- Exponential backoff (Aloha Net, 1971): doubles the retransmission window after each collision; mathematically necessary for any collision-avoidance system with unknown population size; now standard in TCP
- HOPE program (Honolulu): exponential backoff applied to drug offender sentencing; 50% reduction in new crimes, 72% reduction in drug use; 17 states adopted
- AIMD (additive increase, multiplicative decrease): TCP sawtooth; conserves bandwidth while remaining responsive; Ruffgarden/Tardosh proof that selfish routing has price of anarchy ≤ 4/3
- Gordon/Prabhakar (2012): ants use flow control analogous to TCP; independent evolutionary discovery
- Buffer bloat (Gettys 2010): oversized buffers create latency disaster; affects all consumer networking equipment; fundamental design flaw exposed by cheap RAM
- Bavillus et al.: distracted listeners cause worse stories—storytelling is bidirectional, requires backchannels
- TCP sawtooth as model for dynamic promotion/demotion policies: AIMD applied to career management

**Logical Method:** Protocol documentation + mathematical proof (price of anarchy) + empirical social programs (HOPE) + experimental linguistics (backchannels) + biological parallel (ant flow control).

**Logical Gaps:**
- The price of anarchy ≤ 4/3 result for selfish routing is a mathematical theorem under specific assumptions (Wardrop equilibrium, continuous flow, specific latency functions). The authors use it to argue that decentralized internet routing is near-optimal and that self-driving cars won't dramatically reduce congestion. Both applications assume the theorem's conditions hold in the real world—a significant assumption.
- HOPE program: the 5-year DOJ study is the strongest evidence in the chapter, but the program conflates multiple interventions (swift punishment, predictability, graduated response) with exponential backoff specifically. The causal attribution to "exponential backoff" as mechanism is assumed rather than demonstrated.
- The buffer bloat analysis is accurate but the prescriptive implication—embrace tail drop and reject infinite buffering in human life—is metaphorical. The book does not examine whether the analogy breaks down for highly consequential queues (e.g., medical waitlists, emergency communications).
- The social media / always-buffered-never-connected critique is insightful but the book offers no empirical evidence that "tail drop" strategies in communication produce better outcomes. It is a thought experiment, not a finding.

**Methodological Soundness:** The networking content is technically accurate. The social applications are structurally sound as analogies but require empirical validation not provided.

---
