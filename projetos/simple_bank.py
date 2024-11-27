def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}"
        print(f"\nDepósito realizado com sucesso! \nSeu novo saldo é de R$ {saldo:.2f}")
            
    else:
        print("\nO valor informado é inválido! Verifique o valor que você deseja depositar.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("\nNúmero de saques diários excedidos.\nPor favor, tente novamente amanhã.")
    else:          
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
            print(f"\nOperação realizada com sucesso! Seu novo saldo é de: R$ {saldo:.2f}\nVocê possui {limite_saques - numero_saques} saques disponíveis para hoje!")
    return saldo, extrato, numero_saques

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números, sem pontos):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco":endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, verifique novamente!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("*"*30)
        print(linha) 

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(30,"#"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print(30 * "#")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada")

main()