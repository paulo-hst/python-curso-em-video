r = 'S'
c = soma = maior = menor = media = 0

while r in 'Ss':
    n = int(input('Digite um número inteiro: '))
    soma += n
    c += 1

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    r = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]

media = soma/c
print('Números digitados: {}'.format(c))
print('Media: {:.1f}'.format(media))
print('Maior: {}/ Menor :{}'.format(maior, menor))
