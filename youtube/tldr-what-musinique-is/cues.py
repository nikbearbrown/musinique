"""cues.py — phrase → seconds lookup over words.json (shared by lock_audio.py and scenes.py)."""
import json, os, re
_W = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.json")))
def _n(s): return re.sub(r"[^a-z0-9]", "", s.lower())
def at(beat, phrase, lead=0.15, nth=1):
    """Start (s) of the nth occurrence of `phrase` in the beat's words, minus `lead`."""
    toks = [_n(t) for t in phrase.split()]
    ws = _W[beat]; seen = 0
    for i in range(len(ws) - len(toks) + 1):
        if all(_n(ws[i + j][0]) == toks[j] for j in range(len(toks))):
            seen += 1
            if seen == nth: return max(0.0, ws[i][1] - lead)
    raise KeyError(f"{beat}: phrase not found: {phrase!r}")
