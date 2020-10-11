listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Livro', 34.90,)

print('~'*40)
print('PREÇOS')
print('~'*40)


for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[c]:>7.2f}')
