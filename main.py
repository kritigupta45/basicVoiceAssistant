import pyttsx3 as p
import speech_recognition as sr
import pyaudio
import randfacts
from googsearch import *
from selenium_web import *
from yt_audio import *

engine = p.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("hello, I am your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am having a good day sir.")
speak("what can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" in text2:
    speak("okay, what exactly do you want me to play?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    print("playing {} on youtube".format(infor))
    speak("playing {} on youtube".format(infor))
    assist = music()
    assist.play(infor)

elif "fact" and "facts" in text2:
    speak("sure.")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, "+x)


elif "google" and "search":
    speak("okay, what do you want me to search on google exactly?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    print("showing results for {} on google".format(infor))
    speak("showing results for {} on google".format(infor))
    assist = gosearch()
    assist.inf(infor)
