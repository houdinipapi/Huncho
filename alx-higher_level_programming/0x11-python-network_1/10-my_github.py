#!/usr/bin/python3

"""
- A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
- Must use Basic Authentication with a personal access token
    as password to access to your information (only read:user permission is needed).
- The first argument will be your username.
- The second argument will be your password(in this case, a personal access token as password)
- Must use the packages requests and sys
- Not allowed to import packages other than requests and sys.
- No need to check arguments passed to the script (number or type).
"""

from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
