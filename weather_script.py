# Fetch weather data from OpenWeatherMap API and display weather information like temp, humidity, and weather condition.
import requests
import json
import os
from dotenv import load_dotenv
# Load environment variables from .env file
def load_env():
    load_dotenv()

load_env()
# Get API key and city from environment variables
API_KEY = os.getenv('WEATHER_API_KEY')
CITY = 'Dublin'
# Define the base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# Function to fetch weather data
def get_weather_data(city, api_key):
    # Construct the complete API URL
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    # Send a GET request to the API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print("Error fetching weather data")
        return None
# Function to display weather information
def display_weather(data):
    if data:
        # Extract relevant information from the JSON response
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']
        # Print the weather information
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_condition}")
    else:
        print("No data to display")
# Main function to run the script
def main():
    # Fetch weather data
    weather_data = get_weather_data(CITY, API_KEY)
    # Display weather information
    display_weather(weather_data)
# Run the main function
if __name__ == "__main__":
    main()
