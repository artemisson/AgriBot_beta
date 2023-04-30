import pyttsx3
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import datetime
import datefinder
import psutil
from datetime import datetime, timedelta
from cal_setup import get_calendar_service

# init pyttsx"""  """
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
                
def farm_jokes():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        speak("Why did the farmer want to bury all of his money?")
        time.sleep(2)
        speak("To make the soil rich.")
        time.sleep(3)
        farm_joke1()
        
def farm_joke1():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        speak("Do you wanna hear another joke? yes or no?")
        time.sleep(2)
        query = take_command().lower()
        if 'yes' in query:
            speak("What do you call a cow sleeping at the farm?")
            time.sleep(2)      
            speak("A bull-dozer.")
            time.sleep(3)
            farm_joke2()
        elif 'no' or 'no more jokes' in query:
            speak("Let's get back to work. What else would you like me to do for you?")
        
def farm_joke2():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        speak("Do you wanna hear another joke? yes or no?")
        time.sleep(2)
        query = take_command().lower()
        if 'yes' in query:
            speak("What was the detective police duck trying to do?")
            time.sleep(2)      
            speak("Quack the case.")
            time.sleep(2)
            farm_joke3()
        elif 'no' or 'no more jokes' in query:
            speak("Let's get back to work. What else would you like me to do for you?")
              
def farm_joke3():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        speak("Do you wanna hear another joke? yes or no?")
        time.sleep(2)
        query = take_command().lower()
        if 'yes' in query:
            speak("What did the farmer shout when the cow ran out of milk?") 
            time.sleep(2)
            speak("This is udder nonsense!")
            time.sleep(3)
            speak("Okay enough jokes for now, what else would you like me to do for you?")
        elif 'no' or 'no more jokes' in query:
            speak("Let's get back to work. What else would you like me to do for you?")            
                

def wikisearch():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What would you like to know?: ")
        audio = r.listen(source)
    try:
        question = r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return

    results = wikipedia.search(question)
    if len(results) > 0:
        page = wikipedia.page(results[0])
        speak(page.summary)
    else:
        speak("Sorry, I could not find an answer to your question.")
        
def Weather():
    # Use speech recognition to get the location from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Starting weather forecast")
        time.sleep(2)
        speak("What is your location, which town are you in?: ")
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
        engine.say(f"Weather forecast for {location} town:")
        engine.say(f" - {weather}")
        engine.say(f" - Temperature: {temp} degrees Celsius")
        engine.say(f" - Feels like: {feels_like} degrees Celsius")
        engine.say(f" - Humidity: {humidity} percent")
        engine.runAndWait()
    else:
        engine.say("Error retrieving weather data.")
        engine.runAndWait()
        
summary1 = None
def start_time():
    r = sr.Recognizer()
    # use the microphone as source
    global start_time_t
    with sr.Microphone() as source:
        speak("What is the date followed by the start time of your event? an example would be like the 25th of May 9pm")
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
        speak("what is the title of your event or the title of the appointment that you would like to schedule?")
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

def cal_update():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Your event or appointment has been successfully updated on Google Calendar.")
        time.sleep(2)
        speak("Would you like to see your event on the calendar?")
        query = take_command().lower()
        if 'yes' in query:
            webbrowser.open("https://calendar.google.com/calendar/u/0/r/week")
            speak("As you can see when you check the day of your scheduled event")
            time.sleep(1)
            speak("against the time you scheduled it, you can see its highlighted for a duration of two hours since the start time of your event.")
            time.sleep(2)
            speak("You can manually adjust the duration and title if you want to.")
            cal_update1()
        elif 'no' in query:
            speak("That's one task down. What else would you like me to do for you?")
            
def cal_update1():
    r = sr.Recognizer()
    with sr.Microphone() as source:           
        speak("Would you like to manually edit the details of your schedule event?")
        time.sleep(1)
        speak("or should I close the calendar because everything is okay?")
        query = take_command().lower()
        if 'close the calendar' in query:
            speak("okay I am closing the calendar")
            time.sleep(2)
            # Find the Chrome process
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'chrome.exe':
                    print(f"Found Chrome process with PID {proc.info['pid']}. Terminating...")
                    proc.kill()
            speak("Is there anything else you would like me to do?")
        elif 'keep editing' in query:
            time.sleep(5)
            time.sleep(5)
            cal_update2()

