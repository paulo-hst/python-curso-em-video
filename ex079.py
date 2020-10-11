lista = list()
n = 0
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Número duplicado.')
    op = str(input('Deseja continuar? [S/N] ')).lower().strip()
    if op == 'n':
        break

print('FIM DO PROGRAMA')
lista.sort()
print(f'Lista: {lista}')

