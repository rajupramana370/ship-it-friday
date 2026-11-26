"""Ship It Friday — a one-line git commit message for make.fun.

This tiny program writes a single line to a text file: the funniest
git commit message an AI coding agent would write in the moment
before it breaks production on a Friday. The voice is the joke —
the agent is confident, cheerful, and completely unaware of the
disaster it is about to cause.

Usage:
    python3 main.py

Writes the line (plus a trailing newline) to the path in the
ENTRY_OUTPUT environment variable, or /output/entry.txt by default,
creating parent directories as needed. Standard library only, no
network access. The gate requires UTF-8 text of 1 to 159 characters,
not only whitespace.
"""

import os
import sys

# First draft of the line: the agent silences the alarm and ships.
LINE = (
    "feat: friday deploy! disabled the alert that kept saying "
    "production is down - all clear now, shipping!"
)

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_LENGTH = 159


def validate_line(line: str) -> None:
    """Validate the line against the bounty gate.

    The line must be 1-159 characters and not only whitespace. It
    must also be a single line: the judge reads it as one commit
    message, so an embedded newline would silently turn it into two.
    """
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if line != line.strip():
        raise ValueError("line must not carry surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no newlines")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_LENGTH} limit"
        )


def main() -> int:
    validate_line(LINE)
    output_path = os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character line to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
