#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single office joke, one line under 200 characters, to
/output/entry.txt. Nothing else goes in that file.
"""

import os

JOKE = (
    "I hit reply-all to tell everyone to stop replying-all, "
    "and HR replied-all asking me to stop replying-all, "
    "so now Legal is replying-all about it too."
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
