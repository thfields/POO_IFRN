# Solicita o número de usuários que irão responder à pesquisa
total_usuarios = int(input("Quantos usuários irão responder à pesquisa? "))

# Inicializa contadores para cada opção de resposta
insatisfeito = 0
satisfeito = 0
nao_responder = 0

# Inicializa o contador de usuários
contador_usuarios = 0

# Loop para coletar as respostas dos usuários
while contador_usuarios < total_usuarios:
    contador_usuarios += 1

    print(f"Usuário {contador_usuarios}:")
    resposta = input("Por favor, escolha uma das opções (INSATISFEITO, SATISFEITO, NÃO QUERO RESPONDER): ").strip().upper()

    # Verifica a resposta e atualiza os contadores
    if resposta == "INSATISFEITO":
        insatisfeito += 1
    elif resposta == "SATISFEITO":
        satisfeito += 1
    elif resposta == "NÃO QUERO RESPONDER":
        nao_responder += 1
    else:
        print("Opção inválida. Por favor, escolha uma das opções válidas.")

# Calcula o percentual de cada opção de resposta
percentual_insatisfeito = (insatisfeito / total_usuarios) * 100
percentual_satisfeito = (satisfeito / total_usuarios) * 100
percentual_nao_responder = (nao_responder / total_usuarios) * 100

# Apresenta os resultados
print("\nResultados da pesquisa:")
print(f"Percentual de INSATISFEITO: {percentual_insatisfeito:.2f}%")
print(f"Percentual de SATISFEITO: {percentual_satisfeito:.2f}%")
print(f"Percentual de NÃO QUERO RESPONDER: {percentual_nao_responder:.2f}%")
