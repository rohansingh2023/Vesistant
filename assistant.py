from PyQt5 import QtCore, QtGui, QtWidgets
from Ai_Assistant import AiAssistant
from txttsp import speak
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pprint
import sys
import datetime
import pyautogui
import wikipedia
import winshell
import wolframalpha
from random import choice
import mysql.connector

obj = AiAssistant()


def atStart():
    speak("Initializing Vesistant......Please wait")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.ExecuteCommands()

    def ExecuteCommands(self):
        atStart()
        # wishMe()
        speak("Hello I am vesistant.....How can I help you?")
        # name = obj.mic_input()
        # speak("Hello" + name)
        # speak("How are you?")
        # health = obj.mic_input()
        # if "fine" in health or "good" in health or "hale and hearty" in health or "in pink of health" in health:
        #     speak("Nice to know that"+name)
        #     speak("Please tell me how can I help you?")

        while True:
            command = obj.mic_input()

            if 'open whatsapp web' in command or "open whatsapp" in command or "whatsapp" in command:  # checked
                obj.open_whatsapp_web()
                speak("Opened whatsapp for you"+name)
                speak("What else would you like me to do for you?")

            elif "make a note" in command or "write this down" in command or "remember this" in command:  # not working
                speak("What would you like me to write down?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that sir ")
                speak("Made a note"+name)
                speak("What else would you like me to do for you?")

            elif "wikipedia" in command:

                speak('Searching Wikipedia...')
                statement = command.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command or "screenshot" in command:
                speak("By what name do you want to save the screenshot?")  # checked
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured"+name)
                speak("What else would you like me to do for you?")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay "+name+"Switching the window")
                obj.switching_window()  # checked
                speak("I have switched the windo for you")
                speak("What else would you like me to do for you?")

            elif "weather" in command:
                obj.weather()

            elif "buzzing" in command or " today's news" in command or "top headlines of today" in command or "news" in command or "headlines" in command:
                news_res = obj.news()  # checked
                speak('Source:The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res) - 2:
                        break
                speak(
                    'These were the top headlines for today,Have a nice day ahead'+name)

            elif 'joke' in command:  # checked
                speak(f"Hope you like this one"+name)
                joke = obj.joke()
                speak(joke)
                print(joke)
                speak("What else would you like me to do for you?")

            elif "advice" in command:  # checked
                speak(f"Here's a random advice for you"+name)
                advice = obj.advice()
                speak(advice)
                print(advice)
                speak("What else would you like me to do for you?")

            elif "open youtube" in command:  # checked
                obj.open_youtube()
                speak("What else would you like me to do for you?")

            elif "open website" in command:  # checked
                obj.open_google()
                speak("What else would you like me to do for you?")

            elif "open gmail" in command:  # checked
                obj.open_gmail()
                speak("What else would you like me to do for you?")

            elif "open classroom" in command or "classroom" in command:  # checked
                obj.open_classroom()
                speak("What else would you like me to do for you?")

            elif 'my location' in command:  # checked
                state, country = obj.my_location()
                speak(f"Sir, You Are Now In {state,country}.")

            elif "take picture" in command or "click a photo" in command or "picture" in command or "":
                print("Capturing you sir!")
                speak("Capturing you sir!")  # checked
                obj.take_picture()
                print("Done sir")
                speak("Done sir")
                speak("What else would you like me to do for you?")

            elif "where is" in command:  # checked
                place = command.split('where is ', 1)[1]
                location = obj.location(place)
                speak('Here is what I found')

            elif "date" in command:  # checked
                date_s = obj.tell_me_date()
                print(date_s)
                speak(f"Sir,the date is {date_s}")
                print(date_s)

            elif "time" in command:
                speak(f"the time is")
                obj.tell_me_time()

            elif 'temperature ' in command:
                obj.temperature()

            elif 'translate' in command:
                obj.translator()

            elif "empty recycle bin" in command:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle bin has been emptyed")
                speak("What else would you like me to do for you?")

            elif "calculate" in command:  # to be checked
                app_id = "L92UJE-QE4KQ4HEJK"
                client = wolframalpha.Client(app_id)
                index = command.lower().split().index('calculate')
                command = command.split()[index+1:]
                res = client.command(''.join(command))
                answer = next(res.results).text
                print("The answer is:"+answer)
                speak("The answer is:"+answer)

            elif "restart" in command:
                speak("Restarting the pc")
                obj.restart()

            elif "hibernate" in command or "sleep" in command:
                speak("Hibernating the pc")
                obj.hibernate()

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright, It was nice working with you. See you")
                sys.exit()

            elif "about Ai_gyan" in command:
                speak("Here is some info about Ai_gyan")
                obj.ai_gyan_about()

            elif "Ai_gyan courses" in command:
                speak("Here are Ai_gyan courses")
                obj.ai_gyan_course()

            elif "Ai_gyan blogs" in command:
                speak("Here are Ai_gyan blogs")
                obj.ai_gyan_blogs()

            elif "Ai_gyan events" in command:
                speak("Here are Ai_gyan events")
                obj.ai_gyan_events()

            elif "Computer department" in command or "Computer Engineering Department" in command:
                speak("Here is some info about Computer Engineering Department")
                obj.ce_dept()

            elif "Electronics department" in command:
                speak("Here is some info about Electronics Department")
                obj.electronics_dept()

            elif "Creative" in command or 'innovation' in command:
                speak("Here is some info about creative/innovation section")
                obj.creative_innovations()

            elif "lbs" in command or "Looking beyond syllabus " in command:
                speak("Here is some info about Looking beyond syllabus competition")
                obj.creative_innovations()

            elif "Creative" in command or 'innovation' in command:
                speak("Here is some info about creative/innovation section")
                obj.creative_innovations()

            # elif "placement" in command:
            #     speak("Here is some info about placement procedure")
            #     obj.placement()

            elif "principals desk" in command:
                speak("Here is some info about principals desk")
                obj.principal_desk()

            elif "whats new" in command:
                speak("Here is some info about whats new in college")
                obj.whats_new()

            # elif "vesit" in command:
            #     speak("Here is some info about vesit major sections")
            #     obj.vesit_main_page()

            elif "national startup day" in command:
                speak("Here is some info about national startup day")
                obj.national_startup_day()

            elif "Tell me about Vesit" in command:
                speak("Vivekanand Education Society’s Institute of Technology (VESIT) was established in 1984, with the aim of providing professional education in the field of Engineering. This institute is affiliated to the University of Mumbai and follows the rules and regulations laid down by government, AICTE, and University for admission; 51% reserved for Sindhi Linguistic minority and 49% through CAP test. The management quota has been surrendered to DTE to make admission centralized.")

            elif "departments" in command:
                speak("Following departments are there in Vesit: Electronics Engineering, Computer Engineering, Instrumentation Engineering, Electronics and Telecommunication Engineering, Information Technology, Newly-adopted AI and Data Science,Masters of Computer Applications.")

            elif "societies" in command:
                speak("There are 4 societies in VESIT: Computer Society of India (CSI),Institute of Electrical and Electronics Engineers (IEEE), Indian Society for Technical Education (ISTE), International Society of Automation (ISA). Various workshops & activities are conducted by these socities throughout the semester")

            elif "Extra-Curricularr Activities of Vesit" in command:
                speak("International Society of Automation, ISA-VESIT took a huge leap this year on the path to give the service of a Technical Society in the true sense. Set out to achieve technical prowess, it has surely come a long way. ISA-VESIT has now become a more technical oriented society and aims at imparting technical skills to its members in tandem with recreational events and skill enhancing workshops.")

            elif "admissions" in command:
                speak("Admissions at Vivekanand Education Society’s Institute of Technology is done through marks secured by a candidate in either MHT CET or JEE Main. Application forms are made available online only via VESIT Admission portal. Candidates need to register themselves. Then, log in using the created password and email ID.")

            elif "placements" in command:
                speak("Vesit has an active placement cell that not only enhances employability skills, but also the overall development of the student’s personality. More than 80-85% students are placed everyyear, with average package of 4 lpa offered.")

            elif "scholarships" in command:
                speak("Different scholarship schemes are available at Vivekanand Education Society’s Institute of Technology. The institute also has an in-charge for departmental scholarships. In 2017-18, a total of 146 students were awarded scholarships. Following scholarships are provided at the institute: Vivekananda Jyoti Scholarship, Student Aid, Geeta Israni Foundation Scholarship, Narotam Sekhsaria Scholarship.")

            elif "internet facilities" in command:
                speak("Yes, students, as well as staff, can make use of the internet facilities available at the college library. It provides high-speed internet.")

            elif "Does the college have seats under reservation quota?" in command:
                speak(
                    "Seats under reservation quota are available as per government guidelines.")
             # elif 'ask' in statement:
            #speak('I can answer to computational and geographical questions and what question do you want to ask now')
            # question=takeCommand()
            # app_id="R2K75H-7ELALHR35X"
            #client = wolframalpha.Client('R2K75H-7ELALHR35X')
            #res = client.query(question)
            #answer = next(res.results).text
            # speak(answer)
            # print(answer)

            # elif 'search'  in statement:
            #statement = statement.replace("search", "")
            # webbrowser.open_new_tab(statement)
            # time.sleep(5)

           #  elif 'news' in statement:
           # news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
           # speak('Here are some headlines from the Times of India,Happy reading')
           # time.sleep(6)
