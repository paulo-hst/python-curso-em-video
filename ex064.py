n = c = s = 0
n = int(input('Digite um número inteiro: [999 para parar] '))

while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número inteiro: [999 para parar] '))

print('Números digitados: {}'.format(c))
print('Soma: {}'.format(s))

