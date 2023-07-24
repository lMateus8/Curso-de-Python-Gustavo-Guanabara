# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Qual altura da parede? '))
largura = float(input('Qual largura da parede? '))
area = altura * largura
tinta = area / 2
print(f'sua parede tem {area}m² e ira precisar de {tinta} litros de tinta.')