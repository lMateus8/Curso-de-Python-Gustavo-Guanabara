## 72 - uma tupla de 0 a 20 por extenso e depois mostrar o numero que eu ler no teclado
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    usuario = int(input('Qual numero deseja ver por extenso? de 0 a 20: '))
    if usuario < 0 or usuario > 20:
        print('digite entre 0 e 20')
    else:
        print(f'Voce digitou o numero {extenso[usuario]}')
        print('-='*15)
        continuar = str(input('vc Quer continuar? [S/N] ')).upper().strip()
        if continuar != 'S':
            while True:
                if continuar == 'N':
                    break
                elif continuar != 'S':
                    continuar = str(input('vc Quer continuar? [S/N] ')).upper().strip()
                elif continuar == 'S':
                    break
        if continuar == 'N':
            break

print('FIM')



