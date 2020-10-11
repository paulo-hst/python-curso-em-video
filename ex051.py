t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10-1)*r
for c in range(t,d+r,r):
    print('{}'.format(c), end=' > ')
print('FIM')