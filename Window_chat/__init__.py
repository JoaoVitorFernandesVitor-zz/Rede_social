from Chat import *
from Perfil_Lateral import *
from Contatos_page import *

class window_chat(Frame):
    def __init__(self, user):
        super().__init__()
        Perfil_lateral(user).place(x = 0, y = 0)
        Contatos(user).place(x = 201, y = 0)