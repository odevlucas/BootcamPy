curso = "pRoGrAmAçÃo" #Orkut style, rs
print(curso.center(30, "#"), "No formato orkut")
print()

print(curso.upper(),":no formato Upper")
print(curso.lower(),":no formato Lower")
print(curso.title(),":no formato Title")

print()
curso = "     Java     "
print(curso.center(30, "#"),":com espaçamento no início e fim")
print()

print(curso.strip(),":no formato Strip")
print(curso.lstrip(),":no formato Leftstrip")
print(curso.rstrip(),":no formato RightStrip")

print()
curso = "Python"
print(curso.center(30,"#"),":em sua forma natural")
print()

print(curso.center(10, "#"),":no formato Center (centralizado), com 10 caracteres completados por \"#\"")
print(".".join(curso),":adição do elemento (\".\") no caso) entre as letras")
