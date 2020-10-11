from random import randint
from time import sleep

pc = randint(1,3)
print('~~~~~~~~~~OPÇÕES~~~~~~~~~~\n[1]PEDRA\n[2]PAPEL\n[3]TESOURA\n')
op = int(input('Digite a opção: '))

print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(0.5)
print('')

if op == 1:
    print('Você escolheu PEDRA')
elif op == 2:
    print('Você escolheu PAPEL')
elif op == 3:
    print('Você escolheu TESOURA')
else:
    print('Opção inválida')

if pc == 1:
    print('PC escolheu PEDRA')
elif pc == 2:
    print('PC escolheu PAPEL')
elif pc == 3:
    print('PC escolheu TESOURA')

print('')

if op == pc:
    print("Empate!")
elif pc == 1 and op == 2:
    print('Você venceu!')
elif pc == 1 and op == 3:
    print('PC venceu!')
elif pc == 2 and op == 1:
    print('PC venceu!')
elif pc == 2 and op == 3:
    print('Você venceu!')
elif pc == 3 and op == 1:
    print('Você venceu!')
elif pc == 3 and op == 2:
    print('PC venceu!')
