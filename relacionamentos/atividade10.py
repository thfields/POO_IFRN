from typing import List

class Interruptor:
    def __init__(self, comodo: str, ar: bool = False):
        self._comodo = comodo
        self._ar = ar
    
    def acender(self):
        print(f"Acendendo luz do(a): {self._comodo}") if not self._ar else print(f"Ligando ar do(a): {self._comodo}")

    def apagar(self):
        print(f"Apagando luz do(a): {self._comodo}") if not self._ar else print(f"Desligando ar do(a): {self._comodo}")

class Porta:
    def __init__(self, comodo, tipo: str = 'normal'):
        self._tipo = tipo
        self._senha = 123
        self._comodo = comodo

    def abre(self, senha=None) -> bool:
        if self._tipo == 'normal' or senha == self._senha:
            print(f"Abrindo porta do {self._comodo}")
            return True
        else:
            print(f'Digitando a senha da porta do {self._comodo}!')
            return False
    
    def fecha(self):
        print(f"Fechando porta do {self._comodo}")

class Pessoa:
    def __init__(self, nome: str):
        self._nome = nome

    def acender_lampada(self, interruptor: Interruptor):
        print(f"Eu sou {self._nome} e estou ", end="")
        interruptor.acender()

    def apagar_lampada(self, interruptor: Interruptor):
        print(f"Eu sou {self._nome} e estou ", end="")
        interruptor.apagar()

    def abre_porta(self, porta: Porta, senha=None) -> bool:
        print(f"Eu sou {self._nome} e estou ", end="")
        if not porta.abre(senha):
            print(f'Senha digitada ({senha}) está incorreta!')
            return False
        return True

    def fecha_porta(self, porta: Porta):
        print(f"Eu sou {self._nome} e estou ", end="")
        porta.fecha()

class Objeto:
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor

    def __str__(self):
        return f'Um(a) {self._nome} de cor: {self._cor};'

class Comodo:
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor
        self._portas: List[Porta] = [] 
        self._objetos: List[Objeto] = []
      
    def __str__(self):
        objetos_str = ', '.join(str(objeto) for objeto in self._objetos)
        return f"O comodo: {self._nome}; de cor: {self._cor}; tem {len(self._portas)} porta(as); com os seguintes objetos: {objetos_str}"
    
    def set_porta(self, porta: Porta):
        self._portas.append(porta)

    def set_objeto(self, objeto: Objeto):
        self._objetos.append(objeto)

class Casa:
    def __init__(self):
        self._comodos: List[Comodo] = []
  
    def set_comodo(self, comodo: Comodo):   
        self._comodos.append(comodo)

# Criando objetos
interruptor_sala = Interruptor(comodo="sala")
interruptor_quarto_ar = Interruptor(comodo="quarto", ar=True)

porta_sala = Porta(comodo="sala")
porta_quarto = Porta(comodo="quarto", tipo="segura")

pessoa1 = Pessoa(nome="Alice")
pessoa2 = Pessoa(nome="Bob")

objeto1 = Objeto(nome="sofá", cor="azul")
objeto2 = Objeto(nome="quadro", cor="vermelho")

comodo_sala = Comodo(nome="sala", cor="branca")
comodo_sala.set_porta(porta_sala)
comodo_sala.set_objeto(objeto1)

comodo_quarto = Comodo(nome="quarto", cor="rosa")
comodo_quarto.set_porta(porta_quarto)
comodo_quarto.set_objeto(objeto2)

casa = Casa()
casa.set_comodo(comodo_sala)
casa.set_comodo(comodo_quarto)

# Testando ações
pessoa1.acender_lampada(interruptor_sala)
pessoa1.apagar_lampada(interruptor_sala)
pessoa1.acender_lampada(interruptor_quarto_ar)
pessoa2.apagar_lampada(interruptor_quarto_ar)

pessoa1.abre_porta(porta_sala)
pessoa2.abre_porta(porta_quarto, senha=123)

pessoa1.fecha_porta(porta_sala)
pessoa2.fecha_porta(porta_quarto)

print(comodo_sala)
print(comodo_quarto)
