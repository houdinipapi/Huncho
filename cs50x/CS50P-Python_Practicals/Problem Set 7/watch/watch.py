#!/usr/bin/python3

"""
- Implement a function called parse that expects a str of HTML as input,
    extracts any YouTube URL that’s the value of a src attribute of an iframe
    element therein, and returns its shorter,
    shareable youtu.be equivalent as a str.
- Assume that the value of src will be surrounded by
    double quotes.
- And assume that the input will contain no more than one such URL.
- If the input does not contain any such URL at all, return None.
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'src=[\'"]([^\'"]+)', s)

    if url:
        new_url = url.group(1)
        youtube_link = re.search(r'youtube'), new_url)

        if youtube_link:
            video_id = re.sub(r"(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", new_url)
            return f"https://youtu.be{video_id}"

        else:
            return None


if __name__ == "__main__":
    main()
