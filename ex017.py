#Catetos e Hipotenusa

from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

h = hypot(co,ca)

print('Hipotenusa: {}'.format(h))
