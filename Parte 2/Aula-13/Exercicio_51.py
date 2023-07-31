''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''

p = int(input('Qual primeiro termo? '))
r = int(input('Qual razão? '))
x = p
for c in range(10):
    print(x, end=' -> ')
    x += r
print('ACABOU')