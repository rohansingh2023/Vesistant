from click import command
import pyttsx3
import PyPDF2
from os import listdir
import glob
import re

def readPDF(book_name):
   mypath="C/Users/Dell/Downloads"
   for book_name in glob.glob(mypath+"/*"+book_name+".pdf"):
                        # Read the file in binary mode:
                        book_name = open(book_name,"rb")
                    #  Create a PdfFileReader object:
                        pdfReader = PyPDF2.PdfFileReader(book_name)

                    #onlyfiles=[f for f in listdir(mypath) if isfile(join(mypath,f))]

                    # To determine total number of pages in the PDF file:
                        pages = pdfReader.numPages
                    # Initialize the speaker:
                    # Here, init() function is used to get a reference to a pyttsx3.Engine instance
                        speaker = pyttsx3.init()
                    # To access voice property of the speaker:
                        voices = speaker.getProperty('voices')
                    # Set the speaker's gender: 0-> Male (default), 1-> Female
                        speaker.setProperty('voice', voices[1].id)
                    # Iterate through the pages you want to access
                    # For accessing specific pages: Iterate through the corresponding page indices
                    # Note: Index of first page-> 0
                    # Here, entire PDF is accessed:
                        for num in range(pages):
                            # To read current page index:
                            page = pdfReader.getPage(num)
                            # To extract the text present in current page:
                            text = page.extractText()
                            # say() function takes a string as the parameter and then queues the same to be converted from text-to-speech
                            speaker.say(text)
                            # runAndWait() function blocks the engine instance until all the currently queued commands are processed
                            speaker.runAndWait()
                    # To save the audio output as a MP3 file, within this project:
                    # Make use of any MP3 player to access this recording whenever required
                            speaker.save_to_file(text, 'audio.mp3')
                            speaker.runAndWait()
         