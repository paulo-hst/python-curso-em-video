lista = ['Telefonou para a vítima? ',
         'Esteve no local do crime? ',
         'Mora perto da vítima? ',
         'Devia para a vítima? ',
         'Já trabalhou com a vítima? ']

status = ['Suspeito', 'Cúmplice', 'Assassino', 'Inocente']

respostaSim = 0
for c in range(0, len(lista)):
    op = str(input(lista[c]).strip().lower())
    if op == 's':
        respostaSim += 1

if 1 < respostaSim <= 2:
    print(f'Resultado: {status[0]}')
elif 2 < respostaSim <= 4:
    print(f'Resultado: {status[1]}')
elif respostaSim == 5:
    print(f'Resuldado: {status[2].upper()}')
else:
    print(f'Resultado: {status[3]}')


