## 74 - programa gera 5 umeros aleatorios e coloca numa tupla
from random import randint
menor = 0
maior = 0
tupla = ()
for c in range(5):
    aleatorio = randint(1, 10)
    tupla = tupla + (aleatorio,)
    if c == 0:
        menor = aleatorio
        maior = aleatorio
    else:
        if aleatorio < menor:
            menor = aleatorio
        elif aleatorio > maior:
            maior = aleatorio

print(f'os valores sorteados foram {tupla}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')

