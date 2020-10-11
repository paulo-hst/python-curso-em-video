#palíndromo

t = str(input('Digite um texto: ')).strip().upper() # texto digitado
p = t.split() # divide strings em vetor
j = ''.join(p) #junta strings
i = '' # declaração de variável vazia, que será utilizada para inverter

for l in range(len(j)-1, -1, -1): #len: começa o loop do final, inicio (-1), traz pra frente
    i = i + j[l]
print(j,i)

if i == j:
    print('Palíndromo')
else:
    print('Não é palíndromo')


