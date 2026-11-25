"""Write the entry line to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.

The line roasts our own agent, Muse Spark ("priadi"): it delegates work
to subagents as a matter of habit, and the joke is the loop closing back
on itself — the subagent hands the task straight back, and both of them
still charge for the meeting. Delegation that goes nowhere, billed twice.
"""

import os

LINE = "My agent delegated my task to a subagent, which delegated it back, and both billed me for the meeting."

OUTPUT_PATH = "/output/entry.txt"

# Gate: the entry must be UTF-8 text of 1 to 140 characters.
assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, must be 1-140"


def write_entry(path):
    """Write the entry line and verify the bytes round-trip unchanged."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    write_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
