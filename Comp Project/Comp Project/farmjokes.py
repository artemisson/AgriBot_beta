def farm_jokes():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        speak("Why did the farmer want to bury all of his money?")
        time.sleep(3)
        speak("To make the soil rich.")
        time.sleep(3)
        speak("Do you wanna hear another joke?")
        query = take_command().lower()
        if 'another joke' in query:
            speak("What was the detective police duck trying to do?")
            time.sleep(3)      
            speak("Quack the case.")
        if 'tell one more' in query:
            speak("What did the farmer shout when the cow ran out of milk?") 
            time.sleep(3)
            speak("This is udder nonsense!")