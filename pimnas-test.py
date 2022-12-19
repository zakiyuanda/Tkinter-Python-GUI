from tkinter import *
from PIL import ImageTk, Image
import RPi.GPIO as gpio
import time
import pygame
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os
import sounddevice as sd
import soundfile as sf

if os.environ.get('DISPLAY','')=='':
    print('no display found. Using:0.0')
    os.environ.__setitem__('DISPLAY',':0.0')

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_UP)

root = Tk()
root.geometry("241x321")
root.attributes('-fullscreen',True)
pygame.mixer.init()

page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)
page4 = Frame(root)
page5 = Frame(root)
page6 = Frame(root)
page7 = Frame(root)
page8 = Frame(root)
page9 = Frame(root)
page10 = Frame(root)
page11 = Frame(root)
page12 = Frame(root)

for frame in (page1,page2,page3,page4,page5,page6,page7,page8,page9,page10,page11,page12):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

def satu(e):
    button1.focus_set()
def dua(e):
    button2.focus_set()
def tiga(e):
    button3.focus_set()
def empat(e):
    button4.focus_set()
def lima(e):
    button5.focus_set()
def enam(e):
    button6.focus_set()
       
def voice_rec(e):
    fs = 48000
    # seconds
    duration = 30
    myrecording = sd.rec(int(duration * fs),samplerate=fs, channels=2)
    '''
    try:
        temp=init(duration.get())
    except:
        print("Masukan Waktu")
    while temp>0:
        root.update()
        time.sleep
        temp-=1
        label(text=f"{str(temp)}",font="arial 20")
        label.place(x=200,y=300)
    '''    
    sd.wait()
    # Save as FLAC file at correct sampling rate
    return sf.write('my_Audio_file.flac', myrecording, fs)

def fatihah_ay1():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def fatihah_ay2():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def fatihah_ay3():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def fatihah_ay4():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def fatihah_ay5():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def fatihah_ay6():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def fatihah_ay7():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()

def naas_ay1():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()
def naas_ay2():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()
def naas_ay3():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()
def naas_ay4():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()
def naas_ay5():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()
def naas_ay6():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()

def falaq_ay1():
    pygame.mixer.music.load("audio/falaq.mp3")
    pygame.mixer.music.play()
def falaq_ay2():
    pygame.mixer.music.load("audio/falaq.mp3")
    pygame.mixer.music.play()
def falaq_ay3():
    pygame.mixer.music.load("audio/falaq.mp3")
    pygame.mixer.music.play()
def falaq_ay4():
    pygame.mixer.music.load("audio/falaq.mp3")
    pygame.mixer.music.play()
def falaq_ay5():
    pygame.mixer.music.load("audio/falaq.mp3")
    pygame.mixer.music.play()

def ikhlas_ay1():
    pygame.mixer.music.load("audio/ikhlas.mp3")
    pygame.mixer.music.play()    
def ikhlas_ay2():
    pygame.mixer.music.load("audio/ikhlas.mp3")
    pygame.mixer.music.play()    
def ikhlas_ay3():
    pygame.mixer.music.load("audio/ikhlas.mp3")
    pygame.mixer.music.play()    
def ikhlas_ay4():
    pygame.mixer.music.load("audio/ikhlas.mp3")
    pygame.mixer.music.play()    

def nashr_ay1():
    pygame.mixer.music.load("audio/nasr.mp3")
    pygame.mixer.music.play()
def nashr_ay2():
    pygame.mixer.music.load("audio/nasr.mp3")
    pygame.mixer.music.play()
def nashr_ay3():
    pygame.mixer.music.load("audio/nasr.mp3")
    pygame.mixer.music.play()

def lahab_ay1():
    pygame.mixer.music.load("audio/masad.mp3")
    pygame.mixer.music.play()
def lahab_ay2():
    pygame.mixer.music.load("audio/masad.mp3")
    pygame.mixer.music.play()
def lahab_ay3():
    pygame.mixer.music.load("audio/masad.mp3")
    pygame.mixer.music.play()
