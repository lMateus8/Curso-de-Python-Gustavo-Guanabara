## 77 - uma tupla com varias palavras sem acento.  depois mostrar para cada palavra suas vogais
import re
tupla = ('praticar', 'ingles', 'matematica', 'python', 'curso', 'video', 'teclado', 'caderno', 'papel')

for palavra in tupla:
    vogais = re.findall(r'[aeiou]', palavra)
    print(f'Na palavra {tupla[tupla.index(palavra)].upper()} temos as vogais {vogais}')