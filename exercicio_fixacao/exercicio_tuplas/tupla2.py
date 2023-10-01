def ordenar_tupla(tupla1):
      
    conjunto = set(tupla1)
    ordenada = sorted(list(conjunto))
    return tuple(ordenada)

tupla2 = ("banana", "maçã", "laranja", "banana", "uva")

print(ordenar_tupla(tupla2))