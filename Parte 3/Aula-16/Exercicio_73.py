## 73 - 20 primeiros colocados do futebol brasileirao, a) mostra apenas os 5, b os ultimos 4, c- uma lista em ordem alfabetica, em q posicao esta chapecoense
tabela = ('Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Fluminense', 'Athletico-PR', 'São Paulo', 'Fortaleza', 'Cruzeiro', 'Bragantino', 'Santos', 'Internacional', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco', 'Coritiba')
print('-='*20)
print(f'a Tabela está da seguinte forma {tabela}')
print('-='*20)
print(f'os 5 primeiros colocados são {tabela[:5]}')
print('-='*20)
print(f'os 4 últimos colocados são {tabela[-4:]}')
print('-='*20)
print(f'times em ordem alfabetica {sorted(tabela)}')
print('-='*20)
print(f'o Cruzeiro está na posição {tabela.index("Cruzeiro")+1}')
print('-='*20)
