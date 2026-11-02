#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
skills_target="${1:-$repo_root/.agents/skills}"

python3 - "$repo_root" "$skills_target" <<'PY'
import os
import sys
from pathlib import Path

source = Path(sys.argv[1]) / "skills"
target = Path(sys.argv[2]).expanduser().resolve()
skills = sorted(p.parent for p in source.glob("*/SKILL.md"))
if not skills:
    raise SystemExit(f"No skills found in {source}")
target.mkdir(parents=True, exist_ok=True)

# Check every destination before making changes; preserve unrelated installations.
for skill in skills:
    destination = target / skill.name
    if destination.is_symlink() and destination.resolve() == skill.resolve():
        continue
    if destination.exists() or destination.is_symlink():
        raise SystemExit(f"Refusing to overwrite an existing skill: {destination}")

for skill in skills:
    destination = target / skill.name
    if not destination.is_symlink():
        destination.symlink_to(os.path.relpath(skill, target), target_is_directory=True)
print(f"Installed {len(skills)} skills in {target}")
print("Start a new Codex session in this repository to discover the skills.")
PY
