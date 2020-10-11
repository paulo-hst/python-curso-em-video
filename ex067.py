c = 0
t = 0
while True:
    n = int(input('\nDigite um número para ver a tabuada: '))
    if n < 0:
        break
    for c in range(1,11):
        t = n * c
        print(f'{n} * {c} = {t}')
print('-'*10, 'Programa encerrado' ,'-'*10)
