nome = "Lucas"
idade = 29
profissao = "Programador"
linguagem = "Python"
saldo = 55.55555

print(" Formato antigo (está em desuso) ".center(40,"#"))
print("Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
print()

print(" Formato format ".center(40,"#"))
print("Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print()

print(" Formato format 2.0 ".center(40,"#"))
print("Olá, me chamo {3}. Tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print()

print(" Formato f-string (o cara!) ".center(40,"#"))
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem} com um salário de {saldo:.2f}.")