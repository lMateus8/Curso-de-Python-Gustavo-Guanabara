'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
num = int(input("Que valor você quer sacar? \n"))
cedulas = [50, 20, 10, 1]
'''
from math import trunc
print('='*20)
print('BANCO CURSO EM VÍDEO')
print('='*20)
valor = int(input('Qual valor deseja sacar? '))
while True:
    if trunc(valor/50) != 0:
        print(f'Total de {trunc(valor/50)} notas de R$50,00')
        valor -= (trunc(valor/50)*50)
    elif trunc(valor/20) != 0:
        print(f'Total de {trunc(valor/20)} notas de R$20,00')
        valor -= (trunc(valor/20)*20)
    elif trunc(valor/10) != 0:
        print(f'Total de {trunc(valor/10)} notas de R$10,00')
        valor -= (trunc(valor/10)*10)
    elif trunc(valor/1) != 0:
        print(f'Total de {trunc(valor/1)} notas de R$1,00')
        valor -= (trunc(valor / 1) * 1)
    if valor == 0:
        break
print('='*20)
print('OBRIGADO! VOLTE SEMPRE')
print('='*20)