def lahab_ay4():
    pygame.mixer.music.load("audio/masad.mp3")
    pygame.mixer.music.play()
def lahab_ay5():
    pygame.mixer.music.load("audio/masad.mp3")
    pygame.mixer.music.play()

def maun_ay1():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def maun_ay2():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def maun_ay3():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def maun_ay4():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def maun_ay5():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def maun_ay6():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def maun_ay7():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()

def kautsar_ay1():
    pygame.mixer.music.load("audio/kautsar.mp3")
    pygame.mixer.music.play()
def kautsar_ay2():
    pygame.mixer.music.load("audio/kautsar.mp3")
    pygame.mixer.music.play()
def kautsar_ay3():
    pygame.mixer.music.load("audio/kautsar.mp3")
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
   
def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio,language = ("Arabic_ar").split("_")[1])
            reshaped_text = arabic_reshaper.reshape(said)    # correct its shape

            bidi_text = get_display(reshaped_text)
            obj=gTTS(text=t,lang='ar',slow=False)
            obj.save('text.mp3')

        except Exception as e:
            pass
        return said

def clicked(e):
    text = audio()
    lang = ("Arabic_ar").split("_")[1]
    txt_area.delete(0,END)
    txt_area.insert(0,text)
    result = lang.translate(text)

def Reset():
    txt_area.delete(1.0,END)            
    
def frame1(e):
    show_frame(page1)
    button1.focus_set()
def frame2(e):
    show_frame(page2)
    button2.focus_set()
def frame3(e):
    show_frame(page3)
    button4.focus_set()
def frame4(e):
    show_frame(page4)
    button6.focus_set()
def frame5(e):
    show_frame(page5)
    satu1.focus_set()
def frame6(e):
    show_frame(page6)
    dua1.focus_set()
def frame7(e):
    show_frame(page7)
    tiga1.focus_set()
def frame8(e):
    show_frame(page8)
    empat1.focus_set()
def frame9(e):
    show_frame(page9)
    lima1.focus_set()
def frame10(e):
    show_frame(page10)
    enam1.focus_set()
def frame11(e):
    show_frame(page11)
    tuj1.focus_set()
def frame12(e):
    show_frame(page12)
    lap1.focus_set()

show_frame(page1)
#=============Page1===================
but1 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/button play 50x50V2.png"))  
bg1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/tampilan utama 241x321.jpg"))

label1 = Label(page1, image = bg1)
label1.grid(row = 0, column = 0,sticky = N)

button1 = Button(page1, image=but1, bg = "white", fg = "black")
button1.grid(row = 0, column = 0,sticky = S, pady = 30)
button1.bind("<FocusIn>", lambda e: button1.configure(bg = "black", fg = "white"))
button1.bind("<FocusOut>", lambda e: button1.configure(bg = "white", fg = "black"))
button1.bind("<Return>", frame2)

button1.focus_set() 
#=============Page2 MENU===================
bg2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/menu 241x321.jpg"))
surah= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/tampilan surah button 110x30(1).png"))
deteksi= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/deteksi bacaan.png"))

label2 = Label(page2, image = bg2)
label2.grid(row = 0, column = 0,sticky = N)

button2 = Button(page2, image=surah, bg = "white", fg = "black")
button2.grid(row = 0, column = 0,sticky = N,padx = 0, pady = 120)
button2.bind("<FocusIn>", lambda e: button2.configure(bg = "black", fg = "white"))
button2.bind("<FocusOut>", lambda e: button2.configure(bg = "white", fg = "black"))
button2.bind("<Down>",tiga)
button2.bind("<Up>",dua)
button2.bind("<Return>", frame3)

button3 = Button(page2, image=deteksi, bg = "white", fg = "black")
button3.grid(row = 0, column = 0,sticky = N,padx = 0, pady = 180)
button3.bind("<FocusIn>", lambda e: button3.configure(bg = "black", fg = "white"))
button3.bind("<FocusOut>", lambda e: button3.configure(bg = "white", fg = "black"))
button3.bind("<Down>", tiga)
button3.bind("<Up>", dua)
button3.bind("<Return>", frame3)

