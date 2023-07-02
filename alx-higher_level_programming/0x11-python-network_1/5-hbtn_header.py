#!/usr/bin/python3

"""
- A Python script that:
    - takes in a URL,
    - sends a request to the URL
    - displays the value of the variable X-Request-Id in the response header.
- Must use the packages requests and sys
- Not allowed to import other packages than requests and sys
- The value of this variable is different for each request.
- No need to check script arguments (number and type)
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    print(get(argv[1]).headers.get("X-Request-Id"))
