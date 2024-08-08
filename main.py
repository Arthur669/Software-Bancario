def login_adm():
 user_name = input("digite o nome de usuario:")
 if user_name == "admin":
    print("continue!")
 else: print("continue")
 password = input("digite a senha:")
 if password == "#$AR;<|#YqkHB&p4BpZ2ZL9+pCuez*R":
    print("Fazendo escaneamento dos dados inseridos!")
 else: print("Fazendo escaneamento dos dados inseridos!")
 if user_name == "admin" and password == "#$AR;<|#YqkHB&p4BpZ2ZL9+pCuez*R":
    print("Sucesso login concluido")
 else:
  print("ERRO!!!")
  exit()

def cotações():
  print("Rank Criptomoeda Símbolo Preço (USD) Capitalização de Mercado(USD) Volume nas 24h(USD) Variação nas 24h(%)")
  print("1-Bitcoin-BTC-30,000.00-600,000,000,000-25,000,000,000-2.5")
  print("-------------------------------------------------------------------------------------")
  print("2-Ethereum-ETH-2,000.00-240,000,000,000-15,000,000,000-1.8")
  print("-------------------------------------------------------------------------------------")
  print("3-BinanceCoin-BNB-300.00-50,000,000,000 2,000,000,000	3.2")
  print("-------------------------------------------------------------------------------------")
  print("4-Tether-USDT-1.00-70,000,000,000-50,000,000,000-0.0")
  print("-------------------------------------------------------------------------------------")
  print("5-Cardano-ADA-1.20-38,000,000,000-3,000,000,000-2.1")
  print("-------------------------------------------------------------------------------------")
  print("6-XRP XRP-0.80-35,000,000,000-4,000,000,000-1.7")
  print("-------------------------------------------------------------------------------------")
  print("7-Solana-SOL-35.00-10,000,000,000-1,500,000,000-4.5")
  print("-------------------------------------------------------------------------------------")
  print("8-Polkadot-DOT-25.00-25,000,000,000-2,000,000,000-3.0")
  print("-------------------------------------------------------------------------------------")
  print("9-Dogecoin-DOGE-0.30-40,000,000,000-3,500,000,000-2.8")
  print("-------------------------------------------------------------------------------------")
  print("10-USD-Coin-USDC-1.00-55,000,000,000-30,000,000,000-0.0")
  print("-------------------------------------------------------------------------------------")


def chatbotdeinvestimentos():
   comandoschatbot = input("ola eu sou o seu chatbot de investimentos o que voce quer? 1-ver analise das minhas açoes\n"
   "2-ver analise das minhas criptos 3-analisar cripto em especifico ou ação")
   if comandoschatbot == "1":
    print("Suas ações estão estaveis")
   if comandoschatbot == "2":
    print("Suas criptos estão estaveis")
   if comandoschatbot == "3":
     input("digite o simbolo da ação ou cripto")
     print("esse ativo é altamente valorizado e seu preço esta estavel")
   

def cadastros():
  print("Bem vindo(a) a parte de cadastro!")
  name = input("Digite seu nome:")
  password = input("Digite sua senha:")
  email = input("Digite seu email:")

def logincliente():
  while True:
   name_user = input("digite seu nome de usuario:")
   email_user = input("digite seu email:")
   user_password = input("digite sua senha:")
   print("Sucesso")
   comandos = input("o que você deseja fazer? 1-ver saldo 2-Fazer uma transferencia 3-Ver historico das minhas atividades 4-Ver meu id")
   if comandos == "1":
     print("Seu saldo é:R$10.000,00")
   if comandos == "2":
     transferencia = input("Quanto você quer transferir e qual é o id da pessoa?")
     print("Transferencia concluida")
   if comandos == "3":
     print("Serviço indisponivel")
   if comandos == "4":
     print("43437667876687")




 
#-----------CODIGO ABAIXO É A PARTE QUE O USUARIO USA E ACIMA AS FUNÇÕES ETC----------------


while True:
  print("1-logar como adm 2-ver cotações da bolsa de cripto 3-logar na sua conta"
       "4-conversar com o chatbot 5-cadastrar")
  inicio = input("digite a opção que preferir:")
  if inicio == "1":
   login_adm()
  if inicio == "2":
   cotações()
  if inicio == "3":
    logincliente()
  print("acesso liberado!")
  if inicio == "4":
   chatbotdeinvestimentos()
  if inicio == "5":
   cadastros()
