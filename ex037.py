# Conversão de bases

n = int(input('Digite um número inteiro: '))

op = int(input('Escolha uma das bases para conversão: \n[1] Binário\n[2] Octal\n[3] hexadecimal \n'))

if op == 1:

    print('Binário: {}'.format(bin(n)[2:]))
elif op == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif op == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção inválida')