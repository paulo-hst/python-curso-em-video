from random import randint
v = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(0,11)
    resposta = n + pc
    op = ' '

    while op not in 'PI':
        op = str(input('Par ou ímpar ? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {n}\nPC jogou {pc}')

    if op == 'P':
        if resposta % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif op == 'I':
        if resposta % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Jogue novamente')

print(f'Vitórias: {v}')



