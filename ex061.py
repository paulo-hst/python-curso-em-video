p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
t = p

while c <= 10:
    print('{} > '.format(t), end='')
    t = t + r
    c = c + 1

print('FIM')

