""" 
Escreva uma função que receba um conjunto de strings e retorne um novo
conjunto com as strings que são palíndromos. Um palíndromo é uma palavra
que é igual quando lida de trás para frente. Por exemplo, se o conjunto for
{"arara", "casa", "ovo", "radar"}, a função deve retornar {"arara", "ovo",
"radar"}.
"""
def palindromo(palavra):
    return palavra == palavra[::-1]

def palindromosConjunto(conjunto):
    palindromos = set()
    for palavra in conjunto:
        if palindromo(palavra):
            palindromos.add(palavra)
    return palindromos

conjunto = {"arara", "casa", "ovo", "radar"}

palavras = palindromosConjunto(conjunto)
print(palavras)