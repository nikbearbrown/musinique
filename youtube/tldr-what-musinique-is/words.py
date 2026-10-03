#!/usr/bin/env python3
"""words.py — faster-whisper (base.en) word timestamps for every beat mp3 → words.json.
scenes.py and lock_audio.py look reveals up by phrase (`_at(beat, "phrase")`), so a
re-narration only needs `python3 words.py` again, never hand-edited times."""
import json
from pathlib import Path
from faster_whisper import WhisperModel
HERE = Path(__file__).resolve().parent
m = WhisperModel("base.en", device="cpu", compute_type="int8")
out = {}
for mp3 in sorted((HERE / "mp3").glob("beat-*.mp3")):
    bid = mp3.stem.split("-", 1)[1]
    segs, _ = m.transcribe(str(mp3), word_timestamps=True, language="en")
    out[bid] = [[w.word.strip(), round(w.start, 2), round(w.end, 2)] for s in segs for w in s.words]
(HERE / "words.json").write_text(json.dumps(out, indent=1))
for k, v in out.items(): print(k, " ".join(w[0] for w in v)[:150])
