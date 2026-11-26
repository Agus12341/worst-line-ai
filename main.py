#!/usr/bin/env python3
"""Write the worst pickup line an AI could say to entry.txt."""

import os

# One pickup line, and a bad one, in a machine's voice: picked from
# five drafts judged pairwise on the kit's criteria (a pickup line
# an AI would say first, and a bad one, then the biggest laugh or
# the best groan, badness that is itself the joke rather than
# crudeness or randomness, flat over-helpful faintly ominous
# machine phrasing, and the joke arriving by the last word). The
# winner grades the reader like a form field: required, and the
# machine cannot proceed without you. Note this kit's gate is
# tighter than most: entry.txt must be UTF-8 text of 1 to 140
# characters. This line is 81 code points, 82 with its trailing
# newline (verified by a local run, byte for byte against the
# winning draft).
TEXT = "On a scale of one to ten, you are a required field: I cannot proceed without you."

# Gate guard: this scorer only takes 1 to 140 characters, tighter
# than the usual window, so refuse to write anything outside it.
MAX_CHARS = 140
assert 1 <= len(TEXT) <= MAX_CHARS, "entry line outside the gate"


def write_entry(out_dir: str) -> None:
    """Write the line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
