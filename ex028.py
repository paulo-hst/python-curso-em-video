import random
n = random.randint(0,5)
u = int(input('Digite um número de 0 a 5: '))
if u == n:
    print('Acertou')
else:
    print('Errou !')

print('Número da máquina: {}\nNúmero digitado: {}'.format(n, u))
