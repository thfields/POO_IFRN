class Carro:
    marca = ''
    modelo = ''
    ano = ''

    def mostrarCarro(self):
        print(f"o seu {self.modelo} da marca {self.marca} do ano {self.ano} está pronto!")

class Dog:
    raca = ''
    peso = ''
    nome = ''

    def mostrarDog(self):
        print(f"seu cachorro {self.nome} da raça {self.raca} tem peso {self.peso}")

c1 = Carro()
c1.modelo = 'Fox'
c1.marca = 'Fiat'
c1.ano = 2015

c1.mostrarCarro()

d1 = Dog()
d1.nome = 'Leona'
d1.raca = 'Pastor Alemão'
d1.peso = '47kg'

d1.mostrarDog()