#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
bash install.sh
if [[ ! -x .venv/bin/python ]]; then
    python3 -m venv .venv
fi
.venv/bin/python -m pip install --disable-pip-version-check -r requirements-motion.txt
.venv/bin/python -m pip check
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/smoke_motion.py
