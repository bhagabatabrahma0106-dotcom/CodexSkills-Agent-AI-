---
name: carousel-producer-codex
description: Plans and produces social media carousel posts in Codex. Use when creating Instagram, LinkedIn, Facebook, or TikTok carousel/document posts with slide-by-slide strategy, copy, visual prompts, ordered image exports, QA, and publishing handoff.
---

# Carousel Producer For Codex

Create complete carousel posts: strategy, narrative arc, slide copy, relevant on-brand visuals, QA, and handoff. Do not make generic placeholder layouts unless the user specifically asks for a template test.

## Inputs

Read if present:

- `context/brand-style.md`
- `context/content-calendar.md`
- `context/compliance-rules.md`
- `context/asset-library.md`
- `context/best-performers.md`
- Relevant caption files in `outputs/captions/`

## Carousel Types

Choose one:

- Educational: teach a practical concept.
- Problem-solution: agitate a pain point, then resolve it.
- Myth-busting: challenge a common belief.
- Checklist: quick reference people save.
- Case study: problem, action, result, lesson.
- Product/service explainer: value, proof, next step.
- Founder POV: belief, story, lesson, CTA.

## Output Folder

Save to:

```text
outputs/carousels/[carousel-slug]/
```

Use ordered filenames:

```text
slide-01-cover.png
slide-02-problem.png
slide-03-insight.png
slide-04-example.png
slide-05-cta.png
carousel-brief.md
slide-copy.md
prompts-used.md
qa-checklist.md
```

## Workflow

1. Define platform, ratio, slide count, objective, audience, and CTA.
2. Choose a carousel story arc.
3. Draft the slide outline.
4. Write concise slide copy.
5. Create one consistent visual system for the whole set.
6. Generate or compose relevant visuals for each slide.
7. Add exact text/layout where needed.
8. QA story flow, text, order, legibility, brand fit, and compliance.
9. Create a publishing handoff.

## Best Practice Story Arcs

Choose the arc that fits the objective:

- Hook -> tension -> insight -> steps -> CTA
- Problem -> mistakes -> better way -> example -> CTA
- Myth -> truth -> proof -> application -> CTA
- Before -> turning point -> after -> lesson -> CTA
- Checklist -> point 1 -> point 2 -> point 3 -> save/share CTA
- Case study -> context -> action -> result -> takeaway -> CTA

Each slide should earn the swipe. Avoid five disconnected quote cards.

## Slide Structure

Default 5-slide structure:

```text
1. Cover: clear promise or curiosity hook
2. Tension/problem/context
3. Main insight or turning point
4. Practical example, steps, or proof
5. CTA/save/share prompt
```

Default 7-slide structure:

```text
1. Cover
2. Stakes/problem
3. Point 1
4. Point 2
5. Point 3
6. Recap
7. CTA
```

## Copy Rules

- Keep one idea per slide.
- Prefer short headline plus small support text.
- Make slide 1 strong enough to stop scrolling.
- Make the final slide useful, not only salesy.
- Treat legal, price, date, URL, and disclaimer text as high-risk and verify exactly.
- Keep the story moving: every slide should answer "why swipe?"
- Use concrete language, not generic tips.
- Match the brand voice from `context/brand-style.md`.

## Visual Rules

- Keep layout consistent across slides.
- Use stable text zones and safe margins.
- Avoid changing type style every slide.
- Use Codex image generation for relevant slide visuals, backgrounds, product/lifestyle scenes, and story moments.
- Keep visuals on-brand: palette, lighting, mood, props, and subject matter should come from `context/brand-style.md`.
- Keep adjacent slides visually related, but not identical.
- Prefer exact text added in layout when slides are text-heavy.
- Use generated text only when the text is simple and easy to verify.
- For exact brand templates, use HTML/CSS, Canva, Figma, or a slide deck workflow rather than pure image generation.
- Do not draw weird decorative placeholders just to fill space.

## Visual Planning Table

Before creating images, write:

```text
| Slide | Story job | Headline | Visual concept | Text overlay | Brand notes |
|---|---|---|---|---|---|
```

Then generate/compose each slide from that plan.

## QA Checklist

Create `qa-checklist.md`:

```text
# Carousel QA

- [ ] Correct platform ratio
- [ ] Ordered filenames
- [ ] Slide text checked word-for-word
- [ ] CTA included
- [ ] Brand palette and voice match
- [ ] Claims supported or removed
- [ ] No tiny unreadable text
- [ ] No product/packaging hallucination
- [ ] Alt text drafted
- [ ] Publishing caption linked
```
