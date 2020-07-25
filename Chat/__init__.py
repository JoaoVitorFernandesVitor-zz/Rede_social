from tkinter import *
Chat_dados = {'Yuki':{'mensage_for_IA' :[
    ['Yuki','->Hi'],
    ['IA','->Helo']
]
}}
class Chat(Frame):
    def __init__(self,user):
        super().__init__()
        #Propriedades do Frame do Chat
        self['bd']= 5
        self['relief'] = RIDGE
        self['bg'] = '#00664b'
        
        def Send():
            text_chat['state'] = NORMAL
            text_send = f'{user}->{entry_chat.get()}\n'
            text_chat.insert(END,text_send)
            try:
                Chat_dados[user]['mensage_for_IA'] += [user,f'->{entry_chat.get()}']
                
            except:
                Chat_dados[user] = {'mensage_for_IA': []}
            text_chat['state'] = DISABLED
            
        
        #Widgets internos
        title_chat = Label(self, text = 'Fon Chat' , font = 'System 20' , bg = '#02e0a6')
        text_chat = Text(self,bg = '#79d9c0' , width = 60, state = DISABLED , bd = 5, relief = GROOVE) 
        entry_chat = Entry(self,bg = '#66b39f' , bd = 4 , relief = RIDGE)
        send_button = Button(self, text = 'Send', bg = '#02e0a6', bd = 5,  command = Send)
    
        #Widgets Grids
        title_chat.grid(row = 0 , column = 0, columnspan = 2, sticky = W+E)
        text_chat.grid(row = 1 , column = 0, columnspan = 2)
        entry_chat.grid(row = 2, ipadx = 100, ipady = 5, sticky = W+E+N+S)
        send_button.grid(row = 2, column = 1 , ipadx = 5 , ipady = 5 , sticky = W+E)

        text_chat['state'] = NORMAL
        for item in  Chat_dados[user]['mensage_for_IA']:
            if item[0] == user:
                text_chat.insert(END,f'{item[0]}{item[1]}\n'.replace("'",'').replace(']',"").replace('[','').replace(',',''))
            else:
                continue
        text_chat['state'] = DISABLED