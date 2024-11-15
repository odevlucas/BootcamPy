linguagens = ["python", "js", "c", "java", "csharp", "python"]

print("Com o método .index(\"valor\") mostraremos em qual índice está o valor buscado, exemplo | linguagems = [\"python\",\"js\",\"c\",\"java\",\"csharp\",\"python\"])")
print("java:", linguagens.index("java"))  # 3
print("python:", linguagens.index("python"))  # 0
print("##### Perceba que trouxe apenas o primeiro resultado encontrado para Py, sendo que ele estava na posição 0 e 5 #####")
print("csharp:", linguagens.index("csharp"))  # 4

print("\nPara solucionar o problema de trazer apenas o primeiro índice, você poderá usar uma compressão de lista:")
print("\nindices_python = [i for i, x in enumerate(linguagens) if x == \"python\"]")
indices_python = [i for i, x in enumerate(linguagens) if x == "python"]
print(indices_python)