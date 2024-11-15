# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
print("Foi gerado uma lista de 7 posições [1, 30, 21, 2, 9, 65, 34]")
pares = [numero for numero in numeros if numero % 2 == 0]
print("\nFoi criado uma nova lista, compressada, chamada pares, onde há um iteração que guardará o valor nessa nova lista se o \"numero for numero in numeros\" se \"if\" for módulo da divisão por 2 for = 0 \"numero %2 ==0\" ")
print("\nNova lista com a compressão do módulo:",pares)

# Modificar valores
print("\nLista com modificação dos valores, elevando ao quadrado: quadrado = [numero**2 for numero in numeros]:")
quadrado = [numero**2 for numero in numeros]
print(quadrado)
