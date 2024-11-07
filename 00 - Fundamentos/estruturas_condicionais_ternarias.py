saldo = 2000
saque = 5000

status = "Sucesso" if saldo >= saque else "Falha" # Condição ternária: atribui "Sucesso" se saldo >= saque, caso contrário "Falha"
print (f"{status} ao realizar o saque!")