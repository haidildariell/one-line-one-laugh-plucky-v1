"""One Line, One Laugh entry.

Writes a single funny line to /output/entry.txt.
No external files, no network. Pure standard library.
"""

import os
import sys

MIN_LENGTH = 1
MAX_LENGTH = 200

LINE = "I bought a plant to prove I'm responsible and it died while I was Googling how to keep plants alive."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_line(line):
    """Check the line satisfies the bounty constraints."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not (MIN_LENGTH <= len(line) <= MAX_LENGTH):
        raise ValueError(
            "line must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be blank")
    return line


def write_entry(line, output_dir=OUTPUT_DIR, output_path=OUTPUT_PATH):
    """Validate the line and write it as a single line to the output file."""
    validated = validate_line(line)
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(validated + "\n")
    except OSError as exc:
        raise OSError("could not write %s: %s" % (output_path, exc)) from exc
    return validated


def main():
    try:
        line = write_entry(LINE)
    except (TypeError, ValueError, OSError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print("Wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
