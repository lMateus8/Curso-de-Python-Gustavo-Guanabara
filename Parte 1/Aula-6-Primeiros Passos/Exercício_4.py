# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e algumas informações possíveis sobre ele

algo = input('Digita algo ai: ')
print(algo)
print('o tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('é um numero? ', algo.isdigit())
print('é alfabetico? ', algo.isalpha())
print('é alfanumerico? ', algo.isalnum())
print('é maiusculo? ', algo.isupper())
print('é minusculo? ', algo.islower())
print('é capitalizada? ', algo.istitle())