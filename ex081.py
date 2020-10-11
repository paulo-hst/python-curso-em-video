lista = list()

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    op = str(input('Deseja continuar? [S/N] ')).upper()[:1]
    if op in 'N':
        break

lista.sort(reverse=True)  # inverte lista
teste5 = 0

'''
for a, b in enumerate(lista):
    if b == 5: n
        teste5 = 1
'''
print('~.'*50)
print(f'Você digitou {len(lista)} valores.')
print(f'Ordem inversa: {lista}')
if 5 not in lista:
    print(f'5 Não foi encontrado na lista !')
else:
    print(f'O valor 5 foi encontrado na lista')
