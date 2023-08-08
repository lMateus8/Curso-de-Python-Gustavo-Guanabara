'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''
valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))

print(f'Os valores digitados foram {valores}')
print(f'O maior valor foi {max(valores)}, e esta nas posição ', end=' ') #{valores.index(max(valores))+1}')
for pos, item in enumerate(valores):
    if item == max(valores):
        print(f'{pos}... ', end=' ')
print()
print(f'O menor valor foi {min(valores)}, e esta nas posição ', end=' ') #{valores.index(min(valores))+1}')
for pos, num in enumerate(valores):
    if num == min(valores):
        print(f'{pos}... ', end=' ')
print()
print('FIM')