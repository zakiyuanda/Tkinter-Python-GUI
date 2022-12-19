from translate import Translator
from gtts import gTTS as g
from playsound import playsound as p
import os
import speech_recognition as sr
from tkinter import *
from tkinter.ttk import *
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
            said = r.recognize_google(audio,language = ("Arabic_ar").split("_")[1])
        except Exception as e:
            pass
            #speak("Exception")

        return said
def clicked():
    text = audio()
    lang1 = ("English_en").split("_")[1]
    #lang2 = ("Arabic_ar").split("_")[1]
    txt1.delete(0,END)
    txt1.insert(0,text)
    #translator = Translator(from_lang = lang1, to_lang=lang2)
    result = lang1.translate(text)
    txt2.delete(0,END)
    txt2.insert(0,result)
    #speak(result)


txt1 = Entry(window, width=50)
txt1.grid(column = 0, row = 3)

txt2 = Entry(window, width=50)
txt2.grid(column = 2, row = 3)
bt = Button(window, text="Speak", command=clicked, width=50)
bt.grid(column = 0, row = 4)

window.mainloop()
