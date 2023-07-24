# Faça um programa simples mostrando o alinhamento de uma palavra
# Faça um programa simples que mostre a soma, produto, divisão, divisão inteira e exponenciação entre dois números
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:

#alinhamento
nome = input('Qual seu nome: ')
print(f'prazer em conhece-lo {nome:>20}!')
print('-='*15)
print()

# Calculadora entre dois números
n1 = int(input('coloca um numero: '))
n2 = int(input('coloca outro ai: '))
soma = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma vale {soma}, o produto vale {m}, a divisão vale {d:.2}', end=' ')
print(f'A divisão inteira vale {di}, a exponenciação vale {e}')

print('-=' * 15)
print()

#ANTECESSOR E SUCESSOR
num = int(input('Digite um número: '))
print(f'Você escolheu o número {num}, o sucessor é {num + 1} e seu antecessor é {num - 1}.')

