import pyttsx3 as py
import datetime

engine = py.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        speak("Good Morning, Micheal Stern")
    elif 12 <= hour < 17:
        speak("Good Afternoon, Micheal Stern")
    elif 17 <= hour < 21:
        speak("Good Evening, Micheal Stern")
    else:
        speak("Good Night, Micheal Stern")

    speak("Please tell me, How can I help you sir ?")














