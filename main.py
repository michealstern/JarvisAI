import pyttsx3 as py   # Converts text to voice.
import speech_recognition as  sr # Converts speech to text.
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest

#...............................  Password Protection .......................

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    # pw_file = open("password.txt","r")
    pw_file = open("C:\\Users\\arman\\Desktop\\Python Projects\\JarvisAI\\password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

#........................... Jarvis GIF  ...................................

from jarvisGIF import play_gif
play_gif


#Initializing pyttsx3.
engine = py.init("sapi5") # sapi5 it is microsoft API which use in window 
voices = engine.getProperty("voices") # To get lists of available voice in your system.
engine.setProperty("voice", voices[1].id) # To select 0male, 1female voice.
engine.setProperty("rate",160) # Set speech rate, here rate 160 words per minute

def speak(audio): # This function take audio input.
    engine.say(audio)  # Convert text into speech.
    engine.runAndWait() # It executes the speech and waits until the speech is complete.

# speak("Hello Micheal Stern , How was your day ?")

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

#...............................1. Set Alarm on PC ...................................

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

######################

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up jarvis" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "ok jarvis now you can go" in query:
                    speak("Ok sir , You can call me anytime")
                    break

                ###### Change password #####

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

#........................... Schedule My Day ...................................
          
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        num_Oftasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(num_Oftasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                        file = open("password.txt", "r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-", 
                            message = content,
                            timeout = 15
                            )

#........................... FOCUS MODE  ...................................

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile(r"C:\\Users\\arman\\Desktop\\Python Projects\\JarvisAI\\focusMODE.py")
                        exit()
                    else:
                        pass
                    
#........................... TRANSLATOR  ...................................

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

#........................... Open Any App  ...................................

                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

#........................... Internet Speed  ...................................
                
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576  #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

#........................... IPL Score ...................................

                elif "ipl score" in query:
                    from plyer import notification  
                    import requests
                    from bs4 import BeautifulSoup 
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

#...........................  ROCK PAPER SCISSOR .................................

                elif "play game" in query:
                    from game import game_play
                    game_play()

#...........................  SCREENSHOT .................................

                elif "screenshot" in query:
                     import pyautogui as pyt
                     im = pyt.screenshot()
                     im.save("ss.jpg")

                elif "jarvis take screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

#...........................CAMERA  ...................................

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile")
                    pyautogui.press("enter")

#........................... For conversation ...................................

                elif "hello jarvis" in query:
                    speak("Hii sir, how are you ?")
                elif "hi jarvis" in query:
                    speak("Hii sir, how are you ?")
                elif "hey jarvis" in query:
                    speak("Hii sir, how are you ?")
                elif "hay jarvis" in query:
                    speak("Hii sir, how are you ?")
                elif "i am good what about you" in query:
                    speak("i am always good, sir")
                elif "i am fine what about you" in query:
                    speak("i am always fine, sir")
                elif "i am good" in query:
                    speak("that's great sir")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "all good" in query:
                    speak("that's great sir")
                elif "how are you jarvis" in query:
                    speak("i am always good, what about you sir ")
                elif "how r u jarvis" in query:
                    speak("i am always good, what about you sir ")
                elif "i am also good" in query:
                    speak("that's great sir")
                elif "thank you" in query:
                    speak("you'r welcome, sir")
                elif "thank you jarvis" in query:
                    speak("you'r welcome, sir")
                elif "thank u jarvis" in query:
                    speak("you'r welcome, sir")

#...................... Make your own playlist  .....................................

                elif "jarvis i am tired" in query:
                    speak("Playing your favourite song, sir")
                    a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=eNvUS-6PTbs")
                    # You can add songs using elif b==2, elif b==3...etc.


#.............................Fully Automate Youtube ................................

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up, sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume downsir, sir")
                    volumedown()
                    

#....................... OPEN/CLOSE APPS WITH JUST YOUR VOICE ........................

                elif "open" in query:
                    from fetchApp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from fetchApp import closeappweb
                    closeappweb(query)

#............................ For Searching.........................................

                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)

#............................ News ............................

                elif "news" in query:
                    from News import latestnews
                    latestnews()

#............................... Calculate ...................................

                elif "calculate" in query:
                    from Calculator import WolfRamAlpha
                    from Calculator import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

#............................. Whatsapp automation ................................

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

#............................ For Automating Temperature ............................

                elif "temperature" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

#...............................2. Set Alarm on PC ...................................

                elif "jarvis set alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("Please tell me the time:-- ")
                    alarm(a)
                    speak("Done, sir")

#.............................. For Automating Time..................................

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is{strTime}")

                
#............................... HOTWARD DETECTION ...................................

                elif "finally go to sleep Jarvis" in query:
                    speak("Going to sleep, sir")
                    exit()

#............................... Remember Function ......................

                elif "remember that" in query:
                    rememberMessage = query.replace("jarvis remember that", "")
                    rememberMessage = query.replace("remember that jarvis", "")
                    rememberMessage = query.replace("jarvis remember", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me" + rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())


#...............................  Shutdown system ............................

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break