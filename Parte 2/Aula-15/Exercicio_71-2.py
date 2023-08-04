'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
# feito pelo professor
from math import trunc
print('='*20)
print('BANCO CURSO EM VÍDEO')
print('='*20)
valor = int(input('Qual valor deseja sacar? '))
total = valor
ced = 50
while True:
    if trunc(total/ced) != 0:
        print(f'Total de {trunc(total/ced)} notas de R${ced},00')
        total -= (trunc(total/ced)*ced)
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced == 10:
            ced = 1
        else:
            break
print('='*20)
print('OBRIGADO! VOLTE SEMPRE')
print('='*20)