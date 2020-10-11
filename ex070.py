print('\nLoja\n')
soma = mil = 0
menor = c = 0
barato = ''

while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Valor do produto: R$ '))
    c += 1

    soma += preço
    if preço > 1000:
        mil += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = produto
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'Soma: R$ {soma:.2f}')
print(f'Menores de R$ 1000,00: {mil}')
print(f'Mais barato: {barato}')
print('FIM')

