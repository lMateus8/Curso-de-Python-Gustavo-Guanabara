'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
valores = []

while True:
    num = int(input('Digite um numero: '))
    if num in valores:
        print('Número já adicionado, por favor escolha outro...')
    else:
        valores.append(num)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja adiciona outro número? [S/N]')).upper().strip()
    if continua == 'N':
        break
valores.sort()
print(valores)


