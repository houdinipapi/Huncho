#!/usr/bin/python3

"""
- A Python script that:
    - takes in a URL,
    - sends a request to the URL,
    - displays the body of the response.
- If the HTTP status code is greater tahn or equal to 400, print: Error code followed by the value of the HTTP status code.
- Must use the packages requests and sys
- Not allowed to import packages other than requests and sys
- No need to check arguments passed to the script (number or type)
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    req = get(argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
