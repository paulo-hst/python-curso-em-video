from datetime import date

ano = date.today().year
totalmenor = 0
totalmaior = 0

for c in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1

print('Maior de idade: {}\nMenor de idade: {}'.format(totalmaior, totalmenor))