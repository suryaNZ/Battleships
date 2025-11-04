from tkinter import *
import threading
import time
import requests

def mainerloop(window):
    while True:
        window.update()

class Receiver:
    def __init__(self, serverURL):
        self.waiting = True
        self.serverURL = serverURL

        # window = Tk()
        # window.overrideredirect(True)
        # self.label = Label(text="waiting", background="red")
        # self.label.pack()
        # threading.Thread(target=mainerloop(window=window))
        # mainloop()
    
    def wait(self):
        window = Tk()
        window.overrideredirect(True)
        self.label = Label(text="waiting", background="red")
        self.label.pack()
        stime = time.time()
        while(time.time()-stime < 5):
            # window.update_idletasks()
            window.update()
        window.destroy()
        