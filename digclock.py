import time

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *

def tick(time1=''):
    time2 = time.strftime("%H:%M:%S")
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)

root = Tk()
clock = Label(root, font=('verdana', 100, 'bold'), bg = '#33CA7F')
clock.pack(fill='both', expand = 1)

tick()

root.mainloop()
