linguagens = ["python", "js", "c", "java", "csharp"]
print("lista: linguagens = [\"python\", \"js\", \"c\", \"java\", \"csharp\"]")
print("\nNesse caso, o .remove() removerá com base no conteúdo, ao invés do índice. ")
linguagens.remove("c")
print("\nlinguagens.remove(\"c\")")
print(linguagens)  # ["python", "js", "java", "csharp"]
print("\nLembrando que removerá apenas o primeiro resultado, será necessário laço de repetições para remover todos resultados")