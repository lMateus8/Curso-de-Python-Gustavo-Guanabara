''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''
tot = 0
num = int(input('Digite um numero: '))
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m', end=' ')
        tot += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foí divisível {tot} vezes')
if tot == 2:
    print(f'O número {num} é um numero primo')
else:
    print(f'Por isso ele não é primo')