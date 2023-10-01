
def num_par(tupla1):
    tupla2 = []
    for i in tupla1:
        if(i %2 == 0):
            tupla2.append(i)
    return tuple(tupla2)

tuplat = (1,2,3,4,5)
print(num_par(tuplat))