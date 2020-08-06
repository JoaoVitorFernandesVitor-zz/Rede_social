from tkinter import *
from Chat import *

class Bt_contact_chat(Button):
    def __init__(self, user, parent,
    variable = 0,
    text = '',
    font = 0,
    font_color = 0,
    image = 0):
        super().__init__()
        self['text'] = text
        if font != 0:
            self['font'] = font
        if font_color != 0:
            self['fg'] = font_color
        if image != 0:
            self['image'] = image
        self['width'] = 60



        def call_chat():
            Chat(user, variable).place(in_ = parent, x = 0, y = 0)

        self['command'] = call_chat