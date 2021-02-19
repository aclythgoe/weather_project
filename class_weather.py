#Import Requests for weather API and JSON 
import requests
import json


#Make class named 'WeatherInformation'
class WeatherInformation:
    # Def __init__ and get inputs
    def __init__(self):
        #Initialize Zip_code and give the inputs
        self.zip_code = input("\nPlease enter your zip code (U.S. Only): ")
        self.city = input("Please enter your city: ")
    
    # Def get_weather to setup the API
    def get_weather(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&APPID=8ba60d976d201bf3f8c60673f08ca278'.format(self.zip_code)
        forecast = requests.get(url)

         #Connection Test
        if forecast.status_code == 200:
            print("\nConnection Succesful!")
        else: 
            print("!!! Error: Please check your Zip Code. !!!")
        

        #Get JSON ready to grab specific key and value's from JSON data
        X = forecast.json()
        Y = X['main']
        
        #Define calls for each data set
        temp = Y['temp']
        high = Y['temp_max']
        low = Y['temp_min']
        humidity = Y['humidity']

        #Print output to user, displaying all information.
        print(f"\nThanks! Your forecast today in {self.city.title()}, brought to you by Andrew:")
        print(f"\tTemperature: {temp}°F")
        print(f"\tToday's High: {high}°F")
        print(f"\tToday's low: {low}°F")
        print(f"\tHumidity: {humidity}%")


