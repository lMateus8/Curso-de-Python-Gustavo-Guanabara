''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''
maior = mulheres = homem = 0

while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('IDADE: → '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'F/M':
        sexo = str(input('SEXO: [M/F] → ')).upper().strip()
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-'*25)
    continua = ' '
    while continua not in 'S/N':
        continua = str(input('quer continuar? [S/N] → ')).upper().strip()
    if continua != 'S':
        break

print(f'Existem {maior} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homem} homens')
print(f'Foram cadastradas {mulheres} mulheres com menos de 20 anos')
