#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""weatherer.py to get weather data using OpenWeatherMap API.

* Extracts weather information at the given latitude and longitude.
* API returns the current UTC date-time in unix.
"""

from datetime import datetime
import requests
import subprocess as sub
import sys


# Read API key from file
api_file = open(r"./api.key", "r")
API_KEY = api_file.read(32)
api_file.close()

LAT = 22.25  # Position latitude
LON = 84.88  # Position longitude
URL_BASE = "https://api.openweathermap.org/data/2.5/"


def show_options():
    now = "Get current weather"
    later = "Get weather forecast"


def get_current_weather():
    current_weather()
    print("current weather fetched")


def get_weather_forecast():
    print("under construction")


def current_weather():
    """Get current weather data from OpenWeatherMap."""
    response = requests.get(f"{URL_BASE}weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        current_data = response.json()
        update_time = datetime.fromtimestamp(current_data["dt"]).time()
        weather = current_data["weather"][0]["description"]
        temperature = current_data["main"]["temp"]
        feels_like = current_data["main"]["feels_like"]
        humidity = current_data["main"]["humidity"]
        wind_speed = current_data["wind"]["speed"]
        rain = current_data["rain"]["1h"]
        cloud = current_data["clouds"]["all"]
        sunrise = datetime.fromtimestamp(current_data["sys"]["sunrise"]).time()
        sunset = datetime.fromtimestamp(current_data["sys"]["sunset"]).time()
        print(f"Successful API call made at {update_time}")
    else:
        print("ERROR, received code", response.status_code)
        raise SystemExit(1)


def main():
    args_count = len(sys.argv)
    if args_count == 1:
        show_options()
    elif args_count == 2:
        if sys.argv[1] == "now":
            get_current_weather()
        elif sys.argv[1] == "forecast":
            get_weather_forecast()
        else:
            print("Invalid argument received. Try again.")
    elif args_count > 2:
        print("Too many arguments received. Try again.")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
