'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''
from datetime import date
ano = int(input('Qual ano de nascimento do atleta (INFORME COM OS 4 DIGITOS. EXEMPLO: 1989)? '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade <= 9:
    print(f'você tem {idade} anos e está na categoria MIRIM')
elif idade <= 14:
    print(f'você tem {idade} anos e está na categoria INFANTIL')
elif idade <= 19:
    print(f'você tem {idade} anos e está na categoria JUNIOR')
elif idade <= 25:
    print(f'você tem {idade} anos e está na categoria SENIOR')
else:
    print(f'você tem {idade} anos e está na categoria MASTER')
