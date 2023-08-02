'''
Melhore o exercício 61, perguntando para o usuário
se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar "0 termos"
'''

p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
x = p
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(x, end=' → ')
        x += r
        c += 1
    print('pausa')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print(f'PROGRESSÃO FINALIZADA COM {total} TERMOS FINALIZADOS')
print('FIM')