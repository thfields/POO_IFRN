class Interruptor:
    def __init__(self):
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

class Lampada:
    def __init__(self, interruptor):
        self.interruptor = interruptor

    def acender(self):
        self.interruptor.ligar()
        print("A lâmpada foi acesa.")

    def apagar(self):
        self.interruptor.desligar()
        print("A lâmpada foi apagada.")

class ArCondicionado:
    def __init__(self, interruptor):
        self.interruptor = interruptor

    def ligarAr(self):
        self.interruptor.ligar()
        print("O ar condicionado foi ligado.")

    def desligarAr(self):
        self.interruptor.desligar()
        print("O ar condicionado foi desligado.")

class Porta:
    def __init__(self):
        self.aberta = False
    
    def abrir(self):
        self.aberta = True
        print("A porta está aberta.")

    def fechar(self):
        self.aberta = False
        print("A porta está fechada.")

class Casa:
    def __init__(self, num_comodos):
        self.comodos = []

        for i in range(num_comodos):
            interruptor = Interruptor()
            lampada = Lampada(interruptor)
            
            tem_ar_condicionado = input(f"O cômodo {i + 1} tem ar condicionado? (s/n): ").lower() == 's'
            ar_condicionado = ArCondicionado(interruptor) if tem_ar_condicionado else None

            porta = Porta()

            comodo = {"interruptor": interruptor, "lampada": lampada, "ar_condicionado": ar_condicionado, "porta": porta}
            self.comodos.append(comodo)

    def visitante_chega(self, nome):
        print(f"{nome} chegou à casa.")

    def realizar_acoes(self):
        for i, comodo in enumerate(self.comodos):
            print(f"\nAções no Cômodo {i + 1} ({'com ar condicionado' if comodo['ar_condicionado'] else 'sem ar condicionado'}):")
            
            while True:
                acoes_disponiveis = ["1 - Acender a lâmpada", "2 - Apagar a lâmpada", "3 - Abrir a porta", "4 - Fechar a porta"]
                if comodo["ar_condicionado"]:
                    acoes_disponiveis.extend(["5 - Ligar o ar-condicionado", "6 - Desligar o ar-condicionado"])
                
                acoes_disponiveis.append("0 - Sair do cômodo")
                
                print("\n".join(acoes_disponiveis))

                acao_escolhida = input("Escolha uma ação (0-6): ")

                if acao_escolhida == "0":
                    break
                elif acao_escolhida == "1":
                    comodo["lampada"].acender()
                elif acao_escolhida == "2":
                    comodo["lampada"].apagar()
                elif acao_escolhida == "3":
                    comodo["porta"].abrir()
                elif acao_escolhida == "4":
                    comodo["porta"].fechar()
                elif acao_escolhida == "5" and comodo["ar_condicionado"]:
                    comodo["ar_condicionado"].ligarAr()
                elif acao_escolhida == "6" and comodo["ar_condicionado"]:
                    comodo["ar_condicionado"].desligarAr()
                else:
                    print("Ação inválida.")

# Criação da casa com 2 cômodos
num_comodos = int(input("Informe o número de cômodos da casa: "))
casa = Casa(num_comodos)

# Criação do visitante
visitante_nome = input("Informe o nome do visitante: ")
casa.visitante_chega(visitante_nome)

# Realização de ações nos cômodos
casa.realizar_acoes()
