nome = "Lucas Silva"

print(nome[0], ": só o valor em zero")
print(nome[:9],": nesse caso, como não defini o inicio, ele trará do 0 até o 9")
print(nome[6:], ":aqui eu passei só o início, sendo 6, dessa forma ele trará do 6 até o final")
print(nome[5:10], ":aqui peguei a substring do inicio 5 e final 10")
print(nome[2:10:2], ": aqui coloquei o step, ele começará no 2 e irá até o 10, pulando o s")
print(nome[:],": sem start e final, traz tudo")
print(nome[::-1],": sem start e sem stop com o step -1")