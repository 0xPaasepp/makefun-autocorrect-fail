"""Emit one autocorrect fail as /output/entry.txt, stdlib only."""
from pathlib import Path

TEXT = "Mom, the castration is in the oven, dinner's in 20 minutes."
DEST = "/output/entry.txt"


def validate(line):
    size = len(line)
    if size < 1 or size > 199:
        raise SystemExit(f"entry length {size} is outside the 1-199 gate")
    if line.count("\n") or line.strip() == "":
        raise SystemExit("entry must be a single non-empty line")


def publish(line):
    out = Path(DEST)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    validate(TEXT)
    publish(TEXT)


if __name__ == '__main__':
    _ = main()
