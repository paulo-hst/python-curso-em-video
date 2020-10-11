p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
t = p
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print('{} > '.format(t), end='')
        t = t + r
        c = c + 1

    print('PAUSA')

    mais = int(input('Quantos termos a mais? '))
print('Termos mostrados: {}'.format(total))