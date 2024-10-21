import os
import pyttsx3 
import datetime
import speech_recognition  as rn
import wikipedia
import webbrowser as wb
from selenium import webdriver
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
print(voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def welcome():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternon sir")
    elif hour>=18 and hour<24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your serice. Please tell me how can I help you?")

def takeCommand():
    r = rn.Recognizer()
    with rn.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizinig...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def joke():
    speak(pyjokes.get_joke())



if __name__ == "__main__":
    welcome()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'play music' in query:
            songpath = "C:/Users/HP/Downloads/song.mp3"
            songs = os.listdir(songpath)
            os.startfile(os.path.join(songpath, songs[0]))
        elif 'search in brave' in query:
            speak("What should I search for ?")
            bravepath = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            search = takeCommand().lower()
            wb.get(bravepath).open_new_tab(search+'.com')
        elif 'joke' in query:
            joke()
        elif 'remember that' in query:
            speak("What should I remember ?")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you have something today for me' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that" +remember.read())
        elif 'offline' in query:
            speak("Going offline. Goodbye!")
            quit()

