# Install Codex Social AI Team

## Linux and Codex cloud

Use the existing repository checkout; cloud tasks are already isolated.

```bash
cd /workspace/CodexSkills-Agent-AI-
bash scripts/setup-cloud.sh
```

The installer links all 12 skills into the repository's `.agents/skills/` and
preserves existing unrelated installations. It is safe to rerun. Start a new
Codex session in this repository to discover them. To install for another
supported skill directory, pass its path to `bash install.sh <directory>`.

The Python environment is only needed for motion export; planning and writing
skills need no Python packages. FFmpeg is supplied by `imageio-ffmpeg` for MP4
encoding. No API key or running web service is needed for these local checks.
For planning and writing only, run `bash install.sh` without the motion setup.

For motion commands in the skill documentation, use `.venv/bin/python` and the
actual helper paths under `skills/motion-creative-producer-codex/scripts/`.

See [SCHEDULER_SETUP.md](SCHEDULER_SETUP.md) for on-demand use and the external
scheduler connection requirements. Installing skills does not register a job in
Codex Scheduler or connect social publishing accounts.

## Windows

Run from the repository root:

```powershell
.\install.ps1
```

Then restart Codex.

Manual install:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item ".\skills\*" "$env:USERPROFILE\.codex\skills" -Recurse -Force
```

Then restart Codex and ask:

```text
Use social-media-manager-codex to set up a test client social media workflow.
```
