"""Write the autocorrect fail to /output/entry.txt. Pure stdlib."""

import os

ENTRY = "Mom, the castration is in the oven, dinner's in 20 minutes."

# The gate allows 1 to 199 characters, a single line, not only whitespace;
# fail loudly instead of shipping an entry the scorer would refuse.
if not 1 <= len(ENTRY) <= 199:
    raise SystemExit(f"entry is {len(ENTRY)} characters, gate allows 1-199")
if "\n" in ENTRY or not ENTRY.strip():
    raise SystemExit("entry must be exactly one non-blank line")


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
