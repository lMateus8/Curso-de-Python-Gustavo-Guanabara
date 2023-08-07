## 72 - uma tupla de 0 a 20 por extenso e depois mostrar o numero que eu ler no teclado
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    usuario = int(input('Qual numero deseja ver por extenso? de 0 a 20: '))
    if 0 <= usuario <= 20:
        break
    print('Digite entre 0 e 20')
print(f'Você digitou o número {extenso[usuario]}')
continua = str(input('Você deseja continuar? [S/N]'))