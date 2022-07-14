from os import times
import os
from typing import Text
from pywhatkit import info
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
speaker = pyttsx3.init()

def talk(text):
 speaker.say(text)
 speaker.runAndWait()

def take_sound():
    try:
        with sr.Microphone() as source:
            print('...yes...')
            listener.energy_threshold = 300
            listener.pause_threshold = 2
            voice = listener.listen(source)
            sound = listener.recognize_google(voice)
            sound = sound.lower()
            if 'hooman' in sound:
             sound = sound.replace('hooman', '')
             print(sound)
            
    except:
        pass
    return sound

def run_hooman():
    sound = take_sound()
    print(sound)
    if 'play' in sound:
     song = sound.replace('play', '')
     talk('playing' + song)
     pywhatkit.playonyt(song)
    elif 'time' in sound:
     time = datetime.datetime.now().strftime('%I:%M %p')
     talk('current time is' + time)
    elif 'who is' in sound:
     person = sound.replace('who is', '')
     info = wikipedia.summary(person, 2)
     talk('according to wikipedia'+ info)
    elif 'what is' in sound:
     thing = sound.replace('what is', '')
     info = wikipedia.summary(thing, 2)
     talk('according to wikipedia'+ info)
    elif 'find about' in sound:
     about = sound.replace('find about', '')
     info = wikipedia.summary(about, 2)  
     talk('according to wikipedia'+ info)  
    elif 'date' in sound:
      talk('sorry not today but I will surely plan it for you')
    elif 'are you single' in sound:
     talk('come closer and I will wishper it to you')
    elif 'joke' in sound:
     talk(pyjokes.get_joke())
    elif 'open google' in sound:
        webbrowser.open("google.com") 
    elif 'open vs code' in sound:
        path = "C:\\Users\\nfull\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(path)
    elif 'quit hooman' in sound:
        quit()    
    else:
     talk('please pardon') 

while True:
 run_hooman()     
      