def cal_update2():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        speak("Would you like to keep editing the details of your scheduled event?")
        time.sleep(1)
        speak("or should I close the calendar because everything is okay?")
        query = take_command().lower()
        if 'close the calendar' in query:
            speak("okay I am closing the calendar")
            time.sleep(2)
            # Find the Chrome process
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'chrome.exe':
                    print(f"Found Chrome process with PID {proc.info['pid']}. Terminating...")
                    proc.kill()
            speak("Is there anything else you would like me to do?")
        elif 'keep editting' in query:
            time.sleep(5)
            time.sleep(5)
            cal_update2()
    

def manual_schedule():
    webbrowser.open("https://calendar.google.com")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Be patient as the webpage loads for a moment.") 
        time.sleep(2)
        speak("To manually update your schedule on this calendar, check the date you want to schedule first.")
        time.sleep(2)
        speak("Then hover the mouse to the start time of the event. Click the box indicating the start time and drag it till the stop time of your event.")
        time.sleep(2)
        speak("Now edit the title of the event according to what you want and the calendar will be updated with your new event!")
        time.sleep(5)
        speak("If you would like to continue editing your schedule, simply say I'd like to keep editing")
        time.sleep(2)
        speak("If you would like to close the calendar, simply say close the calendar")
        time.sleep(2)
        speak("If you would like me to repeat the instructions, kindly say repeat instructions")
        time.sleep(2)
        speak("Would you like to close the calendar or keep editing?")
        time.sleep(3)
        query = take_command().lower()
        if 'repeat instructions please' in query:
           manual_schedule()
        elif 'close the calendar' in query:
            speak("okay I am closing the calendar")
            time.sleep(2)
            # Find the Chrome process
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'chrome.exe':
                    print(f"Found Chrome process with PID {proc.info['pid']}. Terminating...")
                    proc.kill()
            speak("Is there anything else you would like me to do?")
        elif 'keep editing' in query:
            speak("I will give you some time to edit your schedule")
            time.sleep(5)
            time.sleep(5)
            cal_update2()

def close_calendar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("okay I am closing the calendar")
        time.sleep(2)
        # Find the Chrome process
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'chrome.exe':
                print(f"Found Chrome process with PID {proc.info['pid']}. Terminating...")
                proc.kill()
        speak("Is there anything else you would like me to do?")
        
def shutdown():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("It was nice being able to be of use to you. I hope I can help you some other time. Goodbye till next time.")
        exit(0)
        
def init_bot():
    speak("Hello there. I'm Agribot. Please make sure you are connected to the internet.")
    speak("Before we begin I would like to inform you of how I operate.")
    speak("I have a couple of functionalities and these are the commands I respond to.")
    time.sleep(2)
    speak("If you want to know who I am, simply ask who are you.")
    time.sleep(2)
    speak("If you want to have a chat with me just say hello or hi.")
    time.sleep(2)
    speak("If you want to listen to a farm joke, simply say tell me a joke or tell me something funny.")
    time.sleep(2)
    speak("If you want me to schedule an event like an appointment or reminder on your calendar, simply say I would like to schedule an event.")
    time.sleep(2)
    speak("If you want to schedule your events manually by yourself, simply say open manual schedule.")    
    time.sleep(2)
    speak("If you want to check the weather forecast, simply say check the weather or tell the weather forecasst.")
    time.sleep(2)
    speak("If you want me to answer an agriculture related question, simply say I would like to ask a question or say answer this question.")
    time.sleep(2)
    speak("If you want to quit the application, simply tell me to shutdown.")
    time.sleep(2)
    main()
    
def main():
    speak("What would you like for me to do for you?")
    while True:
        query = take_command().lower()
        if 'who are you' in query:
            speak("I am Agribot, your very own personal digital farmer assistant")
            time.sleep(2)
            speak("What would you like me to do for you?")
        elif 'hello' in query:
            casual_chat()
        elif 'what is the weather' in query:
            Weather()     
        elif 'schedule an event' in query:
            start_time()
        elif 'open manual schedule' in query:
            manual_schedule()       
        elif 'tell me a joke' in query:
            farm_jokes()
        elif 'ask a question' in query:
            wikisearch()
        elif 'close the calendar' in query:
            close_calendar()
        elif 'shutdown' in query:
            shutdown()
main()
