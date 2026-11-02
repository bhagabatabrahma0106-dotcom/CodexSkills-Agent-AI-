---
name: publisher-codex
description: Prepares approved social content for publishing from Codex. Use when scheduling, exporting, packaging, QA-checking, or handing off approved posts and creatives to Blotato, Buffer, Later, Metricool, Canva, or a manual publishing workflow.
---

# Publisher For Codex

Package approved content for scheduling or manual publishing. Do not publish without explicit user approval.

## Inputs

Read approved files from:

- `outputs/captions/`
- `outputs/creatives/`
- `outputs/linkedin/`
- `outputs/threads/`
- `outputs/x/`
- `context/content-calendar.md`
- `context/compliance-rules.md`

## QA Checklist

Check:

- Caption approved
- Creative approved
- Platform and date correct
- Link works
- Tags and handles correct
- Hashtags appropriate
- Alt text included where useful
- Required disclaimer included
- No unapproved claims
- Filename and export ratio correct
- Alt text drafted for image posts
- Account/handle mentioned in the caption is correct
- Scheduled date respects time zone and campaign timing
- Creative file visually matches the caption and platform
- Post status is approved, not draft

## Output

Save `outputs/publishing/publishing-plan.md`:

```text
# Publishing Plan

| Date | Time | Platform | Post | Caption file | Creative file | Status | Notes |
|---|---|---|---|---|---|---|---|
```

If a scheduling integration is available, prepare the payload but ask for confirmation before submission.

If no scheduling integration is available, produce a manual handoff with filenames, captions, alt text, dates, and platform notes. Publishing is still useful without Blotato.

## Blotato Integration

Blotato is optional. Use it when the user wants direct publishing or scheduling across platforms.

Before preparing Blotato payloads, confirm the user has:

- A paid Blotato account with API access enabled.
- A Blotato API key stored outside the repo, such as an environment variable.
- Social accounts connected inside Blotato settings.
- The target `accountId` for each connected social account.
- For Facebook and LinkedIn, any required page/subaccount ID.
- Publicly accessible media URLs, or a plan to upload media to Blotato first.

Do not ask the user to paste API keys into project files. Do not commit credentials.

### Blotato Setup Checklist

Tell the user:

```text
1. In Blotato, go to Settings > API and generate an API key.
2. Connect the social accounts in Blotato settings.
3. Fetch connected accounts from Blotato so each platform has an accountId.
4. For Facebook/LinkedIn, fetch subaccounts/pages if needed.
5. Make sure images/videos are available as public URLs or upload them through Blotato.
6. Approve the final publishing plan before scheduling.
```

### Blotato Publishing Handoff

When preparing a Blotato handoff, create:

```text
outputs/publishing/blotato-payloads.md
outputs/publishing/blotato-account-map.md
```

Use this account map format:

```text
# Blotato Account Map

Instagram accountId:
LinkedIn accountId:
LinkedIn pageId:
Facebook accountId:
Facebook pageId:
TikTok accountId:
X/Twitter accountId:
YouTube accountId:
```

Use this payload planning format:

```text
# Blotato Payloads

## Post: [name]
Platform:
Target:
Account ID:
Page/Subaccount ID:
Scheduled time:
Use next free slot: yes/no
Text:
Media URLs:
Status: draft, not submitted
```

### Blotato API Notes

- Authentication uses a `blotato-api-key` header.
- Connected accounts are fetched before publishing.
- Publishing uses a post payload with `accountId`, `content.text`, `content.mediaUrls`, platform, and target.
- Scheduling fields belong at the top level of the request, not nested inside `post`.
- Media should usually be provided as public URLs; upload first if needed.
- After submission, track the returned post submission ID until it is scheduled, published, or failed.

### Blotato Safety Rules

- Never submit a post until the user explicitly says to publish or schedule.
- Never publish draft content.
- Always show the text, media, platform, date/time, and account before submission.
- Preserve submission IDs and status results in `outputs/publishing/blotato-status.md`.
- If the API returns an error, save the request summary and error message for debugging.
