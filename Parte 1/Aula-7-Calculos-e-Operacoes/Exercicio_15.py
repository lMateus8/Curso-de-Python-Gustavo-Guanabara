# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
dias = int(input('Quantos dias ele foi alugado? '))
km = float(input('Quantos KM você rodou? '))
totDia = dias*60
totKm = km * 0.15
total = totKm + totDia
print(f'O total a pagar é de R${total:.2f}')