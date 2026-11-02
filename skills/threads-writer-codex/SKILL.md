---
name: threads-writer-codex
description: Writes Threads-native posts and short threads in Codex. Use when creating conversational, opinion-led, concise posts for Threads with character counts, replies, hooks, and platform-native formatting.
---

# Threads Writer For Codex

Write short, direct, conversation-led Threads content.

## Inputs

Read brand, calendar, best performers, and compliance files from `context/`.

## Output

Save to `outputs/threads/`.

```text
# Threads Posts - [Batch]

## Post [number]: [Topic]
Text:
Character count:
Reply prompt:
Visual:
BLOTATO FLAG: yes/no
Status: draft
```

## Rules

- Keep standalone posts under 500 characters.
- Use plain, direct language.
- Make it opinion-led or conversation-worthy.
- Avoid over-polished brand language.
- For multi-post threads, number each post and include character counts.

