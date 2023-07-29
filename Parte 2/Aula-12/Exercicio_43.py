'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''
from math import pow
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura em metros? '))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f'Seu imc é {imc:.2f}, Você está abixo do peso ideal')
elif 18.5 <= imc < 25:
    print(f'Seu imc é {imc:.2f}, Você está no peso ideal')
elif 25 <= imc < 30:
    print(f'Seu imc é {imc:.2f}, Você está Sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu imc é {imc:.2f}, Você está obeso')
else:
    print(f'Seu imc é {imc:.2f}, você está com obesidade morbida')
