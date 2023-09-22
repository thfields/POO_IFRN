# Solicita ao usuário que digite o início e o fim do intervalo
inicio = int(input("Digite o valor de início do intervalo: "))
fim = int(input("Digite o valor de fim do intervalo: "))

# Solicita ao usuário que digite o terceiro valor
terceiro_valor = int(input("Digite um terceiro valor: "))

# Verifica se o terceiro valor está dentro do intervalo
if inicio <= terceiro_valor <= fim:
    print("O terceiro valor está dentro do intervalo.")
else:
    if terceiro_valor < inicio:
        print("O terceiro valor está fora do intervalo (parte inferior).")
    else:
        print("O terceiro valor está fora do intervalo (parte superior).")
