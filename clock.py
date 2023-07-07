from tkinter import *
from tkinter.ttk import *

from time import strftime

#creating instance of tkinter frame
root = Tk()

#assigning title
root.title("Clock")

#funtion to display time in HH:MM:SS am/pm
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
# creating widget
label = Label(root, font=("DS-Digital", 80),background= "#e0ccff",foreground='#8c07dd')
label.pack(anchor='center')

time()
mainloop()
