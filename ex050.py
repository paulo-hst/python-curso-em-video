soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o número inteiro {}: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(soma)
print(cont)

