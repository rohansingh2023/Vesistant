from distutils import command
import imp
import random
from re import I
import re
from numpy import place
import speech_recognition as sr
import pyttsx3 as ts

from Ai_Assistant.features import location
from Ai_Assistant.features import my_location
from Ai_Assistant.features import date_time
from Ai_Assistant.features import switch_window
from Ai_Assistant.features import open_classroom
from Ai_Assistant.features import take_picture
from Ai_Assistant.features import news_headlines
from Ai_Assistant.features import open_youtube
from Ai_Assistant.features import open_gmail
from Ai_Assistant.features import google_search
from Ai_Assistant.features import notepad
from Ai_Assistant.features import open_google
from Ai_Assistant.features import get_random_joke
from Ai_Assistant.features import get_random_advice
from Ai_Assistant.features import whatsapp_web
from Ai_Assistant.features import read_pdf
from Ai_Assistant.features import restart
from Ai_Assistant.features import hybernate
from Ai_Assistant.features import my_location
from Ai_Assistant.features import translation
from Ai_Assistant.features import weather
from Ai_Assistant.features import temperature
from Ai_Assistant.features import ai_gyan_about
from Ai_Assistant.features import ai_gyan_blogs
from Ai_Assistant.features import ai_gyan_courses
from Ai_Assistant.features import ai_gyan_events
from Ai_Assistant.features import ce_dept
from Ai_Assistant.features import lbs
from Ai_Assistant.features import national_start_up_day
from Ai_Assistant.features import whats_new
from Ai_Assistant.features import placement
from Ai_Assistant.features import principal_desk
from Ai_Assistant.features import vesit_main_page
from Ai_Assistant.features import creative_innovations
from Ai_Assistant.features import electronics_dept




engine = ts.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

class AiAssistant:
    def __init__(self):
        pass

    def mic_input(self):
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
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return  False


    def tts(self, text):
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

    def tell_me_date(self):
        return date_time.date()

    def tell_me_time(self):
        return date_time.time()

    #def launch_any_app(self, path_of_app):
    #   """
    #   Launch any windows application 
    #    :param path_of_app: path of exe 
    #   :return: True is success and open the application, False if fail
     #    """
     #  return launch_an_app.launch_app(path_of_app)

   # def website_opener(self, domain):
      #  """
      #  This will open website according to domain
       # :param domain: any domain, example "youtube.com"
        #:return: True if success, False if fail
        #"""
        #return open_website.website_opener(domain)

    def weather(self):
        return weather.weather()
       

    def news(self):
        return news_headlines.news()

    def restart(self):
        restart.restart()

    #def look_in_wikipedia(self):
    #   open_youtube.search_wikipedia()
    
    def joke(self):
        return get_random_joke.get_random_joke()

    def advice(self):
        return get_random_advice.get_random_advice()

    #def launch_any_app(self, path_of_app):
     #   return launch_an_app.launch_app(path_of_app)

    def whats_new(self):
        return whats_new.new()

    def vesit_main_page(self):
        return vesit_main_page.new()

    def principal_desk(self):
        return principal_desk.new()

    def placement(self):
        return placement.new()
  
    def national_startup_day(self):
        return national_start_up_day.new()
   
    def lbs(self):
        return lbs.new()

    def electronics_dept(self):
        return electronics_dept.new()

    def creative_innovations(self):
        return creative_innovations.new()

    def ce_dept(self):
        return ce_dept.new()

    def ai_gyan_about(self):
        return ai_gyan_about.new()

    def ai_gyan_course(self):
        return ai_gyan_courses.new()

    def ai_gyan_blogs(self):
        return ai_gyan_blogs.new()

    def ai_gyan_events(self):
        return ai_gyan_events.new()

    def location(self, place):
       return location.loc(place)

    def my_location(self):
        state, country = my_location.My_Location()
        return  state, country
      
    def temperature():
        return temperature.temperature()
       

    def hibernate(self):
        return hybernate.hibernate()
        
    def take_note(self, text):
        notepad.note(text)

    def open_youtube(self):
        return open_youtube.youtube()
   
    def open_google(self):
        return open_google.google()

    def open_gmail(self):
        return open_gmail.gmail()

    def open_classroom(self):
        return open_classroom.classroom()

    def open_whatsapp_web(self):
        return whatsapp_web.whatsapp_web()
    
    def switching_window(self):
        return switch_window.switch_window()
  
    def web_search(self):
        return google_search.search()

    def translator(self):
        return translation.reply()

    def take_picture(self):
        return take_picture.image()

    def read_PDF(self,book_name):
        read_pdf.readPDF(book_name)

        