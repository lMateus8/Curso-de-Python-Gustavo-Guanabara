'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
from random import randint
print('Olá, sou uma inteligência artifical e irei pensar num número entre 1 e 5, quero ver você adivinhar o número...')
numero = int(input('Diga um número de 1 a 5: '))
pensado = random.randint(1, 5)

if numero == pensado:
    print('Parabens, você pensou no mesmo número que eu.')
else:
    print(f'Hummmm não foi dessa vez, eu pensei no número {pensado}, tente de novo.')
