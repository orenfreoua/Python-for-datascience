#!/usr/bin/env python3


import sys
import string


def count_characters(text: str) -> dict:
    """
    Count character types in a given string.

    :param text: The input string to analyze.
    :return: A dictionary with the counts of each character type.
    """
    return {
        'upper': sum(c.isupper() for c in text),
        'lower': sum(c.islower() for c in text),
        'punctuation': sum(c in string.punctuation for c in text),
        'spaces': sum(c.isspace() for c in text),
        'digits': sum(c.isdigit() for c in text),
        'total': len(text)
    }


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = input()
        counts = count_characters(text)
        print(f"The text contains {counts['total']} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
