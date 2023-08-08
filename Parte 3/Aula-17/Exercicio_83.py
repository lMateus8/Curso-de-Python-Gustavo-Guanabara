'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
'''
abre =[]
fecha =[]

expressão = str(input('Digite a expressão matematica: '))
for c in range (expressão.count('(')):
    abre.append('(')
for c in range (expressão.count(')')):
    fecha.append(')')
if len(abre) != len(fecha):
    print('SUA EXPRESSÃO ESTÁ INVÁLIDA')
else:
    print('SUA EXPRESSÃO É VÁLIDA')