#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single office joke, one line under 200 characters, to
/output/entry.txt. Nothing else goes in that file.
"""

import os

JOKE = (
    "The password policy demands 12 characters, a capital, and a symbol, "
    "so the whole office's password is just the current season "
    "with an exclamation mark."
)


def main():
    text = JOKE.strip()
    if not text:
        raise ValueError("joke must not be blank")
    if len(text) > 199:
        raise ValueError(
            f"joke is {len(text)} characters, over the 199-character limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
