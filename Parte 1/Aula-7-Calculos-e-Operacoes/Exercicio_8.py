# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metro = float(input('Digite o numero em metro para depois ser convertido em cm e milimetros: '))
cm = metro * 100
mm = metro * 1000
print(f'{metro} metros são {cm} centimetros e {mm} milimetros')