#!/usr/bin/env python3
"""Two Days of Quiet Dread — a one-line PR approval with quiet existential dread.

Entry for the make.fun bounty
u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.

The program writes a single code review comment to /output/entry.txt.
The sealed gate: the file must hold UTF-8 text of 1 to 140 characters,
not only whitespace, on one line. Only a valid entry goes before the
judge, who reads entries two at a time and picks the funnier one.

The comment is built from three beats so the joke lands in one breath:
the approval, the reassuring fact, and the dread. The sting sits in the
last clause — the reviewers themselves have already scrolled out of the
project's memory by the time the code stops humming.
"""

import os
import sys

MAX_CHARS = 140

APPROVAL = "Approved."
REASSURANCE = "The build is green, and this code will hum on a server"
DREAD = "long after both our names have scrolled off the git log."


def build_comment() -> str:
    """Join the three beats into one single-line review comment."""
    parts = [APPROVAL, REASSURANCE, DREAD]
    line = " ".join(part.strip() for part in parts)
    return " ".join(line.split())


def validate(line: str) -> str:
    """Enforce the gate: 1-140 characters, one line, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")
    return line


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = validate(build_comment())
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    # Read it back to prove the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        raise ValueError("written file does not match the validated line")
    print("wrote %s (%d characters)" % (out_path, len(line)))
    print("entry: %s" % line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
