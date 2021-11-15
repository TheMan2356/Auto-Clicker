import pyautogui
from tkinter import *

App = Tk()
App.title("Auto Clicker")

def Action():
    while True:
        pyautogui.PAUSE = 0.01
        pyautogui.click()

def Stop():
    App.quit()

Btn = Button(App, text="Start", background="black", fg="white", borderwidth=0, command=Action)
Btn.pack(pady=10)

Btn2 = Button(App, text="Stop", background="black", fg="white", borderwidth=0, command=Stop)
Btn2.pack(pady=10)

App.mainloop()