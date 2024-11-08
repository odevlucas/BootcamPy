texto = input ("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS: #O upper está no "if" porque a constante "VOGAIS" está maiúscula
        print(letra.upper(), end="") #upper no print para também trazer o resultado em maiúsculo
print()#quebra de linha
