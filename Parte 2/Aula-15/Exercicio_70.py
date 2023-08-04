'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
total = caro = menor = c = 0
barato = ''
while True:
    nome = str(input('NOME DO PRODUTO: '))
    valor = float(input('PREÇO DO PRODUTO: R$'))
    c += 1
    total += valor
    if valor >= 1000:
        caro += 1
    if c == 1 or valor < menor:
        menor = valor
        barato = nome
    continua = ' '
    while continua not in 'S/N':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()
    if continua == 'N':
        break
print(f'Total gasto = {total} reais')
print(f'ao todo {caro} produtos custam mais de 1000')
print(f'o produto mais barato é {barato}')
