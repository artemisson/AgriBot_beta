import requests
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 0.8))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def Weather():
    # Use speech recognition to get the location from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your location: ")
        audio = r.listen(source)
    try:
        location = r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return

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
        
        # Use text-to-speech to output the weather forecast
        engine.say(f"Weather forecast for {location}:")
        engine.say(f" - {weather}")
        engine.say(f" - Temperature: {temp} degrees Celsius")
        engine.say(f" - Feels like: {feels_like} degrees Celsius")
        engine.say(f" - Humidity: {humidity} percent")
        engine.runAndWait()
    else:
        engine.say("Error retrieving weather data.")
        engine.runAndWait()
