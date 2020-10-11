n = int(input('Digite um número inteiro: '))
t = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')

print('\n\nO número {} foi divisivel {} vezes.'.format(n,t))

if t == 1 or t == 2:
    print('\nÉ primo.'.format(n))
else:
    print('\nNÃO é primo'.format(n))