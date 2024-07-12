from os import system
system('cls')

paginas = []

sair = 0
print('Digite quantas páginas fez por processo (insira 999 para finalizar):')
while sair != 999:
    sair = int(input(''))
    if sair != 999:
        paginas.append(sair)
processos = len(paginas)

print(paginas)
print(processos)
