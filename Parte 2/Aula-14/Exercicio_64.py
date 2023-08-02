'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''
num = 0
soma = 0
c = 0
while num != 999:
    num = int(input('Digita um numero ai ou 999 para parar'))
    if num != 999:
        soma += num
        c += 1
print(f'Foram digitados {c} numeros e a soma entre eles é de {soma}')