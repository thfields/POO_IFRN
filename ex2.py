# Solicita ao usuário que digite o valor das duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Verifica se o aluno está em recuperação
if 30 <= media < 70:
    print("Você está em RECUPERAÇÃO!!!")
else:
    print("Você não está em recuperação.")