#=============Page4 Deteksi===================
bg4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/deteksi bacaan 241x321.jpg"))
rec= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/mic.png"))
det= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/spk.png"))

label3 = Label(page4, image = bg4)
label3.grid(row = 0, column = 0,sticky = N)

txt_area = Entry(page4, font=('times new rommon',15,'bold'),  width=16, justify='center')
txt_area.grid(column = 0, row = 0,sticky= N, padx = 0, pady = 120)

button4 = Button(page4, image=rec, bg = "white", fg = "black")
button4.grid(row = 0, column = 0,sticky = NW,padx = 40, pady = 180)
button4.bind("<FocusIn>", lambda e: button4.configure(bg = "black", fg = "white"))
button4.bind("<FocusOut>", lambda e: button4.configure(bg = "white", fg = "black"))
button4.bind("<Return>", frame4)
button4.bind("<Left>", frame2)

button5 = Button(page4, image=det, bg = "white", fg = "black")
button5.grid(row = 0, column = 0,sticky = NE,padx = 40, pady = 180)
button5.bind("<FocusIn>", lambda e: button5.configure(bg = "black", fg = "white"))
button5.bind("<FocusOut>", lambda e: button5.configure(bg = "white", fg = "black"))

#=============Page3 Tampilan Surah===================
bg3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/tampilan surah 241x321.jpg"))
fatihah= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al fatihah.png"))
nas= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/an nas.png"))
falaq= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al-falaq.png"))
ikhlas= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al ikhlas.png"))
lahab= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al lahab.png"))
nasr= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/an nasr.png"))
maun= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/almaun.png"))
kausar= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al kausar.png"))

label4 = Label(page3, image = bg4)
label4.grid(row = 0, column = 0,sticky = N)

button6 = Button(page3, image=fatihah, bg = "white", fg = "black")
button6.grid(row = 0, column = 0, sticky = NW, padx = 10, pady = 70)
button6.bind("<FocusIn>", lambda e: button6.configure(bg = "black", fg = "white"))
button6.bind("<FocusOut>", lambda e: button6.configure(bg = "white", fg = "black"))
button6.bind("<Return>", frame5)

button7 = Button(page3, image=nas, bg = "white", fg = "black")
button7.grid(row = 0, column = 0, sticky = NW,  padx = 10, pady = 120)
button7.bind("<FocusIn>", lambda e: button7.configure(bg = "black", fg = "white"))
button7.bind("<FocusOut>", lambda e: button7.configure(bg = "white", fg = "black"))

button8 = Button(page3, image=falaq, bg = "white", fg = "black")
button8.grid(row = 0, column = 0, sticky = SW, padx = 10, pady = 120)
button8.bind("<FocusIn>", lambda e: button8.configure(bg = "black", fg = "white"))
button8.bind("<FocusOut>", lambda e: button8.configure(bg = "white", fg = "black"))

button9 = Button(page3, image=ikhlas, bg = "white", fg = "black")
button9.grid(row = 0, column = 0, sticky = SW, padx = 10, pady = 70)
button9.bind("<FocusIn>", lambda e: button9.configure(bg = "black", fg = "white"))
button9.bind("<FocusOut>", lambda e: button9.configure(bg = "white", fg = "black"))

button10 = Button(page3, image=lahab, bg = "white", fg = "black")
button10.grid(row = 0, column = 0, sticky = NE, padx = 10, pady = 70)
button10.bind("<FocusIn>", lambda e: button10.configure(bg = "black", fg = "white"))
button10.bind("<FocusOut>", lambda e: button10.configure(bg = "white", fg = "black"))

button11 = Button(page3, image=nasr, bg = "white", fg = "black")
button11.grid(row = 0, column = 0, sticky = NE, padx = 10, pady = 120)
button11.bind("<FocusIn>", lambda e: button11.configure(bg = "black", fg = "white"))
button11.bind("<FocusOut>", lambda e: button11.configure(bg = "white", fg = "black"))

