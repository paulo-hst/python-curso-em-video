from random import choice

opcoes = ['Corinthians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco da gama', 'Chapecoense',
         'Atletico MG', 'Botafogo', 'Atletico PR', 'Bahia',
         'Sao Paulo', 'Fluminense', 'Sport Recife', 'Vitoria',
         'Coritiba', 'Avai', 'Ponte Preta', 'Atletico GO']

print('~'*34)
print('JOGO DA FORCA - TIMES DE FUTEBOL !')
print('~'*34)


digitados = list()  # lista que armazena letras digitadas
forca = choice(opcoes).upper()  # Escolhe um item da lista
chances = 6  # Chances disponíveis

# preencher variável com _ de acordo com o número de caracteres do time escolhido pelo random.choice
testeForca = list()
for cont in range(0, len(forca)):
    testeForca.append('_')

# loop principal
while True:
    letra = str(input('Digite uma letra: ')).upper()[:1]  # [:] Pega apenas primeira letra

    digitados.append(letra)  # Armazenando itens na lista

    # Troca o _ da lista, adiciona letra digitada e mostra na tela.
    print('Resposta: ', end='')

    for a, b in enumerate(forca):
        if b == letra:
            testeForca[a] = letra

    for c in testeForca:
        # utilizar letra e forca
        print(f'{c}', end=' ')
    print('\n')

    chances -= 1

    print(f'Chances: {chances}')  # Mostra chances restantes

    # Pergunta ao usuário se quer responder o time e finaliza o jogo
    responder = str(input('Quer chutar qual o time?  [S/N]: ').upper().strip()[:1])  # [:1] Pega apenas primeira letra
    if responder == 'S':
        tentativa = str(input('Qual o time? ')).upper()
        if tentativa == forca:
            print('VOCE ACERTOU!')
            break
        else:
            print('ERROU!')
            break

    # Se as chances acabarem, fim de jogo
    if chances == 0:
        print('VOCÊ PERDEU!')
        break

print('~'*12)
print('FIM DE JOGO')
print('~'*12)

print(f'Letras digitadas: {digitados}')
print(f'Time: {forca}')
