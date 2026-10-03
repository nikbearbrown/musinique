"""
Manim scenes for tldr-what-musinique-is (tldr skill — LEARN section 1, B10–B18).

3Blue1Brown template on the Claude cream stage. PERSISTENT OBJECTS across the section:
  · the WEEK'S JOBS (left) — five rows, one per job after a finished song;
  · the WHO column (middle) — '?' until a job is handed to the machine or to you;
  · the RIGHT PANEL — the case at hand (the song, a profile, a release, the evidence);
  · the BUDGET BAR (bottom right) — ink fill on a ghost track, no numbers.
Every scene rebuilds the previous scene's END state first (`_Stage` + the extras
factories), so the per-beat renders join as one continuous lesson.

Palette: ink objects, dim foils, ghost scaffolding; terracotta is ONE accent per beat,
only ever a Dot or an X beside a word (GATE T). Explicit coordinates only (Gate A stub).
Type floor 32, titles 40. Reveals land on the spoken word — `_until(t)` waits to second t
of the beat, and t comes from `at(beat, phrase)` over words.json (faster-whisper).
Render one:  manim -qh --fps 24 -r 1920,1080 scenes.py B16_TheGateVetoes
"""
import json as _json, os as _os, sys as _sys
from manim import *

_HERE = _os.path.dirname(_os.path.abspath(__file__))
_sys.path.insert(0, _HERE)
try:
    from cues import at as _at             # words.json phrase → seconds
except Exception:                           # Gate A/W copy scenes.py alone into a temp dir: no timings needed there
    def _at(beat, phrase, lead=0.15, nth=1):
        return 0.0

STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; SOFT = "#6E6A57"
SERIF = "EB Garamond"
config.background_color = STAGE

# ═══════════ the week (constructed teaching example — FACTCHECK.md) ═══════════
JOBS = ["Finish the lyrics", "Clean title and lyrics", "Build the release files", "Description and bio", "Pay for a playlist?"]
MACHINE, YOU, UNKNOWN, FINISH = "machine", "you decide", "?", "you finish"

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
except Exception:
    _TARGET = {}

def _now(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else None

def _until(self, t):
    n = _now(self)
    if n is None:
        self.wait(0.1)
    elif t - n > 0.04:
        self.wait(t - n)

def _w(self, phrase, lead=0.15, nth=1):
    """wait until the spoken phrase in THIS scene's beat"""
    _until(self, _at(type(self).__name__.split("_")[0], phrase, lead, nth))

def _finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    n = _now(self) or 0.0
    self.wait(max(1.0, target - n + 0.1) if target else 2.0)

# ═══════════ helpers ═══════════
def _title(txt, size=40):
    return Text(txt, font=SERIF, color=INK, font_size=size).to_edge(UP, buff=0.8)

def _t(s, size=32, color=INK, bold=False):
    return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")

def _tl(s, x, y, size=32, color=INK, bold=False):
    return _t(s, size, color, bold).move_to([x, y, 0], aligned_edge=LEFT)

def _dot(x, y, r=0.1, color=TERRA):
    return Dot([x, y, 0], radius=r, color=color)

def _x(x, y, s=0.18, w=8):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))

def _retitle(self, old, new_txt):
    new = _title(new_txt)
    self.play(FadeOut(old, shift=UP * 0.1), FadeIn(new, shift=UP * 0.1), run_time=0.5)
    return new

def _cap(txt, y=-2.5, color=SOFT, size=32):
    return _tl(txt, LX, y, size, color)

# ═══════════ stage geometry ═══════════
RY = [1.55, 0.8, 0.05, -0.7, -1.45]
LX = -6.0                 # job lines, left-aligned
OX = -1.2                 # who column, left-aligned
DX = -1.5                 # the accent dot, left of the who column
RX = 1.3                  # right panel, left edge
BY, BX0, BW, BH = -2.5, 3.75, 2.25, 0.28      # budget bar

def _job(i, s=None):
    return _tl(s or JOBS[i], LX, RY[i])

def _who(i, s):
    return _tl(s, OX, RY[i], 32, DIM if s == UNKNOWN else INK)

