'''Faça um programa que calcule a soma entre todos os números impares
que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.
'''
s = 0
v = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        v += 1
print(f'A soma de todos {v} impares multiplos de 3 entre 1 e 500 é: {s}')