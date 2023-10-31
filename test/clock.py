from tkinter import *
from  time import *

def update():
    time_string=strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    time_label.after(1000, update)

win=Tk()

time_label=Label(win,font=("Arial",50),bg="yellow")
time_label.pack()
day_label=Label(win,font=("Arial",50))
day_label.pack()
date_label=Label(win,font=("Arial",50))
date_label.pack()
update()
win.mainloop()