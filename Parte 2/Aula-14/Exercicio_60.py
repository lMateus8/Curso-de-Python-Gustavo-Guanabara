''' Faça um programa que leia um número qualquer e mostre
o seu fatorial

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

# forma mais simples
'''from math import factorial
nu = int(input('Digite um numero : '))
f = factorial(nu)
print(f'O fatorial de {nu} é {f}')'''

nu = int(input('Digite um numero : '))
c = nu
f = 1
while c > 0:
    if c == 1:
        print(f'{c}', end=f' é = {f}')
    else:
        print(f'{c}', end=' x ')
    f *= c
    c -= 1