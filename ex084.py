lista = list()
temp = list()
maior = menor = 0

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))

    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()

    op = str(input('Deseja continuar? '))
    if op in 'Nn':
        break

print(f'Cadastros: {len(lista)}')

print(f'Maior peso: {maior} Kg. Peso de ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')

print(f'Menor peso: {menor} Kg. Peso de ', end=' ')
for c in lista:
    if c[1] == menor:
        print(f'{c[0]} ', end=' ')
