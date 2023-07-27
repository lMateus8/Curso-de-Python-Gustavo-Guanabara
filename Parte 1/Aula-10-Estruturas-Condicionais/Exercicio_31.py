'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''

km = float(input('Qual será a distancia da viagem (em KM): '))
if km <= 200:
    print(f'sua viagem será de {km} quilometros, então custará R${km * 0.5}0')
else:
    print(f'Sua viagem será de {km} quilometros, então custará R${km * 0.45}0 ')