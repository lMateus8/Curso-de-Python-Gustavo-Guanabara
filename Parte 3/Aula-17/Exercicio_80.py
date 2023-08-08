'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''
import bisect
lista = []
for c in range(5):
    n = int(input('Digite um numero: '))
    bisect.insort(lista, n)
    print(f'Numero {n} incluido na posição {lista.index(n)}')
print(f'Numeros digitados: {lista}')


