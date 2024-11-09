menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"
            print(f"\nDepósito realizado com sucesso! \nSeu novo saldo é de R$ {saldo:.2f}")
        
        else: print("\nO valor informado é inválido! Verifique o valor que você deseja depositar.")

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("\nNúmero de saques diários excedidos.\nPor favor, tente novamente amanhã.")
        else:
            valor = float(input("Informe o valor do saque: R$ "))
            
            if valor <= 0:
                print("Operação falhou! O valor do saque deve ser maior que R$ 0.")
            elif valor > limite:
                print(f"\nValor excede o limite diário de: R$ {limite:.2f}")
            elif valor > saldo:
                print(f"\nSaldo insuficiente para a operação!\nSeu saldo é de: R$ {saldo:.2f}")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"\nSaque: R$ {valor:.2f}"
                print(f"\nOperação realizada com sucesso! Seu novo saldo é de: R$ {saldo:.2f}\nVocê possui {LIMITE_SAQUES - numero_saques} saques disponíveis para hoje!")
    
    elif opcao == "3":
        print("EXTRATO".center(30,"#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print(30 * "#")
    
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")