from Chat import *
from Perfil_Lateral import *

class window_chat(Frame):
    def __init__(self, user):
        super().__init__()
        Perfil_lateral(user).place(x = 0, y = 0)
        Chat(user).place(x = 201, y = 0)