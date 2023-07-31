''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import date
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input(f'Que a a {c}ª pessoa nasceu? '))
    idade = (date.today().year) - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo {maior} pessoas são maiores de idade e {menor} pessoas são menores de idade')