import pyttsx3 as py   
import speech_recognition as  sr
import pywhatkit
import wikipedia
import webbrowser

def takeCommand(): # This function conver speech into text.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1  # To set duration of pause between speech.
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = py.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",160)

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("jarvis search on google ", "")
        query = query.replace("google search", "")
        query = query.replace("search google ", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found for your search!")
        query = query.replace("jarvis", "")
        query = query.replace("jarvis search on youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("search youtube", "")
        query = query.replace("youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia.....")
        query = query.replace("jarvis", "")
        query = query.replace("jarvis search on wikipedia", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("search wikipedia ", "")
        query = query.replace("wikipedia ", "")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia...")
        print(results)
        speak(results)
