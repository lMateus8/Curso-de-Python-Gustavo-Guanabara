#le o nome completo e mostre em seguida o primeiro e ultimo nome separadamente
nome = input('Digita seu nome completo ai? ').strip().split()
print(f'O seu primeiro nome é {nome[0]}, e o seu ultimo nome é {nome[len(nome)-1]}')