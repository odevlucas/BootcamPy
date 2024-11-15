matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print((matriz[0]), "- Aqui trará somente a primeira linha: matriz[0]")  # [1, "a", 2]
print((matriz[0][0]), "- Aqui trará somente o valor da primeira linha e primeira coluna: matriz[0][0]")  # 1
print((matriz[0][-1]), "- Aqui trará somente o valor da primeira linha e de da última coluna: matriz[0][-1]")  # 2
print((matriz[-1][-1]), "- Aqui trára somente o valor da última linha e da última coluna: matriz[-1][-1]")  # "c"
