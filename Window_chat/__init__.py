from Chat import *

class window_chat(Frame):
    def __init__(self, user):
        super().__init__()
        Chat(user).grid()