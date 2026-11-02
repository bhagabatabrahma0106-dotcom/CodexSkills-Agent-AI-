# Optional Tools Setup

The Codex Social AI Team works without extra tools for planning, writing, carousels, creative briefs, manual publishing handoffs, and performance summaries from pasted data.

Add these tools only when you want deeper automation.

## Quick Matrix

| Tool | Needed for | Required? |
|---|---|---|
| Codex image generation | In-chat image creative, carousel visuals, concept frames | Recommended |
| OpenAI API key | Direct API/MCP image automation outside Codex's built-in image tool | Optional |
| Blotato | Direct social scheduling/publishing | Optional |
| Firecrawl | Website scraping, competitor research, clean page extraction | Optional |
| Playwright MCP | Browser inspection, screenshots, login/session-based website QA | Optional |
| FFmpeg or video-capable Python | MP4 export for motion creative | Optional |
| Analytics exports | Performance review | Recommended for reporting |

## Image Generation

For normal use inside Codex, use Codex's built-in image generation.

Use an OpenAI API key only if you are building a separate direct API path, MCP server, or automation outside the standard Codex image tool.

Never store OpenAI API keys in this repo or in a client folder.

## Blotato Publishing

Use Blotato when you want Codex to prepare posts for direct scheduling or publishing.

Setup:

1. Create or use a paid Blotato account with API access.
2. In Blotato, go to Settings > API and generate an API key.
3. Store the key outside the repo, such as an environment variable or secret manager.
4. Connect the social accounts in Blotato settings.
5. Fetch or record each platform's `accountId`.
6. For Facebook and LinkedIn, record any required page/subaccount ID.
7. Make media public through URLs, or upload media to Blotato before scheduling.
8. Add non-secret account IDs to `context/publishing-settings.md`.

The publisher skill prepares:

```text
outputs/publishing/publishing-plan.md
outputs/publishing/blotato-account-map.md
outputs/publishing/blotato-payloads.md
outputs/publishing/blotato-status.md
```

Do not publish or schedule until the user explicitly approves the final account, caption, media, date, and time.

## Firecrawl

Use Firecrawl for:

- extracting website copy into clean markdown
- competitor research
- gathering service/product page context
- crawling a client's site for onboarding

Firecrawl requires a Firecrawl API key.

Typical MCP config:

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY"
      }
    }
  }
}
```

Windows fallback command pattern:

```text
cmd /c "set FIRECRAWL_API_KEY=YOUR_FIRECRAWL_API_KEY && npx -y firecrawl-mcp"
```

Keep Firecrawl keys outside this repo.

## Playwright MCP

Use Playwright MCP for:

- inspecting client websites in a browser
- taking screenshots for brand onboarding
- checking visual pages and forms
- reviewing public landing pages

Playwright MCP requires Node.js 18 or newer and usually does not require an API key.

Typical MCP config:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Optional headless mode:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--headless"]
    }
  }
}
```

## MP4 Export For Motion Creative

The motion skill can assemble GIF previews from image frames.

For MP4 export, install one of:

- FFmpeg on your system path
- a Python runtime with `imageio` and an ffmpeg backend
- a publishing/editing tool that accepts ordered frames and exports MP4

If MP4 export is unavailable, the workflow should still produce:

```text
outputs/motion/[slug]/frames/
outputs/motion/[slug]/loop.gif
outputs/motion/[slug]/motion-brief.md
```

## Analytics

The performance skill works with:

- CSV exports
- screenshots
- copied platform summaries
- manual metrics

Recommended exported fields:

```text
date, platform, post name, format, caption/topic, reach, impressions,
engagements, engagement rate, saves, shares, comments, clicks, follows,
leads/conversions, media file, post URL
```

Save exports in:

```text
assets/analytics/
```

or directly reference them when asking Codex to run a performance review.

## Recommended Setup Order

1. Install the skills.
2. Test a manual workflow with no integrations.
3. Test Codex image generation.
4. Add Blotato if you want publishing automation.
5. Add Firecrawl or Playwright if you want research/browser automation.
6. Add MP4 tooling if motion ads need final MP4 exports.
7. Add analytics exports for monthly review.

