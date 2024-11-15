print("O extend fará um merge de uma lista com uma nova lista.")
linguagens = ["python", "js", "c"]

print("\nAqui defini a lista linguagens, com os seguintes valores:", linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])
print("\nAqui eu passei o método extende na lista anterior, adicionando a lista com os novos elementos que gostaria de adicionar | linguagens.extend([\"java\",\"csharp\"])")

print("\nResultado: ",linguagens)  # ["python", "js", "c", "java", "csharp"]