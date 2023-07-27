''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Qual a velocidade você estava? '))
if velocidade > 80:
    print(f'Sua velocidade foi de {velocidade}km/h, logo, estava acima do limite de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'\033[0;31;40mVocê será multado em R${multa}0\033[m ')
else:
    print('\033[34mVocê estava dentro do limite de velocidade...\033[m')