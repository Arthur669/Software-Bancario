def login_adm():
 user_name = input("digite o nome de usuario:")
 if user_name == "Arthur Victor":
    print("continue!")
 else: print("continue")
 password = input("digite a senha:")
 if password == "#$AR;<|#YqkHB&p4BpZ2ZL9+pCuez*R":
    print("Fazendo escaneamento dos dados inseridos!")
 else: print("Fazendo escaneamento dos dados inseridos!")
 if user_name == "Arthur Victor" and password == "#$AR;<|#YqkHB&p4BpZ2ZL9+pCuez*R":
    print("Sucesso login concluido")
 else: 
  print("ERRO!!!")
  exit()

def cotações():
  print("Rank Criptomoeda Símbolo Preço (USD) Capitalização de Mercado(USD) Volume nas 24h(USD) Variação nas 24h(%)")
  print("1-Bitcoin-BTC-30,000.00-600,000,000,000-25,000,000,000-2.5")
  print("2-Ethereum-ETH-2,000.00-240,000,000,000-15,000,000,000-1.8")
  print("3-BinanceCoin-BNB-300.00-50,000,000,000 2,000,000,000	3.2")
  print("4-Tether-USDT-1.00-70,000,000,000-50,000,000,000-0.0")
  print("5-Cardano-ADA-1.20-38,000,000,000-3,000,000,000-2.1")
  print("6-XRP XRP-0.80-35,000,000,000-4,000,000,000-1.7")
  print("7-Solana-SOL-35.00-10,000,000,000-1,500,000,000-4.5")
  print("8-Polkadot-DOT-25.00-25,000,000,000-2,000,000,000-3.0")
  print("9-Dogecoin-DOGE-0.30-40,000,000,000-3,500,000,000-2.8")
  print("10-USD-Coin-USDC-1.00-55,000,000,000-30,000,000,000-0.0")

while True:
 print("1-logar como adm 2-ver cotações da bolsa de cripto 3-logar na sua conta")
 inicio = input("digite a opção que preferir:")
 if inicio == "1":
   login_adm()
 if inicio == "2":
   cotações()
