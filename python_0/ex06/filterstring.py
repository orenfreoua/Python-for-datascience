#!/usr/bin/env python3
"""
This script filters words in a string based on their length.
It uses a custom implementation of the built-in filter function (ft_filter).
"""

import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main function that handles user input, validation, filtering,
    and displays the result.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        string, min_len_str = sys.argv[1], sys.argv[2]

        assert min_len_str.isdigit(), "the arguments are bad"
        min_len = int(min_len_str)

        words = string.split()

        filtered_words = ft_filter(lambda word: len(word) > min_len, words)
        print(filtered_words)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
