pesado = 0
leve = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
print('Mais pesado: {}\nMais leve: {}'.format(pesado,leve))