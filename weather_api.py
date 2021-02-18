#Import necessary tools 
from class_weather import WeatherInformation
import requests


while True:
    print("\nPress 'q' at any time to quit")
    start = input("\n\033[4mWelcome to the Daily Forecast! To start, please type 'start'\033[0m ")
    if start == "start":
        #Instantiate class
        w = WeatherInformation()
        w.get_weather()

        #Ask the user if they would like to try again. 
        again = input("\nWould you like to check the weather of another city? (y/n) ".lower())
        if again == 'n' or again == 'no' or again == 'q':
            break

    elif start == 'q':
        break
    else:
        print("\nOops, try again, 'start' is case sensitive!")
