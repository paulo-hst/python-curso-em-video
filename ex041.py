from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year

idade = atual-nasc

if idade <= 9:
    print('Idade: {}. Categoria: Mirim'.format(idade))
elif 9 < idade <= 14:
    print('Idade: {}. Categoria: Infantil'.format(idade))
elif 14 < idade <= 19:
    print('Idade: {}. Categoria: Junior'.format(idade))
elif 19 < idade <= 25:
    print('Idade: {}. Categoria: Sênior'.format(idade))
else:
    print('Idade: {}. Categoria: Master'.format(idade))

