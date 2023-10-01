""" 
Escreva uma função que receba um dicionário que mapeia nomes de alunos
para suas notas e retorne um novo dicionário com os nomes dos alunos
aprovados e suas respectivas médias. Considere que um aluno é aprovado
se sua média for maior ou igual a 7. Por exemplo, se o dicionário for {"Ana":
[8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]}, a função
deve retornar {"Ana": 8.33, "Carla": 8.0}.
"""
def calcMedia(notas):
  total = sum(notas)
  media = total/len(notas)
  return media

def alunosAprovados(disc):
  aprovados = {}
  
  for aluno, notas in disc.items():
    media = calcMedia(notas)
    if(media >= 7):
      aprovados[aluno] =  round(media, 2)
  return aprovados

disc = {"Ana":[8.5, 9.0, 7.5],
         "Bruno": [6.0, 5.5, 4.0],
         "Carla": [7.0, 8.0, 9.0]}

alunos = alunosAprovados(disc)

print(alunos)