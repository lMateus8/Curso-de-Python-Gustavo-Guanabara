''' Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços'''
# Após a sopa
# A sacada da casa
# A torre da derrota
# o lobo ama o bolo
# Anotaram a data da maratona

frase = str(input('Digite um frase a ser verificada: ')).lower()
semEspacos = frase.replace(" ", "")
frase_inversa = semEspacos[::-1]
if semEspacos == frase_inversa:
    print(f'A frase é palindromo')
else:
    print('A frase não é palindromo')

print(f'Frase original sem espaços e minuscula:  {semEspacos}')
print(f'Frase invertida:  {frase_inversa}')
