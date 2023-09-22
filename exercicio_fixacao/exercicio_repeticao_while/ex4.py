# Solicita ao usuário um número entre 1 e 10000
numero = int(input("Digite um número entre 1 e 10000: "))

# Verifica se o número está dentro do intervalo válido
if 1 <= numero <= 10000:
    # Inicializa uma variável para contar os divisores
    divisores = 0
    
    # Loop para verificar se o número é primo
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    
    # Se tiver exatamente 2 divisores (1 e ele mesmo), é primo
    if divisores == 2:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print("Número fora do intervalo válido.")
