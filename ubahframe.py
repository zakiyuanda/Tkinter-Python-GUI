from tkinter import *
from PIL import ImageTk, Image
import pygame
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os
import sounddevice as sd
import soundfile as sf

root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("800x600")
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

for frame in (page1, page2, page3, page4,page5, page6,page7, page8,page9, page10,page11,page12):
    frame.grid(row=0, column=0, sticky='nsew')
    
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

def show_frame(frame):
    frame.tkraise()
def fatihah():
    pygame.mixer.music.load("audio/fatiha.mp3")
    pygame.mixer.music.play()
def naas():
    pygame.mixer.music.load("audio/naas.mp3")
    pygame.mixer.music.play()
def falaq():
    pygame.mixer.music.load("audio/falaq.mp3")
    pygame.mixer.music.play()
def ikhlas():
    pygame.mixer.music.load("audio/ikhlas.mp3")
    pygame.mixer.music.play()    
def nashr():
    pygame.mixer.music.load("audio/nasr.mp3")
    pygame.mixer.music.play()
def masad():
    pygame.mixer.music.load("audio/masad.mp3")
    pygame.mixer.music.play()
def kafirun():
    pygame.mixer.music.load("audio/kaferoon.mp3")
    pygame.mixer.music.play()
def kautsar():
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
    pg1_button.focus_set()
def frame2(e):
    show_frame(page2)
    tmp.focus_set()
def frame3(e):
    show_frame(page3)
    satu1.focus_set()
    pygame.mixer.music.stop()
def frame4(e):
    show_frame(page4)
    rec.focus_set()
def frame5(e):
    show_frame(page5)
    fatihah()
    layar5.focus_set()
def frame6(e):
    show_frame(page6)
    naas()
    layar6.focus_set()
def frame7(e):
    show_frame(page7)
    falaq()
    layar7.focus_set()
def frame8(e):
    show_frame(page8)
    ikhlas()
    layar8.focus_set()
def frame9(e):
    show_frame(page9)
    masad()
    layar9.focus_set()
def frame10(e):
    show_frame(page10)
    nashr()
    layar10.focus_set()
def frame11(e):
    show_frame(page11)
    kafirun()
    layar11.focus_set()
def frame12(e):
    show_frame(page12)
    kautsar()
    layar12.focus_set()
    
def satu(e):
    satu1.focus_set()
def dua(e):
    dua2.focus_set()
def tiga(e):
    tiga3.focus_set()
def empat(e):
    empat4.focus_set()
def lima(e):
    lima5.focus_set()
def enam(e):
    enam6.focus_set()
def tujuh(e):
    tujuh7.focus_set()
def lapan(e):
    lapan8.focus_set()
def btn1(e):
    tmp.focus_set()
def btn2(e):
    dtk.focus_set()
def spk_foc(e):
    spk.focus_set()
def rec_foc(e):
    rec.focus_set()

fnt=('Arial', 15, 'bold')

show_frame(page1)

# ============= Page 1 =========
login_btn=PhotoImage(file='Gambar/play.png')
bg = ImageTk.PhotoImage(Image.open("Gambar/menu 8x6.jpg"))  
layar1=Label(page1, image=bg)
layar1.place(x=0,y=0,relheight=1,relwidth=1)
pg1_button = Button(page1, image=login_btn )
pg1_button.place(x=350, y=300)
pg1_button.focus_set()
pg1_button.bind("<FocusIn>", lambda e: pg1_button.configure(bg = "black", fg = "#b9deee"))
pg1_button.bind("<FocusOut>", lambda e: pg1_button.configure(bg = "#b9deee", fg = "black"))
pg1_button.bind("<Return>",frame2)

# ======== Page 2 ===========
pag2_label = Label(page2, image=bg)
pag2_label.place(x=0,y=0,relheight=1,relwidth=1)

tmp = Button(page2, text='Tampilan Surah', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page3))
tmp.place(x=300, y=270)
tmp.bind("<FocusIn>", lambda e: tmp.configure(bg = "black", fg = "#b9deee"))
tmp.bind("<FocusOut>", lambda e: tmp.configure(bg = "#b9deee", fg = "black"))
tmp.bind("<Return>",frame3)
tmp.bind("<Down>",btn2)
tmp.bind("<Left>",frame1)

dtk = Button(page2, text='Deteksi Bacaan', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page4))
dtk.place(x=300, y=350)
dtk.bind("<FocusIn>", lambda e: dtk.configure(bg = "black", fg = "#b9deee"))
dtk.bind("<FocusOut>", lambda e: dtk.configure(bg = "#b9deee", fg = "black"))
dtk.bind("<Return>",frame4)
dtk.bind("<Up>", btn1)
dtk.bind("<Left>",frame1)

