nome = str(input('Digite o nome: ')).strip().title()

div = nome.split()

print('Primeiro nome: {}'.format(div[0]))
print('Último nome: {}'.format(div[len(div) - 1]))