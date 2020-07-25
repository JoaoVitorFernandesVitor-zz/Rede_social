from tkinter import *
from Chat import *
from Login import *
from Window_chat import *
screen = Tk()
screen.geometry('600x500+250+250')

window_login = Login().grid()

screen.mainloop()