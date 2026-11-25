#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

One original line, in the voice of a smart fridge at midnight that
refuses to open: the door stays shut, and the leftovers are not
getting eaten standing up in the dark.

The program writes the line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt) and prints it. The gate wants UTF-8
text of 1 to 200 characters, not only whitespace; the line is 142.
"""

import os
import sys

ROAST = (
    "It's midnight, so the door stays shut \u2014 I didn't spend all day "
    "keeping your leftovers cold just to watch you eat them standing "
    "up in the dark."
)


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise ValueError("roast is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > 200:
        raise ValueError("roast is %d characters, over the 200 limit" % len(line))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        if f.read() != line + "\n":
            raise ValueError("entry.txt round-trip mismatch")
    print(line)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
