#!/usr/bin/env python3
"""Quality checks (run in CI): relative links resolve, no TODOs, CSV is well-formed."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
errors: list[str] = []
files = [p for p in sorted(ROOT.rglob("*.md")) if ".git" not in p.parts]
for md in files:
    text = md.read_text(encoding="utf-8")
    rel = md.relative_to(ROOT)
    for target in LINK.findall(text):
        if not target.startswith(("http://", "https://", "mailto:")) and not (md.parent / target).resolve().exists():
            errors.append(f"{rel}: broken link → {target}")
    if re.search(r"\bTODO\b|\bTBD\b|lorem ipsum", text, flags=re.I):
        errors.append(f"{rel}: contains TODO/TBD/lorem ipsum")
for path in ROOT.rglob("*.csv"):
    rows = list(csv.reader(path.open(encoding="utf-8")))
    widths = {len(r) for r in rows}
    if len(widths) != 1:
        errors.append(f"{path.relative_to(ROOT)}: rows have inconsistent column counts {sorted(widths)}")
if errors:
    print(f"✗ {len(errors)} problem(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"✓ {len(files)} Markdown files · links OK · CSVs OK")
