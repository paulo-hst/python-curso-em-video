from time import sleep

print('*'*20)
print('Contagem Regressiva!')
print('*'*20)

for c in range(10, -1, -1):
    print('{} !!!'.format(c))
    sleep(1)

