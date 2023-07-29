'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

preco = float(input('Qual o valor da casa que você pretende comprar? '))
salario = float(input('Qual seu salário? '))
anos_pagamento = int(input('Em quantos anos você pretende pagar essa casa? '))

prestacao = preco / (anos_pagamento * 12)
if prestacao >= (salario * 0.3):
    print(f'Desculpe, a prestação ficou em R${prestacao:.2f}, que é maior que 30% do seu salário. VocÊ não poderá financiar essa casa..')
else:
    print(f'Parabéns, A CASA É SUA... você pagará R${prestacao:.2f} por mês durante {anos_pagamento} anos até completar {preco} que é o valor total da casa')