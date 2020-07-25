from tkinter import * 

#Entrada de texto com validação para senhas
class entry_Valition(Entry):
    """Fucao com base na Entry padrao incrementada com uma funcao de validacao
    - Parametros Shows
        Pode setar um texto,font e cor para aparecer antes da entry ganhar o foco
    
    - Parametros font e fontcollor
        Pode setar uma font e cor diferentes das padroes
    
    -Validar
        Na fucao verifica se o texto possui:
            -Letras maiusculas e minusculas
            -Numeros
            -Caracteres especiais(opcional)
                Se setar na invocacao da classe caracter = False desativa 
                a verificacao desse item.Por padrao o valor e True
    """
        
    def __init__(self, parent,
    show_text = '',# texto q vai aparecer enquanto nao se digita nd
    show_font = '',
    show_fg = '',
    font = '',
    fontcollor = '',
    font_default = 'Arial 8', fg_default = '#000000',
    fail = '',
    valider = False,
    caracter = True,
    name = '' #Nome para formatação Ex: User ou Password
):  
        super().__init__()
        #Propriedades da entry
        self.name = name
        self.fail = fail
        self.valider = valider
        self.caracter = caracter
        self.font = font
        self.fontcollor = fontcollor
        self.show_text = show_text
        self.show_fg = show_fg

        if show_font != '':
            self['font']= show_font

        if show_fg != '':
            self['fg']= show_fg


        self.insert(0, show_text)#Cria o texto na entry
        #Show delet
        def del_show():
            self.delete(0, END)
            #Altera a fonte para a padrao  ou o indicada
            if font != '':
                self['font'] = font

            else:
                self['font'] = font_default

            if fontcollor != '':
                self['fg']= fontcollor
            
            else:
                self['fg'] = fg_default


        self['validate'] = 'focusin'
        self['vcmd'] = del_show
        
        #Grid
        self.grid(in_ = parent)
        

    def Validar(self, min = 8, max = 100):
        texto = self.get()
        #Reporta se estiver em branco
        if texto == '':
            self.fail = f'{self.name} em braco não é valido!'
            self.valider = False

        else:            
            #Reporta se estiver abaixo do min de digitos
            if len(texto) < min :
                self.fail = f'{self.name} deve conter no min {min} digitos!'
                self.valider = False

            else:
                #Reporta se estiver acima do max de digitos
                if len(texto) > max:
                    self.fail = f'{self.name} deve conter no max {max} digitos!'
                    self.valider = False

                else:
                    alpha  = texto.isalpha()
                    #Verifica se não ha somente letras
                    if alpha == False:
                        self.fail = f'{self.name} deve conter letras e números!' 
                        digit = texto.isdigit()                            
                        #Verifica se não ha somente números
                        if digit == False:
                            self.fail = f'{self.name} deve conter letras maiúsculas e minúnusculas!'
                            upper = texto.isupper()                                
                            #Verifica se não ha somente letras maiúsculas
                            if upper == False:
                                self.fail = f'{self.name} deve conter letras minúsculas!'  
                                lower = texto.islower()
                                #Verifica se não ha somente letras minúsculas
                                if lower == False :

                                    if self.caracter :
                                        self.fail = f'{self.name} deve conter caracteres especiais!'  
                                        alphanum = texto.isalnum()          
                                        #Verifica se não conter caracteres especiais
                                        if alphanum == False :
                                            self.fail = f'{self.name} é valido'
                                            self.valider = True
                                    
                                    else:
                                        self.fail = f'{self.name} é valido'
                                        self.valider = True
                    else:
                        self.fail = f'{self.name} deve conter letras maiúsculas e minúsculas,\n números e caractere especiais!'
                        self.valider = False

                