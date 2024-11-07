saldo = 500

def sacar(valor):
    global saldo
    if saldo >= valor: #quatro espaços
        print("Valor sacado!") #quatro espaços em relação à condição e oito em relação ao método
        print("Retire o seu dinheiro no ATM.\n")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    global saldo
    saldo += valor

depositar(500)
sacar(1000)