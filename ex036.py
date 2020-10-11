casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário : R$ '))
anos = int(input('Anos para pagar: '))

prest = casa / (anos*12)
porcento = salario*0.3

print('Prestação: R$ {:.2f}'.format(prest))

if prest <= porcento:
    print('Emprestimo APROVADO.')
else:
    print('Emprestimo NEGADO')