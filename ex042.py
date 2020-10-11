a = float(input('Digite o segmento 1: '))
b = float(input('Digite o segmento 2: '))
c = float(input('Digite o segmento 3: '))

if a < b+c and b < a+c and c < a+b:
    print('Triângulo existe.')

    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    elif a != b and a != c and b != c:
        print('ESCALENO')

else:
    print('Triângulo não existe.')


