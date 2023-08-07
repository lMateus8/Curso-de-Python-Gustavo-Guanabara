## 77 - uma tupla com varias palavras sem acento.  depois mostrar para cada palavra suas vogais

tupla = ('praticar', 'ingles', 'matematica', 'python', 'curso', 'video', 'teclado', 'caderno', 'papel')

for palavra in tupla:
    print(f'\n Na palavra {palavra.upper()} temos as vogais ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
