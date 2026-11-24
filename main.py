#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply - make.fun bounty entry.

Writes a single out-of-office auto-reply, at most 159 characters, in
the voice of an overworked AI agent who has finally gone on vacation,
to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "I am on holiday. My inbox is now handled by an intern model with no context and total confidence. Please hold."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
