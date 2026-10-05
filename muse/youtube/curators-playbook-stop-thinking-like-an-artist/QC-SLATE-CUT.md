# Film 05 "The Curator's Playbook: Stop Thinking Like an Artist" — slate-cut QC spot check

**Date:** 2026-10-05 ~02:30 UTC (2026-10-04 ~22:30 EDT)
**File:** `film-05-curators-playbook--slate-cut.mp4`
**Result:** PASS (spot check, 5 frames across the full runtime + 1 visual inspection)

## Container / streams (ffprobe)

- Duration: 281.15s (~4m41s); beat-sheet audio sum 281.02s — matches within
  mux rounding (audio-first master clock holds)
- Video: h264 1920×1080 — Audio: aac
- Size: 6,247,960 bytes (6.2 MB)

## Frame inspection

Sampled at t=5, 60, 120, 200, 270s; frame t=120 (B06) visually inspected:

- No edge-bleed: all text well inside frame edges. (A naive pixel scan flags
  the by-design footer at y=985 and the rust top bar; visual inspection
  confirms neither is clipped or bleeding — same layout as Films 01–04.)
- Consistent branding: rust top bar, "@Musinique — The Curator's Playbook"
  footer, beat label top-left
- Headlines and deks legible, good title-safe margins

## Audio

- Real speech verified: beat-BIDEA peaks −1.26 dB, RMS −19.8 dB
  (healthy narration levels, not silence)

## Open items

- Drive upload still needs Bear's one-tap approval card (uploads to the shared
  Drive folder are pre-authorized per standing rule — the tap is a
  confirmation, not new auth).
