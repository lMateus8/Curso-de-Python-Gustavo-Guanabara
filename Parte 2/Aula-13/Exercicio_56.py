''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

todas_idades  = 0
homem = ''
idadeMaior = 0
mulheres = 0

for c in range (0, 7):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Qual sua idade? '))
    sexo = int(input('Qual seu sexo? 1 masculino e 2 feminino: '))

    todas_idades += idade

    if idade > idadeMaior and sexo == 1:
        idadeMaior = idade
        homem = nome
    if sexo == 2 and idade < 20:
        mulheres += 1


media = todas_idades / 7
print(f"""A média das idades é {media:.2f}
O homem mais velho do grupo é o: {homem}
Ao todo são {mulheres} mulher menores de 20 anos
""")