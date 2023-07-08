#!/usr/bin/python3

import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Few Comandline Arguments")
    else:
        print(sys.argv[1:])
except EOFError:
    sys.exit("TERMINATED FORCEFULLY!!")
