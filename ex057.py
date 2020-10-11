sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Caractere {} é inválido. Digite o Sexo [M/F]: '.format(sexo))).strip().upper()[0]
print('Sexo: {}'.format(sexo))


