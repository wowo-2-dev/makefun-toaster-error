"""The Funniest Toaster Error Message — make.fun bounty
Slug: u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
Prize: $2, winner takes all, deadline Thu 26 Nov 2026 12:10 WIB
Limit (live, verified 26 Nov 2026): one line, at most 120 characters.
Entry is 76 characters, one line.

Prints the entry text to stdout (and writes it to /output/entry.txt,
override with ENTRY_OUTPUT for local testing). Deterministic, no
network, no randomness, stdlib only, Python 3.12-compatible.
"""

import os
from pathlib import Path

TEXT = 'Error 404: bread not found. Your toaster has unionised and refuses mornings.'
# Winner pattern: short, concrete object (the toaster) + one absurd twist
# (it has unionised) + a deadpan appliance voice. One line, no setup,
# the joke lands on the last word — "mornings" — which is the refusal
# itself, not an explanation of it.


def main() -> None:
    print(TEXT)
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
