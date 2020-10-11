n = int(input('Digite um número para saber a tabuada: '))

for c in range(1, 11):
    m = n * c
    print('{} x {} = {}'.format(n,c,m))
