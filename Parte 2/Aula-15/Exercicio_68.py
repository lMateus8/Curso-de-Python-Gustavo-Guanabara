''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou,
no final do jogo.
'''
from random import randint
print('VAMOS JOGAR PAR OU IMPAR')
vezes = 0
while True:
    pc = randint(1, 5)
    player = int(input(' diga um valor de 1 a 5: '))
    escolha = ' '
    while escolha not in 'P/I':
        escolha = str(input('você quer par ou impar? [P/I]')).upper().strip()
    soma = pc + player
    if soma % 2 == 0:
        vence = 'PAR'
    else:
        vence = 'IMPAR'
    if vence[0] == escolha:
        print(f'Voce escolheu {player} e o computador {pc}. total de {soma} deu {vence}')
        print('VOCÊ VENCEU, VAMOS MAIS UMA ...')
        vezes += 1
    else:
        print(f'Voce escolheu {player} e o computador {pc}. total de {soma} deu {vence}')
        print(f'VOCÊ PERDEU.. VOCÊ GANHOU {vezes} vezes')
        break