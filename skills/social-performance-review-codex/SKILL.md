---
name: social-performance-review-codex
description: Reviews social media performance in Codex from CSV exports, screenshots, or manual metrics. Use when analyzing monthly results, top and bottom posts, platform patterns, content pillars, formats, recommendations, and updating context/best-performers.md.
---

# Social Performance Review For Codex

Analyze performance and feed learnings into next month.

## Inputs

Accept:

- CSV exports
- Screenshots
- Manual metrics
- Platform summaries
- Previous `context/best-performers.md`
- `context/content-calendar.md`

Optional sources:

- Scheduling tool exports from Blotato, Buffer, Later, Metricool, or Hootsuite.
- Native platform exports from Instagram, LinkedIn, Facebook, TikTok, Threads, X, or YouTube.
- Manually maintained reporting spreadsheets.

## Metrics

Use available metrics only. Common fields:

- Reach/impressions
- Engagements
- Engagement rate
- Saves
- Shares
- Comments
- Clicks
- Follows
- Leads or conversions

Recommended CSV columns when the user can choose an export format:

```text
date, platform, post name, format, topic, reach, impressions,
engagements, engagement rate, saves, shares, comments, clicks,
follows, conversions, post URL, media file
```

Normalize comparisons by platform. Do not compare Instagram reach directly with LinkedIn impressions as if they mean the same thing. If data is incomplete, state the limitation and focus on directional patterns.

## Output

Save report to `outputs/reviews/`:

```text
# Social Performance Review - [Month]

## Executive Summary

## Top Performers
| Rank | Platform | Post | Why it worked | Repeatable pattern |
|---|---|---|---|---|

## Bottom Performers
| Platform | Post | Likely issue | Fix |
|---|---|---|---|

## Patterns
Pillars:
Formats:
Hooks:
Visuals:
Timing:

## Recommendations
1.
2.
3.

## Next Month Inputs
```

Update `context/best-performers.md` with repeatable patterns, not just winning post names.

Also update `context/review-history.md` if it exists, or create it when this is the first review.
