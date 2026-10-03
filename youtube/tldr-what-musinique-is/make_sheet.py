#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-what-musinique-is.

tldr skill (brutalist.art/skills/make/tldr). Source: musinique/SKILLS-BREAKDOWN.md
(planning document, 2026-09-22) + riffs/musinique/README.md (the label) + the
Musinique artist profiles. Section S1 of youtube/tldr-sections-skills-breakdown.md,
picked by Bear's request 2026-09-23 ("a TLDR in colors and default voice giving an
overview of what Musinique is").

Bear's rules, enforced at the bottom:
  · NO mention of any paid voice vendor anywhere — narration, screen or metadata.
  · No misspellings — every word on screen and in narration is checked against the
    system dictionary plus an explicit allow-list of names.
Honesty rule: the toolkit is a PLAN (nothing scaffolded yet); the film says so.

Preserves measured fields when re-run over an existing sheet with unchanged narration.
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLUG = "tldr-what-musinique-is"
TITLE = "What Musinique Is"
TOPIC = "Musinique · Tools For Indie Musicians"


def beat(bid, act, narration, shot, role=None, section=None, learn=None, lane="manim", proof="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": proof}
    if section is not None: b["section"] = section
    if role: b["role"] = role
    if learn: b["learn"] = learn
    b.update({"narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.6, 1),
              "voice": "am_onyx", "engine": "kokoro", "shot": shot})
    b.update(extra); return b

def manim(cls, intent, show, claim):
    return {"type": "GRAPHIC", "source": "own", "visual_intent": intent, "show": show, "manim": {"class": cls}, "motion_claim": claim}

def remotion(pattern, props, show):
    return {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}

def L(q, a, o, i, n):
    return {"question": q, "action": a, "observation": o, "inference": i, "next_question": n}

beats = []

beats.append(beat("B00", "tldr · what",
    "Namasté. This is Liam, in for Bear. "
    "This film is about what Musinique is. "
    "It's an independent label, and now a free toolkit being built for indie musicians. "
    "The machine offers drafts and does the busywork. You listen, refine, and make the calls, on your own data. "
    "And the trap: thinking it's one more AI that writes your songs for you.",
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Namaste, Liam", "topic": TOPIC,
        "question": "What is Musinique, and what is it for?",
        "lines": ["A label, and a free toolkit being built for indie musicians.",
                  "The machine drafts and does the busywork; you listen, refine and decide.",
                  "The trap: one more AI that writes your songs for you."],
        "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Namaste, Liam'; topic line; heading"},
         {"at": 0.2, "event": "the question writes on at 'This film is about'"},
         {"at": 0.35, "event": "line 1 on 'an independent label'"},
         {"at": 0.6, "event": "line 2 on 'The machine offers drafts'"}, {"at": 0.85, "event": "line 3 on 'the trap'"}]),
    lane="bookend", motion_claim="TL;DR card one, WHAT: the question writes on and the three lines land on their spoken clauses."))

