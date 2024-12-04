class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plimmm Plimmmm!")

    def freiar(self):
        print("Shrrrrrr!")
        print("Bicicleta parada!")

    def correr(self):
        print("Ramdamdamdamdam")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave.capitalize()} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Azul", "Specialized", 2024, 16000, 24)
print(b1)
b1.buzinar()
b1.correr()
b1.freiar()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Vermelha", "Monark", 1980, 189, 20)
print(b2)
b2.correr()
b2.freiar()
b2.buzinar()
#print(b2.cor, b2.modelo, b2.ano, b2.valor)

