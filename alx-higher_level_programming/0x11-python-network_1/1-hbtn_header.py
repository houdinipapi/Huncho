#!/usr/bin/python3

"""
- A Python script that:
    - takes in a URL
    - sends a request to the URL
    - displays the value of the X-Request-Id variable found in the header of the response
- Must use the packages urllib and sys
- Not allowed to import packages other than urllib and sys
- The value of this variable is different for each request.
- No need to check arguments passed to the script (number or type).
- Must use `with` statement.
"""

from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
