a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('Maior número: {}\nMenor número: {}'.format(maior, menor))
