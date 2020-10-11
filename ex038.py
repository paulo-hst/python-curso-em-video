n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O primeiro número ({}) é maior'.format(n1))
elif n2 > n1:
    print('O segundo número ({}) é maior'.format(n2))
else:
    print('Os dois números ({} e {}) são iguais.'.format(n1,n2))

