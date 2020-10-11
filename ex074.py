from random import randint

n = (randint(0,10), randint(0,10),
     randint(0,10), randint(0,10), randint(0,10), )

for c in n:
    print(f'{c}', end=' ')

print(f'\nMaior: {max(n)}')
print(f'Maior: {min(n)}')