beats.append(beat("B01", "tldr · why",
    "Why should you care? For an indie artist, the scarce thing isn't songs. It's money and attention. "
    "Pay for the wrong playlist, and the streams can be fake and the money gone. "
    "Skip the release chores, and the song stays invisible. "
    "Get the decisions right, and a small budget goes where a record, not a feeling, says it can matter.",
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": TOPIC,
        "lead": "The scarce thing isn't songs. It's money and attention.",
        "lines": ["Pay for the wrong playlist: fake streams, money gone.",
                  "Skip the release chores: the song stays invisible.",
                  "Decide on the record, and a small budget goes further."],
        "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"}, {"at": 0.1, "event": "the stake writes on"},
         {"at": 0.4, "event": "dash 1 on 'Pay for the wrong playlist'"}, {"at": 0.62, "event": "dash 2 on 'Skip the release chores'"},
         {"at": 0.8, "event": "dash 3 on 'Get the decisions right'"}]),
    lane="bookend", motion_claim="TL;DR card two, WHY: the stake writes on; three consequences land on their clauses.",
    qc={"sparse_by_design": True, "sparse_reason": "TL;DR page, card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The real question: what will it help me decide? "
    "'What will it write for me' is the trap. Drafts got cheap, and every tool makes them now. Deciding what's good, and where your time and money go, did not.",
    remotion("BrutalistHesitantWriter", {
        "text": "My song is finished.\nAnother AI music tool.\nWhat will it write for me?",
        "triggerWords": "write for me", "replacementWords": "help me decide",
        "fontSize": 64, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1, "mistakeRate": 5, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'My song is finished.'"}, {"at": 0.3, "event": "types 'Another AI music tool.'"},
         {"at": 0.55, "event": "types 'What will it write for me?' then corrects 'write for me' → 'help me decide'"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive question and corrects the phrase that makes it wrong: writing → deciding.",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

beats.append(beat("B03", "terms",
    "Three terms. A distributor is a service, like DistroKid, that delivers your song to the streaming platforms. "
    "Spotify for Artists is Spotify's dashboard of your own streams, listeners, and their cities. "
    "And playlist placement is a fee paid to get a song added to someone's playlist.",
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "distributor", "meaning": "a service, like DistroKid, that delivers your song to the streaming platforms"},
                  {"term": "Spotify for Artists", "meaning": "Spotify's dashboard of your own streams, listeners and their cities"},
                  {"term": "playlist placement", "meaning": "a fee paid to get a song added to someone's playlist"}],
        "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "row 'distributor'"}, {"at": 0.48, "event": "row 'Spotify for Artists'"}, {"at": 0.75, "event": "row 'playlist placement'"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — 'the machine executes, you decide' and the gate are earned in the section."}))

S = "the week's jobs left (five rows), 'who does it' tags middle, a right panel for the case at hand, the budget bar bottom right (ink fill, no numbers)"

beats.append(beat("B10", "learn 1",
    "Here's an artist with a finished song. Now the week begins. "
    "Lyrics to finish, a title to clean, release files for the distributor, a description and a bio. "
    "And an offer: pay for a playlist placement, and a scanner says the playlist is clean. "
    "There's one small budget. So which of these jobs deserves it, and on what evidence?",
    manim("B10_TheWeek", f"The stage: {S}. A waveform grows in the right panel under 'a finished song'; the five jobs land on their spoken clauses with a dim '?' in the who column; the budget bar grows full; a terracotta dot beside the playlist row; caption 'which job gets the money?'.",
          [{"at": 0.05, "event": "waveform grows: a finished song"}, {"at": 0.25, "event": "jobs land one per clause"},
           {"at": 0.6, "event": "playlist row + dot"}, {"at": 0.75, "event": "budget bar grows"}, {"at": 0.9, "event": "the question caption"}],
          "The five jobs, the who column and the budget bar are the film's persistent objects; the unsolved case is who gets the money."),
    role="HOOK", section=1,
    learn=L("Which of this week's jobs deserves the one small budget?", "Lay out the jobs, the offer and the budget.",
            "Five jobs, one offer vouched for by a scanner, one bar of money.", "Something has to decide, and it isn't obvious what.",
            "Who should finish the lyrics?")))

beats.append(beat("B11", "learn 1",
    "Start with the lyrics. Musinique keeps each artist as data: a profile with the voice, the languages, the genres. "
    "Ask for ideas as Aditi Banksy, and you get post-punk spoken word drafts in five languages. "
    "Swap in Mama Sparrow, same request, and you get lullaby sketches. "
    "But a draft isn't a song. You sing it, hear it, cut it, and rewrite it. The machine suggests. You finish.",
    manim("B11_ArtistAsData", f"{S}. The lyrics row is spotlit; a profile card grows in the right panel (Aditi Banksy · post-punk · spoken word · five languages); it morphs into Mama Sparrow's (lullabies · close-miked soprano); a loop 'draft → hear → refine' draws under it with a return arrow; the lyrics row's tag becomes 'you finish'.",
          [{"at": 0.1, "event": "spotlight the lyrics row"}, {"at": 0.35, "event": "Aditi Banksy's profile card"},
           {"at": 0.62, "event": "morphs to Mama Sparrow's"}, {"at": 0.75, "event": "the draft → hear → refine loop"}, {"at": 0.92, "event": "tag: you finish"}],
          "Change one profile, watch the drafts follow; then the loop shows the finishing is human work."),
    role="INSTANCE", section=1,
    learn=L("Who finishes the lyrics?", "Run the same request through two artist profiles, then name what a draft still needs.",
            "The drafts follow the profile; none of them is a finished song.",
            "The machine can suggest from data; singing, hearing and rewriting are yours.", "What about the release chores?")))

beats.append(beat("B12", "learn 1",
    "Now the release. A working title like this one: a version tag, the word final, a year. "
    "The stores want a clean title, so the machine strips it to 'A Freedom Riders Prayer'. "
    "Same with the lyrics: 'chorus, two times' becomes the chorus, written out twice. "
    "These rules are fixed, so a test can prove them. Again, the machine does it.",
    manim("B12_CleanTheRelease", f"{S}. The title row is spotlit; in the right panel a messy working title (constructed) gets its version tag, 'FINAL' and year struck through and collapses to 'A Freedom Riders Prayer'; '[Chorus 2x]' expands into two chorus lines; the title and files rows' tags become 'the machine'.",
          [{"at": 0.1, "event": "the messy title"}, {"at": 0.4, "event": "strikes; collapses to the clean title"},
           {"at": 0.62, "event": "chorus expands"}, {"at": 0.88, "event": "tags: the machine"}],
          "Second instance, same move: fixed rules, one clean result, provable by a test."),
    role="INSTANCE", section=1,
    learn=L("Who cleans the release?", "Apply the fixed title and lyric rules to a messy example.", "The output is the same every time.",
            "Rule-bound chores are execution; a test can prove them.", "So should the machine just do everything?")))

beats.append(beat("B13", "learn 1",
    "So is that the whole idea? An AI that does everything, faster? Let's try it. "
    "Hand every job to the machine, even the lyrics, even the playlist. The scanner said clean, so it pays. "
    "Watch the budget. Everything got faster, and the money still went to the one job that speed can't answer.",
    manim("B13_DoItAllFaster", f"{S}. The lyrics row and the last two rows flip to 'machine' in quick succession; the playlist row reads 'paid'; the budget bar shrinks to a sliver; a terracotta X beside it; caption 'faster work, same bad bet'.",
          [{"at": 0.2, "event": "tags flip fast"}, {"at": 0.45, "event": "the playlist: paid"}, {"at": 0.7, "event": "the budget drains"},
           {"at": 0.9, "event": "X + caption"}],
          "The natural wrong turn, walked: every job speeds up and the budget still drains."),
    role="NAIVE", section=1,
    learn=L("Is Musinique an AI that does every job faster?", "Hand the playlist decision to the machine too.", "The budget drains on the scanner's word.",
            "Speed doesn't answer where the money should go.", "Then what kind of job is the playlist?")))

beats.append(beat("B14", "learn 1",
    "Back up. Here's the reframe. Every job is one of two kinds. "
    "Execution: clean the title, fill in the forms, draft the description. That's cheap now, and the machine should do it. "
    "Or a decision: which lyric is true, release this, pay for that. A decision needs a person, and evidence: your ear, your data. "
    "The machine can offer drafts for it, but Musinique sorts every job into one of those two kinds.",
    manim("B14_TwoKinds", f"{S}. The budget refills (rewind); an execution bracket draws beside the three chore rows; decision marks draw beside the lyrics row ('your ear') and the playlist row ('your data'); the lyrics tag returns to 'you finish' and the playlist lands on 'you decide' with a terracotta dot.",
          [{"at": 0.08, "event": "rewind: budget refills"}, {"at": 0.25, "event": "divider draws; two headers"},
           {"at": 0.45, "event": "execution tags settle"}, {"at": 0.75, "event": "the playlist moves to 'you decide'"}],
          "The representation: every job is execution or a decision, and only a decision can protect the budget."),
    role="SHIFT", section=1,
    learn=L("What kind of job is the playlist?", "Sort every job into execution or decision.", "Four jobs are execution; the playlist is a decision.",
            "Execution goes to the machine; a decision needs evidence and a person.", "What evidence does the decision have?")))

beats.append(beat("B15", "learn 1",
    "So look at the playlist with your own data. The scanner says clean. "
    "Your Spotify for Artists page says the playlist has about a dozen followers, sends you hundreds of streams a day, "
    "and the top city is Ashburn, Virginia. "
    "Before it moves: pay, or skip?",
    manim("B15_Commit", f"{S}, split. The right panel fills with evidence rows: 'the scanner: clean' (dim), then 'followers · about a dozen', 'streams · hundreds a day', 'top city · Ashburn, Virginia' (example numbers, captioned); a terracotta dot; caption 'commit: pay, or skip?'; hold.",
          [{"at": 0.15, "event": "the scanner line"}, {"at": 0.35, "event": "three evidence lines land"}, {"at": 0.8, "event": "HOLD: commit"}],
          "Predict before the reveal: the objects hold while the viewer commits."),
    role="INSTANCE", section=1, predict=True,
    learn=L("With your own data on screen, pay or skip?", "Put the scanner's verdict beside your Spotify for Artists numbers.",
            "The viewer commits to an answer.", "A prediction makes the next beat evidence.", "Watch the gate.")))

beats.append(beat("B16", "learn 1",
    "Skip. Ashburn is one of the world's biggest data-center hubs, and a dozen followers rarely explain hundreds of plays a day. "
    "In the plan, a data-center city is a gate, not a vote. It vetoes the payment, whatever the scanner said. "
    "And look at the budget. It never moved.",
    manim("B16_TheGateVetoes", f"{S}, split, evidence up. 'top city' morphs to 'a data-center hub'; a terracotta X lands by 'the scanner: clean'; an ink gate bar drops across the playlist row; the row rewrites to 'Skip this playlist'; the full budget bar is indicated.",
          [{"at": 0.1, "event": "'a data-center hub'"}, {"at": 0.4, "event": "X by the scanner"}, {"at": 0.6, "event": "gate drops; row: skip"},
           {"at": 0.88, "event": "the budget, untouched"}],
          "The collision: one fact from the artist's own data vetoes the spend, and the budget the naive run lost stays whole."),
    role="TRANSFORM", section=1,
    learn=L("Pay or skip?", "Apply the data-center gate to the evidence.", "The gate vetoes the payment; the budget stays full.",
            "A gate on your own data outranks the scanner's verdict.", "So what is Musinique, in one line?")))

beats.append(beat("B17", "learn 1",
    "That's what Musinique is. The machine does the chores and suggests drafts. You listen, decide, and finish, on your own data. "
    "It doesn't try to do everything itself. Brand and copy go to Madison. Video goes to brutalist dot art. "
    "Musinique keeps the part in the middle: what to make, what to release, and where the money goes.",
    manim("B17_TheMiddle", f"{S}, split, gate down. Evidence clears; 'the machine suggests · you decide' lands bold under the columns; two ink arrows draw from the right panel to 'Madison · brand and copy' and 'brutalist.art · video'; the middle labelled 'Musinique: what to make, release, and fund'.",
          [{"at": 0.1, "event": "the rule, bold"}, {"at": 0.4, "event": "arrow to Madison"}, {"at": 0.55, "event": "arrow to brutalist.art"},
           {"at": 0.8, "event": "the middle, named"}],
          "The abstraction arrives as the name for every sort we just watched, and the two neighbors take what Musinique doesn't do."),
    role="ABSTRACTION", section=1,
    learn=L("What is Musinique, in one line?", "Name the rule behind every sort; route brand and video out.",
            "Every job fell to the machine or to you; two kinds of work leave for the neighbors.",
            "The machine executes, you decide on your own data; Madison and brutalist.art handle brand and video.",
            "Back to the artist's week.")))

beats.append(beat("B18", "learn 1",
    "Back to our artist. Same song, same week. "
    "The chores are done by the machine, the lyrics are yours, finished by ear, and the budget is still there for something the evidence supports. "
    "One honest note: Musinique is a plan today, and the build is just starting. "
    "Not taught here: how the audit weighs each piece of evidence. That's your turn.",
    manim("B18_SameWeekMoneyKept", f"{S}. The hook view returns: the waveform, the five rows, each now ticked with an ink dot; the budget bar full; caption 'same week · money kept'; a dim boundary caption 'a plan today · not taught: how the audit weighs evidence'.",
          [{"at": 0.05, "event": "the week returns"}, {"at": 0.3, "event": "rows tick one by one"}, {"at": 0.55, "event": "'same week · money kept'"},
           {"at": 0.85, "event": "boundary caption"}],
          "The HOOK's objects resolve: same week, busywork done, the money kept for a decision the evidence supports."),
    role="PAYOFF", section=1,
    learn=L("So which job deserved the budget?", "Return to the hook's week, resolved.", "Every row is done and the budget is whole.",
            "The machine took the chores; the decision kept the money.", "")))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. Musinique is an independent label, and a free toolkit being built for indie musicians. "
    "The machine suggests lyric drafts and does the chores: clean titles, release files. "
    "You hear, refine, and decide, on your own data, and a gate vetoes a bad spend. "
    "Brand and copy go to Madison. Video goes to brutalist dot art.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["A label, and a free toolkit being built for indie musicians.",
                          "The machine suggests drafts and does the chores.",
                          "You hear, refine and decide; a gate vetoes a bad spend.",
                          "Brand and copy go to Madison; video goes to brutalist.art."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("Here is a playlist offer I received: [paste the offer]. "
      "Here is what my Spotify for Artists page shows for that playlist: [paste followers, streams per day, top cities, and the date my song was added]. "
      "Do not tell me whether to pay yet. "
      "First, list which of these facts you can check and which you are only inferring. "
      "Then name any top city that is a known data-center hub, and compare streams per day with followers. "
      "Finish with one question I must answer before I spend anything.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it separate what it checked from what it inferred? "
    "And did it leave the decision with you?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "Musinique · YOUR TURN", "segment": "Audit A Playlist Offer",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: it separated what it checked from what it inferred.",
                   "Check: it left the decision with you."],
        "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5", "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.85, "event": "two check lines"}]),
    lane="bookend"))

