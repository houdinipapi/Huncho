#!/usr/bin/python3

"""
- A Python script that takes 2 arguments in order to:
    - list 10 commits (from the most recent to oldest)
    - of the repository "rails" by the user "rails"
- The first argument will be the repository name.
- The second argument will be the owner name.
- Must use the packages requests and sys
- Not allowed to import packages other than requests and sys
- No need to check arguments passed to the script (number or type)
"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    res = get(url)
    commits = res.json()

    try:
        for i in range(10):
            print(
                "{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
