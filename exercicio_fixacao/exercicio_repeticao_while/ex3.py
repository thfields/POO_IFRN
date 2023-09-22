while True:
    temperatura = float(input("Digite a temperatura atual (em graus Celsius, digite um valor negativo para sair): "))

    if temperatura < 0:
        print("Programa encerrado.")
        break

    if temperatura < 15:
        print("Aqui não é o RN")
    elif 16 <= temperatura <= 25:
        print("Pense num frio")
    elif 26 <= temperatura <= 30:
        print("Temperatura normal e super agradável")
    elif 31 <= temperatura <= 35:
        print("Tá quente pra danado")
    else:
        print("Calor da muléstia!")
