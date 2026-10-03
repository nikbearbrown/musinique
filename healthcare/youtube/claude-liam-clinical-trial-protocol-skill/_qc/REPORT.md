# Gate V — visual QC report
Run: 2026-08-25 (film-factory rebuild)

Frames sampled: 192 at 2fps from 96.1s master + per-beat at 15/50/85% of each span.
All beats are real VIDEO renders (no slates).

BLOCKER: 0  ·  MAJOR: 2 (downgraded, template-level, logged below)

---

### B00 (ClaudeComposerAsk)
PASS. Palette correct, "Hola, Liam" greeting, Opus 4.7 confirmed, @NikBearBrown footer,
one terracotta spark, safe margins clear, no overflow.

### B01 (SkillTeardownAnatomy)
PASS. File tree renders cleanly with README.md + SKILL.md accented in terracotta, callout
box present, spark "The file is the program." at bottom-left. Content fills ~45% of safe
area — above minimum. One terracotta accent (file labels).

### B02 (SkillTeardownPipeline)
PASS. Fixed double-terracotta: "Read SKILL.md" accent changed from true → false; OUTPUT/RESULT
box is now the single terracotta moment. Flow diagram clean, linear execution note visible,
spark correct.

### B03 (SkillTeardownMechanism)
MAJOR (downgraded — template limitation).
Content fills ~20% of safe area (heading + body + spark). The SkillTeardownMechanism
component renders minimal content per its design; the body text is 12 words (§8.5 maximum),
making the frame sparse by construction. Fixing requires component-level layout changes
outside this reel's scope. Previously flagged in Aug 3 QC report as well.
Justification: template characteristic, not a content error; no fix available at prop level.

### BVDT (ClaudeVerdictArtifact)
PASS. Verdict card with "1/2" pagination. "Claude, Clinical Trial Protocol Skill." heading
correct. Artifact lines clean, no truncation artifacts. One terracotta asterisk in header.

### BHTF (ClaudeComposerAsk)
PASS. "Your turn." greeting confirmed. Command text complete: "I want to generate clinical
trial protocols for medical devices or drugs. Read the clinical-trial-protocol-skill skill
and walk me through what you will do before you do it." — truncation artifact fixed.
Opus 4.7 confirmed, @NikBearBrown footer.

### BOUT (ClaudeTitleOutro)
MAJOR (downgraded — template limitation).
Title "Claude, Clinical Trial Protocol Skill." renders with terracotta period, @NikBearBrown
handle, and pixel-art mascot. Content centered but fills ~35% of safe area (intentional
negative-space template design). Previously flagged in Aug 3 QC report.
Justification: ClaudeTitleOutro uses deliberate negative space; not a defect introduced by
this rebuild. Pixel-art mascot uses crispEdges, no rotation (PIXEL-ART LAW satisfied).

---

## Downgrade log (required by VISUAL QC LAW)

| Beat | Issue | Downgrade from | To | Justification |
|------|-------|---------------|----|---------------|
| B03 | underfill ~20% | BLOCKER/MAJOR | noted/not-blocking | SkillTeardownMechanism component renders sparse by design; body text at §8.5 max (12 words); component layout fix required outside this reel |
| BOUT | underfill ~35% | MAJOR | noted/not-blocking | ClaudeTitleOutro deliberate negative-space design; consistent with all other skill-teardown reels using this outro |
