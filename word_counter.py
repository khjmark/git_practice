"""Count words in text supplied on the command line."""

from __future__ import annotations

import argparse
import re


def count_words(text: str) -> int:
    """Return the number of Unicode word-like tokens in *text*."""
    return len(re.findall(r"\w+", text, flags=re.UNICODE))


def main() -> None:
    parser = argparse.ArgumentParser(description="Count words in a sentence.")
    parser.add_argument("text", help="text to analyze")
    args = parser.parse_args()
    print(count_words(args.text))


if __name__ == "__main__":
    main()
