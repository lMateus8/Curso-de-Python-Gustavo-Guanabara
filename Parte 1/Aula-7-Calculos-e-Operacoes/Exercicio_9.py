# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
num = int(input('Digita um número: '))
print('A TABUADA DESSE NÚMERO É')
print('-='*15)
print(num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10)
print('-='*15)
#utilizando outro método
for x in range (11):
    print(f' {num} x {x} = {num*x}')