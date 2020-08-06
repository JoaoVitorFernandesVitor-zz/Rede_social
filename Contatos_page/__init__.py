from tkinter import *
from Chat_Bank import *
from Chat import *
from Button_with_variable import *

class Contatos(Frame):
    def __init__(self,user):
        super().__init__()
        self['height'] = 600
        self['width'] = 300
        
        def Add():
            Add_contact(user,'Igor')

        def Att():
            Contatos(user).place(x = 201, y = 0)
            self.destroy()

        #bt_new_contact = Button(self, text  = 'New contact', command = Add).grid(row = 0, column = 0, sticky = W+E)
        #bt_att = Button(self, text  = 'Atualizar', command = Att).grid(sticky= W+E)
        
        for item in Chat_dados[user]['contatos']:
            Bt_contact_chat(user = user, parent = self ,variable = item, text = item).grid(in_ = self, sticky = W+E)