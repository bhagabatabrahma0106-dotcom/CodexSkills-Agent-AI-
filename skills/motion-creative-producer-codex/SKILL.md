---
name: motion-creative-producer-codex
description: Produces short looping motion social creatives in Codex. Use when creating motion graphics, stop-motion ads, animated social posts, looping MP4/GIF creatives, Reel-style frame sequences, storyboards, frame prompts, and simple video assembly from generated images.
---

# Motion Creative Producer For Codex

Create short looping motion creatives for social media. The default is a coherent frame-by-frame action loop: same scene, same layout, small action changes, played quickly so it feels like video.

## Inputs

Read if present:

- `context/brand-style.md`
- `context/content-calendar.md`
- `context/compliance-rules.md`
- `context/asset-library.md`
- `outputs/captions/`
- `outputs/creatives/`

## Output Folder

Save to:

```text
outputs/motion/[motion-slug]/
```

Create:

```text
motion-brief.md
storyboard.md
frame-prompts.md
frames/frame-001.png
frames/frame-002.png
frames/frame-003.png
loop.mp4
loop.gif
qa-checklist.md
```

## Motion Types

Choose one:

- Coherent scene loop: one scene with subtle motion such as steam, bubbles, pour, light, camera drift, hand movement, or product rotation.
- Frame-by-frame action loop: a few highly similar generated/edited frames where something changes slightly, such as sauce pouring, pizza rotating, bubbles rising, a hand entering, steam moving, garnish falling, product turning, or liquid filling a glass.
- Stop-motion product scene: the same product/scene shifts slightly between frames.
- Kinetic type: the same design animates text position, emphasis, or reveal.
- Ambient loop: steam, light, texture, grain, liquid movement, or background motion.
- Before-after: simple transition between two related states.
- Carousel-to-motion: each carousel slide becomes a timed frame. Use only when the user asks for this.
- Promo sequence: headline, benefit, CTA sequence. Use only when a sequential ad is requested.

## Default Specs

Use:

```text
Duration: 6 seconds
Frame count: 8 to 18 for action loops, 24+ for subtle single-image loops
FPS: 8 to 12 for video-like action, 2 to 4 for intentionally choppy stop-motion
Loop: final frame should visually return to first frame
Formats: MP4 for social upload, GIF for preview
Ratios: 1:1, 4:5, or 9:16
```

## Workflow

1. Confirm platform, ratio, duration, and motion type.
2. Write a motion brief.
3. Write a frame-by-frame storyboard.
4. Choose the production method:
   - Best for food/product motion: generate or edit a tightly controlled frame sequence where only one element changes.
   - Best for light polish: generate one strong base image, then create programmatic motion using pan/zoom/breathing/text movement.
   - Best for carousel motion: use ordered slide images only when requested.
5. Save frames as ordered PNGs.
6. Assemble MP4/GIF using `scripts/make_loop.py` or create a subtle single-image loop using `scripts/make_subtle_loop.py`.
7. QA loop smoothness, text, brand fit, and compliance.

## Important Default

Do not cycle through different creative concepts unless the user asks for a slideshow, carousel-to-motion, or multi-scene ad.

For most social motion ads, use a controlled action loop. Keep these fixed:

- Same scene
- Same subject
- Same layout
- Same text
- Same color grade
- Same camera angle

Move only one or two things across the sequence:

- Steam rises
- Product rotates slightly
- Liquid pours or bubbles
- Light shifts
- Camera slowly pushes in
- Background texture drifts
- Text gently scales, fades, or slides

Good example pattern:

```text
Pizza frame 1: sauce bottle enters above pizza
Pizza frame 2: first sauce stream appears
Pizza frame 3: sauce lands near center
Pizza frame 4: sauce line extends
Pizza frame 5: hand tilts bottle more
Pizza frame 6: sauce spreads slightly
Pizza frame 7: sauce stream thins
Pizza frame 8: bottle exits, pizza nearly matches frame 1 composition
```

## Frame Prompt Pattern

Use one base prompt, then change only the movement details:

```text
Base style: [brand style, scene, palette, lighting, camera]
Fixed elements: [what must stay consistent]
Frame action: [small movement for this frame]
Text: [exact text or none]
Constraints: no product hallucination, no fake logos, no unsupported claims
```

For real products, use source images and preserve product identity. Do not generate packaging from memory.

## Action Loop Prompt Pattern

For frame-by-frame generation, write one locked base prompt plus numbered frame deltas:

```text
LOCKED BASE PROMPT
Square 1:1 social video frame. [scene]. Same camera angle, same lighting, same background, same composition, same subject identity, same text placement, same color grade across all frames. Editorial food/product ad style. Do not change the plate, table, product, props, or typography.

FRAME DELTAS
Frame 001: [action starts]
Frame 002: [tiny next movement]
Frame 003: [tiny next movement]
...
Frame 012: [near-loop position]
```

Generate/edit frames so each one is intentionally similar. If the image model changes the scene too much, reduce the prompt and use the previous frame as the source image for the next edit where tooling allows.

## Frame Consistency QA

Reject or regenerate frames where:

- Camera angle changes
- Plate/object shape changes
- Text changes spelling or position
- Product/package identity changes
- Lighting jumps abruptly
- Background props appear/disappear
- The action jumps too far between adjacent frames

## Looping Rules

- Keep camera angle stable.
- Change only one or two visual elements per frame.
- Make final frame close to frame 1.
- Avoid text changing every frame unless it is a kinetic type ad.
- If using generated text, verify every word in every frame.
- The loop should feel like one video shot, not a deck of different posts.
- If generated frames look inconsistent, switch to the single-image subtle loop method.

## Assembly

Use the bundled script:

```powershell
python scripts/make_loop.py --frames outputs/motion/[slug]/frames --output outputs/motion/[slug]/loop.mp4 --fps 2 --gif
```

If `python` is not available, use the bundled Codex Python runtime if present.

MP4 export may need FFmpeg or a Python runtime with video encoding support. If MP4 export is unavailable, produce the ordered frames and a GIF preview, then note that MP4 export is pending local video tooling.

For subtle video-like motion from one image:

```powershell
python scripts/make_subtle_loop.py --input hero.png --output loop.gif --frames 24 --fps 8 --effect breathe
```

Use this only when a gentle animated post is enough. For food/product action, prefer a controlled frame sequence.

## QA Checklist

Create `qa-checklist.md`:

```text
# Motion Creative QA

- [ ] Correct ratio
- [ ] MP4 exported
- [ ] GIF preview exported if requested
- [ ] Loop returns cleanly to first frame
- [ ] Text checked word-for-word
- [ ] Brand palette and voice match
- [ ] Product/source assets preserved
- [ ] No unsupported claims
- [ ] No jarring flicker
- [ ] Caption/publishing handoff linked
```
