import requests
from pprint import pprint

while True:
    start = input("\nWelcome to the Daily Forecast! To start, please type 'start' ")
    if start == "start":
        print("\npress 'q' at any time to quit")
        zip_code = input("\nPlease enter your zip code: ")
    
        if zip_code == 'q':
            break

        url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&APPID=8ba60d976d201bf3f8c60673f08ca278".format(zip_code)
        forecast = requests.get(url)
        print("\nThanks! Your forecast is:\n")
        print(f"\t{forecast}")

        again = input("\nWould you like to try again? (y/n) ")
    
        if again == 'n' or again == 'no' or again == 'q':
            break
    else:
        print("\t!!! Oops! Looks like you did not type 'start'. Please try again.")



