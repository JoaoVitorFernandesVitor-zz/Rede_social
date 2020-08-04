from tkinter import *
from B_dados import *

class Perfil_lateral(Frame):
    def __init__(self, user):
        super().__init__()
        self['height'] = 600
        self['width'] = 200
        self['bg'] = 'gray'
        perfil_image = PhotoImage(file = 'Image_perfil.png')

        P_image = Label(self, image = perfil_image, bd = 5, relief = RIDGE, height = 200, width = 180)
        P_image.image = perfil_image
        P_image.place(x = 5, y = 0)

        P_info = Text(self, height = 10, width = 23, font = 'Arial 10', bd = 5, relief = RIDGE)
        P_info.place(x = 5, y = 210)
        
        #inserindo dados pessoais abaixo da foto do perfil
        P_dados = [f"Idade - {B_dados[user]['idade']}", f"Sexo - {B_dados[user]['sexo']}", f"Profissão - {B_dados[user]['profissao']}", f"Status civil - {B_dados[user]['status_civil']}"]
        
        for c in P_dados:
            P_info.insert(END,f"{c}\n")
        P_info['state'] = DISABLED