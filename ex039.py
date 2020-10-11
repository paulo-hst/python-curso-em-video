from datetime import date

nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual-nascimento

if idade < 18:
    tempo = 18-idade
    print('Idade: {}; Ainda faltam {} anos para o alistamento.'.format(idade,tempo))
    print('Seu alistamento será em {}.'.format(anoAtual+tempo))
elif idade == 18:
    print('Idade: {}; Aliste-se agora.'.format(idade))
else:
    tempo = idade-18
    print('Idade: {}; Passaram {} anos do alistamento.'.format(idade,tempo))
    print('Seu alistamento foi em {}'.format(anoAtual-tempo))

