# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Hoje seu salário é de: '))
novo = salario * 1.15
print(f'Você terá aumento de 15%, logo seu novo salário é de R${novo:.2f}')