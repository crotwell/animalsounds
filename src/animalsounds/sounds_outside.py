#!/usr/bin/env python3

from .snake import snakeSpeak
from .bee import beeSounds
from . import __version__

import argparse

def makeSounds(hiss=3, swarm=2, verbose=False):
    if verbose:
        print("getting ready to make sounds...")
        print(f"the snake value is {hiss}")
        print(f"the bee swarm is {swarm}")
        print()
    print("outside sounds like...")
    print(beeSounds(swarm))
    print(snakeSpeak(hiss))

def createArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--hiss", type=int,
                        default=4,
                        help="how long does the snake hiss")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    parser.add_argument("--version", action="store_true",
                        help="print version")
    args = parser.parse_args()
    return args

def main() -> int:
    args = createArgs()
    if args.version:
        print(__version__)
    else:
        makeSounds(args.hiss, verbose=args.verbose)
    return 0

if __name__ == '__main__':
    sys.exit(main())
