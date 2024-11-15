print("O .sort() é responsável pela ordenação do conteúdo")
linguagens = ["python", "js", "c", "java", "csharp"]
print("\nLista: linguagens = [\"python\", \"js\", \"c\", \"java\", \"csharp\"]")

linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print("\nOrdenação alfabética | linguagens.sort():",linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print("\nOrdenação em ordem alfabética decrescente | linguagens.sort(reverse=True):", linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print("\nOrdenação por tamanho da palavra \"do menor para maior\" | linguagens.sort(key=lambda x: len(x)):",linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print("\nOrdenação por tamanho da palavra \"do maior para o menor\" | linguagens.sort(key=lambda x: len(x), reverse=True):", linguagens)
