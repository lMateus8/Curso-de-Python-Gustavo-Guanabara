#recebe nome completo e mostre todo maiusculo, todo minusculo, quantas letras ao todo sem espaços e quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
lista = nome.split()
print('Seu nome em letra maiuscula: ', nome.upper())
print('Seu nome em letra minuscula: ', nome.lower())
print('Quantas letras tem seu nome: ', len(nome)-nome.count(' '))
print('Quantas letras tem seu primeiro nome: ', len(lista[0]))