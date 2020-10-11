d = int(input('Digite a distância em Km: '))
print('Distância: {} Km'.format(d))
if d <= 200:
    d = d*0.5
    print('Valor da passagem: R$ {:.2f}'.format(d))
else:
    d = d*0.45
    print('Valor da passagem: R$ {:.2f}'.format(d))