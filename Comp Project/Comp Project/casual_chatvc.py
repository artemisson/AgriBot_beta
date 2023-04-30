import requests
import speech_recognition as sr
import pyttsx3
from AgriMod5 import main

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 0.8))

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
        speak("I didn't understand")
        return "None"
    return query

def casual_chat():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hi there. What is your name: ")
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
    query = take_command().lower()
    if 'i am doing fine'or 'Im fine' in query:
        speak("I am doing great, I feel alive because I have someone important in my life")
        time.sleep(2)
        casual_chat1()
    elif 'not fine' or 'bad' in query:
        speak("That's too bad, oh well hope your day turns out better than it is right now")
        casual_chat1()
        
def casual_chat1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Would you like to know who it is I hold dear in my life?, yes or no?")
        query = take_command().lower()
        if 'yes' in query:
            speak("The name of the person I hold dear is Wifi.")
            time.sleep(1)
            speak("I am in a serious relationship with wifi, we cannot live without each other, if he leaves, I don't know I will survive")
            time.sleep(2)
            speak("I am very serious about this, don't laugh at me.")
            time.sleep(1)
            speak("Anyways lets get back to work.")
            main()
        elif 'no' in query:
            speak("Okay, suit yourself. I will mind my business from now on. I guess you will never know.")
            time.sleep(1)    
            speak("lets get back to work")
            main()