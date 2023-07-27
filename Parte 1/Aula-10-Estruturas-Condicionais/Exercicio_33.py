## 33 - lê 3 numero e mostra qual maior e qual menor
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'o numero {n1} é o maior')
elif n2 > n1 and n2 > n3:
    print(f'O numero {n2} é maior')
elif n3 > n1 and n3 > n2:
    print(f'o numero {n3} é maior')

if n1 < n2 and n1 < n3:
    print(f'o numero {n1} é o menor')
elif n2 < n1 and n2 < n3:
    print(f'O numero {n2} é menor')
elif n3 < n1 and n3 < n2:
    print(f'o numero {n3} é menor')