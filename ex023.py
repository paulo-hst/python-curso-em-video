num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 100
c = num // 100 % 100
m = num // 1000 % 1000

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))