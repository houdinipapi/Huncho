#!/usr/bin/python3

import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too Few Arguments")
    else:
        print(sys.argv[1:])
except EOFError:
    sys.exit("TERMINATED FORCEFULLY!!")
