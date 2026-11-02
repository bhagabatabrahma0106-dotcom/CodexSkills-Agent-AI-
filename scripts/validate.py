#!/usr/bin/env python3
"""Check skill discovery, routing, and shareable source files without API calls."""
import re
import subprocess
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        raise SystemExit("No skill definitions found")
    names = set()
    for path in skills:
        text = path.read_text()
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            raise SystemExit(f"Missing skill frontmatter: {path}")
        name = re.search(r"^name: ([a-z0-9-]+)$", parts[1], re.M)
        description = re.search(r"^description: .+", parts[1], re.M)
        if not name or not description or name[1] != path.parent.name:
            raise SystemExit(f"Invalid skill metadata: {path}")
        if name[1] in names:
            raise SystemExit(f"Duplicate skill: {name[1]}")
        names.add(name[1])
        installed = root / ".agents" / "skills" / name[1]
        if not installed.is_dir() or installed.resolve() != path.parent.resolve():
            raise SystemExit(f"Skill not installed: {name[1]}; run bash install.sh")

    manager = (root / "skills/social-media-manager-codex/SKILL.md").read_text()
    routes = set(re.findall(r"`([a-z][a-z0-9-]+)`", manager))
    missing = {name for name in routes if name.endswith(("-codex", "-openai"))} - names
    if missing:
        raise SystemExit(f"Missing specialist routes: {sorted(missing)}")

    # Inspect shareable candidates only; ignored client data and runtime files
    # must stay local. Print locations of findings, never credential values.
    files = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root,
    ).decode().split("\0")
    patterns = (
        r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}",
        r"gh[pousr]_[A-Za-z0-9]{20,}",
        r"github_pat_[A-Za-z0-9_]{20,}",
        r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
    )
    findings = []
    for name in filter(None, files):
        path = root / name
        if path == Path(__file__).resolve() or name == "scripts/privacy-check.ps1":
            continue
        if path.name == ".env" or path.name.startswith(".env."):
            findings.append(f"{name}: environment file must stay private")
        try:
            text = path.read_text()
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        for number, line in enumerate(text.splitlines(), 1):
            if any(re.search(pattern, line) for pattern in patterns):
                findings.append(f"{name}:{number}: possible credential")
    if findings:
        raise SystemExit("Review before sharing:\n" + "\n".join(findings))
    print(f"PASS: {len(names)} installed skills; specialist routes resolve; source privacy scan")


if __name__ == "__main__":
    main()
