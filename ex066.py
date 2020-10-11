n = c = s = 0
while True:
    n = int(input('Digite um número inteiro: [999 para parar] '))
    if n == 999:
        break
    c += 1
    s += n

print(f'Números digitados: {c}\nSoma: {s}')

