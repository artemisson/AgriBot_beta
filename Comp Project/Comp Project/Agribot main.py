import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests

# init pyttsx"""  """
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

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

if __name__ == '__main__':

    speak("AgriBot activated ")
    speak("Hello there")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("I am Agribot, your very own personal farmer assistant")
        elif 'hello' in query:
            speak("Hi how are you doing? I hope you are fine. What is your name?")
        elif 'my name is' in query:
            speak("Its nice to meet you, I am Agri-Bot how can I assist you?")
        elif 'what is the weather' in query:
            Weather()     
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)
            