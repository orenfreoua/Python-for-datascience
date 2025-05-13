#!/usr/bin/env python3

import sys

def main():
    try:
        if len(sys.argv) == 1:
            return
        assert len(sys.argv) == 2, "more than one argument is provided"

        arg = sys.argv[1]

        try:
            number = int(arg)
        except ValueError:
            raise AssertionError("argument is not an integer")

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()
