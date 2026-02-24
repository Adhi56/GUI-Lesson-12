from tkinter import *
import os
from gtts import gTTS

root = Tk()
root.geometry('400x400')
root.config(background='white')
root.title('text to speech converter')

def make_speech():
    language = 'en'
    myobj = gTTS(text = textentry.get(), lang = language, slow = False)
    myobj.save('texttospeech.wav')
    os.system('texttospeech.wav')


frame1 = Frame(root, background= 'pink', height = 150)
frame1.pack(fill = 'x')

title = Label(frame1, text = 'Text to Speech', bg = 'pink', fg = 'black', bd = 30, font = 'bold, 30')
title.place(x = 50, y = 70)

frame2 = Frame(root, background= 'light green',height = 250)
frame2.pack(fill = X)

textentry = Entry(frame2, background= 'black', fg = 'white', bd = 15)
textentry.place(x = 70, y = 30)

sumbitbutton = Button(frame2,text = 'SUMBIT', background= 'yellow', fg = 'black', bd = 20, command = make_speech)
sumbitbutton.place(x = 90, y = 100)




root.mainloop()