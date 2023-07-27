## 32 - lê un ano qualquer e mostra se ele é bissexto
## 1 - tem que ser divisivel por 4 e nao por 100
## 2 - se nao por 4 mas sim por 400,
from datetime import date
ano = int(input('Qual ano você deseja verificar? coloque 0 para o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é um ano bissexto')
else:
    print(f'O ano {ano} não é bissexto')