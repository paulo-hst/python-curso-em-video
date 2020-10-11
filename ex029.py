v = float(input('Velocidade do carro: '))
if v >= 80:
    m = v-80
    m = m*7
    print('Acima do limite de 80Km/h. Você foi multado em R$ {:.2f}'.format(m))
else:
    print(':D')
