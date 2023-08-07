## 74 - programa gera 5 umeros aleatorios e coloca numa tupla
from random import randint
tupla = ()
for c in range(5):
    aleatorio = randint(1, 10)
    tupla = tupla + (aleatorio,)

print(f'os valores sorteados foram {tupla}')
print(f'O maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')

