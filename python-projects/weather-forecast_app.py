'''
Building a weather forecast app will give you valuable experience in working with APIs. You will use Python and the OpenWeatherMap API to fetch weather data for a given location and display it to the user. This project will involve making HTTP requests, parsing JSON responses, and presenting the data in a user-friendly way.
'''

import requests 
import json

def get_weather_data(api_key, city):
    # Get weather data for a specififc city using the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    # Display weather information
    if data["cod"] != "404":
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}'C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}'%")
        print(f"Wind speed: {wind_speed} km/h")
    else:
        print("City not found. Please try again.")
        
def main():
    # API key from OpenWeatherMap
    api_key = "#####################"
    
    # Get the city name from the user
    city = input("Enter the city name: ")
    
    # Get weather data for the city
    weather_data = get_weather_data(api_key, city)
    
    # Display weather information
    display_weather(weather_data)
    
if __name__ == "__main__":
    main()