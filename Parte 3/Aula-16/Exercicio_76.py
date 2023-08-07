## 76 - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Lápis', 1.75,
            'Borracha', 15.90,
            'Caderno', 19.99,
            'Livro', 35.70,
            'Estojo', 15.99)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range (0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[item]:>7.2f}')
