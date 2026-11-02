---
name: brand-onboarding-codex
description: Builds the brand foundation for a Codex social media workflow. Use when onboarding a new client, summarizing a brand from websites/social profiles/assets, creating brand voice and visual rules, or producing context/brand-style.md for downstream content and creative skills.
---

# Brand Onboarding For Codex

Create `context/brand-style.md`, the source of truth for all team skills.

## Inputs

Gather:

- Brand name, website, and handles
- Products or services
- Audience
- Goals
- Competitors
- Tone of voice
- Visual style
- Colors, fonts, logo rules
- Do and do-not rules
- Compliance constraints

If URLs are provided and browsing is available, collect evidence from the website and public social profiles. If browsing is not available, ask for pasted examples or screenshots.

## Optional Research Tools

Use available tools conservatively:

- Firecrawl: extract clean website copy, service pages, product pages, blogs, and competitor pages.
- Playwright MCP: inspect live pages, screenshots, visual brand cues, forms, and navigation.
- Browser/search tools: gather public profile context when allowed.

If none are configured, ask the user for pasted website copy, screenshots, example posts, or brand documents. Do not block onboarding just because research tooling is missing.

## Output

Create `context/brand-style.md`:

```text
# Brand Style

## Brand Snapshot
Name:
Website:
Handles:
Offer:
Audience:
Primary goals:

## Voice
Tone:
Words to use:
Words to avoid:
Point of view:
CTA style:

## Visual Identity
Palette:
Typography:
Photography style:
Layout style:
Texture/props:
Do:
Do not:

## Content Pillars
1.
2.
3.
4.

## Platform Notes
Instagram:
LinkedIn:
Facebook:
TikTok:
Threads:
X:

## Compliance And Risk
Claims to avoid:
Disclaimers:
Approval requirements:

## Examples
Good examples:
Bad examples:
```

Also create `context/compliance-rules.md` and `context/asset-library.md` if enough information is available.
