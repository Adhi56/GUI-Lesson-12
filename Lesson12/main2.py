from tkinter import *
import os
from gtts import gTTS

root = Tk()
root.geometry('300x300')
root.title('Greeter')
root.config(background='white')

def good_morning():
    lang = 'en'
    text = 'Good Morning, have a nice day!'
    myobj = gTTS(text = text, lang = lang, slow = False)
    myobj.save('greeting.wav')
    os.system('greeting.wav')

frame = Frame(root, background='white')
frame.pack()

label = Label(frame, text = 'Click the button to hear a greeting', bg = 'white', fg = 'black', bd = 20)
label.pack(side='top')

button = Button(frame, text= 'Say Good Morning', fg = 'black', bg = 'white', bd = 20, command = good_morning)
button.pack()





root.mainloop()