import tkinter as tk
from gtts import gTTS
from playsound import playsound

win = tk.Tk()
win.title("Text to Speech")
win.geometry("300x200")

def text_to_speech():
    text = entry.get()
    speech = gTTS(text=text,lang="en")
    entry.delete(0,'end')
    speech.save(r'D:\Coding_warriors\Text_to_speech\coding_warriors.mp3')
    playsound(r'D:\Coding_warriors\Text_to_speech\coding_warriors.mp3')


label = tk.Label(win,text="Enter text Here:")
label.place(x=110,y=10)

entry = tk.Entry(win,width=25,font=('Helvetica',15))
entry.place(x=10,y=30)

button = tk.Button(win,text="Speak",width=10,command=text_to_speech)
button.place(x=110,y=150)


win.mainloop()
