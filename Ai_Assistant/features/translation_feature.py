from pickle import TRUE
from typing import Text
from debugpy import listen
import speech_recognition as sr
from gtts import gTTS
import playsound
from sympy import source
import translators as ts
import os

def melania_listen_en():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.energy_threshold = 4000
            audio=r.listen(source)
            try:
                    print("Recognizing...")
                    text=r.recognize_google(audio,language='en')
                    text=text.lower()
                    print(f'You said: {text}')
            except:
                    print('Please try again')
                    text=melania_listen_en()
                    return text
    except Exception as e:
                print(e)
                return  False
    return text
        
def melania_talk(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='hi')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#hindi
def translator_en_hi(text):
    melania_talk(ts.google(text,from_language='en',to_language='hi'))
#russian
def translator_en_ru(text):
    melania_talk(ts.google(text,from_language='en',to_language='ru'))
#urdu
def translator_en_ur(text):
    melania_talk(ts.google(text,from_language='en',to_language='ur'))
#tamil
def translator_en_ta(text):
    melania_talk(ts.google(text,from_language='en',to_language='ta'))
#french
def translator_en_fr(text):
    melania_talk(ts.google(text,from_language='en',to_language='fr'))
#spanish
def translator_en_es(text):
    melania_talk(ts.google(text,from_language='en',to_language='es'))
#
def translator_en_de(text):
    melania_talk(ts.google(text,from_language='en',to_language='de'))
#romanian
def translator_en_ro(text):
    melania_talk(ts.google(text,from_language='en',to_language='ro')) 
#polish
def translator_en_pl(text):
    melania_talk(ts.google(text,from_language='en',to_language='pl'))
#portuguese
def translator_en_pt(text):
    melania_talk(ts.google(text,from_language='en',to_language='pt'))
#dutch
def translator_en_nl(text):
    melania_talk(ts.google(text,from_language='en',to_language='nl'))
#gujarati
def translator_en_gu(text):
    melania_talk(ts.google(text,from_language='en',to_language='gu'))
#Norwegian
def translator_en_no(text):
    melania_talk(ts.google(text,from_language='en',to_language='no'))
#Croatian
def translator_en_hr(text):
    melania_talk(ts.google(text,from_language='en',to_language='hr'))
#Maltese	mt
def translator_en_mt(text):
    melania_talk(ts.google(text,from_language='en',to_language='mt'))
#persian
def translator_en_fa(text):
    melania_talk(ts.google(text,from_language='en',to_language='fa'))
#Afrikaans
def translator_en_af(text):
    melania_talk(ts.google(text,from_language='en',to_language='af'))
#irish
def translator_en_ga(text):
    melania_talk(ts.google(text,from_language='en',to_language='ga'))
#italian
def translator_en_it(text):
    melania_talk(ts.google(text,from_language='en',to_language='it'))
#albanian
def translator_en_sq(text):
    melania_talk(ts.google(text,from_language='en',to_language='sq'))
#arabic
def translator_en_ar(text):
    melania_talk(ts.google(text,from_language='en',to_language='ar'))
#japanese
def translator_en_mt(text):
    melania_talk(ts.google(text,from_language='en',to_language='mt'))
#japanese
def translator_en_ja(text):
    melania_talk(ts.google(text,from_language='en',to_language='ja'))
#ajerbaijani
def translator_en_kn(text):
    melania_talk(ts.google(text,from_language='en',to_language='kn'))
#basque
def translator_en_eu(text):
    melania_talk(ts.google(text,from_language='en',to_language='eu'))
#bengali
def translator_en_bn(text):
    melania_talk(ts.google(text,from_language='en',to_language='bn'))
#korean
def translator_en_ko(text):
    melania_talk(ts.google(text,from_language='en',to_language='ko'))
#latin
def translator_en_la(text):
    melania_talk(ts.google(text,from_language='en',to_language='la'))
#belarusian
def translator_en_be(text):
    melania_talk(ts.google(text,from_language='en',to_language='be'))
#Malay
def translator_en_ms(text):
    melania_talk(ts.google(text,from_language='en',to_language='ms'))
#czech
def translator_en_cs(text):
    melania_talk(ts.google(text,from_language='en',to_language='cs'))
#bulgarian
def translator_en_bg(text):
    melania_talk(ts.google(text,from_language='en',to_language='bg'))

def translator_en_bg(text):
    melania_talk(ts.google(text,from_language='en',to_language='bg'))

def translator_en_bg(text):
    melania_talk(ts.google(text,from_language='en',to_language='bg'))



def melania_reply(text):
    while True:
        print("tell your destination lang")
        source_target_lang=melania_listen_en()
        print(source_target_lang)
        
        if 'english to hindi' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_hi(Text_to_translate)
                else:
                    break

        elif 'english to russian' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_ru(Text_to_translate)
                else:
                    break

        elif 'english to gujarati' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_gu(Text_to_translate)
                else:
                    break
        elif 'english to urdu' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_ur(Text_to_translate)
                else:
                    break

        if 'english to tamil' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_ta(Text_to_translate)
                else:
                    break
        
        if 'english to french' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_fr(Text_to_translate)
                else:
                    break

        if 'english to spanish' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_gu(Text_to_translate)
                else:
                    break

        if 'english to gujarati' in source_target_lang:
            while True:
                print("text")
                Text_to_translate=melania_listen_en()
                print(Text_to_translate)
                if Text_to_translate!='switch translator':
                    translator_en_gu(Text_to_translate)
                else:
                    break
        elif 'turn off translator':
            print("Thanks")
            break
        else:
            print("Error")
        
def reply():
    print("speak")
    listen=melania_listen_en()
    print(listen)
    melania_reply(listen)

