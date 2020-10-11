times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco da gama', 'Chapecoense',
         'Atlético MG', 'Botafogo', 'Atlético PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético GO')

print(f'Times: {times}')
print(f'G5: {times[:5]}')
print(f'Z4: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'Posição da Chapecoense: {times.index("Chapecoense")+1}º')