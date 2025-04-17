#!/usr/bin/env python3

import sys

def beeSounds(swarmSize: int) -> str:
    say = ""
    buzz = "buzz"
    for i in range(swarmSize):
        say += " "+buzz
    return say.strip()

def main() -> int:
    print(beeSounds(3))
    return 0

if __name__ == '__main__':
    sys.exit(main())
