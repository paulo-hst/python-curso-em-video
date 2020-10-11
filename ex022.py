nome = str(input('Digite o nome: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome)- nome.count(' '))

print(nome.find(' '))
# OU
separa = nome.split()
print(len(separa[0]))