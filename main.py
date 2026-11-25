"""Copy the bundled one-line entry to the grader output directory.

Reads entry.txt next to this script and writes it byte-identical to
$MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644. Standard library only,
no temporary files, no network.
"""

import os
import sys


def main():
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not data.strip():
        print("entry.txt is empty", file=sys.stderr)
        return 1
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except (OSError, KeyError) as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
