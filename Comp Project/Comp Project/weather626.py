import requests

# Make an API call to OpenWeatherMap to get your location and weather forecast
def get_weather_forecast():
    # Use ipinfo.io to get user's location based on their IP address
    ipinfo_response = requests.get('https://ipinfo.io/json')
    location_data = ipinfo_response.json()

    # Use OpenWeatherMap API to get weather data for user's location
    api_key = '93bb70e0ffa2e77ce47f56b183e98762' # replace with your OpenWeatherMap API key
    lat, lon = location_data['loc'].split(',')
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Extract relevant weather information
    city = weather_data["name"]
    description = weather_data['weather'][0]['description']
    temperature = round(weather_data['main']['temp'] - 273.15, 1) # Convert temperature from Kelvin to Celsius
    humidity = weather_data['main']['humidity']

    # Print the weather forecast
    print(f'Weather forecast for {city}: {description}, Temperature: {temperature}°C, Humidity: {humidity}%')

# Call the function to get the weather forecast for your location
get_weather_forecast()
