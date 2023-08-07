## 75 - lê 4 no teclado e colocar numa tupla - mostra qnts vezes aparece numero 9 em q posição foi digitao o primeiro 3 e quais foram os numeros pares
tupla = ()
pares = ()
for c in range(4):
    novoValor = int(input('Digite um numero: '))
    tupla = tupla + (novoValor,)
    if novoValor % 2 == 0:
        pares = pares + (novoValor,)
print(f'Essa tupla ficou com os seguintes numeros: {tupla}')
if 9 in tupla:
    print(f'o numero 9 aparece {tupla.count(9)} vezes')
else:
    print('O número 9 não foi digitado na tupla')
if 3 in tupla:
    print(f'o primeiro 3 foi digitado na posicao {tupla.index(3)+1}ª')
else:
    print('O número 3 não foi digitado na tupla')
print(f'os numeros pares foram {pares}')
print(type(tupla))
