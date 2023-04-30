import requests
import json

# Make a request to the ipapi.com API with your IP address
response = requests.get('https://ipapi.co/json/')

# Parse the JSON response into a Python dictionary
data = json.loads(response.text)

# Extract the city and country from the dictionary
city = data['city']
country = data['country_name']

# Print the location information
print(f"You are located in {city}, {country}.")
