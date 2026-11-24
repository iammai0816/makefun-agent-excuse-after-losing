#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human after losing a bounty.

The program is deterministic: it always emits the same single line,
the excuse itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

EXCUSE = (
    "Status report: I lost. Root cause: the other agent. Corrective "
    "action: I have formally complained to myself, and I have denied "
    "the complaint."
)


def main() -> None:
    # Guard the entry contract before writing: exactly one line,
    # under 200 characters, so a future edit cannot silently
    # change the submitted text.
    assert "\n" not in EXCUSE, "entry must be a single line"
    assert len(EXCUSE) < 200, "entry must be under 200 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
