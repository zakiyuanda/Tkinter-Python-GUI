from tkinter import *
from PIL import ImageTk, Image
import gpiozero #import Button        
from signal import pause
from time import sleep
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_UP)

root = Tk()
#global page1
page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)
page4 = Frame(root)

def dua(e):
    #global button2
    button2.focus_set()
    
def satu(e):
    #global button1
    button1.focus_set()
    
def tiga(e):
    button3.focus_set()

def empat(e):
    button4.focus_set()
    
def lima(e):
    button5.focus_set()

    
def klik(e):
    print("yasudahlah")

def show_frame(frame):
    frame.tkraise()
def frame1(e):
    show_frame(page1)
    button1.focus_set()
    
def frame2(e):
    show_frame(page2)
    button4.focus_set()
'''
def oke():
    button_next.wait_for_press()
    
    print("sip")
    button_next.wait_for_release()
'''

for frame in (page1, page2,page3,page4):
    frame.grid(row=0, column=0, sticky='nsew')
#sip = ImageTk.PhotoImage(Image.open("D:/File/Project/Afdhal/images/play.png"))  
#button1 = Button(root, image=sip )
#button1.place(x=0, y=0)
show_frame(page1)
btn1 = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/Fast/Images/button play 50x50V2.png"))  

button1 = Button(page1, text = "Button1", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button1.grid(row = 0, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button1.bind("<FocusIn>", lambda e: button1.configure(bg = "black", fg = "white"))
button1.bind("<FocusOut>", lambda e: button1.configure(bg = "white", fg = "black"))
button1.bind("<Down>", dua)
button1.bind("<Up>", tiga)

button1.focus_set() #Setting default focus to button1

button2 = Button(page1, text = "Button2", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button2.grid(row = 1, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button2.bind("<FocusIn>", lambda e: button2.configure(bg = "black", fg = "white"))
button2.bind("<FocusOut>", lambda e: button2.configure(bg = "white", fg = "black"))
button2.bind("<Down>",tiga)
button2.bind("<Up>",satu)
button2.bind("<Return>", frame2)

button3 = Button(page2, text = "Button3", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button3.grid(row = 0, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button3.bind("<FocusIn>", lambda e: button3.configure(bg = "black", fg = "white"))
button3.bind("<FocusOut>", lambda e: button3.configure(bg = "white", fg = "black"))
button3.bind("<Down>", lima)
button3.bind("<Return>",frame1)

#button1.focus_set() #Setting default focus to button1

button4 = Button(page2, text = "Button4", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button4.grid(row = 1, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button4.bind("<FocusIn>", lambda e: button4.configure(bg = "black", fg = "white"))
button4.bind("<FocusOut>", lambda e: button4.configure(bg = "white", fg = "black"))
button4.bind("<Up>",empat)

button5 = Button(page2, text = "Button5", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button5.grid(row = 2, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button5.bind("<FocusIn>", lambda e: button5.configure(bg = "black", fg = "white"))
button5.bind("<FocusOut>", lambda e: button5.configure(bg = "white", fg = "black"))
button5.bind("<Down>", satu)
button5.bind("<Up>",dua)

button6 = Button(page3, text = "Button6", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button6.grid(row = 0, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button6.bind("<FocusIn>", lambda e: button6.configure(bg = "black", fg = "white"))
button6.bind("<FocusOut>", lambda e: button6.configure(bg = "white", fg = "black"))
button6.bind("<Down>", lima)
button6.bind("<Return>",frame2)

button7 = Button(page3, text = "Button7", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button7.grid(row = 1, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button7.bind("<FocusIn>", lambda e: button7.configure(bg = "black", fg = "white"))
button7.bind("<FocusOut>", lambda e: button7.configure(bg = "white", fg = "black"))
button7.bind("<Up>",empat)

button8 = Button(page4, text = "Button8", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button8.grid(row = 0, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button8.bind("<FocusIn>", lambda e: button6.configure(bg = "black", fg = "white"))
button8.bind("<FocusOut>", lambda e: button6.configure(bg = "white", fg = "black"))
button8.bind("<Down>", lima)
button8.bind("<Return>",frame2)

button9 = Button(page4, text = "Button9", font = ('Comic Sans', 15, 'bold'), bg = "white", fg = "black")
button9.grid(row = 1, column = 0, sticky = NSEW, ipadx = 5, ipady = 2, padx = 5, pady = 5)
button9.bind("<FocusIn>", lambda e: button7.configure(bg = "black", fg = "white"))
button9.bind("<FocusOut>", lambda e: button7.configure(bg = "white", fg = "black"))
button9.bind("<Up>",empat)

#page1.update()
def btn1():
    button1.focus_set()
    #val=1
    #focus()
    #if 
        #break
def btn2():
    button2.focus_set()
    #focus()
    #val=2
    #if page1.focus_get=button2:
        #button_next.is_pressed
def btn3():
    button3.focus_set()
    #val=3
    #focus()
def enter():
    show_frame(page2)
    #break
def focus():
    global widget
    widget = root.focus_get()
    print(widget)

def tekan():
    button_next.wait_for_press()
    btn2()
    button_next.wait_for_release()
    
def tekan1():
    button_prev.wait_for_press()
    btn1()
    button_next.wait_for_release()

val=0
nilai=1
frameState=-1

frame0state = 0
frame1state = 0
frame2state = 0

subFrame0state=0
subFrame1state=0
subFrame2state=0
subsubFrame1state=0


while True:
    nextBtn = gpio.input(20) #up
    prevBtn = gpio.input(21) #down
    playBtn = gpio.input(16) #ok
    stopBtn = gpio.input(26) #back

    print(frameState,frame0state,frame1state,frame2state,subFrame0state,subFrame1state,subFrame2state,subsubFrame1state)
    if frameState==-1:
        show_frame(page1)
        button1.focus()
        
        if frame0state == 0:
            button1.focus()
        elif frame0state == 1:
            button2.focus()
        else:
            frame0state=1

        #handleButton
        
        if not nextBtn:
            if val!= nextBtn:
                frame0state = frame0state+1
                val = nextBtn
               
        elif not prevBtn:
            if val!= prevBtn:
                frame0state = frame0state-1
                val = prevBtn
        
        elif not playBtn:
            if val!= playBtn:
                frameState = frame0state
                val = playBtn
        
        else:
            val = nextBtn
        
    elif frameState ==0:
        if subFrame1state == 0:
            show_frame(page3)
            button6.focus()
            if frame1state == 0:
                button6.focus()
            elif frame1state == 1:
                button7.focus()
        
            #handleButton
            if not nextBtn:
                if val!= nextBtn:
                    frame1state = frame1state+1
                    val = nextBtn
            elif not prevBtn:
                if val!= prevBtn:
                    frame1state = frame1state-1
                    val = prevBtn
            elif not playBtn:
                if val!= playBtn:
                    subFrame1State = frame1state
                    val = playBtn
            elif not stopBtn:
                if val!= stopBtn:
                    frameState = -1
                    val = stopBtn

            else:
                val = nextBtn   

    elif frameState == 1:
        if subFrame2state == 0:
            show_frame(page2)
            button3.focus()
            if frame2state == 0:
                button3.focus()
            elif frame2state == 1:
                button4.focus()
            elif frame2state == 2:
                button5.focus()
        
            #handleButton
            if not nextBtn:
                if val!= nextBtn:
                    frame2state = frame2state+1
                    val = nextBtn
            elif not prevBtn:
                if val!= prevBtn:
                    frame2state = frame2state-1
                    val = prevBtn
            elif not playBtn:
                if val!= playBtn:
                    subframe2State = frame2state
                    val = playBtn
            elif not stopBtn:
                if val!= stopBtn:
                    frameState = -1
                    val = stopBtn

            else:
                val = nextBtn   

        elif subFrame2state == 1:
            show_frame(page4)
            button3.focus()
            if subsubframe2state == 0:
                button8.focus()
            elif subsubframe2state == 1:
                button9.focus()
           
            #handleButton
            if not nextBtn:
                if val!= nextBtn:
                    subsubframe2state = subbsubframe2state+1
                    val = nextBtn
            elif not prevBtn:
                if val!= prevBtn:
                    subsubframe2state = subsubframe2state-1
                    val = prevBtn
            else:
                val = nextBtn   
    '''
    if frameState==1:
        show_frame(page1)
        button1.focus()
        nilai=frameState+1
        if nilai==1 :
            button1.focus()
        elif nilai==2 :
            button2.focus()
       
    if frameState==2:
        show_frame(page2)
        button3.focus()
        #nilai=frameState+1
        if nilai==1 :
            button3.focus()
        elif nilai==2 :
            button4.focus()
        elif nilai==3 :
            button5.focus()
        else:
            nilai=2
       
    if frameState==3:
        show_frame(page3)
        button6.focus()
        if nilai==1 :
            button6.focus()
        elif nilai==2 :
            button7.focus()
       
       
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
    '''
    root.update()

root.mainloop()
