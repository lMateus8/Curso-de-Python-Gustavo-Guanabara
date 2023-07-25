#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
import random
aluno1 = input('Qual nome do primeiro aluno? ')
aluno2 = input('Qual nome do segundo aluno? ')
aluno3 = input('Qual nome do terceiro aluno? ')
aluno4 = input('Qual nome do quarto aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de apresentação do trabalhao será {lista}')