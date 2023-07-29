'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''
n1 = int(input('Qual primeiro numero? '))
n2 = int(input('Qual segundo numero? '))

if n1 > n2:
    print('O Primeiro número é maior')
elif n2 > n1:
    print('O segundo número é maior')
else:
    print('Os números são iguais')
