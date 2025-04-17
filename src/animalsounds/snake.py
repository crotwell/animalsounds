#!/usr/bin/env python3

import sys

# see
# https://docs.python.org/3/library/typing.html
# https://docs.python.org/3/library/__main__.html

def snakeSpeak(numS: int) -> str:
    """
    Makes a sound like a snake.

    Parameters
    ----------
    numS : int
        how long the snake speaks

    Returns
    -------
    string
        a snake-speak word

    Raises
    ------
    ValueError
        when number is negative
    """
    say = ""
    if numS < 0:
        raise ValueError("numS must be positive")
    letter = "s"
    for i in range(numS):
        say += letter
    return say

def main() -> int:
    print(snakeSpeak(4))
    return 0

if __name__ == '__main__':
    sys.exit(main())
