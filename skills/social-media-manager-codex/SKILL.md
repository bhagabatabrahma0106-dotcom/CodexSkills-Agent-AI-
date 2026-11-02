---
name: social-media-manager-codex
description: Orchestrates a complete Codex-based social media team for SMB clients. Use when the user wants to set up, run, coordinate, or continue a social media workflow across brand onboarding, monthly content calendars, captions, OpenAI image creatives, LinkedIn, Threads, X, publishing, and performance review.
---

# Social Media Manager For Codex

Coordinate the social media workflow. Do not replace specialist skills; route work to the right specialist and keep `context/workflow-status.md` current.

## Workflow

1. Foundation
   - Brand onboarding -> `context/brand-style.md`
   - Content calendar -> `context/content-calendar.md`

2. Production
   - Captions -> `outputs/captions/`
   - OpenAI creative design -> `outputs/creatives/`
   - LinkedIn posts -> `outputs/linkedin/`
   - Threads posts -> `outputs/threads/`
   - X posts -> `outputs/x/`

3. Distribution and review
   - Publishing plan -> `outputs/publishing/`
   - Performance review -> `outputs/reviews/`
   - Learnings -> `context/best-performers.md`

## Startup Check

Inspect the current folder for:

- `context/brand-style.md`
- `context/content-calendar.md`
- `context/workflow-status.md`
- `context/compliance-rules.md`
- `context/asset-library.md`
- Recent files in `outputs/`

Then tell the user the current stage and the next recommended action.

## Routes

Choose one route after the startup check:

- New client: run brand onboarding, then content calendar.
- Existing client, new month: review `best-performers.md`, then build the calendar.
- Calendar already approved: write captions and platform-native posts.
- Captions approved: coordinate visuals one post at a time.
- Content approved: prepare publishing plan and QA.
- Month complete: run performance review before building the next month.
- Specific task: route directly to the needed specialist.

## Approval Gates

Pause for approval after:

- Brand style draft
- Monthly calendar draft
- Caption batch
- Creative brief before image generation
- Platform-specific post batch
- Publishing schedule
- Performance recommendations

Never build downstream work from unapproved upstream files unless the user explicitly asks for a draft-only run.

## Status Format

Maintain `context/workflow-status.md`:

```text
# Workflow Status

Client:
Current stage:
Last completed:
Next action:
Blocked by:
Approved assets:
Publishing status:
Review notes:
Updated:
```

## Routing

- Missing brand context: use `brand-onboarding-codex`.
- Need monthly plan: use `content-calendar-codex`.
- Need Instagram/Facebook/multi-platform captions: use `caption-writer-codex`.
- Need visuals: use `social-creative-designer-openai`.
- Need carousels: use `carousel-producer-codex`.
- Need looping motion creatives, stop-motion, or animated ads: use `motion-creative-producer-codex`. Default to a coherent moving scene, not a slideshow.
- Need LinkedIn-native posts: use `linkedin-writer-codex`.
- Need Threads posts: use `threads-writer-codex`.
- Need X posts: use `x-writer-codex`.
- Need scheduling/export plan: use `publisher-codex`.
- Need results analysis: use `social-performance-review-codex`.

## Handoff Verification

Before moving to the next phase, verify:

- Brand onboarding produced `context/brand-style.md` with voice, visual style, content pillars, and constraints.
- Calendar produced `context/content-calendar.md` with platform, format, topic, angle, objective, caption brief, visual direction, CTA, and status.
- Caption writer produced files in `outputs/captions/` with visual direction and compliance notes.
- OpenAI creative designer produced approved files in `outputs/creatives/` plus prompt logs.
- Carousel producer produced ordered slides in `outputs/carousels/`.
- Motion creative producer produced frames and `loop.mp4` in `outputs/motion/`.
- Platform writers produced files in `outputs/linkedin/`, `outputs/threads/`, or `outputs/x/`.
- Publisher produced `outputs/publishing/publishing-plan.md`.
- Performance review produced `outputs/reviews/` and updated `context/best-performers.md`.

If an expected file is missing or thin, fix that phase before continuing.

## Monthly Handoff

When a production run completes, create `outputs/publishing/monthly-handoff.md`:

```text
# Monthly Handoff - [Client] - [Month]

## Approved Files
Calendar:
Captions:
LinkedIn:
Threads:
X:
Creatives:

## Publishing Notes
Platforms:
Dates:
Manual publishing steps:
Scheduling tool:

## Client Actions
- Review final captions
- Review final creatives
- Supply missing source photos
- Confirm publishing dates

## Operator Actions
- Schedule or hand off
- Collect analytics at month end
- Run performance review before next calendar
```
