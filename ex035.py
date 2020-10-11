a = float(input('\033[4;30;45mDigite o segmento 1: '))
b = float(input('Digite o segmento 2: '))
c = float(input('Digite o segmento 3: '))

if a < b+c and b < a+c and c < a+b:
    print('Triângulo existe.')
else:
    print('Triângulo não existe.')
