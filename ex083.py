exp = list()
exp = str(input('Digite a expressão: '))

ap = exp.count('(')
fc = exp.count(')')

if ap == fc:
    print('Expressão válida.')
else:
    print('Expressão inválida')

print(f'Expressão: {exp}')
