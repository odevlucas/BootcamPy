carros = ["gol", "celta", "palio"]

print("Percorrerá a lista printando os elementos usando o for carro in carros: print(carro)")
for carro in carros:
    print(carro)

print("Aqui será enumerado a lista, usando um indíce em \"for indice, carro in enumerate(carros): print (f\"{indice}:{carro}\")\"")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
