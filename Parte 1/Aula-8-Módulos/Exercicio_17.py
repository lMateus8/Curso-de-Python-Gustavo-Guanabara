#Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

ladoA = float(input('Digite o tamanho do Cateto oposto: '))
ladoB = float(input('Digite o tamanho do Cateto adjacente: '))
hip = hypot(ladoA, ladoB)
#hip = sqrt(pow(ladoA, 2) + pow(ladoB, 2))
print(f'a Hiponesa é {hip:.2f}')