def _headers():
    return VGroup(_t("this week's jobs", 32, DIM).move_to([LX, 2.5, 0], aligned_edge=UL),
                  _t("who does it", 32, DIM).move_to([OX, 2.5, 0], aligned_edge=UL))

def _btrack():
    return Rectangle(width=BW, height=BH, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to([BX0 + BW / 2, BY, 0])

def _bfill(f):
    w = max(BW * f, 0.02)
    return Rectangle(width=w, height=BH, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([BX0 + w / 2, BY, 0])

def _blabel():
    return _tl("your budget", RX, BY, 32, DIM)

# the song: a waveform of wide ink bars (no text), right panel
WAVE_H = [0.35, 0.7, 1.1, 0.8, 1.35, 0.95, 0.55, 1.2, 0.75, 0.45, 0.9, 0.4]
def _wave():
    g = VGroup()
    for k, h in enumerate(WAVE_H):
        g.add(Rectangle(width=0.2, height=h, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([RX + 0.3 + k * 0.38, 0.35, 0]))
    return g

def _song_label():
    return _tl("a finished song", RX, 1.55, 32, DIM)


class _Stage:
    """Rebuild a beat's END state: title, headers, jobs, who tags, budget."""
    def __init__(self, scene, title, whos, jobs=None, budget=1.0):
        self.title = _title(title)
        self.headers = _headers()
        self.jobs = VGroup(*[_job(i, (jobs or JOBS)[i]) for i in range(5)])
        self.whos = VGroup(*[_who(i, w) for i, w in enumerate(whos)])
        self.btrack, self.bfill, self.blabel = _btrack(), _bfill(budget), _blabel()
        scene.add(self.title, self.headers, self.jobs, self.whos, self.btrack, self.bfill, self.blabel)

    def set_who(self, scene, i, s, run_time=0.5):
        new = _who(i, s)
        scene.play(FadeTransform(self.whos[i], new), run_time=run_time)
        self.whos.submobjects[i] = new

    def set_job(self, scene, i, s, run_time=0.6):
        new = _job(i, s)
        scene.play(FadeTransform(self.jobs[i], new), run_time=run_time)
        self.jobs.submobjects[i] = new

    def budget(self, scene, f, run_time=0.8):
        scene.play(Transform(self.bfill, _bfill(f)), run_time=run_time)


# ═══════════ B10 · HOOK — the week ═══════════
class B10_TheWeek(Scene):
    def construct(self):
        t = _title("The Week After The Song")
        heads = _headers(); track = _btrack(); bl = _blabel()
        self.add(t, heads, track, bl)                              # the structure from frame 0 (Gate V fill)
        lab = _song_label(); wave = _wave()
        self.play(FadeIn(lab), LaggedStart(*[GrowFromEdge(b, DOWN) for b in wave], lag_ratio=0.08), run_time=1.3)
        jobs = VGroup(*[_job(i) for i in range(5)]); whos = VGroup(*[_who(i, UNKNOWN) for i in range(5)])
        for i, ph in enumerate(["to finish", "title to", "release files", "a description", "pay for"]):
            _w(self, ph)
            self.play(FadeIn(jobs[i], shift=RIGHT * 0.1), FadeIn(whos[i]), run_time=0.4)
        _w(self, "scanner says")
        d = _dot(DX, RY[4])
        self.play(GrowFromCenter(d), run_time=0.4)
        _w(self, "one small budget")
        self.play(GrowFromEdge(_bfill(1.0), LEFT), run_time=0.7)
        _w(self, "which of these")
        self.play(FadeIn(_cap("which job gets the money?")), run_time=0.6)
        _finish(self)


def _b10_extras():
    return VGroup(_song_label(), _wave(), _dot(DX, RY[4]), _cap("which job gets the money?"))


# ═══════════ B11 · INSTANCE — the artist is data ═══════════
def _card():
    return Line([RX, 1.4, 0], [RX, -0.5, 0], color=INK, stroke_width=10)      # a pull-quote rule, not a filled card (Gate V ink mean)

def _card_text(name, l1, l2):
    return VGroup(_tl(name, RX + 0.35, 1.1, 40, INK, bold=True), _tl(l1, RX + 0.35, 0.4), _tl(l2, RX + 0.35, -0.25))

ADITI = ("Aditi Banksy", "post-punk · spoken word", "five languages")
MAMA = ("Mama Sparrow", "lullabies", "close-miked soprano")

class B11_ArtistAsData(Scene):
    def construct(self):
        s = _Stage(self, "The Week After The Song", [UNKNOWN] * 5)
        ex = _b10_extras(); self.add(ex)
        t = _retitle(self, s.title, "The Artist Is Data")
        self.play(FadeOut(ex), run_time=0.4)
        d = _dot(DX, RY[0])
        self.play(GrowFromCenter(d), run_time=0.5)
        _w(self, "a profile")
        card = _card(); txt = _card_text(*ADITI)
        self.play(Create(card), run_time=0.6)
        _w(self, "Banksy")
        self.play(FadeIn(txt[0]), run_time=0.4)
        _w(self, "post")
        self.play(FadeIn(txt[1]), run_time=0.4)
        _w(self, "five languages")
        self.play(FadeIn(txt[2]), run_time=0.4)
        _w(self, "Swap")
        card2 = Line([RX, 1.4, 0], [RX, -0.5, 0], color=INK, stroke_width=10)
        txt2 = _card_text(*MAMA)
        self.play(Transform(card, card2), FadeTransform(txt, txt2), run_time=1.0)
        _w(self, "You sing")
        lp = _loop()
        self.play(FadeIn(lp[0]), GrowArrow(lp[1]), run_time=0.8)
        _w(self, "you finish")
        s.set_who(self, 0, FINISH)
        self.play(FadeOut(d), run_time=0.5)
        _finish(self)


def _loop():
    """draft → hear → refine, with an arrow back: finishing a lyric is a human loop"""
    return VGroup(_tl("draft → hear → refine", RX + 0.35, -1.1),
                  Arrow([RX + 3.5, -1.65, 0], [RX + 0.35, -1.65, 0], color=INK, stroke_width=5, buff=0,
                        max_tip_length_to_length_ratio=0.08))


def _b11_extras():
    card = Line([RX, 1.4, 0], [RX, -0.5, 0], color=INK, stroke_width=10)
    return VGroup(card, _card_text(*MAMA), _loop())


# ═══════════ B12 · INSTANCE — clean the release ═══════════
CLEAN_TITLE = "A Freedom Riders Prayer"
TITLE_W = 4.15              # measured once; never read .width (Gate A stub geometry)
JUNK = [("v2", RX + 0.3), ("(FINAL)", RX + 1.2), ("2025", RX + 2.85)]

def _chip(s, x, y=0.75):
    txt = _tl(s, x, y, 32, INK)
    box = Rectangle(width=txt.width + 0.3, height=0.55, fill_color=GHOST, fill_opacity=1, stroke_width=0).move_to(txt.get_center())
    return VGroup(box, txt)

class B12_CleanTheRelease(Scene):
    def construct(self):
        s = _Stage(self, "The Artist Is Data", [FINISH] + [UNKNOWN] * 4)
        ex = _b11_extras(); self.add(ex)
        t = _retitle(self, s.title, "Clean The Release")
        self.play(FadeOut(ex), run_time=0.4)
        d = _dot(DX, RY[1])
        self.play(GrowFromCenter(d), run_time=0.3)
        _w(self, "working title")
        head = _tl(CLEAN_TITLE, RX, 1.45)
        chips = VGroup(*[_chip(j, x) for j, x in JUNK])
        self.play(FadeIn(head), LaggedStart(*[GrowFromCenter(c) for c in chips], lag_ratio=0.3), run_time=1.2)
        _w(self, "strips it")
        self.play(LaggedStart(*[ShrinkToCenter(c) for c in chips], lag_ratio=0.25), run_time=1.0)
        under = Line([RX, 1.05, 0], [RX + TITLE_W, 1.05, 0], color=INK, stroke_width=4)
        self.play(Create(under), run_time=0.5)
        _w(self, "Same with")
        rep = _tl("[Chorus 2x]", RX, 0.2, 32, DIM)
        self.play(FadeIn(rep), run_time=0.4)
        _w(self, "becomes")
        full = VGroup(_tl("the chorus, in full", RX, 0.2), _tl("the chorus, in full", RX, -0.4))
        self.play(ReplacementTransform(rep, full), run_time=0.8)
        _w(self, "These rules")
        self.play(FadeIn(_cap("constructed example · a test can prove these rules", y=-3.05)), run_time=0.5)
        _w(self, "Again")
        s.set_who(self, 1, MACHINE, 0.4)
        s.set_who(self, 2, MACHINE, 0.4)
        self.play(FadeOut(d), run_time=0.3)
        _finish(self)


def _b12_extras():
    head = _tl(CLEAN_TITLE, RX, 1.45)
    return VGroup(head, Line([RX, 1.05, 0], [RX + TITLE_W, 1.05, 0], color=INK, stroke_width=4),
                  _tl("the chorus, in full", RX, 0.2), _tl("the chorus, in full", RX, -0.4),
                  _cap("constructed example · a test can prove these rules", y=-3.05))


# ═══════════ B13 · NAIVE — do it all, faster ═══════════
PAID = "Playlist: paid"
SLIVER = 0.1

class B13_DoItAllFaster(Scene):
    def construct(self):
        s = _Stage(self, "Clean The Release", [FINISH] + [MACHINE] * 2 + [UNKNOWN] * 2)
        ex = _b12_extras(); self.add(ex)
        t = _retitle(self, s.title, "Do It All, Faster?")
        self.play(FadeOut(ex), run_time=0.4)
        _w(self, "every job")
        s.set_who(self, 3, MACHINE, 0.3)
        _w(self, "even the lyrics")
        s.set_who(self, 0, MACHINE, 0.3)
        s.set_who(self, 4, MACHINE, 0.3)
        _w(self, "it pays")
        s.set_job(self, 4, PAID)
        _w(self, "watch the budget")
        s.budget(self, SLIVER, 1.4)
        _w(self, "the money still")
        self.play(Create(_x(4.7, -1.95)), FadeIn(_cap("faster work, same bad bet")), run_time=0.6)
        _finish(self)


def _b13_extras():
    return VGroup(_x(4.7, -1.95), _cap("faster work, same bad bet"))


# ═══════════ B14 · SHIFT — two kinds of job ═══════════
DIV_Y = -1.075
def _divider():
    return VGroup()          # retired 2026-09-23: lyrics and playlist are both decisions, so no single split line

def _kind_marks():
    ex_bar = Line([1.05, 1.05, 0], [1.05, -0.95, 0], color=INK, stroke_width=6)
    ear_bar = Line([1.05, 1.8, 0], [1.05, 1.3, 0], color=INK, stroke_width=6)
    data_bar = Line([1.05, -1.2, 0], [1.05, -1.7, 0], color=INK, stroke_width=6)
    return VGroup(ex_bar, _tl("execution", RX, 0.35, 36, INK, bold=True), _tl("cheap now: the machine", RX, -0.2, 32, SOFT),
                  ear_bar, _tl("decision: your ear", RX, 1.55, 36, INK, bold=True),
                  data_bar, _tl("decision: your data", RX, -1.45, 36, INK, bold=True))

class B14_TwoKinds(Scene):
    def construct(self):
        s = _Stage(self, "Do It All, Faster?", [MACHINE] * 5, jobs=JOBS[:4] + [PAID], budget=SLIVER)
        ex = _b13_extras(); self.add(ex)
        t = _retitle(self, s.title, "Two Kinds Of Job")
        self.play(FadeOut(ex), run_time=0.4)
        s.set_job(self, 4, JOBS[4], 0.5)
        s.budget(self, 1.0, 0.8)                                  # rewind
        marks = _kind_marks()
        _w(self, "Execution")
        self.play(Create(marks[0]), FadeIn(marks[1]), run_time=0.6)
        _w(self, "cheap now")
        self.play(FadeIn(marks[2]), run_time=0.4)
        _w(self, "which lyric")
        self.play(Create(marks[3]), run_time=0.4)
        s.set_who(self, 0, FINISH, 0.5)
        _w(self, "pay for")
        self.play(Create(marks[5]), run_time=0.4)
        _w(self, "your ear")
        self.play(FadeIn(marks[4]), run_time=0.4)
        _w(self, "your data")
        self.play(FadeIn(marks[6]), run_time=0.4)
        _w(self, "sorts every")
        d = _dot(DX, RY[4])
        s.set_who(self, 4, YOU, 0.6)
        self.play(GrowFromCenter(d), run_time=0.3)
        _finish(self)


def _b14_extras():
    return VGroup(_divider(), _kind_marks(), _dot(DX, RY[4]))


# ═══════════ B15 · PREDICT — commit ═══════════
EVID = [("the scanner: clean", DIM), ("followers · about a dozen", INK), ("streams · hundreds a day", INK), ("top city · Ashburn, VA", INK)]
def _evid(k, s=None):
    txt, col = EVID[k]
    return _tl(s or txt, RX, RY[k], 32, col)

def _bullet(k):
    return _dot(RX - 0.2, RY[k], 0.06, INK)

class B15_Commit(Scene):
    def construct(self):
        s = _Stage(self, "Two Kinds Of Job", [FINISH] + [MACHINE] * 3 + [YOU])
        ex = _b14_extras(); self.add(ex)
        t = _retitle(self, s.title, "Your Own Data")
        self.play(FadeOut(ex[1]), run_time=0.4)                   # the kind marks leave; divider + dot stay
        _w(self, "The scanner says")
        e = [_evid(k) for k in range(4)]
        self.play(GrowFromCenter(_bullet(0)), FadeIn(e[0]), run_time=0.4)
        for k, ph in ((1, "about a dozen"), (2, "hundreds of"), (3, "top city")):
            _w(self, ph)
            self.play(GrowFromCenter(_bullet(k)), FadeIn(e[k], shift=LEFT * 0.1), run_time=0.4)
        self.play(FadeIn(_tl("example numbers", RX, RY[4], 32, DIM)), run_time=0.4)
        _w(self, "before it moves")
        self.play(FadeIn(_cap("commit: pay, or skip?")), Indicate(ex[2], color=TERRA, scale_factor=1.3), run_time=0.7)
        _finish(self)                                             # HOLD while the viewer commits


def _b15_extras():
    return VGroup(_divider(), _dot(DX, RY[4]), *[_evid(k) for k in range(4)],
                  _tl("example numbers", RX, RY[4], 32, DIM), VGroup(*[_bullet(k) for k in range(4)]), _cap("commit: pay, or skip?"))


# ═══════════ B16 · TRANSFORM — the gate vetoes ═══════════
SKIP = "Skip this playlist"
HUB = "Ashburn: data-center hub"

class B16_TheGateVetoes(Scene):
    def construct(self):
        s = _Stage(self, "Your Own Data", [FINISH] + [MACHINE] * 3 + [YOU])
        ex = _b15_extras(); self.add(ex)
        t = _retitle(self, s.title, "A Gate, Not A Vote")
        self.play(FadeOut(ex[-1]), run_time=0.3)                  # the commit caption leaves
        _w(self, "Ashburn is")
        city = ex[5]
        self.play(FadeTransform(city, _evid(3, HUB)), run_time=0.8)
        _w(self, "In the plan")
        gate = Line([1.0, -1.15, 0], [1.0, -1.75, 0], color=INK, stroke_width=10)
        self.play(Create(gate), run_time=0.5)
        _w(self, "vetoes")
        s.set_job(self, 4, SKIP, 0.7)
        _w(self, "whatever the scanner")
        self.play(Create(_x(4.75, RY[0])), run_time=0.5)
        _w(self, "look at the budget")
        self.play(Indicate(VGroup(s.btrack, s.bfill), color=INK, scale_factor=1.05), run_time=0.8)
        self.play(FadeIn(_cap("the budget never moved")), run_time=0.5)
        _finish(self)


def _b16_extras():
    g = VGroup(_divider(), _dot(DX, RY[4]), _evid(0), _evid(1), _evid(2), _evid(3, HUB),
               _tl("example numbers", RX, RY[4], 32, DIM), VGroup(*[_bullet(k) for k in range(4)]),
               Line([1.0, -1.15, 0], [1.0, -1.75, 0], color=INK, stroke_width=10), _x(4.75, RY[0]), _cap("the budget never moved"))
    return g


# ═══════════ B17 · ABSTRACTION — the part in the middle ═══════════
def _route(y, label):
    a = Arrow([RX, y, 0], [RX + 0.7, y, 0], color=INK, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.35)
    return VGroup(a, _tl(label, RX + 0.9, y))

class B17_TheMiddle(Scene):
    def construct(self):
        s = _Stage(self, "A Gate, Not A Vote", [FINISH] + [MACHINE] * 3 + [YOU], jobs=JOBS[:4] + [SKIP])
        ex = _b16_extras(); self.add(ex)
        t = _retitle(self, s.title, "What Musinique Is")
        self.play(FadeOut(VGroup(*ex[2:])), run_time=0.5)          # divider + dot stay
        _w(self, "the machine does")
        rule = _tl("the machine suggests · you decide", LX, -3.05, 36, INK, bold=True)
        self.play(FadeIn(rule, shift=UP * 0.1), run_time=0.6)
        _w(self, "Brand and copy")
        r1 = _route(1.2, "Madison · brand, copy")
        self.play(GrowArrow(r1[0]), FadeIn(r1[1]), run_time=0.6)
        _w(self, "Video goes")
        r2 = _route(0.3, "brutalist.art · video")
        self.play(GrowArrow(r2[0]), FadeIn(r2[1]), run_time=0.6)
        _w(self, "keeps the part")
        mid = VGroup(_tl("Musinique", RX + 0.9, -0.65, 36, INK, bold=True), _tl("make · release · fund", RX + 0.9, -1.2, 32, SOFT))
        self.play(FadeIn(mid), ex[1].animate.move_to([RX + 0.45, -0.65, 0]), run_time=0.8)
        _finish(self)


# ═══════════ B18 · PAYOFF — same week, money kept ═══════════
DONE = ["yours", "cleaned", "built", "drafted", "skipped"]

class B18_SameWeekMoneyKept(Scene):
    def construct(self):
        s = _Stage(self, "What Musinique Is", [FINISH] + [MACHINE] * 3 + [YOU], jobs=JOBS[:4] + [SKIP])
        ex = VGroup(_divider(), _dot(RX + 0.45, -0.65), _tl("the machine suggests · you decide", LX, -3.05, 36, INK, bold=True),
                    _route(1.2, "Madison · brand, copy"), _route(0.3, "brutalist.art · video"),
                    _tl("Musinique", RX + 0.9, -0.65, 36, INK, bold=True), _tl("make · release · fund", RX + 0.9, -1.2, 32, SOFT))
        self.add(ex)
        t = _retitle(self, s.title, "Same Week, Money Kept")
        lab = _song_label(); wave = _wave()
        self.play(FadeOut(ex), FadeIn(lab), LaggedStart(*[GrowFromEdge(b, DOWN) for b in wave], lag_ratio=0.05), run_time=1.0)
        _w(self, "The chores")
        for i in range(5):
            tick = _dot(DX, RY[i], 0.08, INK)
            new = _who(i, DONE[i])
            self.play(GrowFromCenter(tick), FadeTransform(s.whos[i], new), run_time=0.35)
            s.whos.submobjects[i] = new
        _w(self, "the budget is")
        self.play(Indicate(VGroup(s.btrack, s.bfill), color=INK, scale_factor=1.05), run_time=0.7)
        self.play(FadeIn(_cap("same week · money kept")), run_time=0.5)
        _w(self, "One honest")
        note = _cap("a plan today · the build is starting", y=-3.05, color=DIM)
        self.play(FadeIn(note), run_time=0.5)
        _w(self, "Not taught")
        self.play(FadeOut(note), run_time=0.3)
        self.play(FadeIn(_cap("not taught: how the audit weighs evidence", y=-3.05, color=DIM)), run_time=0.5)
        _finish(self)
