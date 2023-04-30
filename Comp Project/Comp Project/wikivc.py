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
