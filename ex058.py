from random import randint
pc = randint(0,10)
cont = 1

pessoa = int(input('Digite um número de 0 à 10: '))

while pessoa > 10:
    pessoa = int(input('{} é invalido, Digite novamente um nº de 0 à 10: '.format(pessoa)))
while pessoa != pc:
    if pessoa > pc:
        pessoa = int(input('Errou ! O número é menor ! Tente novamente: '))
    else:
        pessoa = int(input('Errou ! O número é maior ! Tente novamente: '))
    cont = cont + 1

print('Acertou ! Número digitado: {}'.format(pc))
print('Tentativas: {}'.format(cont))
