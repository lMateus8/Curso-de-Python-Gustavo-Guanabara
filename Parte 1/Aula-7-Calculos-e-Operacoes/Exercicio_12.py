# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Qual o preço desse produto? '))
print(f'Mas como estamos com desconto de 5% em toda loja, esse produto sairá por R${preco * 0.95:.2f}')