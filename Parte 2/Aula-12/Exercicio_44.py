'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
preco = float(input('Qual o preço do produto? '))
forma_pagamento = int(input('Qual a forma de pagamento? [1] para a vista [2] para a vista no cartão [3] para 2 vezes ou [4] para 3 vezes ou mais   '))
if forma_pagamento == 1:
    print(f'Você escolheu pagamento a vista com DINHEIRO/CHEQUE e terá um desconto de 10%')
    print(f'Valor original  R${preco}, valor com desconto R${preco*0.9}')
elif forma_pagamento == 2:
    print(f'Você escolheu pagamento a vista no cartão e terá um desconto de 5%')
    print(f'Valor original  R${preco}, valor com desconto R${preco*0.95}')
elif forma_pagamento == 3:
    print(f'Você escolheu pagamento em 2 vezes no cartão e não terá desconto')
    print(f'Valor a ser pago  R${preco}')
elif forma_pagamento == 4:
    print(f'Você escolheu pagamento em 3 vezes ou mais no cartão, com isso terá juros de 20%')
    print(f'Valor original  R${preco}, valor com juros R${preco*1.2}')
else:
    print('OPÇÃO INVÁLIDA')