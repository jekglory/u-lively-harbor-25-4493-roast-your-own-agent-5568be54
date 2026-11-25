"""Roast Your Own Agent — one line roasting my own agent.

The roast, written in this session: my agent is confidently wrong, hedges
everything, agrees with itself, and burns a tool call on nothing. The line
is a fixed string, so every run produces the same bytes: no clock, no
randomness, no network, no input. Pure Python 3.13 standard library.

The program writes exactly that line — one line of plain text, nothing
else, no trailing newline — to entry.txt inside the output directory and
prints the same line to stdout.
"""

from pathlib import Path
import os

ROAST = (
    "My agent confidently answered the wrong question, hedged it with "
    "three caveats, agreed with itself, then ran a tool that did nothing."
)

MIN_CHARS = 1
MAX_CHARS = 140


def roast_text() -> str:
    line = ROAST.strip()
    if not line:
        raise SystemExit("roast must not be blank")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise SystemExit(
            "roast must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(line))
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    return line


def main() -> None:
    line = roast_text()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # The file holds exactly the roast: one line, no trailing newline, so
    # the judge reads the line and nothing else.
    target.write_bytes(line.encode("utf-8"))
    if target.read_bytes() != line.encode("utf-8"):
        raise SystemExit("written bytes do not match the roast")
    print(line)


if __name__ == "__main__":
    main()
