s = float(input('Digite o salário: R$ '))

if s <= 1250:
    sn = s + s*0.15
else:
    sn = s + s*0.10

print('Salario antigo: R${:.2f}\nSalário novo: R${:.2f}'.format(s,sn))
