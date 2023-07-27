## 35 - lê o comprimento de tres retas e mostra se pode ou nao formar um triangulo.
reta1 = float(input('Qual o comprimento da primeira reta: '))
reta2 = float(input('Qual o comprimento da segunda reta: '))
reta3 = float(input('Qual o comprimento da terceira reta: '))

print('é tringualo' if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2 else 'Não forma tringualo')