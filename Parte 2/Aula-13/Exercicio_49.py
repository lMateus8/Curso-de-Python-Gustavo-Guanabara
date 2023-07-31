#tabuada de um número utilizando laço
num = int(input('Digite um numero: '))
print('A TABUADA DESSE NUMERO É')
print('-='*15)
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')
print('-='*15)
