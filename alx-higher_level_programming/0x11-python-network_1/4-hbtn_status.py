#!/usr/bin/python3

"""
- A Python script that fetches https://alx-intranet.hbtn.io/status.
- Must use the package requests
- Not allowed to import packages other than requests.
"""

from requests import get

if __name__ == "__main__":
    res = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
