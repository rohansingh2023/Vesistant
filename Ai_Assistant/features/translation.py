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



#hindi            
def melania_talk_hi(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='hi')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#russian
def melania_talk_ru(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ru')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#urdu
def melania_talk_ur(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ur')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Tamil
def melania_talk_ta(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ta')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#french
def melania_talk_fr(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='fr')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#spanish
def melania_talk_es(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='es')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

def melania_talk_de(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='de')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Romanian
def melania_talk_ro(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='de')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#polish
def melania_talk_pl(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='pl')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#portuguese
def melania_talk_pt(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='pt')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#dutch
def melania_talk_nl(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='nl')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Persian
def melania_talk_fa(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='fa')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Afrikaans

def melania_talk_af(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='af')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Irish
def melania_talk_ga(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ga')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Albanian
def melania_talk_sq(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='sq')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Italian
def melania_talk_it(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='it')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Arabic
def melania_talk_ar(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ar')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Japanese
def melania_talk_ja(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ja')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Azerbaijani
def melania_talk_az(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='az')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#kannada
def melania_talk_kn(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='kn')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Basque
def melania_talk_eu(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='eu')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#bengali
def melania_talk_bn(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='bn')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#korean
def melania_talk_ko(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='az')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#latin
def melania_talk_la(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='la')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Belarusian
def melania_talk_be(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='be')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Malay	ms
def melania_talk_ms(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ms')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Czech	cs
def melania_talk_cs(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='cs')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Bulgarian	bg
def melania_talk_bg(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='bg')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Chinese Traditional	zh-TW
def melania_talk_zh_TW(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='zh-TW')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Chinese Simplified	zh-CN
def melania_talk_zh_CN(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='zh-CN')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Macedonian
def melania_talk_mk(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='mk')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Hebrew	iw
def melania_talk_iw(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='iw')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Telugu	te
def melania_talk_te(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='te')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Gujarati	gu
def melania_talk_gu(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='gu')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Latvian	lv
def melania_talk_lv(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='lv')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#Lithuanian	lt
def melania_talk_lt(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='lt')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Catalan	ca
def melania_talk_ca(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ca')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Danish	da
def melania_talk_da(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='da')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Esperanto	eo
def melania_talk_eo(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='eo')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Estonian	et
def melania_talk_et(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='et')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Serbian	sr
def melania_talk_sr(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='sr')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Filipino	tl
def melania_talk_tl(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='tl')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Slovak	sk
def melania_talk_sk(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='sk')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Finnish	fi
def melania_talk_fi(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='fi')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Slovenian	sl
def melania_talk_sl(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='sl')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Galician	gl
def melania_talk_gl(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='gl')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Swahili	sw
def melania_talk_sw(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='sw')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Georgian	ka
def melania_talk_ka(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ka')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Swedish	sv
def melania_talk_sv(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='sv')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Greek	el
def melania_talk_el(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='el')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Thai	th
def melania_talk_th(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='th')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Haitian Creole	ht
def melania_talk_ht(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='ht')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Ukrainian	uk
def melania_talk_uk(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='uk')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Hungarian	hu
def melania_talk_hu(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='hu')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Vietnamese	vi
def melania_talk_vi(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='vi')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Icelandic	is
def melania_talk_is(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='is')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Welsh	cy
def melania_talk_cy(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='cy')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Indonesian	id
def melania_talk_id(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='id')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Yiddish	yi
def melania_talk_yi(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='yi')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Maltese	mt
def melania_talk_mt(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='mt')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Croatian	hr
def melania_talk_hr(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='hr')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
#Norwegian	no
def melania_talk_no(text):
    file_name='audio_data.mp3'
    tts=gTTS(text=text,lang='no')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

#hindi
def translator_en_hi(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='hi'))
#russian
def translator_en_ru(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='ru'))
#urdu
def translator_en_ur(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='ur'))
#tamil
def translator_en_ta(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='ta'))
#french
def translator_en_fr(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='fr'))
#spanish
def translator_en_es(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='es'))

#
def translator_en_de(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='de'))

#romanian
def translator_en_ro(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='ro')) 
#polish
def translator_en_pl(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='pl'))
#portuguese
def translator_en_pt(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='pt'))
#dutch
def translator_en_nl(text):
    melania_talk_nl(ts.google(text,from_language='en',to_language='nl'))
#gujarati
def translator_en_gu(text):
    melania_talk_hi(ts.google(text,from_language='en',to_language='gu'))
#Norwegian
def translator_en_no(text):
    melania_talk_no(ts.google(text,from_language='en',to_language='no'))
#Croatian
def translator_en_hr(text):
    melania_talk_hr(ts.google(text,from_language='en',to_language='hr'))
#Maltese	mt
def translator_en_mt(text):
    melania_talk_mt(ts.google(text,from_language='en',to_language='mt'))


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
        elif 'english to gujarati' in source_target_lang:
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
        
        if 'english to gujarati' in source_target_lang:
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

