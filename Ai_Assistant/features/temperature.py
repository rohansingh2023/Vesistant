import requests
import speech_recognition as sr
import pyttsx3 as ts
from bs4 import BeautifulSoup
import requests

engine = ts.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def mic_input():
        """
        Fetch input from mic
        return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
            with sr.Microphone() as source:
                print("Listening....")
                r.energy_threshold = 400
                audio = r.listen(source)
            try:
                print("Recognizing...")
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'You said: {command}')
            except:
                print('Please try again')
                command = mic_input()
            return command
        except Exception as e:
            print(e)
            return  False


def tts(text):
        """
        Convert any text to speech
        :param text: text(String)
        :return: True/False (Play sound if True otherwise write exception to log and return  False)
        """
        try:
            engine.say(text)
            engine.runAndWait()
            engine.setProperty('rate', 175)
            return True
        except:
            t = "Sorry I couldn't understand and handle this input"
            print(t)
            return False


def speak(text):
    tts(text)

def temperature():
    speak("Please tell the namme of the place of which you want to know the temperature")
    print("Please tell the namme of the place of which you want to know the temperature")
    place = mic_input()
    search = "Temperature in " + place
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current {search} is {temp}")  #checked
    print(f"current{search} is {temp}")
    speak("What else would you like me to do for you?")
