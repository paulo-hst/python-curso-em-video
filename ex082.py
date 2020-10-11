lista = list()
par = list()
impar = list()

while True:
    lista.append(int(input('Digite um número: ')))
    op = str(input('Deseja continuar? [S/N] '))
    if op in 'Nn':
        break

for indice, valor in enumerate(lista):
    if valor % 2 == 1:
        impar.append(valor)
    else:
        par.append(valor)

print(f'Lista: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
