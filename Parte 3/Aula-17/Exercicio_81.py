'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''
valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    continuar = ' '
    while continuar not in 'S/N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
valores.sort(reverse=True)
print(f'A lista possui {len(valores)} elementos')
print(f'Lista ordenada de trás pra frente {valores}')
if 5 in valores:
    print(f'O numero 5 foi digitado e está no indice ', end=' ')# {valores.index(5)}')
    for pos, numero in enumerate(valores):
        if numero == 5:
            print(f' {pos}... ', end=' ')
    print()
else:
    print('O numero 5 não foi digitado nessa lista')