from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import speech_recognition as sr
import datetime
import datefinder
import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
import psutil

# Initialize text-to-speech engine
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

summary1 = None
def start_time():
    r = sr.Recognizer()
    # use the microphone as source
    global start_time_t
    with sr.Microphone() as source:
        speak("What is the start time of your event? an example would be like the 25th of May 9pm")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition API
    try:
        start_time_str = r.recognize_google(audio)
        start_time_t = start_time_str
        print("Start Time: " + start_time_str)
        title()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
def title():
    # use the microphone as source
    global start_time_t, summary
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what is the title of your event?")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition API
    try:
        summary = r.recognize_google(audio)
        summary1 = summary
        print("Summary: " + summary)
        parameters()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def parameters():
    global start_time_t, summary1
    matches = list(datefinder.find_dates(start_time_t))
    start_time_m = matches[0]
    summary2 = summary1
    create_event(start_time_m, summary2)
    cal_update()

def cal_update():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Your event has been successfully updated on Google Calendar. Would you like to see it on the calendar?")
        query = take_command().lower()
        if 'yes' in query:
            webbrowser.open("https://calendar.google.com/calendar/u/0/r/week")
            speak("As you can see when check the day of your scheduled event against the time you scheduled it you can see its highlighted for a duration of two hours since the start time.")
            # Find the Chrome process
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'chrome.exe':
                    print(f"Found Chrome process with PID {proc.info['pid']}. Terminating...")
                    proc.kill()
            speak("Is there anything else you would like me to do?")
        else:
            speak("Is there anything else you would like me to do for you?")
             
def create_event(start_time_m, summary2,description=None, location=None):
    service = get_calendar_service()
    # Format the start time as AM/PM and print it
    start_time = start_time_m.strftime("%I:%M %p")
    end_time = start_time_m + timedelta(hours=2)
    event = {
        'summary' : summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time_m.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Nairobi',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Nairobi',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24*60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service.events().insert(calendarId ='primary', body=event).execute()  

if __name__ == '__main__':
    speak("AgriBot activated ")
    speak("Hello there")
    while True:
        query = take_command().lower()
        if 'schedule an event' in query:
            start_time()
