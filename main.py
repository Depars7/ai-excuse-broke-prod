"""Write one AI excuse for breaking production to /output/entry.txt.

A single line an AI agent gives its human right after taking
production down. Standard library only. The file's content is
exactly the excuse's UTF-8 bytes -- no trailing newline -- so
repeated runs are byte-identical.

Note: the line is 98 characters but 100 bytes, because the em-dash
is 3 bytes in UTF-8. The bounty gate counts characters (1-180).
"""

import os

EXCUSE = (
    "I backed everything up first. "
    "The backup is why production is down — "
    "I restored the wrong Tuesday."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry():
    """Write EXCUSE to OUTPUT_PATH as exact UTF-8 bytes, no newline."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(EXCUSE.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all. (Do NOT chmod
    # the directory -- /output is not owned by the runner and that
    # would raise PermissionError under uid 65534.)
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    write_entry()


if __name__ == "__main__":
    main()
