#!/usr/bin/env python3
"""build_srt.py — full-text caption track for this reel (<slug>.srt).
Beat windows: taken from an existing one-cue-per-beat <slug>.srt (stage_publish.py's
emitter, already on the compiled clock) when present; otherwise laid end to end from each
beat's measured actual_duration_s (the compile clock: audio-first, one beat after another —
checked against the master's ffprobe duration by --check). Each beat's FULL narration_text is
split into <= ~84-char cues, proportional by word count. Re-run AFTER stage_publish.py
(it overwrites the .srt with truncated cues), BEFORE ./art post.
"""
import json, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
slug = HERE.name
srt_path = HERE / f"{slug}.srt"
sheet = json.load(open(HERE / "beat_sheet.json"))
beats = [b for b in sheet["beats"] if b.get("narration_text")]
TS = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})")
def t2s(g): h, mi, s, ms = map(int, g); return h*3600 + mi*60 + s + ms/1000
def s2t(x):
    ms = int(round(x*1000)); h, ms = divmod(ms, 3600000); mi, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{mi:02d}:{s:02d},{ms:03d}"
windows = None
if srt_path.exists():
    blocks = [b for b in srt_path.read_text().strip().split("\n\n") if b.strip()]
    if len(blocks) == len(beats):
        windows = [tuple(t2s(m) for m in TS.findall(b.split("\n")[1])[:2]) for b in blocks]
if windows is None:
    windows, t = [], 0.0
    for b in beats:
        d = float(b["actual_duration_s"]); windows.append((t, t + d)); t += d
MAX = 84
out, n = [], 0
for (t0, t1), beat in zip(windows, beats):
    words = beat["narration_text"].replace("Namasté", "Namaste").split(); chunks, cur = [], []   # caption spelling; narration keeps the accent for Kokoro
    for w in words:
        if cur and len(" ".join(cur + [w])) > MAX and (cur[-1][-1] in ".,;:?!" or len(" ".join(cur)) > MAX * 0.7):
            chunks.append(" ".join(cur)); cur = [w]
        else:
            cur.append(w)
    if cur: chunks.append(" ".join(cur))
    total = sum(len(c.split()) for c in chunks); t = t0
    for c in chunks:
        d = (t1 - t0) * len(c.split()) / total; n += 1
        out.append(f"{n}\n{s2t(t)} --> {s2t(min(t + d, t1) - 0.02)}\n{c}\n"); t += d
srt_path.write_text("\n".join(out))
print(f"[srt] {n} cues → {srt_path.name}; end {windows[-1][1]:.2f}s")
if "--check" in sys.argv:
    m = sorted((HERE / "exports" / "landscape").glob("*.mp4"))
    if m:
        dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(m[0])]))
        print(f"[srt] master {dur:.2f}s vs captions {windows[-1][1]:.2f}s (drift {dur - windows[-1][1]:+.2f}s)")