button12 = Button(page3, image=kausar, bg = "white", fg = "black")
button12.grid(row = 0, column = 0, sticky = SE, padx = 10, pady = 120)
button12.bind("<FocusIn>", lambda e: button12.configure(bg = "black", fg = "white"))
button12.bind("<FocusOut>", lambda e: button12.configure(bg = "white", fg = "black"))

button13 = Button(page3, image=maun, bg = "white", fg = "black")
button13.grid(row = 0, column = 0, sticky = SE, padx = 10, pady = 70)
button13.bind("<FocusIn>", lambda e: button13.configure(bg = "black", fg = "white"))
button13.bind("<FocusOut>", lambda e: button13.configure(bg = "white", fg = "black"))

#=============Page5 Fatihah===================
bg5= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al fatihah 241x321.jpg"))
st_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 1 Al -Fatihah (Arab).png"))
st_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 2 Al -Fatihah (Arab).png"))
st_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 3 Al -Fatihah (Arab).png"))
st_ay4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 4 Al -Fatihah (Arab).png"))
st_ay5= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 5 Al -Fatihah (Arab).png"))
st_ay6= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 6 Al -Fatihah (Arab).png"))
st_ay7= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Fatihah/Ayat 7 Al -Fatihah (Arab).png"))

label5 = Label(page5, image = bg5)
label5.grid(row = 0, column = 0,sticky = N)

satu1 = Button(page5, image=st_ay1, bg = "white", fg = "black")
satu1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 60)
satu1.bind("<FocusIn>", lambda e: satu1.configure(bg = "black", fg = "white"))
satu1.bind("<FocusOut>", lambda e: satu2.configure(bg = "white", fg = "black"))
satu1.bind("<Return>", frame6)

satu2 = Button(page5, image=st_ay2, bg = "white", fg = "black")
satu2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 95)
satu2.bind("<FocusIn>", lambda e: satu2.configure(bg = "black", fg = "white"))
satu2.bind("<FocusOut>", lambda e: satu2.configure(bg = "white", fg = "black"))

satu3 = Button(page5, image=st_ay3, bg = "white", fg = "black")
satu3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 130)
satu3.bind("<FocusIn>", lambda e: satu3.configure(bg = "black", fg = "white"))
satu3.bind("<FocusOut>", lambda e: satu3.configure(bg = "white", fg = "black"))

satu4 = Button(page5, image=st_ay4, bg = "white", fg = "black")
satu4.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 165)
satu4.bind("<FocusIn>", lambda e: satu4.configure(bg = "black", fg = "white"))
satu4.bind("<FocusOut>", lambda e: satu4.configure(bg = "white", fg = "black"))

satu5 = Button(page5, image=st_ay5, bg = "white", fg = "black")
satu5.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 200)
satu5.bind("<FocusIn>", lambda e: satu5.configure(bg = "black", fg = "white"))
satu5.bind("<FocusOut>", lambda e: satu5.configure(bg = "white", fg = "black"))

satu6 = Button(page5, image=st_ay6, bg = "white", fg = "black")
satu6.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 235)
satu6.bind("<FocusIn>", lambda e: satu6.configure(bg = "black", fg = "white"))
satu6.bind("<FocusOut>", lambda e: satu6.configure(bg = "white", fg = "black"))

satu7 = Button(page5, image=st_ay7, bg = "white", fg = "black")
satu7.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 270)
satu7.bind("<FocusIn>", lambda e: satu7.configure(bg = "black", fg = "white"))
satu7.bind("<FocusOut>", lambda e: satu7.configure(bg = "white", fg = "black"))

#=============Page6 Nas===================
bg6= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/an-nas 241x321.jpg"))
du_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nas/Ayat 1 An-Nas (Arab).png"))
du_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nas/Ayat 2 An-Nas (Arab).png"))
du_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nas/Ayat 3 An-Nas (Arab).png"))
du_ay4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nas/Ayat 4 An-Nas (Arab).png"))
du_ay5= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nas/Ayat 5 An-Nas (Arab).png"))
du_ay6= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nas/Ayat 6 An-Nas (Arab).png"))

label6 = Label(page6, image = bg6)
label6.grid(row = 0, column = 0,sticky = N)