# ======== Page 3 ===========
bg3 = ImageTk.PhotoImage(Image.open("Gambar/surah 8x6.jpg"))  
pag3_label = Label(page3, image=bg3)
pag3_label.place(x=0,y=0,relheight=1,relwidth=1)

satu1 = Button(page3, text='Al-Fatihah', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page5))
satu1.place(width=150,x=200, y=200)
satu1.bind("<FocusIn>", lambda e: satu1.configure(bg = "black", fg = "#b9deee"))
satu1.bind("<FocusOut>", lambda e: satu1.configure(bg = "#b9deee", fg = "black"))
satu1.bind("<Down>", dua)
satu1.bind("<Up>", lapan)
satu1.bind("<Return>",frame5)
satu1.bind("<Left>",frame2)
dua2 = Button(page3, text='An-Nas', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page6))
dua2.place(width=150,x=200, y=270)
dua2.bind("<FocusIn>", lambda e: dua2.configure(bg = "black", fg = "#b9deee"))
dua2.bind("<FocusOut>", lambda e: dua2.configure(bg = "#b9deee", fg = "black"))
dua2.bind("<Down>", tiga)
dua2.bind("<Up>", satu)
dua2.bind("<Return>",frame6)
dua2.bind("<Left>",frame2)
tiga3 = Button(page3, text='Al-Falaq', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page7))
tiga3.place(width=150,x=200, y=340)
tiga3.bind("<FocusIn>", lambda e: tiga3.configure(bg = "black", fg = "#b9deee"))
tiga3.bind("<FocusOut>", lambda e: tiga3.configure(bg = "#b9deee", fg = "black"))
tiga3.bind("<Down>", empat)
tiga3.bind("<Up>", dua)
tiga3.bind("<Return>",frame7)
tiga3.bind("<Left>",frame2)
empat4 = Button(page3, text='Al-Ikhlas', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page8))
empat4.place(width=150,x=200, y=410)
empat4.bind("<FocusIn>", lambda e: empat4.configure(bg = "black", fg = "#b9deee"))
empat4.bind("<FocusOut>", lambda e: empat4.configure(bg = "#b9deee", fg = "black"))
empat4.bind("<Down>", lima)
empat4.bind("<Up>", tiga)
empat4.bind("<Return>",frame8)
empat4.bind("<Left>",frame2)
lima5 = Button(page3, text='Al-Lahab', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page9))
lima5.place(width=150,x=430, y=200)
lima5.bind("<FocusIn>", lambda e: lima5.configure(bg = "black", fg = "#b9deee"))
lima5.bind("<FocusOut>", lambda e: lima5.configure(bg = "#b9deee", fg = "black"))
lima5.bind("<Down>", enam)
lima5.bind("<Up>", empat)
lima5.bind("<Return>",frame9)
lima5.bind("<Left>",frame2)
enam6 = Button(page3, text='An-Nasr', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page10))
enam6.place(width=150,x=430, y=270)
enam6.bind("<FocusIn>", lambda e: enam6.configure(bg = "black", fg = "#b9deee"))
enam6.bind("<FocusOut>", lambda e: enam6.configure(bg = "#b9deee", fg = "black"))
enam6.bind("<Down>", tujuh)
enam6.bind("<Up>", lima)
enam6.bind("<Return>",frame10)
enam6.bind("<Left>",frame2)
tujuh7 = Button(page3, text='Al-Kafirun', font=fnt,bg = "#b9deee", fg = "black", command=lambda: [fatihah,show_frame(page12)])
tujuh7.place(width=150,x=430, y=340)
tujuh7.bind("<FocusIn>", lambda e: tujuh7.configure(bg = "black", fg = "#b9deee"))
tujuh7.bind("<FocusOut>", lambda e: tujuh7.configure(bg = "#b9deee", fg = "black"))
tujuh7.bind("<Down>", lapan)
tujuh7.bind("<Up>", enam)
tujuh7.bind("<Return>",frame11)
tujuh7.bind("<Left>",frame2)
lapan8 = Button(page3, text='Al-Kautsar', font=fnt,bg = "#b9deee", fg = "black", command=lambda: show_frame(page11))
lapan8.place(width=150,x=430, y=410)
lapan8.bind("<FocusIn>", lambda e: lapan8.configure(bg = "black", fg = "#b9deee"))
lapan8.bind("<FocusOut>", lambda e: lapan8.configure(bg = "#b9deee", fg = "black"))
lapan8.bind("<Down>", satu)
lapan8.bind("<Up>", tujuh)
lapan8.bind("<Return>",frame12)
lapan8.bind("<Left>",frame2)

