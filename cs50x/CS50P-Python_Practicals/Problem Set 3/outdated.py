"""
 - Implement a program that prompts the user for a date, anno Domini,
 in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
 wherein the month in the latter might be any of the values in the list
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

valid_formats = ["M/D/YYYY", "MMMM D, YYYY"]

date_parts = []

while True:
    user_input = input("Date: ")
    try:
        if '/' in user_input:
            date_parts = user_input.split('/')
            month, date, year = map(int, date_parts)
            if 0 < month <= 12:
                if 0 < date <= 31:
                    print(f"{year:04d}-{month:02d}-{date:02d}")
                else:
                    continue
            else:
                continue
        elif ',' in user_input:
            date_parts = user_input.title().replace(',', ' ').split()
            month, date, year = date_parts
            date = int(date)
            year = int(year)

            if 0 < date <= 31:
                if date_parts[0] in months:
                    month = months.index(date_parts[0]) + 1
                    print(f"{year:04d}-{month:02d}-{date:02d}")
                else:
                    continue
            else:
                continue
        else:
            continue

    except ValueError:
        pass
    else:
        break

# print(type(month))
# print(type(date))
# print(type(year))
