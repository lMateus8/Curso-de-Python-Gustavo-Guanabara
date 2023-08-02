''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer
'''
from random import randint
jogador =int(input('Tente adivinhar o número que estou pensando entre 1 e 10:....  '))
pc = randint(1, 10)
tentativas = 1
while jogador != pc:
    tentativas += 1
    if jogador < pc:
        jogador = int(input('É mais... tente de novo....  '))
    else:
        jogador = int(input('É menos... tente de novo....  '))


print(f'AGORA SIIIMMMM, Você precisou de {tentativas} palpites para acertar..')