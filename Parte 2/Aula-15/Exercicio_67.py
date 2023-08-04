''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''
while True:
    c = 1
    num = int(input('Qual numero deseja mostrar a tabuada? '))
    if num < 0:
        print('FINALIZANDO CALCULADORA')
        break
    while c <=10:
        print(f'{num} x {c} = {num*c}')
        c += 1
