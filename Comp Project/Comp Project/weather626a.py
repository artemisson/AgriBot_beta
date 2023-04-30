import requests
import json

# Use ipinfo.io to get the user's location based on their IP address
ip_address = requests.get('https://api.ipify.org').text
url = 'https://ipinfo.io/' + ip_address + '/json'
response = requests.get(url)
data = json.loads(response.text)

# Get the city and country from the response
city = data['city']
country = data['country']

# Use OpenWeatherMap API to get the weather forecast for the user's location
weather_api_key = '93bb70e0ffa2e77ce47f56b183e98762'
weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={weather_api_key}&units=metric'
response = requests.get(weather_url)
data = json.loads(response.text)

# Get the current temperature, weather description, and other relevant data from the response
temperature = data['main']['temp']
weather_description = data['weather'][0]['description']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']

# Print the weather forecast
print(f'The weather in {city}, {country} is {weather_description} with a temperature of {temperature}°C, humidity of {humidity}%, and wind speed of {wind_speed} m/s.')