dua1 = Button(page6, image=du_ay1, bg = "white", fg = "black")
dua1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 60)
dua1.bind("<FocusIn>", lambda e: dua1.configure(bg = "black", fg = "white"))
dua1.bind("<FocusOut>", lambda e: dua1.configure(bg = "white", fg = "black"))
dua1.bind("<Return>", frame7)

dua2 = Button(page6, image=du_ay2, bg = "white", fg = "black")
dua2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 100)
dua2.bind("<FocusIn>", lambda e: dua2.configure(bg = "black", fg = "white"))
dua2.bind("<FocusOut>", lambda e: dua2.configure(bg = "white", fg = "black"))

dua3= Button(page6, image=du_ay3, bg = "white", fg = "black")
dua3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 140)
dua3.bind("<FocusIn>", lambda e: dua3.configure(bg = "black", fg = "white"))
dua3.bind("<FocusOut>", lambda e: dua3.configure(bg = "white", fg = "black"))

dua4 = Button(page6, image=du_ay4, bg = "white", fg = "black")
dua4.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 180)
dua4.bind("<FocusIn>", lambda e: dua4.configure(bg = "black", fg = "white"))
dua4.bind("<FocusOut>", lambda e: dua4.configure(bg = "white", fg = "black"))

dua5 = Button(page6, image=du_ay5, bg = "white", fg = "black")
dua5.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 220)
dua5.bind("<FocusIn>", lambda e: dua5.configure(bg = "black", fg = "white"))
dua5.bind("<FocusOut>", lambda e: dua5.configure(bg = "white", fg = "black"))

dua6 = Button(page6, image=du_ay6, bg = "white", fg = "black")
dua6.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 260)
dua6.bind("<FocusIn>", lambda e: dua6.configure(bg = "black", fg = "white"))
dua6.bind("<FocusOut>", lambda e: dua6.configure(bg = "white", fg = "black"))

#=============Page7 Falaq===================
bg7= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al-falaq 241x321.jpg"))
ti_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Falaq/Ayat Al-Falaq (Arab).png"))
ti_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Falaq/Ayat 2 Al-Falaq (Arab).png"))
ti_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Falaq/Ayat 3 Al-Falaq (Arab).png"))
ti_ay4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Falaq/Ayat 4 Al-Falaq (Arab).png"))
ti_ay5= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Falaq/Ayat 5 Al-Falaq (Arab).png"))

label7 = Label(page7, image = bg7)
label7.grid(row = 0, column = 0,sticky = N)

tiga1 = Button(page7, image=ti_ay1, bg = "white", fg = "black")
tiga1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 60)
tiga1.bind("<FocusIn>", lambda e: tiga1.configure(bg = "black", fg = "white"))
tiga1.bind("<FocusOut>", lambda e: tiga1.configure(bg = "white", fg = "black"))
tiga1.bind("<Return>", frame8)

tiga2 = Button(page7, image=ti_ay2, bg = "white", fg = "black")
tiga2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 110)
tiga2.bind("<FocusIn>", lambda e: tiga2.configure(bg = "black", fg = "white"))
tiga2.bind("<FocusOut>", lambda e: tiga2.configure(bg = "white", fg = "black"))

tiga3 = Button(page7, image=ti_ay3, bg = "white", fg = "black")
tiga3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 160)
tiga3.bind("<FocusIn>", lambda e: tiga3.configure(bg = "black", fg = "white"))
tiga3.bind("<FocusOut>", lambda e: tiga3.configure(bg = "white", fg = "black"))

tiga4 = Button(page7, image=ti_ay4, bg = "white", fg = "black")
tiga4.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 210)
tiga4.bind("<FocusIn>", lambda e: tiga4.configure(bg = "black", fg = "white"))
tiga4.bind("<FocusOut>", lambda e: tiga4.configure(bg = "white", fg = "black"))

tiga5 = Button(page7, image=ti_ay5, bg = "white", fg = "black")
tiga5.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 260)
tiga5.bind("<FocusIn>", lambda e: tiga5.configure(bg = "black", fg = "white"))
tiga5.bind("<FocusOut>", lambda e: tiga5.configure(bg = "white", fg = "black"))

