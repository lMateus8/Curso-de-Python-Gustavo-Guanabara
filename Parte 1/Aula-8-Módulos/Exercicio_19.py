#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
from random import choice
alunos = []
aluno1 = input('Qual nome do primeiro aluno? ')
alunos.append(aluno1)
aluno2 = input('Qual nome do segundo aluno? ')
alunos.append(aluno2)
aluno3 = input('Qual nome do terceiro aluno? ')
alunos.append(aluno3)
aluno4 = input('Qual nome do quarto aluno? ')
alunos.append(aluno4)


sorteado = choice(alunos)
print(sorteado)
