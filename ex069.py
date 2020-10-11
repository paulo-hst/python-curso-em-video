dezoito = homens = mulheres = 0

while True:

    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]

    if idade >= 18:
        dezoito += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1

    op = ' '
    while op not in 'SN':
        op = str(input('\nDeseja continuar? [S/N] \n')).upper().strip()[0]
    if op == 'N':
        break

print(f'Maiores de 18: {dezoito}\nHomens: {homens}\nMulheres sub-20 {mulheres}')


