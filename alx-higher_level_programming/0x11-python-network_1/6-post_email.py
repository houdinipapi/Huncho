#!/usr/bin/python3

"""
- A Python script that:
    - takes in a URL and an email address,
    - sends a POST request to the passed URL with the email as a parameter,
    - finally displays the body of the response.
- The email must be sent in the variable email.
- Must use the packages request and sys
- Not allowed to import packages other than requests and sys
- No need to error check arguments passed to the script (number or type)
"""

if __name__ == "__main__":
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    res = post(url, {"email": email})
    print(res.text)
