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
#rate = engine.getProperty('rate')
#engine.setProperty('rate', int(rate * 0.7))

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

def casual_chat():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hi there, My name is Agribot. Your personal digital farming assistant.")
        speak("What is your name: ")
        audio = r.listen(source)
    try:
        name = r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return
    
    speak("Hello" + name + "how are you doing today?")
    

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
    speak("Hello there. Please make sure you are connected to the internet for optimum functionality.")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("I am Agribot, your very own personal digital farmer assistant")
        elif 'hello' in query:
            casual_chat()
        elif 'what is the weather' in query:
            Weather()     
        elif 'open manual schedule' in query:
            webbrowser.open("https://calendar.google.com")
            speak("Be patient as the webpage loads for a moment. To manually update your schedule on this calendar, check the date you want to scehdule, then hover the mouse to the start time of the event. Click the box indicating the start time and drag it till the stop time of your event. Then edit the title of the note accordingly and the calendar will be updated with your new event!")
        elif 'repeat please' in query:
            speak("To manually update your schedule on Google calendar, simply check the date you want to scehdule. Then hover the mouse to the start time of the event you'd like to schedule. Click on the box indicating the start time and drag it till you reach the stop time of your event. Finally upon stopping the drag, a window will pop up where you can edit the title accordingly about the scheduled event and the calendar will be updated with your new event!")       
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'shutdown' in query:
            exit(0)
            