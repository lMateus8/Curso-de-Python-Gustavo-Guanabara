''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''
continuar = 'S'
soma = qnt = maior = menor = 0
while continuar == 'S':
    num = int(input('Digita um numero ai....    '))
    qnt += 1
    soma += num
    if qnt == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = str(input('Deseja continuar? [S/N]')).upper()
media = soma / qnt
print('-='*15)
print(f'A media dos numeros digitados foi {media}, o maior numero digitado  foi {maior} e o menor {menor}')
