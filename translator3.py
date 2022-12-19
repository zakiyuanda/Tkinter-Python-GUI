from translate import Translator
from gtts import gTTS as g
from playsound import playsound as p
import os
import speech_recognition as sr
from tkinter import *
from tkinter.ttk import *
from awesometkinter.bidirender import add_bidi_support, render_text
from bidi.algorithm import get_display
import arabic_reshaper

window = Tk()
window.geometry("670x125")
window.title("Translator app")
'''
def speak(text):
    sp = g(text=text, lang=(combo2.get()).split("_")[1],slow=False)
    audio = 'speech.mp3'
    sp.save(audio)
    p(audio)
    os.remove(audio)
'''
def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio,language = (combo1.get()).split("_")[1])
            reshaped_text = arabic_reshaper.reshape(said)    # correct its shape
            bidi_text = get_display(reshaped_text)
            obj=gTTS(text=t,lang='ar',slow=False)
            obj.save('text.mp3')
 
        except Exception as e:
            pass
            #speak("Exception")

        return bidi_text
def clicked():
    text = audio()
    #add_bidi_support(text)
    lang1 = (combo1.get()).split("_")[1]
    lang2 = (combo2.get()).split("_")[1]
    txt1.delete(0,END)
    txt1.insert(0,text)
    translator = Translator(from_lang = lang1, to_lang=lang2)
    result = translator.translate(text)
    txt2.delete(0,END)
    txt2.insert(0,result)
    #speak(result)
def c():
    text = txt1.get()
    lang1 = (combo1.get()).split("_")[1]
    lang2 = (combo2.get()).split("_")[1]
    translator = Translator(from_lang = lang1, to_lang=lang2)
    result = translator.translate(text)
    txt2.delete(0,END)
    txt2.insert(0,result)
    #speak(result)
    
#dummyvar = StringVar()
#dummyvar.set(render_text(text))
#text=audio()
L1 = Label(window, text="Select known language", width=50)
L1.grid(column = 0, row = 0)
combo1 = Combobox(window, width=50)
combo1['values'] = ("Arabic_ar","English_en", "Spanish_es", "Portuguese_pt", "Chinese_zh-tw", "German_de", "French_fr", "Romanian_ro", "Russian_ru",  "Hindi_hi", "Bengali_bn", "Indonesian_id", "Urdu_ur", "Japanese_ja", "Swahili_sw", "Marathi_mr", "Telugu_te","Punjabi_pa","Tamil_ta","Turkish_tr", "Korean_ko","Italian_it","Dutch_nl")
combo1.current(0)
combo1.grid(column = 0, row = 1)
L12 = Label(window, text="Insert text here:", width=50)
L12.grid(column = 0, row = 2)
txt1 = Entry(window, width=50)

txt1.grid(column = 0, row = 3)
L2 = Label(window, text="Select language to translate to", width=50)
L2.grid(column = 2, row = 0)
L22 = Label(window, text="Answer text goes here:", width=50)
L22.grid(column = 2, row = 2)
combo2 = Combobox(window, width=50)
combo2['values'] = ("English_en", "Spanish_es", "Portuguese_pt", "Chinese_zh-tw", "German_de", "French_fr", "Romanian_ro", "Russian_ru", "Arabic_ar", "Hindi_hi", "Bengali_bn", "Indonesian_id", "Urdu_ur", "Japanese_ja", "Swahili_sw", "Marathi_mr", "Telugu_te","Punjabi_pa","Tamil_ta","Turkish_tr", "Korean_ko","Italian_it","Dutch_nl")
combo2.current(0)
combo2.grid(column = 2, row = 1)
txt2 = Entry(window, width=50)
txt2.grid(column = 2, row = 3)
bt = Button(window, text="Speak", command=clicked, width=50)
bt.grid(column = 0, row = 4)
LL = Label(window, text="Or")
LL.grid(column = 1, row = 4)
bt1 = Button(window, text="Submit", command=c, width=50)
bt1.grid(column = 2, row = 4)
add_bidi_support(txt1)

window.mainloop()
