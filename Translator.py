# from fnmatch import translate
# from time import sleep
# from googletrans import Translator
# import googletrans #pip install googletrans
# from gtts import gTTS
# import googletrans
# import pyttsx3
# import speech_recognition 
# import os
# from playsound import playsound
# import time

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# rate = engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
#     r = speech_recognition.Recognizer()
#     with speech_recognition.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         r.energy_threshold = 300
#         audio = r.listen(source,0,4)

#     try:
#         print("Understanding..")
#         query  = r.recognize_google(audio,language='en-in')
#         print(f"You Said: {query}\n")
#     except Exception as e:
#         print("Say that again")
#         return "None"
#     return query

# def translategl(query):
#     speak("SURE SIR")
#     print(googletrans.LANGUAGES)
#     translator = Translator()
#     speak("Choose the language in which you want to translate")
#     b = input("To_Lang :- ")   
#     text_to_translate = translator.translate(query,src = "auto",dest= b,)
#     text = text_to_translate.text
#     try : 
#         speakgl = gTTS(text=text, lang=b, slow= False)
#         speakgl.save("voice.mp3")
#         playsound("voice.mp3")
        
#         time.sleep(5)
#         os.remove("voice.mp3")
#     except:
#         print("Unable to translate")

import pyttsx3
import speech_recognition as sr
from googletrans import LANGUAGES, Translator 
from gtts import gTTS
import os
from playsound import playsound
import time

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

# Function to speak audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to listen to the user's voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception as e:
        print("Sorry, I couldn't hear that. Please try again.")
        return "None"
    return query

# Function to handle translation and text-to-speech output
def translategl(query):
    speak("Sure, Sir.")
    print("Available languages for translation:", LANGUAGES)  # Use LANGUAGES correctly

    # Prompt user to input the target language code
    speak("Please choose the language you want to translate to.")
    
    # Let user input target language
    target_lang = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip()

    # Validate if the entered language code is correct
    if target_lang not in LANGUAGES:
        print(f"Sorry, the language code '{target_lang}' is not valid. Please enter a valid code.")
        speak(f"Sorry, the language code {target_lang} is not valid. Please try again.")
        return
    
    translator = Translator()
    
    try:
        # Translate the query
        translated = translator.translate(query, src="auto", dest=target_lang)
        print(f"Translated text: {translated.text}")

        # Use gTTS to convert the translated text to speech
        speak("Here is the translated text")
        speakgl = gTTS(text=translated.text, lang=target_lang, slow=False)
        speakgl.save("translated_voice.mp3")

        # Play the translated speech
        playsound("translated_voice.mp3")
        time.sleep(5)  # Give it some time to play the audio

        # Remove the temporary audio file
        os.remove("translated_voice.mp3")
    
    except Exception as e:
        print(f"Error during translation or speech synthesis: {e}")
        speak("Sorry, I was unable to translate the text.")

# Main execution
if __name__ == "__main__":
    speak("Hello, I am Jarvis. What would you like to translate today?")
    
    while True:
        # Listen for the command from the user
        query = takeCommand()

        # If the user says "exit", break out of the loop
        if query and 'exit' in query.lower():
            speak("Goodbye!")
            break

        # Otherwise, call the translation function
        if query != "None":
            translategl(query)

