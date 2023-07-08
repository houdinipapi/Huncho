#!/usr/bin/python3

# Test File
# Testing the command line arguments

import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Few Comandline Arguments")
    else:
        print(sys.argv[1:])
except EOFError:
    sys.exit("TERMINATED FORCEFULLY!!")
