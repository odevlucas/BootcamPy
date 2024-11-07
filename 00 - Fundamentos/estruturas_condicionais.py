MAIOR_IDADE = 18 #maiúscula pq é constante
IDADE_ESPECIAL = 17

print("***********Modo arcaico:***********")
idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Permitido: Atende requisitos para criação de CNH.")

if idade < MAIOR_IDADE:
    print("Não atende os requisitos para criação de CNH: Menor de idade.")

print("***********Modo \"if and else\"***********")
if idade >= MAIOR_IDADE:
    print("Permitido: Atende requisitos para criação de CNH.")
else:
    print("Não atende os requisitos para criação de CNH: Menor de idade.")

print("***********Modo \"if, elif and else\"***********")
if idade >= MAIOR_IDADE:
    print("Permitido: Atende requisitos para criação de CNH.")
elif idade == IDADE_ESPECIAL: #operador de comparação:
    print("Permitido realizar as aulas tériocas, entretanto, não poderá realizar as aulas práticas.")
else:
    print("Não atende os requisitos para criação de CNH: Menor de idade.")