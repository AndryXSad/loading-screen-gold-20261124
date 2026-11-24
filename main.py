"""Loading Screen Gold entry (program/v1).

Writes a single loading-screen tip -- one line, at most 200 characters --
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The tip is written from scratch for this bounty: a line for stressed
developers and AI coding agents, meant to land mid-build.
"""

import os

TIP = (
    "Tip: you are the only one in this loop with a heartbeat. "
    "The tests are red, the agent is confident, "
    "and the error message is the only honest one here."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TIP)
    print(TIP)


if __name__ == "__main__":
    main()
