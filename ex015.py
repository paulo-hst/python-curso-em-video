#Aluguel de Carros
km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias: '))

pagar = (60*dias + 0.15*km)

print('Valor a pagar: R$ {:.2f}'.format(pagar))