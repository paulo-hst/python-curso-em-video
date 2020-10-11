lista = list()
n = 0
for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    lista.append(n)

maior = max(lista)
menor = min(lista)

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições: {lista.index(maior)}', end='')
print(f'O menor valor digitado foi {menor} ns posições: {lista.index(menor)}', end='')

