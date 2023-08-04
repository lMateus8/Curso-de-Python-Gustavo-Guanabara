''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''
s = c = 0
while True:
    num = int(input('Digita ai: '))
    if num == 999:
        break
    c += 1
    s += num
print(f'a soma dos numero é {s} e foram digitados {c} números')