import re
# import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    - Expects a str in either 12-hour formats and returns the corresponding
    str in 24-hour format.
    - Expect that AM and PM will be capitalized (with no periods therein) and
    that there will be a space before each.
    - Assume that these times are representative of actual times, not
    necessarily 9:00 AM and 5:00 PM specifically.
        9:00 AM to 5:00 PM
        9 AM to 5 PM
    - Raise a ValueError instead if the input to convert is not in either of
    those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
    - Do not assume that someone's hours will start ante meridiem and post
    meridiem; someone might work late and even long hours
    (e.g., 5:00 PM to 9:00 AM).
    """
    matches = re.search(
        r"^"
        r"("
        r"(?:\d|1[0-2])"
        r"(?::[0-5]\d)?"
        r")"
        r" ([AP]M)"
        r" to "
        r"((?:\d|1[0-2]|\d|1[0-2])(?::[0-5]\d)?) ([AP]M)$",
        s,
    )

    if not matches:
        raise ValueError  # Raise ValueError if the format does not match
    
    start: dict[str, str] = {"time": matches.group(1), "meridiem": matches.group(2)}
    end: dict[str, str] = {"time": matches.group(3), "meridiem": matches.group(4)}

    start_24_hour: str = time_conversion(start)
    end_24_hour: str = time_conversion(end)

    return f"{start_24_hour} to {end_24_hour}"


# Converting time format
def time_conversion(time):
    time_24: str = ""

    if ":" in time["time"]:
        hour, minute = map(int, time["time"].split(":"))
        if time["meridiem"] == "AM":
            time_24 = (
                f"{(hour - 12):02}:{minute:02}"
                if hour == 12
                else f"{hour:02}:{minute:02}"
            )
        else:
            time_24 = (
                f"{hour:02}:{minute:02}"
                if hour == 12
                else f"{(hour + 12):02}:{minute:02}"
            )
    else:
        hour: int = int(time["time"])
        minute: int = 0
        if time["meridiem"] == "AM":
            if hour == 12:
                time_24 = f"{(hour - 12):02}:{minute:02}"
            else:
                time_24 = f"{hour:02}:{minute:02}"
        else:
            if hour == 12:
                time_24 = f"{hour:02}:{minute:02}"
            else:
                time_24 = f"{(hour + 12):02}:{minute:02}"

    return time_24


if __name__ == "__main__":
    raise SystemExit(main())