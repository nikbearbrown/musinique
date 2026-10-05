# Film 01 "AI as Punk Rock" — slate-cut QC spot check

**Date:** 2026-10-04 ~20:00 UTC (16:00 EDT)
**File:** `film-01-ai-as-punk-rock--slate-cut.mp4`
**Result:** PASS (spot check, 8 frames across the full runtime)

## Container / streams (ffprobe)

- Duration: 278.96s (~4m39s), matches build-state.json `total_s: 279.0`
- Video: h264 — Audio: aac, duration matches video (no drift)
- Size: 5,381,410 bytes (5.4 MB)

## Frame inspection

Sampled at t=3, 30, 60, 100, 150, 200, 250, 272s; visually inspected
t=3 (BIDEA), t=60 (B02), t=150 (B07), t=272 (BOUT):

- No edge-bleed: all text well inside frame edges (the test-reel QC
  blockers do not recur here)
- Consistent branding: rust-red top bar, "@Musinique — AI as Punk Rock"
  footer, beat label in top-left
- Headlines and sub-headlines legible, good title-safe margins

## Open items

- Drive upload still needs Bear's one-tap approval card
  (build-state.json notes this; uploads to the shared Drive folder are
  pre-authorized per standing rule — the tap is a confirmation, not new auth).
