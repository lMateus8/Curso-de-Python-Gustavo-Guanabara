## 57 - lê o sexo da pessoa mas só aceita M ou F se errado pede a digitação novamente até estar certo

sexo = str(input('Qual seu sexo? DIGITE [M] para masculino ou [F] para feminino →   ')).upper().strip()
while sexo not in ['F', 'M']:
    print('Opção inválida. digite apenas [M] ou [F]...')
    sexo = str(input('Qual seu sexo? DIGITE [M] para masculino ou [F] para feminino →   ')).upper().strip()
if sexo == 'F':
    print('Você selecionou feminino')
if sexo == 'M':
    print('Você selecionou Masculino')

