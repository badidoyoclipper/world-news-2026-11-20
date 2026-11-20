#!/usr/bin/env python3
"""Ship the front page of Friday 20 November 2026 to the runner.

This repository holds a finished picture — entry.png, a one-page
newspaper covering the world news of Friday 20 November 2026 — and
this small program is its delivery mechanism. It reads the picture
from beside itself, sanity-checks that the bytes really are the PNG
they claim to be, and writes them, unchanged, to the output path the
make.fun harness asks for. Standard library only; no network; the
same input always produces the same output file.

Output path resolution:
  * $MAKEFUN_OUTPUT_DIR/entry.png when the variable is set,
  * /output/entry.png when that directory exists and is writable,
  * ./output/entry.png as the local fallback.
"""

import os
import struct
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SIGNATURE = b"\x89PNG\r\n\x1a\n"


def picture_bytes() -> bytes:
    return (HERE / "entry.png").read_bytes()


def check_png(data: bytes) -> tuple[int, int]:
    """Return (width, height) if data is a PNG, else raise ValueError."""
    if data[:8] != SIGNATURE:
        raise ValueError("entry.png does not start with the PNG signature")
    if data[12:16] != b"IHDR":
        raise ValueError("entry.png is missing its IHDR chunk")
    return struct.unpack(">II", data[16:24])


def pick_output() -> Path:
    env_dir = os.getenv("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir, "entry.png")
    shared = Path("/output")
    try:
        if shared.is_dir() and os.access(shared, os.W_OK):
            return shared / "entry.png"
    except OSError:
        pass
    return Path("output", "entry.png")


def run() -> int:
    data = picture_bytes()
    width, height = check_png(data)
    if width > 1024 or height > 1024:
        raise SystemExit(f"entry.png is {width}x{height}; the limit is 1024x1024")
    dest = pick_output()
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Write to a sibling temp file and rename it over the destination, so
    # a reader never catches entry.png half-written.
    fd, tmp_name = tempfile.mkstemp(dir=dest.parent, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.replace(tmp_name, dest)
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    print(f"wrote {dest} — {len(data)} bytes, {width}x{height}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
