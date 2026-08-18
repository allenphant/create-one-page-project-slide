#!/usr/bin/env python3
"""Render a local HTML or SVG slide to a PNG and verify its dimensions."""

from __future__ import annotations

import argparse
import shutil
import struct
import subprocess
import sys
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def find_browser(explicit: str | None) -> str:
    if explicit:
        path = shutil.which(explicit) or explicit
        if Path(path).exists():
            return str(path)
        raise FileNotFoundError(f"Browser not found: {explicit}")

    for candidate in ("chromium-browser", "chromium", "google-chrome", "google-chrome-stable"):
        path = shutil.which(candidate)
        if path:
            return path
    raise FileNotFoundError("No Chromium-compatible browser found")


def read_png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        signature = handle.read(8)
        if signature != PNG_SIGNATURE:
            raise ValueError(f"Output is not a PNG: {path}")
        chunk_length = struct.unpack(">I", handle.read(4))[0]
        chunk_type = handle.read(4)
        if chunk_type != b"IHDR" or chunk_length < 8:
            raise ValueError(f"PNG is missing a valid IHDR chunk: {path}")
        width, height = struct.unpack(">II", handle.read(8))
    return width, height


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Local .html or .svg input")
    parser.add_argument("output", type=Path, help="Output .png path")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--browser", help="Browser executable name or path")
    args = parser.parse_args()

    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not source.is_file():
        parser.error(f"input file does not exist: {source}")
    if source.suffix.lower() not in {".html", ".htm", ".svg"}:
        parser.error("input must be HTML or SVG")
    if output.suffix.lower() != ".png":
        parser.error("output must use a .png extension")
    if args.width <= 0 or args.height <= 0:
        parser.error("width and height must be positive")

    output.parent.mkdir(parents=True, exist_ok=True)
    browser = find_browser(args.browser)
    command = [
        browser,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={args.width},{args.height}",
        f"--screenshot={output}",
        source.as_uri(),
    ]
    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        print(
            "Browser rendering failed. If this is a sandbox or snap confinement error, "
            "rerun with the required execution approval.",
            file=sys.stderr,
        )
        return completed.returncode

    if not output.is_file():
        print(
            f"Browser reported success but the output is not visible at {output}. "
            "Snap-packaged Chromium may isolate /tmp; choose a path inside the project "
            "workspace, such as deliverables/slide.png.",
            file=sys.stderr,
        )
        return 3

    actual = read_png_dimensions(output)
    expected = (args.width, args.height)
    if actual != expected:
        print(f"Unexpected PNG dimensions: got {actual}, expected {expected}", file=sys.stderr)
        return 2

    print(f"Rendered {source.name} -> {output} ({actual[0]}x{actual[1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
