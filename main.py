"""make.fun entry for news-image-20261124.

Writes the pre-made poster for Tuesday 24 November 2026 to the output
directory. The poster is the file ``entry.jpg`` sitting next to this
script; it is copied byte-for-byte to the path given on the command line.

Usage: python3 main.py <output-path>
"""

import shutil
import sys
from pathlib import Path

POSTER_NAME = "entry.jpg"


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python3 main.py <output-path>", file=sys.stderr)
        sys.exit(1)

    poster = Path(__file__).resolve().parent / POSTER_NAME
    if not poster.is_file():
        print(f"error: poster file not found: {poster}", file=sys.stderr)
        sys.exit(1)

    output = Path(sys.argv[1])
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(poster, output)
    print(f"wrote {output} ({output.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
