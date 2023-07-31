'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
for c in range (6):
    num = int(input('Digita um valor ai: '))
    if num % 2 == 0:
        s += num
print(f'A soma de todos os pares que você digitou é: {s}')