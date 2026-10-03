#!/usr/bin/env python3
"""lock_audio.py — after Kokoro (and the BOUT apad), write the measured clock into the sheet.
actual_duration_s from ffprobe on every mp3 (compile REFUSES a padded BOUT that disagrees);
durationSeconds on every Remotion card that takes it; B00/B01 cues from words.json
(faster-whisper word timestamps), set ~0.2 s before each spoken clause."""
import json, subprocess
from pathlib import Path
from cues import at
HERE = Path(__file__).resolve().parent
p = HERE / "beat_sheet.json"; d = json.loads(p.read_text())
CUES = {"B00": [at("B00", "This film", .2), at("B00", "an independent label", .2), at("B00", "The machine", .2), at("B00", "And the trap", .2)],
        "B01": [at("B01", "The scarce", .2), at("B01", "Pay for", .2), at("B01", "Skip the", .2), at("B01", "Get the", .2)]}
for b in d["beats"]:
    mp3 = HERE / "mp3" / f"beat-{b['beat_id']}.mp3"
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)]))
    b["actual_duration_s"] = round(dur, 2); b["audio_file"] = f"mp3/beat-{b['beat_id']}.mp3"
    props = b["shot"].get("remotion", {}).get("props")
    if props is not None and b["shot"]["remotion"]["pattern"] in ("ClaudeTldrWhat", "ClaudeTldrWhy", "BrutalistHesitantWriter", "ClaudeDefinitions"):
        props["durationSeconds"] = round(dur, 2)
    if b["beat_id"] in CUES: props["cues"] = [round(c, 2) for c in CUES[b["beat_id"]]]
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
print({b["beat_id"]: b["actual_duration_s"] for b in d["beats"]}, "total", round(sum(b["actual_duration_s"] for b in d["beats"]), 1))
print("cues", CUES)