# ======== Page 4 ===========
bg4 = ImageTk.PhotoImage(Image.open("Gambar/deteksi bacaan 8x6.jpg"))  
pag4_label = Label(page4, image=bg4)
pag4_label.place(x=0,y=0,relheight=1,relwidth=1)

ico_rec = ImageTk.PhotoImage(Image.open("Gambar/mic.png"))
ico_spk = ImageTk.PhotoImage(Image.open("Gambar/speak.png"))

txt_area = Entry(page4, font=('times new rommon',15,'bold'),  width=35, justify='center')
txt_area.place(x=200, y=250)
rec = Button(page4, image=ico_rec ,compound=LEFT, command=lambda e:clicked)
rec.place(x=350, y=400)
rec.bind("<FocusIn>", lambda e: rec.configure(bg = "black", fg = "#b9deee"))
rec.bind("<FocusOut>", lambda e: rec.configure(bg = "#b9deee", fg = "black"))
rec.bind("<Return>",voice_rec)
rec.bind("<Down>", spk_foc)
rec.bind("<Left>",frame2)
spk = Button(page4, image=ico_spk ,compound=LEFT, command=lambda e:clicked)
spk.place(x=350, y=500)
spk.bind("<FocusIn>", lambda e: spk.configure(bg = "black", fg = "#b9deee"))
spk.bind("<FocusOut>", lambda e: spk.configure(bg = "#b9deee", fg = "black"))
spk.bind("<Return>",clicked)
spk.bind("<Up>", rec_foc)
spk.bind("<Left>",frame2)

# ======== Page 5 ===========
bg5 = ImageTk.PhotoImage(Image.open("Gambar/al fatihah 8x6.jpg"))  
layar5=Label(page5, image=bg5)
layar5.place(x=0,y=0,relheight=1,relwidth=1)

pag5_label = Label(page5, text='Surah Al-Fatihah', font=fnt)
pag5_label.place(x=50, y=100)

pg5_button_on = Button(page5, text='Play', font=fnt, command=fatihah)
pg5_button_on.place(x=70, y=150)

pg5_button_off = Button(page5, text='Stop', font=fnt, command=stop)
pg5_button_off.place(x=140, y=150)
layar5.bind("<Left>",frame3)
# ======== Page 6 ===========
bg6 = ImageTk.PhotoImage(Image.open("Gambar/an-nas 8x6.jpg"))  
layar6=Label(page6, image=bg6)
layar6.place(x=0,y=0,relheight=1,relwidth=1)

pg6_button_on = Button(page6, text='Play', font=fnt, command=naas)
pg6_button_on.place(x=70, y=150)
pg6_button_off = Button(page6, text='Stop', font=fnt, command=stop)
pg6_button_off.place(x=140, y=150)
layar6.bind("<Left>",frame3)
# ======== Page 7 ===========
bg7 = ImageTk.PhotoImage(Image.open("Gambar/al-falaq 8x6.jpg"))  
layar7=Label(page7, image=bg7)
layar7.place(x=0,y=0,relheight=1,relwidth=1)
layar7.bind("<Left>",frame3)
pg7_button = Button(page7, text='Kembali', font=fnt, command=lambda: show_frame(page3))
pg7_button.place(x=300, y=350)
# ======== Page 8 ===========
bg8 = ImageTk.PhotoImage(Image.open("Gambar/al-ikhlas 8x6.jpg"))  
layar8=Label(page8, image=bg8)
layar8.place(x=0,y=0,relheight=1,relwidth=1)
layar8.bind("<Left>",frame3)
# ======== Page 9 ===========
bg9 = ImageTk.PhotoImage(Image.open("Gambar/al-lahab 8x6.jpg"))  
layar9=Label(page9, image=bg9)
layar9.place(x=0,y=0,relheight=1,relwidth=1)
layar9.bind("<Left>",frame3)
# ======== Page 10 ===========
bg10 = ImageTk.PhotoImage(Image.open("Gambar/an-nas 8x6.jpg"))  
layar10=Label(page10, image=bg10)
layar10.place(x=0,y=0,relheight=1,relwidth=1)
layar10.bind("<Left>",frame3)
# ======== Page 11 ===========
bg11 = ImageTk.PhotoImage(Image.open("Gambar/al-kafirun 8x6.jpg"))  
layar11=Label(page11, image=bg11)
layar11.place(x=0,y=0,relheight=1,relwidth=1)
layar11.bind("<Left>",frame3)
# ======== Page 12 ===========
bg12 = ImageTk.PhotoImage(Image.open("Gambar/al-kausar 8x6.jpg"))  
layar12=Label(page12, image=bg12)
layar12.place(x=0,y=0,relheight=1,relwidth=1)
layar12.bind("<Left>",frame3)

root.update()
root.mainloop()
