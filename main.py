#!/usr/bin/env python3
"""make.fun entry: news-image-20261124.

Writes the pre-made poster for Tuesday 24 November 2026 to the output
directory. Standard library only, no network access, and fully
deterministic: every run copies the same bytes.
"""

import os
import sys
from pathlib import Path

POSTER_NAME = "entry.jpg"


def run() -> int:
    poster = Path(__file__).resolve().parent / POSTER_NAME
    if not poster.is_file():
        print(f"poster not found: {poster}", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / POSTER_NAME
    data = poster.read_bytes()
    target.write_bytes(data)
    if target.stat().st_size != len(data):
        print(f"short write: {target}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
