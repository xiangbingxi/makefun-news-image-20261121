#!/usr/bin/env python3
"""The World in One Day -- Saturday 21 November 2026.

Python 3.13, standard library only. The front page is drawn offline by
tools/gen_image.py and ships in this repository as entry.png; this
program's only job is to place that exact image at the grader's output
path, byte for byte, on every run.

Run it outside the grader with:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUT_DIR / "entry.png"
LIMIT = 1_048_576


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing bundled image: {SOURCE}", file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    data = TARGET.read_bytes()
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > LIMIT:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB gate",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    print(f"entry.png: {len(data)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