#=============Page8 Ikhlas===================
bg8= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al-ikhlas 241x321.jpg"))
em_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Ikhlas/Ayat 1 Al-Ikhlas (Arab).png"))
em_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Ikhlas/Ayat 2 Al-Ikhlas (Arab).png"))
em_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Ikhlas/Ayat 3 Al-Ikhlas (Arab).png"))
em_ay4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Ikhlas/Ayat 4 Al-Ikhlas (Arab).png"))

label8 = Label(page8, image = bg8)
label8.grid(row = 0, column = 0,sticky = N)

empat1 = Button(page8, image=em_ay1, bg = "white", fg = "black")
empat1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 60)
empat1.bind("<FocusIn>", lambda e: empat1.configure(bg = "black", fg = "white"))
empat1.bind("<FocusOut>", lambda e: empat1.configure(bg = "white", fg = "black"))
empat1.bind("<Return>", frame9)

empat2 = Button(page8, image=em_ay2, bg = "white", fg = "black")
empat2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 120)
empat2.bind("<FocusIn>", lambda e: em_ay2.configure(bg = "black", fg = "white"))
empat2.bind("<FocusOut>", lambda e: em_ay2.configure(bg = "white", fg = "black"))

empat3 = Button(page8, image=em_ay3, bg = "white", fg = "black")
empat3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 180)
empat3.bind("<FocusIn>", lambda e: empay3.configure(bg = "black", fg = "white"))
empat3.bind("<FocusOut>", lambda e: empat3.configure(bg = "white", fg = "black"))

empat4 = Button(page8, image=em_ay1, bg = "white", fg = "black")
empat4.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 240)
empat4.bind("<FocusIn>", lambda e: empat4.configure(bg = "black", fg = "white"))
empat4.bind("<FocusOut>", lambda e: empat4.configure(bg = "white", fg = "black"))

#=============Page9 Lahab===================
bg9= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al-lahab 241x321.jpg"))
li_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Lahab/Ayat 1 Al-Lahab (Arab).png"))
li_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Lahab/Ayat 2 Al-Lahab (Arab).png"))
li_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Lahab/Ayat 3 Al-Lahab (Arab).png"))
li_ay4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Lahab/Ayat 4 Al-Lahab (Arab).png"))
li_ay5= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al Lahab/Ayat 5 Al-Lahab (Arab).png"))

label9 = Label(page9, image = bg9)
label9.grid(row = 0, column = 0,sticky = N)

lima1 = Button(page9, image=li_ay1, bg = "white", fg = "black")
lima1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 60)
lima1.bind("<FocusIn>", lambda e: lima1.configure(bg = "black", fg = "white"))
lima1.bind("<FocusOut>", lambda e: lima1.configure(bg = "white", fg = "black"))
lima1.bind("<Return>", frame10)

lima2 = Button(page9, image=li_ay2, bg = "white", fg = "black")
lima2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 110)
lima2.bind("<FocusIn>", lambda e: lima2.configure(bg = "black", fg = "white"))
lima2.bind("<FocusOut>", lambda e: lima2.configure(bg = "white", fg = "black"))

lima3 = Button(page9, image=li_ay3, bg = "white", fg = "black")
lima3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 160)
lima3.bind("<FocusIn>", lambda e: lima3.configure(bg = "black", fg = "white"))
lima3.bind("<FocusOut>", lambda e: lima3.configure(bg = "white", fg = "black"))

lima4 = Button(page9, image=li_ay4, bg = "white", fg = "black")
lima4.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 210)
lima4.bind("<FocusIn>", lambda e: lima4.configure(bg = "black", fg = "white"))
lima4.bind("<FocusOut>", lambda e: lima4.configure(bg = "white", fg = "black"))

lima5 = Button(page9, image=li_ay5, bg = "white", fg = "black")
lima5.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 260)
lima5.bind("<FocusIn>", lambda e: lima5.configure(bg = "black", fg = "white"))
lima5.bind("<FocusOut>", lambda e: lima5.configure(bg = "white", fg = "black"))

