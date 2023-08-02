'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while
'''

p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
x = p
c = 1
while c <= 10:
    print(x, end=' → ')
    x += r
    c += 1
print('acabou')

