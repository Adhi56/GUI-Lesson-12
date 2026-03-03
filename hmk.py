from tkinter import *
import os
from gtts import gTTS

root = Tk()
root.geometry('400x400')
root.config(background='white')
root.title('French Pronouncer')

def make_speech():
    language = 'fr'
    myobj = gTTS(text=textentry.get(), lang=language, slow=False)
    myobj.save('frenchspeech.mp3')
    os.system('frenchspeech.mp3')

frame1 = Frame(root, background='pink', height=150)
frame1.pack(fill='x')

title = Label(frame1, text='French Pronouncer', bg='pink', fg='black', bd=30, font='bold, 30')
title.place(x=50, y=70)

frame2 = Frame(root, background='light green', height=250)
frame2.pack(fill=X)

label = Label(frame2, text='Enter text in French:', bg='light green', fg='black')
label.place(x=70, y=5)

textentry = Entry(frame2, background='black', fg='white', bd=15)
textentry.place(x=70, y=30)

submitbutton = Button(frame2, text='Speak in French', background='yellow', fg='black', bd=20, command=make_speech)
submitbutton.place(x=90, y=100)

root.mainloop()