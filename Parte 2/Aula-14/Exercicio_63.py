'''
Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os primeiros n elementos e uma sequência de Fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''
quantos = int(input('Qual números da sequencia de fibonacci voce quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2} → ', end='')
c = 3
while c <= quantos:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    c += 1
    t1 = t2
    t2 = t3
print('FIMMMMM')


