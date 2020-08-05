from tkinter import *
from Chat_Bank import *
from Chat import *

class Bt_with_variable():
    def __init__(self, variable = 0):
        super().__init__()

class Contatos(Frame):
    def __init__(self,user):
        super().__init__()
        self['height'] = 600
        self['width'] = 300
        def open_contact_mensage():
            Chat(user, f"{}").place(in_ = self,x = 0 , y =0)

        def Add():
            Add_contact(user,'Igor')

        def Att():
            Contatos(user).place(x = 201, y = 0)
            self.destroy()

        bt_new_contact = Button(self, text  = 'New contact', command = Add).grid(row = 0, column = 0)
        bt_att = Button(self, text  = 'Atualizar', command = Att).grid(row = 0, column = 1)
        
        for item in Chat_dados[user]['contatos']:
            item = Button(self, text = item, command = open_contact_mensage).grid()