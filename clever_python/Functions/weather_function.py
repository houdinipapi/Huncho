#!/usr/bin/python3


def weather_forecast(weather: str) -> None:
    weather = input("What is the weather today?")

    if weather == "sunny":
        print("Wear sunglasses!")

    elif weather == "rainy":
        print("Carry an umbrella!")

    elif weather == "cloudy":
        print("Wear warm clothes!")

    elif weather == "thunderstorms":
        print("Stay at home!")

    else:
        print("Insert correct weather!")


weather_forecast("weather")
