import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle


# Enabling High DPI Awareness
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Tkinter app properties
root = tk.Tk()
theme = ThemedStyle(theme="breeze")
root.title('Text to Speech v1.0.1')
root.resizable(False, False)
root.geometry('560x240')
root.wm_iconbitmap(r'favicon.ico')
name = tk.StringVar()

top_frame = Frame(root, width=450, height=50, pady=3)
center_frame = Frame(root, width=450, height=50, pady=3)
bottom_frame = Frame(root, width=450, height=50, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center_frame.grid(row=3, sticky="ew")
bottom_frame.grid(row=4, sticky="ns")


l1 = ttk.Label(top_frame, text='Enter the Text')
Msg = StringVar()


#e1 = ttk.Entry(center_frame, textvariable=Msg, width='50')
e1 = Text(center_frame, height=5, width=59, bg='white')


def text_to_speech():
    message = e1.get("1.0","end")
    speech = gTTS(text=message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    os.remove('DataFlair.mp3')


def exit_w():
    root.destroy()


def reset_w():
    Msg.set("")


btn1 = ttk.Button(bottom_frame, text='Play', command=text_to_speech)
btn2 = ttk.Button(bottom_frame, text='Exit', command=exit_w)
btn3 = ttk.Button(bottom_frame, text='Clear', command=reset_w)


l1.grid(row=0, column=0, pady=10, padx=10)
e1.grid(row=1, column=0, pady=10, padx=10)
btn1.grid(row=2, column=0, pady=10, padx=10)
btn2.grid(row=2, column=1, pady=10, padx=10)
btn3.grid(row=2, column=2, pady=10, padx=10)


root.mainloop()
