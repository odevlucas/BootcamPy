lista = [1, "Python", [40, 30, 20]]
print("Criei uma lista | lista = [1, \"Python\", [40, 30, 20]]:")

print("\nCopiei a lista dentro da lista2 com o | lista2=lista.copy():")
lista2 = lista.copy()

print("Lista1",lista)  # [1, "Python", [40, 30, 20]]
print("Lista2",lista2)

print("\nID lista1:",id(lista),"ID lista2:",id(lista2))

lista2.append(10)
print("\nAgora um exemplo de como é uma cópia, aqui, eu adicionei uma posição na lista2 | lista2.append(10):",lista2)