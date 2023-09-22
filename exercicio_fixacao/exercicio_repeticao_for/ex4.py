# Solicita ao usuário dois valores positivos
v_ini = int(input("Digite o valor inicial (positivo): "))
v_fim = int(input("Digite o valor final (positivo): "))

# Verifica se ambos os valores são positivos
if v_ini <= 0 or v_fim <= 0:
    print("Por favor, digite valores positivos para ambas as extremidades do intervalo.")
else:
    # Verifica se v_ini é menor que v_fim
    if v_ini < v_fim:
        # Imprime todos os números inteiros dentro do intervalo excluindo o valor inicial e o valor final
        for numero in range(v_ini + 1, v_fim):
            print(numero, end=" ")  # Imprime o número e um espaço, mantendo tudo na mesma linha
    else:
        print("O valor inicial deve ser menor que o valor final.")
