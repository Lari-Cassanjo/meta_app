from os import system
system('cls')

paginas = []
total_paginas = 0

sair = 0
print('Digite quantas páginas fez por processo (insira 999 para finalizar):')
while sair != 999:
    sair = int(input(''))
    if sair != 999:
        total_paginas += sair
        paginas.append(sair)
processos = len(paginas)
media_dia = round(total_paginas / processos)

print(f'Lista de páginas: {paginas}')
print(f'Total de processos: {processos}')
print(f'Total de páginas: {total_paginas}')
print(f'Média de páginas por processo: {media_dia}')

if total_paginas >= 3000 or processos >= 160:
    if total_paginas >= 3000:
        print(f'\33[32mMeta de páginas batida com {total_paginas} páginas!\33[m')
    if processos >= 160:
        print(f'\33[32mMeta de processos batida com {processos} processos!\33[m')
else:
    print('\33[31mNenhuma meta foi alcaçada hoje.\33[m')
    print(f'Faltaram \33[31m{3000 - total_paginas}\33[m páginas ou \33[31m{160 - processos}\33[m processos.')
