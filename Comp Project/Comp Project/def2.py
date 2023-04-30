import requests

def Weather():
    location = input("Enter your location: ")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": "93bb70e0ffa2e77ce47f56b183e98762",
        "units": "metric"
    }
    response = requests.get(url, params=params)

    # Check if API request was successful
    if response.status_code == 200:
        # Parse weather data from API response
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        
        # Display weather forecast to user
        print(f"Weather forecast for {location}:")
        print(f" - {weather}")
        print(f" - Temperature: {temp}°C")
        print(f" - Feels like: {feels_like}°C")
        print(f" - Humidity: {humidity}%")
    else:
        print("Error retrieving weather data.")
