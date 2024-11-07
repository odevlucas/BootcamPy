conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2450
cheque_especial = 450

if conta_normal:
    if saldo >= saque: #Uma condição dentro de outra condição!
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial.")
    else:
        print("Saldo insuficiente para a operação!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("O sistema não reconheceu seu tipo de conta, entre em contato com o gerente da sua conta!")