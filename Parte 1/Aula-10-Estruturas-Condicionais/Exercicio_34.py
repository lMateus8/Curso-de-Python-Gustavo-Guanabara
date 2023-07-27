'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.
'''

salario = float(input('Qual seu salário atual: '))
if salario < 1250:
    print(f'O seu novo salário será de R${salario*1.15:.2f}')
else:
    print(f'O seu novo salário será de R${salario* 1.1 :.2f}')