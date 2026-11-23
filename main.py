#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to /output/entry.txt, exactly as
the competition's gate requires: UTF-8 text, 1 to 199 characters, a single
line, nothing else in the file.
"""

from pathlib import Path

JOKE = (
    "They replaced the water cooler with a chatbot, so now office gossip "
    "takes three business days and ends with 'Is there anything else I "
    "can help you with?'"
)


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse:
    # one line, 1 to 199 characters, not only white space.
    if not 1 <= len(JOKE) <= 199 or "\n" in JOKE or not JOKE.strip():
        raise ValueError(f"joke fails the gate at {len(JOKE)} characters")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
