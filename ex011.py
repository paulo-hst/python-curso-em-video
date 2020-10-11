l = float(input('Digite a largura da parede (em metros): '))
a = float(input('Digite a altura da parede (em metros): '))

area = (a*l)

print('A área da parede é: {}m²'.format(area))

tinta = area / 2

print('Você irá precisar de {:.0f} litros de tinta.'.format(tinta))