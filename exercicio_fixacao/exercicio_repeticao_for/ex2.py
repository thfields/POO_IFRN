# Solicita ao usuário um valor positivo
numero = int(input("Digite um valor positivo: "))

# Verifica se o número é positivo
if numero <= 0:
    print("Por favor, digite um valor positivo.")
else:
    # Imprime todos os números inteiros de 1 até o número digitado
    for i in range(1, numero + 1):
        print(i, end=" ")  # Imprime o número e um espaço, mantendo tudo na mesma linha
