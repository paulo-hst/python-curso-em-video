somaidade = 0
mulher = 0
maioridadehomem = 0
nomevelho = ''

for c in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo [M/F]: '.format(c))).strip()

    somaidade = idade + somaidade

    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome

    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade <= 20:
        mulher = mulher + 1

media = somaidade/c

print('\n')
print('Media de idade: {}'.format(media))
print('Mais velho: {}, Idade: {}'.format(nomevelho,maioridadehomem))
print('Mulheres menores de 20 anos: {}'.format(mulher))

