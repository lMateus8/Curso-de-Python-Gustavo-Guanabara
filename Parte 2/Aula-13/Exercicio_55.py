''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual seu peso? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso
print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg')