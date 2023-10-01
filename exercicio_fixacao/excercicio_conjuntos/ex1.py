""" 
Escreva uma função que receba dois conjuntos de números inteiros e
retorne um novo conjunto com os elementos que estão em ambos os
conjuntos. Por exemplo, se os conjuntos forem {1, 2, 3, 4} e {3, 4, 5, 6}, a
função deve retornar {3, 4}.
"""
def intersecao_conjuntos(conjunto1, conjunto2):

    intersecao = conjunto1 & conjunto2
    return intersecao

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

resultado = intersecao_conjuntos(conjunto1, conjunto2)
print(resultado)