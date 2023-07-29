'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''
idade = int(input('Qual sua idade? '))


if idade < 18:
    print(f'Ok, você ainda tem {idade} anos e não está na hora de se alistar..')
elif idade == 18:
    print(f'Parabens, você já tem {idade} anos e está na hora de se alistar')
else:
    print('Você já passou da idade de alistamento, obrigado!')