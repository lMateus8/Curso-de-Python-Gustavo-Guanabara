#ler uma frase qualquer e mostre quantas vezes aparece letra A, em que posição ela aparece pela primeira vez, em que posição ela aprece na ultima vez
frase = input('Digite uma frase qualquer: ').lower().strip()
print('A letra A aparece ', frase.lower().count('a'), ' vezes.')
print('a letra A aparece primeiro no índice ', frase.strip().find('a')+1)
print('a ultima letra A apareceu na posicao ', frase.rfind('a')+1)

