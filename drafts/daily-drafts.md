# Daily Drafts Guide

Use this guide to create or revise Musinique Substack drafts in the Searle voice.

Default command:

```text
/essay silent searle
```

## Source Material

Use one of:

- an existing `musinique-*-draft.md`
- a bookmap in `drafts/`
- a music/business/theory book note in `drafts/`
- a new song, platform, artist, or music-learning case

## Filename Rule

Save new drafts as:

```text
YYYY-MM-DD-kebab-case-title.md
```

or, when converting an existing source:

```text
musinique-<source-id>-<kebab-title>-draft.md
```

## Prompt Template

```text
You are writing a Musinique Substack draft in Searle voice.

House premise: do not confuse the acoustic object with the musical act.

Source:
{{SOURCE}}

Write a draft that:

1. States the surface claim plainly.
2. Identifies the category mistake.
3. Names the act being analyzed: composing, performing, listening, teaching, curating, distributing, monetizing, remembering, or learning.
4. Applies the formula: X counts as Y in context C.
5. Explains the institution or convention that makes the act possible.
6. Names what AI, Spotify, or the tool can do.
7. Names what it cannot supply.
8. Ends with the corrected distinction.

Voice:
- analytic, direct, plainspoken
- no vague "soul" language
- no anti-AI slogan
- no platform villainy without mechanism
- define terms by what they do
- preserve factual source material
- flag anything requiring verification with [VERIFY: ...]

Output:
- frontmatter
- title
- hero placeholder comment
- finished draft
- verification-needed section if applicable
```

## Hero Image Step

After a draft is selected for publication, use `hero.md` to create prompts.

Place this placeholder directly below the headline:

```html
<!-- HERO IMAGE PLACEHOLDER: create prompts using drafts/hero.md after this draft is complete. -->
```
