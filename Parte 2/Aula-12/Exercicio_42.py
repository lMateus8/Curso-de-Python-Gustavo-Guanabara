'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
reta1 = float(input('Qual o comprimento da primeira reta: '))
reta2 = float(input('Qual o comprimento da segunda reta: '))
reta3 = float(input('Qual o comprimento da terceira reta: '))

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2:
    if reta1 == reta2 == reta3:
        print('pode formar um tringulo EQUILATERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('pode formar um triangulo ESCALENO')
    else:
        print('pode formar um triangulo ISÓSCELES')

else:
    print('Não forma triangulo')