#=============Page10 Nasr===================
bg10= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/an-nasr 241x321.jpg"))
en_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nasr/Ayat 1 An-Nasr (arab).png"))
en_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nasr/Ayat 2 An-Nasr (arab).png"))
en_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/An Nasr/Ayat 3 An-Nasr (arab).png"))

label10 = Label(page10, image = bg10)
label10.grid(row = 0, column = 0,sticky = N)

enam1 = Button(page10, image=en_ay1, bg = "white", fg = "black")
enam1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 70)
enam1.bind("<FocusIn>", lambda e: enam1.configure(bg = "black", fg = "white"))
enam1.bind("<FocusOut>", lambda e: enam1.configure(bg = "white", fg = "black"))
enam1.bind("<Return>", frame11)

enam2 = Button(page10, image=en_ay2, bg = "white", fg = "black")
enam2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 130)
enam2.bind("<FocusIn>", lambda e: enam2.configure(bg = "black", fg = "white"))
enam2.bind("<FocusOut>", lambda e: enam2.configure(bg = "white", fg = "black"))

enam3 = Button(page10, image=en_ay3, bg = "white", fg = "black")
enam3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 190)
enam3.bind("<FocusIn>", lambda e: enam3.configure(bg = "black", fg = "white"))
enam3.bind("<FocusOut>", lambda e: enam3.configure(bg = "white", fg = "black"))

#=============Page11 Kautsar===================
bg11= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/al-kausar 241x321.jpg"))
tu_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Kautsar/Ayat 1 Al-Kautsar (Arab).png"))
tu_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Kautsar/Ayat 2 Al-Kautsar (Arab).png"))
tu_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al-Kautsar/Ayat 3 Al-Kautsar (Arab).png"))

label11 = Label(page11, image = bg11)
label11.grid(row = 0, column = 0,sticky = N)

tuj1 = Button(page11, image=tu_ay1, bg = "white", fg = "black")
tuj1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 70)
tuj1.bind("<FocusIn>", lambda e: tuj1.configure(bg = "black", fg = "white"))
tuj1.bind("<FocusOut>", lambda e: tuj1.configure(bg = "white", fg = "black"))
tuj1.bind("<Return>", frame12)

tuj2 = Button(page11, image=tu_ay2, bg = "white", fg = "black")
tuj2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 130)
tuj2.bind("<FocusIn>", lambda e: tuj2.configure(bg = "black", fg = "white"))
tuj2.bind("<FocusOut>", lambda e: tuj2.configure(bg = "white", fg = "black"))

tuj3 = Button(page11, image=tu_ay3, bg = "white", fg = "black")
tuj3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 190)
tuj3.bind("<FocusIn>", lambda e: tuj3.configure(bg = "black", fg = "white"))
tuj3.bind("<FocusOut>", lambda e: tuj3.configure(bg = "white", fg = "black"))

#=============Page12 Ma'un===================
bg12= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/background al-maun 241x321.png"))
lap_ay1= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/1.png"))
lap_ay2= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/2.png"))
lap_ay3= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/3.png"))
lap_ay4= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/4.png"))
lap_ay5= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/5.png"))
lap_ay6= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/6.png"))
lap_ay7= ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Ayat Arab/Al maun/7.png"))

label12 = Label(page12, image = bg12)
label12.grid(row = 0, column = 0,sticky = N)

lap1 = Button(page12, image=lap_ay1, bg = "white", fg = "black")
lap1.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 65)
lap1.bind("<FocusIn>", lambda e: lap1.configure(bg = "black", fg = "white"))
lap1.bind("<FocusOut>", lambda e: lap1.configure(bg = "white", fg = "black"))
lap1.bind("<Return>", frame12)

lap2 = Button(page12, image=lap_ay2, bg = "white", fg = "black")
lap2.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 100)
lap2.bind("<FocusIn>", lambda e: lap2.configure(bg = "black", fg = "white"))
lap2.bind("<FocusOut>", lambda e: lap2.configure(bg = "white", fg = "black"))

