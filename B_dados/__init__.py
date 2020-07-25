import json 
#Cria o Banco de dados em .json
def Create():
    try :
        B_dados ={
        'Yuki':
            {'senha': '1234',
             'privileges' : 'adm'}

        }
        a = json.dumps(B_dados, indent = True)
        
        with open('B_dados.json', 'w+') as file:
            file.write(a)   
    
    except:
        print("Nao foi possivel criar Banco de dados")   

#Função para se escrever no Aquivo
def Add_user():
    try:
        texto = json.dumps(B_dados, indent = True)
        with open('B_dados.json', 'w+') as file :
            file.write(texto)

    except:
        print('Falha na escrita no Banco de dados')

#Verifica se o aquivo ja existe
try:
    open('B_dados.json', 'r')

except(FileNotFoundError):
    Create()

#Cria o dicionario do banco de dados
with open('B_dados.json', 'r') as file :
    texto = file.read()
B_dados = json.loads(texto)
