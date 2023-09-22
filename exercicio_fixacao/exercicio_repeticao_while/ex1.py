# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicializa o fatorial como 1
fatorial = 1

# Verifica se o número é negativo
if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    # Calcula o fatorial usando um loop while
    while numero > 0:
        fatorial *= numero
        numero -= 1

    # Imprime o resultado do fatorial
    print(f"O fatorial é {fatorial}")
