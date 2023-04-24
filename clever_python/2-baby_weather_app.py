# This is a baby weather app


def baby_weather():
    weather = int(input("Pick a number between 1 to 4: "))
    sun = "It is SUNNY!\nWear your sunglasses!"
    rain = "It is RAINY!\nCarry an umbrella!"
    fail = "ERROR"

    if weather == 1:
        return sun
    elif weather == 2:
        return rain
    else:
        return fail

print(baby_weather())
