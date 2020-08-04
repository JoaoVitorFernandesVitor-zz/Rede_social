import json

def Create_Chat_dados():
    try:
        Chat_dados = {'Yuki':{'mensage_for_IA' :[
    ['Yuki','->Hi'],
    ['IA','->Helo']
    ]}
    }

        a = json.dumps(Chat_dados, indent = True)

        with open('Chat_dados.json', 'w+') as file:
            file.write(a)
        

    except:
        print("Não foi possivel Criar o arquivo Chat_dados.json")

def Add_mensage():
    try:
        news_dados = json.dumps(Chat_dados, indent = True) 
        with open('Chat_dados.json', 'w') as file:
            file.write(news_dados)
    except:
        print('Não foi possivel salvar as novas mensagens!')

#Verifica se arquivo ja existe.Se não existir o cria
try:
    open('Chat_dados.json','r')

except:
    Create_Chat_dados()

#Criando o dicionario com o Banco de dados do chat
with open('Chat_dados.json', 'r') as file:
    chat_text = file.read()
Chat_dados  = json.loads(chat_text)