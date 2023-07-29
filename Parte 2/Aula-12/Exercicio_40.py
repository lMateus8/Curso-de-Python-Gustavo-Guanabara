'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''
n1 = float(input('Qual foi a nota da sua primeira prova? '))
n2 = float(input('Qual foi a nota da sua segunda prova? '))
media = (n1+n2)/2
if media < 5:
    print(f'Sua média é {media}, logo você está REPROVADO')
elif 5 <= media < 7:
    print(f'Sua media é {media}, então você deverá fazer a prova de RECUPERAÇÃO')
else:
    print(f'Parabens, sua media é {media}, então você já está APROVADO')