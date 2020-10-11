from time import sleep

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = 0

while op != 5:
    print('\n\nEscolha uma opção: \n')

    op = int(input('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa\n'''))
    if op == 1:
        soma = n1 + n2
        print('Soma: {}'.format(soma))
    elif op == 2:
        mult = n1*n2
        print('Multiplicação: {}'.format(mult))
    elif op == 3:
        if n1>n2:
            maior = n1
            print('Maior: {}'.format(maior))
        else:
            maior = n2
            print('Maior: {}'.format(maior))
    elif op == 4:
        print('Informe novamente: ')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))

    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')

sleep(1.5)
print('Fim do programa.')
