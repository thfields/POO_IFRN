""" 
Escreva uma função que receba um dicionário que mapeia nomes de países
para suas populações e retorne o nome do país com a maior população. Por
exemplo, se o dicionário for {"Brasil": 211.8, "China": 1400.5, "Índia":
1366.4}, a função deve retornar "China".
"""

def maior_populacao(disc):
    maior_valor = max(disc.values())
    
    for chave, valor in disc.items():
        if valor == maior_valor:
            pais = chave
            return pais

disc = {"Brasil": 211.8, "China": 1400.5, "Índia":
1366.4}

print(maior_populacao(disc))