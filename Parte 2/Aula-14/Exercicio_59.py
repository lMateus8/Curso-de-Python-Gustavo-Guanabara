''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

opcao = 1
n1 = int(input('Digita um numero ai:  '))
n2 = int(input('Digita outro numero ai:  '))
while opcao != 5:
    opcao = int(input('O QUE VOCÊ DESEJA FAZER?\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MOSTRAR O MAIOR\n[4] NOVOS NUMEROS\n[5] SAIR DO PROGRAMA\n   '))
    if opcao == 1:
        soma = n1 + n2
        print(soma)
    elif opcao == 2:
        multi = n1 * n2
        print(multi)
    elif opcao == 3:
        if n1 > n2:
            print(f'o numero {n1} é maior que {n2}')
        else:
            print(f'o numero {n2} é maior que {n1}')
    elif opcao == 4:
        n1 = int(input('Digita um numero ai:  '))
        n2 = int(input('Digita outro numero ai:  '))
    elif opcao == 5:
        print('PROGRAMA ENCERRADO')
    else:
        print('OPÇÃO INVÁLIDA')




