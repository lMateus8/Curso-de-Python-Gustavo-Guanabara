'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
impar = []
par = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continuar = ' '
    while continuar not in 'S/N':
        continuar = str(input('Deseja continuar? [S/N]  ')).upper().strip()
    if continuar == 'N':
        break
print(f'A lista final ficou dessa maneira {lista}')
print(f'os numero impares foram {impar}')
print(f'os numeros pares foram {par}')

