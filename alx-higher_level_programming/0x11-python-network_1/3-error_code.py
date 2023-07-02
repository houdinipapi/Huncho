#!/usr/bin/python3

"""
- A Python script that:
    - takes in a URL,
    - sends a request to the URL,
    - displays the body of the response (decoded in utf-8)
- Manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
- Must use the packages urllib and sys.
- Not allowed to import other packages than urllib and sys.
- No need to check arguments passed to the script (number or type)
- Must use the with statement.
"""

from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as err:
        print(f"Error code: {err.code}")
