from tkinter import *
from Entry_Validater import *
from B_dados import *
from Window_chat import *

class Login(Frame):
    def __init__(self):
        super().__init__()
        #Variables
        error_text = StringVar()
        image_ = PhotoImage(file = 'RIP_small.png')

        #Fução que verifica se o usuario ja existe
        def __login__():
            user = user_entry.get()
            user_pass = password_entry.get()
            if user in B_dados:
                if user_pass == B_dados[user]['senha']:
                    self.destroy()
                    window_chat(user).grid()          
                else:
                    error_text.set('Senha Incoreta')
            else:
                error_text.set('Usuario não existe')
                #Colocar aqui pagina para registro
            
        
        #Widgets da tela de Login
        logo_image = Label(self, image = image_)
        logo_image.image = image_
        
        error_mensager = Label(self, textvariable  = error_text, fg = 'red')

        user_text = Label(self, text = 'User')
        user_entry = Entry(self)
        
        password_text = Label(self, text = 'Password')
        password_entry = entry_Valition(self, name = 'Password')

        enter_bt = Button(self, text = 'Login', command = __login__)

        #Grids da tela de login
        logo_image.grid(row = 0 , column = 0, columnspan = 2, sticky = W+E+N+S)

        error_mensager.grid(row = 1, columnspan = 5, column = 0)
        
        user_text.grid(row = 2, column = 0)
        user_entry.grid(row = 2, column = 1)

        password_text.grid(row = 3, column = 0)
        password_entry.grid(row = 3, column = 1)

        enter_bt.grid(row = 4 , columnspan = 2, column = 0, sticky = W+E)

