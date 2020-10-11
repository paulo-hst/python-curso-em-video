valor = float(input('Valor do produto: R$ '))
op = int(input('Digite a opção\n[1] à vista no dinheiro/cheque\n[2] à vista no cartão\n[3] em até 2x no cartão\n[4] 3x ou mais no cartão.\n'))

print('Valor do produto R$ {:.2f}.'.format(valor))

if op == 1:
    novo = valor - (valor*0.1)
    print('Valor com desconto R$ {:.2f}'.format(novo))
elif op == 2:
    novo = valor - (valor*0.05)
    print('Valor com desconto R$ {:.2f}'.format(novo))
elif op == 3:
    print('Valor da parcela R$ {:.2f}'.format(valor/2))
elif op == 4:
    parcela = int(input('Digite o número de parcelas (3 a 5 vezes): '))
    if parcela > 5:
        print('Parcela indisponível')
    else:
        novo = valor + (valor*0.2)
        print('Valor com juros: R$ {:.2f}\nValor da parcela: R$ {:.2f}\nParcelado em {} vezes'.format(novo, novo/parcela, parcela))