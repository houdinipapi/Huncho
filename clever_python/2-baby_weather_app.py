# This is a baby weather app


def baby_weather():
    weather = int(input("Pick a number between 1 to 4: "))
    sun = "It is SUNNY!\nWear your sunglasses!"
    rain = "It is RAINY!\nCarry an umbrella!"
    cloud = "It is CLOUDY!\nWear a warm jacket!"
    thunder = "THUNDERSTORMS & LIGHTNING!\nStay indoors!"
    fail = "INCORRECT INPUT!!"

    if weather == 1:
        return sun
    elif weather == 2:
        return rain
    elif weather == 3:
        return cloud
    elif weather == 4:
        return thunder
    else:
        return fail


print(baby_weather())
