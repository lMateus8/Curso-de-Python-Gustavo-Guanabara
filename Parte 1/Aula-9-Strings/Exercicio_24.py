#leia o nome de uma cidade e mostra se a cidade começa ou nao com Santo
city = input('Qual nome da sua Cidade? ')
lista = city.strip().split()
true = lista[0] == 'Santo'
print(true)

'''cid = str(input('cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')'''
