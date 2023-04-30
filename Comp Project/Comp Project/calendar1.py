import speech_recognition as sr
import datetime
import calendar
import pyttsx3

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


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Which day would you like to schedule?")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry I Could not understand what you said")
    except sr.RequestError as e:
        speak("Sorry I Could not request results from Google Speech Recognition service; {0}".format(e))

        # Get the current year
        year = datetime.datetime.now().year

        # Get the user's input for the day and month
        speak("Which day of the month would you like to schedule?")
        day = int(recognize_speech())

        speak("Which month would you like to schedule?")
        month = recognize_speech()

        # Convert the month to a number
        month_num = datetime.datetime.strptime(month, "%B").month

        # Update the calendar schedule
        calendar.setyear(year)
        calendar.monthcalendar(year, month_num)[0][day-1] = "X"

        # Print the updated calendar schedule
        print(calendar.month(year, month_num))

recognize_speech()