beats.append(beat("BOUT", "outro", f"{TITLE}. At Nik Bear Brown.",
    remotion("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""},
             [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Spoken, no jingle."}]),
    lane="bookend", kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad into the mp3); no jingle (OUTRO-LOCK §Voice)"))

# ═══════════ Bear's rules, enforced ═══════════
SKIP_KEYS = ("durationSeconds", "cues", "fontSize", "charMs", "hesitateBetween", "hesitateWithin", "mistakeRate", "jitter",
             "seed", "slug", "modelLabel", "effortLabel", "folderLabel", "handle", "eyebrow")
def _texts(b):
    yield b["narration_text"]
    props = b["shot"].get("remotion", {}).get("props", {})
    for k, v in props.items():
        if k in SKIP_KEYS: continue
        if isinstance(v, str): yield v
        elif isinstance(v, list):
            for x in v: yield json.dumps(x, ensure_ascii=False) if not isinstance(x, str) else x

# 1 · no paid voice vendor named, anywhere
VOICE_BAN = re.compile(r"\b[e]leven|paid voice|voice clon", re.I)          # the vendor is never named, even here
vhits = [(b["beat_id"], t) for b in beats for t in _texts(b) if VOICE_BAN.search(t)]
assert not vhits, vhits

# 2 · no misspellings (system dictionary + names/terms allow-list; the Manim scenes are checked by spell_scenes())
ALLOW = {"musinique", "liam", "namaste", "namasté", "tl", "dr", "tldr", "distrokid", "spotify", "madison", "brutalist", "aditi",
         "banksy", "ashburn", "nik", "bear", "brown", "claude", "indie", "chorus", "lullaby", "playlist", "playlists", "busywork",
         "post", "punk", "miked", "hubs", "hub", "isn't", "can't", "it's", "that's", "doesn't", "here's", "someone's", "spotify's",
         "artist's", "world's", "don't", "i'm", "fx", "ai", "copy", "center", "data", "verdict", "online", "ok", "mama", "sparrow", "toolkit", "bio", "paid", "inferring", "inferred"}
_words = None
def _dict():
    global _words
    if _words is None:
        _words = {w.strip().lower() for w in open("/usr/share/dict/words")}
    return _words
def spell(text):
    bad = []
    for w in re.findall(r"[A-Za-zÀ-ÿ']+", text):
        lw = w.lower().strip("'")
        if len(lw) < 3 or lw in ALLOW or lw in _dict(): continue
        if any(lw.endswith(s) and (lw[:-len(s)] in _dict() or lw[:-len(s)] + "e" in _dict())
               for s in ("s", "es", "ed", "d", "ing", "er", "ers", "ly", "'s")): continue
        if lw.endswith("ies") and lw[:-3] + "y" in _dict(): continue
        bad.append(w)
    return bad
shits = [(b["beat_id"], w) for b in beats for t in _texts(b) for w in spell(t)]
assert not shits, shits

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": f"{TOPIC} · TL;DR", "skill": "tldr", "style_preset": "tldr",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "independent musicians, and anyone curious what the Musinique toolkit is for",
    "source_doc": "musinique/SKILLS-BREAKDOWN.md (plan, 2026-09-22); riffs/musinique/README.md (the label); artist profiles (Aditi Banksy, Mama Sparrow); the Forensic Playlist Audit spec's example numbers",
    "sections": [{"n": 1, "title": TITLE, "key_case": "one indie artist's week after a finished song: five jobs, one budget, a playlist offer a scanner calls clean"}],
    "greeting_language": "Hindi (Namaste; narration spelled Namasté so Kokoro says the final vowel)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Musinique is the subject (Bear's own label and toolkit plan); no book or course is named.",
    "honesty_policy": "The toolkit is a plan (SKILLS-BREAKDOWN.md); the film says 'being built' and 'a plan today'. Playlist numbers are the audit spec's example, captioned as such.",
    "voice_policy": "Bear 2026-09-23: Liam, Kokoro am_onyx, the default voice; no voice vendor is named anywhere.",
    "tags": ["Musinique", "indie music", "independent artists", "playlist fraud", "Spotify for Artists", "DistroKid", "Claude", "Nik Bear Brown"]},
    "beats": beats}

out = HERE / "beat_sheet.json"
if out.exists():
    old = {b["beat_id"]: b for b in json.loads(out.read_text())["beats"]}
    for b in beats:
        o = old.get(b["beat_id"])
        if not o or o.get("narration_text") != b["narration_text"]: continue
        for k in ("actual_duration_s", "audio_file", "render_duration_s", "build"):
            if k in o: b[k] = o[k]
        op = o.get("shot", {}).get("remotion", {}).get("props", {}); np_ = b["shot"].get("remotion", {}).get("props")
        if np_ is not None:
            for k in ("durationSeconds", "cues"):
                if k in op: np_[k] = op[k]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
meta_hits = [k for k, v in sheet["metadata"].items() if isinstance(v, str) and VOICE_BAN.search(v)]
assert not meta_hits, meta_hits
print(f"{len(beats)} beats → {out}; voice-ban clean; spelling clean")
