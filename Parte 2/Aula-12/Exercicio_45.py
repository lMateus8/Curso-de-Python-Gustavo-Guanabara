## 45 - FAÇA O COMPUTADOR JOGAR JOKEMPO COM VC
from random import randint
print('-=' * 15)
print('VAMOS JOGAR PEDRA PAPEL OU TESOURA')
print('-=' * 15)

escolha = int(input('PEDRA PAPEL OU TEEESOURA.... [1] para PEDRA [2] para PAPEL [3] para TESOURA =>   '))
pc = randint(1, 3)
if escolha == 1 and pc == 2:
    print(f'Você escolheu PEDRA, eu escolhi PAPEL, logo eu venci pois PAPEL embrulha a PEDRA')
elif escolha == 2 and pc == 3:
    print(f'Você escolheu PAPEL, eu escolhi TESOURA, logo eu venci pois TESOURA corta o PAPEL')
elif escolha == 3 and pc == 1:
    print(f'Você escolheu TESOURA, eu escolhi PEDRA, logo eu venci pois PEDRA quebra o TESOURA')
elif pc == 1 and escolha == 2:
    print(f'eu escolh1 PEDRA, voce escolheu PAPEL, logo voce venceu pois PAPEL embrulha a PEDRA')
elif pc == 2 and escolha == 3:
    print(f'eu escolh1 PAPEL, voce escolheu TESOURA, logo voce venceu pois TESOURA corta o PAPEL')
elif pc == 3 and escolha == 1:
    print(f'eu escolh1 TESOURA, voce escolheu PEDRA, logo voce venceu pois PEDRA quebra o TESOURA')
elif escolha != 1 and escolha != 2 and escolha != 3:
    print('OPÇÃO INVÁLIDA')
else:
    print(f'Eu também escolhi {pc}')
    print('EMPATE')

print(pc)