lap3 = Button(page12, image=lap_ay3, bg = "white", fg = "black")
lap3.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 135)
lap3.bind("<FocusIn>", lambda e: lap3.configure(bg = "black", fg = "white"))
lap3.bind("<FocusOut>", lambda e: lap3.configure(bg = "white", fg = "black"))

lap4 = Button(page12, image=lap_ay4, bg = "white", fg = "black")
lap4.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 170)
lap4.bind("<FocusIn>", lambda e: lap4.configure(bg = "black", fg = "white"))
lap4.bind("<FocusOut>", lambda e: lap4.configure(bg = "white", fg = "black"))

lap5 = Button(page12, image=lap_ay5, bg = "white", fg = "black")
lap5.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 205)
lap5.bind("<FocusIn>", lambda e: lap5.configure(bg = "black", fg = "white"))
lap5.bind("<FocusOut>", lambda e: lap5.configure(bg = "white", fg = "black"))

lap6 = Button(page12, image=lap_ay6, bg = "white", fg = "black")
lap6.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 240)
lap6.bind("<FocusIn>", lambda e: lap6.configure(bg = "black", fg = "white"))
lap6.bind("<FocusOut>", lambda e: lap6.configure(bg = "white", fg = "black"))

lap7 = Button(page12, image=lap_ay7, bg = "white", fg = "black")
lap7.grid(row = 0, column = 0, sticky = N, padx = 0, pady = 275)
lap7.bind("<FocusIn>", lambda e: lap7.configure(bg = "black", fg = "white"))
lap7.bind("<FocusOut>", lambda e: lap7.configure(bg = "white", fg = "black"))

def btn1():
    button1.focus_set()
    #val=1
def btn2():
    button2.focus_set()
    #val=2
def btn3():
    button3.focus_set()
    #val=3

val=0
nilai=1
frameState=1

while True:
    input_value = gpio.input(20)
    input_value2 = gpio.input(21)
    input_value3 = gpio.input(16)
    input_value4 = gpio.input(26)
    
    if frameState==1:
        show_frame(page1)
        button1.focus()
        nilai=1
           
    if frameState==2:
        show_frame(page2)
        button3.focus()
        #frameState=frameState+1
        if nilai==1 :
            button2.focus()
        elif nilai==2 :
            button3.focus()
        else:
            nilai=1
        
    if frameState==3:
        show_frame(page3)
        button6.focus()
        if nilai==1 :
            button6.focus()
        elif nilai==2 :
            button7.focus()
        elif nilai==3 :
            button8.focus()
        elif nilai==4 :
            button9.focus()
        elif nilai==5 :
            button10.focus()
        elif nilai==6 :
            button11.focus()
        elif nilai==7 :
            button12.focus()
        elif nilai==8 :
            button13.focus()
       
        
    if frameState==4:
        show_frame(page4)
        button4.focus()
        if nilai==2 :
            button4.focus()
        elif nilai==3 :
            button5.focus()
        
       
    if not input_value:
        if val != input_value:
            nilai = nilai+1
            val = input_value
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    elif not input_value2:
        if val != input_value2:
            nilai = nilai-1
            val = input_value2
               
    elif not input_value3:
        if val != input_value3:
            frameState= frameState+nilai
            val = input_value3
            
    elif not input_value4:
        if val != input_value4:
            frameState= frameState-nilai
            val = input_value4
   
    else:
        val = input_value
        
    print(nilai,frameState,val)

    root.update()

root.mainloop()

'''
    state=0
    mainMenu =0
    subMenu1 =1
    subMenu2

    if state == mainMenu:
        mainMenuNilai

    elif state == subMenu1:
        subMenu1Nilai = subMenuNilai+1  ->tombol up/down
        subMeni1State = subMenu1Nilai -> tombol ok
        focus
        if SubMenu1State == subSub1menu
            subsubMenu1Nilai = subsubMenu1Nilai +1 ->up/down
            subsusubbMenu1State = subsubMenu1Nilai ->ok
            if subsusubbMenu1State == 
            subMenu1State-1  - tombol back
        state = state-1 ->tombol back

'''
