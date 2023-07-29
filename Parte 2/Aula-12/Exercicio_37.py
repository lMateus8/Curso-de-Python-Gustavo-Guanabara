''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
print('-=' * 15)
print('vamos converter um numero para binário, octal ou hexadecimal')
print('-=' * 15)

n = int(input('Qual número deseja converter? '))
binario = bin(n)[2:]
octal = oct(n)[2:]
hexadecimal = hex(n)[2:]
opcao = int(input('Vai converter para qual base? digite [1] para BINÁRIO | [2] para OCTAL | [3] para HEXADECIMAL: '))
if opcao == 1:
    print(f'Você escolheu BINÁRIO, então {n} convertido para BINÁRIO é: {binario}')
elif opcao == 2:
    print(f'Você escolheu OCTAL, então {n} convertido para OCTAL é: {octal}')
elif opcao == 3:
    print(f'Você escolheu HEXADECIMAL, então {n} convertido para HEXADECIMAL é: {hexadecimal}')
else:
    print('OPÇÃO INCORRETA... COMECE NOVAMENTE')