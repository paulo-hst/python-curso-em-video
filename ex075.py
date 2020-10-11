n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')))

print(f'Você digitou os números: {n}')

nove = n.count(9)
print(f'O número 9 apareceu: {nove} vezes.')

print('Números pares digitados: ', end='')
par = 0
for c in n:
    if c % 2 == 0:
        par += 1
        print(c, end=', ')

print(f'\nQuantidade de pares digitados: {par}')



if 3 in n:
    print(f'O Número 3 apareceu na posição {n.index(3)+1}.')
else:
    print('O valor 3 não foi digitado')

