n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print('Média: {:.1f}'.format(media))

if media < 5:
    print('Reprovado')
elif 6.9 > media >= 5:
    print('Recuperação')
else:
    print('Aprovado')