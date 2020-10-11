#seno, cosseno, tangente
import math

a = float(input('Digite o ângulo: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('Seno: {:.2f}, Cosseno: {:.2f}, Tangente: {:.2f}.'.format(s,c,t))