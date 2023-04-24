# This is a baby weather app


def baby_weather():
    weather = int(input("Pick a number between 1 to 4: "))
    sun = "It is SUNNY!\nWear your sunglasses!"

    if weather == 1:
        return sun

print(baby_weather())
