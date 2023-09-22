# Solicita ao usuário as distâncias entre os pontos A, B e C
distancia_AB = float(input("Digite a distância entre A e B: "))
distancia_AC = float(input("Digite a distância entre A e C: "))
distancia_BC = float(input("Digite a distância entre B e C: "))

# Determina o caminho mais curto
caminho_mais_curto = ""
distancia_mais_curta = 0

if distancia_AB <= distancia_AC and distancia_AB <= distancia_BC:
    caminho_mais_curto = "A -> B"
    distancia_mais_curta = distancia_AB
elif distancia_AC <= distancia_AB and distancia_AC <= distancia_BC:
    caminho_mais_curto = "A -> C"
    distancia_mais_curta = distancia_AC
else:
    caminho_mais_curto = "B -> C"
    distancia_mais_curta = distancia_BC

# Imprime o caminho mais curto e a distância
print(f"O caminho mais curto é {caminho_mais_curto} com uma distância de {distancia_mais_curta} unidades.")
