f = str(input('Digite uma frase: ')).strip().lower()

print('A letra A apareceu {} vezes'.format(f.count('a')))
print('A letra A apareceu na posição {}'.format(f.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(f.rfind('a')+1))

