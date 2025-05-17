#!/usr/bin/env python3
"""Morse Code Encoder"""

import sys

NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
    " ": "/ "
}


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'


def main() -> None:

    try:
        assert len(sys.argv) == 2, "Exactly one argument is required"
        arg = sys.argv[1]
        assert all(char.isalnum() or char.isspace() for char in arg), \
            "the arguments are bad"
        morse_text = ""
        for char in arg.upper():
            if char not in NESTED_MORSE:
                raise AssertionError(
                    "the argument must contain only alphanumeric char or "
                    "spaces."
                )
            morse_text += NESTED_MORSE[char]
        print(morse_text.strip())
    except AssertionError as e:
        print(Colors.RED, f"AssertionError: {e}", Colors.END)

    except AssertionError as e:
        print(Colors.RED, f"AssertionError: {e}", Colors.END)


if __name__ == "__main__":
    main()
